.. _getting-started-microservices:

Microservices
=============

Introduction
------------
This guide will help you build and use microservices inside your Sesam instance. 

    .. tip::

        Microservices may help you increase your node's connectivity capabilities, but make sure that these aren't functionalities covered in the built-in Sesam functionalities already. Quite often people create microservices only to discover that either someone has already created one or that the desired functionality was already covered in the Sesam software. 

        Sesam has a public git repository located `here <https://www.github.com/sesam-community>`_ where we publish microservices that we ourselves have found very useful.


This guide is divided into two sections: :ref:`Creating a microservice <tutorial_microservice_create>` and :ref:`Using a microservice in Sesam <tutorial_microservice_use>`. 

In "Creating a microservice" we will go through all the important aspects to have in mind when creating a microservice for use in Sesam. These concepts covers:

  - How Sesam passes data to and receives data from a microservice (incl. streaming, empty list last batch and system attributes/_deleted)
  - Passing variables between the microservice and Sesam
  - How to enable change tracking in a pipe connected to a microservice
  - Support for optimistic locking in a microservice
  - Memory awareness
  - Logging
  - Basic testing


In "Using a microservice in Sesam" we will talk about how the microservice communicates with your Sesam instance. These concepts covers:

  - Connecting Sesam to a Docker image
  - System config (incl env. vars)
  - Connecting microservice system to a pipe
  - Status page
  - Passing arguments from pipe

Steps
-----

.. toctree::
   :maxdepth: 1

   Creating a microservice  <tutorial-microservice-create>
   Using a microservice <tutorial-microservice-use>



Lessons
-------

.. toctree::
   :maxdepth: 1

   Microservices - Continuation support  <lesson-microservice-continuation-support>




