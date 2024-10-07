Update
------
​
Split into two separate pipelines. Update typically uses the :ref:`optimistic locking <optimistic_locking>` to compare the payload relative to current state in the target system. Comparison could also be made between the current state of the system and the payload to see if an update is required.