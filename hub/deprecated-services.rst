.. _deprecated_services:

===================
Deprecated services
===================

This document contains deprecated services from the documentation. Do
not make use of these services.

.. toctree::
   :maxdepth: 1
   :hidden:

   Sesam Talk <../talk/index>

.. _sesam_talk_deprecated:

Sesam Talk
==========

The :doc:`Sesam Talk service <../talk/index>` consumes data from a Kafka topic. The consumer stores the offset in the pipe, and does not commit the consumer offset back to Kafka.