.. _setup-version-control:

-----------------------------------------
Using Sesam with a version control system
-----------------------------------------

Internal versioning
-------------------

Sesam will always store the previous version of a pipe or system that has been uploaded to the node, in the same way it stores the previous data for an updated entity in a dataset. You can view these entities by going to the ''internal datasets'' pane under ''Subscription''-settings, they will be located in the ''system:config'' dataset. Note that there is nothing you can do with these entities, as this is just a view of the versions of the uploaded configurations. Hence this cannot be regarded as a proper version control of the configuration (although you can always use this dataset to retrieve the current or a previous configuration of a pipe or system). You can also view the previous configurations for each pipe or system in the editor.

A Sesam configuration should then always be stored in a separate version control system such as Git, Concurrent Versions System (CVS), Subversion, TeamCity, Mercurial or other.

Downloading your Sesam configuration to your local version control system repository
------------------------------------------------------------------------------------

A Sesam configuration can be exported to a directory structure by using either the Sesam :ref:`client <concepts-sesam-client>`, API or portal. The exported directory structure should be located under your local copy of the repository of your chosen version control system.

The basic structure of an exported Sesam configuration is as follows:
::

	├ pipes
	| └ ++
	├ systems
	| └ ++
	└ ++

However, depending on your version control system and how you structure your repository, there might be some additional files and folders that needs to be added. 

For instance we recommend using this directory structure if your version control system is Git:
::

    my-project-directory
      ├ expected
      ├ pipes
      ├ systems
      ├ variables
      ├ README.md
      ├ LICENSE
      ├ .gitignore
      └ ++

Recommended workflow for a Sesam project
----------------------------------------

We strongly promote using the `Github-Flow <https://guides.github.com/introduction/flow/>`_ as workflow for working with Sesam projects. To add a version number or tag to release we recommend using `semantic versioning <https://semver.org>`_.
