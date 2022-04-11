.. _microservices_in_sesam:

======================
Microservices in Sesam
======================

Microservices in Sesam can be use to either add extra functionality or simply to set up connections to endpoints that require some extra logic. 
In this section we will show you some functionalities and details that may come handy when writing your own microservice for use in Sesam.


Passing variables to a microservice
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  
In Sesam there are three typical ways of passing variables from Sesam into a microservice: 

- By setting environmental variables directly to the Docker container in which the microservice runs. These are defined as docker specific parameters in the :ref:`microservice system configuration <microservice_system>`.
- Through `dynamic URL's <https://stackoverflow.com/questions/35107885/how-to-generate-dynamic-urls-in-flask>`_. An example of these can be seen in the tutorial :ref:`Custom Data Source - The Microservice System - Import data <tutorial_custom_data_source_microservice>`.
- Through the request parameters  in the :ref:`JSON pull <json_pull>` and :ref:`JSON push <json_push>` protocols.

Environmental variables are usually system specific varables, i.e. they are used throughout the whole microservice and not for a spesific endpoint. Example of these might be access tokens, base URL's or headers. 

Variables through dynamic URL's are generally pipe spesific variables that are only used for specific endpoints. These include variables such as endpoint URL's or entity data that are specific for that pipe.

The request parameters are set variables containing information about the the request and state of the pipe such as batch information and since values. 

Logs from a microservice
^^^^^^^^^^^^^^^^^^^^^^^^

The best way to display information from the microservice in Sesam is to set up logging statements inside the microservice (an example of this can be seen in line 30 in the microservice template above). These logs can later be viewed in the microservice system's **Status page**. You will also be able to see some error messages and full tracebacks in the **execution logs** of the pipes executing the microservice's routes. These messages can however be hard to read, and does not always log all the needed information.   

Memory awareness
^^^^^^^^^^^^^^^^

An other important concept to be aware of if memory usage of your microservices. This both entails the total memory of the Docker container in which the microservice runs as well as the required memory to GET and POST data to and from Sesam. You can yourself decide how much MB of RAM to allocate for a Docker container through the :ref:`Microservice system configuration <microservice_system>`, but be aware that Docker container memory usage could affect the whole Sesam instance if misused and should therefore be thoroughly considered before changed. 

For container size we advise to create as minimalistic containers as possible (especially when concidering container OS), and for the required memory when importing/exporting data we suggest to stream data directly to Sesam instead of storing it in the Docker container.  

The following streaming examples are available:

- `Simple OData <https://github.com/sesam-community/simple-odata>`_
- `rest-transform <https://github.com/sesam-community/rest-transform>`_
