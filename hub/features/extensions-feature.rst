.. _extensions_feature:

:badge:`Free feature,badge-success badge-pill`

Extensions
==========

Sesam provides a finite number of :ref:`systems <concepts-systems>`, but you can build and run your own microservice extension systems. The :ref:`microservice system <microservice_system>` allows you to use custom Docker images to host them inside of the Sesam service.

Use case
========

Sesam readily supports the use of :ref:`REST API's <rest_system>` in addition to hosting an open source `GitHub organization <https://github.com/sesam-community/>`_ which has multiple pre-built microservice extensions that are continuously evolved and updated by project demand and experience. However if an API is not already supported by Sesam, then you may need to write a new microservice extension.

.. tip::

    If you haven't worked with microservice extensions and hosting via Docker, you should look at our guide on :ref:`Customize Extension Points <guide_customize_extension_points>` and try it out.
