Changelog
=========

2017-11-08
----------
* The :ref:`JSON push sink  <json_push_sink>` now supports customizable HTTP headers via a ``headers`` property.

2017-10-12
----------
* Documented the :doc:`JSON Pull Protocol <json-pull>`.

2017-10-09
----------
* If a pipe is running and the pipe-config is modified, the pipe will no longer be stopped. Instead
  a "An old version of the pipe is still running" warning will be displayed, and it is up to the user
  if they want to stop the running pipe or not.

2017-09-06
----------
* Improved and expanded documentation on :ref:`namespaced identifiers <namespaces>` and the features related to it.
* Moved the deprecations to a :ref:`separate document <deprecations>`.

2017-09-05
----------
* Added a ``track_dead_letters`` option to the pump configuration. If set to true, it will delete "dead" entities from the dead letter dataset if a later version of it is successfully written to the sink. Note that using this option incurs a performance cost so use with care.

2017-08-23
----------
* It is now possible to specify ``track-dependencies`` on all the HOPS_SPEC in a specific :ref:`hops <hops_function>` DTL function. This change was made so that one can disable tracking for any of the HOP_SPECs, not just the last one.

2017-08-16
----------
* The :ref:`json-parse <json_parse_dtl_function>` and :ref:`json-transit-parse <json_transit_parse_dtl_function>` DTL functions now accept an optional default value expression. The default value expression is used when the input value is not valid JSON.

2017-08-08
----------
* The :ref:`datetime-parse <datetime-parse>` and :ref:`datetime-format <datetime-format>` DTL functions now accept an optional timezone argument. This makes it possible to parse datetime strings and format datetime values in specific timezones.

2017-06-29
----------
* When a pipe is reset then the pipe's retry queue is now also reset.
* Bug fix: It is now possible to interrupt pumps that are performing retries.
* Indexing of datasets changed so that each dataset is indexed for a maximum of five minutes in each iteration. This prevents some datasets from being blocked from indexing when there are other large datasets being indexed.

2017-06-26
----------
* Added the :ref:`enumerate <enumerate_dtl_function>` DTL function that can be used to enumerate values, i.e. combine values with an enumeration count.
* Added the :ref:`json-parse <json_parse_dtl_function>` and :ref:`json-transit-parse <json_transit_parse_dtl_function>` DTL functions.

2017-06-23
----------
* Added a :ref:`conditional transform <conditional_transform>`. This works the same way as conditional sinks and sources.

2017-06-20
----------
* Added functionality for preventing *all* pipes from automatically running (useful in some debugging
  scenarios). See the `Low level debugging <./low-level-debugging.html#preventing-pipes-from-automatically-running>`_ page for
  details.

2017-06-16
----------
* Added a ``is_sorted`` property to the :ref:`RDF source <rdf_source>` to indicate that the input data is sorted
  on subject, enabling the source to avoid loading the entire file into memory. Note that it only works for
  ``nt`` (NTriples) format files without blank nodes.

2017-06-12
----------
* Added a ``write_retry_delay`` property to pipe pumps. This is used in conjunction with
  ``max_consecutive_write_errors`` when the system the pipe is writing to is known to be
  sporadically (non-transiently) unavailable. See the :ref:`Pump section <pump_section>` for details.

2017-06-08
----------
* The :doc:`Security <security>` document now contains a description of
  :ref:`users, roles and permissions in Sesam.<security_subscriptions_users_roles_and_permissions>`

2017-05-31
----------
* Added support for bulk operations in the :ref:`SQL sink <sql_sink>`. Bulk operations are currently only
  supported for the :ref:`MSSQL and Microsoft Azure SQL Data Warehouse <mssql-bulk-operations>`
  systems.

2017-05-29
----------
* Added the ``indexes`` property to the :ref:`dataset <dataset_sink>` sink. If set to ``"$ids"`` then an index will be maintained for the ``$ids`` property. This index will then be used by the dataset browser to look up entities both by _id and $ids.
* The default value of the ``max_depth`` property in :ref:`hops <hops_function>` has been changed from ``null`` to ``10``. This means that the default is to stop the recursion at level 10.

2017-05-26
----------
* The JSON push protocol has been simplified to make it easier to write receivers. It will now always
  send the entities as an array, even if it contains just a single object. The JSON push sink has been updated to
  reflect this. If you need single-object JSON POST/PUT operations, you should use the REST sink instead.
* Systems now support environment variables in their config like pipes do

2017-05-19
----------
* Added the :ref:`tuples <tuples_dtl_function>` DTL function that can be used to create composite join keys.

2017-04-28
----------
* The ``equality`` property on the ``merge`` source is now optional.

2017-04-24
----------
* Changed the default value of the "schedule_interval" :ref:`pump <pump_section>` configuration property. Before, the
  default value was 30 seconds for all pipes. The new default value for
  pipes with a :ref:`dataset sink <dataset_sink>` *and* a :ref:`dataset sink <dataset_source>` is now
  30 seconds +/- 1.5 seconds. For all other pipes, the default is 900 seconds +/- 45 seconds.
  (The ``+/-`` part helps stagger the start-time of the pipes, so that we don't get lots of pipes starting at the
  same instant.)
* Added a warning in the GUI for non-internal pipes that don't have a "schedule_interval" or a "cron_expression"
  attribute set.


2017-03-30
----------
* Extended all :ref:`systems <system_section>` to accept a new property ``worker_threads`` that limits the number of concurrent pipes that can run against a particular system. The default value is 10. For input pipes the source system is used and for output pipes the sink system is used. For internal pipes, the the pool has 50 worker threads (i.e. for dataset to dataset pipes or receiver/publisher endpoints).

2017-03-24
----------
* Extended the :ref:`URL system <url_system>` and :ref:`REST system <rest_system>` to accept default custom request headers using the ``headers`` property. Also fixed the REST system schema to reflect authentication options and the ``jwt_token`` property.

2017-03-20
----------
* Extended the :ref:`in <in_dtl_function>` DTL function to allow a single value in the second argument.

2017-03-16
----------
* The :doc:`JSON Push Protocol <json-push>` document now contains :ref:`examples <json_push_examples>` of how to use ``curl`` to perform incremental and full syncs.

2017-03-15
----------
* Added the :ref:`_R <r_variable>` variable, which can be used to refer to the root context in a DTL transform.

2017-03-14
----------
* The ``base_url`` property of the :ref:`URL system <url_system>` and :ref:`REST system <rest_system>` has been deprecated. It has been superseded by the the ``url_pattern`` property.

2017-03-10
----------
* Added the :ref:`slice <slice_dtl_function>`, :ref:`insert <insert_dtl_function>` and :ref:`combine <combine_dtl_function>` DTL functions that can be used to manipulate lists.

2017-03-09
----------
* Added the :ref:`is-changed <is_changed_dtl_function>` DTL function that can be used compare data from the current and the previous version of the source entity.

2017-03-07
----------
* Added :ref:`encrypt <encrypt_dtl_function>` and :ref:`decrypt <decrypt_dtl_function>` DTL functions

2017-03-02
----------
* Added a :ref:`conditional source <conditional_source>` and :ref:`conditional sink <conditional_sink>` that can pick from a list of actual candidates, typically controlled by an environment variable.

2017-03-01
----------
* Added a :ref:`substring <substring_dtl_function>` DTL function that returns a substring of another string given a start and end index.

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
