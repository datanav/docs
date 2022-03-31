.. _demo:

====
Demo
====

We have built a demo solution that showcases synchronization of organizational data between a Hubspot instance and various other services. It also shows how to use data from public data sources.

.. note::

  You can access a read only instance of the demo in your `dashboard <https://portal.sesam.io>`_. You can also set up your own demo instance by following the :ref:`Getting started guide <getting-started>`.


Hubspot companies
-----------------

The demo implements a bi-directional synchronization of the `companies in Hubspot <https://developers.hubspot.com/docs/api/crm/companies>`_ data.

The global model
----------------

The global model in the demo is a subset of the Hubspot model and contains mappings for the Hubspot properties that we want to manage with Sesam.

The other services
------------------

We have attached an accounting system `Wave <https://developer.waveapps.com/hc/en-us/articles/360019968212-API-Reference>`_ and an HR system `Freshteam by Freshworks <https://www.freshworks.com/hrms/>`_ that contains data that we want to map into our global model.

Public data sources
-------------------

The demo combines `company data from DBpedia <https://dbpedia.org/ontology/Company>`_, `legal entities from the Norwegian enhetsregisteret <https://en.wikipedia.org/wiki/Entity_Registry>`_ and more. Combining an English source and a Norwegian source shows how different languages play together in Sesam.

Multi-tenancy
-------------

The demo also contains a setup for handling multiple tenants in one subscription. The setup contains the shared data from the public data sources, and a generator that uses a configuration template in `global-config` to generate a configuration for each tenant defined in `global-customer`. These configurations are added as separate :ref:`config groups <concepts-configgroup>`. The configuration template uses a copy of the shared data for each tenant to keep the data isolated between the tenants.

The demo uses an :ref:`embedded source <embedded_source>` for both customers and the template to keep it simple. This can easily be extended to get the list of customers from an external source, as well as the template from an external version control system.
