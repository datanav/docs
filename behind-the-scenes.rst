=================
Behind the scenes
=================

.. contents:: Table of Contents
   :depth: 1
   :local:

Introduction
============

There are two types of Sesam service architectures: single machine and clustered. The single machine setup runs the Sesam service on a single virtual machine. The subscription types *Small*, *Medium* and *Large* are all of this type. Note that the *Small* type is for development use only. The *Extra Large* subscription type uses the clustered setup and can scale to a large number of machines. In the future we aim to host all subscription types on the same architecture. Both setups use container runtimes to host the service.

The Sesam software is distributed as standard `OCI images <https://opencontainers.org/>`_ (aka Docker images). The container images are hosted on `Docker Hub <https://hub.docker.com/>`_ in a private repository.

The infrastructure is provisioned by `Terraform <https://www.terraform.io/>`_ on `Microsoft Azure <https://azure.microsoft.com/>`_ . The default Microsoft Azure region is North Europe (Dublin, Ireland). The data never leaves this region. The data is encrypted at rest using a key managed by Microsoft Azure. Bringing your own key is currently not yet supported.

Sesam uses `RocksDB <https://rocksdb.org/>`_, an embedded high-performance key-value database, to persist data. The data
is stored in the compact `MessagePack <https://msgpack.org/>`_ data format, and is further compressed using
RocksDB's default `compression <https://github.com/facebook/rocksdb/wiki/Compression/>`_ settings.


.. single_arch:

Single machine service
======================

This service is hosted on a single virtual machine. The size of the virtual machine varies between the subscription types. All software runs as Docker containers, except the agent which runs directly on the host. These subscriptions are provisioned as individual resource groups in one shared Azure subscription. Each subscription has its own Azure Network Security Group. Data is stored on managed network disks. 

The services consists of the following software components:

- An agent that self-updates and makes sure that the other software that should run actually are running. It will also automatically upgrade the other software components.

- A reverse proxy that does TLS termination, traffic management and routing. The TLS certificate is automatically managed via `Let's Encrypt <https://letsencrypt.org/>`_, but it is also possible to bring your own certificates. The proxy listens to port 443 and routes traffic to the Sesam service instance.

- The Sesam service instance – commonly called "the node". This is the service that hosts the service API.

- A log shipper that ships logs. Logs are shipped to Sesam for monitoring, notification and billing purposes.

- A metrics agent that ships metrics. Metrics are shipped to Sesam for monitoring purposes.

- User-defined :ref:`microservices <microservice_system>` . The microservice systems are spun up as individual Docker containers.

.. _single_arch_backup:

Backup
------

Backup is performed once every 24 hours. Seven daily checkpoints are retained on the local disk if the backup policy is ``Local``. If ``Geo-redundant`` backup is enabled then the Azure VM Backup service creates a backup of the VM daily.  The ``Geo-redundant`` retension policy is to keep the last backup, 7 daily backups, 4 weekly backups and 4 monthly backups.

Note that ``Geo-redundant`` backups are kept for 30 days after deletion as this is mandated by Azure. If the service is self-hosted then the owner is responsible for creating off-site backups of the checkpoint directories or the virtual machine.

.. _multi_arch:

Clustered service
=================

This service is hosted on `Kubernetes <https://kubernetes.io/>`_ and can scale out to a large number of machines. It is dynamic and can scale out as your processing requirements increase. These subscriptions will be provisioned in one Azure subscription per customer. Each subscription has its own Azure Network Security Group. Data is stored on local NVMe disks and/or managed network disks. 

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
------

Backup is performed once every 24 hours. A ``Geo-redundant`` backup is written to the Azure subscription's Azure storage account at the same time. The ``Geo-redundant`` retension policy is to keep the last backup, 7 daily backups, 4 weekly backups and 2 monthly backups.

.. _monitoring:

Monitoring
==========

Logs
----

The following kinds of logs are shipped to Sesam:

- Service logs. This includes error messages.
  
- Health checks and service status.
  
- Sesam configuration. No sensitive data is shipped, so no embedded data nor secrets are shipped. 
  
- The pipe execution dataset. This is only shipped when pipe monitoring is enabled. It is used to trigger notifications for registered notification rules. Execution logs regarding failing pipes contain the entity objects which caused the failure, however these objects are not shipped to Sesam.
  
- System logs, currently only the kernel logs are shipped. 

Metrics
-------

This is a Prometheus-compatible system that pushes telemetry data from the local virtual machines to Sesam. The metrics include information like memory usage, disk usage and other resource usage. This information is used for monitoring and operations.

Isolation
=========

Subscriptions are segregated and run on separate isolated hardware. Subscriptions under the same *subscription group* share a common network. In the :ref:`clustered service <multi_arch>` a subscription group exists inside its own Azure subscription.

Firewall
========

All cloud services have an Azure Network Security Group in front. Only port 443 can be opened as this is the port used by the :doc:`service API <api>`. 

Termination
===========

When a subscription is terminated all data in it is deleted. Backups are deleted, but in the case of Azure backups as described in the :ref:`single machine service <single_arch_backup>` those backups are retained for 30 days after deletion. 

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
