.. _projects-infrastructure-novice-4-2:

Novice
------

.. _node-config-4-2:

Node config
~~~~~~~~~~~

.. sidebar:: Summary

  The Node config...

  - is a Sesam node´s skeletal structure
  - consists of configuration files   

The node config in a Sesam node is like its skeletal structure. An example of said skeletal structure is presented below:

::

  my-project-directory/
    ├ node/
    | ├ expected/
    | ├ pipes/
    | ├ systems/
    | ├ variables/
    | | ├ development.json
    | | ├ test.json
    | | └ production.json
    | └ node-metadata.conf.json    
    ├ README.md
    ├ LICENSE
    ├ .gitignore
    ├ test-env.json
    └ ++

The folder ``my-project-directory/`` will be your root folder. You will typically give this folder a name specific to the project you are working on, i.e: ``sesam/``. In general, it is recommended to have a total of `four Sesam nodes <https://docs.sesam.io/setup-environment.html#subscriptions>`_, which in project terms will be development, CI-test, test and production as this ensures CI/CD workflows can be carried out. Distinct to each environment you will have an environment.json file in your ``variables/`` folder. This will be elaborated on when talking about the ``node/`` folder. Finally, in the root folder, you will have files such as ``README.md``, ``LICENSE`` and ``.gitignore``. As the ``LICENSE`` and ``.gitignore`` files are quite generic, further description of these will be omitted here. The ``README.md`` file however will be specific to each project you are working on, and should ensure thorough documentation of the practices in place.  

Moving on from your root folder, the next folder will be your ``node/`` folder. This folder is the one that holds the skeletal information pertaining to all the metadata in your Sesam node. In the ``node/`` folder you will find four subfolders: ``expected/``, ``pipes/``, ``systems/`` and ``variables/`` in addition to the json file ``node-metadata.conf.json``. The subfolders only contain json files. This is an important aspect to remember, as everything in a Sesam node is json.    

The ``expected/`` folder is where all expected outputs from `outbound pipes <https://docs.sesam.io/data-modelling.html#outbound-pipes>`_ are stored. These are used by the Sesam-CLI and CI/CD workflows to verify correct outputs. This approach is described in detail here :ref:`sesam-cli-4-1`. The ``pipes/`` folder contains all your pipe files whilst the ``systems/`` folder contains all your system files. Finally, the ``variables/`` folder will contain all your defined variables files pertaining to each environment. For this example our environment is development, and as such we will be looking at the ``development.json`` file placed in the ``variables/`` folder:

.. code-block:: json

  {
    "erp_base_url": "https://my_erp_system.com/api/v1/",
    "erp_username": "test007@gmail.com",
    "salesforce_base_url": "https://salesforce.com/api/v2/",
    "salesforce_username": "test007",
    "node-env": "test"
  } 

As can be seen from the above we have defined variables for an erp and salesforce system. This should tell you that these two systems are in use in your development environment. In addition, the property ``"node-env": "test"`` tells you that in your development environment the node is using embedded data to run all its dataflows. Embedded data is synonymous with test data and is described in detail here :ref:`best-practice-inbound-pipes`. Additionally, the CI-test recommended Sesam node will have its variables defined by the file ``test-env.json`` placed in your root project folder. 

Finally, the ``node-metadata.conf.json`` is a json file that contain metadata about how a Sesam node is globally parameterized. A typical example is presented below:

.. code-block:: json

  {
    "_id": "node",
    "type": "metadata",
    "namespaced_identifiers": true
  }

The last entry in the above example ``"namespaced_identifiers": true`` is particularly important, as this entry ensures that `namespaces <https://docs.sesam.io/concepts.html#namespaces>`_ are added as data enters and moves through Sesam.

.. seealso::

  :ref:`learn-sesam` > :ref:`projects-and-infrastructure` > :ref:`projects-and-infrastructure-beginner-4-1` > :ref:`sesam-cli-4-1`

  :ref:`concepts` > :ref:`concepts-features` > :ref:`concepts-namespaces`

.. _deployment-4-2:

CI/CD Workflow
~~~~~~~~~~~~~~

.. sidebar:: Summary

  The CI/CD Workflow...

  - is the preferred method to work on a Sesam project
  - needs a configured Sesam CLI and a GIT software to operate
  - is tightly coupled with the skeletal structure of the node config
  - ensures that incremental changes can be implemented in an agile manner
  - minimizes risk of erroneous deployments damaging an ecosystem

Building upon the knowledge you just acquired reading the above section :ref:`node-config-4-2` is should now be obvious to you that Sesam advocate working in a CI/CD workflow.
In order for you to carry out said workflow you need to know just how Sesam enables this.
To start off explaining this, you should know about the :ref:`sesam-cli-4-1` and `GIT <https://git-scm.com/>`_.
GIT is a free and open source distributed version control system (VCS) and is the recommended VCS when setting up the CI/CD workflow in a Sesam project.

.. The following statement might be assuming a bit too much, but at least if you want continuous integration and deployment in a Sesam project, this is our recommended way of doing it.
.. I'm adding the comment here instead of in GitHub to presist it in case we want to rephrase later.

As such, you will want your Sesam project work to be continously integrated and continously deployed.

This ensures that incremental changes can be implemented in an agile manner and among other things,
eases the way in which teams can work together whilst also minimizing risk of erroneous deployments damaging an ecosystem.

To implement said workflow, Sesam has developed a microservice named `Github Autodeployer <https://github.com/sesam-community/github-autodeployer>`_.
This microservice connects to the GitHub API and integrates with a node config, as described in :ref:`node-config-4-2`, shared via GitHub.
The Github Autodeployer will regularly, based on a defined cron expression, compare the configuration of your Sesam node with the configuration present on GitHub.
If the two are different, the Github Autodeployer will pull the GitHub configuration and overwrite your Sesam node configuration with it.

To implement the Github Autodeployer look to the below example system configuration in Sesam:

.. code-block:: json

  {
    "_id": "github-autodeployer",
    "type": "system:microservice",
    "docker": {
      "environment": {
        "AUTODEPLOYER_PATH": "systems/github-autodeployer.conf.json",
        "BRANCH": "master",
        "DEPLOY_TOKEN": "$SECRET(sesam-autodeployer-key)",
        "GIT_REPO": "git@github.com:MITdata/sesam.git",
        "JWT": "$SECRET(autodeployer-jwt)",
        "LOG_LEVEL": "INFO",
        "SESAM_API_URL": "$ENV(sesam_base_url)",
        "SYNC_ROOT": "node",
        "TAG": "Hotfix-12.1.2",
        "VARIABLES_FILE_PATH": "/node/variables/production.json"
     },
      "image": "sesamcommunity/github-autodeployer:2.1.5",
      "port": 5000
    }
  }

From the above system configuration we will now focus on the ``environment`` dictionary part.
This part contains information that relates to a given Sesam node in addition to the folder structure in the used node config, as outlined in :ref:`node-config-4-2`.

The information relating to a Sesam node are the properties ``SESAM_API_URL`` and ``JWT``.
These properties allow you to connect to a given Sesam node's API.

With regards to the node config, the properties ``GIT_REPO``, ``SYNC_ROOT`` and ``VARIABLES_FILE_PATH`` are all related to the skeletal structure of the node config.
The ``GIT_REPO`` is equivalent to your root project folder,
whilst the ``SYNC_ROOT`` is equivalent to the ``node/`` folder whilst finally the ``VARIABLES_FILE_PATH`` defines which of the variables files,
placed in the ``variables/`` folder, should be used when the Github Autodeployer automatically uploads an updated node config to your Sesam node as you push changes via the Sesam CLI towards GitHub. 


.. caution::

  Pay attention to how changes in your pipe configurations might affect the transform state of data downstream in a dataflow, as this might require you to restart pipes.
  A pipe restart are most of the time straight forward, albeit if a lot of data must be re-transformed, estimate some time for completion.
  The pipe menu is elaborated `here <https://docs.sesam.io/management-studio.html?highlight=restart#pipe-menu>`_.

.. seealso::

  :ref:`best-practices` > :ref:`project-workflow` > :ref:`setting-up-a-new-sesam-project`

  :ref:`tools` > :ref:`sesam-management-studio` > :ref:`management-studio-pipes`

  :ref:`tools` > :ref:`sesam-client`

  `Github Autodeployer <https://github.com/sesam-community/github-autodeployer>`_

  `Sesam CLI GitHub repository <https://github.com/sesam-community/sesam-py>`_

.. _monitorering-4-2:

Monitorering
~~~~~~~~~~~~~

microservices

pipes

ekstern monitorering

Execution logs/system dataset

.. seealso::

  TODO

.. _working-methods-4-2:

Working Methods Flytte denne til Intermediate "Workflow"?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Dokumentere source-data og sink-data før en flyt

formater

datamengde

frekvens

2. Analysere innkommende data for globala dataset

3. Lage testdata

4. Drøfte behov & Løsninger

5. Velge løsning

6. Lag løsning

Mer?

.. seealso::

  TODO

.. _tasks-for-projects-infrastructure-novice-4-2:

Tasks for Projects & Infrastructure: Novice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
