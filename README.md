# 🌱 Plant Tracker

A simple web application to track, manage, and care for your plants.  
Built with **Flask**, **SQLite**, and a lightweight UI using **HTML/CSS**.

---

## 🚀 Features

- Add, update, and delete plants in your collection  
- Store details like plant name, species, and care notes  
- SQLite database for persistent storage  
- Responsive, minimal web UI  
- Sample data included for quick testing

---

## 🛠️ Tech Stack

- **Backend:** Python (Flask)  
- **Database:** SQLite  
- **Frontend:** HTML, CSS

---

## 📂 Project Structure

```
plantTracker/
├─ app.py              # Main Flask application
├─ init_db.py          # Initialize the database
├─ check_schema.py     # Validate/inspect DB schema
├─ requirements.txt    # Python dependencies
├─ templates/          # Jinja2 HTML templates
├─ static/             # CSS and other static assets
├─ samples/            # Example/sample data
└─ README.md           # Project documentation
```

---

## ⚡ Getting Started

### 1) Clone the repository
```bash
git clone https://github.com/jayatigupta05/plantTracker.git
cd plantTracker
```

### 2) Create & activate a virtual environment (recommended)
**macOS/Linux**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows (PowerShell)**
```bash
python -m venv venv
.env\Scripts\Activate.ps1
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Initialize the database
```bash
python init_db.py
```

### 5) Run the application
```bash
python app.py
```
Then open your browser at: http://127.0.0.1:5000/

> Alternatively (if configured), you can run with Flask CLI:
> ```bash
> set FLASK_APP=app.py && flask run   # Windows
> export FLASK_APP=app.py && flask run # macOS/Linux
> ```

---

## 🧪 Sample Data

Check the `samples/` directory for example inputs to quickly try the app.

---

## 🤝 Contributing

1. Fork the repository  
2. Create a feature branch: `git checkout -b feature/your-feature`  
3. Commit your changes: `git commit -m "Add your message"`  
4. Push to the branch: `git push origin feature/your-feature`  
5. Open a Pull Request
