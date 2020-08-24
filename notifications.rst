=============
Notifications
=============

.. contents:: Table of Contents
   :depth: 2
   :local:


Introduction
============

SESAM lets users specify "notification rules" that will trigger alerts when certain
conditions occur.

When a notification rule triggers, the user(s) get notified in the GUI and optionally by email.

Notification rules are added under the "Notifications" tab on the "Pipe"-page in the GUI.


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

.. _pipe_completed_property__reason_why_stopped:

Reason why stopped
~~~~~~~~~~~~~~~~~~

When a pipe-run fails, this value contains an error message that describes the problem.

Since this is not a numeric value, it cannot be used with the "Value too high/low" rule types. It
is intended to be used with the :ref:`Pattern match <pump_completed_pattern_match_notification_rule>` rule.

Example::

   requests.exceptions.ConnectionError: HTTPConnectionPool(host='testsystem', port=9999): Max retries exceeded with url: /sludder (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x7f12b7aaa518>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution',))


.. _pipe_completed_property__traceback:

Traceback
~~~~~~~~~

When a pipe-run fails, this value contains the stacktrace of the error.

Since this is not a numeric value, it cannot be used with the "Value too high/low" rule types. It
is intended to be used with the :ref:`Pattern match <pump_completed_pattern_match_notification_rule>` rule.

Tip: It is usually better to use the :ref:`Reason why stopped <pipe_completed_property__reason_why_stopped>` value
instead, since that is less verbose while still usually containing the relevant error-message.

Example::

   Traceback (most recent call last):\n  File \"/usr/local/lib/python3.6/dist-packages/requests/packages/urllib3/connection.py\", line 142, in _new_conn\n    (self.host, self.port), self.timeout, **extra_kw)\n  File \"/usr/local/lib/python3.6/dist-packages/requests/packages/urllib3/util/connection.py\", line 67, in create_connection\n    for res in socket.getaddrinfo(host, port, 0, socket.SOCK_STREAM):\n  File \"/usr/lib/python3.6/socket.py\", line 745, in getaddrinfo\n    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):\nsocket.gaierror: [Errno -3] Temporary failure in name resolution\n\nDuring handling of the above exception, another exception occurred:\nTraceback (most recent call last):\n  File \"/usr/local/lib/python3.6/dist-packages/requests/packages/urllib3/connectionpool.py\", line 578, in urlopen\n    chunked=chunked)\n  File \"/usr/local/lib/python3.6/dist-packages/requests/packages/urllib3/connectionpool.py\", line 362, in _make_request\n    conn.request(method, url, **httplib_request_kw)\n  File \"/usr/lib/python3.6/http/client.py\", line 1239, in request\n    self._send_request(method, url, body, headers, encode_chunked)\n  File \"/usr/lib/python3.6/http/client.py\", line 1285, in _send_request\n    self.endheaders(body, encode_chunked=encode_chunked)\n  File \"/usr/lib/python3.6/http/client.py\", line 1234, in endheaders\n    self._send_output(message_body, encode_chunked=encode_chunked)\n  File \"/usr/lib/python3.6/http/client.py\", line 1026, in _send_output\n    self.send(msg)\n  File \"/usr/lib/python3.6/http/client.py\", line 964, in send\n    self.connect()\n  File \"/usr/local/lib/python3.6/dist-packages/requests/packages/urllib3/connection.py\", line 167, in connect\n    conn = self._new_conn()\n  File \"/usr/local/lib/python3.6/dist-packages/requests/packages/urllib3/connection.py\", line 151, in _new_conn\n    self, \"Failed to establish a new connection: %s\" % e)\nrequests.packages.urllib3.exceptions.NewConnectionError: <requests.packages.urllib3.connection.HTTPConnection object at 0x7f12b7a954a8>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution\n\nDuring handling of the above exception, another exception occurred:\nTraceback (most recent call last):\n  File \"/usr/local/lib/python3.6/dist-packages/requests/adapters.py\", line 403, in send\n    timeout=timeout\n  File \"/usr/local/lib/python3.6/dist-packages/requests/packages/urllib3/connectionpool.py\", line 623, in urlopen\n    _stacktrace=sys.exc_info()[2])\n  File \"/usr/local/lib/python3.6/dist-packages/requests/packages/urllib3/util/retry.py\", line 281, in increment\n    raise MaxRetryError(_pool, url, error or ResponseError(cause))\nrequests.packages.urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='testsystem', port=9999): Max retries exceeded with url: /sludder (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x7f12b7a954a8>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution',))\n\nDuring handling of the above exception, another exception occurred:\nTraceback (most recent call last):\n  File \"/usr/local/lib/python3.6/dist-packages/lake/sources/json.py\", line 31, in getEntities\n    with self.system.getStream(session, absolute_url, params=params) as stream:\n  File \"/usr/local/lib/python3.6/dist-packages/lake/systems/url.py\", line 189, in getStream\n    session=session, url=url, params=params, headers=headers)\n  File \"/usr/local/lib/python3.6/dist-packages/lake/systems/url.py\", line 182, in getStreamAndContentLength\n    r, content_length = self.getRequestAndContentLength(session, url, params=params, headers=headers)\n  File \"/usr/local/lib/python3.6/dist-packages/lake/systems/url.py\", line 160, in getRequestAndContentLength\n    verify=self.verify_ssl, timeout=self.timeout)\n  File \"/usr/local/lib/python3.6/dist-packages/requests/sessions.py\", line 487, in get\n    return self.request('GET', url, **kwargs)\n  File \"/usr/local/lib/python3.6/dist-packages/requests/sessions.py\", line 475, in request\n    resp = self.send(prep, **send_kwargs)\n  File \"/usr/local/lib/python3.6/dist-packages/requests/sessions.py\", line 585, in send\n    r = adapter.send(request, **kwargs)\n  File \"/usr/local/lib/python3.6/dist-packages/requests/adapters.py\", line 467, in send\n    raise ConnectionError(e, request=request)\nrequests.exceptions.ConnectionError: HTTPConnectionPool(host='testsystem', port=9999): Max retries exceeded with url: /sludder (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x7f12b7a954a8>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution',))







.. _pipe_completed_property__original_error_message:

Additional low-level errormessage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a pipe-run fails, this value can in some cases contain an additional
low-level description of what went wrong. Note: If no additional information is available, this
property will be empty.

Since this is not a numeric value, it cannot be used with the "Value too high/low" rule types. It
is intended to be used with the :ref:`Pattern match <pump_completed_pattern_match_notification_rule>` rule.


Additional low-level traceback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a pipe-run fails, this value can in some cases contain an additional low-level stacktrace of the
error. Note: If no additional information is available, this value will be empty.

Since this is not a numeric value, it cannot be used with the "Value too high/low" rule types. It
is intended to be used with the :ref:`Pattern match <pump_completed_pattern_match_notification_rule>` rule.

Tip: It is usually better to use the :ref:`Additional low-level errormessage <pipe_completed_property__original_error_message>` value
instead of this value, since that is less verbose while still usually containing the relevant error-message.


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

If the current expected starttime is passed by more than 5 minutes without the pipe having started again, an alert
is generated.

The "Grace period" parameter can be used to extend the timeout by specifying an addition number
of seconds the pipe-run can be overdue. The number of seconds in the "Grace period" parameter is added to the
'built-in' grace-period of 300 seconds.

.. _pump_finished_overdue_notification_rule:

Pump finished overdue
=====================

The purpose of this rule type is to alert the user if a pipe hasn't finished running by the
time it is supposed to.

The "Limit" parameter specified the number of seconds that the pipe is allowed to run before an alert is generated.
The number of seconds in the "Limit" parameter is added to the 'built-in' limit of 300 seconds.


.. _pump_failed_notification_rule:

Pump failed
===========

This ruletype checks if the pipe failed the last time it ran, for any reason.

If more control of when the notification rule triggers is needed, the
:ref:`Pattern match <pump_completed_pattern_match_notification_rule>` rule can be used instead.

.. _restore_completed_notification_rule:

Restore completed
=================

This ruletype triggers when the pipe and its associated state and data has been restored from backup. This can happen
if the machine the pipe is running on has failed for some reason; in this case the pipe's state and data might
be restored from a remote backup. After a restore the pipe will be in the state it was when the backup was made,
which means data might be reprocessed.

See also the :ref:`Pump offset set <pump_offset_set_notification_rule>` notification rule.

.. _pump_offset_set_notification_rule:

Pump offset set
===============

This ruletype triggers when the pipe's offset has been set for any reason. The offset can be set manually by a
user (for instance by resetting the pipe), or automatically if the pipe detects that something has happened to
the upstream pipes that requires the pipe's offset to be modified.

A typical usecase is that an upstream pipe has been restored from backup; in this case the pipe's offset may be
rewound to match the max offset of the restored upstread pipe.

See also the :ref:`Restore completed <restore_completed_notification_rule>` notification rule.


.. _pump_completed_pattern_match_notification_rule:

Pattern match
=============

The purpose of this rule type is to alert the user if a pipe has failed with a specific error-message.

The user can specify which value to examine, but the most common use case is the
:ref:`Reason why stopped <pipe_completed_property__reason_why_stopped>` value.

The pattern supports the "\*" and "?" wildcard characters. "\*" matches any number of characters.
"?" matches one single character.

Example:
If the "Reason why stopped" looks like this::

   requests.exceptions.ConnectionError: HTTPConnectionPool(host='testsystem', port=9999): Max retries exceeded with url: /sludder (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x7f12b7b32550>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution',))

appropriate patterns to use to match this error could be::

   Failed to establish a new connection

or::

   Temporary failure in name resolution

or::

   Failed to establish a new connection*name resolution

, depending on which part(s) of the errormessage the user is interested in.

Tip: there is no need for wildcards at the start and/or end of the pattern; if the pattern matches
*anywhere* in the value the notification-rule will trigger.

Note: If the value is missing or empty, the pattern will *never* match.

If the intention is to get a notification whenever a pipe fails, it is better to use the
:ref:`Pump failed <pump_failed_notification_rule>` rule instead.


Node heartbeat overdue
======================

The purpose of this rule is to alert the user if something is wrong in the notification-machinery itself.

This is a special built-in rule that is automatically applied to pipes that have one or more
user-specified rules. It is normally never visible to end-users.

Notifications generated by this rule will show up in the `Alert <https://portal.sesam.io/unified/alerts>`_ page
in the GUI. The notification rule will not send any email notifications.

Technical details: This rule triggers if something has gone wrong in the notification machinery itself (hardware problems
with a server machine, bugs in a software component, etc). The way it works is that a sesam-node is supposed to send
a "heartbeat" message at regular intervals. If the Sesam portal backend hasn't seen a message from the sesam-node for
a long time, a "Node heartbeat overdue" notification is triggered.


Alert rate limiting
===================

To avoid flooding users with alert, each notification rule will only generate at most one alert
per hour. If the notification rule triggered more than once during that hour, the alert-message
will say something like this::

    "First occurrence: 2017-11-16 09:53:16. This event has triggered
    an additional 215 times after the first occurrence. The last time
    it triggered was 2017-11-16 11:40:57."


Notification summary API
========================

The SESAM portal backend publishes a notification summary on the API endpoint https://portal.sesam.io/api/notifications-summary .

This endpoint is intended for advanced users who want a quick way of checking if any notification-rules on a
subscription have triggered (for instance to create a status-board website).

Example::

    curl 'https://portal.sesam.io/api/notifications-summary' -H 'Authorization: bearer <JWT-for-the-subscription-12345644-2a04-4ff1-9d77-7b3eb615974c>'

will result in a response that looks like this::

    [
      {
        "_deleted": false,
        "_id": "12345644-2a04-4ff1-9d77-7b3eb615974c",
        "_updated": 4,
        "status": "ok",
        "subscription_id": "12345644-2a04-4ff1-9d77-7b3eb615974c"
      },
      {
        "_deleted": false,
        "_id": "12345644-2a04-4ff1-9d77-7b3eb615974c_pumpoverduetest",
        "_updated": 6,
        "pipe_id": "pumpoverduetest",
        "status": "ok",
        "subscription_id": "12345644-2a04-4ff1-9d77-7b3eb615974c"
      },
      {
        "_deleted": false,
        "_id": "12345644-2a04-4ff1-9d77-7b3eb615974c_monitoring-canary",
        "_updated": 261,
        "notifications": [
          {
            "alerts_will_be_visible_for_the_current_user": true,
            "event_count": 1,
            "event_timestamp": "2019-09-09T11:24:46.187000Z",
            "is_ongoing": true,
            "last_event_timestamp": "2019-09-09T11:24:46.187000Z",
            "msg": "The value of the 'Entities processed' parameter was 0, which is below the specified limit 1.",
            "notification_id": 57763,
            "notification_rule_id": "12345653-f722-4e7e-9afd-59bb3a4f82d5",
            "notification_rule_name": "Too low test",
            "notification_rule_type": "pump_completed_value_too_low",
            "pipe_id": "monitoring-canary",
            "subscription_id": "12345644-2a04-4ff1-9d77-7b3eb615974c"
          },
          {
            "alerts_will_be_visible_for_the_current_user": true,
            "event_count": 1,
            "event_timestamp": "2019-09-09T11:24:46.187000Z",
            "is_ongoing": true,
            "last_event_timestamp": "2019-09-09T11:24:46.187000Z",
            "msg": "The value of the 'Entities processed' parameter was 0, which is below the specified limit 2.",
            "notification_id": 57762,
            "notification_rule_id": "1234560e-cf92-4325-bc39-51cf2604d646",
            "notification_rule_name": "Too low test2",
            "notification_rule_type": "pump_completed_value_too_low",
            "pipe_id": "monitoring-canary",
            "subscription_id": "12345644-2a04-4ff1-9d77-7b3eb615974c"
          }
        ],
        "pipe_id": "monitoring-canary",
        "status": "failed",
        "subscription_id": "12345644-2a04-4ff1-9d77-7b3eb615974c"
      }
    ]

Each entry refers to either a subscription or to a pipe and represents a summary of all the notification rules
defined for that subscription or pipe. Only pipes with at least one user-defined notification-rule will show up in
the list.

The "subscription_id" property refers to the internal id of the SESAM subscription. When using the GUI, this id is
visible in the browser's address bar. Example for the '12345644-2a04-4ff1-9d77-7b3eb615974c' subscription::

    https://portal.sesam.io/unified/subscription/12345644-2a04-4ff1-9d77-7b3eb615974c/overview

The "pipe_id" property refers to the "_id" value in the pipe config (subscription summary-entries don't have a
"pipe_id" property).

If none of the notification rules on a pipe has been triggered, the summary-entry for the pipe will have a
"status"-property with the value "ok".

If at least one rule is currently triggered, the summary-entry for the pipe will have a "status"-property with the
value "failed" and a "notifications"-property with a list of the ongoing notifications.

This endpoint implements the :doc:`JSON Pull Protocol <json-pull>`.
