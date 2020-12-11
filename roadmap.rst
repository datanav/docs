=======
Roadmap
=======

.. contents:: Table of Contents
   :depth: 2
   :local:

Future plans. Disclaimer safe harbour. More transparency.

Data browsing
-------------

Why? Databrowser hard to configure. Not integrated into MS. Targeted at external users.
Goal? Easier to understand data. More efficient development.
How? Integrated search engine. Enterprise feature. Global setting.

Extensions
----------

Why? Microservices second hand citizens. Unstructured documentation (README, etc). Not possible to add middleware
(cross cutting concerns) across systems.
Goal? No difference between built in systems and extensions. Provide a marketplace. Trivial to enable an extensions
on a subscription.
How? Manifest (declaration). Config passed in a defined way. Endpoint patterns and behaviour defined. Built on JSON
pull/push protocol and JSON configuration.

Unified architecture
--------------------

Why? Currently have two architectures (standalone and kubernetes). Some features are only available in some of the
architectures. Not an automated way to get from one to the other. Two code paths.
Goal? End user can upgrade without assistance.
How? Standalone will be transitioned to kubernetes with one compute node. Self-hosted installations will require
Kubernetes. There are single machine kubernetes wrappers (Kind) that makes this doable.