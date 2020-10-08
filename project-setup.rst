------------------------------
Setting up a new Sesam project
------------------------------

When setting up a new Sesam project there are several tasks that needs to be done in order to ensure a good working environment for the project and its team. One thing is the Sesam installation itself, but in every software development project, concepts such as version control, continuous integration (CI) testing and automatic deployment are key factors for a successful project.

As a product, Sesam in itself does not contain any features that supports versioning of its configuration, local or automated CI testing and automatic deployment, but it provides a set of features (mostly through its API) that can be used in regular development tools or scripts for this purpose. This is flexible in terms of requirements set by the various customer, whose development platforms might vary. It does, however, mean that some time must be spent at the beginning of the project. In this document we will go through how to setup a Sesam project with these features, with examples and links to more in-depth documents.

.. _setup-version-control:

Set up version control
----------------------

Sesam will always store the previous version of a pipe or system that has been uploaded to the node, in the same way it stores the previous data for an updated entity in a dataset. These entities can be found in the ''system:config'' dataset, remember to check 'system' under 'Origin' to display the system datasets. However, this only lets you view the versions of the uploaded configurations, there is nothing you can do with these entities. As so, this cannot be regarded as a proper version control of the configuration (although you can always use this dataset to retrieve the current or a previous configuration of a pipe or system).

A Sesam configuration should hence always be stored in a separate version control system such as Git, Concurrent Versions System (CVS), Subversion, TeamCity, Mercurial or other. Git is the most commonly used and will be used in the examples in this document, but in terms of a project, the overall handling should be the same.

We will describe how to set up a version control repository for Sesam with Git in mind, but the overall way of how to work with branches and flows in another version control system should be the same.


Initial repository setup
========================

The initial repository should contain two main branches with an infinite lifetime.
Parallel to the master branch, another branch should exist, called develop.

*master*

*develop*

We consider origin/master to be the main branch where the source code always reflects a production-ready state.
We consider origin/develop to be the main branch where the source code always reflects a state with the latest delivered development changes for the next release. Some would call this the “integration branch”.

When the source code in the develop branch reaches a stable point and is ready to be released, all of the changes should be merged back into master branch and then tagged with a release number.

Therefore, each time when changes are merged back into master, this is a new production release by definition.
We follow this practice very strictly.

**Supporting branches**

Next to the main branches master and develop, our development model uses a variety of supporting branches to aid parallel development between team members, ease tracking of features, prepare for production releases and to assist in quickly fixing live production problems.

Unlike the main branches, these branches always have a limited life time, since they will be removed eventually.

The different types of branches we may use are:

*Feature branches*

*Release branches*

*Hotfix branches*

Each of these branches have a specific purpose and are bound to strict rules as to which branches may be their originating branch and which branches must be their merge targets.

+-------------+----------------------+-----------------------+-----------------------------------------------------------+
| Branch Type | May branch off from  | Must merge back into  | Branch naming convention                                  |
+-------------+----------------------+-----------------------+-----------------------------------------------------------+
|Feature      | develop              | develop               | Aything except master, develop, release-*, or hotfix-*    |
+-------------+----------------------+-----------------------+-----------------------------------------------------------+
|Release      | master               | develop and master    | release-*                                                 |
+-------------+----------------------+-----------------------+-----------------------------------------------------------+
|Hotfix       | master               | develop and master    | hotfix-*                                                  |
+-------------+----------------------+-----------------------+-----------------------------------------------------------+

**One exception to the rule here is that, when a release branch currently exists, the hotfix changes need to be merged into that release branch, instead of develop.**

For information on how to set up the master branch in Git, read :ref:`here<git-master-branch>`.
For information on how to set up the development branch in Git, read :ref:`here<git-development-branch>`.

Versioning of releases
======================

You should use `semantic versioning <https://semver.org>`_ for any of your releases to production.

Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible changes to the configuration,
2. MINOR version when you add functionality in a backwards compatible manner, and
3. PATCH version when you make backwards compatible bug fixes

.. _setup-local-tests:

Set up local tests
------------------

In a normal workflow you should test your local changes before committing them to a repository. For setting up local testing of a Sesam configuration we recommend using the Sesam client, which is a command line tool for interacting with a Sesam service instance. To install and configure the Sesam client, read this :ref:`document <concepts-sesam-client>`.

Testing a Sesam configuration should be done by running all the pipes in your local node until no pipes has any entities left in their queues, except the output pipes (which should either be disabled or unable to send data to their respective systems). Doing this manually could hence be a tedious job, especially if your configuration consists of numerous pipes, having to repeatedly start all or several pipes. The output of the endpoint pipes should then be verified against the expected output of the pipes. The Sesam client includes a nifty feature for this, both for running the pipes to their conclusion and verifying the end result.

Configuring tests
=================

However, for this to work, you have to configure your Sesam configuration with a test-file for each endpoint pipe. In the same directory as you have your 'pipes' and 'systems' folders, you need to add a new folder named 'expected', this will be the folder that contains the test files and the expected result for each pipe.

For each endpoint pipe in your Sesam configuration, you need to add two files (replace <name_of_pipe> with the name of the pipe):

	* <name_of_pipe>.json
	* <name_of_pipe>.test.json

The file with the .json extension is the file that shall contain the expected result. The file with the .test.json extension should contain the test configuration for that pipe, the available settings for this file are listed below:

.. list-table::
   :header-rows: 1
   :widths: 10, 25, 10, 10, 30

   * - Property
     - Description
     - Type
     - Required 
     - Default 

   * - ``_id``
     - | Name of the test.
     - | ``string``
     - |  No
     - |  Name of the ``.test.json file``

   * - ``type``
     - | Config type so that this later can just be part of the rest of the config.
     - | ``string``
     - |  No
     - |  Test

   * - ``description``
     - | A description of the test.
     - | ``string``
     - |  No
     - |  

   * - ``ignore``
     - | If the output should be ignored during tests.
     - | ``boolean``
     - |   No
     - | ``false``

   * - ``endpoint``
     - | If the output should be fetched from a published endpoint instead.
     - | ``string``
     - |   No
     - | By default the json is grabbed from ``/pipes/<my-pipe>/entities``

   * - ``stage``
     - | In which pipe stage to get the entities (source/before-transform/after-transform/sink).
     - | ``string``
     - |   No
     - | By default the stage is ``sink``

   * - ``file``
     - | File that contains the expected results.
     - | ``string``
     - |   No
     - | Name of the .test.json file without .test (e.g. foo.test.json looks for foo.json).

   * - ``pipe``
     - | Pipe that contains the output to test.
     - | ``string``
     - |   No
     - | Name of the .test.json file without .test (e.g. foo.test.json looks for foo.json).

   * - ``blacklist``
     - | Properties to ignore in the output.
     - | ``Array of strings``
     - |   No
     - | ``[]``

   * - ``parameters``
     - | Which parameters to pass as bound parameters. Note that parameters only works for published endpoints.
     - | ``Object``
     - |   No
     - | ``{}``

Example: 

::

    {
    	$ cat foo.test.json
        {
	      "_id": "foo",
	      "type": "test",
	      "file": "foo.json"
	      "blacklist": ["my-last-updated-ts"],
	      "ignore": false
        }
    }

DTL parameters
==============

If you need to pass various variations of bound parameters to the DTL, you just create multiple .test.json files for each combination of parameters.

Example:

::
    
    {
    	$ cat foo-A.test.json
	    {
	      "pipe": "foo",
	      "file": "foo-A.xml",
	      "endpoint": "xml",
	      "parameters": {
	      	"my-param": "A"
	      }
	    }

    	$ cat foo-B.test.json
	    {
	      "pipe": "foo",
	      "file": "foo-B.xml",
	      "endpoint": "xml",
	      "parameters": {
	      	"my-param": "B"
	      }
	    }
	}

This will compare the output of ``/publishers/foo/xml?my-param=A`` with the contents of ``foo-A.xml`` and ``/publishers/foo/xml?my-param=B`` with the contents of ``foo-B.xml``.

Internal properties
===================

All internal properties except ``_id`` and ``_deleted`` are removed from the output. Entities that has ``_deleted`` set to ``false`` will also be removed.

Endpoints
=========

By default the entities are fetched from ``/pipes/<my-pipe>/entities``, but if endpoint is set it will be fetched from
``/publishers/<my-pipe>/<endpoint-type>`` based on the endpoint type specified. Note that the pipe needs to be configured to publish to this endpoint.
 
Example:

::

    {
      "_id": "foo",
      "type": "test",
      "endpoint": "xml",
      "file": "foo.xml"
    }

This will compare the output of ``/publishers/foo/xml`` with the contents of ``foo.xml``.

Example:

::

    {
      "_id": "foo",
      "type": "test",
      "endpoint": "json",
      "stage": "source"
    }

This will compare the output of ``/pipes/foo/entities?stage=source`` with the contents of ``foo.json``, useful when the pipe's sink strips away the "_id" property for example.

Running tests locally
=====================

To test your Sesam configuration locally, run the following commmand:
::

    sesam -vv test

If you haven't configured up the tests correctly or there are endpoint pipes that doesn't have any corresponding test file, you will be notified. If so, fix the missing tests and then run the commmand again. If the tests runs ok, you will get a message that all the tests has passed. If any test failed, you will be notified which test / pipe that failed and get a comparision of the expected result and the received result.

.. _setup-ci:

Set up automatic CI testing
---------------------------

Automatic tests are needed to verify that your pull request does not break any existing pipes/flows inside sesam.
To perform these types of tests we need to set up automatic tests. Since there are a few different CI/CD tools, we are going to explain a few of the most common ones.

In order to fully be able to have an automated CI test of your Sesam configuration, you need to have a designated CI node. The only purpose of the CI node is to provide an environment to test changes to the configuration so that it doesn't break. 

When setting up automatic CI testing for a Sesam project, the following check should be required for the test to pass:

- Running, validating and passing a test of the configuration against the CI node.

Another check that should be considered is:

- Only pull requests (PR) that are approved by another person in the team should be valid (this is however, )
  
CI node
=======

In order to be able to test your Sesam configuration across the project team, you need to have a CI node. This node's sole purpose is to provide a Sesam environment to test changes to the configuration against. Tests will be run in the same way as you will test your configuration locally, except that it should be initiated from your automatic CI testing system instead.

It is important that when running testing against the CI node, only one test should run at the same time. When running a test against a CI node with the Sesam client, the configuration will be overwritten, which will cause a running test to fail or not to finish. Setting up your automatic CI testing, you need to have this in mind.

The CI node should be unable to write any data to another system, bear this in mind when configuring up the node. As the least safety regarding this, the node should not contain any variables or secrets necessary to connect to a system that the Sesam configuration usually will send data to.

Usually, the CI node could be a smaller instance than the production node, as the data used in the tests should not be of a considerable size.

Jenkins
=======

This section describes how to set up Jenkins build with GCloud.

Jenkins is a CI/CD tool that does not support single build pipeline. The reason for the need of single build pipeline is that we upload the node config to a single node, if there are mulitple builds running at the same time there will be pushed multiple configs to the one node, which will result into tests not completing.

To set up builds in jenkins, you will need to add a few file to your repository
my-project-directory
::

  my-project-directory
    ├ deployment
    | ├ jenkins
    | | └ jobs
    | |   └ build
    | |     ├ dm-pod.yaml
    | |     └ Jenkinsfile
    | └ sesam
    |   ├ cloudbuild.yaml
    |   ├ Dockerfile
    |   └ Readme.md
    ├ node
    | └ ++
    └ ++

dm-pod.yaml:

Describes what type of container that should be used in the build process.
::

    apiVersion: v1
    kind: Pod
    spec:

      containers:
      - name: sesam-ci-container
        image: eu.gcr.io/<your_gcr_repo>/sesam:<version_of_sesam_client>
        tty: true
        command:
        - cat
        resources:
          limits:
            memory: 6Gi
            cpu: 1.7

Jenkinsfile:

The Jenkinsfile contains the stages that are supposed to run when the tests are running. The three default stages are:

- Set environment variables for container

- Verify usage of correct Sesam client version.

- Running the tests and printing scheduler logs to see error messages in output.

::

  #!groovy

  pipeline {
      options {
          disableConcurrentBuilds()
      }
      agent {
          kubernetes {
              label "dm-${BRANCH_NAME}-${BUILD_ID}"
              defaultContainer 'jnlp'
              yamlFile 'deployment/jenkins/jobs/build/dm-pod.yaml'
          }
      }
      environment {
          Sesam_CI_node_jwt = credentials('Sesam_CI_node_jwt')
      }
      stages {
          stage('Set Sesam env vars') {
              steps {
                  script {
                      env.Sesam_CI_node = "datahub-****.sesam.cloud"
                  }
              }
          }
          stage("Verify Sesam version") {
              steps {
                  dir('') {
                      container('sesam-ci-container') {
                          sh "/./sesam -version"
                      }
                  }
              }
          }
          stage("Run Sesam tests") {
              steps {
                  dir('') {
                      container('sesam-ci-container') {
                          sh "export NODE='${env.Sesam_CI_node}'; export JWT='$Sesam_CI_node_jwt'; cd node && /./sesam -vv test  -print-scheduler-log"
                      }
                  }
              }
          }
      }
  }


The files under the sesam folder here describes the files that should exist in the repository where jenkins is configured. Usually you do not have access to this repository, but you will need to provide these files.

cloudbuild.yaml:

cloudbuild.yaml A build config file defines the fields that are needed for Cloud Build to perform your tasks. You'll need a build config file if you're starting builds using the gcloud command-line tool or build triggers. You can write the build config file using the YAML or the JSON syntax.

::

  steps:
    - name: 'gcr.io/cloud-builders/docker'
      args: [
        'build',
        '-t', 'eu.gcr.io/<your_gcr_repo>/sesam:latest',
        '-t', 'eu.gcr.io/<your_gcr_repo>/sesam:1.16.1',
        '.'
      ]
  images:
    - 'eu.gcr.io/<your_gcr_repo>/sesam'
  tags:
    - '1.16.1'
    - 'latest'

Dockerfile:

The dockerfile describes the contianer that should run when the build process is executed. This container should be deployed to the repository that is used

::

  FROM debian:9.9-slim
  MAINTAINER [Your name] "your.email.address@domain.no"

  ARG SESAM_CI_VERSION=1.16.1

  SHELL ["/bin/bash", "-c"]

  RUN apt-get update
  RUN apt-get install -y wget

  RUN set -x
  RUN wget -O sesam.tar.gz https://github.com/sesam-community/sesam-py/releases/download/$SESAM_CI_VERSION/sesam-linux-$SESAM_CI_VERSION.tar.gz
  RUN tar -xf sesam.tar.gz
  RUN rm sesam.tar.gz

This dockerfile builds a container with the sesam client that is needed to execute the build. Replace [Your name] with the name of the person responsible for the build process, alongside his or hers email-address.

Azure DevOps
============

Azure DevOps is a bit easier to set up with single build pipeline. You will need to add the following config to your Azure DevOps setup under Pipelines

::

  # Sesam AzureDevops Pipeline

  trigger: none

  pool:
    vmImage: 'ubuntu-latest'

  steps:
  - script: |
      wget -O sesam.tar.gz https://github.com/sesam-community/sesam-py/releases/download/$(sesam_cli_version)/sesam-linux-$(sesam_cli_version).tar.gz
      tar -xf sesam.tar.gz
      rm sesam.tar.gz
    displayName: 'Download Sesam CLI'

  - script: ./sesam -version
    displayName: 'Verify Sesam CLI version'

  - script: |
      export NODE='$(node)'
      export JWT='$(node_jwt)'
      cd node
      .././sesam -vv test  -print-scheduler-log
    displayName: 'Run Tests'

You will also have to add variables

::

  sesam_cli_version = 1.16.1 (version of the CLI used in your project)
  node              = datahub-***.sesam.cloud (the node url to the CI server used in your project)
  node_jwt          = bearer ****** (jwt for the CI server used in your project)


Branch permissions are also needed to not be able to merge a Pull Request unless the tests have completed successfully. These permissions needs to be set under

``Repos->Branches->More->Branch Policies->Add Build Policy``

Use the default settings.

You will also need to turn on ``Require a minimum number of reviewers``, and set it to ``1`` and ``Check for linked work items``. This makes it Easier to trace and close the tasks/issues for the Pull Request.

These settings are required for your main branches ``develop`` and ``master``.

Since the ``trigger`` parameter is set to ``none``, the build process will only trigger on PR's. There is no need to build ``master`` and ``develop`` after merge.

Note if there is support for parallel builds on the agent pool you will need to disable this so that only one build process runs and the second build is queued up. This can be done by adding capability on the build agent. You will also need to add a this in the yaml file to enable this.
Add user capabilities in the agent pool (key value pair), key = Limit and value = DisAbleParallel

Your yaml file:
::

  pool:
    name: {agent pool name}
    demands: Limit -equals DisAbleParallel

Your configuration will end up being in your repository under the main directory:
::

  my-project-directory
    ├ node
    | ├ pipes
    | ├ systems
    | ├ expected
    | └ ++
    └ azure-pipelines.yml


.. _setup-deployment:

Set up automatic deployment
---------------------------

Whether setting up automatic deployment of a Sesam configuration is a disputed theme. In normal usecases, you would like to have more control of when a release is deployed to a production environment, especially in larger or business critical installations. But if you decide upon setting up automatic deployment of your Sesam configuration, it can be done in several ways.

GitHub Autodeployer microservice
================================

One way to easy set up automatic deployment of your Sesam configuration is to use the GitHub Autodeployer microservice. This is a microservice that you can configure in your Sesam node that at given intervals will check the configured Git repository for changes. If any changes to the repo is found, it will read the configuration from the repo and deploy it to the node.

In the configuration you can either specify a branch or a tag. Use tags when deploying a release branch with a version number (which should be a tag in the repo). If no tag is specified, the autodeployer will use the branch variable, which defaults to "master" if not set. Depending on the specified branch or tag, the autodeployer will compare the current Sesam configuration against the configuration in the repository, if any changes are found, the deployer will read the updated configuration from the repository and deploy it to the node.

WARNING! Any existing pipes and systems will be overwritten when the autodeployer deploys a new version to the node. Any pipe or system configuration in the node not existing in the branch will be removed.

Also note that the autodeployer only deploys a configuration, it does not do any other actions on the node, such as starting or resetting pipes. If any pipes need to be reset as part of the deployment for instance, the autodeployer will not perform any such task and this must be done manually.

Information on how to configure the GitHub Autodeployer microservice can be found at its corresponding GitHub page: `https://github.com/sesam-community/github-autodeployer <https://github.com/sesam-community/github-autodeployer>`_.

Using Jenkins, Azure DevOps or any other CD tools
=================================================

Automatic deployment could also be done using the same tools you use for your automatic CI testing, like Jenkins or Azure DevOps. For this, you need to change the step for testing with a step for deploying the given branch. See the document about the :ref:`Sesam client <concepts-sesam-client>` for the correct parameters to use.

Remember to add parameters to your configuration for which release version to deploy.