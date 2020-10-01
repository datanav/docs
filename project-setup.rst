==============================
Setting up a new Sesam project
==============================

.. contents:: Table of Contents
   :depth: 2
   :local:

Introduction
------------

When setting up a new Sesam project there are several tasks that needs to be done in order to ensure a good working environment for the project and its team. One thing is the Sesam installation itself, but in every software development project, concepts such as version control, continuous integration (CI) testing and automatic deployment are key factors for a successful project.

As a product, Sesam in itself does not contain any features that supports versioning of its configuration, local or automated CI testing and automatic deployment, but it provides a set of features (mostly through its API) that can be used in regular development tools or scripts for this purpose. This is flexible in terms of requirements set by the various customer, whose development platforms might vary. It does, however, mean that some time must be spent at the beginning of the project. In this document we will go through how to setup a Sesam project with these features, with examples and links to more in-depth documents.

.. image:: images/datahub.jpg
    :width: 800px
    :align: center
    :alt: Sesam


.. _setup_versioncontrol

Set up version control
----------------------

Sesam will always store the previous version of a pipe or system that has been uploaded to the node, in the same way it stores the previous data for an updated entity in a dataset. These entities can be found in the ''system:config'' dataset, remember to check 'system' under 'Origin' to display the system datasets. However, this only lets you view the versions of the uploaded configurations, there is nothing you can do with these entities. As so, this cannot be regarded as a proper version control of the configuration (although you can always use this dataset to retrieve the current or a previous configuration of a pipe or system).

A Sesam configuration should hence always be stored in a separate version control system such as Git, Concurrent Versions System (CVS), Subversion, TeamCity, Mercurial or others. Git is the most common used and will be used in the examples in this document, but in terms of a project, the overall handling should be the same.




.. _setup-tests:

Set up local tests
------------------

**COMING SOON**


.. _setup-ci:

Set up automatic CI testing
---------------------------

**COMING SOON**

.. _setup-deployment:

Set up automatic deployment
---------------------------

**COMING SOON**

