.. _gdpr_platform_developer_docs:

=====================================
GDPR platform developer documentation
=====================================

.. contents:: Table of Contents
   :depth: 2
   :local:

Overview
========

For automation of the GDPR platform, there are several APIs/integration points available:

* :ref:`GDPR subject <gdpr_subject>`
* :ref:`GDPR consent <gdpr_consent>`
* :ref:`GDPR subject consent <gdpr_subject_consent>`
* :ref:`GDPR purpose <gdpr_purpose>`
* :ref:`GDPR purpose type <gdpr_purpose_type>`
* :ref:`GDPR data type <gdpr_data_type>`
* :ref:`GDPR policy <gdpr_policy>`
* :ref:`GDPR custom translations <gdpr_custom_translations>`

These APIs are datasets with a defined data-structure that can be integrated with existing systems and associated
:ref:`input <http_endpoint_source>` and :ref:`output <http_endpoint_sink>` published endpoints for JSON input
and/or consumption. The input and output endpoints conform to the :doc:`JSON Push Protocol <json-push>`.

For unstructured data such as documents and emails the GDPR platform offers a content extraction and
indexing service coupled with a semi-automatic workflow prior to making this data available to the data subject:

* :ref:`Unstructured data integration <gdpr_unstructured_data>`

Prior to using the APIs for automation purposes, the GDPR platform must be configured for automation. This is
similar to the process described in the :ref:`GDPR data types and purposes configuration <gdpr_data_types_purposes_configuration>` document, but involves
a couple of additional columns in the data type sheet of the setup spreadsheet. The purposes sheet is unchanged.

You can download a template with these additional columns :download:`here <files/GDPR setup data automated.xlsx>`

The additional columns are ``Identifiers``, ``TypeID`` and ``Exclude``. In addition, the ``Level`` field takes on special
meaning when automating the subject data flow.

The additional data type properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30, 70

   * - Column
     - Description

   * - ``TypeID``
     - This is a unique type identifier that should match the dataset id where the data will reside in the GDPR
       platform.

   * - ``Level``
     - The "level" of the data - it can be either "Personal" or "Related", i.e. directly about the data subject or
       indirectly (for example data about the customer such as address or orders for the customer, respectively)

   * - ``Identifiers``
     - One or more (comma separated), optionally namespaced, property names that will be used to uniquely identify
       a subject for this data type (see :ref:`GDPR data type <gdpr_data_type>` and :ref:`GDPR subject <gdpr_subject>`)
       when the ``level`` property is ``Personal``. If the ``level`` property is ``Related`` it will be matched to the
       closest "parent" record with the top-most in such a chain being matched with subject record (a "Personal" level
       data type". See below for a more detailed description.

   * - ``Exclude``
     - One or more (comma separated), optionally namespaced, property names that will be used to filter out any
       matching properties from the data typed by this data type.

The ``Level`` property in automated flows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the ``Level`` property is set to ``Personal`` it means that the data type represents information directly
pertaining to a data subject for example a person, customer, employee record. In this case, the ``identifiers`` property
represents one or more properties in this record that uniquely identifies the subject (for example customer id, ssn,
mobile phone number and/or email address).

If the ``Level`` property is set to ``Related``, the contents of ``Identifiers`` should be a set of properties that will
be matched to either another ``Related`` data type or to a ``Personal`` data type. There can be multiple data types
of ``Related`` level that can be matched with each other in a "chain" where the topmost record should be matched to a
subject id property.

Example with customers, orders and order line records
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The best way to illustrate the use of these properties is with an example. In this simplified imagined usecase, we have set up
pipes to get data about customers, their orders and the order lines of these orders into datasets named ``customers``
``orders`` and ``order-lines`` respectively. The customer records contain two properties ``customer_id`` and ``email_address``
that can be used to identify a customer (in addition to metadata about the customer). In addition to properties about the order,
the ``orders`` records contain a reference to the customer in the ``customer_id`` property, and a unique ``order_id`` property.
Finally, ``order-lines`` records reference the order they belong to in a ``order_id`` property (in addition to information
about the particular item in the order).

To automate this flow, we first need to configure the GDPR platform for these data types by creating three new rows in the
"data type" sheet; one row for "customer", "order" and "order-line". We also need to add at least one "Purpose" in the
"purpose sheet" to explain why we have this data and link the data types to their purpose.

The "customer" row should have the level ``Personal`` and the ``Identifiers`` column should contain ``email_address`` (or
``customer_id``). We set the "TypeID" column to match the dataset the data resides (here ``customers``).

The "order" row will then have the type ``Related`` and the ``Identifiers`` column should contain the value ``customer_id``.
We set the "TypeID" column to match the dataset the data resides (``orders``).

Finally, the "order-line" row also have level set to "Related" and the ``Identifiers`` column set to ``order_id``.
We set its "TypeID" column to match the dataset the data resides (``order-lines``).

The last step needed is to register the ``customers``, ``orders`` and ``order-lines`` dataset in the pipe for the
``custom-subject-data``. The dataset from this pipe is merged with the internal dataset(s) for processing the GDPR data
and ultimately link it with a GDPR access request from a matching data subject.

.. _gdpr_subject:

GDPR subject
============

The GDPR subject dataset (dataset name ``gdpr-subject``) contains entities about data subjects with the following datastructure:

Prototype
^^^^^^^^^

::

    {
      "gdpr-subject:subject-id": "unique-ID-for-data-subject",
      "gdpr-subject:identifier": ["a-list", "of-identifier-values", "to-match-this-data-subject", "to-other-instances"]
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

   * - ``gdpr-subject:subject-id``
     - String
     - A unique ID for the data subject
     -
     - Yes

   * - ``gdpr-subject:identifier``
     - List<String{>=1}>
     - A list of values to match this data subject to other instances of the same data subject.
     -
     - Yes

Input API
^^^^^^^^^

The input API for the ``gdpr-subject`` dataset is the ``gdpr-subject-in`` :ref:`HTTP endpoint <http_endpoint_source>` pipe.
Its URL is on the form:

::

    https://gdpr-platform-datahub-url/api/receivers/gdpr-subject-in/entities

The endpoint expects JSON data on the form outlined above and implements the :doc:`JSON Push Protocol <json-push>` (receiver/sink).

Output API
^^^^^^^^^^

The output API for the ``gdpr-subject`` dataset is the ``gdpr-subject-out`` :ref:`HTTP endpoint <http_endpoint_sink>` pipe.
Its URL is on the form:

::

    https://gdpr-platform-datahub-url/api/publishers/gdpr-subject-out/entities

The endpoint implements the :doc:`JSON Push Protocol <json-push>` (source).

.. _gdpr_subject_internal_api:

Internal API
^^^^^^^^^^^^

The internal API must be a dataset with the id ``custom-subject``. This dataset is required to contain entities on the
form outlined above. Any entities from this dataset will be merged with any data posted to the input API endpoint
before being stored in the ``gdpr-subject`` dataset. The entites in this dataset are available externally through
the output API pipe.

.. _gdpr_consent:

GDPR consent
============

The GDPR consent dataset (dataset name ``gdpr-consent``) contains entities with information about consent purposes with the following datastructure:

Prototype
^^^^^^^^^

::

    {
      "gdpr-consent:consent-id": "unique-ID-for-the-consent",
      "gdpr-consent:version": "version-code",
      "gdpr-consent:lang": "iso-lang-code",
      "gdpr-consent:title": "A descriptive title for the consent definition",
      "gdpr-consent:consent-request": "The YES/NO question to the data subject",
      "gdpr-consent:valid-from": "2018-05-25T00:00:00.001Z",
      "gdpr-consent:valid-to": "2018-05-25T00:00:00.001Z",
      "gdpr-consent:description": "Details about the consent request",
      "gdpr-consent:data-source": "How did you obtain the data connected to this processing activity",
      "gdpr-consent:data-target": "Who are you sending the data to",
      "gdpr-consent:business-process": "What business process is the processing activity connected to",
      "gdpr-consent:policy-id": "unique-ID-of-a-policy-defined-in-the-GDPR-platform",
      "gdpr-consent:policy-link": "https://a.link.to/policy-document"
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

   * - ``gdpr-consent:consent-id``
     - String
     - A unique IDs for the consent
     -
     - Yes

   * - ``gdpr-consent:version``
     - String
     - A code specifying the version of this consent
     -
     - Yes

   * - ``gdpr-consent:lang``
     - String
     - A ISO code specifying the language of the consent version (for example "en" or "en-GB").
       It is a concatenation of the two-letter ISO 639 language code with the two letter ISO 3166 country code,
       using a hyphen (``"-"``) character as a separator. The ISO 3166 part is optional.
     -
     - Yes

   * - ``gdpr-consent:title``
     - String
     - A descriptive title for the consent definition
     -
     - Yes

   * - ``gdpr-consent:consent-request``
     - String
     - The YES/NO question to the data subject
     -
     - Yes

   * - ``gdpr-consent:valid-from``
     - String
     - A datetime string in ISO 8601 format that specifies what time this purpose definition is valid from (optional)
     -
     -

   * - ``gdpr-consent:valid-to``
     - String
     - A datetime string in ISO 8601 format that specifies how long this purpose definition is valid (optional)
     -
     -

   * - ``gdpr-consent:description``
     - String
     - Details about the consent request
     -
     - Yes

   * - ``gdpr-consent:data-source``
     - String
     - How did you obtain the data connected to this processing activity
     -
     - Yes

   * - ``gdpr-consent:data-target``
     - String
     - Who are you sending the data to
     -
     - Yes

   * - ``gdpr-consent:business-process``
     - String
     - What business process is the processing activity connected to (optional)
     -
     -

   * - ``gdpr-consent:policy-id``
     - String
     - A unique ID of a policy defined in the GDPR platform (optional)
     -
     -

   * - ``gdpr-consent:policy-link``
     - String
     - A URL to a policy document (optional)
     -
     -

Input API
^^^^^^^^^

The input API for the ``gdpr-consent`` dataset is the ``gdpr-consent-in`` :ref:`HTTP endpoint <http_endpoint_source>` pipe.
Its URL is on the form:

::

    https://gdpr-platform-datahub-url/api/receivers/gdpr-consent-in/entities

The endpoint expects JSON data on the form outlined above and implements the :doc:`JSON Push Protocol <json-push>` (receiver/sink).

Output API
^^^^^^^^^^

The output API for the ``gdpr-consent`` dataset is the ``gdpr-consent-out`` :ref:`HTTP endpoint <http_endpoint_sink>` pipe.
Its URL is on the form:

::

    https://gdpr-platform-datahub-url/api/publishers/gdpr-consent-out/entities

The endpoint implements the :doc:`JSON Push Protocol <json-push>` (source).

Internal API
^^^^^^^^^^^^

The internal API must be a dataset with the id ``custom-consent``. This dataset is required to contain entities on the
form outlined above. Any entities from this dataset will be merged with any data posted to the input API endpoint
before being stored in the ``gdpr-consent`` dataset. The entites in this dataset are available externally through
the output API pipe.

.. _gdpr_subject_consent:

GDPR subject consent
====================

The GDPR subject consent dataset (dataset name ``gdpr-subject-consent``) is used to record the consent choices for each
data subject. It contains entities with the following datastructure:

Prototype
^^^^^^^^^

::

    {
      "gdpr-subject-consent:data-subject-id": "unique-ID-for-data-subject",
      "gdpr-subject-consent:consent-id": "unique-ID-for-the-consent",
      "gdpr-subject-consent:consented": false,
      "gdpr-subject-consent:valid-from": "2018-05-25T00:00:00.001Z",
      "gdpr-subject-consent:consent-source-id": "unique-ID-for-the-system-used-to-collect-the-consent",
      "gdpr-subject-consent:consent-source-description": "A description of how the consent was obtained"
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

   * - ``gdpr-subject-consent:data-subject-id``
     - String
     - A unique ID for the data subject
     -
     - Yes

   * - ``gdpr-subject-consent:consent-id``
     - String
     - A uniqe ID for the consent
     -
     - Yes

   * - ``gdpr-subject-consent:consented``
     - Boolean
     - A boolean flag to indicate if the consent is affirmative or not (``true`` or ``false``)
     -
     - Yes

   * - ``gdpr-consent:valid-from``
     - String
     - A datetime string in ISO 8601 format for when the consent selection was made
     -
     -  Yes

   * - ``gdpr-subject-consent:consent-source-id``
     - String
     - A unique ID for the system used to collect the consent (optional)
     -
     -

   * - ``gdpr-subject-consent:consent-source-description``
     - String
     - A description of how the consent was obtained (optional)
     -
     -

Input API
^^^^^^^^^

The input API for the ``gdpr-subject-consent`` dataset is the ``gdpr-subject-consent-in`` :ref:`HTTP endpoint <http_endpoint_source>` pipe.
Its URL is on the form:

::

    https://gdpr-platform-datahub-url/api/receivers/gdpr-subject-consent-in/entities

The endpoint expects JSON data on the form outlined above and implements the :doc:`JSON Push Protocol <json-push>` (receiver/sink).

Output API
^^^^^^^^^^

The output API for the ``gdpr-subject-consent`` dataset is the ``gdpr-subject-consent-out`` :ref:`HTTP endpoint <http_endpoint_sink>` pipe.
Its URL is on the form:

::

    https://gdpr-platform-datahub-url/api/publishers/gdpr-subject-consent-out/entities

The endpoint implements the :doc:`JSON Push Protocol <json-push>` (source).

Internal API
^^^^^^^^^^^^

The internal API must be a dataset with the id ``custom-subject-consent``. This dataset is required to contain entities on the
form outlined above. Any entities from this dataset will be merged with any data posted to the input API endpoint
before being stored in the ``gdpr-subject-consent`` dataset. The entites in this dataset are available externally through
the output API pipe.

.. _gdpr_purpose:

GDPR purpose
============

The GDPR purpose dataset (dataset name ``gdpr-purpose``) is used to record the purposes for which your organisation
is collecting data. It contains entities with the following datastructure:

Prototype
^^^^^^^^^

::

   {
     "gdpr-purpose:purpose-id": "unique-ID-for-the-purpose",
     "gdpr-purpose:version": "version-code",
     "gdpr-purpose:lang": "lang-code",
     "gdpr-purpose:title": "A descriptive title to the purpose definition",
     "gdpr-purpose:purpose-type-id": "The type of purpose (consent, contract, legal-obligation, vital-interest, public-interest, official-authority, legitimate-interest)",
     "gdpr-purpose:detail": "The detail about the purpose",
     "gdpr-purpose:valid-to": "2018-05-25T00:00:00.001Z",
     "gdpr-purpose:description": "Details about the purpose request",
     "gdpr-purpose:data-source": "How did you obtain the data connected to this processing activity",
     "gdpr-purpose:data-target": "Who are you sending the data to",
     "gdpr-purpose:business-process": "What business process is the processing activity connected to",
     "gdpr-purpose:policy-id": "unique-ID-of-a-policy-defined-in-the-GDPR-platform",
     "gdpr-purpose:policy-link": "https://a.link.to/policy-document"
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

   * - ``gdpr-purpose:purpose-id``
     - String
     - A unique ID for the purpose
     -
     - Yes

   * - ``gdpr-purpose:version``
     - String
     - A code specifying the version of this purpose
     -
     - Yes

   * - ``gdpr-purpose:lang``
     - String
     - A ISO code specifying the language of the purpose (for example "en" or "en-GB").
       It is a concatenation of the two-letter ISO 639 language code with the two letter ISO 3166 country code,
       using a hyphen (``"-"``) character as a separator. The ISO 3166 part is optional.
     -
     - Yes

   * - ``gdpr-purpose:title``
     - String
     - A descriptive title to the purpose definition
     -
     - Yes

   * - ``gdpr-purpose:purpose-type-id``
     - Enum<String>
     - The type of purpose. Valid values are one of:

        * ``"consent"``
        * ``"contract"``
        * ``"legal-obligation"``
        * ``"vital-interest"``
        * ``"public-interest"``
        * ``"official-authority"``
        * ``"legitimate-interest"``
     -
     - Yes

   * - ``gdpr-purpose:valid-from``
     - String
     - A datetime string in ISO 8601 format that specifies how long this purpose definition is valid
     -
     -

   * - ``gdpr-purpose:description``
     - String
     - Details about the purpose request
     -
     - Yes

   * - ``gdpr-purpose:data-source``
     - String
     - How did you obtain the data connected to this processing activity
     -
     - Yes

   * - ``gdpr-purpose:data-target``
     - String
     - Who are you sending the data to
     -
     - Yes

   * - ``gdpr-purpose:business-process``
     - String
     - What business process is the processing activity connected to (optional)
     -
     -

   * - ``gdpr-purpose:policy-id``
     - String
     - A unique ID of a policy defined in the GDPR platform (optional)
     -
     -

   * - ``gdpr-purpose:policy-link``
     - String
     - A URL to a policy document (optional)
     -
     -

Input API
^^^^^^^^^

The input API for the ``gdpr-purpose`` dataset is the ``gdpr-purpose-in`` :ref:`HTTP endpoint <http_endpoint_source>` pipe.
Its URL is on the form:

::

    https://gdpr-platform-datahub-url/api/receivers/gdpr-purpose-in/entities

The endpoint expects JSON data on the form outlined above and implements the :doc:`JSON Push Protocol <json-push>` (receiver/sink).

Output API
^^^^^^^^^^

The output API for the ``gdpr-purpose`` dataset is the ``gdpr-purpose-out`` :ref:`HTTP endpoint <http_endpoint_sink>` pipe.
Its URL is on the form:

::

    https://gdpr-platform-datahub-url/api/publishers/gdpr-purpose-out/entities

The endpoint implements the :doc:`JSON Push Protocol <json-push>` (source).

Internal API
^^^^^^^^^^^^

The internal API must be a dataset with the id ``custom-purpose``. This dataset is required to contain entities on the
form outlined above. Any entities from this dataset will be merged with any data posted to the input API endpoint
before being stored in the ``gdpr-purpose`` dataset. The entites in this dataset are available externally through
the output API pipe.

.. _gdpr_purpose_type:

GDPR purpose type
=================

The GDPR purpose type dataset (dataset name ``gdpr-purpose-type``) is used to record the types of purposes for which your organisation
is collecting data. It contains entities with the following datastructure:

Prototype
^^^^^^^^^

::

   {
     "gdpr-purpose-type:purpose-type-id": "unique-ID-for-the-purpose-type",
     "gdpr-purpose-type:lang": "lang-code",
     "gdpr-purpose-type:title": "A descriptive title to the purpose-type definition",
     "gdpr-purpose-type:description": "Description of the purpose-type",
     "gdpr-purpose-type:legal-link": "https://a.link.to/legal-document"
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

   * - ``gdpr-purpose-type:purpose-type-id``
     - String
     - A unique ID for the purpose-type
     -
     - Yes

   * - ``gdpr-purpose-type:lang``
     - String
     - A ISO code specifying the language of the purpose type (for example "en" or "en-GB").
       It is a concatenation of the two-letter ISO 639 language code with the two letter ISO 3166 country code,
       using a hyphen (``"-"``) character as a separator. The ISO 3166 part is optional.
     -
     - Yes

   * - ``gdpr-purpose-type:description``
     - String
     - Description of the purpose-type (optional)
     -
     -

   * - ``gdpr-purpose-type:policy-link``
     - String
     - A URL to a legal document (optional)
     -
     -

Input API
^^^^^^^^^

The input API for the ``gdpr-purpose-type`` dataset is the ``gdpr-purpose-in`` :ref:`HTTP endpoint <http_endpoint_source>` pipe.
Its URL is on the form:

::

    https://gdpr-platform-datahub-url/api/receivers/gdpr-purpose-type-in/entities

The endpoint expects JSON data on the form outlined above and implements the :doc:`JSON Push Protocol <json-push>` (receiver/sink).

Output API
^^^^^^^^^^

The output API for the ``gdpr-purpose-type`` dataset is the ``gdpr-purpose-type-out`` :ref:`HTTP endpoint <http_endpoint_sink>` pipe.
Its URL is on the form:

::

    https://gdpr-platform-datahub-url/api/publishers/gdpr-purpose-out/entities

The endpoint implements the :doc:`JSON Push Protocol <json-push>` (source).

Internal API
^^^^^^^^^^^^

The internal API must be a dataset with the id ``custom-purpose-type``. This dataset is required to contain entities on the
form outlined above. Any entities from this dataset will be merged with any data posted to the input API endpoint
before being stored in the ``gdpr-purpose-type`` dataset. If the ``custom-purpose-type`` and ``gdpr-purpose-type-in`` dataset
contain the same entity (i.e. with the same ``purpose-type-id``), the newest version will be chosen.

The entites in this dataset are available externally through the output API pipe.


.. _gdpr_data_type:

GDPR data type
==============

The GDPR data type dataset (dataset name ``gdpr-data-type``) is used to record the types of data your organisation
is collecting. It contains entities with the following datastructure:

Prototype
^^^^^^^^^

::

   {
     "gdpr-data-type:data-type-id": "unique-ID-for-the-data-type",
     "gdpr-data-type:level": "identificator-for-privacy-level-of-the-data",
     "gdpr-data-type:description": "A default description of the data type",
     "gdpr-data-type:en-description": "A description of the data type, using language code ``en``",
     "gdpr-data-type:xx-description": "A description of the data type, using language code ``xx``",
     "gdpr-data-type:xx-YY-description": "A description of the data type, using language code ``xx-YY``",
     "gdpr-data-type:system-id": "ID-for-the-system-containg-the-data",
     "gdpr-data-type:purpose-id": ["A list of", "purposes", "applying to", "this data type"],
     "gdpr-data-type:contact": "some.body@somewhere.com"
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

   * - ``gdpr-data-type:data-type-id``
     - String
     - A unique ID for the data-type
     -
     - Yes

   * - ``gdpr-data-type:level``
     - Enum<String>
     - An identificator for the privacy level of the data. Valid values are one of:

        * ``"sensitive"``
        * ``"personal"``
        * ``"related"``
     -
     - Yes

   * - ``gdpr-data-type:description``
     - String
     - A default description of the data type (no language qualification)
     -
     - Yes

   * - ``gdpr-data-type:description-en``
     - String
     - A description of the data type for the english language (optional)
     -
     -

   * - ``gdpr-data-type:description-xx-YY``
     - String
     - A description of the data type for the language ``xx`` using the country variant ``YY``. For example ``en-GB`` (optional).
     -
     -

   * - ``gdpr-data-type:system-id``
     - String
     - A ID for the system containg the data (optional)
     -
     -

   * - ``gdpr-data-type:purpose-id``
     - List<String>
     - A list of purposes (purpose ids) applying to this data type (optional)
     -
     -

   * - ``gdpr-data-type:contact``
     - String
     - A mail address for the responsible contact for this data type (optional)
     -
     -

Input API
^^^^^^^^^

The input API for the ``gdpr-data-type`` dataset is the ``gdpr-data-type-in`` :ref:`HTTP endpoint <http_endpoint_source>` pipe.
Its URL is on the form:

::

    https://gdpr-platform-datahub-url/api/receivers/gdpr-data-type-in/entities

The endpoint expects JSON data on the form outlined above and implements the :doc:`JSON Push Protocol <json-push>` (receiver/sink).

Output API
^^^^^^^^^^

The output API for the ``gdpr-data-type`` dataset is the ``gdpr-data-type-out`` :ref:`HTTP endpoint <http_endpoint_sink>` pipe.
Its URL is on the form:

::

    https://gdpr-platform-datahub-url/api/publishers/gdpr-data-type-out/entities

The endpoint implements the :doc:`JSON Push Protocol <json-push>` (source).

Internal API
^^^^^^^^^^^^

The internal API must be a dataset with the id ``custom-data-type``. This dataset is required to contain entities on the
form outlined above. Any entities from this dataset will be merged with any data posted to the input API endpoint
before being stored in the ``gdpr-data-type`` dataset. The entites in this dataset are available externally through
the output API pipe.

.. _gdpr_policy:

GDPR policy
===========

The GDPR policy dataset (dataset name ``gdpr-policy``) is used to record the types of policies for your organisation.
It contains entities with the following datastructure:

Prototype
^^^^^^^^^

::

   {
     "gdpr-policy:policy-id": "unique-ID-for-the-policy",
     "gdpr-policy:version": "version-code",
     "gdpr-policy:lang": "iso-code",
     "gdpr-policy:title": "A descriptive title for the policy",
     "gdpr-policy:description": "Details about the policy",
     "gdpr-policy:link": "https://a.link.to/policy-document",
     "gdpr-policy:markup": "<HTML markup for the policy/>",
     "gdpr-policy:valid-from": "2018-05-25T00:00:00.001Z",
     "gdpr-policy:valid-to": "2018-05-25T00:00:00.001Z"
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

   * - ``gdpr-policy:policy-id``
     - String
     - A unique ID for the policy
     -
     - Yes

   * - ``gdpr-policy:version``
     - String
     - A code specifying the version of this policy
     -
     - Yes

   * - ``gdpr-policy:lang``
     - String
     - A ISO code specifying the language of the policy definition (for example "en" or "en-GB").
       It is a concatenation of the two-letter ISO 639 language code with the two letter ISO 3166 country code,
       using a hyphen (``"-"``) character as a separator. The ISO 3166 part is optional.
     -
     - Yes

   * - ``gdpr-policy:title``
     - String
     - A descriptive title for the policy
     -
     - Yes

   * - ``gdpr-policy:description``
     - String
     - A description of the policy
     -
     - Yes

   * - ``gdpr-policy:link``
     - String
     - A URL to a policy document (optional)
     -
     -

   * - ``gdpr-policy:markup``
     - String
     - HTML markup for the policy (optional)
     -
     -

   * - ``gdpr-policy:valid-from``
     - String
     - A datetime string in ISO 8601 format that specifies what time this policy is valid from (optional)
     -
     -

   * - ``gdpr-policy:valid-to``
     - String
     - A datetime string in ISO 8601 format that specifies how long this policy is valid (optional)
     -
     -

Input API
^^^^^^^^^

The input API for the ``gdpr-policy`` dataset is the ``gdpr-policy-in`` :ref:`HTTP endpoint <http_endpoint_source>` pipe.
Its URL is on the form:

::

    https://gdpr-platform-datahub-url/api/receivers/gdpr-policy-in/entities

The endpoint expects JSON data on the form outlined above and implements the :doc:`JSON Push Protocol <json-push>` (receiver/sink).

Output API
^^^^^^^^^^

The output API for the ``gdpr-policy`` dataset is the ``gdpr-policy-out`` :ref:`HTTP endpoint <http_endpoint_sink>` pipe.
Its URL is on the form:

::

    https://gdpr-platform-datahub-url/api/publishers/gdpr-policy-out/entities

The endpoint implements the :doc:`JSON Push Protocol <json-push>` (source).

Internal API
^^^^^^^^^^^^

The internal API must be a dataset with the id ``custom-policy``. This dataset is required to contain entities on the
form outlined above. Any entities from this dataset will be merged with any data posted to the input API endpoint
before being stored in the ``gdpr-policy`` dataset. The entites in this dataset are available externally through
the output API pipe.

.. _gdpr_custom_translations:

GDPR custom translations
========================

The text contents of SMS, email messages and some other static strings used in dynamic content generation in the
GDPR plattform exists as data in the data hub.

These text can be customized using the :ref:`Translation GUI<gdpr_custom_text_and_translation>`.

The :ref:`GUI<gdpr_custom_text_and_translation>` is almost always the preferable way of editing the strings, but if you for some reason need to customize the strings programatically, you can do that by editing the configuration of the pipe called ``custom-translations``.
The pipe has an embedded source with entities containing translation information for a certain set of predefined
keys. The structure of each of the entities in the embedded source is on the form:


::

    {
        "_id": "translation-item-key",
        "translations": {
            "iso-code": {
                "property-id": "Translation text here",
                "other-property-id": "Other translation text here",
            },
            "other-iso-code": {
                "property-id": "Other language translation text here",
                "other-property-id": "Other language translation text for other-property-id here"
            }
            ..
        }
    }


The ``iso-code`` should be a ISO language code on the form ``en`` or ``en-us``, and the actual property keys will
wary from item to item.

Description of the translation item keys:

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30, 70

   * - Key
     - Description

   * - ``gdpr_welcome_text``
     - This entity represents the text used by the "Welcome" screen in the GDPR Data Access portal.

   * - ``access_request_mail``
     - This entity represents the text used to send emails to accounts registered as being responsible for a particular
       GDPR data type in the setup excel sheet. It is sent whenever a new GDPR Access Request is received from the
       GDPR Data Access portal.

   * - ``access_request_delete_mail``
     - This entity represents the text used to send emails to accounts registered as being responsible for a particular
       GDPR data type in the setup excel sheet. It is sent whenever a new GDPR Delete Request is received from the
       GDPR Data Access portal.

   * - ``change_request_mail``
     - This entity represents the text used to send emails to accounts registered as being responsible for a particular
       GDPR data type in the setup excel sheet. It is sent whenever a new GDPR Access Request for changing registered data
       is received from the GDPR Data Access portal.

   * - ``subject_data_available_mail``
     - This entity represents the text used to send emails to a GDPR data subject that has previously requested data
       via a GDPR Access Request. It is sent whenever someone responsible for a GDPR data type has filled out and
       uploaded collected data in the data upload excel spread sheet (previously generated by the GDPR access request) or
       if the data subject flow is fully automated it is sent when the access request is received. There is a default delay of
       30 minutes on these messages.

   * - ``subject_data_available_sms``
     - This entity represents the text used to send SMSs to a GDPR data subject that has previously requested data
       via a GDPR Access Request. It is sent whenever someone responsible for a GDPR data type has filled out and
       uploaded collected data in the data upload excel spread sheet (previously generated by the GDPR access request) or
       if the data subject flow is fully automated it is sent when the access request is received. There is a default delay of
       30 minutes on these messages.

   * - ``access_request_type_title``
     - This entity represents the title of GDPR access request objects in the GDPR data access portal.

   * - ``change_request_type_title``
     - This entity represents the title of GDPR change request objects in the GDPR data access portal.

   * - ``consent_change_request_type_title``
     - This entity represents the title of consent change objects in the GDPR data access portal.


The full list of standard items is (english and norwegian translations are provided by default):

::

    {
      "_id": "gdpr_welcome_text",
      "translations": {
        "en": {
          "rdf:title": "Welcome",
          "rdfs:comment": "The goal of GDPR is transparency of what personal data is kept and what is is used for. This means you have the right to see all data we keep about you, even the data that is not obviosly understandable to you. The purposes of why we keep data should be well described. Please contact us if you have any questions about your data. Use this mail adress: info@sesam.io"
        },
        "no": {
          "rdf:title": "Velkommen",
          "rdfs:comment": "Målet for GDPR er åpenhet rundt hvilke personlige data som er lagret og hva det brukes til. Dette innebærer at du har rett til å se alle data vi har lagret om deg, selv de data som ikke er åpenbart forståelig for deg. Formålet for hvorfor vi har disse dataene skal være tydelig beskrevet. Ta kontakt med oss om du har noen spørsål om dine data. Bruk denne epost addressen: info@sesam.io"
        }
      }
    }, {
      "_id": "access_request_type_title",
      "translations": {
        "en": {
          "rdf:title": "GDPR access request"
        },
        "no": {
          "rdf:title": "GDPR innsynsforespørsel"
        }
      }
    }, {
      "_id": "change_request_type_title",
      "translations": {
        "en": {
          "rdf:title": "GDPR change request"
        },
        "no": {
          "rdf:title": "GDPR endringsforespørsel"
        }
      }
    }, {
      "_id": "consent_change_request_type_title",
      "translations": {
        "en": {
          "rdf:title": "Consent changed"
        },
        "no": {
          "rdf:title": "Endret samtykke"
        }
      }
    }, {
      "_id": "access_request_mail",
      "translations": {
        "en": {
          "body_template": "A GDPR data access request from {{ contactinfo }} for data that you have been set as responsible for has been submitted to the GDPR portal. <br><br>You can download the Excel file to fill out at <a href=\"$ENV(sesam-portal-gui-url)subscription/$ENV(subscription)/gdpr/access-requests?email={{ contact }}&id={{ requestId }}\"/>here</a>.",
          "subject_template": "GDPR data access request submitted by {{ contactinfo }}",
          "text_body_template": ""
        },
        "no": {
          "body_template": "En GDPR data tilgangsforespørsel fra {{ contactinfo }} som du er oppgitt som ansvarlig for har blitt registrert i GDPR portalen.<br><br>Du kan laste ned en Excel mal som du kan fylle ut <a href=\"$ENV(sesam-portal-gui-url)subscription/$ENV(subscription)/gdpr/access-requests?email={{ contact }}&id={{ requestId }}\"/>her</a>.",
          "subject_template": "GDPR data tilgangsforespørsel mottatt fra {{ contactinfo }}",
          "text_body_template": ""
        }
      }
    }, {
      "_id": "access_request_delete_mail",
      "translations": {
        "en": {
          "body_template": "A GDPR data access request from {{ contactinfo }} for deletion of data that you have been set as responsible for has been submitted to the GDPR portal. <br><br>You can download the Excel file to fill out at <a href=\"$ENV(sesam-portal-gui-url)subscription/$ENV(subscription)/gdpr/access-requests?email={{ contact }}&id={{ requestId }}\"/>here</a>.",
          "subject_template": "GDPR data access data deletion request submitted by {{ contactinfo }}",
          "text_body_template": ""
        },
        "no": {
          "body_template": "En GDPR data sletting forespørsel fra {{ contactinfo }} som du er oppgitt som ansvarlig for har blitt registrert i GDPR portalen.<br><br>Du kan laste ned en Excel mal som du kan fylle ut <a href=\"$ENV(sesam-portal-gui-url)subscription/$ENV(subscription)/gdpr/access-requests?email={{ contact }}&id={{ requestId }}\"/>her</a>.",
          "subject_template": "GDPR data sletting forespørsel mottatt fra {{ contactinfo }}",
          "text_body_template": ""
        }
      }
    }, {
      "_id": "change_request_mail",
      "translations": {
        "en": {
          "body_template": "A GDPR data change request from {{ contactinfo }} for data that you have been set as responsible for has been submitted to the GDPR portal. <br><br>You can download a Excel file with a list of change requests <a href=\"$ENV(sesam-portal-gui-url)subscription/$ENV(subscription)/gdpr/change-requests?email={{ recipients }}\"/>here</a>.",
          "subject_template": "GDPR change request submitted by {{ contactinfo }}",
          "text_body_template": ""
        },
        "no": {
          "body_template": "En GDPR data endringsforespørsel fra {{ contactinfo }} for data som du er oppgitt som ansvarlig for har blitt registrert i GDPR portalen.<br><br>Du kan laste ned en oversikt i Excel format <a href=\"$ENV(sesam-portal-gui-url)subscription/$ENV(subscription)/gdpr/change-requests?email={{ recipients }}\"/>her</a>.",
          "subject_template": "GDPR endringsforespørsel mottatt fra {{ contactinfo }}",
          "text_body_template": ""
        }
      }
    }, {
      "_id": "subject_data_available_mail",
      "translations": {
        "en": {
          "body_template": "Your requested data is now available in the GDPR portal. <br><br>Please log in at <a href=\"$ENV(portal-url)\">GDPR portal</a> to see it.",
          "subject_template": "GDPR data access request results available",
          "text_body_template": ""
        },
        "no": {
          "body_template": "Data du har forespurt er tilgjengelig i GDPR portalen.<br><br>Logg inn i <a href=\"$ENV(portal-url)\">GDPR portalen</a> for å se dem.",
          "subject_template": "GDPR data tilgjengelig",
          "text_body_template": ""
        }
      }
    }, {
      "_id": "subject_data_available_sms",
      "translations": {
        "en": {
          "body_template": "Your requested data is now available in the GDPR portal. Please log in at $ENV(portal-url) to see it."
        },
        "no": {
          "body_template": "Data du har forespurt er tilgjengelig i GDPR portalen. Logg inn i $ENV(portal-url) for å se dem."
        }
      }
    }

When customizing the content for a particular key you should always start with a copy from this official list.
Place the copy into the embedded source's ``entities`` array and either change the texts as needed or add a new
language key to add text for a new language. Please do not change the macros embedded in the text strings
(within ``{{`` and ``}}`` blocks and the ``$ENV(..)`` variables).

After saving the ``custom-translations`` pipe, make sure you press "start" on the pipe to update the GDPR platform
contents. Note that the changes will not affect already emitted notifications or objects - only new ones.

.. _gdpr_unstructured_data:

GDPR unstructured data support
==============================

The API described thus far is suited for structured/tabular data such as data from SQL servers, CSV files and so on.
In practice, an organization will typically also have a lot of subject data in form of unstructured content such as
emails, PDFs and word documents. This data will often contain relevant information pertaining to a GDPR access request.
Searching for relevant documents in email servers, archiving systems, file shares or other unstructured data repositories
can be time consuming and prone to errors of omission. The Sesam GDPR platform supports automating this process.

However, even if we automate the extraction, indexing and search process the last step before making the data (documents)
available to the data subject in the data access portal will need human intervention. The reason for this is due to the
nature of unstructured data; the automated system might misidentify documents ("false positives") or the document contents
may contain private information about other data subjects - i.e. not just information about the data subject in question.

Thus all search matches for a data subject's GDPR access request must be manually vetted first. As a result of this
vetting proxess, the contents delivered to the user may be withheld completely or partly and/or the textual content
replaced by a reduced or redacted version.

Overview of the solution
^^^^^^^^^^^^^^^^^^^^^^^^

The solution consists of several parts:

* Document sources (microservices)
* Internal dataset API
* Content extractor service
* Document index
* Document search service
* Manual vetting of search results
* Content encryption service

Document sources
^^^^^^^^^^^^^^^^

The input to the system is in the form of one or more document sources. Document sources are microservices which
deliver information (metadata) about a particular repository of unstructured data (files), for example a file
system document source or an email document source. It also has the responsibility of providing a HTTP API for
delivering the file itself.

The document source does this by delivering a stream of JSON documents on a particular format. If the output from the
document source is not already in the required form, the pipe reading from this source has the responsibility to transform
the input to match the following form:

Prototype
^^^^^^^^^

::

    {
      "gdpr-data-type:data-type-id": "source-data-type",
      "gdpr-document:document_id": "source-prefix:unique-id-for-document",
      "gdpr-document:extract-content": "~rhttp://address-to-source-microservice:port/where_to_download?file=the_file_binary",
      "gdpr-document:filesize": 123456,
      "gdpr-document:metadata": {"source-specific": "metadata", "properties":"here" },
      "gdpr-document:mime-type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "gdpr-document:original-url": "~rhttp://original-url:port/to_where_to_download?file=the_file_binary"
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

   * - ``gdpr-data-type:data-type-id``
     - String
     - The data-type ID for the document source. Note that this must match a properly registered GDPR data type in the
       GDPR platform by filling out and uploading the :ref:`GDPR data types and purposes configuration <gdpr_data_types_purposes_configuration>`
       spreadsheet (or using the ``GDPR data type`` API defined earlier in this document).
     -
     - Yes

   * - ``gdpr-document:document_id``
     - String
     - A unique document ID for the document source - it should be prefixed with the ID of the system used
     -
     - Yes

   * - ``gdpr-document:extract-content``
     - String
     - A URL to the document source microservice that produced the data. It should return the binary document data.
       Note that it must NOT require any authentication or authorization. If any is needed, it must proxy this
       to the backend system by itself. It should run in a local network context so it is reachable only by the GDPR
       platform.
     -
     - Yes

   * - ``gdpr-document:metadata``
     - Object
     - An optional dictionary object with metadata properties for the document, it can contain any valid JSON data
     -
     -

   * - ``gdpr-document:filesize``
     - Integer
     - The size in bytes of the document file.
     -
     - Yes

   * - ``gdpr-document:filename``
     - String
     - The filename of the document file (OPTIONAL). Note that if the filename is not provided the GDPR data access portal
       will attempt to generate one based on ``gdpr-document:document_id`` when the file is downloaded by the user.
     -
     -

   * - ``gdpr-document:mime-type``
     - String
     - The mime type of the document.
     -
     - Yes

   * - ``gdpr-document:original-url``
     - String
     - A URL to the original location for the document. It should return the binary document data.
       Note that this URL should challenge for any authentication/authorization needed. The URL must be resolvable
       for any human operator (within the correct network environment) that has the task to vet the document
       search result for a GDPR access request.
     -
     - Yes


See `https://github.com/sesam-community/file-share-service <https://github.com/sesam-community/file-share-service>`_  for
an example of such a service.

Internal API
^^^^^^^^^^^^

The internal API of the unstructured data framework is a dataset with the id ``custom-documents``. This dataset is
required to contain entities on the form outlined above. The associated ``custom-documents`` pipe is a merge pipe with
the complete list of document source datasets that should be used by the indexing service.

Content extractor service
^^^^^^^^^^^^^^^^^^^^^^^^^

The contents of the ``custom-documents`` dataset is fed to the content extractor service. This service will download
the file pointed to by the ``gdpr-document:extract-content`` URL and attempt to extract all text information it can
from the file.

Document index
^^^^^^^^^^^^^^

The extracted textual information is indexed together with the properties outline above (except ``gdpr-document:metadata``)
and put into a search engine/index for indexing. The original file is *not* stored in this process.

Document search service
^^^^^^^^^^^^^^^^^^^^^^^

Whenever a new GDPR access request is created in the GDPR platform, a query is performed against the indexed documents
using the configured subject data properties (email, phone-number, customer id's and so on). The result of this
query, if any, is joined with the original data in ``custom-document`` and stored in the GDPR platform for the
data subject associated with the access request.

It is important to note that there is no automatic re-querying of previous document searches when new documents are added
to the index. The query is a *point-in-time* query and as such reflects the state of the document index at that point
in time. To update the search result, a new GDPR access request must be submitted by the data subject.

Manual vetting of search results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No data is relayed to the GDPR data access portal before a human has vetted this search result. This is done by
downloading :ref:`the data access request excel template <gdpr_data_access_request_template>`.

The spreadsheet will contain one data sheet per document source data type with one row per matching search
result. By downloading and inspecting the files linked to in the spreasheet and editing these rows the human operator
vets the search result. To remove a document the row should be removed. If the file itself should not be delivered to
the data subject, the link in ``gdpr-document:extract-content`` should be removed, and any redacted or partial text
content should be entered into the "text" column for that row. In the same way, metadata can also be edited (or removed)
as needed.

When the vetting process is finished and all data sheets for all data types have been filled out, the spreadsheet should
be uploaded to the GDPR portal, as described in the :ref:`GDPR data access request template <gdpr_data_access_request_template>` section.

Content encryption service
^^^^^^^^^^^^^^^^^^^^^^^^^^

Finally, after the vetted search result have been processed by the GDPR portal, the metadata about the document will be
encrypted using the public key of the data subject and then transmitted to the GDPR data access portal.

Additionally, if there is a ``gdpr-document:extract-content`` property for the document, the file itself will be
downloaded and encrypted before being transmitted to the GDPR data access portal. This "attachment" can then be decrypted
and downloaded as a document/file by the data subject on the client side.
