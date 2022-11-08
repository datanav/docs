.. _software-channels:

:badge:`Free feature,badge-success badge-pill`

Software channels
=================

Sesam software is released through a phased rollout scheme. There are four different release channels – commonly called canaries. This is done to give changes and new features some time in non-production environments before they are rolled out to production. The goal is to reduce risk.

The available channels are:

- ``weekly-prod`` is released once a week, and it is two weeks behind ``nightly``. It is the most stable release. *Use this in production!*
- ``weekly`` is released once a week, and it is one week behind ``nightly``. Use this in staging environments.
- ``nightly`` is released every night. Use this in development environments.
- ``latest`` is released every time a pull request is merged. Use this only for developent environments, and only when you know what you're doing.

.. Note::
  We can for any reason choose to not promote new versions of any software channel, build dates will correspond to a minimum, not a maximum age.

Weekly and nightly upgrades are performed between 00-03 CET. Weekly upgrades are performed night to Monday.
Security hotfixes will not wait for the scheduled window. Downgrades are not supported.
