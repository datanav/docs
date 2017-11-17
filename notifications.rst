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


How can it be monitored?
------------------------

Each of the metric described above can be monitored in a number of different ways.

Value too low
~~~~~~~~~~~~~
This rule type triggers a notification if a metric was below a specified value.


Value too high
~~~~~~~~~~~~~~
This rule type triggers a notification if a metric was above a specified value.


Value too low over time
~~~~~~~~~~~~~~~~~~~~~~~
This rule type triggers a notification if a metric has been below a specified value for a
specified period of time.


Value too high over time
~~~~~~~~~~~~~~~~~~~~~~~~
This rule type triggers a notification if a metric has been above a specified value for a
specified period of time.



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


Alert rate limiting
===================

To avoid flooding users with alert, each notification rule will only generate at most one alert
per hour. If the notification rule triggered more than once during that hour, the alert-message
will say something like this::

    "First occurrence: 2017-11-16 09:53:16. This event has triggered
    an additional 215 times after the first occurrence. The last time
    it triggered was 2017-11-16 11:40:57."
