# Macasero Pokemon API

A REST API for managing Pokemon records using Flask and SQLite.

## Features

- GET all Pokemon
- GET one Pokemon
- POST a new Pokemon
- PUT update a Pokemon
- DELETE a Pokemon
- Basic validation
- SQLite database

## Technologies

- Python
- Flask
- SQLite
- Postman

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /pokemon | Get all Pokemon |
| GET | /pokemon/<id> | Get one Pokemon |
| POST | /pokemon | Create a Pokemon |
| PUT | /pokemon/<id> | Update a Pokemon |
| DELETE | /pokemon/<id> | Delete a Pokemon |

## Status Codes

- 200 OK - Successful GET, PUT, or DELETE
- 201 Created - Pokemon successfully created
- 400 Bad Request - Missing required field or request body
- 404 Not Found - Pokemon does not exist

## How to Run

```bash
python app.py