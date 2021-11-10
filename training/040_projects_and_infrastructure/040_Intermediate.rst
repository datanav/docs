
.. _projects-infrastructure-intermediate-4-3:

Intermediate
------------

.. _dev-ci-test-prod-nodes-4-3:

Multiple Sesam node environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

dev = personlig node der utvikling foregår

test = node som kjører samme config som prod med testdata for å finne
bugs

CI = do tests for pull requests /deployments before deploying.

prod = live node som kjører live integrasjoner

Tagging av brancher for deployment

.. seealso::

  TODO

.. _ci-cd-4-3:

Continoues Integration and Deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ci-node

kjører med test-data

embedded data

NB!! nye cli fra 1.18.1(separat testdata-fodler)

NB!! ikke koblet til live systemer, ikke legg inn secrets som ikke skal
være der

node-env

conditional source

embedded data

NB!! nye cli fra 1.18.1(separat testdata-folder)

conditional transform

Hvordan bruker vi versjonskontroll(git, vcs, svn)

initiere repo (se docs)

protected branches

merge regler

byggserver

Autodeploy/vs ikke

.. seealso::

  TODO

.. _workflow-in-projects-4-3:

Workflow in Projects
~~~~~~~~~~~~~~~~~~~~

Get task

[Document task]

Pull repo

Create branch

Do changes

Test changes

[Create more test cases]

Update expected data

Push changes

Document solution

Deploy to test

Test changes in test – go back to create branch if necessary.

Deploy to prod

.. seealso::

  TODO

.. _tasks-for-projects-and-infrastructure-intermediate-4-3:

Tasks for Projects & Infrastructure: Intermediate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
