# Worker app
This service will execute the functionalities that were stipulated for the relationship with the middleware of the service in order to respond to the requests of the app-fitness.

implementing a worker Celery technology, and a service queue with Rabbit Mq in order to optimize the sending of tasks to be solved.

this service is connected by Docker containers from its Docker image. 

## Installation of dependencies

commands

```bash

pipenv shell
pipenv install

```

## Usage to run Rabbit Mq
command

```bash
docker-compose -f docker/Docker-compose.dev.yml up --build

```
## Usage to run Worker

Next, it is necessary to start the celery worker.
As the worker runs locally (not in a container) make sure it runs in a virtual environment with all the necessary dependencies in the project.

this for the launch.json file in the root .vscode folder

```python
{
  "version": "0.2.0",
  "configurations": [
  
    {
      "name": "worker",
      "type": "python",
      "request": "launch",
      "module": "celery",
      "console": "integratedTerminal",
      "cwd": "${workspaceFolder}",
      "args": [
        "-A",
        "app.worker.reservation",
        "worker",
        "-l",
        "info",
        "-c",
        "1",
        "-Q",
        "reservation"
      ],
      "env": {
        "APP_TITLE": "Guane Worker",
        "APP_DESCRIPTION":"Worker API",
        "APP_VERSION":"1.0.0",
        "RABBITMQ_USER": "user",
        "RABBITMQ_PASSWORD": "bitnami",
        "RABBITMQ_HOST": "localhost",
        "RABBITMQ_PORT": "5673",
        "DB_API": "http://localhost:8001",
        "DEBUGGER": "False",
        "ENVIRONMENT": "str",
        "WORKER_ROUTER": "app.worker.reservation.init_reservation",
        "QUEUE_INTAKE": "reservation"
      }
    }
  ]
}


```

## Important

Please make sure to update tests as appropriate.
if the command to run the program has an error add to the beginning of this default SUDO

## Remember

service-db and middelware services must be running to run and test this one

## License
[MIT](https://choosealicense.com/licenses/mit/)

