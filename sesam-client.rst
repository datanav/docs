============
Sesam Client
============

.. _concepts-sesam-client:

Introduction
============

The Sesam client is a command line tool for interacting with a Sesam service instance (node).
It is great for testing node configuration changes and for facilitating sync with source control systems.

When working on projects it is important to test configuration changes before deploying to production environments.
The Sesam client is designed specifically to ease this operation by having functionality to both upload and download complete configurations to and from a Sesam node,
and also do pipe run simulations from start to finish and compare outputs with expected outputs.

The Sesam client is primarily intended for testing in private Sesam nodes, but its functionality also lends itself well to running tests in Sesam nodes dedicated to CI/CD automation.

The ease of uploading and downloading Sesam configurations and the fact that the configurations are serialized to JSON (no binary data) also enables smooth sync with source control systems.

.. note::

  Only one instance of the sesam client can run commands on a sesam node at a time.

.. warning::

  Avoid manual changes to the Sesam node while the client is running as this will likely lead to undesired results.

.. warning::

  DO NOT run the Sesam client on production nodes! This is outside of its intended usage and may lead to very udesired results.

Pre-requisites
==============

- A personal Sesam node for testing
- A `JWT <https://docs.sesam.io/getting-started.html#json-web-tokens>`__  (JSON Web Token) made available on the personal Sesam node

The "node-id" of your private Sesam node can be found between the node name and the "Overview" link inside your node.

.. image:: images/Node_ID.png
    :width: 800px
    :align: center
    :alt: DataSet

The JWT token can be generated inside your private node under **Settings > Subscription > JWT** (see above).

To use the tool, follow the instructions in the `Sesam client README <https://github.com/sesam-community/sesam-py>`_.
