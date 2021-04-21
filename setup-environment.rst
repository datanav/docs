Setting up a Sesam environment
==============================

Subscriptions
-------------

To decide on the size of production and test environments for a Sesam,
on needs to consider approximate number of datatypes and total entities.

-  Medium: Up to 20 datatypes and 10 million entities.

-  Large: Up to 20 datatypes and 100 million entities.

-  Extra Large: Limitless, by dynamically expanding cluster.

The following subscriptions are necessary for a complete Sesam
environment:

-  Development: Every developer will need a small subscription, with no
   SLA or backup

-  CI-test: A small subscription, including Standard SLA

-  Test: Same size as production, including standard SLA and Backup.

-  Production: Size based on data as described above. Enterprise SLA and
   Backup.

Network connectivity
--------------------

To prepare connectivity the following the ports between connected
systems, and the the test and production environments needs to be opened
in the affected firewalls. Alternatively, a VPN connection can be
established between the Sesam service and the connected systems.

Open the ports for each of your connected systems, in addition to this
list of standard ports:

[*\* LIST OF STANRDARD PORTS \**]

Development environment
-----------------------

The recommended way to work with Sesam is to use test-driven
development. This requires that the configuration include test data for
all incoming data types. The test data allows developers to work
separately on their own Sesame subscription, testing changes locally
before propagating them to the test environment. A CI environment is
also set up to automatically verify that the integrity of existing data
is not violated before updated configuration is deployed.

1. Set up a source control system

2. Set up the CI subscription and connect it to your source control flow

3. **OPTIONAL**: Set up automatic deployment from source control

4. Ensure every developer has set up their local test environment

Security
--------

Sesam has an advanced security model that can be aligned to different
needs, but as a standard the admin needs to add users in one of two main
roles:

1. Developer – Access all data, and deploy changes to the main
   config-group

2. User – Access only data explicitly opened for them, and add their own
   config-group to set up data flows
