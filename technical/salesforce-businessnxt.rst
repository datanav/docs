===================================
Salesforce to Business Nxt Dataflow
===================================

Generated: 2024-09-12 00:00:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Currencytype to Business Nxt Country
-----------------------------------------------
Every Salesforce Currencytype will be synchronized with a Business Nxt Country.

Once a link between a Salesforce Currencytype and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - Business Nxt Country Property
     - Business Nxt Data Type


Salesforce Division to Business Nxt Address
-------------------------------------------
Every Salesforce Division will be synchronized with a Business Nxt Address.

Once a link between a Salesforce Division and a Business Nxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Business Nxt Address:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Business Nxt Address Property
     - Business Nxt Data Type
   * - Name
     - name
     - "string"


Salesforce Invoice to Business Nxt Order
----------------------------------------
Every Salesforce Invoice will be synchronized with a Business Nxt Order.

Once a link between a Salesforce Invoice and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoice and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoice Property
     - Business Nxt Order Property
     - Business Nxt Data Type
   * - FullSettlementDate
     - dueDate
     - "string"
   * - InvoiceDate
     - invoiceDate
     - "string"
   * - PostedDate
     - invoiceDate
     - "string"


Salesforce Invoiceline to Business Nxt Order
--------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Business Nxt Order.

Once a link between a Salesforce Invoiceline and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Business Nxt Order Property
     - Business Nxt Data Type


Salesforce Orderitem to Business Nxt Order
------------------------------------------
Every Salesforce Orderitem will be synchronized with a Business Nxt Order.

Once a link between a Salesforce Orderitem and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Business Nxt Order Property
     - Business Nxt Data Type


Salesforce Quote to Business Nxt Order
--------------------------------------
Every Salesforce Quote will be synchronized with a Business Nxt Order.

Once a link between a Salesforce Quote and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Business Nxt Order Property
     - Business Nxt Data Type
   * - Discount
     - totalDiscountAmountInCurrency
     - "string"
   * - Name
     - name
     - "string"
   * - Tax
     - taxCode
     - "string"


Salesforce Quotelineitem to Business Nxt Order
----------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Business Nxt Order.

Once a link between a Salesforce Quotelineitem and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Business Nxt Order Property
     - Business Nxt Data Type


Salesforce Contact to Business Nxt Country
------------------------------------------
Every Salesforce Contact will be synchronized with a Business Nxt Country.

Once a link between a Salesforce Contact and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Business Nxt Country Property
     - Business Nxt Data Type
   * - MailingCountry
     - name
     - "string"


Salesforce Currencytype to Business Nxt Currency
------------------------------------------------
Every Salesforce Currencytype will be synchronized with a Business Nxt Currency.

Once a link between a Salesforce Currencytype and a Business Nxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a Business Nxt Currency:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - Business Nxt Currency Property
     - Business Nxt Data Type


Salesforce Invoiceline to Business Nxt Orderline
------------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Business Nxt Orderline.

Once a link between a Salesforce Invoiceline and a Business Nxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Business Nxt Orderline:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Business Nxt Orderline Property
     - Business Nxt Data Type


Salesforce Order to Business Nxt Country
----------------------------------------
Every Salesforce Order will be synchronized with a Business Nxt Country.

Once a link between a Salesforce Order and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Business Nxt Country Property
     - Business Nxt Data Type
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


Salesforce Order to Business Nxt Order
--------------------------------------
Every Salesforce Order will be synchronized with a Business Nxt Order.

Once a link between a Salesforce Order and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Business Nxt Order Property
     - Business Nxt Data Type
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


Salesforce Orderitem to Business Nxt Orderline
----------------------------------------------
Every Salesforce Orderitem will be synchronized with a Business Nxt Orderline.

Once a link between a Salesforce Orderitem and a Business Nxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Business Nxt Orderline:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Business Nxt Orderline Property
     - Business Nxt Data Type
   * - OrderId
     - orderNo
     - "string"


Salesforce Organization to Business Nxt Address
-----------------------------------------------
Every Salesforce Organization will be synchronized with a Business Nxt Address.

Once a link between a Salesforce Organization and a Business Nxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Business Nxt Address:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Business Nxt Address Property
     - Business Nxt Data Type
   * - City
     - postalArea
     - "string"
   * - Country
     - countryNo
     - "string"
   * - Fax
     - fax
     - "string"
   * - Fax	
     - fax
     - "string"
   * - ID
     - addressNo
     - "string"
   * - Name
     - name
     - "string"
   * - Name	
     - name
     - "string"
   * - Phone
     - phone
     - "string"
   * - Phone	
     - phone
     - "string"
   * - PostalCode
     - postCode
     - "string"
   * - PostalCode	
     - postCode
     - "string"
   * - Street
     - addressLine1
     - "string"


Salesforce Organization to Business Nxt Company
-----------------------------------------------
Every Salesforce Organization will be synchronized with a Business Nxt Company.

Once a link between a Salesforce Organization and a Business Nxt Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Business Nxt Company:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Business Nxt Company Property
     - Business Nxt Data Type
   * - ID
     - companyNo
     - "string"
   * - Name
     - name
     - "string"
   * - Name	
     - name
     - "string"


Salesforce Product2 to Business Nxt Product
-------------------------------------------
Every Salesforce Product2 will be synchronized with a Business Nxt Product.

Once a link between a Salesforce Product2 and a Business Nxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Business Nxt Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Business Nxt Product Property
     - Business Nxt Data Type
   * - Description
     - description
     - "string"
   * - Description	
     - description
     - "string"
   * - DisplayUrl
     - webPage
     - "string"
   * - DisplayUrl	
     - webPage
     - "string"


Salesforce Quote to Business Nxt Country
----------------------------------------
Every Salesforce Quote will be synchronized with a Business Nxt Country.

Once a link between a Salesforce Quote and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Business Nxt Country Property
     - Business Nxt Data Type
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


Salesforce Quotelineitem to Business Nxt Orderline
--------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Business Nxt Orderline.

Once a link between a Salesforce Quotelineitem and a Business Nxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Business Nxt Orderline:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Business Nxt Orderline Property
     - Business Nxt Data Type


Salesforce User to Business Nxt Country
---------------------------------------
Every Salesforce User will be synchronized with a Business Nxt Country.

Once a link between a Salesforce User and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Business Nxt Country Property
     - Business Nxt Data Type
   * - Country
     - name
     - "string"
   * - CountryCode
     - isoCode
     - "string"

