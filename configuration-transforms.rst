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

::

   {
       "_id": "mypipe",
       "name": "Name of pipe",
       "type": "pipe",
       ...
       "source": {
          ...
       },
       ..
       "transform": {
          "name": "name of transform (NOTE: deprecated)",
          "comment": "This is a comment",
          "description": "description of the transform (optional)"
           ...the rest of the transform configuration goes here...
       }
    }}




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
