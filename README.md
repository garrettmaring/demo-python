# demo-python

Skeleton project demonstrating Python and pytest on the Engi network.

## Install

`pipenv install`

### Generate requirements

`pipenv requirements --dev > requirements.txt`

## Run

`pipenv run pytest --report-log pytest.json`

### Docker

`docker-compose up --exit-code-from tests`

Engi-compatible test runner output is in `pytest.json`