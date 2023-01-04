Setting up an environment
=========================

Subscriptions
-------------

To decide on the size of production and test environments for a Sesam subscription,
one needs to consider the approximate number of datatypes and total entities.

-  Single compute: Up to 20 datatypes and 10 million entities.

-  Multi compute: Limitless, by a dynamically expanding cluster.

The following subscriptions are necessary for a complete Sesam
environment:

-  Development: Every developer will need a developer subscription, with no
   SLA or backup.

-  CI-test: A developer subscription, with no SLA.

-  Test: Same size as in production, including standard SLA and Backup.

-  Production: Size based on data as described above. Enterprise SLA and
   Backup.

Network connectivity
--------------------

To prepare connectivity the following ports between connected
systems, and the test and production environments need to be opened
in the affected firewalls. Alternatively, a VPN connection can be
established between the Sesam service and the connected systems.

Open the ports for each of your connected systems.

If you are running a self hosted Sesam, follow the instructions in the :ref:`Self Hosted Guide <self-hosted>`.

Development environment
-----------------------

The recommended way to work with Sesam is to use test-driven
development. This requires that the configuration includes test data for
all incoming data types. The test data allows developers to work
separately on their own Sesam subscription, testing changes locally
before propagating them to the test environment. A CI environment is
also set up to automatically verify that the integrity of existing data
is not violated before an updated configuration is deployed.

1. Set up a source control system. For information about how to do this for a Sesam configuration, read the :ref:`guide to set up version control <setup-version-control>`.

2. Set up the CI subscription and connect it to your source control flow. For information about to set up CI for a Sesam project, read the :ref:`guide to set up CI <setup-ci>`.

3. **OPTIONAL**: Set up automatic deployment from source control. For information about to set up this for a Sesam project, read the :ref:`guide to set up automic deployment <setup-deployment>`.

4. Ensure every developer has set up their local test environment. For how to set up local testing for test-driven development, follow the instructions in the :ref:`guide to set up local tests <setup-local-tests>`.

Security
--------

Sesam has an advanced security model that can be aligned to different
needs, but as a standard the admin needs to add users in one of two main
roles:

1. Developer – Access all data and deploy changes to the main
   config-group.

2. User – Access only data explicitly opened for them and add their own
   config-group to set up data flows.
