Authentication
==============

The Consumer Portal uses the defined vendors of Sesam Talk as authentication providers. That means that a vendor needs to support an `OpenID Connect <https://openid.net/connect/>`_ authentication flow or an `Oauth2 <https://oauth.net/2/>`_ flow using the "authorization code" grant. We are also looking at the possibility of supporting the "implicit grant" flow in Oauth2.

This lets us identify both the user and the tenant that the user belongs to in the Portal and for general user management.
