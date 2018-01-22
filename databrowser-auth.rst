This document is intended for administrators that has access to the "databrowser.ini"
configuration file.

Authentication and authorization via data
=========================================

Authentication is the process of figuring out who the user is.

Authorization is the process of figuring out what an authenticated user
is allowed to do.
The user's permissions are specified by the documents in the solr database
(see the `Authorization <#authorization>`__ section for details).



Authentication
--------------

The USE\_X\_REMOTE\_USER\_HEADER\_AUTHENTICATION config-variable is set
with the "use\_x\_remote\_user\_header" variable in the "[main]"-section
of the "databrowser.ini" file.

This is a boolean value, with the following meaning:

| False:
| User authentication is done via velruse. This works by redirecting the
  user's webbrowser to some external webpage that does the authentication
  and redirects back to the databrowser.


| True:
| Authentication is done by assuming that a valid username is present in
  the "X-Remote-User"-header in the http-request, NOTE: Only enable this
  if the databrowser webapp is safely hidden behind something (for
  instance httpd or nginx) that handles authentication and sets the
  header accordingly.

The databrowser will attempt to map the specified username to an
email-address like this:

1. Do a solr-search to find all items that has the username in any of
   the fields specified in the X\_REMOTE\_USER\_USERNAME\_FIELDS
   config-variable (which is set by the
   "x\_remote\_user\_username\_psi"-value in the
   "authentication"-section in the "databrowser.ini"-file).

2. Look for fields in the found items using the fieldnames specified in
   the X\_REMOTE\_USER\_EMAIL\_FIELDS config-variable (which is set by
   the "x\_remote\_user\_email\_psi"-value in the
   "authentication"-section in the "databrowser.ini"-file).

If any email-addresses are found, one of them will be stored in the
"email"-attribute of the session-object.

If no email-addresses are found, and the username looks like an
email-address, the username will be stored in the "email"-attribute of
the session-object.

.. _databrowser_authorization_via_solr:

Authorization
-------------

Once authentication has been done, the session object contains an
"email"-attribute with the authenticated user's email address. This is
then used to do a search to figure out which items the user should be
allowed to see.

This is done like this:

1. Do a solr-search for items that has the user's email address in any
   of the fields specified in the EMAIL\_FIELDS config-variable (which
   is set by the "email"-value in the "[search fields]"-section in the
   "databrowser.ini"-file)
2. Make a list of the ids of the found items and of the ids the items
   refers to via "psi\*"-fields.

This list of ids is stored in the "psis"-attribute in the session
object.

.. _databrowser_ini_AUTHORIZATION_MODEL:

AUTHORIZATION\_MODEL config-variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AUTHORIZATION\_MODEL config-variable is set with the "authorization
model" variable in the "`authentication <#authentication>`__"-section of
the "databrowser.ini" file. It specifies how authorization is done.

The config-variable can have these values:

| OPEN:
| No authorization is done: all items that does not have a
  :ref:`config.AUTH\_FIELDS <databrowser_ini_AUTH_FIELDS>` field are available for
  all users.

| AUTHENTICATED:
| All authenticated users have access to all items that do not have a
  :ref:`config.AUTH\_FIELDS <databrowser_ini_AUTH_FIELDS>` field. Anonymous users
  haven't got access to any items.

| AUTHORIZED:
| Authenticated users have only access to items that have a
  :ref:`config.AUTH\_FIELDS <databrowser_ini_AUTH_FIELDS>` or
  config.ID\_FIELDS field that contains one
  of the values in the "psis"-value in the session object.

.. _databrowser_ini_AUTH_FIELDS:

AUTH\_FIELDS config-variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AUTH\_FIELDS config-variable is set with the "auth" variable in the
"[search fields]"-section of the "databrowser.ini" file.

Its meaning depends on the value of the AUTHORIZATION\_MODEL
config-variable:

-  | AUTHORIZATION\_MODEL="OPEN" or
     AUTHORIZATION\_MODEL="AUTHENTICATED":
   | AUTH\_FIELDS is optional. If it is set, only items that does *not*
     have any of the fields specified by the AUTH\_FIELDS variable will
     be returned in a search.

-  | AUTHORIZATION\_MODEL="AUTHORIZED"
   | AUTH\_FIELDS *must* be set.
   | Only items that *does* contain all the fields specified in
     AUTH\_FIELDS will be included in the searchresults.
   | Items with a AUTH\_FIELDS-field that contains one of
     the ids stored in the "psis"-value in the session object will be
     added to the searchresults.
   | Items with a ID\_FIELDS-field that contains one of the
     ids stored in the "psis"-value in the session object will be added
     to the searchresults.


.. _databrowser_ini_authorization_via_jwt_token:

Authentication and authorization via a JWT token
------------------------------------------------

In addition to authenticating against Google or Microsoft Live and authorizing
based on the :ref:`data in solr <databrowser_authorization_via_solr>`, the databrowser supports authentication
and authorization with a `JWT <https://en.wikipedia.org/wiki/JSON_Web_Token>`_  authorization
token created by the `Sesam portal <https://portal.sesam.io>`_.

This is used we want to be able to allow users to use their Sesam portal login credentials
to log into the databrowser. This functionality is normally only used when the databrowser has
been provisioned via the Sesam portal, and in this case the required configuration will have
been done automatically.

JWT authentication
~~~~~~~~~~~~~~~~~~
JWT authentication is enabled by setting the "jwt_authentication_subscription_ids" configuration
variable in the "authentication" section of the "databrowser.ini" file. The value should be
one or more subscription-ids. Example::

    [authentication]
    jwt_authentication_subscription_ids =
        789f4d46-91fe-418a-8652-0e7582f00d18

A value of "*" means that JWTs from all subscriptions will be accepted by the databrowser.

JWT authorization
~~~~~~~~~~~~~~~~~
Once the user has been authenticated with a JWT, authorization is done by looking at the documents in the solr database (see the :ref:`Authorization <databrowser_authorization_via_solr>` section for details).

In addition, if the JWT grants the user the "group:Admin" role, the user will be allowed to see all the solr documents and to edit the databrowser configuration.

Logging in with a JWT
~~~~~~~~~~~~~~~~~~~~~
Logging in via a JWT is usually done behind the scenes by the Sesam portal GUI. An end-user will normally not need to know the details.

The login is done via the databrower url "/jwt_login".

A "GET"-request will display a simple html form where the user can paste in a JWT string and click a "Login" button.

A "POST"-request will parse the specified JWT string, store the user's credentials in the (server-side) http session and redirect to the databrowser frontpage.

