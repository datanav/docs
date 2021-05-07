============
Sesam Client
============

.. contents:: Table of Contents
   :depth: 2
   :local:

.. _concepts-sesam-client:

Introduction
============

The *Sesam client* is a command line tool for interacting with a Sesam service instance, providing a simpler way to interact with the API. The client requires python3 to work and can be installed using Pip.

So what is it used for? When working with a Sesam project, the Sesam client is an invaluable tool for testing purposes, as well as for making the configuration available for interactions with a source control system, such as a Git repository. Note that the Sesam client itself does not contain any functionality to talk with a Git repository for instance.

When applying a new solution to a project, there is a need to perform tests on the results of your solution. If applying the solution without testing the impact of new or modified integrations, we risk affecting the data quality of other integrations connected to the pipe/pipes in question.

The Sesam client allows us to, in a quick and easy manner, to run new DTL configurations and observing the changes in output throughout the whole node. This results in both a more qualitative monitoring of changes to be implemented, but also saves time, as the Sesam client compares new output data with the old output data automatically, giving us an efficient way of testing all the potential connections inside the node. The tests are performed inside your own private Sesam instance, instead of the project instance, which enables us to test new implementations without risking the integrity of the project data.

As the Sesam client stores the pipes and system configurations, as well as the dataset output, it also serves as a version control resource where you can upload old configurations when new ones fail. This data may be uploaded to software development platforms, such as GitHub, giving everyone involved in the project access to the current setup of the node, as well as previous setups.

Sesam only supports the latest version of the client at any given time.

Note that only one instance of the sesam client can run commands on a sesam node at a time. You also need to take care when doing changes via the GUI while the client is running, as this can lead to undefined behavior.

How to use the Sesam client
===========================

Before you start using the Sesam client make sure you have the following ready:

•   Sesam client is available on github (https://github.com/sesam-community/sesam-py). Read about Installation and configuration further down
•   A personal Sesam node for testing
•   A `JWT <https://docs.sesam.io/getting-started.html#json-web-tokens>`__  (Json Web Token) made available on the personal Sesam node
•   A git clone of the repository you wish to work on
•   Initial test setup (task "setting up tests in new projects” in Teams. text to be written)
•   A ".syncconfig" file should be placed in the same folder as the "pipes", "systems" and "variables" folders in your github clone. The content of the file should be on the form;

    ``node=’https://<node-id>.sesam.cloud’
    JWT=’<your-JWT>’``

The "node-id" of your private Sesam node can be found between the node name and the "Overview" link inside your node.

.. image:: images/Node_ID.png
    :width: 800px
    :align: center
    :alt: DataSet

The JWT token can be generated inside your private node under *"Settings" ----> "Subsctiption" ---> "JWT"* (see above).

Then add another folder named "expected" in the same folder as the ".syncconfig" file.

After we have installed Sesam client via pip, we need to configure it. You can read about this here as seen below.

Installation
============

You can either run the sesam.py script directly using python, or you can download and run a stand alone binary from `Github Releases <https://github.com/sesam-community/sesam-py/releases/>`__

To install and run the sesam client with python on Linux/OSX (python 3.5+ required):

::

    $ cd sesam
    $ virtualenv --python=python3 venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt
    $ python sesam.py -version
    sesam version 1.0.0

Configuration
=============

When running the sesam client for the first time, use this command:

::

    $ sesam init

- Enter your Sesam username and press enter, enter your passord and press enter.

- You will then get a list of the various Sesam subscriptions you are a member of. The Sesam client will then ask which Subscription to use? Type in the number corresponding to the subscription you want to connect to, this will typically be your dev node.

- The Sesam client will respond by writing "Config stored in .sesam/config." and then you are ready to go.


Typical workflow
================

•   Start with making sure your GitHub repository is up-to-date.
•   Run the **"sesam test -use-internal-scheduler"** command to ensure that the results from the local repository matches the output of the configuration files. The "-use-internal-scheduler" tag ensures a faster test than without since without it the Sesam client needs to run several operations "behind-the-scene" to execute all pipes.
• The **"sesam test"** command actually runs three different commands:

    ◦ **"sesam upload"**: loads the local configs to the private Sesam node

    ◦ **"sesam run"**: runs the configs inside the local Sesam node and populates the datasets

    ◦ **"sesam verify’"**: matches the output from the current configurations in the private Sesam node with the output in the "expected" folder on the local repository

•   When this is done, create a new local git branch where you can store your future changes
•   Make changes to the configs inside your Sesam node
•   When you are content with your changes, run the command **"sesam download"**. This will pull all the current configs on your node down to the local repository, which you   will need when updating the git repository (explained further down)
•   To check changes in output, run the command **"sesam test -user-internal-scheduler"** again
•   If the changes in output are expected/acceptable, run the command **"sesam update"** to update the output in the "expected" folder to the current output in the private Sesam node. If the output is not expected/acceptable, go back to the private Sesam node and make the necessary adjustments and repeat the last three point (starting with "sesam download")
•   Commit changes and push them [link to git-section?] to the corresponding git repository

Other useful commands:

    •   Adding either -v, -vv or -vvv after your command will yield further information regarging the workings of the Sesam client. **-v** will yield some extra information, **-vv** will yield some more extra information while **-vvv** will yield maximum information.
    •   **"status"** will test if the local configs are up-to-date with the node configs.
    •   **"wipe"** will wipe your private node clean of configs
    •   **-print-scheduler-log** is used with the commands **"sesam run"** or **"sesam test"**. Prints the logs of the scheduler.

For further commands available through the Sesam client, run the command **"sesam -h"**
