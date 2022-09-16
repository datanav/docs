.. _scheduling-and-signalling:

Scheduling and signalling
=========================

The active part of a pipe is called a :ref:`pump <pump_section>`. A pump makes entities flow through the pipe. It can be scheduled to run at regular intervals. These intervals can be specified in seconds or using a :doc:`cron expression <../cron-expressions>`. One can also optionally schedule the pipe to do full rescans.

Signalling is a feature that automatically signals downstream pipes when data changes upstream. :ref:`Signalling <service_metadata_section>` is enabled by default. A signal schedules the pump for immediate execution. This feature allows for new data to flow downstream at a much faster pace than if the pumps just ran at scheduled intervals.