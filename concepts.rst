Concepts
========
The overall data landscape is constantly evolving. With this evolution follows a vast collection of concepts and definitions that may deviate between frameworks or genres. 
Unless we can define exactly what a concept means in specific situation misunderstandings are bound to happen.

In this section we will explain the most central concepts used in Sesam. Many of these concepts exists outside Sesam too, but perhaps with slightly different functionalities. 

.. _whatis-namespaces:

Namespaces
----------
In Semantic web technologies, namespaces are URL references that allows us to reuse names from different sources without loosing context. If you wish to point to different Wikipedia URI's you could define the Wikipedia base URL with the namespace ``wiki = https://en.wikipedia.org/wiki/`` and then refer to any Wikipedia URI as ``wiki:<element>``.

In Sesam, namespaces are used to identify the origin of an attribute. Quite often we wish to merge entities with other similar entities, such as person data from a CRM system and the equivalent person data from an HR system. Sesam prefixes namespaces to each attribute name in order to merge data from multiple sources without losing contex. With some exceptions, attributes will always inherit the pipe name where the attribute was first created as its namespace, i.e. an attribute ``x`` created in pipe ``y`` will become ``x:y``. 

See examples below.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Pipe name
     - Attribute from source
     - Attribute with namespace
   * - hubspot-person
     - name
     - hubspot-person:name
   * - visma-person
     - name
     - visma-person:name
   * - hubspot-company
     - company_name
     - hubspot-company:company_name  
   * - visma-company
     - company_name
     - visma-company:company_name

Example of a Sesam entity with namespaces:

.. code-block:: json

  {
    "_id": "user:123",
    "user:username": "erica",
    "user:first_name": "Erica",
    "user:manager": "~:user:101"
  }

Not that in the entity example above, the ``_id`` property do not retain a namespace, but the value does. This is an exception as the ``_id`` is the property Sesam uses as a unique identifier. 

  .. important::

   Namespaces are not to be confused with :ref:`namespaced identifiers <ni_dtl_function>`. A namespaced identifier, as seen as the value for ``"user:manager"`` in the example above, is the result of an internal Sesam transformation needed for the :ref:` integrated search <integrated-search>`concept.  

.. _whatis-global:

Global
------

A global is a collection of merged datatypes within the same data domain. I.e. customer data, lead data and partner data could all be gathered into a ``global-organization`` dataset which would contain all the data from the organization domain within the enterprise. Similarily ``global-person`` would contain all person domain data and ``global-asset`` all the asset domain data. A global also allows us to map datatypes into global properties, as defined in the global namespace, through *Master Data Management (MDM)*. These global properties are Sesam's equivalent to *golden records*. 

In addition to creating a context in which MDM may be performed, globals comes with several other advantages such as: 

- Making all domain specific data easily visible
- Making all domain specific data easily accessible
- Centralized maintenance

.. _whatis-global-model:

Global model
------------

A global model is the collection of globals and their global properties as defined in the global namespace. There is no clear upper limit to how many globals a global model can contain as long as each global define a clear and appropriate domain.

Most global models contains some or all of the following globals:

- global-person
- global-organization
- global-asset
- global-task
- global-project
- global-document

.. _whatis-datatype:

Datatype
--------

Datatypes typically represents one concept within a system, e.g. customers in a CRM system. A global consists of datatypes from the same data domain.

Typical datatypes for the global ``global-person`` are:

- person
- user
- employee  

.. _whatis-connector:

Connector
---------

A connector is the collection of components required to synchronize one or more datatypes to a system. This synchronization can either be from the outside into Sesam or from Sesam to the outside. Sesam provides a list of built-in connectors to some of the most :doc:`common sources <configuration-systems>`, such as :doc:`SQL <configuration-systems-sql>` or :doc:`rest API's <configuration-systems-rest>`. Sesam also provides a set of :doc:`developer extension points <extension-points>` to which you can build your own connector inside a microservice for extra functionality. 

