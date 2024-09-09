==================================
Salesforce to Businessnxt Dataflow
==================================

Generated: 2024-09-09 08:58:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Currencytype to Businessnxt Country
----------------------------------------------
Every Salesforce Currencytype will be synchronized with a Businessnxt Country.

Once a link between a Salesforce Currencytype and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - Businessnxt Country Property
     - Businessnxt Data Type


Salesforce Division to Businessnxt Address
------------------------------------------
Every Salesforce Division will be synchronized with a Businessnxt Address.

Once a link between a Salesforce Division and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - Name
     - name
     - "string"


Salesforce Invoice to Businessnxt Order
---------------------------------------
Every Salesforce Invoice will be synchronized with a Businessnxt Order.

Once a link between a Salesforce Invoice and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoice and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoice Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - FullSettlementDate
     - dueDate
     - "string"
   * - InvoiceDate
     - invoiceDate
     - "string"
   * - PostedDate
     - invoiceDate
     - "string"


Salesforce Invoiceline to Businessnxt Order
-------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Businessnxt Order.

Once a link between a Salesforce Invoiceline and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Businessnxt Order Property
     - Businessnxt Data Type


Salesforce Orderitem to Businessnxt Order
-----------------------------------------
Every Salesforce Orderitem will be synchronized with a Businessnxt Order.

Once a link between a Salesforce Orderitem and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Businessnxt Order Property
     - Businessnxt Data Type


Salesforce Contact to Businessnxt Country
-----------------------------------------
Every Salesforce Contact will be synchronized with a Businessnxt Country.

Once a link between a Salesforce Contact and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - MailingCountry
     - name
     - "string"


Salesforce Currencytype to Businessnxt Currency
-----------------------------------------------
Every Salesforce Currencytype will be synchronized with a Businessnxt Currency.

Once a link between a Salesforce Currencytype and a Businessnxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a Businessnxt Currency:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - Businessnxt Currency Property
     - Businessnxt Data Type


Salesforce Invoiceline to Businessnxt Orderline
-----------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Businessnxt Orderline.

Once a link between a Salesforce Invoiceline and a Businessnxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Businessnxt Orderline:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Businessnxt Orderline Property
     - Businessnxt Data Type


Salesforce Order to Businessnxt Country
---------------------------------------
Every Salesforce Order will be synchronized with a Businessnxt Country.

Once a link between a Salesforce Order and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - BillingCountry
     - name
     - "string"
   * - BillingCountryCode
     - isoCode
     - "string"
   * - ShippingCountry
     - name
     - "string"
   * - ShippingCountryCode
     - isoCode
     - "string"


Salesforce Order to Businessnxt Order
-------------------------------------
Every Salesforce Order will be synchronized with a Businessnxt Order.

Once a link between a Salesforce Order and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - EffectiveDate
     - dueDate
     - "string"
   * - EffectiveDate
     - orderDate
     - "string"
   * - EndDate
     - dueDate
     - "string"
   * - EndDate
     - settlementDate
     - "string"
   * - Name
     - name
     - "string"
   * - OrderedDate
     - orderDate
     - "string"


Salesforce Orderitem to Businessnxt Orderline
---------------------------------------------
Every Salesforce Orderitem will be synchronized with a Businessnxt Orderline.

Once a link between a Salesforce Orderitem and a Businessnxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Businessnxt Orderline:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Businessnxt Orderline Property
     - Businessnxt Data Type
   * - OrderId
     - orderNo
     - "string"


Salesforce Organization to Businessnxt Address
----------------------------------------------
Every Salesforce Organization will be synchronized with a Businessnxt Address.

Once a link between a Salesforce Organization and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - City
     - postalArea
     - "string"
   * - Country
     - countryNo
     - "string"
   * - Fax	
     - fax
     - "string"
   * - Name	
     - name
     - "string"
   * - Phone	
     - phone
     - "string"
   * - PostalCode	
     - postCode
     - "string"


Salesforce Organization to Businessnxt Company
----------------------------------------------
Every Salesforce Organization will be synchronized with a Businessnxt Company.

Once a link between a Salesforce Organization and a Businessnxt Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Businessnxt Company:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Businessnxt Company Property
     - Businessnxt Data Type
   * - Name	
     - name
     - "string"


Salesforce Product2 to Businessnxt Product
------------------------------------------
Every Salesforce Product2 will be synchronized with a Businessnxt Product.

Once a link between a Salesforce Product2 and a Businessnxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Businessnxt Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Businessnxt Product Property
     - Businessnxt Data Type
   * - Description	
     - description
     - "string"
   * - DisplayUrl	
     - webPage
     - "string"


Salesforce Quote to Businessnxt Country
---------------------------------------
Every Salesforce Quote will be synchronized with a Businessnxt Country.

Once a link between a Salesforce Quote and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - BillingCountry
     - name
     - "string"
   * - BillingCountryCode
     - isoCode
     - "string"
   * - ShippingCountry
     - name
     - "string"
   * - ShippingCountryCode
     - isoCode
     - "string"

