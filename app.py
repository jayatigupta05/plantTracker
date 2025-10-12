from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime
import requests
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

PLANTNET_API_KEY = os.getenv("PLANTNET_API_KEY")
PLANTNET_PROJECT = os.getenv("PLANTNET_PROJECT")


app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'plant_image' not in request.files:
            return 'No file uploaded'

        image_file = request.files['plant_image']
        # print("Uploaded file:", image_file.filename)  # DEBUG

        if image_file.filename == '':
            return 'No file selected'

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
        print("Saving to:", filepath)  # DEBUG
        image_file.save(filepath)

        # Send image to PlantNet API
        with open(filepath, 'rb') as img:
            response = requests.post(
                f"https://my-api.plantnet.org/v2/identify/{PLANTNET_PROJECT}?api-key={PLANTNET_API_KEY}",
                files={'images': img},
                data={'organs': ['leaf']}  # You can try changing this to ['leaf', 'flower', 'fruit', 'bark']
            )

        print("Response status:", response.status_code)  # DEBUG
        print("Response content:", response.text[:500])  # DEBUG: limit to 500 chars

        data = response.json()

        if 'results' not in data or not data['results']:
            return 'No plant identified'

        # Get top result
        top_result = data['results'][0]
        plant_name = top_result['species']['scientificNameWithoutAuthor']
        # print("Identified plant:", plant_name)  # DEBUG

        # Store plant info in the database
        conn = sqlite3.connect('plants.db')
        cursor = conn.cursor()

        # Get plant care data from care_data table
        cursor.execute("SELECT * FROM care_data WHERE sc_name = ?", (plant_name,))
        care_info = cursor.fetchone()

        # if not care_info:
        #     print("No care data found for:", plant_name)  # DEBUG

        if care_info:
            sc_name = care_info[0]
            common_name = care_info[1]
            watering_freq = care_info[2]
            sunlight = care_info[3]
            soil = care_info[4]

            cursor.execute("INSERT INTO plants (species, name, watering_frequency, sunlight, soil) VALUES (?, ?, ?, ?, ?)", 
                           (sc_name, common_name, watering_freq, sunlight, soil))
            plant_id = cursor.lastrowid

            cursor.execute("INSERT INTO tasks (plant_id, plant, task_type, frequency_days) VALUES (?, ?, ?, ?)",
                        (plant_id, common_name, 'water', watering_freq))

            cursor.execute("INSERT INTO tasks (plant_id, plant, task_type, frequency_days) VALUES (?, ?, ?, ?)",
                        (plant_id, common_name, 'sunlight', 1))

            cursor.execute("INSERT INTO tasks (plant_id, plant, task_type, frequency_days) VALUES (?, ?, ?, ?)",
                        (plant_id, common_name, 'soil', 7))

            conn.commit()

        conn.close()

        return redirect('/plants')

    return render_template('index.html')

@app.route('/plants')
def plants():
    conn = sqlite3.connect('plants.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM plants")
    plants = cursor.fetchall()
    conn.close()
    return render_template('plants.html', plants=plants)


@app.route('/tasks')
def show_tasks():
    conn = sqlite3.connect('plants.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    today = datetime.today()

    # Get all tasks
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    # Update due_in_days dynamically
    updated_tasks = []
    for task in tasks:
        last_done = task['last_done']
        freq = task['frequency_days']

        if last_done:
            last_date = datetime.strptime(last_done, "%Y-%m-%d")
            days_passed = (today - last_date).days
            due_in = freq - days_passed
        else:
            # Never done; due now
            due_in = 0

        updated_tasks.append({**dict(task), 'due_in_days': due_in})

    conn.close()

    # Show only tasks due today or earlier
    due_tasks = [t for t in updated_tasks if t['due_in_days'] <= 0]

    return render_template('tasks.html', tasks=due_tasks)



@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    conn = sqlite3.connect('plants.db')
    cursor = conn.cursor()

    completed_at = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("UPDATE tasks SET last_done = ? WHERE id = ?", (completed_at, task_id))

    conn.commit()
    conn.close()

    return redirect(url_for('show_tasks'))



if __name__ == "__main__":

    app.run(debug=True)
