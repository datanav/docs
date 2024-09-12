===================================
Business Nxt to MemberCare Dataflow
===================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Nxt Country to MemberCare Companycategories
----------------------------------------------------
Every Business Nxt Country will be synchronized with a MemberCare Companycategories.

Once a link between a Business Nxt Country and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Country and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - Business Nxt Country Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


Business Nxt Currency to MemberCare Companycategories
-----------------------------------------------------
Every Business Nxt Currency will be synchronized with a MemberCare Companycategories.

Once a link between a Business Nxt Currency and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Currency and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - Business Nxt Currency Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


Business Nxt Order to MemberCare Invoices
-----------------------------------------
Every Business Nxt Order will be synchronized with a MemberCare Invoices.

Once a link between a Business Nxt Order and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Order and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Business Nxt Order Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Business Nxt Orderline to MemberCare Invoices
---------------------------------------------
Every Business Nxt Orderline will be synchronized with a MemberCare Invoices.

Once a link between a Business Nxt Orderline and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Orderline and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Business Nxt Orderline Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Business Nxt Product to MemberCare Products
-------------------------------------------
Every Business Nxt Product will be synchronized with a MemberCare Products.

Once a link between a Business Nxt Product and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Product and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - Business Nxt Product Property
     - MemberCare Products Property
     - MemberCare Data Type


Business Nxt Productcategory to MemberCare Companycategories
------------------------------------------------------------
Every Business Nxt Productcategory will be synchronized with a MemberCare Companycategories.

Once a link between a Business Nxt Productcategory and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Productcategory and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - Business Nxt Productcategory Property
     - MemberCare Companycategories Property
     - MemberCare Data Type
   * - description
     - description
     - "string"


Business Nxt Vat to MemberCare Companycategories
------------------------------------------------
Every Business Nxt Vat will be synchronized with a MemberCare Companycategories.

Once a link between a Business Nxt Vat and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Vat and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - Business Nxt Vat Property
     - MemberCare Companycategories Property
     - MemberCare Data Type
   * - description
     - description
     - "string"


Business Nxt Address to MemberCare Companies
--------------------------------------------
Every Business Nxt Address will be synchronized with a MemberCare Companies.

Once a link between a Business Nxt Address and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Address and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Business Nxt Address Property
     - MemberCare Companies Property
     - MemberCare Data Type
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


Business Nxt Company to MemberCare Companies
--------------------------------------------
Every Business Nxt Company will be synchronized with a MemberCare Companies.

Once a link between a Business Nxt Company and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Company and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Business Nxt Company Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - companyNo
     - addresses.id
     - "string"
   * - name
     - companyName
     - "string"


Business Nxt Country to MemberCare Countries
--------------------------------------------
Every Business Nxt Country will be synchronized with a MemberCare Countries.

Once a link between a Business Nxt Country and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Country and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Business Nxt Country Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - isoCode
     - iso2Letter
     - "string"
   * - name
     - name
     - "string"

