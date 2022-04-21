.. _microservices :

=============
Microservices
=============

Sesam comes with a multitude of built-in connectors that may connect to many of the most common data sources such as SQL servers, open http endpoints or REST APIs  :ref:`and many more <system_section>`. However, some times you need extra functionality in order to ensure a functional and efficient data transfer. One solution to these situations may me to let a microservice do the necessary operations for you.   

A Microservice is a modular self-contained software that provide a particular service. 

From a Sesam perspective microservices often function as connectors to either pull data from a source system or
push data to a target system. They can even be used to transform data as part of a step inside a pipe for situations where you might need that extra functionality.

Microservices are hosted in Sesam as docker containers. They are configured using
system configs and their logs can be inspected through the system's **Status** tab.

Microservice code can essentially be written in any programming language, but in Sesam we usually
prefer Python, and the following examples will be based on Python. We often use the python module `Flask <https://flask.palletsprojects.com/en/2.0.x/>`_ as a web application framework, but you are of cource welcome to use any method you feel familiar with.

Sesam provides a `public GitHub repository <https://github.com/sesam-community>`_ where we publich microservices we have found useful. Before starting to create your own, make sure that the functionality you're looking for does not already exist there. Microservices in our public GitHub repository are also linked to our `public DockerHub repository <https://hub.docker.com/u/sesamcommunity>`_ with Docker images built and ready to use. 


    .. tip::

        Try to minimize the logic performed in microservices. Often it might make sense to just perform transformations on the data inside a microservice instead of sending the data to Sesam and performing the same operations there. But bare in mind :ref:`Sesam's data model <core_principles>`: we want to, to as large extent as possible, keep the source system's original data model in Sesam. Also, once we start changing data inside microservices it might be hard to troubleshoot errors since logic is spread out over different instanses. 


.. _creating_a_microservice :

Creating a microservice
-----------------------

Below you will find a template for a simplified microservice. It will form the baseline to which we will add the different functionalities available for a microservice in use in a Sesam installation. 

.. raw:: html

   <details open>
   <summary><a>Microservice template</a></summary>

.. code-block:: python
  :linenos:

  from flask import Flask, request
  import logging
  import os
  import requests

  app = Flask(__name__)

  logger = None
  format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
  logger = logging.getLogger('microservice-template')

  # Log to stdout
  stdout_handler = logging.StreamHandler()
  stdout_handler.setFormatter(logging.Formatter(format_string))
  logger.addHandler(stdout_handler)
  logger.setLevel(logging.DEBUG)

  access_token = os.environ.get('ACCESS_TOKEN')

  @app.route("/post_entities/<url>", methods=["GET"])
  def post_func(url):
      headers = {"Authorization": "Bearer {}".format(access_token)}
      entities = request.get_json()

      for entity in entities:
          response = requests.post(url=url, headers=headers, data=entity)
          if response.status_code != 200:
              raise AssertionError("Unexpected response status code: %d with response text %s" % (response.status_code, response.text))

      return "Some return message"
      

  @app.route("/get_entities/<url>", methods=["GET"])
  def get_func(url):
      headers = {"Authorization": "Bearer {}".format(access_token)}

      response = requests.get(url = url, headers=headers)
      if response.status_code != 200:
          raise AssertionError("Unexpected response status code: %d with response text %s" % (response.status_code, response.text))

      entities = response.json()
      return json.dumps(entities)

  if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', threaded=True, port=os.environ.get('port',5000))

.. raw:: html

   </details>

.. _passing_variables_to_a_microservice:

Passing variables to a microservice
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Sesam there are three typical ways of passing variables from Sesam into a microservice: 

- By setting environmental variables directly to the Docker container in which the microservice runs. We will explain how this is done through Sesam in the :ref:`Using a microservice <using_a_microservice>` section.
- Through `dynamic URL's <https://stackoverflow.com/questions/35107885/how-to-generate-dynamic-urls-in-flask>`_ in the route decorator.
- Through the request parameters  in the :ref:`JSON pull <json_pull>` and :ref:`JSON push <json_push>` protocols.

Environmental variables are usually system specific varables, i.e. they are used throughout the whole microservice and not for a spesific route. Example of these might be access tokens, base URL's or headers.

Variables through dynamic URL's are generally pipe spesific variables that are only used for specific routes. These variables include variables such as endpoint URL's or entity data that are specific for that pipe.

The request parameters are set variables containing information about the the request and state of the pipe such as batch information and since values. 

Logs from a microservice
^^^^^^^^^^^^^^^^^^^^^^^^

The best way to display information from the microservice in Sesam is to setup logging statements. These logs can later be viewed in the microservice system's **Status page** (link). You will also be able to see some error messages and full tracebacks in the **execution logs** (link) of the pipes executing the microservice's routes. These messages can however be hard to read, and does not always log all the needed information.   

Importing data to Sesam
^^^^^^^^^^^^^^^^^^^^^^^

When setting up a microservice route to import data to Sesam there are some important functionalities you should be aware of and try to implement. Generally you want to try to only import changes in the source data to avoid unnecessary processing of data. You should also, whenever possible, stream data directly into Sesam and not store the data temporarily in the Docker container in order to avoid container taking up to much memory.

Change tracking
***************

Whenever possible we advise to always setup a microservice to only import changes and not full imports. This will drastically reduce the time it takes for a microservice to import data, and therefore also make data available to target systems much faster. In Sesam we refer to this as change tracking (**link**) and how to enable change tracking for microservices can be read about in detail in the section covering :ref:`Continuation support for Microservices <continuation_support_microservices>`.

Our microservice template including continuation support is displayed below.

.. raw:: html

   <details open>
   <summary><a>Microservice template with continuation support</a></summary>

.. code-block:: python
  :linenos:

  from flask import Flask, request
  import logging
  import os
  import requests

  app = Flask(__name__)

  logger = None
  format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
  logger = logging.getLogger('microservice-template')

  # Log to stdout
  stdout_handler = logging.StreamHandler()
  stdout_handler.setFormatter(logging.Formatter(format_string))
  logger.addHandler(stdout_handler)
  logger.setLevel(logging.DEBUG)

  access_token = os.environ.get('ACCESS_TOKEN')

  @app.route("/post_entities/<url>", methods=["GET"])
  def post_func(url):
      entities = request.get_json()

      headers = {"Authorization": "Bearer {}".format(access_token)}

      for entity in entities:
          response = requests.post(url=url, headers=headers, data=entity)
          if response.status_code != 200:
              raise AssertionError("Unexpected response status code: %d with response text %s" % (response.status_code, response.text))

      return "Some return message"
      

  @app.route("/get_entities/<url>", methods=["GET"])
  def get_func(url):
      if request.args.get('since') is None:
          url = url
      else:
          url = url + "?filter=modifiedon ge {}".format(request.args.get('since'))
 
      headers = {"Authorization": "Bearer {}".format(access_token)}

      response = requests.get(url = url, headers=headers)
      if response.status_code != 200:
          raise AssertionError("Unexpected response status code: %d with response text %s" % (response.status_code, response.text))

      entities = response.json()
      for entity in entities:
          entity["_updated"] = entity["modifiedon"]

      return json.dumps(entities)

  if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', threaded=True, port=os.environ.get('port',5000))

.. raw:: html

   </details>

Memory awareness
****************

An other important concept to be aware of if memory usage of your microservices. This both entails the total memory of the Docker container in which the microservice runs as well as the required memory to GET and POST data to and from Sesam. You can yourself decide how much MB of RAM to allocate for a Docker container through the :ref:`Microservice system configuration <microservice_system>`, but be aware that Docker container memory usage could affect the whole Sesam instance if misused and should therefore be thoroughly considered before changed. 

For container size we advise to create as minimalistic containers as possible (especially when concidering container OS), and for the required memory when importing/exporting data we suggest to stream data directly to Sesam instead of storing it in the Docker container.  

Below is an example of the microservice template where we stream entities back to Sesam instead of storing them in the Docker container.

.. raw:: html

   <details open>
   <summary><a>Microservice template streaming</a></summary>

.. code-block:: python
  :linenos:

  TO BE DONE

.. raw:: html

   </details>

Exporting data from Sesam
^^^^^^^^^^^^^^^^^^^^^^^^^
In addition to **memory awareness** and **passing variables to a microservice**, as mentioned above, there are a couple of Sesam functionalities you should be aware of when create route for exporting data from Sesam in a microservice.

When using the :ref:`JSON push sink <json_sink>` to send entities from Sesam to the microservice Sesam includes each entity's system attributes (:ref:`reserved fields <reserved_fields>`). There might very well be use for them in the microservice, but if there is not these may have to be removed before sending the data from the microservice to the target system. This may be especially for entities with *"_deleted": true*. This means the entity is marked as deleted in Sesam and might require some extra functionality to be handeled in the microservice. 

When Sesam sends data through the JSON push sink it sends the data in batches. In addition Sesam will always send one final batch without any data inside it. Therefore, if you have a JSON push sink batch size of 100 (the default value) and try to send 150 entities Sesam will send three different batches. The first batch will contain 100 entities, the second 50 entities and the last one 0 entities. This is good to have in mind when setting up the microservice.   

External transformations
^^^^^^^^^^^^^^^^^^^^^^^^
The term external transformations covers any situation where you utilize functionalities outside Sesam inside a Sesam pipe. These functionalities are accessed by use of the pipe transforms :ref:`http transform <http_transform>` and :ref:`REST transform <rest_transform>`. Use-cases may entail the need to use data from entities to fetch additional data from an API, or you might need additional transform functionality not supported by Sesam to mention some use-cases. For these, and similar situations, an external transformation could be the solution. In it's core, an external transformation uses data from Sesam to perform some kind of action on it outside of Sesam, and sends the results back to a transform in a pipe for further processing.

One explicit use-case for external transformations is to perform the Sesam version of `optimistic locking <https://www.ibm.com/docs/en/db2/11.5?topic=overview-optimistic-locking>`_. 

Optimistic locking with microservices
*************************************
**Starten av denne delen skal muligens være et annet sted i docs, men ligger her pr. nå**

Optimistic locking in Sesam is a key component in bidirectional syncronization of golden records, the product of Sesam's Master Data Management (MDM) (**we should really have a section on MDM in Sesam...**). We utilize optimistic locking in order to minimize the chances of overwriting data in the target system Sesam has yet to import and process. 

**Use-case**:
Imagine Sesam importing person data from systems A, B and C. They all undergo MDM in Sesam in order to create golden recods by combining the data from all three systems. Sesam have now created a new set of golden records which quality is potentionally much highar than the quality in the three source systems. We therefore wish to sync this data back to all three systems to achieve consistency on all levels. However, before sending the golden record #1 back to system A, someone updates the corresponding row in system A. We now risk overwriting those changes with our golden record, changes that really should be sent into Sesam's MDM for processing. 

**Solution**: 
Before updating system A, for each golden record we wish to send we do a single entity lookup and compare the response with the result from the last import. If there are no deviations we can safely update system A. If there is a deviation, that means that row has been updated in system A and we need to wait until that changes has been processed by Sesam before we can try to update that row again. 

In terms of using a microservice for optimistic locking we need the microservice to be able to lookup single entities. We also need the microservice to return not only the response, but the data it got from Sesam in order to be able to compare these two sets of data inside Sesam. 

The example below shows an example on how this may look inside out microservice template. 

.. raw:: html

   <details open>
   <summary><a>Microservice template with optimistic locking support</a></summary>

.. code-block:: python
  :linenos:

  from flask import Flask, request
  import logging
  import os
  import requests

  app = Flask(__name__)

  logger = None
  format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
  logger = logging.getLogger('microservice-template')

  # Log to stdout
  stdout_handler = logging.StreamHandler()
  stdout_handler.setFormatter(logging.Formatter(format_string))
  logger.addHandler(stdout_handler)
  logger.setLevel(logging.DEBUG)

  access_token = os.environ.get('ACCESS_TOKEN')


  @app.route("/single_entity_lookup/<url>", methods=["POST", "GET"])
  def post_func(url):
      headers = {"Authorization": "Bearer {}".format(access_token)}
      payload = request.get_json()

      url += payload["_id"]

      response = requests.post(url=url, headers=headers)
      if response.status_code != 200:
          raise AssertionError("Unexpected response status code: %d with response text %s" % (response.status_code, response.text))

      entity = response.json()
      entity["old_entity"] = payload
      return json.dumps(entity)

  if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', threaded=True, port=os.environ.get('port',5000))

.. raw:: html

   </details>

.. _using_a_microservice :

Using a microservice
--------------------

In this section we will show you how to use microservices in Sesam and how to access and utilize the functionalities in :ref:`Creating a Microservice <creating_a_microservice>`.

To connect a microservice to Sesam you will first need to create a docker image. You can read about creating Docker images for Python microservices `here <https://medium.com/@ssola/building-microservices-with-python-part-2-9f951199094a>`_. Once the image is created you need to make accessible to the Sesam node, in Sesam we often publish our Docker images on a Docker cloud provider, such as `DockerHub <https://hub.docker.com/>`_.

To build a container in Sesam based on your Docker image you need to create a system in Sesam using the :ref:`Microservice system configuration <microservice_system>`. Below you can view a simplified microservice system configuration connected to a public cloud repo:

:: 

  {
    "_id": "test-system",
    "type": "system:microservice",
    "docker": {
      "image": "test-repo/test-image:1.0.0",
      "port": 5000
    }
  }

Connecting pipes to a microservice done by using either the :ref:`JSON push sink <json_sink>` or the :ref:`JSON source <json_source>` depending on if you're exporting data out from Sesam or importing data into Sesam. The **url** property in the two configurations connects to the route URL's in your microservice such that a route on the form

.. code-block:: python

  @app.route("/my_route", methods=["POST", "GET"])

would be activated by setting the **url** property value to "my_route". Thus, different pipes may activate different routes in the same microservice.

Passing variables to a microservice
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
As mentioned :ref:`above <passing_variables_to_a_microservice>` there are three ways of passing non-entity data to a microservice, and in this section we will show you examples of enrironmental variables and variables through dynamic URL's. 

You can read about passing environmental variables to a docker container :ref:`here <microservice_system>`.

The following system configuration shows an example of how environmental variables may be sent to a microservice:
::

  {
    "_id": "test-system",
    "type": "system:microservice",
    "docker": {
      "environment": {
        "access_token": "$SECRET(test-access-token)",
        "base-url": "$ENV(test-base-url)"
      },
      "image": "test-repo/test-image:1.0.0",
      "port": 5000
    }
  }

In this example the access token (stored as a :ref:`secret <secrets_manager>` in Sesam) and the base-url (stored av a node :ref:`environmental variable <environment_variables>` in Sesam) are stored as environmental variables in the Docker container. These variables can be accesses by all routes in the microservice.

The following pipe sink configuration and pytohn snippet shows an example of how dynamic URL's may be used to send pipe specific variables to a specific microservice route:

::

  {
      "type": "json",
      "system": "test-system",
      "url": "my-route/test-endpoint"
   }

.. code-block:: python

  @app.route("/my_route/<endpoint-url>", methods=["POST", "GET"])
  def my_func(endpoint-url):

In this example the endpoint url is accessed only by this specific route in the microservice.







TODO:

- continuation support
- _deleted and other system attributes
- optimistic locking
- execution log
- external transformations


