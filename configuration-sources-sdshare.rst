
.. _sdshare_source:

SDShare source
--------------

The SDShare data source can read `RDF <https://www.w3.org/TR/2004/REC-rdf-primer-20040210/>`_ from `ATOM feeds <https://tools.ietf.org/html/rfc4287>`_ after the
`SDShare specification <http://www.sdshare.org>`_. See the :doc:`rdf-support` document for more information about working with RDF data
in Sesam.


It has the following properties:

Prototype
^^^^^^^^^

::

    {
       "type": "sdshare",
       "system": "url-or-microservice-system-id",
       "sort_lists": true,
       "url": "url-to-sdshare-fragments-feed"
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

   * - ``system``
     - String
     - The ID of the :ref:`URL system <url_system>` or :ref:`microservice system <microservice_system>` component to use.
     -
     - Yes

   * - ``url``
     - String
     - The URL of the SDShare fragments feed to consume.
     -
     - Yes

   * - ``sort_lists``
     - Boolean
     - If the ``sort_lists`` is set to ``true`` any resulting entity properties containing lists of values (due to
       them having the same RDF predicate) will be sorted, making the output predictable. This applies in a recursive
       fashion.
     - true
     -

Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``true`` (Default)

   * - ``is_since_comparable``
     - ``true`` (Fixed)

   * - ``is_chronological``
     - ``false`` (Default)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "sdshare",
            "url": "https://open.sesam.io/sdshare/server/1/fragments/enhetsregisteret"
        }
    }
