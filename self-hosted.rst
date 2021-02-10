===================
Self-hosted service
===================

.. contents:: Table of Contents
   :depth: 2
   :local:

Introduction
------------

Sesam is offered as service that is either hosted for you in the cloud or you host it yourself. We generally recommend the former, but there are scenarios where you would want to host it yourself. This document explains the requirements and the installation steps necessary to get the single-machine Sesam service running in a self-hosted environment.


Hardware requirements
---------------------

We recommend setting up at least a machine with 4 CPUs, 16GB RAM and 350GB fast storage depending on what needs you have.

Software requirements
---------------------

- Ubuntu >= 18.04 or RHEL >= 7. We prefer running Ubuntu if possible.
  
- Python3
  
- Sesam will install the *sesam-agent* which in turn will setup and configure docker.

Firewall requirements
---------------------

In general it is hard to be specific on IP addresses since most of these services are hosted on CDNs which basically means that you have no guarantee that the IPs don't change. If you don't have a firewall that support wildcards and/or use of domain names, an option is to allow this access through a proxy.

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

Outbound firewall rules
=======================

.. WARNING::

   These outbound firewall rules must be active for the service to operate fully. Not opening the ports for the specified domains may violate the terms of service. 

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
     - Only needed if certificates are managed by certbot/letsencrypt (see DESC on port 80 inbound)

       .. WARNING::

          If the outbound firewall is not open the service will not be able to update its Let's Encrypt TLS certificates.

   * - 443/HTTPS
     - Sesam IP
     - ``*.sesam.io``, ``*.sesam.cloud``
     - The sesam-node needs to communicate with several services hosted on these domains. These services include the sesam portal, log shipping, shipping metrics and sesam-agent updates.

       .. WARNING::

          If the outbound firewall is not open the service will not be able to retrieve data from the Sesam portal, and it won't be able to ship logs and metrics to Sesam. This will make notifications not work and it will break billing.

   * - 443/HTTPS
     - Sesam IP
     - ``files.pythonhosted.org``, ``pypi.org``
     - The sesam-agent is a python program that has some dependencies on software that is hosted on [pypi](https://pypi.org/).

       .. WARNING::

          If the outbound firewall is not open the service will not be able to self-update.

Installation
------------

Before starting the setup you will  need:

- A subscription in the `Sesam portal <https://portal.sesam.io>`_

- A license key
  
- A docker repository login (provided by Sesam support)
  
- A sesam-agent config (example below)

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

Agent Configuration File
========================

Example config file (must be located at /etc/sesam-agent/config.json)

::

    {
      "docker_username": "sesamonprem",
      "docker_password": "<TOKEN>",
      "nginx": {
        "disable": false
      },
      "sesam-node": {
        "args": "--sesam-portal-url https://portal.sesam.io/unified/ --redirect-portal-gui 1 -b /sesam/data/backup --backup-use-checkpoints ",
        "tag": "weekly-prod"
      }
    }

.. _self_hosted_install_the_agent:

Install the Agent
=================

::

    sudo wget https://downloads.sesam.io/agent/sesam-agent -O /sbin/sesam-agent
    sudo chmod +x /sbin/sesam-agent
    sudo /sbin/sesam-agent install
    sudo /sbin/sesam-agent start

Log in to `Sesam portal <https://portal.sesam.io>`_ and add your sesam-node URL to the connection under the network tab and finally upload the license.

Bring your own certificate
==========================

In order to serve the node with your own certificate you will need a valid password-less KEY and a cert in PEM format. If your certificate is password protected you can remove the password with openssl or equivalent tools.

Give your cert and key a name and place them in the ``/sesam/nginx/conf/ssl`` folder (``privkey.pem`` and ``fullchain.pem`` in this example).

Update the Sesam configuration file (``/etc/sesam-agent/config.json``) to include the path to the keys in the nginx section:

::

    "nginx": {
      "ssl_cert": "/etc/nginx/includes.d/ssl/fullchain.pem",
      "ssl_key": "/etc/nginx/includes.d/ssl/privkey.pem"
    }

Restart nginx for things to take effect: 

::

    docker restart nginx

Migrate an old installation to use the sesam-agent
==================================================

Be sure to back up your data before proceeding. Before :ref:`Install the Agent <self_hosted_install_the_agent>` section you must make sure you have done the following:

- Stop and remove all running containers.
  
- Copy or move the current store folder and license to the location configured under :ref:`File structure <self_hosted_file_structure>`.
