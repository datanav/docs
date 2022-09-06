.. _change-tracking:

Change Tracking
===============

Inside Sesam, :doc:`entities <../entitymodel>` flows between datasets before sent to their corresponding target system. This flow of entities is controlled by :ref:`pipes <pipe_section>`, and one of the tasks of pipes in Sesam is to make sure that no unnecessary entities are processed.   

Before a pipe writes an entity to a dataset, it will compare the new version of the entity the last version of that entity the pipe produced. If the two version are different, i.e. the entity has been updated, the dataset will be updated and the new entity will be placed at the front of the processing queue. This way the next pipe in line knows this entity has been updated and needs reprocessing. If the two version are identical, the sink will drop the new entity and the dataset will not be updated. This way we ensure that only data that needs reprocessing will be reprocessed.  

The comparison is done by comparing the new and the old entitie's ``_hash`` values. 


**Criteria for posting entities to sink dataset**

- New ``_id`` value - The entity did not exist before 
- Change in entity metadata - all non :ref:`reserved fields <reserved_fields>`
- Change in entity delete status - the entity's ``_deleted`` status changes

Change tracking is a built-in feature in Sesam and will always act in the background. You could however easily make a pipe reprocess all entitites in the source dataset by manually resetting the pipe, or by utilizing any of the rescan options in the pipe's :ref:`pump properties <pump_properties>`