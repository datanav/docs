=========================================
Visma Business Nxt to MemberCare Dataflow
=========================================

Generated: 2024-09-11 08:07:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Visma Business Nxt to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Visma Country to Membercare Companycategories
---------------------------------------------
Every Visma Country will be synchronized with a Membercare Companycategories.

Once a link between a Visma Country and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Country and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - Visma Country Property
     - Membercare Companycategories Property
     - Membercare Data Type


Visma Currency to Membercare Companycategories
----------------------------------------------
Every Visma Currency will be synchronized with a Membercare Companycategories.

Once a link between a Visma Currency and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Currency and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - Visma Currency Property
     - Membercare Companycategories Property
     - Membercare Data Type


Visma Order to Membercare Invoices
----------------------------------
Every Visma Order will be synchronized with a Membercare Invoices.

Once a link between a Visma Order and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Order and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Visma Order Property
     - Membercare Invoices Property
     - Membercare Data Type


Visma Orderline to Membercare Invoices
--------------------------------------
Every Visma Orderline will be synchronized with a Membercare Invoices.

Once a link between a Visma Orderline and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Orderline and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Visma Orderline Property
     - Membercare Invoices Property
     - Membercare Data Type


Visma Product to Membercare Products
------------------------------------
Every Visma Product will be synchronized with a Membercare Products.

Once a link between a Visma Product and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Product and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Visma Product Property
     - Membercare Products Property
     - Membercare Data Type


Visma Productcategory to Membercare Companycategories
-----------------------------------------------------
Every Visma Productcategory will be synchronized with a Membercare Companycategories.

Once a link between a Visma Productcategory and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Productcategory and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - Visma Productcategory Property
     - Membercare Companycategories Property
     - Membercare Data Type
   * - description
     - description
     - "string"


Visma Vat to Membercare Companycategories
-----------------------------------------
Every Visma Vat will be synchronized with a Membercare Companycategories.

Once a link between a Visma Vat and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Vat and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - Visma Vat Property
     - Membercare Companycategories Property
     - Membercare Data Type
   * - description
     - description
     - "string"


Visma Address to MemberCare Companies
-------------------------------------
Every Visma Address will be synchronized with a MemberCare Companies.

Once a link between a Visma Address and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Address and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Visma Address Property
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


Visma Company to MemberCare Companies
-------------------------------------
Every Visma Company will be synchronized with a MemberCare Companies.

Once a link between a Visma Company and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Company and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Visma Company Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - companyNo
     - addresses.id
     - "string"
   * - name
     - companyName
     - "string"


Visma Country to MemberCare Countries
-------------------------------------
Every Visma Country will be synchronized with a MemberCare Countries.

Once a link between a Visma Country and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Country and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Visma Country Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - isoCode
     - iso2Letter
     - "string"
   * - name
     - name
     - "string"

