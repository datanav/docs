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

- Ubuntu >= 18.04 or RHEL >= 7. We prefer running Ubuntu if possible.

- Docker

- Docker-compose

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
     - Sesam uses `Let's Encrypt <https://letsencrypt.org/>`_ for SSL certificates. Letsencrypt requires port 80 to be open for incoming traffic from ANY (they don't provide a list of src IPs)  to support renewal of certificates. If you want to bring your own certificate or use a self-signed this port opening can be skipped.

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

- A working docker-compose installation

.. _self_hosted_file_structure:

File structure
==============

These steps assume that your datadisk is mounted at /srv/data.
If you want your data stored on the root-disk directly, just create the datafolder /sesam/node-00/data and skip the symbolic link.

::

    mkdir -p /srv/data/sesam/node-00/data
    mkdir -p /sesam/node-00
    ln -s /srv/data/sesam/node-00/data /sesam/node-00/data
    mkdir -p /etc/sesam-agent

License Key
===========

Sesam requires a valid license to function. Without a valid license the pipes will stop running. Instructions for obtaining a valid license key can be found in the `Sesam Portal <https://portal.sesam.io/>`__. Save the license key to the ``/srv/data/sesam/node-00/data/license.key`` file.


.. _self_hosted_docker_compose:

Docker-compose configuration
============================

::

    # IMAGE TAGS, USER_ID and HOST names is found in .env file
    version: '3'

    services:
      watchtower:
        image: containrrr/watchtower
        container_name: watchtower
        restart: always
        volumes:
          - /var/run/docker.sock:/var/run/docker.sock
        command: >
          --name sesam-node
          --name fluentbit
          --name traefik
        environment:
          - WATCHTOWER_CLEANUP=true        # Removes old images after updating
          - WATCHTOWER_POLL_INTERVAL=3600   # Check for updates every 60 minutes
          - WATCHTOWER_ROLLING_RESTART=true  # Enable rolling restarts to minimize downtime

      traefik:
        image: traefik:${TRAEFIK_DOCKER_IMAGE_TAG}
        container_name: traefik
        restart: always
        command:
          - "--providers.docker=true"
          - "--entrypoints.web.address=:80"
          - "--entrypoints.websecure.address=:443"
          - "--certificatesresolvers.myleresolver.acme.httpchallenge=true"
          - "--certificatesresolvers.myleresolver.acme.httpchallenge.entrypoint=web"
          - "--certificatesresolvers.myleresolver.acme.email=sesamadmin@sesam.io"
          - "--certificatesresolvers.myleresolver.acme.storage=/letsencrypt/acme.json"
          - "--entrypoints.web.http.redirections.entryPoint.to=websecure"
          - "--entrypoints.web.http.redirections.entryPoint.scheme=https"
        ports:
          - "80:80"
          - "443:443"
        volumes:
          - "/var/run/docker.sock:/var/run/docker.sock:ro"
          - "/srv/data/traefik/letsencrypt:/letsencrypt"
        networks:
          - sesam
          - microservices

      sesam-node:
        image: sesam/sesam-node:${SESAM_NODE_IMAGE_TAG}
        container_name: sesam-node
        restart: always
        networks:
          - sesam
          - microservices
        ports:
          - "9042:9042"
        volumes:
          - /srv/data/sesam/node-00/data:/sesam/data:rprivate
          - sesam-node-tmp:/tmp:z
          - /sesam/node-00:/sesam:rprivate
          - /var/run/docker.sock:/var/run/docker.sock:rprivate
        environment:
          - SESAM_UID=${USER_ID}
          - SESAM_GID=${USER_ID}
          - PATH=/opt/venv/bin:/opt/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
          - LANGUAGE=en_US.UTF-8
          - LANG=en_US.UTF-8
          - LC_ALL=en_US.UTF-8
          - PYTHON_EGG_CACHE=/tmp
          - PYTHONIOENCODING=UTF-8
          - ORACLE_HOME=/opt/instantclient_21_1
          - LD_LIBRARY_PATH=:/opt/instantclient_21_1
          - VIRTUAL_ENV=/opt/venv
          - CXX=g++
          - CC=gcc
          - SSL_CERT_DIR=/usr/lib/ssl/certs
          - SESAM_IMAGE_VERSION=2
        entrypoint: ["/entrypoint.sh"]
        command:
          - sh
          - -c
          - "chown -R -H ${USER_ID}:${USER_ID} /sesam/logs /sesam/data && exec gosu ${USER_ID} lake -l /sesam/logs -d /sesam/data --microservices=engine --enforce-license --sesam-portal-url https://portal.sesam.io/unified/ --redirect-portal-gui 1 -b /sesam/data/backup --backup-use-checkpoints"
        labels:
          - "traefik.enable=true"
          - "traefik.http.routers.sesam-node.rule=Host(`${NODE_DOMAIN}`)"
          - "traefik.http.routers.sesam-node.entrypoints=websecure"
          - "traefik.http.routers.sesam-node.tls=true"
          - "traefik.http.routers.sesam-node.tls.certresolver=myleresolver"
          - "traefik.http.services.sesam-node.loadbalancer.server.port=9042"

      fluentbit:
        image: sesam/fluent-bit:${FLUENTBIT_IMAGE_TAG}
        container_name: fluentbit
        restart: always
        volumes:
          - /sesam/node-00/logs:/logs/node/logs:rw
          - /var/log:/system-logs/logs:rw
          - /sesam/fluentbit/data:/data:rw
        environment:
          - APPLIANCE_ID=${APPLIANCE_ID}
          - SUBSCRIPTION_ID=${SUBSCRIPTION_ID}
          - AUTH_HEADER=${FLUENTBIT_AUTH_HEADER}
          - HOST=${FLUENTBIT_HOST}
          - PORT=443
          - TLS=on
          - FLUENTBIT_VERSION=1.9.4
        entrypoint:
          - /fluent-bit/bin/fluent-bit
        command:
          - /fluent-bit/bin/fluent-bit
          - -c
          - /fluent-bit/etc/fluent-bit.conf

    volumes:
      # Docker Volume definition for sesam-node-tmp
      sesam-node-tmp:
        driver: local

    networks:
      sesam:
        external: true
      microservices:
        external: true



Log in to `Sesam portal <https://portal.sesam.io>`_ and add your sesam-node URL to the connection under the network tab and finally upload the license.


Migrate an old installation to use docker-compose
==================================================

Be sure to back up your data before proceeding. Before :ref:`Docker-compose configuration <self_hosted_docker_compose>` section you must make sure you have done the following:

- Stop and remove all running containers.

- Copy or move the current store folder and license to the location configured under :ref:`File structure <self_hosted_file_structure>`.
