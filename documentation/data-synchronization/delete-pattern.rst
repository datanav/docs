.. _delete_pattern:

Delete Pattern
--------------

Seperate pipeline for deletes. Discards any entity that is not marked with _deleted:true. If you want to delete with a transform and store a log of the delete event, make sure you set _deleted:true to keep the entity in the sink dataset. How do you avoid deletes that the merge source emits when merged entities change _id? What if there is a subset on the way out? How do you avoid deletes from the subset?
