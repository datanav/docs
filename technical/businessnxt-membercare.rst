========================
Businessnxt to  Dataflow
========================

Generated: 2024-09-03 08:57:55

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businessnxt to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Address to  Companies
---------------------------------
Every Businessnxt Address will be synchronized with a  Companies.

Once a link between a Businessnxt Address and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Address and a  Companies:

.. list-table::
   :header-rows: 1

   * - Businessnxt Address Property
     -  Companies Property
     -  Data Type
   * - addressLine1
     - addresses.street
     - "string"
   * - addressNo
     - addresses.id
     - "string"
   * - countryNo
     - addresses.country.id
     - "string"
   * - name
     - companyName
     - "string"
   * - postCode
     - addresses.postalCode.zipCode
     - "string"
   * - postalArea
     - addresses.postalCode.city
     - "string"


Businessnxt Company to  Companies
---------------------------------
Every Businessnxt Company will be synchronized with a  Companies.

Once a link between a Businessnxt Company and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Company and a  Companies:

.. list-table::
   :header-rows: 1

   * - Businessnxt Company Property
     -  Companies Property
     -  Data Type
   * - companyNo
     - addresses.id
     - "string"
   * - name
     - companyName
     - "string"


Businessnxt Country to  Countries
---------------------------------
Every Businessnxt Country will be synchronized with a  Countries.

Once a link between a Businessnxt Country and a  Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Country and a  Countries:

.. list-table::
   :header-rows: 1

   * - Businessnxt Country Property
     -  Countries Property
     -  Data Type
   * - isoCode
     - iso2Letter
     - "string"
   * - name
     - name
     - "string"

