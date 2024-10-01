Receiving webhook events
========================

The pipe should be called ``-event``.

Key concepts
------------
Key concepts in receiving webhook events:

* Before consuming webhook events, you must make sure to register the webhooks. See section :ref:`registering webhooks <registering_webhooks>`.
* In order to consume the webhook events, verify that the manifest includes ``"use_webhook_secrets": true``. This will create webhook secret and set ``group:Anonymous`` and ``write_data`` permissions to all event pipes.
* webhooks sign the payload with a secret key (often HMAC). The secret key is normally set by the ``-registerwebhook`` pipe. The event pipe must have the correct validation expression that uses the webhook secret. This is done to make sure that the webhook event is coming from the correct source.
* some systems use a default secret key, e.g. Shopify uses the ``client_secret`` to sign the webhook payload. In this case, the event pipe must have the correct validation expression that uses the client_secret and ``-registerwebhoook`` pipe don't send any secret key.

Example: validation expression
------------------------------

::

   "validation_expression": "{% if request_headers['X-Shopify-Hmac-SHA256'] == b64encode(hmacsha256digest(secret('oauth_client_secret'), request_body)) %}{% else %}FAIL!{% endif %}"

* When testing the webhooks with Sesampy on dev nodes, this is not automatically handled and you may need to manually put the ``client_secret`` value into the validation expression.
