=======================
Tidsbanken to  Dataflow
=======================

Generated: 2024-08-27 07:32:09

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Avdeling to  Company
-------------------------------
Every Tidsbanken Avdeling will be synchronized with a  Company.

Once a link between a Tidsbanken Avdeling and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Avdeling and a  Company:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Avdeling Property
     -  Company Property
     -  Data Type
   * - Navn
     - name
     - "string"
   * - Organisasjonsnr
     - companyBusinessNo (Dependant on having wd:Q11994066 in countryIsoCode)
     - "string"
   * - sesam_avdelingId
     - companyBusinessNo (Dependant on having wd:Q2366457 in countryIsoCode)
     - "string"


Tidsbanken Kunde to  Company
----------------------------
Every Tidsbanken Kunde will be synchronized with a  Company.

Once a link between a Tidsbanken Kunde and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a  Company:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     -  Company Property
     -  Data Type
   * - Navn
     - name
     - "string"
   * - Organisasjonsnummer
     - companyBusinessNo (Dependant on having NO in countryIsoCodeDependant on having wd:Q11994066 in countryIsoCode)
     - "string"
   * - sesam_kundeId
     - companyBusinessNo (Dependant on having wd:Q852835 in countryIsoCode)
     - "string"


Tidsbanken Ansatt to  Address
-----------------------------
Every Tidsbanken Ansatt will be synchronized with a  Address.

Once a link between a Tidsbanken Ansatt and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a  Address:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     -  Address Property
     -  Data Type
   * - Id
     - companyNo
     - "string"

