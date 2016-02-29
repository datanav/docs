==================
JSON Push Protocol
==================


.. contents:: Table of Contents
   :depth: 2
   :local:

The JSON Push protocol is an HTTP-based protocol that uses POST
requests to perfom incremental or full data syncs across to an HTTP
endpoint. It supports splitting up the data into smaller batches, so
that not all the data have to be sent in a single request.

The protocol is supported by the ``http_endpoint`` source and the
``json_push`` sink.

Requests
--------


The following HTTP request parameters can be used to indicate what is happening:

.. list-table::
   :header-rows: 1
   :widths: 20, 80

   * - Parameter
     - Description

   * - sequence_id
     - A string token that is generated every time the data sync is
       started. Included in all requests.
     
   * - is_full
     - A boolean. Has the value ``true`` if this is a full data sync,
       and ``false`` if not. Included in all requests. The default
       value is ``false``.

   * - request_id
     - A string token that is generated for every request. Included
       in all requests.

   * - previous_request_id
     - A string token referencing the request_id of the
       previous request. Included in all but the first request.
     
   * - is_first
     - A boolean. Included in the first request with the value 'true'.
     
   * - is_last
     - A boolean. Included in the last request with the value 'true'.

The HTTP body is JSON data, either a JSON object if it is a single
entity or an JSON array of objects if it is a list of entities. The
serialisation of entities as JSON is described in more detail
:doc:`here <entitymodel>`.

If the sequence_id is not the same as the one that that is currently
active, then it will replace the active one (full sync only). Only a
single sequence_id should be active at any time. A sequence id goes
out of scope when the 'is_last=true' request parameter is given. Note
that an incremental request does not affect the active sequence.


Conflicts
---------

When doing an incremental sync the request parameters can silently be
ignored and the entities should be accepted.

The HTTP server should recognize these cases as conflicting when doing
a full data sync:

- The ``previous_request_id`` does not match with the request_id of the
  previous request. Return '409 Conflict'.

- The value of ``is_full`` is not the same as in the previous request of
  the same sequence. Return '409 Conflict'.

- The ``is_first`` request parameter is true when we know that it is not
  the first request in the active sequence. Return '409 Conflict'.

If the JSON Push Sink receives a ``409 Conflict`` response code, then it
must stop the active sync, and try again later. It should start from
the beginning with a new sequence if it was a full data sync.
