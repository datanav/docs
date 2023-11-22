.. _sync_modes:

=====================
Synchronisation modes
=====================


Introduction
------------

todo write about default mode, changes and all and custom defaults will determine this.

Read only
---------

todo "shared enabled" toggle off. Means we only read data, never write. Data is relevant for other non-read-only datatypes.

Limited sync
------------

todo Only sync data that was created after the system is connected. Data might sync regardless if the object is referenced/required by another object that is about to be synced. E.g. if a deal is about to be inserted and it references a company or a product that was created before onboarding, it will cause the product or company to be inserted into the target system regardless. This can cause duplicates if that product or company already exists in the target system. Duplicates can therefore appear over time if old entities are references gradidually.

Full sync
---------

todo All data will be synced regardless of when the system was connected. duplicatation will happen once


.. _avoid_duplicates:

Avoiding Duplicates
-------------------

This can cause duplicates if the data types between the different systems don't have merge criteria and both systems are populated with overlapping initial data. 

To prevent duplicates when merging isn't safe, we've disabled `Full Sync`, the synchronization of pre-existing data in the systems before connecting them. This means only new data flows between connected systems. You can enable `Full Sync` at any time in the management console `Management Console <https://talk.sesam.cloud/onboarding>`_  to synchronize all records across connected systems.