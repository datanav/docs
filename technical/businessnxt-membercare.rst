==================================
BusinessNxt to MemberCare Dataflow
==================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessNxt Country to MemberCare Companycategories
---------------------------------------------------
Every BusinessNxt Country will be synchronized with a MemberCare Companycategories.

Once a link between a BusinessNxt Country and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Country and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Country Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


BusinessNxt Currency to MemberCare Companycategories
----------------------------------------------------
Every BusinessNxt Currency will be synchronized with a MemberCare Companycategories.

Once a link between a BusinessNxt Currency and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Currency and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Currency Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


BusinessNxt Order to MemberCare Invoices
----------------------------------------
Every BusinessNxt Order will be synchronized with a MemberCare Invoices.

Once a link between a BusinessNxt Order and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Order and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Order Property
     - MemberCare Invoices Property
     - MemberCare Data Type


BusinessNxt Orderline to MemberCare Invoices
--------------------------------------------
Every BusinessNxt Orderline will be synchronized with a MemberCare Invoices.

Once a link between a BusinessNxt Orderline and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Orderline and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Orderline Property
     - MemberCare Invoices Property
     - MemberCare Data Type


BusinessNxt Product to MemberCare Products
------------------------------------------
Every BusinessNxt Product will be synchronized with a MemberCare Products.

Once a link between a BusinessNxt Product and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Product and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Product Property
     - MemberCare Products Property
     - MemberCare Data Type


BusinessNxt Productcategory to MemberCare Companycategories
-----------------------------------------------------------
Every BusinessNxt Productcategory will be synchronized with a MemberCare Companycategories.

Once a link between a BusinessNxt Productcategory and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Productcategory and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Productcategory Property
     - MemberCare Companycategories Property
     - MemberCare Data Type
   * - description
     - description
     - "string"


BusinessNxt Vat to MemberCare Companycategories
-----------------------------------------------
Every BusinessNxt Vat will be synchronized with a MemberCare Companycategories.

Once a link between a BusinessNxt Vat and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Vat and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Vat Property
     - MemberCare Companycategories Property
     - MemberCare Data Type
   * - description
     - description
     - "string"


BusinessNxt Address to MemberCare Companies
-------------------------------------------
Every BusinessNxt Address will be synchronized with a MemberCare Companies.

Once a link between a BusinessNxt Address and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Address and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Address Property
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


BusinessNxt Company to MemberCare Companies
-------------------------------------------
Every BusinessNxt Company will be synchronized with a MemberCare Companies.

Once a link between a BusinessNxt Company and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Company and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Company Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - companyNo
     - addresses.id
     - "string"
   * - name
     - companyName
     - "string"


BusinessNxt Country to MemberCare Countries
-------------------------------------------
Every BusinessNxt Country will be synchronized with a MemberCare Countries.

Once a link between a BusinessNxt Country and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Country and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Country Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - isoCode
     - iso2Letter
     - "string"
   * - name
     - name
     - "string"

