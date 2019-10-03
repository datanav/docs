.. _git:

========================================
How to deal with different git scenarios
========================================


Set up a new git project for Sesam
----------------------------------

Initial repository setup
========================

Development should be in a develop branch
Master is generally the production environment and should only get changes through releases

These steps are based on that you already have a directory with sesam config you want to put into a repo
Actual steps
The optimal directory structure of Sesam Node project should look like this:
::

    my-project-directory
      ├ node
      | ├ pipes
      | ├ systems
      | └ variables
      ├ README.md
      ├ LICENSE
      ├ .gitignore
      └ ++

Based on this structure you should navigate to the project root (my-project-directory) and run the following command::

    git init

Then your directory will become a git repository (repo). After you've done this, go to your source control website (i.e. github.com). Here you will need to create a new repo under your organisation. Make sure that you don't initialize the repo from the website. When the repo has been created you should be presented with a url to use. (i.e. git@github.com:my_org/my_repo.git)
Connect the your github repo to your local repo::

    git remote add origin git@github.com:my_org/my_repo.git

Push your local repo to github::

    git push -u origin master


Set up branches for development
===============================
Since we want to use the master branch as the production branch, we need to setup a new branch called *￿develop* to use for development.
To do this we need to type the following in terminal::

    git checkout -b develop

This creates a new branch called develop that mirrors master. To push it to github::

    git push --set-upstream origin develop

Now you should have two branches in github. Before we go forward you should go to your repository settings (in Github or equal) and configure the default branch to be develop. After that you should set both *master* and *develop* branches as protected. This means that you won't be able to directly push commits to these branches. We want to force users to do that by creating pull requests.

More information about pull requests can be read BELOW...



Automatic tests
===============

Required checks
 TODO: Explain required checks for a sesam project

Setup

Local git hooks (pre commit checks)

Working on a new feature/change
-------------------------------

Branching
=========

When you want to start working on a new feature, you should start by creating a new feature branch. When checking out the new branch, make sure that you have the latest version of the source branch. Generally new feature branches should be checkout out from the develop branch. Generally we want feature branches to be named after the relevant task/issue id. TODO: LINK
::

    git checkout master
    git pull
    git checkout -b <issue_id>

The feature branch should be named after the corresponding task/issue id.
Now you have a feature branch to start working on. Next you should proceed to read about how to write commit messages.

Commit messages
===============
* Start the commit message with a task/issue id
* Use the imperative mood in the subject line https://chris.beams.io/posts/git-commit/#imperative
    Explain more here

::

    AB-123: Update requirements to fix deprecation error

In this example AB-123 is the issue id. When this pattern is utilized, it makes it much easier to determine why a commit where applied regardless of branch.

Pull request
============

At this point you should a feature branch with some changes that you would like merge into your develop branch. If you've been working on your feature branch for a while, it might be a good idea to rebase the develop branch into your feature branch before creating the pull request.
::

    git fetch develop
    git rebase develop

When doing this, you might encounter conflicts. To resolve these, go to the mentioned files and look to see what version of the code is the one that should be kept. Edit out the code that shouldn't be kept and add the files:
::

    git add <my_file_with_conflict>
    git rebase --continue

When this is done, you should push your latest changes to github or similar and create a pull request with their GUI.



Deploy a new feature
--------------------

When you want to deploy all changes in develop into master
==========================================================
TODO: Talk about creating a release. Tagging. variables, secrets++


When you can't deploy everything in develop into master
=======================================================
::

    git checkout master -b revert/my_feature_branch
    ----



branch from master, checkout files or cherry pick commits in develop you want to get into master
Branch should be called release...

TODO

Branch naming/release tagging
-----------------------------
Branch naming
=============
When we're creating a new feature branch, we want the branch to be named after the relevant issue/task id. Lets say we have a ticket called AB-123. Then you would create your branch like this:
::

    git checkout develop -b AB-123

Release naming
==============
When you want to create a new release to deploy, we want releases to use semantic version numbers. This makes it easier to determine what type of change a release involves.
To determine the next version number, you can follow this diagram:
TODO: insert diagram


Resolve common problems
-----------------------

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

Now you have a branch where the reverted changes have been re-applied. Now you can continue working in the feature branch and fix the issues that required the revert in the first place.
When your changes are done, you can treat this branch as a regular feature branch and create a new pull request to merge your changes.

We found a critical bug in production
=====================================
When this happens, you most likely have two choices. Either revert the change (see :ref:`We found a bug in recently merged PR <git-we-found-a-bug-in-recently-merged-pr>` or fix it directly in production with a hofix branch.
To fix it directly in production, use the following steps:

1. Create an new hotfix branch from master:  ``git checkout master -b hotfix_for_my_feature``
2. Do your changes and commit it to the hotfix branch.
3. Create a PR for both master (production) and develop (to get the correct version for future development)

