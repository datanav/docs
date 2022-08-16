.. _merging-feature:

Merging
=======

An essential feature that enables :ref:`global datasets <global-datasets>` is the ability to merge different entities into one entity representing the same thing. 

Use case
--------
Organizations often have multiple systems that share overlapping information about employees, customers, products etc. The :ref:`merge source <merge_source>` lets you define equivalence rules that enables you to merge entities. The merge source is able to merge incrementally producing a stream of entities that have been merged – or unmerged (when an equivalence rule no longer applies).