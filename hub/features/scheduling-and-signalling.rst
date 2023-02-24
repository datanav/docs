.. _scheduling_and_signalling:

:badge:`Free feature,badge-success badge-pill`

Scheduling and signalling
=========================

The active part of a pipe is called a :ref:`pump <pump_section>`. A pump makes entities flow through the pip and can be scheduled to run at regular intervals. These intervals can be specified in seconds or using a :doc:`cron expression <../cron-expressions>`. Optionally, you can also schedule the pipe to do full rescans.

:ref:`Signalling <service_metadata_global_defaults_use_signalling_internally>` is a feature that automatically signals downstream pipes when data changes upstream. Signalling is enabled by default. A signal schedules the pump for immediate execution. This feature allows for new data to flow downstream at a much faster pace than if the pumps ran at scheduled intervals.
