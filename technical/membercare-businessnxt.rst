==================================
Membercare to Businessnxt Dataflow
==================================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Membercare Companies to Businessnxt Address
-------------------------------------------
Every Membercare Companies will be synchronized with a Businessnxt Address.

Once a link between a Membercare Companies and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
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
   * - addresses.street
     - addressLine1
     - "string"
   * - companyName
     - name
     - "string"


Membercare Companies to Businessnxt Company
-------------------------------------------
Every Membercare Companies will be synchronized with a Businessnxt Company.

Once a link between a Membercare Companies and a Businessnxt Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Businessnxt Company:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Businessnxt Company Property
     - Businessnxt Data Type
   * - addresses.id
     - companyNo
     - "string"
   * - companyName
     - name
     - "string"


Membercare Countries to Businessnxt Country
-------------------------------------------
Every Membercare Countries will be synchronized with a Businessnxt Country.

Once a link between a Membercare Countries and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Countries and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Membercare Countries Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - iso2Letter
     - isoCode
     - "string"
   * - name
     - name
     - "string"


Membercare Invoices to Businessnxt Orderline
--------------------------------------------
Every Membercare Invoices will be synchronized with a Businessnxt Orderline.

Once a link between a Membercare Invoices and a Businessnxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Invoices and a Businessnxt Orderline:

.. list-table::
   :header-rows: 1

   * - Membercare Invoices Property
     - Businessnxt Orderline Property
     - Businessnxt Data Type

