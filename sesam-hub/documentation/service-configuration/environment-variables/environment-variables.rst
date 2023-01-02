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

Environment variables applies to both System and Pipe configuration entities.
