# Charlie Mail Worker 

This is a service that uses Celery and rabbitMQ to create tasks where email ingestion is performed by making a request to the GraphO365 service.

## How To Run
### Develop
1. Run an instance of rabbit (broker) and redis (backend) locally via containers. This is done through docker compose located in the `docker/Docker-compose.dev.yaml` folder.
To do this run the following command

```bash
`docker-compose -f docker/Docker-compose.dev.yaml up -d`
```


2. Then, you need to start the celery worker. For this in the root folder of the project there is an example `launch.json` to put in the `.vscode` folder, used for debugging.
As the worker runs locally (not in a container) be sure that it is running in a virtual environment with all the required dependencies in the project.

3. The last step is to send a task to the worker, to do this you have a `main.py` file in the root of the project, there you must send the required data. And execute with `python main.py`.
