=====================
Cluster Configuration
=====================

A single Sesam Node is a fully functional service for collecting, storing, tramsforming and deliverying data. However some workloads can benefit from multiple nodes running at the same time. These nodes could be on different machines, or be working with different data. When running multiple nodes it would still be nice to access them as though they were a single Sesam service instance.

It is possible to configure a Sesam Node to act just as a Sesam API node. In this mode it is configured to sit in front of a number of Sesam nodes and expose a unified API across them all.



