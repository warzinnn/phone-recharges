## Phone Recharge Project


API used for phone recharges. The user can buy telephone credits for his phone by informing his phone number.

Project realized for studies purpose based on the [Desafio Backend do Jeitto.](https://github.com/Jeitto/jeitto-backend-challenge-201901)


### Built With
- Python (version 3.10.9)
    - Flask
    - TDD
    - Postgresql (with Docker)
    - SQL Alchemy

- Project organization:
    - Blueprints (flask)
    - Repository pattern
    - Factory pattern
    - Models, Entities

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
CONFIGURATION_SETUP="config.DevelopmentConfig"
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
        `python3 app.py` or `flask run`
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
| POSt | /recharge |  Create a new recharge |