============================
SuperOffice to Wave Dataflow
============================

Generated: 2023-06-22 14:18:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Pricelist to Wave Currency
--------------------------------------
Before any synchronization can take place, a link between a SuperOffice Pricelist and a Wave Currency must be established.

A SuperOffice Pricelist will merge with a Wave Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - Wave Currency Property
   * - Currency
     - code

Once a link between a SuperOffice Pricelist and a Wave Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Pricelist and a Wave Currency:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - Wave Currency Property
     - Wave Data Type
   * - Name
     - name
     - "string"


SuperOffice Listcurrencyitems to Wave Currency
----------------------------------------------
Every SuperOffice Listcurrencyitems will be synchronized with a Wave Currency.

If a matching Wave Currency already exists, the SuperOffice Listcurrencyitems will be merged with the existing one.
If no matching Wave Currency is found, a new Wave Currency will be created.

A SuperOffice Listcurrencyitems will merge with a Wave Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - Wave Currency Property
   * - Name
     - code

Once a link between a SuperOffice Listcurrencyitems and a Wave Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a Wave Currency:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - Wave Currency Property
     - Wave Data Type


SuperOffice Product to Wave Product
-----------------------------------
Every SuperOffice Product will be synchronized with a Wave Product.

Once a link between a SuperOffice Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Wave Product Property
     - Wave Data Type
   * - Description
     - description
     - "string"
   * - Name
     - name
     - "string"
   * - UnitListPrice
     - unitPrice
     - "string"

