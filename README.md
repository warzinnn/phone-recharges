## Phone Recharge Project


API (CRUD) used for phone recharges. The user can buy telephone credits for his phone by informing his phone number.


### Built With
- Python
- Pytest
- TDD
- Clean Architecture
- Flask
- Object-Oriented Programming (OOP)
- ORM (SQLAlchemy)
- Relational database
- PostgreSQL
- GIT
- Docker

### Installation

1. Clone the repo
```sh
git clone https://github.com/warzinnn/phone-recharges.git
```

2. Install requirements
```sh
pip install -r requirements
```

3. Set environment variable. Update (or create) the .env file with the following information:  
PS: Type in a postgres user and password of your choice.
```sh
CONFIGURATION_SETUP="src.infrastructure.web_flask.config.DevelopmentConfig"
POSTGRES_USER=CHANGE_THIS
POSTGRES_PASSWORD=CHANGE_THIS
POSTGRES_DB=dev_recharges
POSTGRES_URL="postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:5432/${POSTGRES_DB}"
```

4. Docker (Set up Postgresql)
```sh 
docker-compose up
```

### Usage
- Go to project folder. 
    - Run:  
        `python3 app_flask.py` or `flask --app app_flask run --port 5001`
    - Access:  
        `http://127.0.0.1:5001/`

- For tests use:  
    `python3 -m pytest`

### API Endpoints
- There's a postman collection in the project files with the list of the resources and their respective parameters.
    `phone-recharges.postman_collection.json`

| HTTP Verb | Endpoint | Action |
| --- | --- | --- |
| GET | /company |  Return the list of companies |
| POST | /company |  Create a new company |
| DELETE | /company |  Delete a company |
| GET | /company/products |  Return the list of products |
| POST | /company/products |  Create a new product |
| PUT | /company/products |  Update a product |
| DELETE | /company/products |  Delete a product |
| GET | /recharge |  Return the list of recharges |
| POST | /recharge |  Create a new recharge |