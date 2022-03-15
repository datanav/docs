
.. _ldap_source:

LDAP source
-----------

The LDAP source provides entities from a `LDAP catalog <https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol>`_
configured by a :ref:`LDAP system <ldap_system>`.

It supports the following properties:

Prototype
^^^^^^^^^

::

    {
        "type": "ldap",
        "system": "ldap-system-id",
        "search_base": "*",
        "search_filter": "(objectClass=organizationalPerson)",
        "attributes": "*",
        "id_attribute": "cn",
        "page_size": 500,
        "attribute_blacklist": ["a","list","of","attributes","to","exclude"]
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
     - ID of the LDAP system component to use
     -
     - Yes

   * - ``search_base``
     - String
     - The base LDAP search expression to use when looking for records
     - "*"
     -

   * - ``search_filter``
     - String
     - LDAP filter expression to apply to all records found by the ``search_base`` expression
     - "(objectClass=organizationalPerson)"
     -

   * - ``attributes``
     - String
     - A wildcard expression specifying which attributes to include in the entity.
     - "*"
     -

   * - ``id_attribute``
     - String
     - Sets which of the LDAP attributes to use for the ``_id`` property of a entity.
     - "cn"
     -

   * - ``page_size``
     - Integer
     - The default number of records to read at a time from the LDAP service.
     - 500
     -

   * - ``attribute_blacklist``
     - List
     - A list of attribute names (as strings) to exclude from the record when constructing entities.
     - []
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
     - ``false`` (Fixed)

   * - ``is_since_comparable``
     - ``true`` (Fixed)

   * - ``is_chronological``
     - ``false`` (Fixed)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "ldap",
            "system": "example_ldap",
            "search_base": "ou=Example,dc=example,dc=org"
        }
    }


