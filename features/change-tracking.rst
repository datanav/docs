.. _change-tracking:

:badge:`Free feature,badge-success badge-pill`

Change Tracking
===============

:badge:`Free feature,badge-success badge-pill`

Inside Sesam, :ref:`entities <entity-data-model>` flow between datasets before being sent to their corresponding target system. This flow of entities is controlled by :ref:`pipes <pipe_section>`, and one of the tasks of pipes in Sesam is to make sure that no unnecessary entities are processed.   

Before a pipe writes an entity to a dataset, it will compare the new version of the entity to the last version of that entity the pipe produced. If the two versions are different, i.e. the entity has been updated, the dataset will be updated and the new entity will be placed at the front of the processing queue. This way the next pipe in line knows this entity has been updated and needs reprocessing. If the two versions are identical, the sink will drop the new entity and the dataset will not be updated. This way we ensure that only data that needs reprocessing will be reprocessed.  

The comparison is done by comparing the new and the old entitie's ``_hash`` values. 

**Criteria for posting entities to sink dataset**

- New ``_id`` value - The entity did not exist before 
- Change in entity metadata - all non :ref:`reserved fields <reserved_fields>`
- Change in entity delete status - the entity's ``_deleted`` status changes

Each entity version written to a dataset will receive an ``_updated`` value. An entity's ``_updated`` value, unique to each dataset, is an incremental counter assigned to each entity version when they are stored in the target dataset. When a pipe's pump has sucessfully finished, the pipe will store the last (newest) entity's ``_updated`` value as the pipe's ``since`` value, thereby keeping track of the entities that have already been processed.     

.. admonition::  Good to know:
    
    Change tracking is a built-in feature in Sesam and will always act in the background. You could however easily make a pipe reprocess all or some entitites in the source dataset by changing the pipe's ``since`` value in the following ways:

    #. Resets can be done automatically by defining a :ref:`rescan <pump_properties>` property for the pump.
    #. Resets can be done manually through the :ref:`reset <management-studio-pipe-menu>` function in the management studio pipe menu.
    #. Since changes can be done manually through the :ref:`Update last seen <management-studio-pipe-menu>` function in the management studio pipe menu.