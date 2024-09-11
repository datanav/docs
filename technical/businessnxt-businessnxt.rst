=====================================
Business Nxt to Business Nxt Dataflow
=====================================

Generated: 2024-09-11 11:41:16

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessNxt Currency to BusinessNxt Country
-------------------------------------------
Every BusinessNxt Currency will be synchronized with a BusinessNxt Country.

Once a link between a BusinessNxt Currency and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Currency and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Currency Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - isoCode
     - isoCode
     - "string"
   * - name
     - name
     - "string"


BusinessNxt Orderline to BusinessNxt Order
------------------------------------------
Every BusinessNxt Orderline will be synchronized with a BusinessNxt Order.

Once a link between a BusinessNxt Orderline and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Orderline and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Orderline Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type


BusinessNxt Productcategory to BusinessNxt Country
--------------------------------------------------
Every BusinessNxt Productcategory will be synchronized with a BusinessNxt Country.

Once a link between a BusinessNxt Productcategory and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Productcategory and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Productcategory Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - text
     - name
     - "string"


BusinessNxt Vat to BusinessNxt Country
--------------------------------------
Every BusinessNxt Vat will be synchronized with a BusinessNxt Country.

Once a link between a BusinessNxt Vat and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Vat and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Vat Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type


Business Nxt Address to Business Nxt Company
--------------------------------------------
Every Business Nxt Address will be synchronized with a Business Nxt Company.

Once a link between a Business Nxt Address and a Business Nxt Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Address and a Business Nxt Company:

.. list-table::
   :header-rows: 1

   * - Business Nxt Address Property
     - Business Nxt Company Property
     - Business Nxt Data Type
   * - addressNo
     - companyNo
     - "string"
   * - name
     - name
     - "string"


Business Nxt Company to Business Nxt Address
--------------------------------------------
Every Business Nxt Company will be synchronized with a Business Nxt Address.

Once a link between a Business Nxt Company and a Business Nxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Company and a Business Nxt Address:

.. list-table::
   :header-rows: 1

   * - Business Nxt Company Property
     - Business Nxt Address Property
     - Business Nxt Data Type
   * - companyNo
     - addressNo
     - "string"
   * - name
     - name
     - "string"

