.. _systems-beginner-2-1:

Systems: Beginner
-----------------

.. _what-is-a-system-in-sesam-2-1:

What is a system in Sesam?
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. A system defines the connectors through which Sesam communicates with the outside world.

A system is an interface that enables Sesam to communicate with the outside world.

If you need Sesam to pull data from an external system,
you define that external system as a system config inside Sesam.

If you need Sesam to push data to an external system,
you define that external system as a system config inside Sesam.

When defining a system config in Sesam you usually specify a general connector
to the external system Sesam will interface with.

A typical example would be to specify user credentials and a connection string
when defining a system config to interface with an SQL database.
You would not specify which table to pull from or push to.
This would be specified in the pipe or pipes that would use the system.

By only specifying the general connector settings, Sesam is able to reuse the system config.

So if you need to let Sesam both pull data from and push data to a specific external system,
you would use the same system config for both, and handle the specifics in separate
pipe configs.

.. sidebar:: Summary

  - A Sesam system is a reusable interface to an external system outside of Sesam

.. seealso::

  Concepts - Configuration: :ref:`concepts-systems`

  Developer Guide - Service configuration: :ref:`system_section`

.. _introduction-to-sql-json-systems-2-1:

Introduction to SQL & JSON systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No such thing as a JSON system.

.. _pipe-interaction-with-systems.-2-1:

Pipe interaction with systems.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Input, output (mention transform?)

.. _how-to-create-a-system-with-templates-2-1:

How to create a system with Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let us create a new system from scratch called ``difi``.
In the Sesam Management Studio, navigate to the **Systems** view and follow these steps:

- Click the **New system** button
- Type in "`difi`" as the system's ``_id``
- In the **Templates** panel:

  - Choose System type: ``url prototype``
  - Click the **Replace** button to put the chosen system configuration into the system configuration area
  - Set ``url_pattern`` to "`https://ws.geonorge.no/kommuneinfo/v1/%s`"

You should now have the following system config:

.. _practice-system-config-initial:
.. code-block:: json
  :caption: Practice system config - initial
  :linenos:

  {
    "_id": "difi",
    "type": "system:url",
    "url_pattern": "https://ws.geonorge.no/kommuneinfo/v1/%s"
    "verify_ssl": true
  }

.. note::

  The ``%s`` at the end of the ``url_pattern`` will be substituted by
  the relative url specified in the pipes using this system as a source or sink.

Save the system config by clicking the **Save** button.

You can check the connectivity status by clicking the **Status** tab.

.. seealso::

  Developer Guide - Service Configuration: :ref:`url_system`

  DTL - Beginner: :ref:`dtl-in-practice-3-1`


.. _environment-variables-secrets-2-1:

Environment variables & Secrets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How are secrets stored in the backend? – Discuss with product

How do systems read secrets? Encrypted and decrypted in transmission or
passed as plain text?

$SECRET

$ENV

.. _json-push-pull-protocol-2-1:

JSON Push & Pull protocol
~~~~~~~~~~~~~~~~~~~~~~~~~

Lots of info in docs.

.. _tasks-for-systems-beginner-2-1:

Tasks for Systems: Beginner
~~~~~~~~~~~~~~~~~~~~~~~~~~~
