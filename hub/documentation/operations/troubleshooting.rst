.. _troubleshooting:

Troubleshooting
===============

Working with data management and synchronization can be challenging at times. We have listed a set of challenges and their potential solutions to help you troubleshoot some of the most challenging issues you can encounter.

.. note::
  This document is subject to improvements as we are continuously identifying new issues and trying to provide adequate solutions.

Common issues with data synchronization
---------------------------------------

#. Insert or update of an entity throws an exception due to the target system not being idempotent.

#. Deletes fails due to dependencies on the object you want to delete.

#. Deletes fails due to the object already being deleted in the target system.

#. Wrong order of inserts, an object has dependencies that must exist in the target system before an insert can occur, such as a parent object.

#. Batch inserts and updates, when they fail it is difficult to locate which entities causes the batch to fail.

#. Reading data from a SQL database or other systems that supports incremental updates without configuring partial rescans can lead to entities not being read from the source system.

#. Data that contains erroneous values.

#. Data that is in the wrong form.

#. Microservices causing errors due to:
   
   #. Memory issues.
   #. Unstable or unrobust code.
   #. Lacking good exception handling.

#. Configured dead letter datasets, but no monitoring or handling of them.

#. Duplicates in the target source.

#. Pipes that are stuck and unresponsive.

#. Expired certificates on the server.


Solutions
---------

Common solutions to some of the operation issues above are:

#. The result / status / feedback from the target system for both inserts, updates and deletes should be stored in a dataset in Sesam. Need to separate entity and system failures.
#. Partial rescans on all connect pipes that reads data using incremental update.
#. Data in dead letter datasets should be collected and sent to a monitoring system or other error handling systems.
#. Data being sent from Sesam should be validated.
#. Error messages from deletes that fails due to the object already being deleted should be ignored.
#. Insert pipes should have safeguards against sending duplicates to the target system.