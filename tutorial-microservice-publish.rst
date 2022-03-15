Publish to Docker Hub
=====================
First you need to sign up on `Docker <https://www.docker.com>`__ and create a new repository.

.. image:: images/getting-started/Docker-repo.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Now we need to push the image to the repository:

To check that the you have created image run the command:

::

 docker push <docker_username>/<your_repository_name>:<tagname>

Go to hub.docker.com and check that you can see the tagname in you repository.

.. image:: images/getting-started/docker-push.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept
