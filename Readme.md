# Template Project

This is a project template that creates a Docker environment with useful containers
for the Data For Democracy project.

Docker is a technology that allows you to package up all of the dependencies for a
project in a portable way. It's like virtual environments, but extending to the whole
OS, not just Python packages.

This template sets up a Node webapp server, Flask webapp server, a Conda environment running Jupyter,
and Postgres and MongoDB databases that they can talk to. The idea is that you'll delete the pieces
that you don't intend to use (remove them from `docker-compose.yml` and delete the directories), and
customize the ones you do.

To get started:

1. Install Docker: https://www.docker.com/products/overview
 * If using windows:
 * Get the docker toolbox for windows 10 home or earlier: https://docs.docker.com/toolbox/toolbox_install_windows/
 * Make sure virtualization is enabled (enter BIOS menu, adjust as needed)
 * Create a docker machine. For windows 10 home and earlier use `docker-machine create --driver virtualbox MACHINENAME`. Use other drivers as necessary (https://docs.docker.com/engine/getstarted-voting-app/node-setup/)
 * Setup the machine's environment variables: `docker-machine env MACHINENAME`
 * Finally, activate the machine. The last statement should tell you how but in powershell: `docker-machine env MACHINENAME | invoke-expression`
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

node_1      | Running on http://localhost:5003
```

4. To stop all of the running services, use CTRL+C.

5. Data stored in the database will be preserved from run to run.

6. Code put in source/python will be available to both Conda and the Flask server

7. If you add something to `requirements.txt` or `packages.json` use `docker-compose up --build` to
pick up the new dependencies
