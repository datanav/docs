.. __establish_origin_pattern:

Establish origin pattern
------------------------



In a :ref:`bidirectional synchronizaion <bidirectional-synchronization>` duplicate issues may arise if we no not know which entity from system *A* created which entity from system *B*. Without this relationship clearly established the new entity in system *B* might attempt to insert yet another entity into system *A* (because there might not be a connection between these two entities in the metadata).

In Sesam we solve this issue with the ``establish origin pattern``. This pattern has one external requirement:

- When an entity is inserted into a system, the system's response has to include the new system specific primary key of the new entity. 

When an entity from system *A* is inserted into system 
