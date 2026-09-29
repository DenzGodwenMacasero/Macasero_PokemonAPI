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
            hp INTEGER NOT NULL,
            image_url TEXT
        )
    """)

    columns = conn.execute("PRAGMA table_info(pokemon)").fetchall()
    column_names = [column["name"] for column in columns]

    if "image_url" not in column_names:
        conn.execute("ALTER TABLE pokemon ADD COLUMN image_url TEXT")

    existing_pokemon = conn.execute("SELECT name FROM pokemon").fetchall()
    existing_names = {pokemon["name"] for pokemon in existing_pokemon}

    starter_pokemon = [
        ("Bulbasaur", "Grass/Poison", 16, 45, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/1.gif"),
        ("Charmander", "Fire", 14, 39, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/4.gif"),
        ("Squirtle", "Water", 15, 44, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/7.gif"),
        ("Pikachu", "Electric", 18, 35, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/25.gif"),
        ("Jigglypuff", "Fairy", 12, 115, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/39.gif"),
        ("Meowth", "Normal", 17, 40, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/52.gif"),
        ("Psyduck", "Water", 13, 50, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/54.gif"),
        ("Growlithe", "Fire", 20, 55, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/58.gif"),
        ("Gastly", "Ghost/Poison", 19, 30, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/92.gif"),
        ("Eevee", "Normal", 18, 55, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/133.gif"),
        ("Dratini", "Dragon", 21, 41, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/147.gif"),
        ("Snorlax", "Normal", 25, 160, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/143.gif"),
        ("Mewtwo", "Psychic", 70, 106, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/150.gif"),
        ("Gengar", "Ghost/Poison", 45, 60, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/94.gif"),
        ("Lucario", "Fighting/Steel", 35, 70, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/448.gif")
    ]

    for pokemon in starter_pokemon:
        if pokemon[0] not in existing_names:
            conn.execute(
                """
                INSERT INTO pokemon (name, type, level, hp, image_url)
                VALUES (?, ?, ?, ?, ?)
                """,
                pokemon
            )

    strong_pokemon = [
        ("Arceus", "Normal", 100, 120, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/493.gif"),
        ("Mega Rayquaza", "Dragon/Flying", 100, 105, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/10001.gif"),
        ("Eternatus", "Poison/Dragon", 100, 140, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/890.png"),
        ("Zacian", "Fairy/Steel", 100, 92, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/888.png"),
        ("Zamazenta", "Fighting/Steel", 100, 92, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/889.png"),
        ("Kyogre", "Water", 90, 100, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/382.png"),
        ("Groudon", "Ground", 90, 100, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/383.png"),
        ("Necrozma", "Psychic", 90, 97, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/800.png"),
        ("Miraidon", "Electric/Dragon", 100, 100, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1008.png"),
        ("Koraidon", "Fighting/Dragon", 100, 100, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1007.png")
    ]

    for pokemon in strong_pokemon:
        if pokemon[0] not in existing_names:
            conn.execute(
                """
                INSERT INTO pokemon (name, type, level, hp, image_url)
                VALUES (?, ?, ?, ?, ?)
                """,
                pokemon
            )

    conn.execute("""
        UPDATE pokemon
        SET image_url = CASE name
            WHEN 'Bulbasaur' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/1.gif'
            WHEN 'Charmander' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/4.gif'
            WHEN 'Squirtle' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/7.gif'
            WHEN 'Pikachu' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/25.gif'
            WHEN 'Jigglypuff' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/39.gif'
            WHEN 'Meowth' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/52.gif'
            WHEN 'Psyduck' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/54.gif'
            WHEN 'Growlithe' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/58.gif'
            WHEN 'Gastly' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/92.gif'
            WHEN 'Eevee' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/133.gif'
            WHEN 'Dratini' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/147.gif'
            WHEN 'Snorlax' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/143.gif'
            WHEN 'Mewtwo' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/150.gif'
            WHEN 'Gengar' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/94.gif'
            WHEN 'Lucario' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/448.gif'
            WHEN 'Arceus' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/493.gif'
            WHEN 'Mega Rayquaza' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/10001.gif'
            WHEN 'Eternatus' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/890.png'
            WHEN 'Zacian' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/888.png'
            WHEN 'Zamazenta' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/889.png'
            WHEN 'Kyogre' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/382.png'
            WHEN 'Groudon' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/383.png'
            WHEN 'Necrozma' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/800.png'
            WHEN 'Miraidon' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1008.png'
            WHEN 'Koraidon' THEN 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1007.png'
            ELSE image_url
        END
    """)

    conn.commit()
    conn.close()