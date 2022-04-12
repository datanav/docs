.. _tutorial_custom_data_source_microservice:

Customize Data Source - The Microservice System
===============================================

In this lesson we will look closer into how to crate a custom data source with a microservice. When finished with this tutorial you will have built both the microservice and set up the required configurations in Sesam in order to import data from an external REST API. You will be given information on how to access the API as well as a microservice template in which you will have to add the needed logic to import data from that API into a Sesam pipe.

.. admonition:: Prerequisits

  Before starting on this tutorial we suggest you get familiar with input pipes [link] aswell as the :ref:`Custom Data Source - The Microservice System <custom_data_source_microservice>` article in our documentation. 
    
  Good to have:
    - An account on DockerHub (free)
    - A developer account on HubSpot (free)
    - An understanding on how to create Docker images
    - Coding experience (we use Python in this example, but any coding language works as long as you can translate to it from Python)

.. tip::
    - Set your sensitive variables as secrets in Sesam and send those secrets to the microservice as environmental variables.
    - `Postman <https://www.postman.com>`_ is a great tool for testing API functionality
        

Disclaimer
----------
You will have to make sure that once entities are imported to Sesam they need an "_id" property. If this property does not exist in the original data from your source, the input pipe has to create it.

Use-case
--------
A company uses HubSpot for their CRM solution. The company would like to import all the CRM contacts into Sesam in order to utilize that data across their whole enterprice.  

Remember
--------
Testing how a microservice interacts with Sesam directly in Sesam can be troublesome as you have to create a Docker image and spin up the corresponding container in Sesam for each code change. Make sure you test the microservice thouroughly locally before creating the docker image.

Assignment
----------
Write a microservice that imports all the contacts on your developer HubSpot account. You can find information about the needed API `here <https://developers.hubspot.com/docs/api/crm/contacts>`_. Create a Docker image from the microservice and connect that Docker image to your Sesam node inside a :ref:`Microservice System <microservice_system>` and set up an input pipe that collects the contact data from the Microservice system. 

To start of we have provided you with a microservice template written in Python that you may use if you wish.

.. raw:: html

   <details close>
   <summary><a>Microservice template</a></summary>

.. code-block:: python
  :linenos:

  import requests
  import json 
  from flask import Flask, request, Response
  import logging
  import os

  app = Flask(__name__)
  logger = None
  format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
  logger = logging.getLogger('hubspot')

  # Log to stdout
  stdout_handler = logging.StreamHandler()
  stdout_handler.setFormatter(logging.Formatter(format_string))
  logger.addHandler(stdout_handler)
  logger.setLevel(logging.DEBUG)

  api_key = os.environ.get("")

  @app.route("/get_contacts", methods=["GET", "POST"])
  def get_contacts():
      res = requests.get(url=url)

      if res.status_code != 200:
          logger.error("Unexpected response status code: %d with response text %s" % (res.status_code, res.text))
          raise AssertionError ("Unexpected response status code: %d with response text %s"%(res.status_code, res.text))

      return json.dumps(<some data>)


  if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', threaded=True, port=os.environ.get('port',5000))

.. raw:: html

   </details>

Result
------

When finished you should see at least two contacts from HubSpot imported to your Sesam node (the two default test contacts included in your HubSpot developer account).
