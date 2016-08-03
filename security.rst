========
Security
========

.. contents:: Table of Contents
   :depth: 2
   :local:


------------
Introduction
------------

NOTE: This document is just a suggestion on how we might handle security in SESAM. See the "Security in SESAM"
epic for what the current state of affairs actually is: https://jira.bouvet.no/browse/IS-3098.



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
independently of auth0. All role/permission information is stored by the Sesam Portal in a separate database.


-------------
Authorization
-------------

All role/permission information is stored by the Sesam Portal in an external database. We want to use a
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
        "roles": ["admin"]
      },
      "statnett": {
        "roles": ["readonly-user"]
      }
    }
    ...

Users, roles and permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We use a scheme where each user is given a set of roles in an organization. Each role is then assigned a set of
permissions.

There is one global, hardcoded table of common role/permissions which specifies which permissions each role confers.
The table looks something like this, where the first column contains the roles and the first row contains the
permissions (this is just a small portion of the real table; in reality it contains several other roles and
permissions):

=============== ================== ========= =============== ===================== =========================
Role\Permission create-delete-pipe edit-pipe start-stop-pump read-dataset-entities add-remove-role-from-user
--------------- ------------------ --------- --------------- --------------------- -------------------------
Admin                x                 x            x                 x                         x
User                                   x            x                 x
Public                                                                x
=============== ================== ========= =============== ===================== =========================

This table is hardcoded in the Sesam portal source-code. These are the global default settings, and should
never need to change unless we implement some new functionality. It contains the permissions that are hardcoded
in the Sesam portal and the Sesam node.

In addition to the global defaults, each organization can create its own roles and permissions for their own
specialized purposes. These roles and permissions can be used to restrict access to particular datasets or pipes,
or to give a user access to one specific dataset or pipe.

Below is an example of how an organization-specific role/permission table might look something.
The organization-specific stuff is displayed in bold. Note that the global hardcoded role/permissions mappings are
displayed, but cannot be modified:

================= =================== =============== ================== ========= =============== =====================
Role\Permission   **Read dataset X**  **Start job Y** create-delete-pipe edit-pipe start-stop-pump read-dataset-entities
----------------- ------------------- --------------- ------------------ --------- --------------- ---------------------
**Data fetcher**       **[x]**            **[ ]**             [ ]           [ ]         [x]                [ ]
**Job Starter**        **[ ]**            **[x]**             [ ]           [ ]         [x]                [ ]
Admin                  **[x]**            **[x]**              x             x           x                  x
User                   **[x]**            **[x]**                                        x                  x
Public                 **[ ]**            **[ ]**
================= =================== =============== ================== ========= =============== =====================

[Create new Role] [Create new Permission]

On the Pipe, Dataset and System pages in the Sesam Management Studio, there is a "Permissions"-tab that can be used
to assign organization-specific permissions to that Pipe, Dataset or System.

For a pipe with a custom "start-pump" permission this tab looks something like this:

================= =====================================================
Action            Permissions
----------------- -----------------------------------------------------
start-pump        **<Start job Y>**
read-entities     <read-pump-entities (default)>
================= =====================================================

For a dataset with a custom "read-entities" permission this tab looks something like this:

================= =========================================================
Action            Permissions
----------------- ---------------------------------------------------------
read-entities     **<Read dataset X>**
update-last-seen  <update-dataset-last-seen (default)>
================= =========================================================


-------------------
The JSON Web Tokens
-------------------

The JWT is created by the Sesam Portal (there is a "/jwt" web service that returns the JWT for the current user). This
JWT contains all the permissions that has been granted to the user in the Sesam Portal. The JWT payload looks
something like this::

   {
    "authorization": {
      <subscriptionid1>: {
        "permissions": ["create-delete-pipe", "edit-pipe", "start-stop-pump", "read-dataset-entities"]
      },
      <subscriptionid2>: {
        "permissions": ["read-dataset-entities"]
      }
   }

The "authorization" attribute is basically a flattened version of the "authorization" attribute in the
user-data that is stored in the database. In the Sesam Portal, each user is assigned a set of roles, not permissions,
since it is much easier to group permissions under roles that have to assign each permission separately. But in the
JWT we are only interested in the resulting permissions.

Also, in the Sesam Portal the user is assigned roles for an organization, not for a subscription. But in the JWT, we
only care about the subscription id, since that is what the Sesam node uses.




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
   * define a new custom role
   * remove a custom role
   * define a new custom permission
   * remove a custom permission
   * Assign a custom permission to a role
   * Remove a custom permission from a role

Organization user roles:
(https://jira.bouvet.no/browse/IS-3151)
   * add a role to a user
   * remove a role from a user


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
   we will end up on step 5b.

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



------------------------
Sesam commandline client
------------------------

The commandline client uses JWT-based authentication. The authorization token to use can either be specified as a
commandline argument when invoking a command, or stored as a permanent default value by using the "config" command
(this is similar to how the "server_base_url" can be specified in these two ways).

The authorization token can be obtained in several different ways:
 1. The user can run the "login" command, which will let the user log in using their existing Sesam Portal username
    and password. The sesam client will log on to the Sesam portal and download and store an authorization token.
 2. The Sesam Portal has functionality for constructing authorization tokens with specific permissions baked in;
    this can be useful to give other users a way to interact with the sesam commandline client without having their
    own users in the Sesam Portal. Example: A read-only authorization token could be given to users who only need to
    read data from the sesam node.


----------------------------
Examples of common use cases
----------------------------


Public dataset
~~~~~~~~~~~~~~

In this case, the entities from one specific dataset (call it "X") should be publicly available.

By default, reading the entities of a dataset requires the "read-dataset-entities" permission, which is not assigned
to the build-in "Public" role (the "Public" role represents anonymous users). But in this case we want to replace that
permission-requirement with a new organization-specific permission.

In the Sesam portal:
1. Create a new organization-specific permission and give it a descriptive name. For instance: "Read dataset X".
2. Assign the "Read dataset X" permission to the build-in "Public" role.

In the Sesam management studio:
Update the permission-checks on the "X" dataset from the default

    "read-dataset-entities (default)"

to

    **"Read dataset X"**


Restricted dataset
~~~~~~~~~~~~~~~~~~

In this case, the entities from one specific dataset (call it "Y") should be only be available for some specific users.
By default all datasets are protected by the "read-dataset-entities" permission, which is given to all authenticated
users.

In the Sesam portal:
1. Create a new organization-specific permission and give it a descriptive name. For instance: "Read dataset Y".
2. Create a new organization-specific role and give it a descriptive name. For instance: "Trusted user".
3. Assign the "Read dataset Y" permission to the "Trusted user" role.
4. Assign the "Trusted user" role to the users that should be allowed to read the entities from dataset "Y".

In the Sesam management studio:
Update the permission-checks on the "read-entities" action on the "Y" dataset from the default

    "read-dataset-entities (default)"

to

    "read-dataset-entities (default)" **AND "Read dataset Y"**



Restricted Pump
~~~~~~~~~~~~~~~

In this case, we have one pipe "Z" where only some specific users should be able to start the pump. This is very similar
to the `Restricted dataset`_. case.

By default the "start"-operation on all pump are protected by the "start-stop-pump" permission, which is given to
all authenticated users.

In the Sesam portal:
1. Create a new organization-specific permission and give it a descriptive name. For instance: "Start pump Z".
2. Create a new organization-specific role and give it a descriptive name. For instance: "Z starter".
3. Assign the "Start pump Z" permission to the "Z starter" role.
4. Assign the "Z starter" role to the users that should be allowed to start pump "Z".

In the Sesam management studio:

Go to the "Pipes"-page, click on pipe "Z". On the "pipe Z" page, click on the "Permissions" tab.

Update the permission-checks on the "start-pump"-action from the default

    "start-stop-pump (default)"

to

    "start-stop-pump (default)" **AND "Start pump Z"**

