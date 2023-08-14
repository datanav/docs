========================================
Wave Financial to PowerOfficeGo Dataflow
========================================

Generated: 2023-08-14 10:19:53

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to PowerOfficeGo Address
--------------------------------------
Every Wave Customer will be synchronized with a PowerOfficeGo Address.

Once a link between a Wave Customer and a PowerOfficeGo Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOfficeGo Address:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOfficeGo Address Property
     - PowerOfficeGo Data Type
   * - address.addressLine1
     - address1
     - "string"
   * - address.addressLine2
     - address2
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.code
     - countryCode
     - "string"
   * - address.postalCode
     - zipCode
     - "string"


Wave Invoice to PowerOfficeGo Salesorder
----------------------------------------
Every Wave Invoice will be synchronized with a PowerOfficeGo Salesorder.

Once a link between a Wave Invoice and a PowerOfficeGo Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a PowerOfficeGo Salesorder:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - PowerOfficeGo Salesorder Property
     - PowerOfficeGo Data Type
   * - currency.code
     - Currency
     - "string"
   * - customer.id
     - DepartmentCode
     - "string"


Wave Product to PowerOfficeGo Product
-------------------------------------
Every Wave Product will be synchronized with a PowerOfficeGo Product.

Once a link between a Wave Product and a PowerOfficeGo Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a PowerOfficeGo Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - PowerOfficeGo Product Property
     - PowerOfficeGo Data Type
   * - description
     - Description
     - "string"
   * - description
     - description
     - "string"
   * - modifiedAt
     - LastChanged
     - "string"
   * - modifiedAt
     - lastChanged
     - "string"
   * - name
     - Name
     - "string"
   * - name
     - name
     - "string"
   * - unitPrice
     - SalesPrice
     - "string"
   * - unitPrice
     - salesPrice
     - "string"


Wave Vendor to PowerOfficeGo Address
------------------------------------
Every Wave Vendor will be synchronized with a PowerOfficeGo Address.

Once a link between a Wave Vendor and a PowerOfficeGo Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGo Address:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGo Address Property
     - PowerOfficeGo Data Type
   * - address.addressLine1
     - address1
     - "string"
   * - address.addressLine2
     - address2
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.code
     - countryCode
     - "string"
   * - address.postalCode
     - zipCode
     - "string"


Wave Vendor to PowerOfficeGo Suppliers
--------------------------------------
Every Wave Vendor will be synchronized with a PowerOfficeGo Suppliers.

Once a link between a Wave Vendor and a PowerOfficeGo Suppliers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOfficeGo Suppliers:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOfficeGo Suppliers Property
     - PowerOfficeGo Data Type

