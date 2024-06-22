# Bolivia Moveis Project

This is a Flask application for the online shop called bolivia moveis

## Requirements

- Python 3.8 or higher
- pip (Python package installer)
- Virtualenv (optional but recommended)

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/GuilhermeFiorot/boliviamoveisbackend.git
cd boliviamoveisbackend
```

### 2. Virtual Environment (Optional)
Optional: Create Virtual Enviroment, Activate and install requirements
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Database Set up
Set up the database and run the initial migrations
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### 4. Start Application
Start the Flask application
```bash
flask run
```

### 5. Project Structure
This tree represents the directories this repository have
```
boliviamoveisbackend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── product.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── product.py
│   │   └── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── product_service.py
│   │   └── user_service.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── product.py
│   │   └── user.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── database.py
│   ├── db/
│   │   ├── __init__.py
│   │   └── base.py
├── tests/
│   ├── __init__.py
│   ├── test_product.py
│   ├── test_user.py
│   └── test_cart.py
├── migrations/
│   ├── versions/
│   ├── env.py
│   ├── script.py.mako
│   └── alembic.ini
├── .env
├── requirements.txt
├── run.py
└── README.md
```

### 6. Run Tests
To run the tests, use the following command

```bash
pytest
```