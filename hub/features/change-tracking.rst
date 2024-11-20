:badge:`Free feature,badge-success badge-pill`

.. _change_tracking:

Change Tracking
===============

Inside Sesam, :ref:`entities <entity-data-model>` flow between datasets before being sent to their corresponding target system. This flow of entities is controlled by :ref:`pipes <pipe_section>`, and one of the tasks of pipes in Sesam is to make sure that no unnecessary entities are processed.

Before a pipe writes an entity to a dataset, it will compare the new version of the entity to the last version of that entity the pipe produced. If the two versions are different, i.e. the entity has been updated, the dataset will be updated and the new entity will be placed at the front of the processing queue. This way the next pipe in line knows this entity has been updated and needs reprocessing. If the two versions are identical, the sink will drop the new entity and the dataset will not be updated. This way we ensure that only data that needs reprocessing will be reprocessed.

The comparison is done by comparing the new and the old entity's ``_hash`` values.

**Criteria for posting entities to sink dataset**

- New ``_id`` value - The entity did not exist before
- Change in entity metadata - all non :ref:`reserved fields <reserved_fields>`
- Change in entity delete status - the entity's ``_deleted`` status changes

Each entity version written to a dataset will receive an ``_updated`` value. An entity's ``_updated`` value, unique to each dataset, is an incremental counter assigned to each entity version when they are stored in the target dataset. When a pipe's pump has successfully finished, the pipe will store the last (newest) entity's ``_updated`` value as the pipe's ``since`` value, thereby keeping track of the entities that have already been processed.

.. admonition::  Good to know:

    Change tracking is a built-in feature in Sesam and will always act in the background. You could however easily make a pipe reprocess all or some entitites in the source dataset by changing the pipe's ``since`` value in the following ways:

    #. Resets can be done automatically by defining a :ref:`rescan <pump_properties>` property for the pump.
    #. Resets can be done manually through the :ref:`reset <management-studio-pipe-menu>` function in the management studio pipe menu.
    #. Since changes can be done manually through the :ref:`Update last seen <management-studio-pipe-menu>` function in the management studio pipe menu.


Benefits
--------
Change tracking eliminates the need to process and transfer entire datasets, focusing solely on the modified or new data elements. 
Unlike traditional methods that synchronize all data indiscriminately, this innovative technique focuses on synchronizing only the data that undergoes changes. 

Faster sync times
*****************

By synchronizing only the data that changes, organizations can significantly reduce the amount of data transmitted between systems. This approach optimizes bandwidth and API usage, especially when dealing with large datasets or when connecting systems over limited network resources. As a result, the sync times are noticeably faster, enabling near real-time updates and ensuring that the latest information is readily available across integrated systems.


Minimized data conflicts and improved data quality
**************************************************

When synchronizing only the changed data, the potential for data conflicts is significantly reduced. Conflicts often arise when multiple systems independently modify the same dataset simultaneously. By selectively synchronizing modifications, the chances of conflicting changes are minimized, preserving data integrity and maintaining consistency across integrated systems. Consequently, data quality is improved, ensuring accurate and up-to-date information throughout the organization.


Greater flexibility and scalability
***********************************

Change tracking provides your organization with greater flexibility in integrating various cloud systems. As new systems are added or existing ones are updated, selective synchronization allows for seamless integration without disrupting the entire data ecosystem. This scalability enables you to adapt to evolving business requirements, integrate additional systems with ease, and cater to future growth without compromising system stability.

Enhanced security and compliance
********************************

Data security is a paramount concern for organizations handling sensitive information. Change tracking reduces the risk of unauthorized access and potential data breaches by limiting the transfer of information to only what is necessary. By synchronizing only the changed data, the attack surface is reduced, making it easier to implement stringent security measures and comply with regulatory standards such as GDPR (General Data Protection Regulation) or industry-specific regulations.