=======================
Sesam Management Studio
=======================

.. contents:: Table of Contents
   :depth: 2
   :local:


Overview
========

As well as the API and Sesam Client, we also provide a web based UI for managing a Sesam service instance. This can be used to do nearly all the things that can be done via the API. It can be found by pointing a browser at:
`https://portal.sesam.io <https://portal.sesam.io>`__.


And the home page looks like this:


.. image:: images/management-studio.png
    :width: 800px
    :align: center
    :alt: Sesam Management Studio

If you are familiar with the Sesam concepts then the UI should be quite intuitive.


User accounts
=============

In order to use the Management Studio you first need to log in with your user credentials. You can either
authenticate via a third party authentication provider (as for example Google or Azure), or create
a user-account directly in the Management Studio.

Your user-account is uniquely identified by the email-address. That means that it is possible to use multiple
authentication providers to log in as the same user, as long as the user credentials from the various authentication
providers contain the same email address.

This comes with a small caveat: If you create a user-account directly in the Management Studio you are not required
to verify that the email address you specify actually exists and that you own it. That basically means that anyone can
claim to own any email-address, including addresses that actually belongs to someone else.

On the other hand: most of the third party authentication providers supplies a verified email address.

To avoid someone else to be able to log in with your email-address, the first login with a verified email-address
will disable any unverified user credentials that has been previously used. All other settings on the existing user
account will be kept, though.
