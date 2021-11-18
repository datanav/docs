.. _systems-beginner-2-1:

Beginner
--------

.. _what-is-a-system-in-sesam-2-1:

What is a system in Sesam?
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  A system in Sesam is a reusable interface to an external system outside of Sesam.

A system in Sesam is an interface that enables Sesam to communicate with the outside world.

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

.. seealso::

  :ref:`concepts` > :ref:`concepts-config` > :ref:`concepts-systems`

  :ref:`developer-guide` > :ref:`configuration` > :ref:`system_section`

.. _pipe-interaction-with-systems-2-1:

Pipe interaction with systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  Pipes use systems as:

  - ``source``
  - ``sink``
  - external transform

The systems defined inside Sesam do not do so much by themselves.
It is when they are used by pipes that data can start to flow.

There are three ways a pipe can interact with a system:

#. As a ``source`` for importing data into Sesam
#. As a ``sink`` to push data out from Sesam
#. As an external transform in a ``transform`` step to do intermediate processing


.. seealso::

  :ref:`concepts` > :ref:`concepts-config` > :ref:`concepts-pipes`

  :ref:`learn-sesam` > :ref:`architecture_and_concepts` > :ref:`architecture-and-concepts_beginner-1-1` > :ref:`pipes-1-1`

  :ref:`learn-sesam` > :ref:`dtl` > :ref:`dtl-beginner-3-1` > :ref:`pipes-where-dtl-executes-3-1`

.. _how-to-create-a-system-with-templates-2-1:

How to create a system with Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. TODO:
.. We should consider having a consistent example case to build on throughtout these chapters.

.. sidebar:: Summary

  - From **Systems** view: Click **New system**
  - Fill in ``_id``
  - Click **Templates**
  - Choose **System type**
  - Click **Replace**
  - Fill in any remaining details

Let us create a new system from scratch called "`difi`".
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
    "url_pattern": "https://ws.geonorge.no/kommuneinfo/v1/%s",
    "verify_ssl": true
  }

.. note::

  The ``%s`` at the end of the ``url_pattern`` will be substituted by
  the relative url specified in the pipes using this system as a source or sink.

Save the system config by clicking the **Save** button.

You can check the connectivity status by clicking the **Status** tab.

.. seealso::

  :ref:`developer-guide` > :ref:`configuration` > :ref:`system_section` > :ref:`url_system`

  :ref:`best-practices` > :ref:`best-practice` > :ref:`best-practice-naming-conventions`

  :ref:`learn-sesam` > :ref:`dtl` > :ref:`dtl-beginner-3-1` > :ref:`dtl-in-practice-3-1`


.. _environment-variables-secrets-2-1:

Environment variables & Secrets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  - Environment variables and secrets are named values used to parameterize configs
  - Environment variables are:

    - unencrypted
    - referenced with: ``"$ENV(my-env-var)"``

  - Secrets are:

    - encrypted
    - referenced with: ``"$SECRET(my-secret)"``

  - Both are defined under **Datahub > Variables**
  - Secrets can also be defined under a system's **Secrets** tab
  - Eases and improves config maintenance

In this section we will cover how environment variables and secrets typically
are used in system configs.

Environment variables and secrets are named values
that can be used to parameterize Sesam configs.

Environment variables are stored and processed as *unencrypted* values,
and are referenced with ``"$ENV(my-env-var)"``.

Secrets are stored and processed as *encrypted* values,
and are referenced with ``"$SECRET(my-secret)"``.

Both are defined in the Sesam Management Studio under **Datahub > Variables**.

Secrets can also be defined locally in a system config under the system's
**Secrets** tab.

.. warning::

  If a system config is deleted, all secrets stored locally in that system config is lost!

It is generally a good idea to put the parts of a configuration that differ between
environments (develop, test, production, etc.) into environment variables.
This includes configs such as server names, database connection strings, API URLs, usernames, etc.

By putting these config parts into environment variables you can define each of them
separately in each Sesam node used for the respective environments,
but keep the actual system config identical in each node.

This is also practical for version control of the config.
You can change the values of the environment variables separate from the actual
system config.

Continuing from the example :ref:`practice-system-config-initial`, let us see how the
introduction of environment variables can improve the system config.
The ``url_pattern`` is a good canditate to be put into an environment variable.
Let us call it `"difi-api"` and reference it from the system config.

First we define the new environment variable under
**Datahub > Variables > Environment variables**:

.. code-block:: json

  "difi-api": "https://ws.geonorge.no/kommuneinfo/v1/%s"

Then we change the system config to reference it:

.. _practice-system-config-env-var-ref:
.. code-block:: json
  :caption: Practice system config with environment variable reference
  :linenos:

  {
    "_id": "difi",
    "type": "system:url",
    "url_pattern": "$ENV(difi-api)",
    "verify_ssl": true
  }

Say we want to access different Difi APIs depending on which environment
we are accessing Difi from, or that Difi decided to change the API URL at some point.
The only thing that we have to update is the value of the ``difi-api``
environment variable.
No changes to the actual system config is required.

.. seealso::

  :ref:`concepts` > :ref:`concepts-config` > :ref:`concepts-environment-variables`

  :ref:`concepts` > :ref:`concepts-config` > :ref:`concepts-secrets`

.. _json-push-pull-protocol-2-1:

JSON Push & Pull protocol
~~~~~~~~~~~~~~~~~~~~~~~~~

See :ref:`json_pull_protocol` & :ref:`json_push_protocol`.

.. _tasks-for-systems-beginner-2-1:

Tasks for Systems: Beginner
~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. *What is a system in Sesam?*

#. *From where in the Sesam Management Studio can a new system be created?*

#. *What is a Sesam environment variable?*

#. *What is a Sesam secret?*

#. *Name some of the benefits of using environment variables in a system config?*

#. *Where are environment variables defined?*

#. *Where are secrets defined?*

#. *What is the difference between environment variables and secrets?*

#. *When should secrets be used instead of environment variables?*

#. *How are environment variables referenced in Sesam configs?*

#. *How are secrets referenced in Sesam configs?*
