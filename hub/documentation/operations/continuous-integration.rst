.. _setup-ci:

---------------------------
Continuous integration (CI)
---------------------------

When adding new pipes to your existing Sesam configuration, it is important to verify that these doesn't break any existing pipes, flows or integrations in your Sesam node. To do this you should add automatic tests to your project. In order to fully be able to have automated CI testing it is required to have a designated CI node. 

When setting up automatic CI testing for a Sesam project, the following check should be required for the test to pass:

- Running, validating and passing a test of the configuration against the CI node.

In addition you should consider adding a check that requires that pull requests (PR) needs to be approved by another member of the team in order for the PR to be merged.

CI node
-------

In order to be able to test your Sesam configuration across the project team, you need to have a CI node. The sole purpose of this node is to provide a Sesam environment to test changes to the configuration against. Tests will be run in the same way as you will test your configuration locally, except that it should be initiated from your automatic CI testing system instead.

It is important that when running testing against the CI node, only one test should run at the same time. When running a test against a CI node with the Sesam client, the configuration will be overwritten, which will cause a running test to fail or not to finish. Setting up your automatic CI testing, you need to have this in mind.

The CI node should be unable to write any data to another system, bear this in mind when configuring up the node. As the least safety regarding this, the node should not contain any variables or secrets necessary to connect to a system that the Sesam configuration usually will send data to.

Usually, the CI node should be a smaller instance than the production node, as the data used in the tests should not be of a considerable size.


Using Jenkins or Azure DevOps for automatic CI testing
------------------------------------------------------

Jenkins
=======

This section describes how to set up Jenkins build with Google Cloud.

Jenkins is a CI/CD tool that does not immediately support a single build pipeline. The reason for the need of a single build pipeline is that we upload the node config to a single node, if there are mulitple builds running at the same time, multiple configs will be pushed to one node, which will result in tests not completing. You should therefore consider the following, if choosing to use Jenkins as your CI/CD tool.

To set up builds in jenkins, you will need to add a few files to your repository
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

cloudbuild.yaml A build config file defines the fields that are needed for Cloud Build to perform your tasks. You'll need a build config file if you are starting builds using the gcloud command-line tool or build triggers. You can write the build config file using the YAML or the JSON syntax.

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

The dockerfile describes the container that should run when the build process is executed. This container should be deployed to the repository that is used, i.e:

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

This dockerfile builds a container with the sesam client that is needed to execute the build. Replace [Your name] with the name of the person responsible for the build process, alongside with his or hers email-address.

Azure DevOps
============

Azure DevOps is a bit easier to set up with a single build pipeline. You will need to add the following config to your Azure DevOps setup under Pipelines

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

You will also need to turn on ``Require a minimum number of reviewers``, and set it to ``1`` and ``Check for linked work items``. This makes it easier to trace and close the tasks/issues for the Pull Request.

These settings are required for your main branches ``develop`` and ``master``.

Since the ``trigger`` parameter is set to ``none``, the build process will only trigger on Pull Requests. There is no need to build ``master`` and ``develop`` after merge.

Note if there is support for parallel builds on the agent pool you will need to disable this so that only one build process runs and the second build is queued up. This can be done by adding capability on the build agent. You will also need to add this in the .yaml file to enable it.
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

