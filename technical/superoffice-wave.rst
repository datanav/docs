============================
SuperOffice to Wave Dataflow
============================

Generated: 2023-08-17 09:33:39

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Wave Customer
------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Wave Customer must be established.

A new Wave Customer will be created from a SuperOffice Contact if it is connected to a SuperOffice Sale, Quote, Quoteline, or Quotealternative that is synchronized into Wave.

Once a link between a SuperOffice Contact and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Wave Customer Property
     - Wave Data Type
   * - Address.Postal.Address1
     - shippingDetails.address.addressLine1
     - "string"
   * - Address.Postal.Address2
     - shippingDetails.address.addressLine2
     - "string"
   * - Address.Postal.City
     - shippingDetails.address.city
     - "string"
   * - Address.Postal.Zipcode
     - shippingDetails.address.postalCode
     - "string"
   * - Address.Street.Address1
     - address.addressLine1
     - "string"
   * - Address.Street.Address1
     - shippingDetails.address.addressLine1
     - "string"
   * - Address.Street.Address2
     - address.addressLine2
     - "string"
   * - Address.Street.Address2
     - shippingDetails.address.addressLine2
     - "string"
   * - Address.Street.City
     - shippingDetails.address.city
     - "string"
   * - Address.Street.Zipcode
     - shippingDetails.address.postalCode
     - "string"
   * - Country.CountryId
     - shippingDetails.address.country.code
     - "string"
   * - Domains
     - website
     - "string"
   * - Phones.Value
     - phone
     - "string"
   * - Phones.Value
     - shippingDetails.phone
     - "string"


SuperOffice Quotealternative to Wave Invoice
--------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a Wave Invoice must be established.

A new Wave Invoice will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Sale, Quote, Quoteline, or Quotealternative that is synchronized into Wave.

Once a link between a SuperOffice Quotealternative and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Wave Invoice Property
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

