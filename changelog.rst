Changelog
=========

2017-03-02
----------
* Added a :ref:`conditional source <conditional_source>` and :ref:`conditional sink <conditional_sink>` that can pick from a list of actual candidates, typically controlled by an environment variable.

2017-03-01
----------
* Added a :ref:`substring <substring_dtl_function>`  DTL function that returns a substring of another string given a start and end index.

2017-02-28
----------
* Added ``include_replaced`` property to the :ref:`dataset <dataset_source>` source. This property is used to filter out entities that are replaced by the :ref:`merge <merge_source>` source.

2017-02-20
----------
* Added ``url_pattern`` property to :ref:`URL system <url_system>`. This property gives you more control over how absolute URLs are produced. It can be used instead of the ``base_url`` property.

2017-02-14
----------
* Added a ``jwt`` authentication scheme and ``jwt_token`` property to the :ref:`URL system <url_system>`

2017-02-06
----------
* Added ``text_body_template`` and ``text_body_template_property``properties to the :ref:``EMail message sink <mail_message_sink>``. Use these to explicitly construct a plain-text version of your messages if sending multi-part messages.

2017-02-03
----------
* For security reasons, the Mail and SMS sinks no longer support file-based templates. Note that this is a non-backwards compatible change. You can use :ref:`environment variables <environment_variables>` and upload your existing template files using the environment variable API or the corresponding Management Studio form.

2017-02-01
----------
* Datasets are now scheduled for automatic compaction once every 24 hours. The default is to keep the last 2 versions up until the current time. It is possible to customize the automatic compaction. See documentation on :ref:`compaction <pipe_compaction>` for more information.

2017-01-26
----------
* The SQL source no longer includes columns with null values by default. You can include them by setting the ``preserve_null_values`` property of the SQL source to ``true``. Note that this is a change of the previous default behaviour.
* The CSV source no longer includes empty string values by default. You can include these by setting the CSV source property ``preserve_empty_strings`` to ``true``. Note that this is a change in the default behaviour.

2017-01-23
----------
* The ``dict`` function now takes zero, one or an even number of arguments. If zero arguments given then an empty dict is returned. If an even number of arguments then a new dict with each pair of arguments as key and value. The latter is convenient for easy construction of dicts.
* The transform functions :ref:`add <dtl_transform-add>`  and :ref:`default <dtl_transform-default>` now take an expression in their first argument. This means that the properties can be dynamic and that there can be multiple. :ref:`rename <dtl_transform-rename>` now takes dynamic arguments in the first and second positions.

2017-01-11
----------
*  Documented the ``pool_recycle`` option on :ref:`SQL systems <sql_system>` and changed its default from -1 (no recycling) to 1800 (30 minutes).

2017-01-06
----------
*  Added the :ref:`merge <merge_source>` source. This is a data source that is able to infer the sameness of entities across multiple datasets.

2017-01-04
----------
*  Added an ``unhandled_template_variable_replacement`` property to the :ref:`Email Message sink <mail_message_sink>`.

2016-12-20
----------
*  Added a ``uuid`` DTL function. It takes no parameters and returns a UUID object (type 4).

2016-12-19
----------
*  Added a ``disable_set_last_seen`` property to the :ref:`Pipe properties <pipe_section>`. If set to ``true``, it will not be possible to set or reset the ``last seen`` bookmark on the pipe using the API (i.e. protecting it from accidental changes by principals with write permission on the pipe).

2016-12-15
----------
* Added a ``read_retry_delay`` property to pipe pumps. This is used in conjunction with ``max_read_retries`` when the source is known to be sporadically (non-transiently) unavailable. See the :ref:`Pump section <pump_section>` for details.

2016-12-07
----------
* The documentation on :doc:`cron expressions <cron-expressions>` now makes it clear that they are evaluated in the `UTC <https://en.wikipedia.org/wiki/Coordinated_Universal_Time>`_ timezone.

2016-12-06
----------
* The :ref:`concat <concat_dtl_function>`  DTL function now takes a variable number of arguments. This avoids constructing unnecessary lists.

2016-11-30
----------
* The :ref:`url-quote <url_quote_dtl_function>`  DTL function now takes an optional ``SAFE_CHARS`` argument. This is especially useful when you don't want to quote the ``/`` character.

2016-11-22
----------
* The section on :ref:`Continuation Support <continuation_support>` has been extended. Each source now has a *Continuation support* table that shows the source's support for continuations.

2016-11-09
----------
* Added the :ref:`json <json_dtl_function>` and :ref:`json-transit <json_transit_dtl_function>` DTL functions.
* The :ref:`group-by <group_by_dtl_function>` DTL function has been changed to always return string keys. The string keys are the JSON transit encoded (same type of string as the :ref:`json-transit <json_transit_dtl_function>` function produces). The reason is that the :ref:`entity data model <entity_data_types>` (and `JSON <http://json.org/>`_) only supports string keys. ``group-by`` has also gotten an optional STRING_FUNCTION argument which lets you specify a custom function to create the string keys.
* The :ref:`sorted <sorted_dtl_function>`, :ref:`sorted-descending <sorted_descending_dtl_function>`, :ref:`min <min_dtl_function>`, :ref:`max <max_dtl_function>` DTL functions have been updated to support :ref:`mixed type ordering <mixed_type_ordering>`.

2016-11-07
----------
* Added the :ref:`microservice system <microservice_system>` (Experimental).

2016-11-03
----------
* Added the ``filename`` property to the :ref:`HTTP endpoint sink <http_endpoint_sink>`, :ref:`XML endpoint sink <xml_endpoint_sink>` and :ref:`CSV endpoint sink <csv_endpoint_sink>`. This property provides a hint to HTTP clients on what filename to use when downloading data (via the ``Content-Disposition`` header property).

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
