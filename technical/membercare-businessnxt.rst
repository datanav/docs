==================================
MemberCare to BusinessNxt Dataflow
==================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Companycategories to Visma Country
---------------------------------------------
Every MemberCare Companycategories will be synchronized with a Visma Country.

Once a link between a MemberCare Companycategories and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companycategories and a Visma Country:

.. list-table::
   :header-rows: 1

   * - MemberCare Companycategories Property
     - Visma Country Property
     - Visma Data Type


MemberCare Invoices to Visma Order
----------------------------------
Every MemberCare Invoices will be synchronized with a Visma Order.

Once a link between a MemberCare Invoices and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a Visma Order:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - Visma Order Property
     - Visma Data Type


MemberCare Organizations to Visma Address
-----------------------------------------
Every MemberCare Organizations will be synchronized with a Visma Address.

Once a link between a MemberCare Organizations and a Visma Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Organizations and a Visma Address:

.. list-table::
   :header-rows: 1

   * - MemberCare Organizations Property
     - Visma Address Property
     - Visma Data Type
   * - addresses.country.id
     - countryNo
     - "string"
   * - addresses.id
     - addressNo
     - "string"
   * - addresses.postalCode.city
     - postalArea
     - "string"
   * - addresses.postalCode.zipCode
     - postCode
     - "string"
   * - company.addresses.addressDescription
     - countryNo
     - "string"
   * - company.addresses.id
     - addressNo
     - "string"
   * - company.addresses.municipality
     - postCode
     - "string"
   * - company.addresses.start
     - postalArea
     - "string"
   * - company.addresses.street
     - addressLine1
     - "string"
   * - name
     - name
     - "string"


MemberCare Products to Visma Product
------------------------------------
Every MemberCare Products will be synchronized with a Visma Product.

Once a link between a MemberCare Products and a Visma Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Products and a Visma Product:

.. list-table::
   :header-rows: 1

   * - MemberCare Products Property
     - Visma Product Property
     - Visma Data Type


MemberCare Companies to BusinessNxt Address
-------------------------------------------
Every MemberCare Companies will be synchronized with a BusinessNxt Address.

Once a link between a MemberCare Companies and a BusinessNxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a BusinessNxt Address:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - BusinessNxt Address Property
     - BusinessNxt Data Type
   * - addresses.country.id
     - countryNo
     - "string"
   * - addresses.id
     - addressNo
     - "string"
   * - addresses.postalCode.city
     - postalArea
     - "string"
   * - addresses.postalCode.zipCode
     - postCode
     - "string"
   * - addresses.street
     - addressLine1
     - "string"
   * - companyName
     - name
     - "string"


MemberCare Companies to BusinessNxt Company
-------------------------------------------
Every MemberCare Companies will be synchronized with a BusinessNxt Company.

Once a link between a MemberCare Companies and a BusinessNxt Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a BusinessNxt Company:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - BusinessNxt Company Property
     - BusinessNxt Data Type
   * - addresses.id
     - companyNo
     - "string"
   * - companyName
     - name
     - "string"


MemberCare Countries to BusinessNxt Country
-------------------------------------------
Every MemberCare Countries will be synchronized with a BusinessNxt Country.

Once a link between a MemberCare Countries and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Countries and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - MemberCare Countries Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - iso2Letter
     - isoCode
     - "string"
   * - name
     - name
     - "string"


MemberCare Invoices to BusinessNxt Orderline
--------------------------------------------
Every MemberCare Invoices will be synchronized with a BusinessNxt Orderline.

Once a link between a MemberCare Invoices and a BusinessNxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a BusinessNxt Orderline:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - BusinessNxt Orderline Property
     - BusinessNxt Data Type

