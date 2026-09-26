from flask import Flask, request, jsonify
from database import get_db, init_db

app = Flask(__name__)

init_db()

@app.route("/pokemon", methods=["GET"])
def get_pokemon():
    conn = get_db()
    pokemon = conn.execute("SELECT * FROM pokemon").fetchall()
    conn.close()

    return jsonify([dict(p) for p in pokemon]), 200


@app.route("/pokemon/<int:pokemon_id>", methods=["GET"])
def get_one_pokemon(pokemon_id):
    conn = get_db()
    pokemon = conn.execute(
        "SELECT * FROM pokemon WHERE id = ?",
        (pokemon_id,)
    ).fetchone()
    conn.close()

    if pokemon is None:
        return jsonify({"error": "Pokemon not found"}), 404

    return jsonify(dict(pokemon)), 200


@app.route("/pokemon", methods=["POST"])
def create_pokemon():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    required_fields = ["name", "type", "level", "hp"]

    for field in required_fields:
        if field not in data or data[field] == "":
            return jsonify({"error": f"{field} is required"}), 400

    conn = get_db()

    cursor = conn.execute(
        """
        INSERT INTO pokemon (name, type, level, hp)
        VALUES (?, ?, ?, ?)
        """,
        (data["name"], data["type"], data["level"], data["hp"])
    )

    conn.commit()

    pokemon_id = cursor.lastrowid

    pokemon = conn.execute(
        "SELECT * FROM pokemon WHERE id = ?",
        (pokemon_id,)
    ).fetchone()

    conn.close()

    return jsonify(dict(pokemon)), 201


@app.route("/pokemon/<int:pokemon_id>", methods=["PUT"])
def update_pokemon(pokemon_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    required_fields = ["name", "type", "level", "hp"]

    for field in required_fields:
        if field not in data or data[field] == "":
            return jsonify({"error": f"{field} is required"}), 400

    conn = get_db()

    pokemon = conn.execute(
        "SELECT * FROM pokemon WHERE id = ?",
        (pokemon_id,)
    ).fetchone()

    if pokemon is None:
        conn.close()
        return jsonify({"error": "Pokemon not found"}), 404

    conn.execute(
        """
        UPDATE pokemon
        SET name = ?, type = ?, level = ?, hp = ?
        WHERE id = ?
        """,
        (
            data["name"],
            data["type"],
            data["level"],
            data["hp"],
            pokemon_id
        )
    )

    conn.commit()

    updated = conn.execute(
        "SELECT * FROM pokemon WHERE id = ?",
        (pokemon_id,)
    ).fetchone()

    conn.close()

    return jsonify(dict(updated)), 200


@app.route("/pokemon/<int:pokemon_id>", methods=["DELETE"])
def delete_pokemon(pokemon_id):
    conn = get_db()

    pokemon = conn.execute(
        "SELECT * FROM pokemon WHERE id = ?",
        (pokemon_id,)
    ).fetchone()

    if pokemon is None:
        conn.close()
        return jsonify({"error": "Pokemon not found"}), 404

    conn.execute(
        "DELETE FROM pokemon WHERE id = ?",
        (pokemon_id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Pokemon deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)