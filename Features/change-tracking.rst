.. _change-tracking:

Change Tracking
---------------

When reading data from a source, Change Tracking makes it possible to just ask for the entities that have changed since the last time, that if the source supports it. 
This feature uses the knowledge of the source, such as a last updated time stamp, to ensure that only entities that have been created, deleted or modified are exposed. 

On the side of the dataset, regardless of where the data comes from, an incoming entity is compared with the existing version of that entity and only updated if they are different. The comparison is done by comparing the hashes of the old and new entity.

Usecase
--------
The typical pattern is to read data from a source and push it to a sink that is writing into a dataset. The dataset is essentially a log of the entities it receives. However, if a new log entry was added every time the source was checked then log would grow very fast and be of little use. Change Tracking is one of the mechanisms you can utilise at both ends to prevent this problem.

How to use Change Tracking
--------------------------
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

