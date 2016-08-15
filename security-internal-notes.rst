========
Security
========

.. contents:: Table of Contents
   :depth: 2
   :local:


------------
Introduction
------------

* authentication is handled by a variety of third parties. Auth0, Azure AD, etc.

* roles and permissions are defined in the portal.

* authorisation for actions in a given service instance is configured 'locally' on that service.

* rights checks are performed when using the API, adding or modifying config, and at run time for pipe execution.

See the "Security in SESAM" epic for what the current state of affairs actually is: https://jira.bouvet.no/browse/IS-3098.


-------------------
Definition of terms
-------------------

Auth0 "Profile"
~~~~~~~~~~~~~~~
This represents one top-level user of the "auth0.com" site itself. Only SESAM employees has a auth0 profile.
Each Profile can have access to zero or more auth0 Accounts.

Auth0 "Account"
~~~~~~~~~~~~~~~
We have one Account for each of our enviroments. "sesam", "sesam-dev", "sesam-test".

Auth0 "Client" / Auth0 "Application"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Auth0 "Client" and "Application" are synonymous. In our case the main Application is the "Sesam Portal".
Each auth0 Account can have zero or more Applications.

Auth0 "User"
~~~~~~~~~~~~
The user in auth0 that is created when a person signs up in the Sesam Portal. This user is tied to one auth0
account ("Sesam", "Sesam test", "Sesam ci-test", "Sesam dev").

User data
~~~~~~~~~

We only use auth0 for authentication; all other information about the user is stored by the Sesam Portal in a separate
(i.e. outside of auth0) database.

Organization
~~~~~~~~~~~~
An organization typically represents one customer project. The organization "owns" the sesam subscription(s).


JWT (JSON Web Tokens)
~~~~~~~~~~~~~~~~~~~~~
From https://jwt.io/introduction/ :
"JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained way for securely
transmitting information between parties as a JSON object. This information can be verified and trusted because
it is digitally signed. JWTs can be signed using a secret (with the HMAC algorithm) or a public/private key
pair using RSA."


--------------
Authentication
--------------

We use auth0 for authentication, and for authentication only. All authorization is done by the Sesam Portal
independently of auth0. All authorization information is stored by the Sesam Portal in a separate database.


-------------
Authorization
-------------

All authorization information is stored by the Sesam Portal in an external database. We want to use a
key/value store for this , since those are simple to deal with, and Azure supplies one (https://azure.microsoft.com/en-us/documentation/services/documentdb/).

Each user has an entry in the key/value store (the key is the auth0 "userid" value).

The ids of the organizations the user is a member of are stored under the "organizations" key, like this::

    ...
    "organizations": ["jernbaneverket", "statnett"]
    ...

The reason for not storing the list of users in the organization itself is to avoid having to update the organization
whenever a user is added or removed. Such a list of users can grow arbritrarily large, and we don't want to have
to upload the whole list of users each time we add or remove a user.

The authorization values are stored under an "authorization" key, like this::

    ...
    "authorization": {
      "jernbaneverket": {
        "principals": ["group:Admin"]
      },
      "statnett": {
        "principals": ["group:ReadonlyUser"]
      }
    }
    ...

Users and principals
~~~~~~~~~~~~~~~~~~~~

We use a scheme where each user is given a set of principals in an organization.

In the Sesam Node all Pipes, Datasets and Systems are protected by an ACL (Access Control List) that specified
which operation the various principals are allowed to perform on the resource.

For each type of resource, there is one hardcoded ACL. This ACLs are hardcoded in the Sesam Node source-code, and
should never need to change unless we implement some new functionality.

In the Sesam Node a custom ACL can be assigned to each individual Pipe, Data and System. This custom ACL will then
be evaluated before the default ACL for that item type.


On the Pipe, Dataset and System pages in the Sesam Management Studio, there is a "Permissions"-tab that can be used
to assign organization-specific principals to actions on that Pipe, Dataset or System.

For a pipe with a custom "start-pump" principal this tab looks something like this:


Default settings:

   ===== ================ ========== ========= ===========
   Type  Principal        start-pump stop-pump read-config
   ----- ---------------- ---------- --------- -----------
   Allow group:User            [ ]       [ ]        [x]
   Deny  group:Everyone        [x]       [x]        [x]
   ===== ================ ========== ========= ===========

Custom settings:

   ===== ================ ========== ========= ===========
   Type  Principal        start-pump stop-pump read-config
   ----- ---------------- ---------- --------- -----------
   Allow group:JobStarter     [x]       [ ]        [ ]
   ===== ================ ========== ========= ===========

-------------------
The JSON Web Tokens
-------------------

The JWT is created by the Sesam Portal (there is a "/jwt" web service that returns the JWT for the current user). This
JWT contains all the permissions that has been granted to the user in the Sesam Portal. The JWT payload looks
something like this::

   {
    "principals": {
      "global": ["email:someone@example.org"],
      <subscriptionid1>: {
        "principals": ["group:Admin"]
      },
      <subscriptionid2>: {
        "principals": ["group:User"]
      }
   }

The "principals" attribute is basically a copy of the "principals" attribute in the
user-data that is stored in the database. The main difference is that, in the Sesam Portal the user is assigned roles
for an organization, not for a subscription. But in the JWT, we only care about the subscription id, since that is
what the Sesam node uses.



-------------------
User management GUI
-------------------
We need somewhere to manage users and organizations. Probably as a part of the Sesam Portal.


Organization creation and membership management:
(https://jira.bouvet.no/browse/IS-3134)
   * add organization
   * modify the organization's metadata (at least the name of the organization).
   * delete the organization
   * disable the organization
   * list all users in the organization
   * invite a new user to join the organization by entering the email of the new user. This should send an email to
     the new user with instructions on how to sign up.
   * remove a user from the organization
   * disable a user in the organization (for temporarily stopping a user from doing anything)

Organization custom roles and permissions
(https://jira.bouvet.no/browse/IS-3150)
   * define a new custom principal
   * remove a custom principal

Organization user roles:
(https://jira.bouvet.no/browse/IS-3151)
   * add a principal to a user
   * remove a principal from a user


SESAM Subscription:
This is currently owned by each auth0 user, but it should be possible for an organization to own it, instead.
But users that belong to that organization should be able to administer the subscriptions owned by the organization.



---------------------------------------------
Sesam Portal authentication and authorization
---------------------------------------------

The Sesam Portal uses cookies and http sessions for authenticating the users. Here is a detailed description of how
this works:

1. client: The user points a webbrowser at https://portal.sesam.io
2. server: The web server at portal.sesam.io serves the Sesam Portal javascript web application.
3. client: The javascript calls the "/api/profile" webservice.
4. server: Checks if the cookies the client included contains a valid http session id. If it does,
   include the user-info in the response to the client. In either case, the response will contain the information
   that the client needs to communicate with the auth0 authentication services (client-secret, auth0 domain, etc).

If the user is not authenticated:

5. client: Uses the auth0 "Lock"-gui widget to let the user to sign in or to register for the first time.
6. auth0 server: Once the user has signed in (or created a new user-account), the client is redirected to the
   Sesam Portal's "/auth0_login" url with an authentication code.
7. server: Uses the authentication code to get the user's information from the auth0 server. Creates a http-session
   and stores the user-info in the session. Sends a redirect-response to "/" to the client.
8. client: Loads the web-application from scratch: Return to step (2). But since the user is now authenticated,
   we will end up on in step 5 in the "If the user is already authenticated"-path.

If the user is already authenticated:

5. client: Loads the "Dashboard" page and starts downloading more information from the server (subscriptions, etc).
   At this point all requests to the server will contain a cookie with the session-id. The server will use the
   user info stored in the http session to check user identity and permissions. At regular intervals the server will
   refresh the user info from the auth0 server, just in case the user-info has been directly modified via the
   admin-gui at https://auth0.com.



-----------------------------------------------
Sesam REST API authentication and authorization
-----------------------------------------------

The Sesam web API has two ways of authenticating the user. It can use either a cookie- and http-session based method,
similar to the Sesam Portal, or it can use a JWT (JSON Web Token) supplied in the "Authentication" header in each
http request.



-----------------------
Sesam Management Studio
-----------------------
The management gui uses cookies and http sessions for authenticating the user in the same way as the Sesam Portal
does it. The http session makes it possible for the user to directly access api services (for instance "/api/pipes")
in the web-browser with out having to manually provide an authorization token.

Here is a detailed description of how this works:

1. Sesam node client: The user points a webbrowser at the root sesam node url (for instance http://localhost:9042)
2. Sesam node server: The sesam node web server serves the Sesam Management Studio javascript web application.
3. Sesam node client: The javascript calls the root api url: "/api"
4. Sesam node server: returns a 401 "Authentication required" response if the user is not authenticated.

If the user is not authenticated:

5. Sesam node client: redirect the browser to the url
   https://portal.sesam.io/?managementStudioLoginRedirectURL=http://localhost:9042/login

6. Sesam portal client: If the user is not already authenticated in the portal, the portal shows the normal auth0-based
   login and logs in the user. (The auth0 callback url will contain the 'managementStudioLoginRedirectURL'
   parameter). If the user is authenticated

7. Sesam Portal server: creates a new random authorization code and uses this as a key to
   store the user's JWT in in-memory. Then it creates a new url based on the managementStudioLoginRedirectURL plus
   the authorization code, and redirects the client to the resulting url.

6. Sesam node server: Parses the JWT and verifies it using the Sesam Portal's public rsa key. Creates a http-session
   and stores the user-info and permissions from the JWT in the session. Sends an "ok"-response to the client.

7. client: Loads the "Dashboard" page and starts downloading more information from the server (as in step 5 in the
   "If the user is already authenticated" path).

If the user is already authenticated:

5. client: Loads the "Dashboard" page and starts downloading more information from the server (pipes, etc).
   At this point all requests to the server will contain a cookie with the session-id. The server will use the
   user info stored in the http session to check user identity and permissions.




------------------------
Sesam commandline client
------------------------

The commandline client uses JWT-based authentication. The authorization token to use can either be specified as a
commandline argument when invoking a command, or stored as a permanent default value by using the "config" command
(this is similar to how the "server_base_url" can be specified in these two ways).

The authorization token can be obtained in several different ways:
 1. The user can run the "login" command, which will let the user log in using their existing Sesam Portal username
    and password. The sesam client will log on to the Sesam portal and download and store an authorization token.
 2. The Sesam Portal has functionality for constructing authorization tokens with a specific subset of principals
    baked in; this can be useful to give other users a way to interact with the sesam commandline client without
    having their own users in the Sesam Portal. Example: A read-only authorization token could be given to users who
    only need to read data from the sesam node.

-----------------------------
Resource Types and operations
-----------------------------

Node
~~~~
	- write-metadata
	- read-metadata
	- write-secret
	- list-secrets
	- write-envvars
	- read-envvars


Systems - systems collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	- add item

system-prototype - applies to all system instances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	- write-config
	- read-config
	- read-data
	- write-data
	- read-metadata
	- write-metadata
	- delete

a system - a specific system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	- as prototype

datasets - datasets collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	- add dataset (if a user is able to create datasets. useful if you only want people to create pipes from existing datasets to external systems)

dataset-prototype - applies to all dataset instances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	- read-data      (if a user can use it as a source in a pipe)
	- write-data     (if a user can use it as a sink for a pipe)
	- delete         (if a user can delete this dataset)
	- read-endpoint  (if a user can read the data over the http endpoint)
	- read-metadata
	- write-metadata

a dataset - a specific dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	- as prototype

pipes - pipes collection
~~~~~~~~~~~~~~~~~~~~~~~~
	- add item

pipe-prototype - applies to all pipe instances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	- read-config
	- write-config
	- start-pump
	- stop-pump
	- disable-pump
	- read-execution-log
	- delete (if a user can delete this pipe)
	- endpoint-read-data (if the pipe exposes a named endpoint as the 'sink')
	- endpoint-write-data (if the pipe exposes a named endpoint as the 'source')
	- read-metadata
	- write-metadata

a pipe - a specific pipe
~~~~~~~~~~~~~~~~~~~~~~~~
	- as prototype

secrets collection
~~~~~~~~~~~~~~~~~~
	- add

a secret
~~~~~~~~
	- read
	- write
	- delete


----------------------------
Examples of common use cases
----------------------------


Public dataset
~~~~~~~~~~~~~~

In this case, the entities from one specific dataset (call it "X") should be publicly available.


In the Sesam management studio:
Update the permissions-checks on the "X" dataset by adding the following ACE (access control entry)

   ===== ================ ========== ========== =============
   Type  Principal        read-data  write-data read-endpoint
   ----- ---------------- ---------- ---------- -------------
   Allow group:Everyone      [ ]       [ ]           [x]
   ===== ================ ========== ========== =============


Restricted dataset
~~~~~~~~~~~~~~~~~~

In this case, the entities from one specific dataset (call it "Y") should be only be available for some specific users.

In the Sesam portal:
1. Create a new organization-specific principal and give it a descriptive name. For instance: "group:TrustedUser".

In the Sesam management studio:
Update the permission-checks on "Y" dataset by adding the following ACEs (access control entries):


   ===== ================= ========== ========== =============
   Type  Principal         read-data  write-data read-endpoint
   ----- ----------------- ---------- ---------- -------------
   Allow group:TrustedUser    [ ]       [ ]           [x]
   Deny  group:Everyone       [x]       [ ]           [x]
   ===== ================= ========== ========== =============



Restricted Pump
~~~~~~~~~~~~~~~

In this case, we have one pipe "Z" where only some specific users should be able to start the pump. This is very similar
to the `Restricted dataset`_. case.

In the Sesam portal:
1. Create a new organization-specific principal and give it a descriptive name. For instance: "group:ZStarter".

In the Sesam management studio:

Go to the "Pipes"-page, click on pipe "Z". On the "pipe Z" page, click on the "Permissions" tab.

Update the permissions-checks by adding the following ACEs (access control entries)

   ===== ================ ========== ========= ===========
   Type  Principal        start-pump stop-pump read-config
   ----- ---------------- ---------- --------- -----------
   Allow group:ZStarter       [x]       [ ]        [ ]
   Deny  group:Everyone       [x]       [ ]        [ ]
   ===== ================ ========== ========= ===========

---------------
Run-time checks
---------------

When a user creates a pipe, the pipe-configuration's "principals"-list is set to the principals that the user has.

At run-time this principals list is used to determine if the pipe's pump should be allowed to run.

For a pump to run the pipe MUST have read permission on the datasource and write permission on the sink.
In the case of a datasource for an external system it just needs read access for the system. When the source is a
dataset the pipe needs read access for that dataset. Similarly on the way out, writing to a dataset needs explicit
write to that dataset, writing to a system requires write permission for that system.

