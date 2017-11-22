=============
Notifications
=============

.. contents:: Table of Contents
   :depth: 2
   :local:


Introduction
============

SESAM lets uses specifiy "notification rules" that will trigger alerts when certain
conditions occur.

When a notification rule triggers, the user(s) get notified in the GUI and optionally by email.

Notification rules are added on the "Notifications" tab on the "Pipe"-page in the GUI.


Pump completed / Pump failed notification rules
===============================================

What can be monitored?
----------------------
When a pipe has finished running (either because it has finished normally, or if some error has occured),
it will log some key numbers about the pipe-run.

A notification rule can be added for each of these values, so that the user is alerted if a value
is too high or too low.


.. _pipe_completed_metric__entities_last_run:
Entities processed
~~~~~~~~~~~~~~~~~~
This is the total number of entities that was read from the pipe's source.


.. _pipe_completed_metric__changes_last_run:

Changed entities
~~~~~~~~~~~~~~~~
This is the number or entities that was actually changed. When writing an entity to a dataset, the
pipe will compare the new entity to the version of entity that is already in the dataset (if any). If
the entity is already in the dataset and is identical to the new entity, the new entity is skipped.


.. _pipe_completed_metric__number_of_failed_retries_last_run:

Failed retries
~~~~~~~~~~~~~~
This is the number of entities that was unsuccessfully retried. The pipe will retry these entities again the next
time the pipe runs..


.. _pipe_completed_metric__number_of_dead_entities_last_run:

Dead entities
~~~~~~~~~~~~~
This is the number of entities that the pipe unsuccessfully retried writing to the sink, and where the pipe
has retried so many times that the pipe has permanently given up on the entities.

.. _pipe_completed_metric__retry_errors_last_run:

Failed retried entities
~~~~~~~~~~~~~~~~~~~~~~~
This is the total number of failed retry attempts. This number is the sum of the
:ref:`Failed retries <pipe_completed_metric__number_of_failed_retries_last_run>`
and :ref:`Dead entities <pipe_completed_metric__number_of_dead_entities_last_run>` properties.


.. _pipe_completed_metric__retries_succeeded_last_run:

Successfully retried entities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is the number of entities that was retried, and where the retry attempt succeeded.

.. _pipe_completed_metric__read_errors_last_run:

Read errors
~~~~~~~~~~~
This is the number of time the pipe failed to read entities from the source.


.. _pipe_completed_metric__write_errors_last_run:

Write errors
~~~~~~~~~~~~
This is the number of times the pipe failed to write entities to the sink.


.. _pipe_completed_metric__sink_time:

Sink time
~~~~~~~~~
This is the number of seconds the pipe spent writing to the sink.

.. _pipe_completed_metric__source_time:

Source time
~~~~~~~~~~~
This is the number of seconds the pipe spent reading from the source.

.. _pipe_completed_metric__transform_time:

Transform time
~~~~~~~~~~~~~~
This is the number of seconds the pipe spent doing DTL and other types for transforms.


.. _pipe_completed_property__original_error_message:

Underlying error
~~~~~~~~~~~~~~~~

When a pipe-run fails, this value contains an error message that describes the root cause of the error.
This is the error-message that is displayed on the pipe's "Status" tab.

Since this is not a numeric value, it cannot be used with the "Value too high/low" rule types. It
is intented to be used with the :ref:`Pattern match <pump_completed_pattern_match_notification_rule>` rule.

Example::

   requests.exceptions.ConnectionError: HTTPConnectionPool(host='testsystem', port=9999): Max retries exceeded with url: /sludder (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x7f12b7aaa518>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution',))


Underlying traceback
~~~~~~~~~~~~~~~~~~~~

When a pipe-run fails, this value contains the full stacktrace of the error.

Since this is not a numeric value, it cannot be used with the "Value too high/low" rule types. It
is intented to be used with the :ref:`Pattern match <pump_completed_pattern_match_notification_rule>` rule.

Tip: It is usually better to use the :ref:`Underlying error <pipe_completed_property__original_error_message>` value
instead, since that is less verbose while still usually containing the relevant error-message.

Example::

   Traceback (most recent call last):\n  File \"/usr/local/lib/python3.6/dist-packages/requests/packages/urllib3/connection.py\", line 142, in _new_conn\n    (self.host, self.port), self.timeout, **extra_kw)\n  File \"/usr/local/lib/python3.6/dist-packages/requests/packages/urllib3/util/connection.py\", line 67, in create_connection\n    for res in socket.getaddrinfo(host, port, 0, socket.SOCK_STREAM):\n  File \"/usr/lib/python3.6/socket.py\", line 745, in getaddrinfo\n    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):\nsocket.gaierror: [Errno -3] Temporary failure in name resolution\n\nDuring handling of the above exception, another exception occurred:\nTraceback (most recent call last):\n  File \"/usr/local/lib/python3.6/dist-packages/requests/packages/urllib3/connectionpool.py\", line 578, in urlopen\n    chunked=chunked)\n  File \"/usr/local/lib/python3.6/dist-packages/requests/packages/urllib3/connectionpool.py\", line 362, in _make_request\n    conn.request(method, url, **httplib_request_kw)\n  File \"/usr/lib/python3.6/http/client.py\", line 1239, in request\n    self._send_request(method, url, body, headers, encode_chunked)\n  File \"/usr/lib/python3.6/http/client.py\", line 1285, in _send_request\n    self.endheaders(body, encode_chunked=encode_chunked)\n  File \"/usr/lib/python3.6/http/client.py\", line 1234, in endheaders\n    self._send_output(message_body, encode_chunked=encode_chunked)\n  File \"/usr/lib/python3.6/http/client.py\", line 1026, in _send_output\n    self.send(msg)\n  File \"/usr/lib/python3.6/http/client.py\", line 964, in send\n    self.connect()\n  File \"/usr/local/lib/python3.6/dist-packages/requests/packages/urllib3/connection.py\", line 167, in connect\n    conn = self._new_conn()\n  File \"/usr/local/lib/python3.6/dist-packages/requests/packages/urllib3/connection.py\", line 151, in _new_conn\n    self, \"Failed to establish a new connection: %s\" % e)\nrequests.packages.urllib3.exceptions.NewConnectionError: <requests.packages.urllib3.connection.HTTPConnection object at 0x7f12b7a954a8>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution\n\nDuring handling of the above exception, another exception occurred:\nTraceback (most recent call last):\n  File \"/usr/local/lib/python3.6/dist-packages/requests/adapters.py\", line 403, in send\n    timeout=timeout\n  File \"/usr/local/lib/python3.6/dist-packages/requests/packages/urllib3/connectionpool.py\", line 623, in urlopen\n    _stacktrace=sys.exc_info()[2])\n  File \"/usr/local/lib/python3.6/dist-packages/requests/packages/urllib3/util/retry.py\", line 281, in increment\n    raise MaxRetryError(_pool, url, error or ResponseError(cause))\nrequests.packages.urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='testsystem', port=9999): Max retries exceeded with url: /sludder (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x7f12b7a954a8>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution',))\n\nDuring handling of the above exception, another exception occurred:\nTraceback (most recent call last):\n  File \"/usr/local/lib/python3.6/dist-packages/lake/sources/json.py\", line 31, in getEntities\n    with self.system.getStream(session, absolute_url, params=params) as stream:\n  File \"/usr/local/lib/python3.6/dist-packages/lake/systems/url.py\", line 189, in getStream\n    session=session, url=url, params=params, headers=headers)\n  File \"/usr/local/lib/python3.6/dist-packages/lake/systems/url.py\", line 182, in getStreamAndContentLength\n    r, content_length = self.getRequestAndContentLength(session, url, params=params, headers=headers)\n  File \"/usr/local/lib/python3.6/dist-packages/lake/systems/url.py\", line 160, in getRequestAndContentLength\n    verify=self.verify_ssl, timeout=self.timeout)\n  File \"/usr/local/lib/python3.6/dist-packages/requests/sessions.py\", line 487, in get\n    return self.request('GET', url, **kwargs)\n  File \"/usr/local/lib/python3.6/dist-packages/requests/sessions.py\", line 475, in request\n    resp = self.send(prep, **send_kwargs)\n  File \"/usr/local/lib/python3.6/dist-packages/requests/sessions.py\", line 585, in send\n    r = adapter.send(request, **kwargs)\n  File \"/usr/local/lib/python3.6/dist-packages/requests/adapters.py\", line 467, in send\n    raise ConnectionError(e, request=request)\nrequests.exceptions.ConnectionError: HTTPConnectionPool(host='testsystem', port=9999): Max retries exceeded with url: /sludder (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x7f12b7a954a8>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution',))


How can it be monitored?
------------------------

Each of the metric described above can be monitored in a number of different ways.

.. _pump_completed_value_too_low_notification_rule:
Value too low
~~~~~~~~~~~~~
This rule type triggers a notification if a metric was below a specified value.

.. _pump_completed_value_too_high_notification_rule:
Value too high
~~~~~~~~~~~~~~
This rule type triggers a notification if a metric was above a specified value.


.. _pump_completed_value_too_low_over_time_notification_rule:
Value too low over time
~~~~~~~~~~~~~~~~~~~~~~~
This rule type triggers a notification if a metric has been below a specified value for a
specified period of time.

.. _pump_completed_value_too_high_over_time_notification_rule:
Value too high over time
~~~~~~~~~~~~~~~~~~~~~~~~
This rule type triggers a notification if a metric has been above a specified value for a
specified period of time.


.. _pump_started_overdue_notification_rule:
Pump started overdue
====================

The purpose of this rule type is to alert the user if a pipe hasn't started running by the
time it is supposed to.

When a pipe starts to run, the next expected starttime is calculated based on the pipe's
:ref:`schedule interval<pump_param_schedule_interval>` or :ref:`cron expression<pump_param_cron_expression>`
configuration setting.

When the pipe finishes running, the next expected starttime is calculated again.

If the current expected starttime is ever reached without the pipe having started again, an alert
is generated.


.. _pump_completed_pattern_match_notification_rule:

Pattern match
=============

The purpose of this rule type is to alert the user if a pipe has failed with a specific error-message.

The user can specify which value to examine, but the most common use case is the
:ref:`Underlying error <pipe_completed_property__original_error_message>` value.

The pattern supports the "\*" and "?" wildcard characters. "\*" matches any number of characters.
"?" matches one single character.

Example:
If the "Underlying error" looks like this::

   requests.exceptions.ConnectionError: HTTPConnectionPool(host='testsystem', port=9999): Max retries exceeded with url: /sludder (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x7f12b7b32550>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution',))

appropriate patterns to use to match this error could be::

   Failed to establish a new connection

or::

   Temporary failure in name resolution

or::

   Failed to establish a new connection*name resolution

, depending on which part(s) of the errormessage the user is interested in.

Note that there is no need for wildcards at the start and/or end of the patterns; if the pattern matches
*anywhere* in the value the notification-rule will trigger.


Alert rate limiting
===================

To avoid flooding users with alert, each notification rule will only generate at most one alert
per hour. If the notification rule triggered more than once during that hour, the alert-message
will say something like this::

    "First occurrence: 2017-11-16 09:53:16. This event has triggered
    an additional 215 times after the first occurrence. The last time
    it triggered was 2017-11-16 11:40:57."
