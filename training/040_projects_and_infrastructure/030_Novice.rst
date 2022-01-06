.. _projects-infrastructure-novice-4-2:

Novice
------

.. _node-config-4-2:

Node config
~~~~~~~~~~~

.. sidebar:: Summary

  The Node config ...

  - is a Sesam node´s skeletal structure
  - should mirror your project environment

    - recommended environments are:

      - development
      - test
      - production

  - consists of global and local configuration files   

The node config in a Sesam node is like its skeletal structure. An example of said skeletal structure is presented below:

``
  my-project-directory/
    ├ node/
    | ├ expected/
    | ├ pipes/
    | ├ systems/
    | ├ variables/
    | └ node-metadata.conf.json    
    ├ README.md
    ├ LICENSE
    ├ .gitignore
    └ ++
``

The folder ``my-project-directory/`` will be your root folder. You will typically give this folder a name specific to the project and environment you are working on, i.e: ``sesam-development/``. In general, it is recommended to have a total of three Sesam nodes, which in project terms would be ``development/``, ``test/`` and ``production/`` as this ensures CI/CD workflows can be carried out. For this example our environment is development, and as such we will be looking at the ``sesam-development/`` project for now. Finally, in the root folder, you will have files such as README.md, LICENSE and .gitignore. As these files are generic, further description of these will be omitted for now. 

Moving on from your root folder, the next folder will be your ``node/`` folder. This folder is the one that holds the skeletal information pertaining to all the metadata in your Sesam node. In the ``node/`` folder you will find four subfolders: ``expected/``, ``pipes/``, ``systems/`` and ``variables/`` in addition to the json file ``node-metadata.conf.json``. The subfolders only contain json files. This is an important aspect to remember, as everything in a Sesam node is json.    

The ``expected/`` folder has to be created when first downloading the node config via the Sesam-CLI. This approach is described in detail here :ref:`sesam-cli-4-1`. The ``expected/`` folder is used as a folder for all your json files used for running tests via the Sesam-CLI. The ``pipes/`` folder contains all your pipe json files whilst the ``systems/`` folder contains all your system json files. Finally, the ``variables/`` folder will contain all your defined variables. These are also provided in a json file. Finally, the ``node-metadata.conf.json`` is a json file that contain metadata about how a Sesam node is globally parameterized. A typical example is presented below:

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
