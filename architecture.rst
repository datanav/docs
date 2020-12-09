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

The infrastructure is provisioned by `Terraform <https://www.terraform.io/>`_ on `Microsoft Azure <https://azure.microsoft.com/>`_ . The default Azure region is North Europe (Ireland).

Current architecture
--------------------

This architecture is hosted on a single virtual machine. The size of the virtual machine varies between the subscription types. All software runs as Docker containers, except the agent which runs directly on the host. These subscriptions are provisioned as individual resource groups in one shared Azure subscription. Each subscription has its own Azure Network Security Group.

The services consists of the following software components:

- An agent that self-updates and makes sure that the other software that should run actually are running. It will also automatically upgrade the other software components.

- A reverse proxy that does TLS termination, traffic management and routing. The TLS certificate is automatically managed via `Let's Encrypt <https://letsencrypt.org/>`_, but it is also possible to bring your own certificates. The proxy listens to port 443 and routes traffic to the Sesam service instance.

- The Sesam service instance – commonly called "the node". This is the service that hosts the service API.

- A log shipper that ships logs. Logs are shipped to Sesam for monitoring, notification and billing purposes.

- A metrics agent that ships metrics. Metrics are shipped to Sesam for monitoring purposes.

- User-defined :ref:`microservices <microservice_system>` . The microservice systems are spun up as individual Docker containers.

New architecture
----------------

This architecture is hosted on `Kubernetes <https://kubernetes.io/>`_ and can scale out to a large number of machines. It is dynamic and can scale out as your processing requirements increase. These subscriptions will be provisioned in one Azure subscription per customer. Each subscription has its own Azure Network Security Group.

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
======

Current architecture
--------------------

Backup is performed once every 24 hours. Seven daily checkpoints are retained on the local disk if the backup policy is ``Local``. If ``Geo-redundant`` backup is enabled then the Azure VM Backup service creates a backup of the VM daily.  The ``Geo-redundant`` retension policy is to keep the last backup, 7 daily backups, 4 weekly backups and 4 monthly backups. Note that ``Geo-redundant`` backups are kept for 30 days after deletion as this is mandated by Azure. If the service is self-hosted then the owner is responsible for creating off-site backups of the checkpoint directories or the virtual machine.

New architecture
----------------

Backup is performed once every 24 hours. A ``Geo-redundant`` backup is written to the Azure subscription's Azure storage account at the same time. The ``Geo-redundant`` retension policy is to keep the last backup, 7 daily backups, 4 weekly backups and 2 monthly backups.

Firewall
========

All cloud services have an Azure Network Security Group in front. Only port 443 can be opened as this is the port used by the :doc:`service API <api>`. One has the option of blocking all public access through it or denying all except for a whitelist of ip addresses and ranges. In the new architecture it is possible to push the IP white listing down to the reverse proxy and also allow public access and restricted access to pipes through custom rules on the pipes. There are no restrictions on outgoing traffic currently.

VPN
===

You can extend Sesam into your own network using a IPSec-based Virtual Private Network. The :doc:`Sesam Management Studio <management-studio>` interface does not currently let you configure this. Please contact sales@sesam.io to configure your VPN.

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

This is a Prometheus-compatible system that pushes metrics from the local virtual machines to Sesam. The metrics include information like memory usage, disk usage and other resource usage. This information is used for monitoring and operations.


