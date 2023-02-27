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
    - Models, Entities, Use cases

### Installation

1. Clone the repo
```sh
git clone https://github.com/warzinnn/phone-recharges.git
```

2. Install requirements
```sh
pip install -r requirements
```

3. Set environment variable
```sh
export CONFIGURATION_SETUP="config.DevelopmentConfig"
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
