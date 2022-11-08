.. _extensions-feature:

:badge:`Free feature,badge-success badge-pill`

Extensions
==========

Sesam provides a finite number of :ref:`systems <concepts-systems>`, but you can build and run your own microservice extension systems. The :ref:`microservice system <microservice_system>` allows you to use custom Docker images to host them inside the Sesam service.

Use case
========

Typically, writing a microservice extension is necessary when connecting to an API, which might not be readily available in the systems provided by Sesam. Have in mind that Sesam readily supports the use of :ref:`REST API's <rest_system>` in addition to hosting an open source `GitHub organization <https://github.com/sesam-community/>`_ which hosts multiple pre-built microservice extensions continously evolved and updated by project demand and experience.

.. tip::

    If you haven't already worked with microservice extensions and hosting via Docker, you should look at our guide on :ref:`Customize Extension Points <guide_customize_extension_points>` to try it out.
