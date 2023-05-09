.. _caveats:

Caveats
=======

Dependency tracking
-------------------

* :ref:`Dependency tracking <dependency_tracking>` only works for pipes that use the :ref:`dataset <dataset_source>` source. So if you have a pipe with a :ref:`merge <merge_source>` source then you do not get dependency tracking for the :ref:`hops <hops_dtl_function>` and :ref:`apply-hops <apply_hops_dtl_function>` functions on that pipe. You will have to split the pipe into two pipes in order to make dependency tracking work.

* Dependency tracking works by taking the pipe's :ref:`hops <hops_dtl_function>` and :ref:`apply-hops <apply_hops_dtl_function>` functions and then inversing the traversal. That means that if an entity in a referenced dataset changes, then dependency tracking will traverse from the entity and back to the pipe's source dataset to find entities that need to be reprocessed. The inverse traversal is performed by hops that traverse in the opposite direction of the original hops expression.

* If you have pipe with chained transforms and there are hops on a :ref:`DTL transform <dtl_transform>` that is not the first transform in the chain, then dependency tracking will only work if all the join criteria evaluates to the same values as on the pipe's source dataset entity. In practice this means that you cannot change any of the dataset source entity's properties that involved in the hops's join criteria.

* Similarly to the previous item a pipe with ``"add_namespaces": true`` effectively rewrites the dataset's source entities by adding namespaces. This means that the join criteria won't work in dependency tracking. For that to work you'd have to effectively strip off the namespaces again. The reason for this is that the inverse traversal matches against the source dataset's entities and not the transform's entities.

* The ``_S.$ids`` property is a dynamic property and will automatically wrap and include the ``_S._id`` value as a :ref:`NI value <namespaces-feature>` if the source entity does not already have a ``$ids`` property. The value will be preprended by the pipe's identity namespace, but it will only do this if namespaced identifiers is enabled for the pipe. This means that the value is rewritten and may interfere with the join criteria of the inverse hops in dependency tracking as described above.
