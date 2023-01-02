============
Sesam Client
============

.. _concepts-sesam-client:

Introduction
============

The Sesam client is a command line tool for interacting with Sesam subscriptions.
It is great for testing configuration changes and for facilitating sync with source control systems.

The Sesam client is designed to help you test configuration changes before deploying them to production environments.
Its main features will help you to:

- Download configurations from Sesam subscriptions
- Upload configurations to Sesam subscriptions
- Simulate pipe runs from start to finish
- Compare outputs with expected outputs

The Sesam client is primarily intended for testing in personal Sesam subscriptions,
but its functionality also lends itself well to running tests in Sesam subscriptions dedicated to CI/CD automation.

The ease of uploading and downloading Sesam configurations and the fact that the configurations are serialized to JSON (no binary data) also enables smooth sync with source control systems.

.. note::

  Only one instance of the sesam client can run commands on a Sesam subscription at a time.

.. warning::

  Avoid manual changes to the Sesam subscription while the client is running as this will likely lead to undesired results.

.. warning::

  Do NOT run the Sesam client on production subscriptions! This is outside of its intended usage and may lead to very udesired results.

Pre-requisites
==============

- A personal Sesam subscription for testing
- A JWT (JSON Web Token) made available on the personal Sesam subscription

The URL to your Sesam subscription can be found beneath the subscription name inside your subscription.

.. image:: images/Node_ID.png
    :width: 800px
    :align: center
    :alt: DataSet

The JWT token can be generated inside your subscription under **Settings > Subscription > JWT** (see above).

To use the tool, follow the instructions in the `Sesam client README <https://github.com/sesam-community/sesam-py>`_.
