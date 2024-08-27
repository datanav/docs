========================
SuperOffice to  Dataflow
========================

Generated: 2024-08-27 09:38:16

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to  Address
-------------------------------
Every SuperOffice Contact will be synchronized with a  Address.

Once a link between a SuperOffice Contact and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Address:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Address Property
     -  Data Type
   * - Name
     - name
     - "string"
   * - Phones.Value
     - phone
     - "string"


SuperOffice Contact to  Company
-------------------------------
Every SuperOffice Contact will be synchronized with a  Company.

Once a link between a SuperOffice Contact and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Company:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Company Property
     -  Data Type
   * - Country.ThreeLetterISOCountry
     - companyBusinessNo (Dependant on having wd:Q906278 in countryIsoCode)
     - "string"
   * - Name
     - name
     - "string"
   * - OrgNr
     - companyBusinessNo (Dependant on having  in countryIsoCode)
     - "string"


SuperOffice Listcountryitems to  Country
----------------------------------------
Every SuperOffice Listcountryitems will be synchronized with a  Country.

Once a link between a SuperOffice Listcountryitems and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcountryitems and a  Country:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcountryitems Property
     -  Country Property
     -  Data Type
   * - Name
     - name
     - "string"
   * - TwoLetterISOCountry
     - isoCode
     - "string"


SuperOffice Listcurrencyitems to  Currency
------------------------------------------
Every SuperOffice Listcurrencyitems will be synchronized with a  Currency.

Once a link between a SuperOffice Listcurrencyitems and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a  Currency:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     -  Currency Property
     -  Data Type
   * - Name
     - isoCode
     - "string"


SuperOffice Product to  Product
-------------------------------
Every SuperOffice Product will be synchronized with a  Product.

Once a link between a SuperOffice Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a  Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     -  Product Property
     -  Data Type
   * - Description
     - description
     - "string"
   * - UnitListPrice
     - priceQuantity
     - "string"
   * - Url
     - webPage
     - "string"

