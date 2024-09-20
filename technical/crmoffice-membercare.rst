================================
CRMOffice to MemberCare Dataflow
================================

Generated: 2024-09-20 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CRMOffice Companies to MemberCare Products
------------------------------------------
Every CRMOffice Companies will be synchronized with a MemberCare Products.

Once a link between a CRMOffice Companies and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Companies and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - CRMOffice Companies Property
     - MemberCare Products Property
     - MemberCare Data Type


CRMOffice Contacts to MemberCare Persons
----------------------------------------
Every CRMOffice Contacts will be synchronized with a MemberCare Persons.

Once a link between a CRMOffice Contacts and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Contacts and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - CRMOffice Contacts Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - familyName
     - lastname
     - "string"
   * - givenName
     - firstname
     - "string"


CRMOffice Activities to MemberCare Countries
--------------------------------------------
Every CRMOffice Activities will be synchronized with a MemberCare Countries.

Once a link between a CRMOffice Activities and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Activities and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - CRMOffice Activities Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - address.country
     - name
     - "string"


CRMOffice Companies to MemberCare Companies
-------------------------------------------
Every CRMOffice Companies will be synchronized with a MemberCare Companies.

Once a link between a CRMOffice Companies and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Companies and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - CRMOffice Companies Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - id
     - addresses.id
     - "string"
   * - postAddress.country
     - addresses.country.id
     - "string"
   * - postAddress.postCode
     - addresses.postalCode.zipCode
     - "string"
   * - postAddress.postalArea
     - addresses.postalCode.city
     - "string"
   * - visitAddress.country
     - addresses.country.id
     - "string"
   * - visitAddress.postCode
     - addresses.postalCode.zipCode
     - "string"
   * - visitAddress.postalArea
     - addresses.postalCode.city
     - "string"


CRMOffice Companies to MemberCare Countries
-------------------------------------------
Every CRMOffice Companies will be synchronized with a MemberCare Countries.

Once a link between a CRMOffice Companies and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Companies and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - CRMOffice Companies Property
     - MemberCare Countries Property
     - MemberCare Data Type

