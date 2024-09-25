Connector asymmetry
===================

Some endpoints are asymmetric, i.e. the data model exposed in collect pipeline might differ from the data model required in share pipes. This asymmetry should be managed by the connector such that data coming out of collect pipeline is symmetric with the data coming into the share pipes.

When required connector pipes may perform hops to other connector datasets to achieve symmetry or to satisfy required data dependencies, but not to datasets outside the connector. This should however be performed with caution as you might introduce loops or additional dependencies.

It's recommended to adapt the share model to match the collect model as one can then start building the collect part of a connector first and start using that without breaking backwards compatibility.