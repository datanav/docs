Changelog
=========

2016-11-02
----------
* Added the :ref:`REST sink <rest_sink>` (Experimental).

2016-10-19
----------
* Added the :ref:`range <range_dtl_function>` DTL function.

2016-10-18
----------
* Added the :ref:`Embedded source <embedded_source>`. This is a data source that lets you embed data inside the configuration of the source. This is convenient when you have a small and static dataset.
  
2016-10-17
----------
* Added the :ref:`XML transform <xml_transform>` and :ref:`XML endpoint sink <xml_endpoint_sink>`. These can be
  used to generate XML documents inline in entities or published to external consumers, respectively.

2016-10-13
----------
* Changed the :ref:`CSV endpoint sink <csv_endpoint_sink>` to not output deleted entities by default. Added a new
  :ref:`skip-deleted-entities <csv_endpoint_sink_param_skip_deleted_entities>` config parameter that can be set
  to ``false`` if one want deleted entities to appear in the CSV output.

2016-10-10
----------
* Added DTL Reference Guide section that explains how :ref:`joins <joins>` work.

2016-10-04
----------
* Reworked DTL math functions to reflect that ``float`` is an allowed type in entities. If the function parameters are
  of mixed types, the result will be coerced to the type that is the most precise. I.e. float+decimal=decimal,
  int*float=float, int/div=decimal and so on. Not that this is a change in behaviour as entities that previously only
  had ``decimal`` as types after using DTL math functions if the input was of type float, now may end up with values
  that are floats instead. Use the dtl ``decimal`` cast-function to coerce the result to ``decimal`` if this is
  important to the application.
* Added ``is-float`` and ``float`` DTL functions. Changed ``is-decimal`` function so it no longer returns ``true`` if
  the argument is a ``float``. You will now have to add both a ``is-float`` and a ``is-decimal`` in an ``or`` clause
  to test for both types.

2016-09-28
----------
* Added Elasticsearch support, which includes a :ref:`system <elasticsearch_system>` and a :ref:`sink <elasticsearch_sink>`.
* The :ref:`Solr sink <solr_sink>` now supports :ref:`batching <pipe_batching>`.
* Added the ``commit_at_end`` property to the :ref:`Solr sink <solr_sink>` and the :ref:`Sesam databrowser sink <databrowser_sink>`.
* Moved the ``commit_within`` property from the :ref:`Solr system <solr_system>` to the :ref:`Solr sink <solr_sink>` and the :ref:`Sesam databrowser sink <databrowser_sink>`. The reason is that the commit rate is really specific to how and where it is used. This change is backward compatible, as the default value is taken from the system. It is recommended to update the configuration files accordingly.
* Moved the ``prefix_includes`` and ``keep_existing_solr_ids`` properties from the :ref:`Solr system <solr_system>` to the :ref:`Sesam databrowser sink <databrowser_sink>`. The reason is that they are only relevant there. This change is backward compatible, as the default value is taken from the system.  It is recommended to update the configuration files accordingly.

2016-09-28
----------
* Fixed the documentation for the :ref:`merge <dtl_transform-merge>` DTL transform; it mistakingly stated that
  the merge transformation would not overwrite existing attributes in the target entity.
* Updated the `/api/config GET" <./api.html#/config-GET>`_ endpoint to format the json in a more human-readable way.


2016-09-22
----------
* Added `index inspection on datasets <./api.html#/datasets/{dataset_id}/indexes-GET>`_.
* Added new `analyze-dtl <./api.html#/datasets/{dataset_id}-POST>`_ operation.
* Fixed automatic index creation for the `run-dtl <./api.html#/datasets/{dataset_id}-POST>`_ operation.
* Linked to the changelog from the Management Studio.


2016-09-21
----------
* Added the :ref:`datetime-shift <datetime-shift>` DTL function.
* Added support for timezones to the :ref:`datetime-parse <datetime-parse>` DTL function.
* Added missing sink- and source- prototypes in the "Edit pipe" gui in Management Studio.
* Fixed a bug that prevented users from adding a system in Management Studio.


2016-09-20
----------
* Fixed missing validation in the `/api/pipes "POST" <./api.html#/pipes-POST>`_ endpoint and added support for the "force" parameter.
* Fixed missing validation in the `/api/pipes/{pipe_id}/config "PUT" <./api.html#/pipes/{pipe_id}/config-PUT>`_ endpoint and added support for the "force" parameter.
* Fixed missing validation in the `/api/systems "POST" <./api.html#/systems-POST>`_ endpoint and added support for the "force" parameter.
* Fixed missing validation in the `/api/systems/{system_id}/config "PUT" <./api.html#/systems/{system_id}/config-PUT>`_ endpoint and added support for the "force" parameter.

2016-09-16
----------
* Added `JSON reformatting API with code style support <./api.html#/utils/reformat-config>`_.
