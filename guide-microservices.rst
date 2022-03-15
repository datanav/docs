.. _getting-started-microservices:

Microservices
=============

Introduction
------------
This guide will help you build and use a Sesam extension using microservices.

We start by building a Docker image from our microservice. A Docker image is the blueprint for creating a container with our microservice.

The Docker image is then pushed up to a repository on Docker Hub (or any Docker platform. When hosted in the repository the image can be pulled by anyone with access.

Finally, we pull the image from our Docker Hub repository (although private repositories are also supported) and spin up a container on our Sesam node. The container is created from the image and started. The Docker-commands for this are performed by Sesam. We simply specify the location of the image on Docker Hub in our Sesam system configuration and the container is spun up automatically. Once the Docker image location is defined in the System config Sesam will spin up the correponding container automatically. Finally to transfer data between Sesam datahub and the microservice, we need an inbound pipe or endpoint pipe depending on solution. For example a SQL database sends data to a Sesam pipe via a default microservice available inside your Sesam node, and similarly for data going out of Sesam to target systems.

After you have completed these tutorials you would have:

#. Created and tested a microservice
#. Used the microservice in your Sesam subscription


Steps
-----

.. toctree::
   :maxdepth: 1

   Creating a microservice  <tutorial-microservice-create>
   Testing a microservice  <tutorial-microservice-test>
   Publish to Docker Hub <tutorial-microservice-publish>
   Using a microservice <tutorial-microservice-use>





