# create_db.py
import sqlite3

conn = sqlite3.connect('plants.db')
cursor = conn.cursor()

# Create table for identified plants
cursor.execute('''
CREATE TABLE IF NOT EXISTS plants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    image_path TEXT
)
''')

# Create table for care data (you'll populate this manually)
cursor.execute('''
CREATE TABLE IF NOT EXISTS care_data (
    name TEXT PRIMARY KEY,
    watering_freq_days INTEGER,
    sunlight TEXT,
    soil TEXT
)
''')

# Create table for generated tasks
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plant_id INTEGER,
    plant TEXT,
    task_type TEXT,
    frequency_days INTEGER,
    last_done DATE,
    FOREIGN KEY(plant) REFERENCES plants(name)
)
''')


# cursor.execute('''
#     CREATE TABLE care_data (
#         sc_name TEXT PRIMARY KEY,
#         name TEXT,
#         watering_freq_days INTEGER,
#         sunlight TEXT,
#         soil TEXT
#     )
# ''')

# # Sample care data for plants (you can add more as needed)
# plants_data = [
#     ("Ficus lyrata", "Fiddle Leaf Fig", 7, "Bright indirect light", "Well-draining soil"),
# ("Aloe vera", "Aloe Vera", 14, "Full sun", "Sandy, well-drained soil"),
# ("Opuntia spp.", "Prickly Pear Cactus", 30, "Full sun", "Well-draining, dry soil"),
# ("Sansevieria trifasciata", "Snake Plant", 21, "Low to bright light", "Well-draining soil"),
# ("Chlorophytum comosum", "Spider Plant", 7, "Indirect light", "Loamy soil"),
# ("Epipremnum aureum", "Golden Pothos", 7, "Low to bright indirect light", "Well-draining soil"),
# ("Zamioculcas zamiifolia", "ZZ Plant", 14, "Low to bright indirect light", "Well-draining soil"),
# ("Spathiphyllum spp.", "Peace Lily", 7, "Low to medium light", "Moist, well-draining soil"),
# ("Dracaena marginata", "Dragon Tree", 10, "Bright indirect light", "Well-draining soil"),
# ("Monstera deliciosa", "Swiss Cheese Plant", 7, "Bright indirect light", "Peat-based soil"),
# ("Philodendron hederaceum", "Heartleaf Philodendron", 7, "Medium to bright indirect light", "Well-draining soil"),
# ("Calathea orbifolia", "Prayer Plant", 7, "Low to medium light", "Moist, well-draining soil"),
# ("Peperomia obtusifolia", "Baby Rubber Plant", 10, "Bright indirect light", "Well-draining soil"),
# ("Hedera helix", "English Ivy", 7, "Bright indirect light", "Moist, well-draining soil"),
# ("Maranta leuconeura", "Red Prayer Plant", 7, "Low to medium light", "Moist, well-draining soil"),
# ("Begonia rex", "Rex Begonia", 7, "Bright indirect light", "Well-draining soil"),
# ("Tradescantia zebrina", "Wandering Jew", 7, "Bright indirect light", "Well-draining soil"),
# ("Fittonia albivenis", "Nerve Plant", 5, "Low to medium light", "Moist, well-draining soil"),
# ("Asplenium nidus", "Bird's Nest Fern", 7, "Medium to bright indirect light", "Moist, well-draining soil"),
# ("Nephrolepis exaltata", "Boston Fern", 5, "Bright indirect light", "Moist, well-draining soil"),
# ("Codiaeum variegatum", "Croton", 7, "Bright indirect light", "Well-draining soil"),
# ("Aglaonema commutatum", "Chinese Evergreen", 7, "Low to medium light", "Well-draining soil"),
# ("Anthurium andraeanum", "Flamingo Flower", 7, "Bright indirect light", "Well-draining soil"),
# ("Hoya carnosa", "Wax Plant", 10, "Bright indirect light", "Well-draining soil"),
# ("Pilea peperomioides", "Chinese Money Plant", 7, "Bright indirect light", "Well-draining soil"),
# ("Ficus elastica", "Rubber Plant", 7, "Bright indirect light", "Well-draining soil"),
# ("Schefflera arboricola", "Umbrella Tree", 7, "Bright indirect light", "Well-draining soil"),
# ("Chamaedorea elegans", "Parlor Palm", 7, "Low to medium light", "Well-draining soil"),
# ("Beaucarnea recurvata", "Ponytail Palm", 14, "Bright indirect light", "Well-draining soil"),
# ("Crassula ovata", "Jade Plant", 14, "Full sun", "Well-draining soil"),
# ("Kalanchoe blossfeldiana", "Flaming Katy", 14, "Bright indirect light", "Well-draining soil"),
# ("Alocasia amazonica", "Elephant's Ear", 7, "Bright indirect light", "Moist, well-draining soil"),
# ("Syngonium podophyllum", "Arrowhead Plant", 7, "Medium to bright indirect light", "Well-draining soil"),
# ("Cissus rhombifolia", "Grape Ivy", 7, "Bright indirect light", "Well-draining soil"),
# ("Cordyline fruticosa", "Ti Plant", 7, "Bright indirect light", "Well-draining soil"),
# ("Dieffenbachia seguine", "Dumb Cane", 7, "Medium to bright indirect light", "Well-draining soil"),
# ("Ficus benjamina", "Weeping Fig", 7, "Bright indirect light", "Well-draining soil"),
# ("Gynura aurantiaca", "Purple Passion", 7, "Bright indirect light", "Well-draining soil"),
# ("Soleirolia soleirolii", "Baby's Tears", 5, "Bright indirect light", "Moist, well-draining soil"),
# ("Tolmiea menziesii", "Piggyback Plant", 7, "Bright indirect light", "Moist, well-draining soil"),
# ("Platycerium bifurcatum", "Staghorn Fern", 7, "Bright indirect light", "Moist, well-draining soil"),
# ("Araucaria heterophylla", "Norfolk Island Pine", 7, "Bright indirect light", "Well-draining soil"),
# ("Caladium bicolor", "Caladium", 7, "Bright indirect light", "Moist, well-draining soil"),
# ("Plectranthus verticillatus", "Swedish Ivy", 7, "Bright indirect light", "Well-draining soil"),
# ("Fatsia japonica", "Japanese Aralia", 7, "Bright indirect light", "Well-draining soil"),
# ("Stromanthe sanguinea", "Tricolor Prayer Plant", 7, "Bright indirect light", "Moist, well-draining soil"),
# ("Hypoestes phyllostachya", "Polka Dot Plant", 7, "Bright indirect light", "Moist, well-draining soil"),
# ("Philodendron bipinnatifidum", "Split-Leaf Philodendron", 7, "Bright indirect light", "Well-draining soil"),
# ("Ceropegia woodii", "String of Hearts", 10, "Bright indirect light", "Well-draining soil"),
# ("Scindapsus pictus", "Satin Pothos", 7, "Bright indirect light", "Well-draining soil"),
# ("Calathea lancifolia", "Rattlesnake Plant", 7, "Low to medium light", "Moist, well-draining soil"),
# ("Calathea ornata", "Pinstripe Plant", 7, "Low to medium light", "Moist, well-draining soil"),
# ("Calathea roseopicta", "Rose Painted Calathea", 7, "Low to medium light", "Moist, well-draining soil"),
# ("Calathea makoyana", "Peacock Plant", 7, "Low to medium light", "Moist, well-draining soil"),
# ("Calathea majestica", "White Star Calathea", 7, "Low to medium light", "Moist, well-draining soil"),
# ("Pilea cadierei", "Aluminum Plant", 7, "Bright indirect light", "Well-draining soil"),
# ("Aspidistra elatior", "Cast Iron Plant", 10, "Low to medium light", "Well-draining soil"),
# ("Dracaena fragrans", "Corn Plant", 7, "Bright indirect light", "Well-draining soil"),
# ("Dracaena reflexa", "Song of India", 7, "Bright indirect light", "Well-draining soil"),
# ("Dracaena deremensis", "Janet Craig", 7, "Bright indirect light", "Well-draining soil"),
# ("Dracaena sanderiana", "Lucky Bamboo", 7, "Low to medium light", "Well-draining soil"),
# ("Dracaena compacta", "Compact Dracaena", 7, "Bright indirect light", "Well-draining soil"),
# ("Dracaena surculosa", "Gold Dust Dracaena", 7, "Bright indirect light", "Well-draining soil"),
# ("Dracaena warneckii", "Striped Dracaena", 7, "Bright indirect light", "Well-draining soil"),
# ("Dracaena goldieana", "Goldieana Dracaena", 7, "Bright indirect light", "Well-draining soil"),
# ("Dracaena godseffiana", "Godseffiana Dracaena", 7, "Bright indirect light", "Well-draining soil"),
# ("Dracaena hookeriana", "Hooker's Dracaena", 7, "Bright indirect light", "Well-draining soil"),
# ("Dracaena 'Janet Craig'", "Janet Craig Dracaena", 7, "Bright indirect light", "Well-draining soil"),
# ("Dracaena 'Lemon Lime'", "Lemon Lime Dracaena", 7, "Bright indirect light", "Well-draining soil"),
# ("Dracaena massangeana", "Mass Cane", 7, "Bright indirect light", "Well-draining soil"),
# ("Dracaena steudneri", "Steudner's Dracaena", 7, "Bright indirect light", "Well-draining soil"),
# ("Dracaena trifasciata", "Snake Plant", 7, "Bright indirect light", "Well-draining soil"),
# ("Dracaena umbraculifera", "Umbrella Dracaena", 7, "Bright indirect light", "Well-draining soil"),
# ("Dracaena zeylanica", "Ceylon Dracaena", 7, "Bright indirect light", "Well-draining soil"),
# ("Dracaena deremensis 'Lemon Lime'", "Lemon Lime Dracaena", 7, "Bright indirect light", "Well-draining soil"),
# ]

# # # Insert sample data into care_data table
# cursor.executemany('''
#     INSERT OR REPLACE INTO care_data (sc_name, name, watering_freq_days, sunlight, soil)
#     VALUES (?, ?, ?, ?, ?)
# ''', plants_data)

# cursor.execute('drop table tasks')
# cursor.execute("drop table tasks_new")

conn.commit()
conn.close()
print("Database and tables created.")
