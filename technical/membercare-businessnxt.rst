==================================
MemberCare to BusinessNxt Dataflow
==================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Companycategories to Businessnxt Country
---------------------------------------------------
Every MemberCare Companycategories will be synchronized with a Businessnxt Country.

Once a link between a MemberCare Companycategories and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companycategories and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - MemberCare Companycategories Property
     - Businessnxt Country Property
     - Businessnxt Data Type


MemberCare Invoices to Businessnxt Order
----------------------------------------
Every MemberCare Invoices will be synchronized with a Businessnxt Order.

Once a link between a MemberCare Invoices and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - Businessnxt Order Property
     - Businessnxt Data Type


MemberCare Organizations to Businessnxt Address
-----------------------------------------------
Every MemberCare Organizations will be synchronized with a Businessnxt Address.

Once a link between a MemberCare Organizations and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Organizations and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - MemberCare Organizations Property
     - Businessnxt Address Property
     - Businessnxt Data Type
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


MemberCare Products to Businessnxt Product
------------------------------------------
Every MemberCare Products will be synchronized with a Businessnxt Product.

Once a link between a MemberCare Products and a Businessnxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Products and a Businessnxt Product:

.. list-table::
   :header-rows: 1

   * - MemberCare Products Property
     - Businessnxt Product Property
     - Businessnxt Data Type


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

