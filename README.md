# Macasero Pokemon API

A REST API and frontend application for managing Pokemon records. The backend uses Flask and SQLite, while the frontend uses HTML, CSS, and JavaScript with the Fetch API.

## Features

* View all Pokemon
* View a single Pokemon
* Add a Pokemon
* Edit a Pokemon
* Delete a Pokemon
* Add Pokemon image URLs
* Display Pokemon images
* API validation error handling
* 404 error handling
* Loading state

## Technologies Used

* Python
* Flask
* Flask-CORS
* SQLite
* HTML
* CSS
* JavaScript
* Fetch API

## Project Structure

```text
Macasero_PokemonAPI/
├── app.py
├── database.py
├── requirements.txt
├── pokemon.db
├── README.md
├── screenshots/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
└── venv/
```

## How to Run the Backend

Open a terminal in the project folder:

```powershell
cd C:\Users\XU\Documents\Macasero_PokemonAPI
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Start the Flask API:

```powershell
python app.py
```

The backend will run at:

```text
http://127.0.0.1:5000
```

## How to Run the Frontend

Open a second terminal and go to the frontend folder:

```powershell
cd C:\Users\XU\Documents\Macasero_PokemonAPI\frontend
```

Start the frontend server:

```powershell
py -m http.server 5500
```

Open the application in a browser:

```text
http://127.0.0.1:5500/
```

Keep both the backend and frontend terminals running while using the application.

## API Endpoints

| Method | Endpoint        | Description      |
| ------ | --------------- | ---------------- |
| GET    | `/pokemon`      | Get all Pokemon  |
| GET    | `/pokemon/<id>` | Get one Pokemon  |
| POST   | `/pokemon`      | Add a Pokemon    |
| PUT    | `/pokemon/<id>` | Update a Pokemon |
| DELETE | `/pokemon/<id>` | Delete a Pokemon |

## Frontend

The frontend communicates with the Flask API using JavaScript Fetch API requests.

The application provides forms and buttons for viewing, adding, editing, and deleting Pokemon records. Each Pokemon can also have an image URL that is displayed in the list and details section.

## Validation and Error Handling

The frontend displays validation messages returned by the API when a request has a `400` status.

A `404` response is handled with a user-friendly "Pokemon not found" message.

A loading message is displayed while Pokemon data is being retrieved from the API.

## Repository

GitHub repository:

https://github.com/DenzGodwenMacasero/Macasero_PokemonAPI
