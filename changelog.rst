Changelog
=========

2016-09-23
----------
* Added Elasticsearch support, which includes a :ref:`system <elasticsearch_system>` and a :ref:`sink <elasticsearch_sink>`.
* The :ref:`Solr sink <solr_sink>` now supports :ref:`batching <pipe_batching>`.
* Added the ``commit_at_end`` property to the :ref:`Solr sink <solr_sink>` and the :ref:`Sesam databrowser sink <databrowser_sink>`.
* Moved the ``commit_within`` property from the :ref:`Solr system <solr_system>` to the :ref:`Solr sink <solr_sink>` and the :ref:`Sesam databrowser sink <databrowser_sink>`. The reason is that the commit rate is really specific to how and where it is used. This change is backward compatible, as the default value is taken from the system. It is recommended to update the configuration files accordingly.
* Moved the ``prefix_includes`` and ``keep_existing_solr_ids`` properties from the :ref:`Solr system <solr_system>` to the :ref:`Sesam databrowser sink <databrowser_sink>`. The reason is that they are only relevant there. This change is backward compatible, as the default value is taken from the system.  It is recommended to update the configuration files accordingly.

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
