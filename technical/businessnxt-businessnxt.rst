===================================
Businessnxt to Businessnxt Dataflow
===================================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businessnxt to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Currency to Businessnxt Country
-------------------------------------------
Every Businessnxt Currency will be synchronized with a Businessnxt Country.

Once a link between a Businessnxt Currency and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Currency and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Businessnxt Currency Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - isoCode
     - isoCode
     - "string"
   * - name
     - name
     - "string"


Businessnxt Orderline to Businessnxt Order
------------------------------------------
Every Businessnxt Orderline will be synchronized with a Businessnxt Order.

Once a link between a Businessnxt Orderline and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Orderline and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Businessnxt Orderline Property
     - Businessnxt Order Property
     - Businessnxt Data Type


Businessnxt Productcategory to Businessnxt Country
--------------------------------------------------
Every Businessnxt Productcategory will be synchronized with a Businessnxt Country.

Once a link between a Businessnxt Productcategory and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Productcategory and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Businessnxt Productcategory Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - text
     - name
     - "string"


Businessnxt Vat to Businessnxt Country
--------------------------------------
Every Businessnxt Vat will be synchronized with a Businessnxt Country.

Once a link between a Businessnxt Vat and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Vat and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Businessnxt Vat Property
     - Businessnxt Country Property
     - Businessnxt Data Type


Businessnxt Address to Businessnxt Company
------------------------------------------
Every Businessnxt Address will be synchronized with a Businessnxt Company.

Once a link between a Businessnxt Address and a Businessnxt Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Address and a Businessnxt Company:

.. list-table::
   :header-rows: 1

   * - Businessnxt Address Property
     - Businessnxt Company Property
     - Businessnxt Data Type
   * - addressNo
     - companyNo
     - "string"
   * - name
     - name
     - "string"


Businessnxt Company to Businessnxt Address
------------------------------------------
Every Businessnxt Company will be synchronized with a Businessnxt Address.

Once a link between a Businessnxt Company and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Company and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Businessnxt Company Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - companyNo
     - addressNo
     - "string"
   * - name
     - name
     - "string"

