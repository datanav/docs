.. _tutorial-collect-source-systems:

Source systems in Sesam
=======================

.. sidebar:: Summary

  Source systems in Sesam...

  - should provide streams of entities as input to the pipes they are connected to
  - can provide entities with **any** shape
  - must provide Sesam with a unique identifier called ``_id``

Sesam supports implementing multiple different :ref:`system types <system_section>`, i.e: JSON, SQL, microservice etc. Each system, regardless of type, will have a defined set of implementation functionalities which can be set in its DTL configuration. As such, the intended usage in Sesam should be taken into consideration when implementing a System.

When a System is used as a source it is especially important to recoqnize that providing streams of entities as these are updated in the source system as a :ref:`delta stream <delta-stream-processing>`, ensures that Sesam can propagate data changes through a :ref:`Sesam dataflow <creating-a-sesam-dataflow>` quickly and efficiently, even if the amount of data residing in the source System increases exponentially. As such, avoiding bulk readings of data, as the amount of data residing in your source System increases, should be avoided.

With the above in mind, let us create a source system in Sesam.

.. important:: Prerequisites

  You should have completed the :ref:`getting started guide <getting-started>` before starting on this tutorial.

The source system we will be working with is the...


