.. _reauthorise:

================
Re-authorisation
================


Introduction
------------

In Sesam Talk, we support systems with different authorisation mechanisms. Here we will explain how they work and how some of them might require the user to re-authorise with those systems.

Api keys
--------

Systems that uses api keys often have a mechanism to have the keys expire or that the user can revoke the key in the system. If this happens, we will no longer be able to synchronise with the system. The user will be required to provide us with a new valid api key.

Oauth2 flows
------------

Systems that uses Oauth2 flows often have a way to "uninstall" an application as their way to revoke access for an external application. If this happens, we will no longer be able to synchronise with the system. The user will then be required to re-install the application by following the same authorisation procedure that they did initially.
