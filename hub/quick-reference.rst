.. _quick_reference:

================
 Quick Reference
================

Configuration
=============

.. list-table::
   :widths: 30, 70

   * - Sources
     - :ref:`conditional <conditional_source>` ·
       :ref:`csv <csv_source>` ·
       :ref:`dataset <dataset_source>` ·
       :ref:`diff_datasets <diff_datasets_source>` ·
       :ref:`embedded <embedded_source>` ·
       :ref:`empty <empty_source>` ·
       :ref:`http_endpoint <http_endpoint_source>` ·
       :ref:`json <json_source>` ·
       :ref:`ldap <ldap_source>` ·
       :ref:`merge <merge_source>` ·
       :ref:`merge_datasets <merge_datasets_source>` ·
       :ref:`rdf <rdf_source>` ·
       :ref:`rest <rest_source>` ·
       :ref:`sdshare <sdshare_source>` ·
       :ref:`sparql <sparql_source>` ·
       :ref:`sql <sql_source>` ·
       :ref:`union_datasets <union_datasets_source>`

   * - Sinks
     - :ref:`conditional <conditional_sink>` ·
       :ref:`csv_endpoint <csv_endpoint_sink>` ·
       :ref:`dataset <dataset_sink>` ·
       :ref:`elasticsearch <elasticsearch_sink>` ·
       :ref:`http_endpoint <http_endpoint_sink>` ·
       :ref:`json <json_sink>` ·
       :ref:`mail <mail_sink>` ·
       :ref:`null <null_sink>` ·
       :ref:`rest <rest_sink>` ·
       :ref:`sdshare <sdshare_sink>` ·
       :ref:`sms <sms_sink>` ·
       :ref:`solr <solr_sink>` ·
       :ref:`sparql <sparql_sink>` ·
       :ref:`sql <sql_sink>` ·
       :ref:`xml_endpoint <xml_endpoint_sink>`

   * - Systems
     - :ref:`elasticsearch <elasticsearch_system>` ·
       :ref:`ldap <ldap_system>` ·
       :ref:`microservice <microservice_system>` ·
       :ref:`mssql <mssql_system>` ·
       :ref:`mssql-azure-dw <mssql-azure-dw_system>` ·
       :ref:`mysql <mysql_system>` ·
       :ref:`oracle <oracle_system>` ·
       :ref:`oracle_tns <oracle_tns_system>` ·
       :ref:`postgresql <postgresql_system>` ·
       :ref:`rest <rest_system>` ·
       :ref:`smtp <smtp_system>` ·
       :ref:`solr <solr_system>` ·
       :ref:`twilio <twilio_system>` ·
       :ref:`url <url_system>`

   * - Transforms
     - :ref:`conditional <conditional_transform>` ·
       :ref:`dtl <dtl_transform>` ·
       :ref:`emit_children <emit_children_transform>` ·
       :ref:`http <http_transform>` ·
       :ref:`json_schema <json_schema_transform>` ·
       :ref:`rdf <rdf_transform>` ·
       :ref:`rest <rest_transform>` ·
       :ref:`xml <xml_transform>`

.. _quickref_dtl_transform_functions:

DTL Transform Functions
=======================

.. list-table::
   :widths: 30, 70

   * - Comments
     - :ref:`comment <dtl_transform-comment>`

   * - Conditionals
     - :ref:`case <dtl_transform-case>` ·
       :ref:`case-eq <dtl_transform-case-eq>` ·
       :ref:`if <dtl_transform-if>`

   * - Creation
     - :ref:`create <dtl_transform-create>` ·
       :ref:`create-child <dtl_transform-create-child>`

   * - Filters
     - :ref:`discard <dtl_transform-discard>` ·
       :ref:`filter <dtl_transform-filter>`

   * - Side-effects
     -
       :ref:`add <dtl_transform-add>` ·
       :ref:`copy <dtl_transform-copy>` ·
       :ref:`default <dtl_transform-default>` ·
       :ref:`make-ni <dtl_transform-make-ni>` ·
       :ref:`merge <dtl_transform-merge>` ·
       :ref:`merge-union <dtl_transform-merge-union>` ·
       :ref:`remove <dtl_transform-remove>` ·
       :ref:`rename <dtl_transform-rename>`

.. _quickref_dtl_expression_functions:

DTL Expression Functions
========================

.. list-table::
   :widths: 30, 70

   * - Boolean logic
     - :ref:`all <all_dtl_function>` ·
       :ref:`and <and_dtl_function>` ·
       :ref:`any <any_dtl_function>` ·
       :ref:`or <or_dtl_function>` ·
       :ref:`not <not_dtl_function>`

   * - Booleans
     - :ref:`boolean <boolean_dtl_function>` ·
       :ref:`is-boolean <is_boolean_dtl_function>`

   * - Bytes
     - :ref:`base64-decode <base64_decode_dtl_function>` ·
       :ref:`base64-encode <base64_encode_dtl_function>` ·
       :ref:`bytes <bytes_dtl_function>` ·
       :ref:`is-bytes <is_bytes_dtl_function>`

   * - Comparisons
     - :ref:`eq <eq_dtl_function>` ·
       :ref:`gt <gt_dtl_function>` ·
       :ref:`gte <gte_dtl_function>` ·
       :ref:`lt <lt_dtl_function>` ·
       :ref:`lte <lte_dtl_function>` ·
       :ref:`neq <neq_dtl_function>`

   * - Conditionals
     - :ref:`case <case_dtl_function>` ·
       :ref:`case-eq <case_eq_dtl_function>` ·
       :ref:`if <if_dtl_function>`

   * - Date and time
     - :ref:`datetime <datetime_dtl_function>` ·
       :ref:`datetime-diff <datetime_diff_dtl_function>` ·
       :ref:`datetime-format <datetime_format_dtl_function>` ·
       :ref:`datetime-parse <datetime_parse_dtl_function>` ·
       :ref:`datetime-plus <datetime_plus_dtl_function>` ·
       :ref:`datetime-shift <datetime_shift_dtl_function>` ·
       :ref:`is-datetime <is_datetime_dtl_function>` ·
       :ref:`now <now_dtl_function>`

   * - Dictionaries
     - :ref:`dict <dict_dtl_function>` ·
       :ref:`is-dict <is_dict_dtl_function>` ·
       :ref:`items <items_dtl_function>` ·
       :ref:`key-values <key_values_dtl_function>` ·
       :ref:`keys <keys_dtl_function>` ·
       :ref:`values <values_dtl_function>` ·
       :ref:`path <path_dtl_function>` ·
       :ref:`apply <apply_dtl_function>` ·
       :ref:`apply-hops <apply_hops_dtl_function>` ·
       :ref:`apply-ns <apply_ns_dtl_function>`

   * - Encryption
     - :ref:`decrypt <decrypt_dtl_function>` ·
       :ref:`decrypt-pgp <decrypt_pgp_dtl_function>` ·
       :ref:`decrypt-pki <decrypt_pki_dtl_function>` ·
       :ref:`encrypt <encrypt_dtl_function>` ·
       :ref:`encrypt-pgp <encrypt_pgp_dtl_function>` ·
       :ref:`encrypt-pki <encrypt_pki_dtl_function>`

   * - Hops
     - :ref:`hops <hops_dtl_function>` ·
       :ref:`lookup-entity <lookup_entity_dtl_function>`

   * - JSON
     - :ref:`json <json_dtl_function>` ·
       :ref:`json-parse <json_parse_dtl_function>` ·
       :ref:`json-transit <json_transit_dtl_function>` ·
       :ref:`json-transit-parse <json_transit_parse_dtl_function>`

   * - Lists
     - :ref:`combine <combine_dtl_function>` ·
       :ref:`count <count_dtl_function>` ·
       :ref:`distinct <distinct_dtl_function>` ·
       :ref:`enumerate <enumerate_dtl_function>` ·
       :ref:`filter <filter_dtl_function>` ·
       :ref:`first <first_dtl_function>` ·
       :ref:`flatten <flatten_dtl_function>` ·
       :ref:`group-by <group_by_dtl_function>` ·
       :ref:`in <in_dtl_function>` ·
       :ref:`insert <insert_dtl_function>` ·
       :ref:`is-empty <is_empty_dtl_function>` ·
       :ref:`is-list <is_list_dtl_function>` ·
       :ref:`is-not-empty <is_not_empty_dtl_function>` ·
       :ref:`last <last_dtl_function>` ·
       :ref:`list <list_dtl_function>` ·
       :ref:`map <map_dtl_function>` ·
       :ref:`map-dict <map_dict_dtl_function>` ·
       :ref:`map-values <map_values_dtl_function>` ·
       :ref:`max <max_dtl_function>` ·
       :ref:`min <min_dtl_function>` ·
       :ref:`nth <nth_dtl_function>` ·
       :ref:`range <range_dtl_function>` ·
       :ref:`reversed <reversed_dtl_function>` ·
       :ref:`slice <slice_dtl_function>` ·
       :ref:`sorted <sorted_dtl_function>` ·
       :ref:`sorted-descending <sorted_descending_dtl_function>` ·
       :ref:`sum <sum_dtl_function>`

   * - Math
     - :ref:`- <minus_symbol_dtl_function>` ·
       :ref:`/ <divide_symbol_dtl_function>` ·
       :ref:`\* <multiply_symbol_dtl_function>` ·
       :ref:`% <mod_symbol_dtl_function>` ·
       :ref:`^ <pow_symbol_dtl_function>` ·
       :ref:`+ <plus_symbol_dtl_function>` ·
       :ref:`abs <abs_dtl_function>` ·
       :ref:`ceil <ceil_dtl_function>` ·
       :ref:`cos <cos_dtl_function>` ·
       :ref:`divide <divide_dtl_function>` ·
       :ref:`floor <floor_dtl_function>` ·
       :ref:`minus <minus_dtl_function>` ·
       :ref:`mod <mod_dtl_function>` ·
       :ref:`multiply <multiply_dtl_function>` ·
       :ref:`plus <plus_dtl_function>` ·
       :ref:`pow <pow_dtl_function>` ·
       :ref:`round <round_dtl_function>` ·
       :ref:`sin <sin_dtl_function>` ·
       :ref:`sqrt <sqrt_dtl_function>` ·
       :ref:`tan <tan_dtl_function>`

   * - Misc
     - :ref:`fail! <fail_dtl_function>` ·
       :ref:`hash128 <hash128_dtl_function>` ·
       :ref:`is-changed <is_changed_dtl_function>` ·
       :ref:`literal <literal_dtl_function>` ·
       :ref:`tuples <tuples_dtl_function>`

   * - Namespaced identifiers
     - :ref:`is-ni <is_ni_dtl_function>` ·
       :ref:`ni <ni_dtl_function>` ·
       :ref:`ni-collapse <ni_collapse_dtl_function>` ·
       :ref:`ni-expand <ni_expand_dtl_function>` ·
       :ref:`ni-id <ni_id_dtl_function>` ·
       :ref:`ni-ns <ni_ns_dtl_function>`

   * - Nulls
     - :ref:`coalesce <coalesce_dtl_function>` ·
       :ref:`if-null <if_null_dtl_function>` ·
       :ref:`is-not-null <is_not_null_dtl_function>` ·
       :ref:`is-null <is_null_dtl_function>`

   * - Numbers
     - :ref:`decimal <decimal_dtl_function>` ·
       :ref:`float <float_dtl_function>` ·
       :ref:`hex <hex_dtl_function>` ·
       :ref:`integer <integer_dtl_function>` ·
       :ref:`is-decimal <is_decimal_dtl_function>` ·
       :ref:`is-float <is_float_dtl_function>` ·
       :ref:`is-integer <is_integer_dtl_function>`

   * - Sets
     - :ref:`difference <difference_dtl_function>` ·
       :ref:`intersection <intersection_dtl_function>` ·
       :ref:`intersects <intersects_dtl_function>` ·
       :ref:`union <union_dtl_function>`

   * - Strings
     - :ref:`concat <concat_dtl_function>` ·
       :ref:`is-string <is_string_dtl_function>` ·
       :ref:`join <join_dtl_function>` ·
       :ref:`length <length_dtl_function>` ·
       :ref:`ljust <ljust_dtl_function>` ·
       :ref:`lower <lower_dtl_function>` ·
       :ref:`lstrip <lstrip_dtl_function>` ·
       :ref:`matches <matches_dtl_function>` ·
       :ref:`replace <replace_dtl_function>` ·
       :ref:`rjust <rjust_dtl_function>` ·
       :ref:`rstrip <rstrip_dtl_function>` ·
       :ref:`split <split_dtl_function>` ·
       :ref:`string <string_dtl_function>` ·
       :ref:`strip <strip_dtl_function>` ·
       :ref:`substring <substring_dtl_function>` ·
       :ref:`upper <upper_dtl_function>`

   * - URIs
     - :ref:`is-uri <is_uri_dtl_function>` ·
       :ref:`uri <uri_dtl_function>` ·
       :ref:`url-quote <url_quote_dtl_function>` ·
       :ref:`url-unquote <url_unquote_dtl_function>`

   * - UUIDs
     - :ref:`is-uuid <is_uuid_dtl_function>` ·
       :ref:`uuid <uuid_dtl_function>`

Entity model
============

.. list-table::
   :widths: 30, 70

   * - Reserved fields
     - :ref:`_id <id_field>` ·
       :ref:`_deleted <deleted_field>` ·
       :ref:`_filtered <filtered_field>` ·
       :ref:`_hash <hash_field>` ·
       :ref:`_previous <previous_field>` ·
       :ref:`_tracked <tracked_field>` ·
       :ref:`_ts <ts_field>` ·
       :ref:`_updated <updated_field>`

   * - Special fields
     - :ref:`$children <dollar_children>` ·
       :ref:`$ids <dollar_ids_field>` ·
       :ref:`$replaced <dollar_replaced>`
