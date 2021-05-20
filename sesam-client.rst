============
Sesam Client
============

.. _concepts-sesam-client:

Introduction
============

The *Sesam client* is a command line tool for interacting with a Sesam service instance, providing a simpler way to interact with the API.

So what is it used for? When working with a Sesam project, the Sesam client is an invaluable tool for testing purposes, as well as for making the configuration available for interactions with a source control system, such as a Git repository. Note that the Sesam client itself does not contain any functionality to talk with a Git repository for instance.

When applying a new solution to a project, there is a need to perform tests on the results of your solution. If applying the solution without testing the impact of new or modified integrations, we risk affecting the data quality of other integrations connected to the pipe/pipes in question.

The Sesam client allows us to, in a quick and easy manner, to run new DTL configurations and observing the changes in output throughout the whole node. This results in both a more qualitative monitoring of changes to be implemented, but also saves time, as the Sesam client compares new output data with the old output data automatically, giving us an efficient way of testing all the potential connections inside the node. The tests are performed inside your own private Sesam instance, instead of the project instance, which enables us to test new implementations without risking the integrity of the project data.

As the Sesam client stores the pipes and system configurations, as well as the dataset output, it also serves as a version control resource where you can upload old configurations when new ones fail. This data may be uploaded to software development platforms, such as GitHub, giving everyone involved in the project access to the current setup of the node, as well as previous setups.

Sesam only supports the latest version of the client at any given time.

Note that only one instance of the sesam client can run commands on a sesam node at a time. You also need to take care when doing changes via the GUI while the client is running, as this can lead to undefined behavior.

Pre-requisites
==============

•   A personal Sesam node for testing
•   A `JWT <https://docs.sesam.io/getting-started.html#json-web-tokens>`__  (Json Web Token) made available on the personal Sesam node

The "node-id" of your private Sesam node can be found between the node name and the "Overview" link inside your node.

.. image:: images/Node_ID.png
    :width: 800px
    :align: center
    :alt: DataSet

The JWT token can be generated inside your private node under *"Settings" ----> "Subsctiption" ---> "JWT"* (see above).

To use the tool, follow the instructions in the `Github README <https://github.com/sesam-community/sesam-py>`_.