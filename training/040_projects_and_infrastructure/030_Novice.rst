.. _projects-infrastructure-novice-4-2:

Novice
------

.. _node-config-4-2:

Node config
~~~~~~~~~~~

The node config in a Sesam node is like its skeletal structure. An example of said skeletal structure is presented below:

.. code-block::

  my-project-directory/
    ├ node/
    | ├ expected/
    | ├ pipes/
    | ├ systems/
    | └ variables/
    ├ README.md
    ├ LICENSE
    ├ .gitignore
    └ ++

The folder ``my-project-directory/`` will be your root folder. You will typically give this folder a name specific to the project and environment you are working on, i.e: ``sesam-development/``. In general, it is recommended to have a total of three Sesam nodes, which in project terms would be ``development/``, ``test/`` and ``production/``. For this example we are illustrating a workflow going from our ``sesam-development/`` project to our ``sesam-test/`` project. In addition, you will have files such as README.md, LICENSE and .gitignore placed in the root folder as well. As these files are generic, further description of these will be omitted for now. 

Moving on from your root folder, the next folder will be your ``node/`` folder. This folder is the one that holds the skeletal information pertaining to all the metadata in your Sesam node. In the ``node/`` folder you will find four subfolders: ``expected/``, ``pipes/``, ``systems/`` and ``variables/``. All of these subfolders only contain json files. This is an important aspect to remember, as everything in a Sesam node is json.    

The ``expected/`` folder has to be created when first downloading the node config via the Sesam-CLI. This approach is described in detail here :ref:`sesam-cli-4-1`. The ``expected/`` folder is used as a folder for all your json files used for running tests via the Sesam-CLI. The ``pipes/`` folder contains all your pipe json files whilst the ``systems/`` folder contains all your system json files. Finally, the ``variables/`` folder will contain all your defined variables. These are also provided in a json file.         



Mappestruktur, expected folder, node-metadata.conf.json

Mappestruktur

System

Pipes

Node-metadata.conf.json

+expected

Global metadata

Namespaces

Tag for å inkludere c++ ext.

Dependency tracking hops limit

signalling

Referer mye til dokumentasjon

.. seealso::

  TODO

.. _deployment-4-2:

Deployment
~~~~~~~~~~

Når trenger man å resette pipes?/Når trenger man ikke det

Update last seen

reset to end

reset

Disable/enable pipes (spesifik endpoint)

Indexering

.. seealso::

  TODO

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
