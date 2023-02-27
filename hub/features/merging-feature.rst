.. _merging_feature:
.. _merging-feature:

:badge:`Free feature,badge-success badge-pill`

Merging
=======

An essential feature that enables :ref:`global datasets <global_datasets>` is the ability to merge different entities into one. The resulting entity contains data from multiple upstream entities that had all represented the same thing.

Use case
--------
Organizations often have multiple systems that share overlapping information about employees, customers, products etc. The :ref:`merge source <merge_source>` lets you define equivalence rules that enable you to merge entities. The merge source is able to merge incrementally, producing a stream of entities that have been merged or unmerged (when an equivalence rule no longer applies).