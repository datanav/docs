.. _continuation_support_feature:

:badge:`Free feature,badge-success badge-pill`

Continuation Support
====================

:ref:`Sources <concepts-sources>` can optionally support a since marker which lets them pick up where the previous stream of entities left off - like a "bookmark" in the entity stream. This :ref:`continuation support <continuation_support>` allows a pipe to process changes incrementally. The next time the pipe runs it will continue where the previous run finished. Combined with change tracking this reduces the amount of work that needs to be done.