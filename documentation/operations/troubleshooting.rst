.. _troubleshooting:

Troubleshooting
===============

Working with data management and synchronization can be challenging at times. We have listed a set of challenges and their potential solutions to help you troubleshoot some of the most challenging issues you can encounter.

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
^^^^^^^^^

Common solutions to some of the operation issues above are:

#. The result / status / feedback from the target system for both inserts, updates and deletes should be stored in a dataset in Sesam. Need to separate entity and system failures.

#. Partial rescans on all connect pipes that reads data using incremental update.

#. Data in dead letter datasets should be collected and sent to a monitoring system or other error handling systems.

#. Data being sent from Sesam should be validated.

#. Error messages from deletes that fails due to the object already being deleted should be ignored.

#. Insert pipes should have safeguards against sending duplicates to the target system.

Common issues with data management
----------------------------------

#. Dependency tracking limit failure. Difficult to debug. Join on blank properties. Equality set has too high cardinality.

#. Exceptions when using http transforms, might ignore some errors.

#. Cascading issues, like a pipe waits for another pipe to be ready, which has failed.

#. Unforeseen merges yield wrong data and unwanted load on both Sesam and connected systems.

#. Merged entities in globals has wrong status, entities should be unmerged, versions should be deleted, etc.

#. Systems that automatically changes data that is written to it, causing a loop if the data is part of a bidirectional sync.

#. Using 'first' to return an unique entity from the result of a hops, might not be deterministic.

#. Wrong result out of globals for entities used in a feedback loop.

#. Wrong generation of unique identifiers for a target system, might cause unexpected updates and deletes.

#. An object produces the same child as another object.

#. Use of 'create' in pipes without rescan creates orphaned children.

Solutions
^^^^^^^^^

Common solutions to some of the operation issues above are:

#. Construct the equality sets in hops by using tuples, not all the 'eq'-statements becomes indexes. 

#. Decrease the chance of high cardinality in a hops by joining on more than on property, for example not only join on email, but on email and gender for instance.

#. Include rescans on all pipes still prone to dependency tracking limit failures.

#. Monitor pipes that has been unresponsive or unable to process over a given period.

#. Add circuit breakers to preparation pipes.

#. If the result of a feedback loop in a global is wrong, verify that the documented feedback pattern has been used.

#. Be ware of the difference between 'in' and 'eq' in DTL.