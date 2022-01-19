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

Building upon the knowledge you just acquired reading the above section :ref:`node-config-4-2` it should now be known to you that Sesam advocate working in a CI/CD workflow.
In order for you to carry out said workflow you need to know just how Sesam enables this.
To start off explaining this, you should know about the :ref:`sesam-cli-4-1` and `GIT <https://git-scm.com/>`_.
GIT is a free and open source distributed version control system (VCS) and is the recommended VCS when setting up the CI/CD workflow in a Sesam project.

As such, you will want your Sesam project work to be continously integrated and continously deployed.

This ensures that incremental changes can be implemented in an agile manner and among other things,
eases the way in which teams can work together whilst also minimizing risk of erroneous deployments damaging an ecosystem.

To implement said workflow, Sesam has developed a microservice named `Github Autodeployer <https://github.com/sesam-community/github-autodeployer>`_.
This microservice connects to the GitHub API and integrates with a node config.
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
The ``GIT_REPO`` must contain the link to the GIT repo where your project's Sesam configuration resides.
The ``SYNC_ROOT`` is equivalent to the ``node/`` folder. Finally, the ``VARIABLES_FILE_PATH`` defines which of the variables files should be used when the Github Autodeployer automatically uploads an updated node config to your Sesam node. 


.. caution::

  Pay attention to how changes in your pipe configurations might affect the transform state of data downstream in a dataflow, as this might require you to restart pipes.
  A pipe restart are most of the time straight forward, albeit if a lot of data must be re-transformed, estimate some time for completion.
  The pipe menu is elaborated in this `section <https://docs.sesam.io/management-studio.html?highlight=restart#pipe-menu>`_.

.. seealso::

  :ref:`best-practices` > :ref:`project-workflow` > :ref:`setting-up-a-new-sesam-project`

  :ref:`tools` > :ref:`sesam-management-studio` > :ref:`management-studio-pipes`

  :ref:`tools` > :ref:`sesam-client`

  `Github Autodeployer <https://github.com/sesam-community/github-autodeployer>`_

  `Sesam CLI GitHub repository <https://github.com/sesam-community/sesam-py>`_

.. _monitoring-4-2:

Monitoring
~~~~~~~~~~

.. sidebar:: Summary

  Monitoring...

  - of each node will automatically undertake periodic health checks
  - of a pipe is done for each run in the pipe execution dataset
  - of systems is done in logs and will vary depending on system type
  - externally can be implemented by requesting resources i.e: `Statuspage <https://github.com/sesam-community/statuspage>`_ and `Statuspage monitoring pipes <https://github.com/sesam-community/statuspage-monitoring-pipes>`_


Sesam generates a set of different logs. These can be found `here <https://docs.sesam.io/behind-the-scenes.html?highlight=monitoring#logs>`_. With regards to the section topic being projects and infrastructure, you will be introduced to health checks and service status in addition to the pipe execution dataset and system logs now. Additionally, you will also be presented with the microservices `statuspage <https://github.com/sesam-community/statuspage>`_ and `statuspage monitoring pipes <https://github.com/sesam-community/statuspage-monitoring-pipes>`_ as means of external monitoring.

Health checks and Service status
################################

Each node will automatically undertake periodic health checks. These health checks ensure Sesam's product team can act if any node behaves unexpectedly. The service status aspect is composed of status codes which is used in parrallel with these health checks.

Pipe execution dataset
######################

The pipe execution dataset keeps a record after each pump run of a given pipe. This dataset is in the shape of a json file. An example os said file can be seen below:

.. code-block:: json

  {
    "_id": "pump-failed",
    "_updated": 953,
    "_previous": 951,
    "_deleted": false,
    "_ts": 1642412027429326,
    "_hash": "f0b5ae4f77c6867a439b203c944a9225",
    "end_time": "2022-01-17T09:33:47.427823Z",
    "event_type": "pump-failed",
    "exception_entity": {
      "salesforce-account:results": [
        {
          "salesforce-account:id": 1,
          "salesforce-account:name": "MIT",
          "salesforce-account:owner": "Nohar Vard",
          "salesforce-account:progress_state": 1
        },
        {
          "salesforce-account:id": 2,
          "salesforce-account:name": "Harvard",
          "salesforce-account:owner": "Nom It",
          "salesforce-account:progress_state": 2
        }
      ]
    },
    "metrics": {
      "entities": {
        "changes_last_run": 0,
        "entities_last_run": 0,
        "entities_per_second": 0,
        "read_errors_last_run": 0,
        "sink_time": 0,
        "source_time": 0.00008929986506700516,
        "transform_time": 0,
        "write_errors_last_run": 0
      }
    },
    "next_interval": 927.09,
    "node_build_info": {
      "build": "220106.961",
      "date": "2022-01-06T17:15:10.342885+00:00",
      "dirty": false,
      "git-revision": "ff9500371",
      "hash": "ff9500371",
      "release": "1.0",
      "teamcity-buildnumber": "220106.961",
      "version": "1.0.220106.961"
    },
    "original_error_message": "",
    "original_traceback": "",
    "pipe": "mssql-accounts-2",
    "pipe_offset": "",
    "pump_definition": "pump:salesforce-account",
    "pump_started_location": 952,
    "reason_why_stopped": "DTL transform failed with error: Target entity _id missing or is of invalid type: None",
    "retry_entities_exist": false,
    "start_time": "2022-01-17T09:33:47.365728Z",
    "sync_type": "full",
    "total_time": 0.062095,
    "traceback": "Traceback (most recent call last):\n  File \"/opt/venv/lib/python3.9/site-packages/lake/task/datasynctask/datasynctask.py\", line 2862, in _run_task\n    full_data_set = self.do_sync()\n  File \"/opt/venv/lib/python3.9/site-packages/lake/task/datasynctask/datasynctask.py\", line 1986, in do_sync\n    raise e\n  File \"/opt/venv/lib/python3.9/site-packages/lake/task/datasynctask/datasynctask.py\", line 1959, in do_sync\n    self._do_sync_step5_handle_results()\n  File \"/opt/venv/lib/python3.9/site-packages/lake/task/datasynctask/datasynctask.py\", line 2557, in _do_sync_step5_handle_results\n    if process_batch(entity_batch):\n  File \"/opt/venv/lib/python3.9/site-packages/lake/task/datasynctask/datasynctask.py\", line 2533, in process_batch\n    _entity_batch = self._do_sync_step3_transforms(_entity_batch)\n  File \"/opt/venv/lib/python3.9/site-packages/lake/task/datasynctask/datasynctask.py\", line 2169, in _do_sync_step3_transforms\n    entity_batch = pipe.transform.transform(entity_batch, metrics=self.metrics)\n  File \"/opt/venv/lib/python3.9/site-packages/lake/transforms/dtl_transform.py\", line 1517, in transform\n    transformed_entity_batch = self.cpp_transform(environment, entity_batch)\n  File \"lake/rapids/transforms/dtl_transform.pyx\", line 47, in lake.rapids.rapids_c.CppDTLTransform.cpp_transform\n  File \"lake/rapids/transforms/dtl_transform.pyx\", line 55, in lake.rapids.rapids_c.CppDTLTransform.cpp_transform\nlake.node.exceptions.TransformException: DTL transform failed with error: Target entity _id missing or is of invalid type: None"
  }

As can be seen from the above dataset, this is a ``pump-failed`` entity. Sesam also produces entities for each ``pump-started`` and ``pump-completed`` run in the execution dataset. Generally speaking it will often times be most relevant to look at ``pump-failed``datasets as for example a ``pump-completed`` will just tell you that everything ran as expected.

From the ``pump-failed`` entity presented above, you will see the properties ``reason_why_stopped`` and ``traceback``. The ``reason_why_stopped`` property provides a brief description of why the pump failed whilst the ``traceback`` property provides a more detailed description of why the pump failed. In general, the property ``reason_why_stopped`` is a good first candidate to check when a pipe fails its run. In terms of automating monitoring you can set up mail notification when line of business related pipes fail a given run. This allows you to act quickly if fails should occur.  

System logs
###########

System logs, as opposed to the execution dataset, varies depending on which system you are looking at. Some systems will only return a status code in its logs, i.e: an :ref:`oracle_system` will return 200 if everything is fine. This is however not the case for the :ref:`microservice_system`. A microservice system will have user defined logging and can therefore vary quite a bit.

User defined logging should consider the following:

  - status codes
  - declarative and precise error messages
  - critical steps in logic

External monitoring
###################

External monitoring can be implemented by requesting resources from the :ref:`api-top`. This has been done in the microservices: `Statuspage <https://github.com/sesam-community/statuspage>`_ and `Statuspage monitoring pipes <https://github.com/sesam-community/statuspage-monitoring-pipes>`_ which connects to the Statuspage API in addition the Service API in Sesam.

The Statuspage microservice monitors a Sesam node's health whereas the Statuspage monitoring pipes microservice monitors pipes. What is convenient about the Statuspage API is that it provides the user with an overview of monitored instances in addition to sending out emails when and if a monitored instance fails.  

.. seealso::

  :ref:`sesam-community`

  `Sesam's community at GitHub <https://github.com/sesam-community>`_

  `Statuspage <https://github.com/sesam-community/statuspage>`_

  `Statuspage monitoring pipes <https://github.com/sesam-community/statuspage-monitoring-pipes>`_

  :ref:`developer-guide` > :ref:`configuration` > :ref:`system_section`

  :ref:`developer-guide` > :ref:`api-top`

  :ref:`monitoring`

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
