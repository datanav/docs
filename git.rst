----------------------------
Using Git in a Sesam project
----------------------------

Initial repository setup
------------------------

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

.. _git-master-branch:

Set up master branch
====================

Based on the structure described above you should navigate to the project root (my-project-directory) and run the following command::

    git init

Then your directory will become a Git repository (repo). After you've done this, go to your source control website (i.e. github.com). Here you will need to create a new repo under your organisation. Make sure that you don't initialize the repo from the website. When the repo has been created you should be presented with a url to use. (i.e. git@github.com:my_org/my_repo.git)
Connect the Git repo to your local repo::

    git remote add origin git@github.com:my_org/my_repo.git

Push your local repo to Git::

    git push -u origin master

    (Tip: Sometimes you need to first add and commit README.md file, to make your first push to remote repo.)

.. _git-development-branch:

Set up development branch
=========================

Since we want to use the master branch as the production branch, we need to setup a new branch called *develop* to use for development.
To do this we need to type the following in terminal::

    git checkout -b develop

This creates a new branch called develop that mirrors master. To push it to Git::

    git push --set-upstream origin develop

Now you should have two branches in Git. Before we go forward you should go to your repository settings (in Github or equal) and configure the default branch to be develop. After that you should set both *master* and *develop* branches as protected. This means that you won't be able to directly push commits to these branches. We want to force users to do that by creating pull requests.

More information about pull requests can be read in this :ref:`document<pull-request>`
https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request.

.. _git-feature-branch:

Set up feature branches
=======================

Creation:
::

    $ git checkout -b myfeature develop
    Switched to a new branch "myfeature"

Incorporating a finished feature on develop :
::

    $ git checkout develop
    Switched to branch 'develop'
    $ git merge --no-ff myfeature
    Updating ea1b82a..05e9557
    (Summary of changes)
    $ git branch -d myfeature
    Deleted branch myfeature (was 05e9557).
    $ git push origin develop

Tip: The --no-ff flag causes the merge to always create a new commit object, even if the merge could be performed with a fast-forward. This avoids losing information about the historical existence of a feature branch and groups together all commits that together added the feature.

.. _git-release-branch:

Set up release branches
=======================

Creation :
::

    $ git checkout -b release-1.0.0 master
    Switched to a new branch "release-1.1.0"
    $ ./bump-version.sh 1.1.0
    Files modified successfully, version bumped to 1.1.0

(Here, bump-version.sh is a fictional shell script that changes some files in the working copy to reflect the new version.
(This can of course be a manual change—the point being that some files change.) Then, the bumped version number is committed.))
::

    $ git commit -a -m "Bumped version number to 1.1.0"
    [release-1.2 74d9424] Bumped version number to 1.1.0
    1 files changed, 1 insertions(+), 1 deletions(-)

Finishing a release branch:
::

    $ git checkout master
    Switched to branch 'master'
    $ git merge --no-ff release-1.1.0
    Merge made by recursive.
    (Summary of changes)
    $ git tag -a 1.2

The release is now done, and tagged for future reference. To keep the changes made in the release branch, we need to merge those back into develop, though:
::

    $ git checkout develop
    Switched to branch 'develop'
    $ git merge --no-ff release-1.1.0
    Merge made by recursive.
    (Summary of changes)

This step may well lead to a merge conflict (probably even, since we have changed the version number). If so, fix it and commit.
Now we are really done and the release branch may be removed, since we don’t need it anymore:
::

    $ git branch -d release-1.1.0
    Deleted branch release-1.1.0 (was ff452fe).

.. _git-hotfix-branch:

Set up hotfix branches
======================

Creation:
::

      $ git checkout -b hotfix-1.1.1 master
      Switched to a new branch "hotfix-1.1.1"
      $ ./bump-version.sh 1.1.1
      Files modified successfully, version bumped to 1.1.1.
      $ git commit -a -m "Bumped version number to 1.1.1"
      [hotfix-1.1.1 41e61bb] Bumped version number to 1.1.1
      1 files changed, 1 insertions(+), 1 deletions(-)

Finishing a hotfix branch:
::

    $ git checkout master
    Switched to branch 'master'
    $ git merge --no-ff hotfix-1.1.1
    Merge made by recursive.
    (Summary of changes)
    $ git tag -a 1.1.1

Next, include the bugfix in develop too:
::

    $ git checkout develop
    Switched to branch 'develop'
    $ git merge --no-ff hotfix-1.1.1
    Merge made by recursive.
    (Summary of changes)

Important: The one exception to the rule here is that, when a release branch currently exists, the changes in the hotfix needs to be merged into that release branch, instead of develop.
::

    $ git branch -d hotfix-1.1.1
    Deleted branch hotfix-1.1.1 (was abbe5d6).

Working on a new feature/change
-------------------------------

Branching
=========

When you want to start working on a new feature, you should start by creating a new feature branch. When checking out the new branch, make sure that you have the latest version of the source branch. Generally new feature branches should be checkout out from the develop branch. Generally we want feature branches to be named after the relevant task/issue id. You can read more about how to name the branches correctly in :ref:`Branch naming <branch-naming>`.
::

    git checkout master
    git pull
    git checkout -b <issue_id>

Now you have a feature branch to start working on. Next you should proceed to read about how to write commit messages.

Commit messages
===============

* Start the commit message with a task/issue id
* Use the imperative mood in the subject line, as described `here <https://chris.beams.io/posts/git-commit/#imperative>`_.

There are some simple rules to follow. A properly formed Git commit subject line should always be able to complete the following sentence:

If applied, this commit will <your subject line here>

For example, a commit message like "update the rdf:type in proarc-document pipe" will result in:

::

    If applied, this commit will update the rdf:type in proarc-document pipe

Try to avoid having commit messages like: "Fixed bug with Y".
This is a non-imperative form and when we apply the imperative mood to the text "Fixed bug with Y" the sentence will result into:

::

    If applied, this commit will Fixed bug with Y.

An example of a commit message with a task/issue id:

::

    AB-123: Update requirements to fix deprecation error

In this example AB-123 is the issue id. When this pattern is utilized, it makes it much easier to determine why a commit where applied regardless of branch.

.. _pull-request:

Pull request
============

At this point you should have a feature branch with some changes that you would like to merge into your develop branch. If you've been working on your feature branch for a while, it might be a good idea to merge the develop branch back into your feature branch before creating the pull request.
::

    git fetch develop
    git merge develop

When doing this, you might encounter conflicts. To resolve these, go to the mentioned files and look to see what version of the code is the one that should be kept. Edit out the code that shouldn't be kept and add the files:
::

    git add <my_file_with_conflict>
    git merge --continue

When this is done, you should push your latest changes to github or similar and create a pull request with their GUI.

Deploy a new feature
--------------------

Creating a release
==================

Release branches contain production ready new features and bug fixes that come from a stable develop branch. In most cases, the master branch is always behind the develop branch as new features will first be pushed to that branch. After finishing release branches, they get merged back into develop and master branches so that both of these branches eventually will match each other.

We can split a release into two different categories, minor releases and major releases. These two different release types are defined by how big the change to master is.

Usually you would have feature releases as minor releases, while major releases would include big changes like restructuring pipe-combinations and merge rules.

Hotfixes
========

Hotfixes are used to deploy critical changes to production. It also includes small fixes to pipes (as long as it is something that already is deployed to production\*). When creating a hotfix you should branch off from master branch, merge into master and back to develop so that both of the main branches gets the update.

\*Small fixes will often be forgotten and end up in the develop branch without being added to a release. This validates having small fixes/changes to pipes/systems as a hotfix and not only beeing added as a part of a release.

Tagging
=======

Tags are a simple aspect of Git, they allow you to identify specific release versions of your code. You can think of a tag as a branch that doesn't change. Once it is created, it loses the ability to change the history of commits.

In a Sesam perspective we add tags if we need to revert to a previous version, if we figure out that a release or hotfix is not working as expected.

Tags are also a good way to have different versions of config in different environments. A good example of this is if multiple releases are done, but one version has not been tested to the full extent. You can run one tag in the staging environment, and another in the production environment.

For tags we use semantic versioning. You can read more about semantic versioning here `semantic versioning <https://semver.org>`_.

Variables
=========

Variable files are often added to Git so that we are able to track and keep control of existing environment variables. Environment variables should exist in the repository under the folder node\variables. You should have 3 files:

-variables-dev.json

-variables-staging.json

-variables-prod.json

These three files should reflect what the variables are in your/the projects node environment. Changes/addition of environment variables should be added to Git with the feature you are editing or in the hotfix you are creating.

When creating a release you must remember to add the updated files to your release branch.

Secrets
=======

Secrets should ideally be saved in a keymanager, and not in Git.

When you want to deploy all changes in develop into master
==========================================================

First off we will need to create a ticket for your release so we get a task number. This is done in your projects issuetracker. In this case the ticket created is named AB-2324.

When you are ready to deploy your changes to production, you will have to create a release to master.

This is done with:
::

    git checkout master
    git checkoub -b release-*.*.*
    (creating release branch that is semantically versioned)
    git checkout develop -- .
    (checkout all files from the develop branch and add it to your current release-*.*.*. )

this will add all the expected files that you have in your expected folder as well.

you should now run tests to see if everything works as expected.
::

    sesam -vv test

If the result of the test comes back as OK, you are ready to commit.
::

    git add .
    (adds all files)
    git commit -m "AB-2324: add all files from develop to release-*.*.*"
    (When using task number AB-2324 you will create a reference to the ticket and in some issuetrackers you will be able to see a link to the Pull request)
    git push

You are now ready to create the pull request in your version control system. This will trigger your build process to trigger a new build. When your build has completed successfully, you are ready to merge your release branch into master.

When the merge is completed you can now tag your release in your version control system to release-*.*.*

When you can't deploy everything in develop into master
=======================================================

When you can't deploy everything from develop into production, and you would like to release some feature that is completed. you will need to find the config files manually. You will need to figure out what pipes/systems that are ready for deploy, but you would still need to go through the same process as noted in the "When you want to deploy all changes in develop into master" stage.
::

    git checkout master
    git checkout -b release-*.*.*
    (creating a branch based on master branch)

You will now have to have a list of the pipes/systems you would like to deploy.

Considering you are in the node folder:
::

    git checkout develop pipes/<my_pipe_name> systems/<my_system_name>

this will only checkout the pipes/systems that you would like to be included in this release. Note that your tests will fail now, since you have not checked out the corresponding tests to the pipe you just checked out.::

    git checkout develop expected/<my_pipe_name>.*
    *(this will check out the two expected files that are in relation to the pipe you have checked out)*
    sesam -vv test
    (run the test to see if testresults are ok)

Remember to checkout the environment config files as well.

If everything is ok, you can now add and commit the files to your new release-branch.
::

    git add .
    git commit -m "AB-2324: adding specific files from dev to my new release-*.*.*"
    git push

You are now ready to create the pull request in your version control system. This will trigger your build process to trigger a new build. When your build has completed successfully, you are ready to merge your release branch into master.

When the merge is completed you can now tag your release in your version control system to release-*.*.*. You are now ready to merge back to develop.

Often you might end up having merge conflicts when you merge back to develop. You can read more about this in :ref:`Resolve common problems <resolve-common-problems>`.

Branch naming/release tagging
-----------------------------

.. _branch-naming:

Branch naming
=============

When we're creating a new feature branch, we want the branch to be named after the relevant issue/task id. Lets say we have a ticket called AB-123. Then you would create your branch like this:
::

    git checkout develop -b AB-123

Release naming
==============

When you want to create a new release to deploy, we want releases to use semantic version numbers. This makes it easier to determine what type of change a release involves.

To determine the next version number, you can follow this diagram:

.. image:: images/se-ver.png
  :width: 600

.. image:: images/se-ver2.png
  :width: 600

.. _resolve-common-problems:

Resolve common problems
-----------------------

Merging back to develop creates merge conflicts
===============================================

When you have worked on a release, there will be cases when your develop and master branch diverges. Lets say you have not created a release in a long time. You will end up having a lot of new features in your develop branch that does not exist in master.

Even though new pipes and systems will not have a merge conflict, you will have cases where your global pipes have many new features in dev that does not exist in master. You will need to fix the release so that you only add the features you want to release. An example of this follows:

your-global-pipe-in-dev:
::

    "datasets": ["dataset_foo", "dataset_bar", "dataset_baz", "dataset_foobar", "dataset_foobaz"]

While your global-pipe in master looks like:
::

    "datasets": ["dataset_foo", "dataset_bar", "dataset_foobar"]

Your feature with ``"dataset_baz"`` is now finished and you will only want to release this, and not all the others that are not finished. You will have to do changes as a commit in the release branch to get the correct structure in your master branch.

And your global pipe should look like this:
::

    "datasets": ["dataset_foo", "dataset_bar", "dataset_foobar", "dataset_baz"]

You can see that the order in your dev global pipe vs your master global pipe is diverging now. Since our Master branch is the Main branch, and develop is continually under development we will need to restructure develop to match the newest release.

::

    dev (currently):
    "datasets": ["dataset_foo", "dataset_bar", "dataset_baz", "dataset_foobar", "dataset_foobaz"]
    master (after changes to release-branch)
    "datasets": ["dataset_foo", "dataset_bar", "dataset_foobar", "dataset_baz"]

When this type of change is merged back to develop you will get merge conflicts that needs to be resolved. The order that is primary choice is the changes from master. Which results into dev looking like:
::

    dev (after merge back from release branch):
    "datasets": ["dataset_foo", "dataset_bar", "dataset_foobar", "dataset_baz", "dataset_foobaz"]
    master (after changes to release-branch)
    "datasets": ["dataset_foo", "dataset_bar", "dataset_foobar", "dataset_baz"]

You can see that the order is changed in develop to match what is in master.

.. _git-we-found-a-bug-in-recently-merged-pr:

We found a bug in recently merged PR
====================================

The following strategy will revert a merge commit. This can be used in any branch where you want to undo a merge.
::

    git checkout develop -b revert/my_feature_branch

Now you will need to find the commit hash of the merge commit. This can be found with "git log". Then use the hash in the next command::

    git revert -m 1 <hash of merge commit>

Now you have a branch that reverts the merge. Use that for a new pull request against develop.
If you want to fix the feature you can start with following steps after you have merged the previous revert.
::

    git pull develop
    ..
    git checkout develop -b my_feature_branch
    ..
    git revert -m 1 <hash of revert commit from earlier>

Now you have a branch where the reverted changes have been re-applied. Now you can continue working in the feature branch and fix the issues that required the revert in the first place. When your changes are done, you can treat this branch as a regular feature branch and create a new pull request to merge your changes.

We found a critical bug in production
=====================================

When this happens, you most likely have two choices. Either revert the change (see :ref:`We found a bug in recently merged PR <git-we-found-a-bug-in-recently-merged-pr>` or fix it directly in production with a hofix branch.

To fix it directly in production, use the following steps:

1. Create an new hotfix branch from master: ``git checkout master -b hotfix_for_my_feature``.
2. Do your changes and commit it to the hotfix branch.
3. Create a PR for both master (production) and develop (to get the correct version for future development).
