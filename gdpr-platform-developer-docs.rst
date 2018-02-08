.. _gdpr_platform_developer_docs:

=====================================
GDPR platform developer documentation
=====================================

.. contents:: Table of Contents
   :depth: 2
   :local:

Overview
========

For automation of the GDPR platform, there are three main APIs/integration points available:

* GDPR subject
* GDPR consent
* GDPR subject consent

These APIs are datasets with a defined data-structure that can be integrated with existing systems:

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

GDPR consent
============

The GDPR consemt dataset (dataset name "gdpr-consent") contains entities with information about consent purposes with the following datastructure:

Prototype
---------

::

    {
      "gdpr-consent:consent-id": "unique-ID-for-the-consent",
      "gdpr-consent:title": "A descriptive title for the Consent definition",
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
     - A uniqe IDs for the consent
     -
     - Yes

   * - ``gdpr-consent:title``
     - String
     - A descriptive title for the Consent definition
     -
     - Yes

   * - ``gdpr-consent:consent-request``
     - String
     - The YES/NO question to the data subject
     -
     - Yes

   * - ``gdpr-consent:valid-from``
     - String
     - A datetime string in ISO 8601 format for when this consent definition is valid from
     -
     - Yes

   * - ``gdpr-consent:valid-to``
     - String
     - A optional datetime string in ISO 8601 format for when this consent definition is valid to
     -
     -

   * - ``gdpr-consent:description``
     - String
     - Details about the consent request
     -
     - Yes

   * - ``gdpr-consent:data-source``
     - String
     - How did you obtain the data connected to this prosessing activity
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
