import sqlite3

DATABASE = "pokemon.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            level INTEGER NOT NULL,
            hp INTEGER NOT NULL
        )
    """)

    count = conn.execute("SELECT COUNT(*) FROM pokemon").fetchone()[0]

    if count == 0:
        pokemon = [
            ("Bulbasaur", "Grass/Poison", 16, 45),
            ("Charmander", "Fire", 14, 39),
            ("Squirtle", "Water", 15, 44),
            ("Pikachu", "Electric", 18, 35),
            ("Jigglypuff", "Fairy", 12, 115),
            ("Meowth", "Normal", 17, 40),
            ("Psyduck", "Water", 13, 50),
            ("Growlithe", "Fire", 20, 55),
            ("Gastly", "Ghost/Poison", 19, 30),
            ("Eevee", "Normal", 18, 55),
            ("Dratini", "Dragon", 21, 41),
            ("Snorlax", "Normal", 25, 160),
            ("Mewtwo", "Psychic", 70, 106),
            ("Gengar", "Ghost/Poison", 45, 60),
            ("Lucario", "Fighting/Steel", 35, 70)
        ]

        conn.executemany(
            "INSERT INTO pokemon (name, type, level, hp) VALUES (?, ?, ?, ?)",
            pokemon
        )

    conn.commit()
    conn.close()