===============
Connector Tools
===============

.. _concepts-connector-tools:

Introduction
============

Within the space of connector tools the :ref:`Sesam Client <concepts-sesam-client>` provides a set of commands that allow developers to work on connectors, by helping generate templates from a manifest file. This allows for you to automatically create :ref:`system <system_section>` and :ref:`pipe <pipe_section>` configuration files. This means that you can quickly generate configuration files regardless of your external data provider and that you can modify the configuration files easily with respect to the different datatypes you are working on. 

To create configuration files an ``expand`` command is run when doing ``sesam upload`` whereas running ``sesam download`` a subsequent ``collapse`` command runs to reflect your configuration file changes locally.

To allow for you to authorize to different external data providers OAuth 2.0 has been implemented as part of this workflow. This happens automatically when using the Sesam Client, albeit to run the authorisation explicitly you should use ``sesam authenticate``.

Pre-requisites
==============

To use the tool, follow the instructions in the `Sesam Client README <https://github.com/sesam-community/sesam-py/blob/master/readme.usage.md>`_.