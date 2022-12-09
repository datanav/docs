Authentication
==============

The Consumer Portal uses the defined vendors of Sesam Talk as authentication providers. That means that a vendor needs to support an [OpenID Connect](https://openid.net/connect/) authentication flow or an [Oauth2](https://oauth.net/2/) flow using the "authorization_code" grant. This lets us identify both the user and the tenant that the user belongs to.
