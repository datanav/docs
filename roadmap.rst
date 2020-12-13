=======
Roadmap
=======

.. contents:: Table of Contents
   :depth: 2
   :local:

Future plans. Disclaimer safe harbour. More transparency.

Planned
=======

The following features are currently being worked on an will be rolled out as soon as they are implemented.

Background reprocessing
-----------------------

Why? Changing a global (e.g. adding a property) requires long downtime..

Goal? Not have significant downtime in data flow when you reset a pipe.

How? Reprocess in the background so that new data is not interrupted while the reprocessing is happening.

Integrated data browsing
------------------------

Why? Databrowser hard to configure. Not integrated into MS. Targeted at external users.

Goal? Easier to understand data. More efficient development.

How? Integrated search engine. Enterprise feature. Global setting.

Extensions
----------

Why? Microservices second hand citizens. Unstructured documentation (README, etc).

Goal? No difference between built in systems and extensions. Provide a marketplace. Trivial to enable an extensions
on a subscription.

How? Manifest (declaration). Config passed in a defined way. Endpoint patterns and behaviour defined. Built on JSON
pull/push protocol and JSON configuration.

Kubernetes based architecture
-----------------------------

Why? Currently have two architectures (docker compose and kubernetes). Some features are only available in one or
the other of the architectures. Not an automated way to get from one to the other. Two code paths.

Goal? End user can upgrade without assistance.

How? Standalone will be transitioned to kubernetes with one compute node. Self-hosted installations will require
Kubernetes. There are single machine kubernetes wrappers (Kind) that makes this doable.

On the radar
============

The following features are on the radar and is not yet planned in the product. We list them here to give you insight
into what we are currently investigating.

System proxy (aka chaining systems)
-----------------------------------

Why? Not possible to add middleware (cross cutting concerns) across HTTP based systems. E.g. signing every request to
AWS services with or do additional header verification on incoming requests. Workaround today requires microservices
to talk to each other without any declartion which we do not want to allow in the future due to security problems.

Goal? Be able to implement such logic in one component and apply it where you want to. Be able to know
about these dependencies.

How? Add a proxy list property on all HTTP-based systems that the system will proxy all requests through. Will also
work on most existing microservices/extensions as the HTTP libraries in Python and Java can be configured to use
proxies through pre-defined environment variables.

Partitioned pipes
-----------------

Why? As data volumes grow the time to reprocess grows. Not considered a problem once the initial computation is done,
but
adding
new
data or reshaping data can take a long time the more data you have and this reduces agility.

Goal? Be able to scale out so that the time to reprocess or import new data is not limited by Sesam.

How? Partitioned pipes. Complex problem due to how merging and complex hops work.

Finding relationships between datasets
--------------------------------------

Why? Manually defining relationsships can be tedious.

Goal? Be able to find relationships by examining the data.

How? Use machine learning to detect them.

Billable SaaS through Azure and AWS
-----------------------------------

Why? Running Sesam requires a sales process today which might hinder adoption.

Goal? Make it easier to find and use Sesam.

How? Offer Sesam as a billable SaaS through the major Cloud vendors marketplaces.

Extend user accessible audit logs to data access
------------------------------------------------

Why? Today you need to contact support in order to get an audit log of data access in Sesam (when, who, which
dataset). That audit log might also not contain what you expect.

Goal? End user should have access to the data access audit logs.

How? Have the possibility to log data access into a separate dataset.