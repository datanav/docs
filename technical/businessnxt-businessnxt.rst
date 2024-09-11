===================================
BusinessNxt to BusinessNxt Dataflow
===================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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

