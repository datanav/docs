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

These APIs are datasets with a defined data-structure that can be integrated with existing systems:

.. _gdpr_subject:

GDPR subject
============

The GDPR subject dataset (dataset name "gdpr-subject") contains entities about data subjects with the following datastructure:

Prototype
---------

::

    {
      "gdpr-subject:subject-id": "unique-ID-for-data-subject",
      "gdpr-subject:identifier": ["a-list", "of-identifier-values", "to-match-this-data-subject", "to-other-instances"]
    }


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

.. _gdpr_consent:

GDPR consent
============

The GDPR consemt dataset (dataset name "gdpr-consent") contains entities with information about consent purposes with the following datastructure:

Prototype
---------

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
----------

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

.. _gdpr_subject_consent:

GDPR subject consent
====================

The GDPR subject consent dataset (dataset name "gdpr-subject-consent") is used to record the consent choices for each
data subject. It contains entities with the following datastructure:

Prototype
---------

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
----------

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

.. _gdpr_purpose:

GDPR purpose
============

The GDPR purpose dataset (dataset name "gdpr-purpose") is used to record the purposes for which your organisation
is collecting data. It contains entities with the following datastructure:

Prototype
---------

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
----------

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

.. _gdpr_purpose_type:

GDPR purpose type
=================

The GDPR purpose type dataset (dataset name "gdpr-purpose-type") is used to record the types of purposes for which your organisation
is collecting data. It contains entities with the following datastructure:

Prototype
---------

::

   {
     "gdpr-purpose-type:purpose-type-id": "unique-ID-for-the-purpose-type",
     "gdpr-purpose-type:lang": "lang-code",
     "gdpr-purpose-type:title": "A descriptive title to the purpose-type definition",
     "gdpr-purpose-type:description": "Description of the purpose-type",
     "gdpr-purpose-type:legal-link": "https://a.link.to/legal-document"
   }


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


.. _gdpr_data_type:

GDPR data type
==============

The GDPR data type dataset (dataset name "gdpr-data-type") is used to record the types of data your organisation
is collecting. It contains entities with the following datastructure:

Prototype
---------

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
----------

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

.. _gdpr_policy:

GDPR policy
===========

The GDPR policy dataset (dataset name "gdpr-policy") is used to record the types of policies for your organisation.
It contains entities with the following datastructure:

Prototype
---------

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
----------

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
