.. _circuit-breakers:

Circuit Breakers
================

A :ref:`circuit breaker <circuit_breakers_section>` is a safety mechanism that one can enable on the :ref:`dataset sink <dataset_sink>`. The circuit breaker will trip if a larger than expected number of entities are written to a dataset in a pipe run. When tripped, the pipe will refuse to run and it has to be untripped manually. This safety mechanism is there to prevent unforeseen tsunamis of changes and to prevent them from propagating downstream.