============
Architecture
============

.. contents:: Table of Contents
   :depth: 2
   :local:

Introduction
============

Sesam is offered as service. The service is either hosted for you in the cloud or it is self-hosted. The service has an :doc:`API <api>` that is used to securely communicate with the service over HTTPS. The service subscription is billed monthly.

The terms of service can be found here: https://sesam.io/terms.html

Tooling
=======

The Sesam service is backed by a centralized portal. The portal is a web service running at `https://portal.sesam.io/ <https://portal.sesam.io/>`_ . The portal is the place were you can sign up for, and manage, your Sesam subscriptions. It is also the place where you go to for the :doc:`Sesam Management Studio <management-studio>`, the user interface for accessing your own Sesam service.

There is also an `experimental version <https://beta.portal.sesam.io/>`_ of the Management Studio where new features are introduced at an earlier stage before they are publicly released in the main portal.

Software channels
=================

Sesam software is released through a phased rollout scheme. There are four different release channels – commonly called canaries. This is done to give changes and new features some time in non-production environments before they are rolled out to production. The goal is to reduce risk.

The available channels are:

- ``weekly-prod`` is release bi-weekly and is the most stable release. *Use this in production!*
- ``weekly`` is release once a week. Use this in staging environments.
- ``nightly`` is released every night. Use this in development environments.
- ``latest`` is released every time a pull request is merged. Use this only for developent environments, and only when you know what you're doing.

Architecture
============

There are currently two types of Sesam architectures; the current architecture and the new architecture. The current architecture runs the Sesam service on a single virtual machine. The subscription types *Small*, *Medium* and *Large* are all of this type. The *Extra Large* subscription type uses the new architecture and can scale to a large number of machines. In the future we aim to host all subscription types on the same architecture. Both architectures use container runtimes to host the service.

The Sesam software is distributed as standard `OCI images <https://opencontainers.org/>`_ (aka Docker images). The container images are hosted on `Docker Hub <https://hub.docker.com/>`_ in a private repository.

The infrastructure is provisioned by `Terraform <https://www.terraform.io/>`_ on `Microsoft Azure <https://azure.microsoft.com/>`_ . The default Microsoft Azure region is North Europe (Dublin, Ireland). The data never leaves this data center. The data is encrypted at rest using a key managed by Microsoft Azure. Bringing your own key is currently not yet supported.

Sesam uses `RocksDB <https://rocksdb.org/>`_, an embedded high-performance key-value database, to persist data.

The Sesam service is built around the principle that Sesam does not own the data stored in the data hub. The idea is that all the data in the data hub can be re-read from the sources and thus be fully rebuilt from scratch.

.. current_architecture:

Current architecture
--------------------

This architecture is hosted on a single virtual machine. The size of the virtual machine varies between the subscription types. All software runs as Docker containers, except the agent which runs directly on the host. These subscriptions are provisioned as individual resource groups in one shared Azure subscription. Each subscription has its own Azure Network Security Group. Data is stored on managed network disks. 

The services consists of the following software components:

- An agent that self-updates and makes sure that the other software that should run actually are running. It will also automatically upgrade the other software components.

- A reverse proxy that does TLS termination, traffic management and routing. The TLS certificate is automatically managed via `Let's Encrypt <https://letsencrypt.org/>`_, but it is also possible to bring your own certificates. The proxy listens to port 443 and routes traffic to the Sesam service instance.

- The Sesam service instance – commonly called "the node". This is the service that hosts the service API.

- A log shipper that ships logs. Logs are shipped to Sesam for monitoring, notification and billing purposes.

- A metrics agent that ships metrics. Metrics are shipped to Sesam for monitoring purposes.

- User-defined :ref:`microservices <microservice_system>` . The microservice systems are spun up as individual Docker containers.

.. _curr_arch_backup:

Backup
######

Backup is performed once every 24 hours. Seven daily checkpoints are retained on the local disk if the backup policy is ``Local``. If ``Geo-redundant`` backup is enabled then the Azure VM Backup service creates a backup of the VM daily.  The ``Geo-redundant`` retension policy is to keep the last backup, 7 daily backups, 4 weekly backups and 4 monthly backups.

Note that ``Geo-redundant`` backups are kept for 30 days after deletion as this is mandated by Azure. If the service is self-hosted then the owner is responsible for creating off-site backups of the checkpoint directories or the virtual machine.

.. _new_architecture:

New architecture
----------------

This architecture is hosted on `Kubernetes <https://kubernetes.io/>`_ and can scale out to a large number of machines. It is dynamic and can scale out as your processing requirements increase. These subscriptions will be provisioned in one Azure subscription per customer. Each subscription has its own Azure Network Security Group. Data is stored on local nvme disks and/or managed network disks. 

The services consists of the following software components:

- A reverse proxy that does TLS termination, traffic management, and routing.  The TLS certificate is automatically managed via `Let's Encrypt <https://letsencrypt.org/>`_. The proxy listens to port 443 and routes traffic to the Sesam service instance.

- Aggregator: the service that hosts the service API.

- Storage node: stores the configuration and the provisioner topology.

- Provisioner: a Kubernetes operator that does provisioning of processing pipes.

- The Sesam service instance(s) – commonly called the "node". Each of these run one or more :ref:`pipes <concepts-pipes>`.

- A log shipper that ships logs. Logs are shipped to Sesam for monitoring and billing purposes.

- A metrics agent that ships metrics. Metrics are shipped to Sesam for monitoring purposes.

- User-defined :ref:`microservices <microservice_system>`. The microservice systems are spun up as individual Kubernetes deployments.

Backup
######

Backup is performed once every 24 hours. A ``Geo-redundant`` backup is written to the Azure subscription's Azure storage account at the same time. The ``Geo-redundant`` retension policy is to keep the last backup, 7 daily backups, 4 weekly backups and 2 monthly backups.

Monitoring
==========

Logs
----

The following kinds of logs are shipped to Sesam:

- Service logs. This includes error messages.
  
- Health checks and service status.
  
- Sesam configuration. No sensitive data is shipped, so no embedded data nor secrets are shipped. 
  
- The pipe execution dataset. This is only shipped when pipe monitoring is enabled. It is used to trigger notifications for registered notification rules.
  
- System logs, currently only the kernel logs are shipped. 

Metrics
-------

This is a Prometheus-compatible system that pushes telemetry data from the local virtual machines to Sesam. The metrics include information like memory usage, disk usage and other resource usage. This information is used for monitoring and operations.

Termination
===========

When a subscription is terminated all data in it is deleted. Backups are deleted, but in the case of Azure backups as described in the :ref:`current architecture <curr_arch_backup>` those backups are retained for 30 days after deletion. 

Security
========

The following security measures are available:

- Virtual Private Network (VPN). All communication can be configured to go through a VPN tunnel.

- Cryptography. All communication via the Service API use Transport Layer Security (TLS).

- Permissions system. Users can register themselvs in the Sesam Portal. The user can then create new subscriptions or be invited into an existing subscription. In a subscription a user can have one or more roles. The list of roles can be managed by the owner(s) of the subscription.

- API access control. Users log into the Sesam Portal where they are given a time-limited `JSON Web Token <https://jwt.io/>`_ that can be used to access the user's subscriptions. JWT tokens are renewed before they expire. The :doc:`Sesam Management Studio <management-studio>` will do this automatically. It is also possible to create custom time-limited JWT tokens for use by automated integrations.

- Backups. Point in time snapshots of the data in the data hub can be kept off-site for safe-keeping.

Isolation
---------

Subscriptions are segregated and run on separate isolated hardware. Subscriptions under the same *subscription group* share a common network. In the :ref:`new architecture <new_architecture>` a subscription group existing inside its own Azure subscription.

Firewall
--------

All cloud services have an Azure Network Security Group in front. Only port 443 can be opened as this is the port used by the :doc:`service API <api>`. One has the option of blocking all public access through it or denying all except for a whitelist of ip addresses and ranges. In the new architecture it is possible to push the IP white listing down to the reverse proxy and also allow public access and restricted access to pipes through custom rules on the pipes. There are no restrictions on outgoing traffic currently.

VPN
---

You can extend Sesam into your own network using a IPSec-based Virtual Private Network. The :doc:`Sesam Management Studio <management-studio>` interface does not currently let you configure this. Please contact sales@sesam.io to configure your VPN.

Secure Development policy
=========================

Sesam is ISO/IEC 27001 certified and follows a secure development policy. This policy ensures that development environments are secure and that the processes for developing and implementing systems and system changes encourage the use of secure coding and development practices. Changes to systems within the development lifecycle is controlled by the use of formal change control procedures.

- Sesam software is developed using a `scaled trunk-based development model <https://trunkbaseddevelopment.com/>`_.

- All software changes must have unit tests, integration tests and other functional tests before being reviewed and then merged into the trunk.

- All software changes must be reviewed by at least one other developer before being elegible for being merged into the trunk. Major changes are reviewed by a larger audience before being accepted.

- Changes relating to security, robustness or stability are planned and approved before development begins.

- Major architectural changes like new technologies, protocols and third-party components are subject to formal change control procedures.

- Before new third-party libraries are used or upgraded, a review of these are made by at least two developers from the core development group. No third-party library will be accepted for use unless it is well-known, has seen steady uptake, is being actively maintained and there are no serious security issues related to it.

- Third-party libraries and their transitive dependencies are pinned to specific versions to avoid unintentional upgrades.

- Third-party dependencies are reviewed on a regular basis.

- Software artifacts are verified and checked against published hashses to avoid tampering risks.

- Automated licensing checks are performed regularly.


Security incidents
==================

Procedure
---------

Security incidents are reported, managed, solved and closed as described in the following procedure:

- End-users, monitoring systems are internal system users reports incident.

- The service desk describes and logs the incident. They connect all reports related to the service interruption.

- The service desk registers date and time, name on the person that reported the incident and creates a unique ID for the incident.

- A service desk agent categorizes the incident. The team will use these categories while evaluating the incident and for various reporting uses.

- A service desk agent prioritizes the indicent based in the criticality.

- A security incident will be categorized as critical and will be sent to the CISO (Chief Information Security Offices), who will coordinate further.

- The team investigates the incident, and attempts to resolve the issue. Service desk agent(s) communicate the incident reports to help complete the diagnosis.

- If necessary, the service desk agent escalates the incident to secondary support handlers.

- The service desk fixes the service incident and verifies that the solution is successful. The decision and changes are documented for future reference.

- The service desk closes the security incident.

After a security incident has been closed, the team members performs a post mortem to determine:

- Missing requirements

- Potential changes to service level agreements.

- Potential improvements to the service and other relevant focus areas.

Risk assessment
===============

Sesam uses the tool `VsRick <https://www.vigilantsoftware.co.uk/topic/vs-risk>`_, and information security risk assessment tool, to do risk assessments.

Procedure
---------

- Risk identification. Qualitative risk assessment, method-threat-vulnerability based on ISO 27005:2011.

- Consequence analysis, effect and probability. Every risk is evaluated and factors like consequences and probability are compared.

- Method for risk assessment. The risk is calculated by multiplying the consequence by the probability.

- Criteria for accepting risk. The basic security criteria is controlled by the business, regulatory and contractual requirements that Sesam has to fulfill with regards to information security.

- Risk management plan and controls. If the alternative to risk management is to avoid, reduce or transfer, then a risk management plan (RTP) must be created and communicated to the asset owner for approval, and when applicable for implementing.

- Risk owners. For every risk an owner needs to be identified.

- Remainder Risk management. Remainder risks are the risks that remain after the risk assessment. Where applicable, remainder risks must be dealt with as new risks and managed like it.

TODO: this was really hard to translate and needs to be reviewed by legal I think.

Disaster Management
===================

When a disaster or catastrophe happens the typical response will be the following:

- Preparedness to assess the damage, decide if the plan should be applied and at what level, to alert customers and so on (within two hours after the situation occurred).

- Facilitation of a service level for the emergency (within six hours after the situation occurred).

- Resurrection of the service as normal (within five days after the situation occurred).

Sesam's key assets are:

- The offices.

- The cloud service provider: Microsoft Azure, data centers in the North Europe region.

When a disaster occurs these are the priorities with regards to information security (in decreasing order by priority):

- Management meeting to get an overview of the disaster. Discuss the practical short-term consequences.

- Alert the other employees about the short-term implications.

- Alert customers that are affected by the disaster.

- Work on a plan for how to get back to normal as quickly as possible.

The Management team's responsibility is to:

- Immediately respond to potential information security threats and to assess the scope of the threat and its effect on information security.

- Decide what elements in the continuity plan for information security that needs to be activated.

- Establish and administer an information security ressurection team to get back to normal operations.

- Make sure that employes get alerted and hand over responsibility and activities as needed.
