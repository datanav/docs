.. _schema-models:

:badge:`Free feature,badge-success badge-pill`

Schema models
=============

A model is a set of entity types. An entity type is a JSON schema, so in practice a model is an array of JSON schemas.

The purpose of a model is to serve as mechanism for grouping entity types, but also allow the user to add descriptions of properties to the JSON schema. Those descriptions are then aggregated up on the property landing page in the Management Studio.
Schema inferencing generates entity types for the pipe source and pipe sink. The sink entity types are automatically mapped to implicit models. You can find these in ``Browse`` > ``Models`` in the Management Studio. You can also filter entity types by model in ``Browse`` > ``Entity types``.

There are three built-in implicit models:

- ``Global`` contains the sink entity types of global pipes
- ``Input`` contains the sink entity types of inbound pipes
- ``Output`` contains the sink entity types of outbound pipes

An implicit model will also be generated for each unique pipe id prefix (the pipe id up until the first "``-``" character), e.g. the ``hubspot-contact`` and ``hubspot-company`` pipes both end up in the ``hubspot`` model.

You can customize what implicit models a pipe is put into by setting the pipe property ``metadata.models`` to an array of model ids, e.g. ``["foo", "bar"]``.

Explicit models can be uploaded through the :ref:`/api/models <api-reference>` APIs.