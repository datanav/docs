Share template extension points
===============================

The share template has specific access points which allows you to manipulate the content and structure of both the payload and the response. These should be used instead of additional transformation whenever possible.

Manipulating insert/update payloads
-----------------------------------

whenever we need to manipulate the content or structure of the payloads in the share template we can use the ``rewrite_rules_payload`` followed by ``rewrite_update_payload`` or the ``rewrite_insert_payload`` extension points documented in the :ref:`transform-share-rest <template_transform_share_rest>`  in docs. 

Manipulating responses
----------------------

At times we need to manipulate the update, insert or delete responses from a system, e.g. if the system returns a primary key in a different format than required. In order to do this we can use the ``rewrite_rules_mutation`` followed by ``rewrite_update``, ``rewrite_insert`` or the ``rewrite_delete`` extension points documented in the :ref:`transform-share-rest <template_transform_share_rest>`  in docs.

Manipulating lookup response
----------------------------

At times we need to manipulate the lookup response to make it fit with the expected format. In order to do this we can use the ``rewrite_rules_lookup`` followed by ``rewrite_lookup`` extension point documented in the :ref:`transform-share-rest <template_transform_share_rest>`  in docs.
