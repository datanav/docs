Concepts
========
The overall data landscape is constantly evolving. With this evolution follows a vast collection of concepts and definitions that may deviate between frameworks or genres. 
Unless we can define exactly what a concept means in specific situation misunderstandings are bound to happen.

In this section we will explain the most central concepts used in Sesam. Many of these concepts exists outside Sesam too, but perhaps with slightly different functionalities. 

.. _whatis-namespaces:

Namespaces
----------
In Semantic web technologies, namespaces are URL references that allows us to reuse names from different sources without loosing context. If you wish to point to different Wikipedia URI's you could define the Wikipedia base URL with the namespace ``wiki = https://en.wikipedia.org/wiki/`` and then refer to any Wikipedia URI as ``wiki:<element>``.

In Sesam, namespaces are used to identify the source of an attribute. Quite often we wish to merge entities with other similar entities, such as person data from a CRM system and the equivalent person data from an HR system. Sesam prefixes namespaces to each attribute name in order to merge data from multiple sources without losing contex, i.e. the attribute ``name`` becomes ``crm-person:name`` and ``hr-person:name``.  

.. _whatis-global:

Global
------

A global is a collection of merged datatypes within the same data domain. I.e. customer data, lead data and partner data could all be gathered into a ``global-organization`` dataset which would contain all the data from the organization domain within the enterprice. Similarily ``global-person`` would contain all person domain data and ``global-asset`` all the asset domain data. A global also allows us to map datatypes into global properties, as defined in the global namespace, through *Master Data Management*. These global properties are Sesam's equivilent to *golden records*.  

.. _whatis-global-model:

Global model
------------

A global model is the collection of globals and their global properties as defined in the global namespace.

.. _whatis-datatype:

Datatype
--------

Datatypes typically represents one concept within a system, e.g. customers in a CRM system. A global consists of datatypes from the same data domain.  

.. _whatis-connector:

Connector
---------

A connector is the collection of components required to synchronize one or more datatypes to a system.

