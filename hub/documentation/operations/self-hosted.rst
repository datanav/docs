.. _self-hosted:

===================
Self-hosted service
===================

Introduction
------------

Sesam is offered as service that is either hosted for you in the cloud or you host it yourself. We generally recommend the former, but there are scenarios where you would want to host it yourself. This document explains the requirements and the installation steps necessary to get the single-machine Sesam service running in a self-hosted environment.

.. Note::
   Self hosted subscriptions are required to run the latest image of their chosen :ref:`software channel <software-channels>`.


Hardware requirements
---------------------

We recommend setting up at least a machine with 4 CPUs, 16GB RAM and a 350GB data partition with fast storage depending on what needs you have.


Software requirements
---------------------

- Ubuntu >= 20.04 or RHEL >= 8. We prefer running Ubuntu if possible.

- Docker


Firewall requirements
---------------------

In general it is hard to be specific on IP addresses since most of these services are hosted on Content Delivery Networks (CDNs), which basically means that you have no guarantee that the IPs don't change. If you don't have a firewall that support wildcards and/or use of domain names, an option is to allow this access through a proxy.

.. _inbound_firewall_rules:

Inbound firewall rules
======================

.. list-table::
   :header-rows: 1
   :widths: 10, 15, 10, 65

   * - Port
     - Source
     - Destination
     - Description

   * - 80/HTTP
     - ANY (Public)
     - Sesam IP
     - Sesam uses Traefik to generate certificates, which requires port 80 to be open for incoming traffic from ANY (they don't provide a list of src IPs)  to support renewal of certificates. If you want to bring your own certificate or use a self-signed this port opening can be skipped.

   * - 443/HTTPS
     - Clients
     - Sesam IP
     - Any client that needs to connect to the sesam node api needs to have access to port 443 on the sesam-node IP. This does not need to happen over the internet and can be access given through local network/VPN or similar.

.. _self_hosted_outbound_firewall_rules:

Outbound firewall rules
=======================

.. WARNING::

   These outbound firewall rules must be active to operate the service. Not opening the ports for the specified domains or IPs is in violation of the terms of service.

.. list-table::
   :header-rows: 1
   :widths: 10, 15, 10, 65

   * - Port
     - Source
     - Destination
     - Description

   * - 443/HTTPS
     - Sesam IP
     - ``*.docker.com``, ``*.docker.io``
     - The sesam-node needs access to docker HUB to pull and update images used by the sesam-node and microservices.

       .. WARNING::

          If the outbound firewall is not open the service will not be able to self-update.

   * - 443/HTTPS
     - Sesam IP
     - ``*.letsencrypt.org``
     - Only needed if certificates are managed by `Certbot <https://certbot.eff.org/>`_ / `Let's Encrypt <https://letsencrypt.org/>`_ (see description on :ref:`inbound port 80 <inbound_firewall_rules>`)

       .. WARNING::

          If the outbound firewall is not open the service will not be able to update its Let's Encrypt TLS certificates.

   * - 443/HTTPS
     - Sesam IP
     - ``*.sesam.io``, ``*.sesam.cloud``
     - The sesam-node needs to communicate with several services hosted on these domains. These services include the sesam portal, log shipping, shipping metrics and sesam-agent updates.

       More information on how monitoring works can be found :ref:`here <monitoring>`.

       .. WARNING::

          If the outbound firewall is not open the service will not be able to retrieve data from the Sesam portal, and it won't be able to ship logs and metrics to Sesam. This will make notifications not work and it will break billing.

   * - 443/HTTPS
     - Sesam IP
     - ``files.pythonhosted.org``, ``pypi.org``, ``pypi.python.org``
     - The sesam-agent is a python program that has some dependencies on software that is hosted on `The Python Package Index (PyPI) <https://pypi.org/>`_.

       .. WARNING::

          If the outbound firewall is not open the service will not be able to self-update.

.. WARNING::

   ``*.sesam.io`` and ``*.sesam.cloud`` can be replaced with IPs ``137.116.234.60`` and ``52.142.116.113``. The former is for downloading and upgrading the agent, and the latter is for log shipping. We do not recommend doing this as these IPs are subject to change at any time.

Installation
------------

Before starting the setup you will  need:

- A subscription in the `Sesam portal <https://portal.sesam.io>`_

- A license key

- A docker repository login (provided by Sesam support)

- A `sesam` user on the virtual machine

.. _self_hosted_file_structure:

File structure
==============

These steps assume that your datadisk is mounted at /srv/data.
If you want your data stored on the root-disk directly, just create the datafolder /sesam/node-00/data and skip the symbolic link.

::

    mkdir -p /srv/data/sesam/node-00/data
    mkdir -p /sesam/node-00
    ln -s /srv/data/sesam/node-00/data /sesam/node-00/data

License Key
===========

Sesam requires a valid license to function. Without a valid license the pipes will stop running. 

Instructions for obtaining a valid license key can be found in the `Sesam Portal <https://portal.sesam.io/>`__. Save the license key to the ``/srv/data/sesam/node-00/data/license.key`` file.


.. _self_hosted_docker_compose:

Docker compose configuration
============================

1. Environment Setup
--------------------

1. Export the base node path:

   .. code:: bash

      export BASE_NODE_PATH='/sesam/node-00'

2. Create necessary directories:

   .. code:: bash

      sudo mkdir -p $BASE_NODE_PATH/logs
      sudo mkdir -p /srv/data/$BASE_NODE_PATH/data

3. Create a symbolic link for the data directory:

   .. code:: bash

      sudo ln -s /srv/data$BASE_NODE_PATH/data $BASE_NODE_PATH/data

4. Save the license key to the data directory:

   .. code:: bash

      sudo echo "$LICENSE" > $BASE_NODE_PATH/data/license.key

5. Create additional directories for other services:

   .. code:: bash

      sudo mkdir -p /srv/data/traefik/letsencrypt

6. Adjust ownership of directories to the ``sesam`` user:

   .. code:: bash

      sudo chown -R sesam:sesam /srv/data
      sudo chown -R sesam:sesam /sesam


--------------

2 A. Docker Setup with letsencrypt
---------------

1. Place the :download:`docker-compose.yaml<files/standard/docker-compose.yaml>` and :download:`env<files/env>` files in the ``/srv/data`` directory:

   .. code:: bash
      
      /srv/data/docker-compose.yml
      /srv/data/.env

2. Create a new unique identifier to use as APPLIANCE_ID 

   .. code:: bash
      
      uuidgen


3. Edit the ``.env`` file with the correct values

4. Create the needed networks

   .. code:: bash
      
      docker network create sesam
      docker network create microservices



2 B. Docker Setup with self provided certificates
---------------


1. Place the :download:`docker-compose.yaml<files/selfcert/docker-compose.yaml>` and :download:`env<files/env>` files in the ``/srv/data`` directory, download `traefik.yaml<files/selfcert/traefik.yaml>` and place in ``/srv/data/traefik/``   :

   .. code:: bash
      
      /srv/data/docker-compose.yml
      /srv/data/.env
      /srv/data/traefik/traefik.yaml
      /srv/data/traefik/certs/example.cert
      /srv/data/traefik/certs/example.key

2. Create a new unique identifier to use as APPLIANCE_ID 

   .. code:: bash
      
      uuidgen


3. Edit the ``.env`` file with the correct values

4. Edit the ``traefik/traefik.yaml`` file with the correct values

5. Create the needed networks

   .. code:: bash
      
      docker network create sesam
      docker network create microservices

--------------

3. Start Services
-----------------

1. Navigate to the ``/srv/data`` directory:

   .. code:: bash

      cd /srv/data

2. Start the services using Docker Compose:

   .. code:: bash

      docker compose up -d

--------------


Log in to `Sesam portal <https://portal.sesam.io>`_ and add your sesam-node URL to the connection under the network tab and finally upload the license.


Migrate an old installation to use docker compose
==================================================

Be sure to back up your data before proceeding. Before :ref:`Docker compose configuration <self_hosted_docker_compose>` section you must make sure you have done the following:

- Stop and remove all running containers.

- Copy or move the current store folder and license to the location configured under :ref:`File structure <self_hosted_file_structure>`.
