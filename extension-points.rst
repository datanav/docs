.. _developer_extension_points:

==========================
Developer Extension Points
==========================

There are many native Sesam components for collecting, transforming and using data. Sometimes however, there might be a need for :ref:`source <source_section>`, :ref:`transform <transform_section>` or :ref:`sink <sink_section>` customizations in order to cover all the needs.

To help in these situations there are well defined patterns and integration points that can be used.

There are two ways of customizing a connection to a Developer Extension Point:

- By using the :ref:`URL system <url_system>` to connect to an external endpoint that follows the :ref:`JSON pull protocol <json_pull>` or the :ref:`JSON push protocol <json_push>`
- By creating a microservice and connecting it to a :ref:`Microservice system <microservice_system>` 

These connections can be used to configure either a :ref:`custom data source <custom_data_source>`, a :ref:`custom transform <custom_data_transform>` or a :ref:`custom data sink <custom_data_sink>`.

Microservices are hosted in Sesam as docker containers. The Docker containers can be configured using
the :ref:`microservice system configuration <microservice_system>` and their logs can be inspected through the system's status tab.


    .. tip::

        As well as writing services from scratch there are also a number of starter service implementations that can be copied
        and changed. To read more about these connectors, or to contribute to the community, enter the the `Sesam community page <https://docs.sesam.io/community.html>`_.



.. rubric:: In this section:

.. toctree::
   :maxdepth: 1

   Custom Data Sources <custom-data-source>
   Custom Data Transforms <custom-data-transform>
   Custom Data Sinks <custom-data-sink>
   Microservices in Sesam <microservices-in-sesam>