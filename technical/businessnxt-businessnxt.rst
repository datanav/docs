=====================================
Business Nxt to Business Nxt Dataflow
=====================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Nxt Currency to Business Nxt Country
---------------------------------------------
Every Business Nxt Currency will be synchronized with a Business Nxt Country.

Once a link between a Business Nxt Currency and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Currency and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - Business Nxt Currency Property
     - Business Nxt Country Property
     - Business Nxt Data Type
   * - isoCode
     - isoCode
     - "string"
   * - name
     - name
     - "string"


Business Nxt Orderline to Business Nxt Order
--------------------------------------------
Every Business Nxt Orderline will be synchronized with a Business Nxt Order.

Once a link between a Business Nxt Orderline and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Orderline and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Business Nxt Orderline Property
     - Business Nxt Order Property
     - Business Nxt Data Type


Business Nxt Productcategory to Business Nxt Country
----------------------------------------------------
Every Business Nxt Productcategory will be synchronized with a Business Nxt Country.

Once a link between a Business Nxt Productcategory and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Productcategory and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - Business Nxt Productcategory Property
     - Business Nxt Country Property
     - Business Nxt Data Type
   * - text
     - name
     - "string"


Business Nxt Vat to Business Nxt Country
----------------------------------------
Every Business Nxt Vat will be synchronized with a Business Nxt Country.

Once a link between a Business Nxt Vat and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Vat and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - Business Nxt Vat Property
     - Business Nxt Country Property
     - Business Nxt Data Type


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

