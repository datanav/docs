===================================
MemberCare to Business Nxt Dataflow
===================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Companycategories to Business Nxt Country
----------------------------------------------------
Every MemberCare Companycategories will be synchronized with a Business Nxt Country.

Once a link between a MemberCare Companycategories and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companycategories and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - MemberCare Companycategories Property
     - Business Nxt Country Property
     - Business Nxt Data Type


MemberCare Invoices to Business Nxt Order
-----------------------------------------
Every MemberCare Invoices will be synchronized with a Business Nxt Order.

Once a link between a MemberCare Invoices and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - Business Nxt Order Property
     - Business Nxt Data Type


MemberCare Organizations to Business Nxt Address
------------------------------------------------
Every MemberCare Organizations will be synchronized with a Business Nxt Address.

Once a link between a MemberCare Organizations and a Business Nxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Organizations and a Business Nxt Address:

.. list-table::
   :header-rows: 1

   * - MemberCare Organizations Property
     - Business Nxt Address Property
     - Business Nxt Data Type
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


MemberCare Products to Business Nxt Product
-------------------------------------------
Every MemberCare Products will be synchronized with a Business Nxt Product.

Once a link between a MemberCare Products and a Business Nxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Products and a Business Nxt Product:

.. list-table::
   :header-rows: 1

   * - MemberCare Products Property
     - Business Nxt Product Property
     - Business Nxt Data Type


MemberCare Companies to Business Nxt Address
--------------------------------------------
Every MemberCare Companies will be synchronized with a Business Nxt Address.

Once a link between a MemberCare Companies and a Business Nxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a Business Nxt Address:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - Business Nxt Address Property
     - Business Nxt Data Type
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


MemberCare Companies to Business Nxt Company
--------------------------------------------
Every MemberCare Companies will be synchronized with a Business Nxt Company.

Once a link between a MemberCare Companies and a Business Nxt Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a Business Nxt Company:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - Business Nxt Company Property
     - Business Nxt Data Type
   * - addresses.id
     - companyNo
     - "string"
   * - companyName
     - name
     - "string"


MemberCare Countries to Business Nxt Country
--------------------------------------------
Every MemberCare Countries will be synchronized with a Business Nxt Country.

Once a link between a MemberCare Countries and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Countries and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - MemberCare Countries Property
     - Business Nxt Country Property
     - Business Nxt Data Type
   * - iso2Letter
     - isoCode
     - "string"
   * - name
     - name
     - "string"


MemberCare Invoices to Business Nxt Orderline
---------------------------------------------
Every MemberCare Invoices will be synchronized with a Business Nxt Orderline.

Once a link between a MemberCare Invoices and a Business Nxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a Business Nxt Orderline:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - Business Nxt Orderline Property
     - Business Nxt Data Type

