.. _twilio_system:

Twilio system
-------------

The `Twilio <https://en.wikipedia.org/wiki/Twilio>`_ system is a ``SMS system`` used with
:ref:`SMS message sinks <sms_sink>` to construct and send SMS messages from entities.

It has the following properties:

Prototype
^^^^^^^^^

::

    {
        "_id": "system-id",
        "name": "Service name",
        "type": "system:twilio",
        "account": "$ENV(account-number-variable)",
        "token": "$SECRET(twilio-api-token-variable)",
        "max_per_hour": 1000,
        "proxy":  "socks5://user:password@socksproxy:1234"
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

   * - ``account``
     - String
     - The ``Twilio`` account number
     -
     - Yes

   * - ``token``
     - String
     - The ``Twilio`` API token
     -
     - Yes

   * - ``max_per_hour``
     - Integer
     - The maximum number of messages to send for any hour. It is used for stopping run-away message sending in
       development or testing. Note that any message not sent will be logged but discarded.
     - 1000
     -

   * - ``proxy``
     - String
     - A optional property that specifies a SOCKS5 proxy for the system. If authentication is used, the embedded
       username and passord should be put into system secrets, i.e. ``$SECRET(username):$SECRET(password)@..``.
     -
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
         "_id": "twilio_service",
         "name": "Twilio Service",
         "type": "system:twilio",
         "account": "$ENV(account-number-variable)",
         "token": "$SECRET(twilio-api-token-variable)",
         "max_per_hour": 100000
    }

