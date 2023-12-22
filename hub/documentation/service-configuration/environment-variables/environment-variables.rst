.. _environment_variables:

Environment variables
=====================

You can insert the values of environment variables into configuration using the syntax "$ENV(variable)" in place of
property values. You can manage these environment variables using a HTTP client with the :ref:`Environment Manager API <api-reference>`.

An example, given a uploaded environment variable JSON file containing:

::

    {
       "server-ip": "10.10.10.1"
    }


You can refer to this property in your configuration by reference:

::

    {
       "_id": "my-system",
       "type": "oracle",
       "host": "$ENV(server-ip)"
       ..
    }

You can also compose a property that consists of several environment variables:

::

   {
     "_id": "my-system",
     "type": "url",
     "base_url": "http://$ENV(my-domain):$ENV(my-port)",
     "..": ".."
   }

Note that when using properties that contain multiple environment variables you cannot nest them inside each other,
and the resulting property will always be a string.

You can combine environment variables and *secrets*, but they cannot be nested within each other. For secret variables
see the :ref:`Secrets manager API <secrets_manager>` for details on how to upload them and their syntax.

Environment variables applies to System, Pipe and service metadata configuration entities.

.. _conditional_properties:

Conditional properties
======================

A more complex way of conditionally setting property values can be achieved by using *conditional properties*.
This construct is supported by the System, Pipe and service metadata entities and can be used to set
one or more configuration property depending on a certain condition (typically set by an environment variable).

Example:

::

   {
      "_id": "test-system",
      "$conditional_properties": {
         "condition": "$ENV(environment)",
         "alternatives": {
           "production": {
              "proxies": {
                  "http": "socks5://mysocksproxy:1234",
                  "https": "socks5://user:password@mysslsocksproxy:1234",
              },
              "connect_timeout": 60,
              "read_timeout": 1800
           },
           "test": {
              "connect_timeout": 300
              "verify_ssl": false
              "url_pattern": "http://test.example.org/test/%s"
           }
      },
      "url_pattern": "http://example.org/test/%s"
   }

Note that conditional properties will *replace* any property set at the same level as the conditional block. In the above example,
the ``url_pattern`` property value will be overwritten by the value in the ``test`` conditional block if the condition
value evaluates to ``"test"``. Note that there is no merge semantics if the conditional property is an object and it
also exists on same level in the configuration entity; if you need to conditionally define only a subset of the original
configuration property object you should instead insert one or more conditional properties within this object.

It is possible to nest conditional properties within another conditional property and it can be placed at any level in
the configuration entity (but note the limitations below). Each conditional block are applied at the same level as where
the conditional properties are defined.

Note that there are some limitations to where the conditional property construct can be used:

 * The ``_id`` or ``type`` properties on the root level of a configuration entity can not be set in a
   conditional block
 * Transforms or embedded data do not support conditional properties
