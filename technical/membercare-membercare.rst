=================================
MemberCare to MemberCare Dataflow
=================================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Countries to MemberCare Companycategories
----------------------------------------------------
Every MemberCare Countries will be synchronized with a MemberCare Companycategories.

Once a link between a MemberCare Countries and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Countries and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - MemberCare Countries Property
     - MemberCare Companycategories Property
     - MemberCare Data Type
   * - url
     - url
     - "string"


MemberCare Organizations to MemberCare Companies
------------------------------------------------
Every MemberCare Organizations will be synchronized with a MemberCare Companies.

Once a link between a MemberCare Organizations and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Organizations and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - MemberCare Organizations Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - addresses.country.id
     - addresses.country.id
     - "string"
   * - addresses.id
     - addresses.id
     - "string"
   * - addresses.postalCode.city
     - addresses.postalCode.city
     - "string"
   * - addresses.postalCode.zipCode
     - addresses.postalCode.zipCode
     - "string"
   * - company.addresses.addressDescription
     - addresses.country.id
     - "string"
   * - company.addresses.id
     - addresses.id
     - "string"
   * - company.addresses.municipality
     - addresses.postalCode.zipCode
     - "string"
   * - company.addresses.start
     - addresses.postalCode.city
     - "string"
   * - company.addresses.street
     - addresses.street
     - "string"
   * - name
     - companyName
     - "string"


MemberCare Organizations to MemberCare Companycategories
--------------------------------------------------------
Every MemberCare Organizations will be synchronized with a MemberCare Companycategories.

Once a link between a MemberCare Organizations and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Organizations and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - MemberCare Organizations Property
     - MemberCare Companycategories Property
     - MemberCare Data Type

