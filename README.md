# Technical Test - UF Microservice

This project consists of a microservice developed with Django and the Django REST Framework that allows you to query the historical value of the Unidad de Fomento (UF) in Chilean pesos for a specific date.

---

## Technologies used

- Python 3.12
- Django 5.2.1
- Django REST Framework
- SQLite3
- Requests (to consume external API)

---

## Project structure

- `technical_test/` - Django project
- `uf/` - Main app with UF microservice logic
- `requirements.txt` - Enviroment dependencies
- `db.sqlite3` - Local database

---

## Functionality

### Available Endpoints:

- `GET /`  
  Welcome page with general information about the microservice.

- `GET /uf/list`  
  Returns a list of all historical UF values ​​stored in the database.

- `GET /uf/price?value=XXXX&date=yyyymmdd`  
  Calculates and returns the equivalent in Chilean pesos for an amount in UF on the indicated date.  
  Example:  
  `/uf/price?value=10&date=20250520`

---

## Data model

The `UF` model contains information about the  Unidad de Fomento:

| Field  | Type   | Description                            |
|--------|--------|----------------------------------------|
| date   | Date   | Date of the UF value                   |
| value  | Float  | Value in Chilean pesos of the UF       |

---

## Data loading process

The data is obtained from the public API  [mindicador.cl](https://mindicador.cl/api/uf) and is stored in the SQLite database using a function that can be executed from the terminal or when starting the project if you want to automate it.

---

## Installation and Execution

```bash
# Clone the repository
git clone https://github.com/your_user/technical_test.git
cd technical_test

# Create and activate virtual environment
python -m venv .venv

# Install dependencies
pip install -r requirements.txt

# Perform migrations
python manage.py migrate

# Run the server
python manage.py runserver


# Created URLs
The URLs needed to access the views when running on the server are:
- http://127.0.0.1:8000/ 
- http://127.0.0.1:8000/uf/list?format=api
- http://127.0.0.1:8000/uf/price?value=10$date=20250520 (Enter the date you prefer)

