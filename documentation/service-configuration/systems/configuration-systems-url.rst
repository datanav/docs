.. _url_system:

URL system
----------

The URL system represents a `HTTP server <https://en.wikipedia.org/wiki/Web_server>`_ (i.e. a web server)
serving `HTTP requests <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>`_ from a base url.
It supports the ``HTTP`` and ``HTTPS`` protocols. It provides session handling, connection pooling and authentication
services to sources and sinks which need to communicate with a HTTP server.

Prototype
^^^^^^^^^

::

    {
        "_id": "id-of-system",
        "name": "Name of system",
        "type": "system:url",
        "url_pattern": "http://host:port/path/%s",
        "verify_ssl": false,
        "custom_ca_pem_chain": "-----BEGIN CERTIFICATE-----\nMIIGYTCCB[...]\n-----END CERTIFICATE-----\n",
        "username": null,
        "password": null,
        "jwt_token": null,
        "headers": {
            "MY_HEADER": "some-value",
            "MY_OTHER_HEADER": "$ENV(key-for-other-value)",
            "MY_SECRET_HEADER": "$SECRET(secret-key)"
        },
        "oauth2": {
            "client_id": "my-client-id",
            "client_secret": "$SECRET(client-secret)",
            "token_url": "https://oath2-enabled-server:port/path/to/service/for/access/token",
            "access_token": "$SECRET(access-token)",
            "refresh_token": "$SECRET(refresh-token)",
            "scope": ["scope1", "scope2"],
            "extra": {
               "some": "extra-params",
               "to": "include-in-token-request"
            }
        },
        "proxies": {
            "http": "socks5://mysocksproxy:1234",
            "https": "socks5://user:password@mysslsocksproxy:1234",
        },
        "authentication": "basic",
        "connect_timeout": 60,
        "read_timeout": 1800
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``url_pattern``
     - String
     - Similar to ``base_url`` except one can use the ``%s`` token to tell where relative URLs are to be inserted into the ``url_pattern`` to produce absolute URLs. If ``%s`` is omitted then the relative URL is appended to the ``url_pattern``.
     -
     - Yes

   * - ``base_url``
     - String
     - Deprecated. Use the ``url_pattern`` property instead. The full URL of the base url of the HTTP server. Relative URLs are URL joined against this base URL to produce absolute URLs. Note that you may want a ``/`` at the end of the value.
     -
     -

   * - ``verify_ssl``
     - Boolean
     - Indicate to the client if it should attempt to verify the SSL certificate when communicating with the
       HTTP server over SSL/TLS.
     - ``false``
     -

   * - ``custom_ca_pem_chain``
     - String
     - If ``verify_ssl`` is set to ``true`` this property can hold a chain of certificates (in PEM format) that
       should be used to verify the SSL connection.
     -
     -

   * - ``username``
     - String
     - The username to use when authenticating with the HTTP server. Note that you also have to specify
       authentication protocol in ``authentication`` and ``password`` for this property to have any effect.
     -
     -

   * - ``password``
     - String
     - The password to use if ``username`` and ``authentication`` is set. It is mandatory if ``username`` is provided.
     -
     - Yes*

   * - ``jwt_token``
     - String
     - If ``authentication`` is set to ``jwt``, this property must hold the `JWT <https://jwt.io/>`_ token to use
       towards the remote server.
     -
     -

   * - ``headers``
     - Dict<String,String>
     - A optional set of header values to set as defaults in request made using the URL system. Both keys and values must
       evaluate to strings. Note that any "Authorization" header provided in this object is automatically overwritten
       when using the ``jwt_token`` property.
     -
     -

   * - ``authentication``
     - String
     - What kind of authentication protocol to use. Note that authentication is opt-in only and the default is no
       authentication. Allowed values is either "basic", "digest", "ntlm" or "jwt". Note that ``username``, ``password`` or ``jwt_token``
       might be also required depending on the authentication scheme selected.
     -
     -

   * - ``oauth2``
     - Dict<String,String>
     - A optional set of properties that specifies support for automatic fetching of JWT access tokens from a oauth2
       enabled provider. The grant types supported are "client credentials" and "refresh token". For the "client credentials"
       grant type you need to supply a ``client_id`` and ``client_secret`` from your oauth2 provider. You must also
       specify a ``token_url`` URL to a service which generates JWT access tokens. For the "refresh token"
       grant type you additionally need to provide ``access_token`` and ``refresh_token``. Optionally you can define a
       list of scopes (in ``scope``) for your client. Note that this option cannot be combined with ``JWT`` authentication
       or the ``jwt_token`` property. Also note that the oauth2 specification mandates TLS secured transport for both
       the token endpoint and the target defined in ``url_pattern``. You can add any extra parameters required by the
       service provider to the token request in the ``extra`` subattribute.
     -
     -

   * - ``proxies``
     - Dict<String,String>
     - A optional set of properties that specifies a set of SOCKS5 proxies for the URL system. The keys represents url-
       prefixes (for example 'http' and 'https') and the values of the HTTP(S) or SOCKS5 servers that the requests matching the
       prefixes should be passed through. The values should be on the form ``socks5://username:password@domain_or_ip:port``
       or .``http(s)://username:password@domain_or_ip:port``
       The ``username:password@..`` syntax is optional. If used, the embedded username and passord should be put into system
       secrets, i.e. ``$SECRET(username):$SECRET(password)@..``.
     -
     -

   * - ``connect_timeout``
     - Integer
     - Number of seconds to wait for connecting to the HTTP server before timing out.
     - ``60``
     -

   * - ``read_timeout``
     - Integer
     - Number of seconds to wait for the HTTP server to respond to a request before timing out.
     - ``1800``
     -

   * - ``ignore_invalid_content_length_response_header``
     - Boolean
     - Normally, the URL system will throw an error if the ``Content-Length`` header is present and
       contains an invalid value. The ``ignore_invalid_content_length_response_header`` property can be set to
       ``true`` in order to attempt to ignore such errors.
     - ``false``
     -

[1] Exactly one of ``base_url`` and ``url_pattern`` must be specified.

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "our-http-server",
        "name": "Our HTTP Server",
        "type": "system:url",
        "base_url": "http://our.domain.com/files"
    }

Example with ntlm configuration:

::

    {
        "_id": "our-http-server",
        "name": "Our HTTP Server",
        "type": "system:url",
        "authentication": "ntlm",
        "username": "$ENV(username-variable)",
        "password": "$SECRET(password-variable)",
        "base_url": "http://our.domain.com/files"
    }
