.. _tutorial_custom_data_source_microservice:

============================================
Custom Data Source - The Microservice System
============================================

*In this lesson we will look closer into how to crate a custom data source with a microservice. When finished with this tutorial you will have built both the microservice and set up the required configurations in Sesam in order to import data from an external REST API. You will be given information to a public API and a microservice template in which you will have to add the needed logic to import data from that API into a Sesam pipe*.

.. admonition:: Pre-requisits

  **Sesam specific pre-requisites**
  
  Before starting on this lesson we expect a general understanding on input pipes in Sesam and we recommend that you read about :ref:`Custom Data Source - The Microservice System <custom_data_source_microservice>` in the Sesam documentation. 
  
  **Other useful pre-requisites**
  In order to finish this lesson the following bullets point will also help:

  - An account on DockerHub (a public account is free of charge and very quickly set up)
  - An understanding on how to create Docker images
  - Coding experience (we use Python in this example, but any coding language works as long as you can translate to it from Python)

Disclaimer
----------
You will have to make sure that once entities are imported to Sesam they need an "_id" property. If this property does not exist in the original data from your source, the input pipe has to create it.


Use-case
--------
An IT consultant company wishes to create an automated CV functionality for all of their employees and publish it on their website. As part of their CV the company want to display all the code repositories each employee owns on their company associated GitHub accounts. 

Remember
--------
Testing how a microservice interacts with Sesam directly in Sesam can be troublesome as you have to create a Docker image and spin up the corresponding container in Sesam for each code change. Make sure you test the microservice thouroughly locally before creating the docker image.

Assignment
----------
Write a microservice that collects metadata for all your GitHub repositories. Create a Docker image from the microservice and connect that Docker image to your Sesam node inside a :ref:`Microservice System <microservice_system>` and set up an input pipe that collects the repository data from the Microservice system. 

To start of we will provide you with a microservice template written in Python that you may use if you wish:

.. raw:: html

   <details open>
   <summary><a>Microservice template</a></summary>

.. code-block:: python
  :linenos:

  from flask import Flask, request
  import logging
  import os
  import requests
  import json

  app = Flask(__name__)

  logger = None
  format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
  logger = logging.getLogger('github')

  # Log to stdout
  stdout_handler = logging.StreamHandler()
  stdout_handler.setFormatter(logging.Formatter(format_string))
  logger.addHandler(stdout_handler)
  logger.setLevel(logging.DEBUG)

  my_access_token = 

  @app.route("/<path>", methods=["POST", "GET"])
  def post(path):
      headers = 
      response = requests.get(url, headers)
      if response.status_code != 200:
          raise AssertionError("Unexpected response status code: %d with response text %s" % (response.status_code, response.text))

      return 
  if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', threaded=True, port=os.environ.get('port',5000))

.. raw:: html

   </details>

For this assignment you will need:

- A `GitHub <https://www.github.com>`_ account
- A `GitHub personal access token <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token>`_
- Some way to store your Docker image in the cloud (i.e. `DockerHub <https://www.dockerhub.com>`_)

    .. tip::
        - Set your access token up as a secret in Sesam and send that secret to the microservice as an environmental variable.
        - `Postman <https://www.postman.com>`_ is a great tool for testing API functionality
        


Result
------

When finished you should see every metadata for each of your repositories in your input pipe's output.
