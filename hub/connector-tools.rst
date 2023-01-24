===============
Connector Tools
===============

.. _concepts-connector-tools:

Introduction
============

Within the space of connector tools Sesam currently has a tool called the connector cli. The connector cli is a command line tool for interacting with Sesam subscriptions and is a companion tool for the :ref:`Sesam Client <concepts-sesam-client>`. It is great for generating templates from a manifest file which allows for you to automatically create :ref:`system <system_section>` and :ref:`collect <collect>` :ref:`pipe <pipe_section>` configuration files. This means that you can quickly generate configuration files regardless of your external data provider and that you can modify the configuration files easily with respect to the different datatypes you are working with. To allow for you to authorize to different external data providers the connector cli supports OAuth 2.0.

Pre-requisites
==============

To use the tool, follow the instructions in the `Connector CLI README <https://github.com/sesam-community/connector-cli>`_. Additionally, remember to add a ``.syncconfig`` file when `configuring the connector cli to work with the Sesam client <https://github.com/sesam-community/sesam-py#configuring>`_.