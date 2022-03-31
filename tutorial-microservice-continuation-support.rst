.. _tutorial_microservices_continuation_support:

====================================
Microservices - Continuation support
====================================

*In this lesson we will look closer into continuation support and change tracking for data imported from a microservice. When finished with this lesson you will have learned to include the necessary logic for implementing continuation support in a Sesam microservice as well as added the corresponding support inside a Sesam input pipe. You will be given information to a public API and a microservice template in which you will have to add the needed logic to import changes from that API into a Sesam pipe*

.. admonition:: Pre-requisits

  **Sesam specific pre-requisites**

  This lesson covers how to implement change tracking through continuation support in microservices. Before starting on this lesson we expect a general understanding on input pipes in Sesam and we recommend that you do the tutorial :ref:`Custom Data Source - The Microservice System <tutorial_custom_data_source_microservice>`. 

  **Other useful pre-requisites**
  
  In order to finish this lesson the following bullets point will also help:

  - An account on DockerHub (a public account is free of charge and very quickly set up)
  - An understanding on how to create Docker images
  - Coding experience (we use Python in this example, but any coding language works as long as you can translate to it from Python)

Disclaimer
----------
Continuation support refers to the functionality which helps the pipe remember what it did last time in order to continue from that spot while change tracking refers to the whole action of importing changes and processing them as a stream of changes in Sesam.

Use-case
--------
An IT consultant company wishes to create an automated CV functionality for all of their employees and publish it on their website. As part of their CV the company want to display all the code repositories each employee owns on their company associated GitHub accounts. Since this is a large company with many employees, they wish to add a functionality where only repositories that has been updated are imported into Sesam (except for the initial full sync) in order to minimize the load in their Sesam node. 

Remember
--------
Each API has different functionalities, and not every API supports query parameters to access only updated data. It's important to throuroughly read the API's documentation in order to set the correct query parameter as you since parameter.

Assignment
----------
Write a microservice with :ref:`continuation support <continuation_support_microservices>` that connects to your personal GitHub instance through the `GitHub API <https://docs.github.com/en/rest/reference/repos>`_ and collects metadata for all your repositories. Create a Docker image from the microservice and connect that Docker image to your Sesam node inside a :ref:`Microservice System <microservice_system>` and set up an input pipe that collects the repository data from the Microservice system. You can make sure that only updates are collected by making a minor change to one of your repositories inside GitHub and see if the pipe registers the change.

To start of we will provide you with the same microservice template as given in :ref:`Custom Data Source - The Microservice System <tutorial_custom_data_source_microservice>`:

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


