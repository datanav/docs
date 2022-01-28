.. _setup-deployment:

--------------------
Automatic deployment
--------------------

Whether setting up automatic deployment of a Sesam configuration is a disputed theme. In normal usecases, you would like to have more control of when a release is deployed to a production environment, especially in larger or business critical installations. But if you decide upon setting up automatic deployment of your Sesam configuration, it can be done in several ways.

GitHub Autodeployer microservice
--------------------------------

One way to easily set up automatic deployment of your Sesam configuration is to use the GitHub Autodeployer microservice. This is a microservice that you can configure in your Sesam node that at given intervals will check the configured Git repository for changes. If any changes to the repo is found, it will read the configuration from the repo and deploy it to the node.

In the configuration you can either specify a branch or a tag. Use tags when deploying a release branch with a version number (which should be a tag in the repo). If no tag is specified, the autodeployer will use the branch variable, which defaults to "master" if not set. Depending on the specified branch or tag, the autodeployer will compare the current Sesam configuration against the configuration in the repository, if any changes are found, the deployer will read the updated configuration from the repository and deploy it to the node.

WARNING! Any existing pipes and systems will be overwritten when the autodeployer deploys a new version to the node. Any pipe or system configuration in the node not existing in the branch will be removed.

Also note that the autodeployer only deploys a configuration, it does not do any other actions on the node, such as starting or resetting pipes. If any pipes need to be reset as part of the deployment for instance, the autodeployer will not perform any such task and this must be done manually.

Information on how to configure the GitHub Autodeployer microservice can be found at its corresponding GitHub page: `https://github.com/sesam-community/github-autodeployer <https://github.com/sesam-community/github-autodeployer>`_.

Using Jenkins, Azure DevOps or any other CD tools
-------------------------------------------------

Automatic deployment could also be done using the same tools you use for your automatic CI testing, like Jenkins or Azure DevOps. For this, you need to change the step for testing with a step for deploying the given branch. See the document about the :ref:`Sesam client <concepts-sesam-client>` for the correct parameters to use.

Remember to add parameters to your configuration for which release version to deploy.
