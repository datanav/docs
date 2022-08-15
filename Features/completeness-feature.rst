.. _completeness-feature:

Completeness
============

:ref:`Completeness <completeness>` is a feature that you typically enable on outgoing pipes. It makes sure that all pipes that this pipe is dependent on have run before it processes the source entities of this pipe. The timestamp of the source entity is compared with the completeness timestamp that was inherited from its upstream and dependent pipes. This feature effectively holds back the processing of source entities until it can be sure that dependent pipes have completed. This is useful when you want to have a final entity version before you send it to the target system. It also reduces the number of times you have to send the entity to the target system as there might be several state transitions until the entity can be considered complete.