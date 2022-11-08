.. _transform_section:

Transforms
==========

Transforms sit between the source and the sink. Entities passed from a
source to a sink, can optionally be passed through a chain of
transforms before they are passed on to the sink. This makes it
possible to reshape the entities on their way to the sink. Transforms
can also be used to filter entities and construct new entities.

Transforms can be configured on a pipe by specifying the
"``transform``" property. The field is optional, and can contain
either a transform configuration object or a list of them.

Prototype
---------

The following *JSON* snippet shows the general form of a transform definition.

::

    {
        "type": "a-transform-type"
        "comment": "This is a comment"
        ..
    }

.. _transform_properties:

Properties
----------

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``type``
     - String
     - The type of the transform, the allowed types are described below
     -
     - Yes

   * - ``comment``
     - String or list of strings
     - A human readable comment on the transform.
     -
     -

   * - ``side_effects``
     - Boolean
     - Set to ``true`` if the transform has side-effects. A side-effect means that it causes changes to the system that it talks to. If the transform alters the system in any way, then this property must be set to ``true`` to prevent inadvertent changes to the system by features like pipe preview.
     - ``false``
     -

.. note::

  You can use a DTL transform with the following snippet ``["filter", ["neq", "_S._deleted", true]]`` to prevent further transforms to be performed on entities marked as deleted. Should only be used on dataset sinks and where ``_id`` is not rewritten.


.. toctree::
   :hidden:
   :maxdepth: 1

   DTL transform <configuration-transforms-dtl>
   JSON Schema validation transform <configuration-transforms-json-schema-validation>
   Conditional transform <configuration-transforms-conditional>
   HTTP transform <configuration-transforms-http>
   Emit children transform <configuration-transforms-emit-children>
   XML transform <configuration-transforms-xml>
   RDF transform <configuration-transforms-rdf>
   REST transform <configuration-transforms-rest>
