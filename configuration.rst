General
=======

 The datalake is configured using JSON structures, either on disk or by posting to the API (see the API section). The main
 concepts to configure for a node is the external systems and the flow between them and the lake. Also flows within
 the lake is configured the same way.

 The node configuration is a JSON list of one or more external system configurations and one or more pipe configurations describing
 the flows into, within and out of the lake from these external systems. These configuration entities are JSON dictionaries
 on the general form:

 ::

 [
   {
     "_id": "some-node-wide-unique-id"
     "type": "component-type:component-subtype",
     "other-properties": "other values",
     ..
   },
   {
     "_id": "some-other-node-wide-unique-id"
     "type": "component-type:component-subtype",
     "other-properties": "other values",
     ..
   },
   ..
 ]

Flows
=====

 A data flow is a set of pipes describing the flow of data entities from an external system, between datasets inside
 the lake and finally out of the lake to a external system. At the sources of each individual pipe in such a flow,
 optional transforms can be specified that transforms the entities streaming from the source to a another form
 before arriving at the destination sink.

 This transform is described using a domain specific language inspired by Lisp called 'DTL' (see the DTL section for
 more detail). The transformed entities can be entirely or partially constructed from entities from other datasets,
 like joins in SQL select statements, with the main difference that the result is persisted for each pipe in the flow.

 The datalake keeps track of the dependencies between datasets through DTL transforms in such a way that only changes
 are propagated along the flow based on what entities are changed at the ultimate source of the flows. This leads to
 a very efficient handling of entity streams within the lake.

The Pipe
========

 A pipe is a triple of a source, sink and data sync task. The task 'pumps' data in the form om entities from the source
 to the sink at regular or scheduled intervals.

 The configuration of a pipe has two forms; one 'complete' form and one short hand form. Let's describe the 'complete'
 form first and revisit the shorthand form after describing the various sinks and sources availble in the datalake core:

 ::

 {
    "_id": "pipe-id",
    "type": "pipe",
    "source": {
      ..
    },
    "sink": {
      ..
    }
    "task":  {
      ..
    }
 }

