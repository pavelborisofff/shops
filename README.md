## Python Code Review Task #2
Simple API service based on Django REST Framework.

## How to use
### 1. Download or clone the repository
### 2. Install Poetry if you don't have it
osx / linux / bashonwindows install instructions:
`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
`
windows powershell install instructions
`(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
`
### 3. Go to the directory with the code
`cd <path_to_code>`
### 4. Create a virtual environment and install dependencies
`poetry install`
### 5. Run the server
`poetry run python manage.py runserver`
<br>If you want to run the server in debug mode, use
<br>`poetry run python manage.py runserver --settings=config.settings.local`
<br>By default the server is running on port 8000.
to change the port use
<br>`poetry run python manage.py runserver --port=<port_number>`
### 6. Test the API
`curl -i http://localhost:8000/api/v1/`