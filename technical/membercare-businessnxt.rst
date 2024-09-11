=========================================
MemberCare to Visma Business Nxt Dataflow
=========================================

Generated: 2024-09-11 07:48:17

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to Visma Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Companycategories to Businessnxt Country
---------------------------------------------------
Every Membercare Companycategories will be synchronized with a Businessnxt Country.

Once a link between a Membercare Companycategories and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companycategories and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Membercare Companycategories Property
     - Businessnxt Country Property
     - Businessnxt Data Type


Membercare Invoices to Businessnxt Order
----------------------------------------
Every Membercare Invoices will be synchronized with a Businessnxt Order.

Once a link between a Membercare Invoices and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Invoices and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Membercare Invoices Property
     - Businessnxt Order Property
     - Businessnxt Data Type


Membercare Organizations to Businessnxt Address
-----------------------------------------------
Every Membercare Organizations will be synchronized with a Businessnxt Address.

Once a link between a Membercare Organizations and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Organizations and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Membercare Organizations Property
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


Membercare Products to Businessnxt Product
------------------------------------------
Every Membercare Products will be synchronized with a Businessnxt Product.

Once a link between a Membercare Products and a Businessnxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Products and a Businessnxt Product:

.. list-table::
   :header-rows: 1

   * - Membercare Products Property
     - Businessnxt Product Property
     - Businessnxt Data Type


MemberCare Companies to Visma Address
-------------------------------------
Every MemberCare Companies will be synchronized with a Visma Address.

Once a link between a MemberCare Companies and a Visma Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a Visma Address:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
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
   * - addresses.street
     - addressLine1
     - "string"
   * - companyName
     - name
     - "string"


MemberCare Companies to Visma Company
-------------------------------------
Every MemberCare Companies will be synchronized with a Visma Company.

Once a link between a MemberCare Companies and a Visma Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a Visma Company:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - Visma Company Property
     - Visma Data Type
   * - addresses.id
     - companyNo
     - "string"
   * - companyName
     - name
     - "string"


MemberCare Countries to Visma Country
-------------------------------------
Every MemberCare Countries will be synchronized with a Visma Country.

Once a link between a MemberCare Countries and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Countries and a Visma Country:

.. list-table::
   :header-rows: 1

   * - MemberCare Countries Property
     - Visma Country Property
     - Visma Data Type
   * - iso2Letter
     - isoCode
     - "string"
   * - name
     - name
     - "string"


MemberCare Invoices to Visma Orderline
--------------------------------------
Every MemberCare Invoices will be synchronized with a Visma Orderline.

Once a link between a MemberCare Invoices and a Visma Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a Visma Orderline:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - Visma Orderline Property
     - Visma Data Type

