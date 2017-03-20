# Template Project

This is a project template that creates a docker environment with useful containers
for the Data For Democracy project.

Docker is a technology that allows you to package up all of the dependencies for a
project in a portable way. It's like virtual environments, but extending to the whole
OS, not just Python packages.

This template creates a dummy postgres database, a Flask server, and a Conda
environment running jupyter. These are just samples, so feel free to change
things in your template.

To get started:

1. Install Docker: https://www.docker.com/products/overview

2. In this directory, run `docker-compose up`
   This will take a while the first time you do it, because it's downloading
   all of the dependencies for all of the subparts of the project. It should
   be much faster after the first time.

3. In the output, you should see lines like these, telling you where to connect:
```
conda_1     |     Copy/paste this URL into your browser when you connect for the first time,
conda_1     |     to login with a token:
conda_1     |         http://localhost:5002/?token=9c010637753fdf9646eb75a3d6b36b0a5e5464e5b5d32df3

flask_1     |  * Running on http://0.0.0.0:5001/ (Press CTRL+C to quit)
```

4. To stop all of the running services, use CTRL+C.

5. Data stored in the database will be preserved from run to run.

6. Code put in source/python will be available to both Conda and the Flask server

7. If you add something to `requirements.txt` use `docker-compose up --build` to
pick up the new dependencies
