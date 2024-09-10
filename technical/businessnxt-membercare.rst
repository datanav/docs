==================================
Businessnxt to Membercare Dataflow
==================================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businessnxt to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Country to Membercare Companycategories
---------------------------------------------------
Every Businessnxt Country will be synchronized with a Membercare Companycategories.

Once a link between a Businessnxt Country and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Country and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - Businessnxt Country Property
     - Membercare Companycategories Property
     - Membercare Data Type


Businessnxt Currency to Membercare Companycategories
----------------------------------------------------
Every Businessnxt Currency will be synchronized with a Membercare Companycategories.

Once a link between a Businessnxt Currency and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Currency and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - Businessnxt Currency Property
     - Membercare Companycategories Property
     - Membercare Data Type


Businessnxt Order to Membercare Invoices
----------------------------------------
Every Businessnxt Order will be synchronized with a Membercare Invoices.

Once a link between a Businessnxt Order and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Order and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Businessnxt Order Property
     - Membercare Invoices Property
     - Membercare Data Type


Businessnxt Orderline to Membercare Invoices
--------------------------------------------
Every Businessnxt Orderline will be synchronized with a Membercare Invoices.

Once a link between a Businessnxt Orderline and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Orderline and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Businessnxt Orderline Property
     - Membercare Invoices Property
     - Membercare Data Type


Businessnxt Product to Membercare Products
------------------------------------------
Every Businessnxt Product will be synchronized with a Membercare Products.

Once a link between a Businessnxt Product and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Product and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Businessnxt Product Property
     - Membercare Products Property
     - Membercare Data Type


Businessnxt Productcategory to Membercare Companycategories
-----------------------------------------------------------
Every Businessnxt Productcategory will be synchronized with a Membercare Companycategories.

Once a link between a Businessnxt Productcategory and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Productcategory and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - Businessnxt Productcategory Property
     - Membercare Companycategories Property
     - Membercare Data Type
   * - description
     - description
     - "string"


Businessnxt Vat to Membercare Companycategories
-----------------------------------------------
Every Businessnxt Vat will be synchronized with a Membercare Companycategories.

Once a link between a Businessnxt Vat and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Vat and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - Businessnxt Vat Property
     - Membercare Companycategories Property
     - Membercare Data Type
   * - description
     - description
     - "string"


Businessnxt Address to Membercare Companies
-------------------------------------------
Every Businessnxt Address will be synchronized with a Membercare Companies.

Once a link between a Businessnxt Address and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Address and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Businessnxt Address Property
     - Membercare Companies Property
     - Membercare Data Type
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


Businessnxt Company to Membercare Companies
-------------------------------------------
Every Businessnxt Company will be synchronized with a Membercare Companies.

Once a link between a Businessnxt Company and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Company and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Businessnxt Company Property
     - Membercare Companies Property
     - Membercare Data Type
   * - companyNo
     - addresses.id
     - "string"
   * - name
     - companyName
     - "string"


Businessnxt Country to Membercare Countries
-------------------------------------------
Every Businessnxt Country will be synchronized with a Membercare Countries.

Once a link between a Businessnxt Country and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Country and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Businessnxt Country Property
     - Membercare Countries Property
     - Membercare Data Type
   * - isoCode
     - iso2Letter
     - "string"
   * - name
     - name
     - "string"

