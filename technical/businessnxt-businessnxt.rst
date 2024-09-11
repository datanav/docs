===================================
BusinessNxt to BusinessNxt Dataflow
===================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Visma Currency to Businessnxt Country
-------------------------------------
Every Visma Currency will be synchronized with a Businessnxt Country.

Once a link between a Visma Currency and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Currency and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Visma Currency Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - isoCode
     - isoCode
     - "string"
   * - name
     - name
     - "string"


Visma Orderline to Businessnxt Order
------------------------------------
Every Visma Orderline will be synchronized with a Businessnxt Order.

Once a link between a Visma Orderline and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Orderline and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Visma Orderline Property
     - Businessnxt Order Property
     - Businessnxt Data Type


Visma Productcategory to Businessnxt Country
--------------------------------------------
Every Visma Productcategory will be synchronized with a Businessnxt Country.

Once a link between a Visma Productcategory and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Productcategory and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Visma Productcategory Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - text
     - name
     - "string"


Visma Vat to Businessnxt Country
--------------------------------
Every Visma Vat will be synchronized with a Businessnxt Country.

Once a link between a Visma Vat and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Vat and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Visma Vat Property
     - Businessnxt Country Property
     - Businessnxt Data Type


BusinessNxt Address to BusinessNxt Company
------------------------------------------
Every BusinessNxt Address will be synchronized with a BusinessNxt Company.

Once a link between a BusinessNxt Address and a BusinessNxt Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Address and a BusinessNxt Company:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Address Property
     - BusinessNxt Company Property
     - BusinessNxt Data Type
   * - addressNo
     - companyNo
     - "string"
   * - name
     - name
     - "string"


BusinessNxt Company to BusinessNxt Address
------------------------------------------
Every BusinessNxt Company will be synchronized with a BusinessNxt Address.

Once a link between a BusinessNxt Company and a BusinessNxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Company and a BusinessNxt Address:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Company Property
     - BusinessNxt Address Property
     - BusinessNxt Data Type
   * - companyNo
     - addressNo
     - "string"
   * - name
     - name
     - "string"

