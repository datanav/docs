.. _smtp_system:

SMTP system
-----------

The SMTP system represents the information needed to connect to a `SMTP <https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol>`_
server for sending emails. It is used in conjunction with the :ref:`mail message sink <mail_sink>` to construct
and send emails based on the entities it receives.

Prototype
^^^^^^^^^

::

    {
        "_id": "id-of-system",
        "name": "Name of system",
        "type": "system:smtp",
        "smtp_server": "localhost",
        "smtp_port": 25,
        "smtp_username": null,
        "smtp_password": null,
        "use_tls": false,
        "max_per_hour": 1000
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``smtp_server``
     - String
     - Contains a ``FQDN`` of the ``SMTP service`` to use
     - "localhost"
     -

   * - ``smtp_port``
     - Integer
     - The TCP port to use when talking to the ``SMTP service``
     - 25
     -

   * - ``smtp_username``
     - String
     - The username to use when authenticating with the ``SMTP service``. If not set, no authentication is attempted.
     -
     -

   * - ``smtp_password``
     - String
     - The password to use if ``smtp_username`` is set. It is mandatory if the ``smtp_username`` is provided.
     -
     - Yes

   * - ``use_tls``
     - Boolean
     - Indicating to the client to use ``TLS encryption`` when communicating with the ``SMTP service``.
     - false
     -

   * - ``max_per_hour``
     - Integer
     - The maximum number of messages to send for any hour. It is used for stopping run-away message sending in
       development or testing. Note that any message not sent will be logged but discarded.
     - 1000
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "our-smtp-server",
        "name": "Our SMTP Server",
        "type": "system:smtp",
        "smtp_server": "localhost",
        "smtp_port": 25,
        "smtp_username": "$ENV(username-variable)",
        "smtp_password": $SECRET(password-variable)
        "max_per_hour": 100000
    }

