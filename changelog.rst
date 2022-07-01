Changelog
=========

.. _changelog_2022_07_01:

2022-07-01
----------
* Added a "discard-inferred-schema" pump operation to the service API. This operation will discard any inferred schema entries for the pipe and writes a special "pump-discard-inferred-schema" entity to the pipe execution log for reference. This operation can only be done on non-running pipes.
* Behavioural change: all pipes that have ``infer_pipe_entity_types`` set to ``true`` either explicitly or via the corresponding global setting, and have a source with continuation support, will now discard their inferred schemas upon being reset.

.. _changelog_2022_06_30:

2022-06-30
----------

* Added a new property :ref:`include_completeness <include_completeness>` to pipes. This property specifies a list of
  dataset ids that should contribute to the completeness timestamp value of the sink dataset. By default, this property
  is equal to the pipe's input datasets, minus any datasets listed in :ref:`exclude_completeness <exclude_completeness>`.
* Pipes that fail to infer their schemas due to limitations on the resulting schema size will no longer fail. The
  :ref:`inferred schema <schema-inferencing>` will instead be truncated and marked as such and the pipe will not
  attempt to do schema inference the next time it runs.

.. _changelog_2022_06_08:

2022-06-08
----------

* The :ref:`VPN <concepts-vpn>` feature now supports high availability for connections. This means that you can set up redundant connections that can be failed over to. This is a :ref:`multi <pricing-production>` subscription only feature.

.. _changelog_2022_05_20:

2022-05-20
----------

* It is now possible to automatically migrate a :ref:`single <pricing-production>` subscription to a :ref:`multi <pricing-production>` subscription. A multi subscription is a scale-out architecture that lets you run pipes and microservices on horizontally scalable hardware. Contact `support <https://support.sesam.io/>`_ if you would like to migrate your single subscription.

.. _changelog_2022_05_19:

2022-05-19
----------

* Added the :ref:`literal <literal_dtl_function>` DTL function.

.. _changelog_2022_05_12:

2022-05-12
----------

* A pipe with :ref:`automatic reprocessing  <automatic_reprocessing>` enabled will now automatically reset if the :ref:`dependency tracking threshold <pipe_properties>` is reached.

.. _changelog_2022_05_03:

2022-05-03
----------

* Transforms now have a :ref:`side_effects <transform_properties>` property that specifies if the transform has side-effects or not. A side-effect means that it causes changes to the system that it talks to. If the transform alters the system in any way, then this property must be set to true to prevent inadvertent changes to the system by features like pipe preview.
* Corrected a bug that for multi subscriptions would cause the default maximum concurrent pipes for a SQL system to be 20 instead of the 10 and essentially unlimited for non-SQL systems. Note that the default number of concurrent pipe for all systems is controlled by the ``worker_threads`` property available on all :ref:`systems <system_section>` and is 10 by default.

.. _changelog_2022_04_25:

2022-04-25
----------

* Documented the :ref:`resource quotas <microservice_system_resource_quotas>` for microservices.
* The default value of ``max_merged`` in the :ref:`merge source <merge_source>` is now set as a global default in the
  :ref:`service metadata <service_metadata_global_defaults_max_merged>`, and
  the default value has been increased to 50000 entities. This is a very high number of entities for the merge source
  to handle at once, and merge sources will start using up large amounts of RAM before hitting this default limit. It
  is recommended to reduce this limit to prevent such high memory usage and then reconfigure any pipes that attempt to
  merge too many entities.

.. _changelog_2022_04_19:

2022-04-19
----------

* Added a new property ``max_merged`` with a default value of 100 entities to the :ref:`merge source <merge_source>`.
  Pipes that attempt to merge more entities than ``max_merged`` will fail with this change. The motivation for adding this
  new property is that merge sources generally should not be merging that many entities in the first place, and the merge
  process can end up using excessive amounts of RAM.

.. _changelog_2022_04_07:

2022-04-07
----------

* :ref:`Schema inferencing <schema-inferencing>` has been extended to collect namespaces used in :ref:`NI values <namespaces>`.

.. _changelog_2022_03_31:

2022-03-31
----------

* Added support for :ref:`Metrics <concepts-metrics-api>`.
* New data option `Metrics and monitoring` in :ref:`test and production pricing <pricing-production>` replaces the pr. pipe monitoring option. Pipe monitoring will still be available for existing subscription that is already using this.

.. _changelog_2022_03_25:

2022-03-25
----------

* New developer subscription size :ref:`Developer Pro <pricing-developer>` is now available.
* Added support for :ref:`Durable Data <concepts-durable-data>`.

.. _changelog_2022_03_24:

2022-03-24
----------

* Subscriptions created in the portal are now provisioned with the :ref:`Clustered architecture <changelog_2022_02_11>`.

.. _changelog_2022_03_21:

2022-03-21
----------

* The :doc:`Databrowser <databrowser>` tool will reach end-of-life December 31st 2023. It is superseded by the
  :ref:`Integrated Search <concepts-integrated-search>` feature. We will notify the current subscribers soon.
* Added a property ``ignore_non_existent_datasets`` to the :ref:`merge <merge_source>`, :ref:`merge_datasets <merge_datasets_source>` and :ref:`union_datasets <union_datasets_source>` sources. By default, listing one or or more datasets in ``initial_datasets`` that do not exist does not prevent the source from being populated. Setting ``ignore_non_existent_datasets`` to ``false`` will make the pipe fail if any non-existent datasets are listed in ``datasets``.
* Fixed a bug where the ``initial_datasets`` property was initialized as an empty list in the :ref:`merge <merge_source>`, :ref:`merge_datasets <merge_datasets_source>` and :ref:`union_datasets <union_datasets_source>` sources if ``initial_datasets`` was not explicitly set. The property now defaults correctly to the same list of datasets listed in ``datasets``. This is a breaking change.
* The :ref:`dataset <dataset_source>` and :ref:`diff_datasets <diff_datasets_source>` now warn the user if any input datasets do not exist. This also applies to the :ref:`merge <merge_source>`, :ref:`merge_datasets <merge_datasets_source>` and :ref:`union_datasets <union_datasets_source>` sources if ``ignore_non_existent_datasets`` is ``false``.

.. _changelog_2022_03_10:

2022-03-10
----------

* Restructured this documentation site. :doc:`What's Sesam <index-whatis>` is targeted at architects and decision makers. :doc:`User guide <index-developer>` is targeted at users of Sesam, with new subsections for :doc:`Data synchronization <index-synchronization>`, :doc:`Data modelling <index-datamodelling>`, :doc:`Data platforms <index-dataplatforms>` and :doc:`Operations <index-operations>`.

.. _changelog_2022_03_03:

2022-03-03
----------

* Pipes with ``manual`` or ``off`` pump mode can now be disabled and enabled.

.. _changelog_2022_02_11:

2022-02-11
----------

* As part of the :ref:`Clustered architecture everywhere <roadmap_clustered_architecture>` initiative we are now in the process of migrating in-cloud subscriptions over to it. You can find the provisioning status of a subscription in ``Subscription`` > ``Basics`` in the :doc:`Management Studio <management-studio>`. There you can see which provisioner version it is running (``version 1`` is old single machine service, ``version 2`` is the new clustered service, if self-hosted it will say ``self-hosted``).

Changes to the user experience:

* Pipes are now being provisioned asynchronous, this is reflected in the UI.
* Config upload when using sesam-py can report taking a little longer.


.. _changelog_2022_02_04:

2022-02-04
----------

* The :ref:`hash128 <hash128_dtl_function>` DTL function now takes an optional seed argument.

.. _changelog_2022_01_25:

2022-01-25
----------

* The :ref:`lower keys <lower_keys_transform>`, :ref:`upper keys <upper_keys_transform>` and :ref:`undirected graph <undirected_graph_transform>` transforms have been deprecated. :ref:`DTL transforms <dtl_transform>` can replace the functionality of lower keys and upper keys transforms.

.. _changelog_2022_01_24:

2022-01-24
----------

* Added a new property :ref:`remove_pk_char_trailing_spaces <remove_pk_char_sql>` to the :ref:`SQL sink <sql_sink>`. This property is enabled by default and fixes an issue with updating table rows when the primary key is of type ``nchar`` or ``char``.

.. _changelog_2022_01_20:

2022-01-20
----------

* Added custom header functionality to :ref:`HTTP transforms <http_transform>`.

.. _changelog_2022_01_12:

2022-01-12
----------

* Added domain name validation to ``docker.hosts`` property on :ref:`microservice systems <microservice_system>`. This ensures that domain names are
  on a format that is accepted by Kubernetes.

.. _changelog_2022_01_03:

2022-01-03
----------

* Added a new :ref:`resolved_entity <execution_log_resolved_entity>` property to write-error entities in the :doc:`execution log <pump-execution>`.
  It contains the entity that was used to resolve the write-error if it is different from the original entity that
  caused the write-error. This property is also set for any tracked dead letters that has been resolved
  (on the deleted dead letter). Fixed a bug where the :ref:`resolved <execution_log_resolved_property>` property was not set (to ``true``) if a
  write-error entity was successfully retried.

.. _changelog_2021_12_20:

2021-12-20
----------

* Renamed the ``prefilters`` property in the :ref:`hops <hops_dtl_function>` DTL function to ``subsets``.
  ``prefilters`` had some known issues and is now deprecated. Note that you may have to reset the pipe if you
  change from ``prefilters`` to ``subsets``. All new pipes should use ``subsets`` to get the documented behaviour.

.. _changelog_2021_12_17:

2021-12-17
----------

* Added ``custom_ca_pem_chain``  property to the :ref:`URL system <url_system>` and :ref:`REST system <rest_system>`.
  This property can hold a custom chain of certificates (in PEM format) that will be used to validate the SSL
  connection if ``verify_ssl`` is set to ``true``.

.. _changelog_2021_12_11:

2021-12-11
----------

* Our security team has investigated the impact of CVE-2021-44228. The following components have been
  analysed as they could potentially be affected:

  #. Integrated search. This component uses Elasticsearch under the hood. The version of Elasticsearch that we use is
     not affected according to this `Elastic Security announcement <https://discuss.elastic
     .co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476>`_.
  #. Legacy Databrowser. This component uses Apache Solr under the hood. The version of Solr that we use is not
     affected according to this `Solr Security announcement <https://solr.apache.org/security
     .html#apache-solr-affected-by-apache-log4j-cve-2021-44228>`_.
  #. GDPR Portal. This component uses Apache Solr under the hood. The version of Solr that we use is not
     affected according to this `Solr Security announcement <https://solr.apache.org/security
     .html#apache-solr-affected-by-apache-log4j-cve-2021-44228>`_.
  #. Unofficial OCI images that are hosted as microservices. These components *can* be affected, and our users
     need to make sure they only run code that they trust.

.. _changelog_2021_11_29:

2021-11-29
----------

* Changed the default value of the ``global_defaults.use_signalling_internally`` property of the :ref:`service metadata <service_metadata_section>` section to ``true``. This property was previously ``false`` by default

.. _changelog_2021_11_26:

2021-11-26
----------
* :ref:`Integrated search <concepts-integrated-search>` is now available for subscriptions running on the
  Clustered Architecture.
* :ref:`VPN <concepts-vpn>` is now configurable for subscriptions running on the Clustered Architecture.

.. _changelog_2021_11_19:

2021-11-19
----------
* The IP address of our log shipping receiver endpoint has changed from ``13.74.166.9`` to ``52.142.116.113``. If you run a self-hosted service and have blocked outgoing traffic then you need to update the firewall accordingly. See the :ref:`Self-hosted service <self_hosted_outbound_firewall_rules>` document.

.. _changelog_2021_17_11:

* Changed the name of "The Microsoft Azure SQL Data Warehouse system" to :ref:`"Microsoft SQL Server system" <mssql-sqlserver_system>` and "The MSSQL system" to :ref:`"Legacy Microsoft SQL system" <mssql_system>`
* The :ref:`"Legacy Microsoft SQL system" <mssql_system>` has been superceeded by the :ref:`"Microsoft SQL Server system" <mssql-sqlserver_system>` and will likely be deprecated in the future
* The :ref:`"Microsoft SQL Server system" <mssql-sqlserver_system>` has a new type ``"system:sqlserver"`` which replaces the old ``"system:mssql-azure-dw"``, which is kept as an alias for now
* Additional note: the recommended :ref:`"Microsoft SQL Server system" <mssql-sqlserver_system>` uses official Microsoft (ODBC) drivers while the :ref:`"Legacy Microsoft SQL system" <mssql_system>` uses open source drivers. The Microsoft ODBC drivers should support all current Microsoft SQL Server compatible products, including Azure Synapse Analytics (previously known as Azure SQL DataWarehouse). Note that switching from the "Legacy Microsoft SQL system" (``"system:mssql``) to the preferred :ref:`"Microsoft SQL Server system" <mssql-sqlserver_system>` (``"system:sqlserver"`` aka ``"system:mssql-azure-dw"``) can lead to minor data differences in properties due to the different driver backends

.. _changelog_2021_11_11:

2021-11-11
----------
* Added a ``encode_error_strategy`` property to the :ref:`CSV endpoint <csv_endpoint_sink>` - it tells the sink how to deal with encoding errors when the encoding is different from "utf-8", the default is to use a "backslashed unicode" replacement but other strategies can be chosen

.. _changelog_2021_11_09:

2021-11-09
----------
* Added a "discard-retries" pump operation to the service API - it is available in the UI as a "Discard retry queue" menu item on pipes. This operation will make the next pipe run ignore any previous write error retries by writing a special "pump-discard-retries" entity to the pipes execution log. This operation can only be done on non-running pipes.

.. _changelog_2021_11_03:

2021-11-03
----------
* Added missing :ref:`is-uuid <is_uuid_dtl_function>` and :ref:`is-bytes <is_bytes_dtl_function>` DTL functions

.. _changelog_2021_10_25:

2021-10-25
----------
* Added a ``byte_order_mark`` property to the :ref:`CSV endpoint <csv_endpoint_sink>` and :ref:`XML endpoint <xml_endpoint_sink>` sinks. If ``true`` these sinks will emit a UTF-8 byte order mark (BOM) to the start of the file/stream. It's ``false`` by default and should only be used in conjunction with a UTF-8 encoding.

.. _changelog_2021_10_11:

2021-10-11
----------
* The :ref:`http_endpoint <http_endpoint_source>` source will now get its :ref:`completeness <completeness>` value
  from the "X-Dataset-Completeness" http request header, if it is present.
  If the header is not present, the current time will be used instead, just as before.

.. _changelog_2021_09_29:

2021-09-29
----------

* Added a new :ref:`Quick Reference <quick-reference>` document for faster and easier navigation to configuration types and DTL transforms and functions.

.. _changelog_2021_09_28:

2021-09-28
----------

* Added the (experimental) :ref:`ni-collapse <ni_collapse_dtl_function>` and :ref:`ni-expand <ni_expand_dtl_function>` DTL functions. Note that these are only meant to work with the ``global_defaults.symmetric_namespace_collapse`` service metadata option set to ``true`` (``false`` by default while this functionality is in experimental state)

.. _changelog_2021_09_27:

2021-09-27
----------

* The "Datasets" page has been removed.
* A dataset is managed by a pipe and considered a part the pipe. All the details about a dataset have therefore been moved to the pipe page of the pipe that writes to the dataset (under Output). Internal datasets can be found under "Datahub" > "Internal datasets".


.. _changelog_2021_09_01:

2021-09-01
----------

* Added an :ref:`explanation <hops_function_targeting_sink>` about why you should not hop to the sink dataset.


.. _changelog_2021_08_16:

2021-08-16
----------

* Clarified when the ``is_first`` and ``is_last`` flags can be expected to be set in the Sesam :doc:`JSON Push Protocol <json-push>` - these flags are only set when running a full sync (i.e. not when in incremental mode). They are intended to signal to the client the start and end of a full sync run across multiple requests.
* Fixed a bug in the :ref:`JSON (push) sink <json_sink>` that set the ``is_first`` flag also on incremental syncs.

.. _changelog_2021_08_04:

2021-08-04
----------

* Added a ``header`` property to the :ref:`JSON source <json_source>`. This property can be used to specify
  additional header values to be set when doing HTTP GET requests. This was added to make the JSON source
  symmetrical with the :ref:`JSON (push) sink <json_sink>`. Note that both the JSON source and sink
  adhere to the Sesam specific :doc:`JSON Pull Protocol <json-pull>`. Consider using the more general REST source or
  sink if you're interacting with a non-Sesam JSON capable REST api.

.. _changelog_2021_06_14:

2021-06-14
----------

* Added a ``json_content_types`` property to the :ref:`REST system <rest_system>`. This property can be used to specify
  additional JSON content types to accept besides the default "application/json". The content must still be valid JSON.
  Note that the REST source will no longer attempt to parse all responses as JSON but check the content-type against the
  list of recognised content-types first. If the response content-type is not in this list, it will be treated as
  "unknown" and an empty entity containing a property with the response body (and optionally the content type) will be
  emitted for further processing with DTL. Support for ``response_include_content_type`` and ``response_property`` has
  been added to the REST source for this scenario.

.. _changelog_2021_06_09:

2021-06-09
----------

* Added a ``initial_since_value`` property to the :ref:`source <continuation_support>` configuration. This property holds the "since" value to use by the source when the pipe offset is unset (or has been reset).
* The ``since_default`` property of the :ref:`SPARQL source <sparql_source>` has been deprecated, please use ``initial_since_value`` instead.

.. _changelog_2021_05_31:

2021-05-31
----------

* We've updated our :doc:`pricing`. For existing customers, the changes will take effect from September 1st 2021.

2021-05-20
----------

* Added a :doc:`Sesam Community <community>` section.

.. _changelog_2021_05_19:

2021-05-19
----------

* Legal documents has been reformatted and are now available under :doc:`legal`.

.. _changelog_2021_05_06:

2021-05-06
----------

* If pipes with sources with the :ref:`chronological strategy <strategy>` fail, they now save their pipe offset based on last successful batch in the pipe run. This improvement makes it more likely that a failing pipe is able to make progress.

.. _changelog_2021_05_05:

2021-05-05
----------

* Added ``rate_limiting_retries`` and ``rate_limiting_delay`` properties to the :ref:`REST source <rest_source>`, :ref:`REST transform <REST_transform>`, :ref:`REST sink <REST_sink>` and :ref:`REST system <rest_system>`. These can be used to retry failed requests that return a HTTP 429 error code.

.. _changelog_2021_05_03:

2021-05-03
----------

* The ``payload_property`` of the :ref:`REST source <rest_source>` and :ref:`REST transform <REST_transform>` now supports traversing a path in the response body using a "dotted" notation.

.. _changelog_2021_04_29:

2021-04-29
----------

* Added a configuration hint for controlling the deployment of microservices. The new :ref:`eager_load_microservices <service_metadata_global_defaults_eager_load_microservices>` option will allow Sesam to hold off starting up microservices which are not connected to any pipes. This option is ``true`` by default, in line with previous behaviour. The option can be overriden per system using the ``eager_load`` flag in the :ref:`Microservice system configuration <microservice_system>`. Individual microservices which need to be run eagerly should have the option ``eager_load`` set to ``true`` explicitly in anticipation of the default changing.

.. _changelog_2021_04_15:

2021-04-15
----------

* Added 'dialect' keyword to :ref:`Microsoft Azure SQL Data Warehouse server <mssql-azure-dw_system>` system to indicate whether it's a normal SQL server or a Synapse server. Note that it uses the 'HEAP' table type when used to create new tables.

.. _changelog_2021_03_25:

2021-03-25
----------

* The driver for the :ref:`LDAP system <ldap_system>` has been changed to version 2.4 of
  `LDAP3 <https://pypi.org/project/ldap3/>`_ . The new driver gives the same results as the old driver
  in our tests, but it is still possible that there may be some subtle changes in how the new driver
  interacts with the LDAP server. The newer version implements some security fixes.

.. _changelog_2021_03_22:

2021-03-22
----------

* The :ref:`mail message sink <mail_sink>` will now automatically add a ``Date`` header to the email message.
* Added support for specifying a list of HTTP response status codes to ignore in the :ref:`REST transform <rest_transform>`.

.. _changelog_2021_03_19:

2021-03-19
----------

* Added support for paginated responses to the :ref:`REST transform <rest_transform>` as well.
* The REST transform ``response-property``, ``replace-entity`` and  ``response-include-content-type`` properties has
  been deprecated. Use ``response_property``, ``replace_entity`` and ``response_include_content_type`` instead.

.. _changelog_2021_03_15:

2021-03-15
----------

* Added experimental :ref:`REST source <rest_source>`. This source is intended to be able to replace some of the connectors that currently require Microservices.

.. _changelog_2021_03_12:

2021-03-12
----------

* Notification status changes on `Status page <https://status.sesam.no>`_ is now fully automated.

.. _changelog_2021_03_05:

2021-03-05
----------

* Added default ``operation``, ``properties`` and ``payload`` values to the :ref:`REST sink <rest_sink>` and :ref:`REST transform <REST_transform>`

.. _changelog_2021_02_19:

2021-02-19
----------

* The driver for the :ref:`MySQL <mysql_system>` database type has been changed to the latest stable version of
  `PyMySQL <https://pypi.org/project/PyMySQL>`_ (the old driver was from 2015, and we wanted to use a more recent driver).
  The new driver gives the same results as the old driver in our tests, but it is still possible that there may be
  some subtle changes in how the new driver interacts with the MySQL database (for instance in how data is converted
  between Sesam's internal format and the fields in a database table).


.. _changelog_2021_02_18:

2021-02-18
----------

* A new property ``equality_sets`` has been added to the :ref:`merge source <merge_source>`. This property can be
  used instead of (or in combination with) the ``equality`` property, and should make it a bit easier to configure
  the equality-rules correctly.

.. _changelog_2021_02_15:

2021-02-15
----------

* Open Sesam will shut down March 31st, 2021. It unfortunately did not gain as much traction among our users as we had hoped and we are focusing more on the core product. We will notify the users by email soon.

.. _changelog_2021_02_11:

2021-02-11
----------

* The default :ref:`batch_size <pipe_batching>` value of pipes that use the :ref:`REST sink <rest_sink>` has been changed to 1 (used to be 100).

.. _changelog_2021_02_05:

2021-02-05
----------

* We are optimizing the maximum number of concurrent running pipes in small subscriptions. The rationale is to get better overall performance. Note that this also affects self-hosted subscriptions.
* Documented the  :ref:`compaction settings  <service_metadata_global_defaults_compaction_settings>` in the global defaults section of the service metadata. Note that should be careful in changing these values as this can lead to loss of data and/or influence dependency tracking functionality.

.. _changelog_2021_02_01:

2021-02-01
----------

* We automatically upgrade a *Small* subscription type to a *Medium* subscription type if the data storage usage exceeds 40 Gb. We also upgrade a *Medium* subscription type to *Large* subscription type if the data storage usage exceeds 350 Gb. Note that this also affects self-hosted subscriptions.

.. _changelog_2021_01_11:

2021-01-11
----------

* Added experimental support for running a :ref:`pipe rescan <pipe_rescans>` in the background while simultaneously doing normal incremental pipe-runs.

.. _changelog_2021_01_04:

2021-01-04
----------

* Added experimental ``skip_identity_columns`` property to the :ref:`SQL sink <sql_sink>`.

.. _changelog_2020_12_01:

2020-12-01
----------

* Changed the receive endpoint for log shipping. See :doc:`Self-hosted service <self-hosted>`.

.. _changelog_2020_11_20:

2020-11-20
----------

* New circuit breaker feature for uploading configuration available in :ref:`service metadata <service_metadata_section>`. Prevents the node from updating it's configuration if the new configuration would result in the deletion of more than 10 and more than 10% of existing components (for example when using the ``/config`` API). The circuit breaker can be activated by setting the service metadata property ``global_defaults.use_config_circuit_breaker`` to ``true``.

.. _changelog_2020_11_16:

2020-11-18
----------

* The ``blacklist`` and ``whitelist`` properties of the :ref:`SQL sink <sql_sink>` has been deprecated. You can use DTL to filter properties to achieve the same functionality.
* Note that these deprecated properties cannot be used to avoid inserting values into or overwriting values of existing table columns (partial table updates) or to support identity columns.
* For the special case of identity columns (columns with automatically assigned values) some RDBMS systems such as MS SQL Server allow you to define a "writable view" that can be used as a workaround for this. We have added some  :ref:`information <mssql-identity-columns>` to the documentation on this usecase for MS SQL Server.

.. _changelog_2020_11_13:

2020-11-13
----------

* :ref:`In the pump configuration section <pump_section>` the ``use_dead_letter_dataset`` property has been deprecated and the ``dead_letter_dataset`` property has been un-deprecated. Please update your configuration. The ``dead_letters_dataset`` should contain a per-pipe unique user dataset id. The motivation for this reversal is that we wish to migrate away from using system datasets for any "dead letters" in a pipe.

.. _changelog_2020_11_06:

2020-11-06
----------

* Added :ref:`note <pipe_compaction>` about compaction not being performed beyond depencency tracking offsets.

.. _changelog_2020_10_23:

2020-10-23
----------
* Documented the :ref:`REST transform <REST_transform>`.

.. _changelog_2020_10_09:

2020-10-09
----------
* Fixed a bug in datetime-shift and other functions that does implicit or explicit timezone-conversion where we didn't have the correct historic daylight saving information. This affects the following ranges: 1895-1901, 1916, 1940-1945, 1959-1965 and any year after 2038.

.. _changelog_2020_08_24:

2020-08-24
----------
* Changed default compaction type to ``sink``. To go back to the previous default, you can set sink compaction to ``false`` on individual pipes or set the global default property ``default_compaction_type`` to ``background`` in the :ref:`service metadata <service_metadata_section>`.

.. _changelog_2020_08_21:

2020-08-21
----------
* Added an optional ``description`` property to pipes and systems - it can be either a string or a list of strings.
* Added an optional ``comment`` property to pipes, systems, sources, sinks, pumps and transforms - - it can be either a string or a list of strings.

.. _changelog_2020_08_17:

2020-08-17
----------
* The :ref:`dataset sink <dataset_sink>` property ``set_initial_offset`` now accepts the ``onload`` enum value. This enum value sets the sink dataset's initial offset when the pipe is loaded / configured.

2020-08-13
----------
* The encrypt-pki, encrypt-pgp and their corresponding decrypt DTL functions now support using '$SECRET()' syntax in their key and password parameters

2020-08-04
----------
* Documented the ``instance`` property of the  :ref:`MS SQL <mssql_system>` system. Please note the the potential consequences for firewall rules when using this property.

2020-06-19
----------
* Experimental pipe entity type inferencing now enabled by default. Change default value by setting service metadata property ``global_defaults.infer_pipe_entity_types`` to ``false``.

2020-05-28
----------
* Added the :ref:`Restore completed <restore_completed_notification_rule>` and :ref:`Pump offset set <pump_offset_set_notification_rule>` notification rule types.

2020-03-27
----------
* Added the ``dependency_tracking`` property to :ref:`service metadata <service_metadata_section>`. It can be used to specify various dependency tracking related properties.

2020-03-23
----------
* Added the ``max_entity_bytes_size`` property to the :ref:`dataset sink <dataset_sink>`.
* Added the ``global_defaults.max_entity_bytes_size`` property to :ref:`service metadata <service_metadata_section>`.

2020-03-18
----------
* Added the ``global_defaults.default_compaction_type`` property to :ref:`service metadata <service_metadata_section>`.

2020-03-05
----------
* The :ref:`union_datasets <union_datasets_source>` source now as a ``prefix_ids`` property that can be set to `false` to not add the dataset id as the prefix on entity ids.

2020-03-03
----------
* The transform function :ref:`rename <dtl_transform-rename>` will now rename properties with a null value. The old behaviour ignored such properties, but that was considered to be a bug.

2020-02-12
----------
* Added support for ``create_table_if_missing`` SQL sink property for the Oracle, Oracle TNS and MySQL systems. Previously only the MS SQL and PostgreSQL systems supported this option.

2020-02-06
----------
* Added support for optional string cast value(s) as argument to the :ref:`uuid <uuid_dtl_function>` DTL function

2020-01-08
----------
* The default value of the ``read_timeout`` property has been changed from 7200 seconds to 1800 seconds for the
  :ref:`URL system <url_system>` and the :ref:`Microservice system <microservice_system>`.

2019-12-23
----------
* Added the :ref:`fail! <fail_dtl_function>` DTL function.

2019-12-19
----------
* The :ref:`replace <replace_dtl_function>` DTL function now takes a dict argument that lets one specify more than one string replacement.

2019-12-18
----------
* Updated the documentation for the ``supports_signalling`` property on dataset sources and the ``global_defaults.use_signalling_internally`` property of the :ref:`service metadata <service_metadata_section>` section.
* The :ref:`The JSON push sink <json_sink>` and :ref:`REST sink <rest_sink>` no longer includes header values or entity data in the traceback details of the execution log on failures.
* The execution log and dead letter entities no longer includes copies of the ``source`` or ``sink`` configuration properties of the pipe.
* The properties of the event entities in the execution log are now truncated at 10 mb to avoid excessive event entity sizes. Note that this cut-off value might be decreased further in the future.
* If the pump fails due to exceeding retry limits, the entity in question is no longer included in the traceback properties. Instead it's put in a separate ``exception_entity`` property. Note that this property is not included in the monitoring data, so you cannot devise notification rules that refer to it.

2019-12-17
----------
* Added support for :ref:`Config groups <api-config-groups>`.

2019-11-25
----------
* The :ref:`RDF source <rdf_source>` will no longer add the ``<rdflibtoplevelelement>`` root wrapper element to literals with datatype ``http://www.w3.org/1999/02/22-rdf-syntax-ns#XMLLiteral``. This is a breaking change.


2019-10-28
----------
* Added the :ref:`hex <hex_dtl_function>` DTL function.
* Updated the :ref:`integer <integer_dtl_function>` DTL function to parse hexadecimal values.
* The :ref:`dataset sink <dataset_sink>` now has a property called ``prevent_multiple_versions`` that makes the pipe fail if an entity already exists in the sink dataset. This is useful if one wants to prevent multiple versions of the same entity to be written.
* The :ref:`dataset sink <dataset_sink>` now has a property called ``suppress_filtered``. The default value is ``false`` unless it is a full sync and the source is of type ``dataset`` and ``include_previous_versions`` is ``false``. The purpose of this property is to make it possible to opt-in or opt-out of a specific optimization in the pipe. The optimization is to suppress entities that are filtered out in a transform early so that they are not passed to the sink. This optimization should only be used when the pipe produces exactly one version per ``_id`` in the output. The optimization is useful when the pipe filters out a lot of entities.

2019-10-07
----------
* :ref:`Sink compaction <pipe_compaction>`, :ref:`merge source <merge_source>`, :ref:`LDAP source <ldap_source>`, :ref:`Email message sink <mail_sink>`, :ref:`SMTP system <smtp_system>`, :ref:`SMS message sink <sms_sink>`, :ref:`Twilio system <twilio_system>`, :ref:`REST system <rest_system>`, and :ref:`REST sink <rest_sink>` are no longer experimental.
* The :ref:`reference <reference_dtl_function>` DTL function has been deprecated.
* The :ref:`Kafka system <kafka_system>`, :ref:`Kafka source <kafka_source>` and :ref:`Kafka sink <kafka_sink>` have been deprecated.

2019-09-04
----------
* Index version 2 is now the default version for dataset indexes. This index implementation (version 2) supports bidirectional traversal and that can be used to expose incremental feeds for one or more subsets of a dataset.

2019-09-04
----------
* Added new :ref:`Pump finished overdue <pump_finished_overdue_notification_rule>` notification rule type.
* Added new :ref:`Pump failed <pump_failed_notification_rule>` notification rule type.


2019-08-27
----------
* DTL :ref:`property path strings <path_expressions_and_hops>` can now be quoted. In practice this means that you can have periods in path elements if you quote them. Example: ``"_S.foo.'john.doe''s'.bar"`` is now equivalent to ``["path", ["list", "foo", "john.doe's", "bar"], , "_S."]``. A quoted path element must begin and end with a single quote. Single quotes can be escaped with ``''``.
* Extended the :doc:`JSON Pull Protocol <json-pull>` document with information about response headers and an example using dataset subsets.

2019-08-26
----------
* We've added support for a feature called :ref:`completeness <completeness>`. When a pipe completes a successful run the sink dataset will inherit the smallest completeness timestamp value of the source datasets and the related datasets. Inbound pipes will use the current time as the completeness timestamp value. This mechanism has been introduced so that a pipe can hold off processing source entities that are more recent than the source dataset's completeness timestamp value. The propagation of these timestamp values is done automatically. Individual datasets can be excluded from completeness timestamp calculation via the ``exclude_completeness`` property on the pipe. One can enable the completeness filtering feature on a pipe by setting the ``completeness`` property on the :ref:`dataset source <dataset_source>` to ``true``.

2019-08-19
----------
* :ref:`Pipes <automatic_reprocessing>` now have a property called ``reprocessing_policy`` that can be set to cause automatic resets when external factors indicate that the pipe should be reset.

2019-08-12
----------
* The :ref:`dataset sink <dataset_sink>` now has a property called ``set_initial_offset`` that specifies how the sink should set the initial offset on the sink dataset (a.k.a. the populated flag).

2019-05-31
----------
* Added experimental support for automatic scheduling of internal (dataset to dataset) pipes and JSON pipes that read from external Sesam datasets via the REST API. See the ``supports_signalling`` property of these sources and the global ``use_signalling_internally`` and ``use_signalling_externally`` options in service metadata section. Please note the limitations and usage notes.

2019-04-23
----------
* The :ref:`embedded <embedded_source>` source now has configurable continuation properties, i.e. ``supports_since``, ``is_chronological`` and ``is_since_comparable``.

2019-04-01
----------
* The :ref:`"dtl" transform <dtl_transform>` will now fail if the target entity's ``_id`` property is either missing or is not a string. It will also do so if the arguments to :ref:`"create" <dtl_transform-create>` and  :ref:`"create-child" <dtl_transform-create-child>` is not a dict or is missing the ``_id`` property or the ``_id`` property is of a non-string type. This is a change in default behaviour, but it is possible to opt-out of this new behaviour by setting the ``id_required`` property to ``false``. It would make it easier to discover logic errors.

2019-03-26
----------
* The ``track_children`` property on the :ref:`dataset sink <dataset_sink>` is now inferred to be ``true`` if any of the pipe's transforms use the ``create-child`` DTL function. It is possible to override this by setting the property's value to ``false``.

2019-03-22
----------
* The :ref:`lookup <lookup_dtl_function>` DTL function has been deprecated and replaced with the :ref:`lookup-entity <lookup_entity_dtl_function>` function. Note that the dataset referenced in its first argument must be populated before the parent pipe will run.

2019-03-14
----------
* The valid characters in pipe and system ids have been restricted to be valid DNS name components. In practice this means that the first character must be a letter or a digit and the rest must be letters, digits and hyphens. The maximum length is 62. Invalid ids will trigger a validation warning.

2019-03-13
----------
* A source that has ``supports_since=true``, ``is_since_comparable=false`` and ``is_chronological=True`` will now use the *chronological* :ref:`continuation strategy <continuation_support>`. Earlier it used no continutation strategy.

2019-02-27
----------
* Added the :ref:`discard <dtl_transform-discard>` DTL transform which can be used to discard the target entity. It is similar to :ref:`filter <dtl_transform-filter>`, but will drop the target entity on the floor and not send it to the sink for deletion.
* Added the :ref:`case <dtl_transform-case>` and :ref:`case-eq <dtl_transform-case-eq>` DTL transforms. These are the sisters of the identically named DTL functions.

2019-02-15
----------
* Made the :ref:`URL system <url_system>` throw an error if it received an invalid 'Content-Length' response header value.
  The URL system used to ignore such errors; the new ``ignore_invalid_content_length_response_header``
  property can be set to get the old behaviour.

2019-02-14
----------
* Added the :ref:`docker.hosts <microservices_system_docker_hosts>` property to the :ref:`microservice system <microservice_system>`. This allow adding custom hostname to IP address mappings to the microservice container.

2019-02-13
----------
* Added a new `coerce_to_decimal` property to the :ref:`Oracle <oracle_system>` and :ref:`Oracle TNS <oracle_tns_system>` systems. If set to `true`, it will force the use of the decimal type for all "numeric" types (i.e. numbers with precision and scale information). Currently what type the column data ends up as is not clearly defined by the oracle backend driver so in some cases it may yield a float value instead of a decimal value. This property should always be set to `true` if your flows care if numeric values are floats or decimals. The default value is `false`.

2019-02-07
----------
* We've changed the default strategy for pipe execution logging. By default, we now will never log any runs which resulted in no processed/changed entities. You can opt-in to the previous behaviour by editing the ``log_events_noop_runs``, ``log_events_noop_runs_changes_only`` and ``notification_granularity`` :ref:`pump properties <pump_section>`.

2019-02-04
----------
* There is now a new index implementation (version 2) that supports bidirectional traversal and that can be used to expose incremental feeds for one or more subsets of a dataset. Index version 1 is currently the default. Nodes must be started with a special command line option in order to change the default value. Version 2 will be made the default at some point once we have enough experience with it.
* The :ref:`dataset <dataset_source>` and :ref:`json <json_source>` sources now support the ``subset`` property. This property is used to specify a subset of the source dataset.
* The :ref:`hops <hops_dtl_function>` and :ref:`apply-hops <apply_hops_dtl_function>` DTL functions now support the ``prefilters`` property. This property is used to specify a subset of the dataset that it is hopped to.
* The ``GET /api/datasets/{dataset_id}/indexes`` API endpoint now includes the indexes' version number.
* The ``DELETE /datasets/{dataset_id}/indexes/{index_int_id}`` API endpoint has been added. It can be used to delete a dataset index.

2019-01-28
----------
* :ref:`Compaction <pipe_compaction>` is now incremental, so it will continue from where it got to the last time.
* Compaction will be performed by the dataset sink if ``compaction.sink`` is set to ``true`` in the pipe configuration. This is only available for pipes using the :ref:`dataset <dataset_sink>` sink. If sink compaction is enabled no scheduled compaction will be done on the dataset as this is no longer neccessary. Index compaction will still require scheduled compaction, but this does not require a lock on the dataset. Note that sink compaction is currently experimental.
* Automatic compaction will now kick if there are 10% or 10000 new dataset offsets since the last compaction. The 10000 cap is fixed for now.

2019-01-03
----------
* The :ref:`dataset <dataset_sink>` sink will now mark the sink dataset as populated when all input datasets are populated and all entities have been read from them. Earlier it marked the sink dataset as populated after the first completed run. This was typically not what you wanted as it caused the sink datasets to be prematurely populated, which then caused unnecessary dependency tracking.
* Added the ``initial_datasets`` property to the :ref:`merge <merge_source>`,  :ref:`merge_datasets <merge_datasets_source>`,  :ref:`union_datasets <union_datasets_source>`, and  :ref:`diff_datasets <diff_datasets_source>` sources. This property should only be used if some of the input datasets will never be populated. The property should then list the datasets that have to be populated before the sink datasets should be populated.

2018-12-07
----------
* Casting decimal numbers containing a "scientific notation" shorthand (i.e. "1E-3", "10E14" etc) to a string using the :ref:`DTL string <string_dtl_function>` function will now expand the exponent to its full representation (i.e. "1E2" -> "100", "1E-3" -> "0.001"). This is a change in behaviour.

2018-12-03
----------
* Added support for specifying SOCKS5 proxies for the :ref:`URL <url_system>`, :ref:`REST <rest_system>` and :ref:`Twilio <twilio_system>` systems.

2018-11-12
----------
* ``["matches", "x*", ["list"]]`` now returns ``false`` instead of ``true``. Note that this is a breaking change, but the old behaviour was considered a bug as it is both non-intuitive and most likely not what you want.

2018-10-31
----------
* Added the ``sslmode`` property to the :ref:`PostgreSQL system <postgresql_system>`. Its default value (``prefer``) reflects the PostgreSQL client library default, hence you should only set this property if you need other behaviour than the default.

2018-10-25
----------
* Added the :ref:`Kafka system <kafka_system>`, :ref:`Kafka source <kafka_source>` and :ref:`Kafka sink <kafka_sink>`.

2018-10-16
----------
* Added ``compaction.growth_threshold`` property to the :ref:`pipe configuration <pipe_compaction>`. This lets you specify when dataset compaction kicks in.
* The ``compaction.keep_versions`` property can now also be set to ``0`` and ``1``. The default value is ``2``; which is needed for dependency tracking to be fully able to find reprocessable entities. Setting it to a lower value means that dependency tracking is best effort only.

2018-09-24
----------
* Added a new ``recreate_table_on_first_run`` boolean flag to the :ref:`sql sink <sql_sink>` - it controls if Sesam should recreate the table from ``schema_definiton`` when the pipe is reset or runs for the first time. Note that this requires the ``create_table_if_missing`` property to also be set to ``true`` to take effect.
* Altered the way the PK is created on schema definition generation. If the sink type is ``sql`` and ``create_table_if_missing`` is set to ``true``, the default primary key is the ``_id`` property of the entities. Previously it would always look for a property with the same contents as ``_id`` (which is still the default for non-sql sink pipes).

2018-09-03
----------
* Added a ``fallback_to_single_entities_on_batch_fail`` boolean flag to the :ref:`pump configuration <pump_section>`. The default reflects the current behaviour (``true``). It can be usefuly to set to ``false`` if the cost of processing a single entity at a time is high and there is a lot of entities in a batch (for example in a typical MS SQL sink in initial bulk upload mode).

2018-08-24
----------
* Datasets that are not populated will no longer be compacted.

2018-08-10
----------
* Receiver and publisher pipes can now be disabled.

2018-08-02
----------
* Added support in the :ref:`split <split_dtl_function>` DTL function to split string into characters using the empty separator.

2018-07-04
----------
* Added a :ref:`translation GUI<gdpr_custom_text_and_translation>` for the GDPR platform. This GUI makes is much easier to customize the various texts used by the GDPR portal.

2018-06-26
----------
* Added the the :ref:`case-eq <case_eq_dtl_function>` and :ref:`case <case_dtl_function>` DTL functions. These can be used to express more complex conditional expressions. Earlier one had to nest ``if`` functions to achieve the same thing.

2018-06-25
----------
* Changed the :ref:`base64-encode <base64_encode_dtl_function>` and :ref:`base64-decode <base64_decode_dtl_function>` DTL functions to only accept bytes and string input respectively.
* Added support for bytes input to the :ref:`string <string_dtl_function>` casting function. The encoding used is ``utf-8``.
* Added a :ref:`bytes <bytes_dtl_function>` casting function that casts strings to (``utf-8`` encoded) bytes representation.

2018-06-19
----------
* Added a :ref:`RDF transform <rdf_transform>`, similar to the XML transform. It will render entities to a NTriples string and embed it in the transformed entity.
* Added the :ref:`base64-encode <base64_encode_dtl_function>` and :ref:`base64-decode <base64_decode_dtl_function>` DTL functions.

2018-06-07
----------
* Added support for having :ref:`secrets <secrets_manager>` that apply only to one specific System.

2018-06-06
----------
* Changed default behaviour of the :ref:`CSV source <csv_source>`: if ``dialect`` is set, this will override the default value of ``auto_dialect``. Previously you would have to both turn off ``auto_dialect`` and set ``dialect``. Note that if ``auto_dialect`` is ``false`` and no ``dialect`` has been set, the ``excel`` dialect is used as default.
* The :ref:`is_chronological <sql_source>` property on the :ref:`SQL source <sql_source>` is now dynamic as it is ``true`` if the ``updated_column`` and ``table`` properties are set.
* Added the :ref:`is_chronological_full <sql_source>` property to the :ref:`SQL source <sql_source>` . If explicity set to ``false`` then a full run will not consider the source to be chronological even though it is chronological in incremental runs. The default value is the value of the ``is_chronological``, but can be set to ``false``.

2018-06-05
----------
* The old ``dead_letter_dataset`` :ref:`pump configuration <pump_section>` option (string) has been deprecated and replaced by ``use_dead_letter_dataset``, which is a boolean flag (false by default). If set to true, the id of the dead letter dataset is automatically generated and linked to the parent pipe id (``system:dead-letter:pipe-id``). Note that entities written to this new dataset will no longer have the pipe id as part of their ``_id`` property. This new dataset will inherit the ACLs from its parent pipe (like pump execution datasets). If the pipe is removed, the automatically created dataset is also removed. The old ``dead_letter_dataset`` property will continue to work as before but will be removed at some future date.

2018-05-29
----------
* Added the :ref:`checkpoint_interval <pipe_batching>` property to the pipe. The default has been changed from ``1`` to ``100``, which means that the pipe offset is now saved after every 100 batches instead of after every batch. The default is effectively every 10000 entities, but since it is dependent on ``batch_size`` the default value is ``100`` (i.e. 10000/``batch_size``). Note that the pipe offset is always saved at the end of every sync if it changed.
* Pipes that perform deletion tracking will now have their pipe offset and deletion tracking state saved every 15 minutes or so. If a pipe is interrupted it will now be able to continue doing deletion tracking from where it last saved it's state.

2018-05-02
----------
* Added the :ref:`ljust <ljust_dtl_function>` and :ref:`rjust <rjust_dtl_function>` DTL functions. They can be used to left-justify and right-justify strings.

2018-04-30
----------
* A partial rescan can now be scheduled :ref:`on a pump <pump_section>` by specifying the two properties ``partial_rescan_count`` and ``partial_rescan_delta``.

2018-04-27
----------
* Added the :ref:`hash128 <hash128_dtl_function>` DTL function. It generates 128 bit integer hashes from bytes and strings.

2018-04-26
----------
* The sink dataset and the dead-letter dataset will now be asserted when the pipe is loaded. Receiver datasets, i.e. sink datasets that are used in combination with the ``http_endpoint`` source, will be automatically populated at the same time. Note that it is possible to opt-out of this behaviour by setting ``auto_populate_dataset`` to ``false`` on the :ref:`http_endpoint <http_endpoint_source>` source. Dead-letter datasets are automatically populated, and it is not possible to opt-out.

  Note that this is a change in behaviour, but in most situations it is the right thing to do. If the initial push to the receiver is a full sync, then it might be good to set ``auto_populate_dataset`` to ``false``. The reason why this is useful for full syncs is because pipes doing hops against the dataset will then wait until the sync is complete and the dataset is populated.

2018-04-23
----------
* Processing of namespaced identifiers have gotten a decent performance boost.
* Regression: The ``make-ni`` DTL function will now return a sorted list of NIs. Earlier the sorting was done by sorting the keys of the source entity, which is a much expensive thing to do.

2018-04-19
----------
* Added support for :ref:`circuit breakers <circuit_breakers_section>`, a safety mechanism that one can enable on the :ref:`dataset sink <dataset_sink>`. The circuit breaker will trip if the number of entities written to a dataset in a pipe run exceeds a certain configurable limit.

2018-04-09
----------
* Added the :ref:`round <round_dtl_function>` DTL function. It rounds to the nearest digit using the "round half to even" rule.

2018-03-20
----------
* Added oauth2 (BackendServerClient profile, aka "client credentials") option to the URL system

2018-03-07
----------
* Changed the default value of the node configuration setting "pipe_cleanup_after_deletion" to "true". This means the node will remove any pipe-related data when a pipe is deleted (execution logs, acls, pipe offsets etc)

2018-03-05
----------
* Added the :ref:`map-values <map_values_dtl_function>` function. It maps over the values of dictionaries and returns a list of mapped values.

2018-02-27
----------
* The :ref:`combine <combine_dtl_function>` DTL function now allows a single argument. This is useful when you want to turn an expression into a list of values. It is extra useful when you don't quite know if the value is a list or not. Example: ``["combine", "_S.x"]``


2018-01-22
----------
* Added a ``content_disposition`` configuration property to be able to specify the type in the ``Content-Dispositon`` HTTP response header to the :ref:`HTTP endpoint sinks <http_endpoint_sink>`.
* Added the possibility to specify the ``filename`` of the :ref:`HTTP endpoint sinks <http_endpoint_sink>` as the last element of the URL (overrides any ``filename`` set in the configuration of the sink).

2018-01-16
----------
* Added the :ref:`url-unquote <url_unquote_dtl_function>` function that URL unquotes any URL quoted characters in its input. See the related :ref:`url-quote <url_quote_dtl_function>` function.

2018-01-15
----------
* The :ref:`RDF source  <rdf_source>` and :ref:`SDShare source  <sdshare_source>` now supports the ``sort_lists`` property to automatically sort resulting properties containing lists (i.e. RDF statements having the same predicate). It is ``true`` by default.

2017-12-15
----------
* The :ref:`JSON source  <json_source>` now supports the ``page_size`` property.

2017-12-14
----------
* Added ``encrypt-pgp`` and ``decrypt-pgp`` DTL functions that can encrypt strings to OpenPGP messages using a PGP
  public key and decrypt these messages back to strings using a PGP private key and its associated password.

2017-12-12
----------
* Added ``encrypt-pki`` and ``decrypt-pki`` DTL functions that can asymmetrically encrypt strings to bytes and decrypt
  bytes to strings using a PKI public/private key-pair in DEM format (PKCSv8). The encryption is performed using RSA
  2048 bits with sha-1 hashes and OAEP/MGF1 padding.

2017-11-23
----------
* Added :ref:`Databrowser documentation <databrowser>`.


2017-11-22
----------
* Added the :ref:`Pattern match <pump_completed_pattern_match_notification_rule>` notification rule type.


2017-11-15
----------
* Added the :ref:`intersects <intersects_dtl_function>` DTL function. This boolean function returns true if there is an overlap between the values in the two arguments.

* The DTL compiler will now issue a warning if you try to perform two
  or more :ref:`join expressions <joins>` between the same two dataset
  aliases. It is there to notify you of possible cardinality issues
  and to tell you about the :ref:`tuples <tuples_dtl_function>`
  function, which may be used to avoid cardinality issues.

  When there are two or more join expressions between the same two
  dataset aliases only the first one is treated as a join expression;
  the rest of them are :ref:`equality comparisions
  <eq_dtl_function>`. One can use the :ref:`tuples
  <tuples_dtl_function>` function to combine them into one big join
  expression at the cost of composite indexes being used.

  .. WARNING::

     Note that the :ref:`eq <eq_dtl_function>`
     function serves a dual purpose. It can both be used for
     :ref:`join expressions <joins>` and it can be used for
     :ref:`equality comparisions <eq_dtl_function>`. These two are
     different in that a join uses intersection (similar to the
     ``intersects`` function) and the equality comparison is an exact
     match. Use the :ref:`intersects <intersects_dtl_function>`
     function if you want to check for intersection/overlap instead of
     an exact match.


2017-11-13
----------
* The default value of the ``keep_existing_solr_ids`` configuration property in the :ref:`The Sesam Databrowser sink <databrowser_sink>`
  has been changed from ``true`` to ``false``.

2017-11-08
----------
* The :ref:`JSON push sink  <json_sink>` now supports customizable HTTP headers via a ``headers`` property.

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
* It is now possible to specify ``track-dependencies`` on all the HOPS_SPEC in a specific :ref:`hops <hops_dtl_function>` DTL function. This change was made so that one can disable tracking for any of the HOP_SPECs, not just the last one.

2017-08-16
----------
* The :ref:`json-parse <json_parse_dtl_function>` and :ref:`json-transit-parse <json_transit_parse_dtl_function>` DTL functions now accept an optional default value expression. The default value expression is used when the input value is not valid JSON.

2017-08-08
----------
* The :ref:`datetime-parse <datetime_parse_dtl_function>` and :ref:`datetime-format <datetime_format_dtl_function>` DTL functions now accept an optional timezone argument. This makes it possible to parse datetime strings and format datetime values in specific timezones.

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
* The default value of the ``max_depth`` property in :ref:`hops <hops_dtl_function>` has been changed from ``null`` to ``10``. This means that the default is to stop the recursion at level 10.

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
* Extended all :ref:`systems <system_section>` to accept a new property ``worker_threads`` that limits the number of concurrent pipes that can run against a particular system. The default value is 10. For inbound pipes the source system is used and for outbound pipes the sink system is used. For internal pipes, the the pool has 50 worker threads (i.e. for dataset to dataset pipes or receiver/publisher endpoints).

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
* Added ``text_body_template`` and ``text_body_template_property`` properties to the :ref:`Email message sink <mail_sink>`. Use these to explicitly construct a plain-text version of your messages if sending multi-part messages.

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
*  Added an ``unhandled_template_variable_replacement`` property to the :ref:`Email Message sink <mail_sink>`.

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
* Added the :ref:`datetime-shift <datetime_shift_dtl_function>` DTL function.
* Added support for timezones to the :ref:`datetime-parse <datetime_parse_dtl_function>` DTL function.
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
