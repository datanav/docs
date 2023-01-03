.. _pattern-rewriting-identity:

Rewriting identity
------------------
When rewriting ``_id`` you should always add a ``["add", "$original_id", "_S._id"]`` in order to be able to trace and debug. Multiple upstream entities could map to the same identity, and this can be very hard to figure out without this information. Also make sure you rewrite the identifier before you do any filtering.