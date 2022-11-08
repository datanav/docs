.. _source_section:

Sources
=======

Sources provide *streams* of :ref:`entities <entity-data-model>` as input to
the :ref:`pipes <pipe_section>` which is the building blocks for the
data flows in Sesam. These entities can take *any* shape (i.e. they
can also be nested), and have a single required property:
**_id**. This ``_id`` field must be *unique within a flow* for a
specific logical entity. There may exist multiple *versions* of this
entity within a flow, however.

Prototype
---------

The following *JSON* snippet shows the general form of a source definition.

..code-block::json

    {
        "type": "a-source-type",
        "comment": "This is a comment"
        
    }

The only universally required property is ``type``.

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
     - The type of the source, the allowed types are described below
     -
     - Yes

   * - ``comment``
     - String or list of strings
     - A human readable comment on the source.
     -
     -


.. _continuation_support:

Continuation support
--------------------

Sources can optionally support a ``since`` marker which lets them pick
up where the previous stream of entities left off - like a "bookmark"
in the entity stream. The ``since`` marker is opaque to the rest of
the Sesam components and it is assumed to be interpretable *only by
the source*. Within an entity the marker is carried in the
``_updated`` property if supported by its source.

    .. important::

        When using continuation support, Sesam will not be able to do automatic deletion tracking. If you wish to include deleted entities in your import, make sure you regularly set a full sync on the imported data.



Sesam supports a diverse set of core data sources. For many of the built-in source modules, such as many of the SQL sources, all you need to to is to place the property :ref:`updated_column <sql_source>` in the :ref:`source <source_section>` section of your config. It's corresponding value should be the column (if it exists) inside the SQL table which contains time-stamp or sequence information from when the row was last updated. For continuation support in a :ref:`microservice <microservices_in_Sesam>`, see the example at the bottom of this section.

There are four characteristics that describe continuation
support. All sources have these and there are three properties
available to describe them. The properties can be fixed, have a
default value or be calculated from other properties (aka dynamic) on
the source. The table below explains them in detail.

.. NOTE::

   It is important that you do not to set any of the boolean properties to
   ``true`` unless the source actually have these
   characteristics. Doing so can mean that the pump is not able track
   changes properly.

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 80

   * - Property
     - Type
     - Description

   * - ``supports_since``
     - Boolean
     - Does the source make use of the 'since' parameter if it gets
       passed one?

       This property is typically used to disable the tracking of the
       ``since`` marker. Sometimes it is not necessary to perform the
       tracking as the source won't make use of it anyway.

       .. NOTE::

          If you set ``supports_since`` to ``true`` then you should
          also make sure that you set either ``is_since_comparable`` to
          ``true`` or ``is_chronological`` to ``true`` — or *both*
          depending on the strategy you want.

   * - ``is_since_comparable``
     - Boolean
     - Can you compare two ``_updated`` values using lexical/bytewise
       comparison and decide their relative order?

       This property is used to specify if the values of two
       entities's ``_updated`` properties are always comparable. If
       the property can contain values of different types or
       structures, then it may not be possible to use lexical/bytewise
       comparison of the two values to decide order.

       .. NOTE::

          If you set ``is_since_comparable`` to ``true`` then you
          should also make sure that ``supports_since`` is set to
          ``true``.

   * - ``is_chronological``
     - Boolean
     - Does the source hand out entities in chronological order, i.e.
       in increasing order?

       If the entities are sorted in chronological other, then the
       pump can shift its ``since`` marker for each new entity in the
       stream. It can also store it away more often. This is a good
       characteristic to have as it makes the source able to continue
       where it left off even though the previous run did not complete
       fully. If the property is set to ``false`` then it can only
       know at the end of the run what the new ``since`` marker is.

       .. NOTE::

          If you set ``is_chronological`` to ``true`` then you
          should also make sure that ``supports_since`` is set to
          ``true``.


   * - ``initial_since_value``
     - String or integer
     - If set, the source will use this value as the "since" value if the pipe offset has not been set yet (or
       the pipe has been reset). It should be used when you don't want the source to fetch all available data when
       the pipe is initially run or has been reset. Note that this value is only used by sources that can support "since".


.. _strategy:

The strategy for tracking the ``since`` marker is chosen like this — and in this specific order:


1. If ``supports_since`` is ``true`` and ``is_chronological`` is ``true`` then continuation support is enabled and the *chronological* strategy is chosen. This strategy will store ``_updated`` values in the order we see them.

2. If ``supports_since`` is ``true`` and ``is_since_comparable`` is ``true`` then continuation support is enabled and the *max* strategy is chosen. This strategy will store the maximum ``_updated`` value seen in the run.

3. If none of the above apply, then continuation support is disabled. No tracking of the ``since`` marker is then done.

The table below shows which strategy is chosen depending on the value of the properties:

.. list-table::
   :header-rows: 1
   :widths: 25, 25, 25, 25

   * - ``supports_since``
     - ``is_since_comparable``
     - ``is_chronological``
     - Strategy

   * - ``false``
     - ``false``
     - ``false``
     - None

   * - ``false``
     - ``false``
     - ``true``
     - None

   * - ``false``
     - ``true``
     - ``false``
     - None

   * - ``false``
     - ``true``
     - ``true``
     - None

   * - ``true``
     - ``false``
     - ``false``
     - None

   * - ``true``
     - ``false``
     - ``true``
     - Chronological

   * - ``true``
     - ``true``
     - ``false``
     - Max

   * - ``true``
     - ``true``
     - ``true``
     - Chronological

If continuation support is enabled for a pipe, the ``since``
marker is stored in the ``pipe_offset`` property on the pump. Note that
one can use the pump's `update-last-seen
<api.html#post--pipes-pipe_id-pump>`_ operation in the :doc:`api` to
update or reset the ``pipe_offset`` value manually. This is useful in
cases where one wants to reprocess the data from scratch for some
reason. The :doc:`api` can also tell you what the current
``pipe_offset`` value is.

.. _continuation_support_microservices:

Continuation support for Microservices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you wish to activate continuation support for a :ref:`microservice <microservices_in_Sesam>` the pipe source needs to have the "supports_since" parameter set as true, as well as either the "is_since_comparable" or "is_chronological" strategy. An example of this is shown in the Sesam config example below.

.. raw:: html

   <details>
   <summary><a>Inbound pipe example of continuation support from a microservice</a></summary>

.. code-block:: python

  {
    "_id": "contacts-test",
    "type": "pipe",
    "source": {
      "type": "json",
      "system": "<system-name>",
      "is_since_comparable": true,
      "supports_since": true,
      "url": "/get-contacts"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["add", "_id", "_S.contactid"],
          ["copy", "*"]
        ]
      }
    },
    "pump": {
      "cron_expression": "0/10 * * * *",
      "rescan_cron_expression": "0 * * * *"
    }
  }

.. raw:: html

   </details>

The microservice needs to pass on an entity property named "_updated" to Sesam for each entity from the source. This property should take the value corresponding to the time-stamp or sequence value of the source data representing the last data update for that entity (the same column as for the "updated_column" for SQL type sources). When the entities have been passed on into Sesam, the inbound pipe will go through all these "_updated" values and pick the max value as the new "pipe_offset".

The first time the inbound pipe runs (or if the pipe is reset), the "pipe_offset" will not have a value, resulting in a complete import of all the data from the endpoint. Once data has been imported, the new "pipe_offset" will get passed to the microservice as the query parameter "since". This parameter can in turn be used as a query parameter to the API ensuring that only data updated after the last "since" value will be included in the GET request. An example of this is shown in the Python code snippet below.



.. raw:: html

   <details>
   <summary><a>Microservice example of continuation support</a></summary>

.. code-block:: python

  @app.route("/get-contacts", methods=["GET", "POST"])
  def get_contacts():
      token = auth()

      if request.args.get('since') is None:
          url = api_url + "/contacts"
      else:
          url = api_url + "/contacts?filter=modifiedon ge {}".format(request.args.get('since'))
      headers = {"Authorization": "Bearer {}".format(token)}

      req = requests.get(url = url, headers = headers)

      if req.status_code != 200:
        logger.error("Unexpected response status code: %d with response text %s" % (req.status_code, req.text))
        raise AssertionError ("Unexpected response status code: %d with response text %s"%(req.status_code, req.text))
      entities = req.json()["value"]

      for entity in entities:
        entity["_updated"] = entity["modifiedon"]

.. raw:: html

   </details>

In this case the data from the source is not ordered chronologically, which means we can not use the "is_chronological" tag. The benefit of chronologically ordered data in the source system is that if the pipe's pump for some reason should fail in the middle of a request, Sesam can use the chronological order of the source data to continue requesting data from the last received entity. If the data is not ordered, Sesam has to re-run the whole last request.




.. toctree::
   :hidden:
   :maxdepth: 1

   Dataset source <configuration-sources-dataset>
   Merge source <configuration-sources-merge>
   Union datasets source <configuration-sources-union-datasets>
   Merge datasets source <configuration-sources-merge-datasets>
   Diff datasets source (experimental) <configuration-sources-diff-datasets>
   Embedded source <configuration-sources-embedded>
   SQL source <configuration-sources-sql>
   Conditional source <configuration-sources-conditional>
   CSV source <configuration-sources-csv>
   RDF source <configuration-sources-rdf>
   SDShare source <configuration-sources-sdshare>
   LDAP source <configuration-sources-ldap>
   JSON source <configuration-sources-json>
   Empty source <configuration-sources-empty>
   HTTP endpoint source <configuration-sources-http>
   SPARQL source <configuration-sources-sparql>
   REST source (experimental) <configuration-sources-rest>
