
.. _microservices-novice-5-2:

Novice
------


.. _interacting-with-a-microservice-in-sesam-5-2:

Interacting with a Microservice in Sesam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  Interacting with microservices...

  - to ingest or expose data is done with, respectively, a pull and push protocol
  - you should use the ``since`` request parameter, in the pull protocol, to enable delta requests
  - the request parameter ``is_first`` in the push protocol, on full data syncs, should be used to parse JSON from an array
  - you should make sure to implement thorough error handling in order to allow for adequate logging
  - logging should allow a non-technical user to understand why and potentially what made a microservice fail
  - is done by "coupling" a given system with a given pipe
  - in terms of triggering a microservice, the trigger is when streams of data flows through the implementation point 

Interacting with a microservice in a Sesam node is by no means a simple thing when it comes to the technicality of utilizing a microservice in the best possible way. In order for you to get the tools necessary to do exactly this, the following sub-sections will explain certain topics related to integrating a microservice optimally in Sesam. 

Protocols
#########

In terms of functionality, a microservice will need to either ingest and/or expose data. Therefore, we will now talk about the pull and push protocols, which respectively allows for ingestion and exposure of data.

The pull and push protocols are HTTP-based protocols. The pull protocol uses GET requests to read streams of JSON data. Requests can be split across multiple requests, albeit you should be cautious about splitting up your request, as you risk to only get a sample of the entire stream of data you are reading. 

The pull protocol supports the following request parameters:

- ``since`` - specifies an offset from which reading of data will start.
- ``limit`` - specifies a maximum number of entities from which the server will cap the response.
- ``subset`` - specifies whether a subset of entities is requested. 

The push protocol uses POST requests to write incremental or full data syncs across to an HTTP endpoint. It allows for splitting up data into smaller batches in order to decrease load on every request.

The push protocol supports the following request parameters:

- ``sequence_id`` - a string token which is generated every time the data sync is started.
- ``is_full`` - a boolean which evaluates to ``true`` on full data syncs and ``false`` if incremental. Default value is ``false``.
- ``request_id`` - a string token which is generated on every request.
- ``previous_request_id`` - a string token which refers to the previous ``request_id``. Present on all, but the first request.
- ``is_first`` - a boolean, only set on full data syncs, which is included on the first request and has a default value of ``true``. 
- ``is_last`` - a boolean, only set on full data syncs, which is included on the last request and has a default value of ``true``.

Additional information about the protocols can be found here: `Pull <https://docs.sesam.io/json-pull.html#json-pull-protocol>`_ or `Push <https://docs.sesam.io/json-push.html#json-push-protocol>`_.


Interaction & triggers
######################

Interacting with a microservice in a Sesam node means in practice creating a system of the type ``system:microservice``. This tells Sesam that the system is in reality a microservice hosted in Docker. An example of such a system can be seen below:

.. code-block:: json

  {
    "_id": "my-system-microservice",
    "type": "system:microservice",
    "docker": {
      "environment": {
        "user": "$ENV(my-username)",
        "password": "$SECRET(my-password)",
        "base_url": "$ENV(my-base_url)"
      }
    },
    "image": "myDockerID/myImageID:<semanticVersion>",
    "port": 5000
  }

After having set up such a system you can move on to making a pipe that interacts with this system:

.. code-block:: json

  {
    "_id": "my-pipe",
    "type": "pipe",
    "source": {
      "type": "json",
      "system": "my-system-microservice",
      "url": "/department"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"],
          ["add", "_id", "_S.departmentID"],
          ["add", "rdf:type", ["ni", "department:Denmark"]]
        ]
      }
    }
  }

As can be seen from the above pipe config you will recognize the name of your recently created system, namely "my-system-microservice". Basically, by specifying this name you tell Sesam that you wish to communicate with that exact microservice. Additionally, the property ``{"url": "/department"}`` is of particular interest to us. This property tells us which endpoint we are interested in ingesting data from. As outlined, you can provide whatever value you want for the key "url". This means that Sesam supports the implementation and use of dynamic endpoints such as Python's <path>. This makes interacting with microservices well supported and as such you do not need to think about compromising on your code in order for it to work in Sesam. 

Finally, the topic of triggering comes into play. Triggering your system in Sesam is governed by how data flows in a given dataflow. An inbound pipe, as shown in the above example, will by default run every 15 minutes, unless otherwise stated or if you choose to start the pipe manually. On the topic of run times, you can state specific run times by the use of cron expressions. A microservice that is used in the middle or at the end of a dataflow will be triggered when data flows through a specific pipe at this particular stage in the dataflow. As such, Sesam triggers microservices in accordance to the streams of data that makes a dataflow. A given change in the stream of data will trigger an interaction with a microservice, but only a load sufficient to handle the trigger will be carried out.


.. seealso::

  :ref:`developer-guide` > :ref:`configuration` > :ref:`source_section` > :ref:`continuation_support`

  :ref:`developer-guide` > :ref:`configuration` > :ref:`system_section` > :ref:`microservice_system`

  :ref:`developer-guide` > :ref:`json_pull_protocol`

  :ref:`developer-guide` > :ref:`json_push_protocol`

  :ref:`learn-sesam` > :ref:`systems` > :ref:`systems-novice-2-2`

.. _microservice-development-prerequisites-5-2:

Microservice Development Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  Microservice development prerequisites are...

  - an integrated development environment (IDE) or text editor
  - a Docker account
  - a GitHub account

In order to develop a microservice that will be used in a Sesam node as outlined in :ref:`interacting-with-a-microservice-in-sesam-5-2` you need to know what development environment you will need locally in order to make this happen.

Initially, Docker is a prerequisite. Adding, that an integrated development environment (IDE) or text editor will most likely also be needed. An IDE or text editor will allow you to write and develop your code. Docker allows for hosting your code as an image. A Docker image is referenced from a Sesam system. From that Docker image, Sesam creates a Docker container that is hosted and run in the Sesam node. In addition, a GitHub account is also advised as this will support for open sourcing your developed code and ease the way in which you can collaborate on developing your code.

The Sesam Community can be found `here <https://github.com/sesam-community>`_.

.. seealso::

  :ref:`developer-guide` > :ref:`configuration` > :ref:`system_section` > :ref:`microservice_system`

  :ref:`sesam-community`

.. _changing-a-microservice-5-2:

Changing a Microservice
~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  Changing a microservice...

  - follows a specific workflow from local development and testing to deployment in a Docker image  
  - is easily done locally by setting up test driven development (TDD)
  - that is open sourced should be forked, typically from GitHub, and then manipulated in accordance to needs
  - in terms of integrating it with Docker, this is done in a DockerFile 

When it comes to changing a microservice, a specific workflow is recommended. Initially, you should fork a publically available repository. The term repository is a synonym for microservice, and is used when the microservice is not yet hosted in Sesam via Docker. Publically available repositories are typically placed on GitHub. Sesam's `repositories <https://github.com/sesam-community>`_ can also be found there. Forking a repository means that you pull a given repository from i.e. Sesam Community on GitHub to your own account on GitHub. This allows for making radical and customer specific changes.

After having forked the repository to your personal account you should clone the repository to your local machine. Having successfully cloned the repository, you should open up the repository in your preferred IDE. At this point, you can start to make desired changes to the repository. When making changes, it is recommended to work from a test driven development (TDD) approach. TDD, among other things, improves design and code quality, minimizes technical depth and eases maintenance. Upon verifying that your changes perform as intended, you can move on to building your Docker image. When building a Docker image, you will be using a file named DockerFile. This file should be placed in the root of your repository. An example of a Dockerfile can be seen below:

.. code-block:: DOCKER
  :caption: DockerFile

  FROM python:3-alpine
  RUN apk update
  RUN pip3 install --upgrade pip
  COPY ./service/requirements.txt /service/requirements.txt
  RUN pip3 install -r /service/requirements.txt
  COPY ./service /service
  EXPOSE 5000 
  CMD ["python3","-u","./service/service.py"]

The DockerFile consists of a set of commands that each executes when building your Docker image. For details on what these specific commands do, you should look `here <https://docs.docker.com/>`_. When the build is running, you will see a set of entries in your CLI. These entries are defined by the above set of commands. To build your Docker image run the following command ``docker build .``. After a build finishes, you should run ``docker images`` to list all images that are currently running from your local Docker instance. If your last entry in this list is your recently build Docker image, everything has been build successfully.

Upon listing your Docker images, you will see a row with the header "IMAGE ID". This row holds unique identifiers for each of your Docker images. This unique identifier is used to tag a semantic version to your recently build Docker image, for example running ``docker tag <your-IMAGE-ID> <dockerUserName>/<nameOfYourDockerImage>:<semanticTag>``. This could in practice look like the following: ``docker tag 876cbf9e3dfa jc89als/autoconnect:deltaStream``. After successfully tagging your Docker image it is time to push your local image to a remote repository. `DockerHub <https://hub.docker.com/>`_ is used as a remote repository for Docker images. 

In order to push your image, extending on the example above, you will need to run the following command: ``docker push jc89als/autoconnect:deltaStream``. After successfully pushing your Docker image the last step is to configure your microservice system in Sesam to use the latest version of your recently pushed image. This could look like the following:

.. code-block:: json

  {
    "_id": "my-system-microservice",
    "type": "system:microservice",
    "docker": {
      "environment": {
        "user": "$ENV(my-username)",
        "password": "$SECRET(my-password)",
        "base_url": "$ENV(autoconnect-base_url)"
      }
    },
    "image": "jc89als/autoconnect:deltaStream",
    "port": 5000
  }

.. tip::

  - A Docker image differs from that of a Docker container in that an image is a template upon which an application can be run. A Docker container, is the isolated environment the application needs in order to run.  

.. seealso::

  :ref:`developer-guide` > :ref:`configuration` > :ref:`system_section` > :ref:`microservice_system`

  :ref:`sesam-community`

  `Sesam's community at GitHub <https://github.com/sesam-community>`_

  `Sesam's community at DockerHub <https://hub.docker.com/u/sesamcommunity>`_

.. _authentication-with-microservices-5-2:

Authentication with microservices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Docker hosting site login

Passing Env-vars/Secrets i Sesam

Oauth2 standard – Salesforce microservice

.. seealso::

  TODO

.. _microservices-sesam-input-output-5-2:

Micorservices in sesam and input/output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Common for sesams input & output

Sesam push/pull protocol

Sesam-json (formattering)

Lister av entiteter

query-parameter

url-parameter

is-first

is-last

.. seealso::

  TODO

.. _using-a-microservice-as-input-in-sesam-5-2:

Using a Microservice as Input in Sesam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Inside sesam

Best practise:

Delta/last seen

request-params

is-first

is-last

.. seealso::

  TODO

.. _looking-inside-an-input-microservice-5-2:

Looking inside an Input Microservice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  To look inside an input microservice...

  - you should only implement the minimum required code logic for Sesam to be able to consume data
  - you should remember that Sesam consumes and produces streams of entities
  - you should implement robust error handling and logging

In order to easily understand how an input microservice works in terms of code functionality, it is important that the microservice does not transform or reshape its source data too much. Keep in mind, Sesam ideally pulls in raw data and then starts to transform the data so that it aligns with the way in which Sesam enriches its data. In addition, by keeping data in its raw state as it enters Sesam, it makes it easier to understand how its source looks and it also retains schema information. Extending on this aspect of looking inside an input microservice, you will now learn about returning entities, streaming, and error handling and logging.

Returning entities
##################

Returning entities, with reference to the topic of looking inside an input microservice, comes down to the fact that you should only implement the minimum required code logic for Sesam to be able to consume data produced by a source system. As stated initially in this section, by retaining to the raw shape of your source data, our Sesam's data modelling approach can more easily be used to both enrich and maintain data integrity as entities are produced and transformed as these move through a Sesam node.   

Streaming
#########

Sesam consumes and produces streams of entities. An entity is very much like a JSON object and consists of a number of key-value pairs along with some special reserved property names. See the `entity data model <https://docs.sesam.io/entitymodel.html>`_ document for more details about entities.

The following is a quick example of the shape of entities that are consumed and exposed by Sesam.

.. code-block:: json

  [
      {
          "_id": "1",
          "name": "Bill",
          "dob": "01-01-1980"
      },
      {
          "_id": "2",
          "name": "Jane",
          "dob": "04-10-1992"
      }
  ]

Streams of entities flow through pipes. A pipe has an associated pump that is scheduled to regularly pull data entities from the source, push them through any transforms and send the results to the sink. The most common source is the `dataset source <https://docs.sesam.io/configuration.html#dataset-source>`_ which reads entities from a dataset. The most common sink is the `dataset sink <https://docs.sesam.io/configuration.html#dataset-sink>`_ which writes entities to a dataset. There are also `sources <https://docs.sesam.io/configuration.html#source-section>`_ and `sinks <https://docs.sesam.io/configuration.html#sink-section>`_ that can read and write data to and from external systems outside of Sesam.

Error handling & logging
########################

Error handling and logging are closely related topics and you should not do the one, without considering the other.

Error handling should be done in such a way that you make sure typical causes of error will be registered in your microservice. Typical causes of error often relates to status codes. A successful request returns a response code of 200, whilst an altogether unsuccessful one returns a response code of 404. If you consider the above two response codes as extremes, in terms of success, there are multiple additional response codes on this scale. These allow for incremental error handling.

Using the information returned from such a response is important and also here logging comes into play. Logging is used in a microservice so that a given user, especially a user not engaged technically in either response codes or code in itself, can explain and understand what made the microservice fail and/or why the microservice failed. Typically, severity in logging goes from logging of information to logging of warnings and finally to logging of errors. Naturally, you should make sure your microservice handles warnings and expecially errors in a robust and transparent way so that a given user will know what to do when such a logging entry occurs.    

.. seealso::

  :ref:`concepts` > :ref:`concepts-streaming`

  :ref:`developer-guide` > :ref:`configuration` > :ref:`source_section` > :ref:`dataset_source`

  :ref:`developer-guide` > :ref:`configuration` > :ref:`sink_section` > :ref:`dataset_sink`

.. _tasks-for-microservices-novice-5-2:

Tasks for Microservices: Novice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run a microservice in Sesam [could be sink, http, source]
