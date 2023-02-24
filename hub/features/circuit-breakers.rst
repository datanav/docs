.. _circuit_breakers:

:badge:`Free feature,badge-success badge-pill`

Circuit Breakers
================

A circuit breaker is a safety mechanism can be enabled on the
:ref:`dataset sink <dataset_sink>`. The circuit breaker will trip if
the number of entities written to a dataset in a pipe's run exceeds a
certain configurable limit.

Note that a circuit breaker is only activated if the sink dataset is
populated. This means that the pipe must have run to
completion at least once. This is to avoid tripping it on the initial
sync.

A tripped circuit breaker will prevent the pipe from running.
It can either be rolled back or committed. Rolling it back
will delete any entities that were written in the pipe run before the
circuit breaker was tripped. Committing it will expose the uncommitted
entities. Both operations resets the circuit breaker so that pipe can
run again.

Compaction will not be performed on datasets with a tripped circuit
breaker. It is also not possible to repost entities to these datasets.

You can rollback or commit the circuit breaker on the dataset page in
the :doc:`Management Studio <../management-studio>`, or use the
`service API <api.html#post--datasets-dataset_id>`_.

Resetting
---------

When the configuration of a pipe is modified in such a way that the entities the pipe
produce change (for instance by changing the DTL transform of the pipe), the pipe's "last-seen"
value must be cleared in order to reprocess already seen entities with the new pipe
configuration.

This can be done by setting the "last-seen" value to an empty string with the
`update-last-seen <./api.html#api-reference-pump-update-last-seen>`__ operation in the Service API.
