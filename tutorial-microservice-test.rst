Testing a microservice
======================

To test that you can run a container from your image locally you can run it directly in the terminal. First we need to login to Docker. Run the command docker login and enter your Docker Hub **username** and **password** when prompted.

Next we'll need to run the image to create the container.

To check that you have created the image run the command:

::

  docker run -p <local_port>:<container_port> <docker_username>/<your_repository_name>:<tagname>

Set **local_port** to 5000 and the container_port to the same as the one you specified in the Dockerfile.

Now you can either go to the url in the browser or do:

::

 curl -v http://localhost:5000/api/orders

in terminal to see if the the container runs.

To stop the container running locally you can run:

::

 docker stop <container name> or docker stop <container_id>
