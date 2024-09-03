==============================
HubSpot to Membercare Dataflow
==============================

Generated: 2024-09-03 13:11:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Membercare Companies
---------------------------------------
Every HubSpot Company will be synchronized with a Membercare Companies.

Once a link between a HubSpot Company and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Membercare Companies Property
     - Membercare Data Type
   * - properties.name
     - companyName
     - "string"
   * - properties.website
     - url
     - "string"


HubSpot Contactcompanyassociationtype to Membercare Companycategories
---------------------------------------------------------------------
Every HubSpot Contactcompanyassociationtype will be synchronized with a Membercare Companycategories.

Once a link between a HubSpot Contactcompanyassociationtype and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociationtype and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociationtype Property
     - Membercare Companycategories Property
     - Membercare Data Type


HubSpot Deal to Membercare Invoices
-----------------------------------
Every HubSpot Deal will be synchronized with a Membercare Invoices.

Once a link between a HubSpot Deal and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Membercare Invoices Property
     - Membercare Data Type
   * - properties.dealstage
     - creationInfo
     - "string"
   * - properties.dealstage
     - creditedInvoiceId
     - "string"
   * - properties.dealstage
     - creditedInvoiceLink
     - "string"
   * - properties.dealstage
     - deliverProductsTo
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.addressDescription
     - "string"
   * - properties.dealstage
     - eInvoiceInfo.accountingNo
     - "string"
   * - properties.dealstage
     - eInvoiceInfo.ean
     - "string"
   * - properties.dealstage
     - eInvoiceInfo.email
     - "string"
   * - properties.dealstage
     - eInvoiceInfo.reference
     - "string"
   * - properties.dealstage
     - eInvoiceInfo.requisitionNo
     - "string"
   * - properties.dealstage
     - eInvoiceInfo.url
     - "string"
   * - properties.dealstage
     - financeDate
     - "string"
   * - properties.dealstage
     - financeStatus
     - "string"
   * - properties.dealstage
     - incomeDate
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.addresses
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.anonymizedOn
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.businessNumbers
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.closeDate
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.closeReason
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.contacts
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.customFieldValues
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.dafualtPayerRule
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.debtorAccountNumber
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.defaultAddressType
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.defaultPayerLink
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.ean
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.einvoiceEan
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.einvoiceEmail
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.emailForInvoices
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.externalId
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.financeType
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.honorific
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.invoiceDistributionPreference
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.invoicesLink
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.lastChange
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.memberType
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.memberships
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.name
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.name1
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.name2
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.sendInvoicesTo
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.sendMailTo
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.socialSecurityNumber
     - "string"
   * - properties.dealstage
     - invoiceItems.buyer.url
     - "string"
   * - properties.dealstage
     - invoiceItems.creditedInvoiceItemId
     - "string"
   * - properties.dealstage
     - invoiceItems.creditedInvoiceLink
     - "string"
   * - properties.dealstage
     - invoiceItems.description
     - "string"
   * - properties.dealstage
     - invoiceItems.feeInfo.baseAmount
     - "string"
   * - properties.dealstage
     - invoiceItems.feeInfo.feeAmountInfo
     - "string"
   * - properties.dealstage
     - invoiceItems.feeInfo.period
     - "string"
   * - properties.dealstage
     - invoiceItems.feeInfo.rate
     - "string"
   * - properties.dealstage
     - invoiceItems.feeInfo.url
     - "string"
   * - properties.dealstage
     - invoiceItems.financeDimensions.department
     - "string"
   * - properties.dealstage
     - invoiceItems.financeDimensions.dimension3
     - "string"
   * - properties.dealstage
     - invoiceItems.financeDimensions.dimension4
     - "string"
   * - properties.dealstage
     - invoiceItems.financeDimensions.dimension5
     - "string"
   * - properties.dealstage
     - invoiceItems.financeDimensions.productIdentification
     - "string"
   * - properties.dealstage
     - invoiceItems.financeDimensions.url
     - "string"
   * - properties.dealstage
     - invoiceItems.id
     - "string"
   * - properties.dealstage
     - invoiceItems.invoiceLink
     - "string"
   * - properties.dealstage
     - invoiceItems.isCredited
     - "string"
   * - properties.dealstage
     - invoiceItems.quantity
     - "string"
   * - properties.dealstage
     - invoiceItems.sequence
     - "string"
   * - properties.dealstage
     - invoiceItems.subscriptionInfo.transactionEnd
     - "string"
   * - properties.dealstage
     - invoiceItems.subscriptionInfo.transactionStart
     - "string"
   * - properties.dealstage
     - invoiceItems.subscriptionInfo.url
     - "string"
   * - properties.dealstage
     - invoiceItems.totalPrice
     - "string"
   * - properties.dealstage
     - invoiceItems.totalVat
     - "string"
   * - properties.dealstage
     - invoiceItems.unitPrice
     - "string"
   * - properties.dealstage
     - invoiceItems.url
     - "string"
   * - properties.dealstage
     - invoiceTexts.invoiceLink
     - "string"
   * - properties.dealstage
     - invoiceTexts.label
     - "string"
   * - properties.dealstage
     - invoiceTexts.labelId
     - "string"
   * - properties.dealstage
     - invoiceTexts.url
     - "string"
   * - properties.dealstage
     - invoiceTexts.value
     - "string"
   * - properties.dealstage
     - payer.addresses.addressDescription
     - "string"
   * - properties.dealstage
     - payer.addresses.addressLineOne
     - "string"
   * - properties.dealstage
     - payer.addresses.addressType
     - "string"
   * - properties.dealstage
     - payer.addresses.attention
     - "string"
   * - properties.dealstage
     - payer.addresses.careOf
     - "string"
   * - properties.dealstage
     - payer.addresses.country
     - "string"
   * - properties.dealstage
     - payer.addresses.end
     - "string"
   * - properties.dealstage
     - payer.addresses.floor
     - "string"
   * - properties.dealstage
     - payer.addresses.formattedAddress
     - "string"
   * - properties.dealstage
     - payer.addresses.id
     - "string"
   * - properties.dealstage
     - payer.addresses.lastChange
     - "string"
   * - properties.dealstage
     - payer.addresses.letter
     - "string"
   * - properties.dealstage
     - payer.addresses.location
     - "string"
   * - properties.dealstage
     - payer.addresses.municipality
     - "string"
   * - properties.dealstage
     - payer.addresses.number
     - "string"
   * - properties.dealstage
     - payer.addresses.postOfficeBox
     - "string"
   * - properties.dealstage
     - payer.addresses.postalCode
     - "string"
   * - properties.dealstage
     - payer.addresses.start
     - "string"
   * - properties.dealstage
     - payer.addresses.street
     - "string"
   * - properties.dealstage
     - payer.addresses.streetAndZipOneLine
     - "string"
   * - properties.dealstage
     - payer.addresses.suite
     - "string"
   * - properties.dealstage
     - payer.addresses.url
     - "string"
   * - properties.dealstage
     - payer.addresses.zipCityCountry
     - "string"
   * - properties.dealstage
     - payer.anonymizedOn
     - "string"
   * - properties.dealstage
     - payer.businessNumbers.debtorLink
     - "string"
   * - properties.dealstage
     - payer.businessNumbers.productionNumber
     - "string"
   * - properties.dealstage
     - payer.businessNumbers.registrationNumberCVR
     - "string"
   * - properties.dealstage
     - payer.businessNumbers.registrationNumberNorwegianCompanyNumber
     - "string"
   * - properties.dealstage
     - payer.businessNumbers.registrationNumberSwedishCompanyNumber
     - "string"
   * - properties.dealstage
     - payer.businessNumbers.registrationNumberVAT
     - "string"
   * - properties.dealstage
     - payer.businessNumbers.registrationNumbersRUT
     - "string"
   * - properties.dealstage
     - payer.businessNumbers.registrationNumbersSE
     - "string"
   * - properties.dealstage
     - payer.businessNumbers.url
     - "string"
   * - properties.dealstage
     - payer.closeDate
     - "string"
   * - properties.dealstage
     - payer.closeReason.description
     - "string"
   * - properties.dealstage
     - payer.closeReason.id
     - "string"
   * - properties.dealstage
     - payer.closeReason.url
     - "string"
   * - properties.dealstage
     - payer.closeReason.valid
     - "string"
   * - properties.dealstage
     - payer.contacts.end
     - "string"
   * - properties.dealstage
     - payer.contacts.id
     - "string"
   * - properties.dealstage
     - payer.contacts.lastChange
     - "string"
   * - properties.dealstage
     - payer.contacts.start
     - "string"
   * - properties.dealstage
     - payer.contacts.type
     - "string"
   * - properties.dealstage
     - payer.contacts.url
     - "string"
   * - properties.dealstage
     - payer.contacts.value
     - "string"
   * - properties.dealstage
     - payer.customFieldValues
     - "string"
   * - properties.dealstage
     - payer.dafualtPayerRule
     - "string"
   * - properties.dealstage
     - payer.debtorAccountNumber
     - "string"
   * - properties.dealstage
     - payer.defaultAddressType
     - "string"
   * - properties.dealstage
     - payer.defaultPayerLink
     - "string"
   * - properties.dealstage
     - payer.ean
     - "string"
   * - properties.dealstage
     - payer.einvoiceEan
     - "string"
   * - properties.dealstage
     - payer.einvoiceEmail
     - "string"
   * - properties.dealstage
     - payer.emailForInvoices
     - "string"
   * - properties.dealstage
     - payer.externalId
     - "string"
   * - properties.dealstage
     - payer.financeType
     - "string"
   * - properties.dealstage
     - payer.honorific
     - "string"
   * - properties.dealstage
     - payer.invoiceDistributionPreference
     - "string"
   * - properties.dealstage
     - payer.invoicesLink
     - "string"
   * - properties.dealstage
     - payer.lastChange
     - "string"
   * - properties.dealstage
     - payer.memberType
     - "string"
   * - properties.dealstage
     - payer.memberships.affiliateDate
     - "string"
   * - properties.dealstage
     - payer.memberships.affiliationReason 
     - "string"
   * - properties.dealstage
     - payer.memberships.affiliationSource 
     - "string"
   * - properties.dealstage
     - payer.memberships.applicationDate
     - "string"
   * - properties.dealstage
     - payer.memberships.applicationProcessDate
     - "string"
   * - properties.dealstage
     - payer.memberships.applicationStatus
     - "string"
   * - properties.dealstage
     - payer.memberships.applicationStatusComment
     - "string"
   * - properties.dealstage
     - payer.memberships.closeDate
     - "string"
   * - properties.dealstage
     - payer.memberships.description
     - "string"
   * - properties.dealstage
     - payer.memberships.disaffiliateDate
     - "string"
   * - properties.dealstage
     - payer.memberships.disaffiliateReason 
     - "string"
   * - properties.dealstage
     - payer.memberships.enableGeographic
     - "string"
   * - properties.dealstage
     - payer.memberships.feeExempt
     - "string"
   * - properties.dealstage
     - payer.memberships.id
     - "string"
   * - properties.dealstage
     - payer.memberships.member 
     - "string"
   * - properties.dealstage
     - payer.memberships.membershipCategory 
     - "string"
   * - properties.dealstage
     - payer.memberships.membershipWeights 
     - "string"
   * - properties.dealstage
     - payer.memberships.url
     - "string"
   * - properties.dealstage
     - payer.name
     - "string"
   * - properties.dealstage
     - payer.name1
     - "string"
   * - properties.dealstage
     - payer.name2
     - "string"
   * - properties.dealstage
     - payer.sendInvoicesTo
     - "string"
   * - properties.dealstage
     - payer.sendMailTo
     - "string"
   * - properties.dealstage
     - payer.socialSecurityNumber.iso2Letter
     - "string"
   * - properties.dealstage
     - payer.socialSecurityNumber.number
     - "string"
   * - properties.dealstage
     - payer.url
     - "string"
   * - properties.dealstage
     - payments.amount
     - "string"
   * - properties.dealstage
     - payments.financeDimensions.department
     - "string"
   * - properties.dealstage
     - payments.financeDimensions.dimension3
     - "string"
   * - properties.dealstage
     - payments.financeDimensions.dimension4
     - "string"
   * - properties.dealstage
     - payments.financeDimensions.dimension5
     - "string"
   * - properties.dealstage
     - payments.financeDimensions.productIdentification
     - "string"
   * - properties.dealstage
     - payments.financeDimensions.url
     - "string"
   * - properties.dealstage
     - payments.financeStatus
     - "string"
   * - properties.dealstage
     - payments.id
     - "string"
   * - properties.dealstage
     - payments.invoiceId
     - "string"
   * - properties.dealstage
     - payments.invoiceLink
     - "string"
   * - properties.dealstage
     - payments.paymentDate
     - "string"
   * - properties.dealstage
     - payments.paymentIdentification
     - "string"
   * - properties.dealstage
     - payments.paymentSystemCardType
     - "string"
   * - properties.dealstage
     - payments.paymentType
     - "string"
   * - properties.dealstage
     - payments.shopOrderId
     - "string"
   * - properties.dealstage
     - payments.url
     - "string"
   * - properties.dealstage
     - payments.voucherNo
     - "string"
   * - properties.dealstage
     - recurringPaymentIdentification
     - "string"
   * - properties.dealstage
     - sendInvoiceTo
     - "string"
   * - properties.dealstage
     - source
     - "string"
   * - properties.dealstage
     - url
     - "string"


HubSpot Dealcompanyassociation to Membercare Invoices
-----------------------------------------------------
Every HubSpot Dealcompanyassociation will be synchronized with a Membercare Invoices.

Once a link between a HubSpot Dealcompanyassociation and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - Membercare Invoices Property
     - Membercare Data Type


HubSpot Dealcompanyassociationtype to Membercare Companycategories
------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a Membercare Companycategories.

Once a link between a HubSpot Dealcompanyassociationtype and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - Membercare Companycategories Property
     - Membercare Data Type


HubSpot Dealcontactassociation to Membercare Invoices
-----------------------------------------------------
Every HubSpot Dealcontactassociation will be synchronized with a Membercare Invoices.

Once a link between a HubSpot Dealcontactassociation and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - Membercare Invoices Property
     - Membercare Data Type


HubSpot Dealcontactassociationtype to Membercare Companycategories
------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a Membercare Companycategories.

Once a link between a HubSpot Dealcontactassociationtype and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - Membercare Companycategories Property
     - Membercare Data Type


HubSpot Lineitem to Membercare Invoices
---------------------------------------
Every HubSpot Lineitem will be synchronized with a Membercare Invoices.

Once a link between a HubSpot Lineitem and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Membercare Invoices Property
     - Membercare Data Type


HubSpot Lineitemdealassociation to Membercare Invoices
------------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a Membercare Invoices.

Once a link between a HubSpot Lineitemdealassociation and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - Membercare Invoices Property
     - Membercare Data Type


HubSpot Lineitemdealassociationtype to Membercare Companycategories
-------------------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a Membercare Companycategories.

Once a link between a HubSpot Lineitemdealassociationtype and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - Membercare Companycategories Property
     - Membercare Data Type


HubSpot Lineitemquoteassociation to Membercare Invoices
-------------------------------------------------------
Every HubSpot Lineitemquoteassociation will be synchronized with a Membercare Invoices.

Once a link between a HubSpot Lineitemquoteassociation and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - Membercare Invoices Property
     - Membercare Data Type


HubSpot Lineitemquoteassociationtype to Membercare Companycategories
--------------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a Membercare Companycategories.

Once a link between a HubSpot Lineitemquoteassociationtype and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - Membercare Companycategories Property
     - Membercare Data Type


HubSpot Quote to Membercare Invoices
------------------------------------
Every HubSpot Quote will be synchronized with a Membercare Invoices.

Once a link between a HubSpot Quote and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Membercare Invoices Property
     - Membercare Data Type


HubSpot Quotecompanyassociation to Membercare Invoices
------------------------------------------------------
Every HubSpot Quotecompanyassociation will be synchronized with a Membercare Invoices.

Once a link between a HubSpot Quotecompanyassociation and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Membercare Invoices Property
     - Membercare Data Type


HubSpot Quotecompanyassociationtype to Membercare Companycategories
-------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a Membercare Companycategories.

Once a link between a HubSpot Quotecompanyassociationtype and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - Membercare Companycategories Property
     - Membercare Data Type


HubSpot Quotecontactassociation to Membercare Invoices
------------------------------------------------------
Every HubSpot Quotecontactassociation will be synchronized with a Membercare Invoices.

Once a link between a HubSpot Quotecontactassociation and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Membercare Invoices Property
     - Membercare Data Type


HubSpot Quotecontactassociationtype to Membercare Companycategories
-------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a Membercare Companycategories.

Once a link between a HubSpot Quotecontactassociationtype and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - Membercare Companycategories Property
     - Membercare Data Type


HubSpot Quotedealassociation to Membercare Invoices
---------------------------------------------------
Every HubSpot Quotedealassociation will be synchronized with a Membercare Invoices.

Once a link between a HubSpot Quotedealassociation and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Membercare Invoices Property
     - Membercare Data Type


HubSpot Quotedealassociationtype to Membercare Companycategories
----------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a Membercare Companycategories.

Once a link between a HubSpot Quotedealassociationtype and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - Membercare Companycategories Property
     - Membercare Data Type


HubSpot Quotequotetemplateassociation to Membercare Invoices
------------------------------------------------------------
Every HubSpot Quotequotetemplateassociation will be synchronized with a Membercare Invoices.

Once a link between a HubSpot Quotequotetemplateassociation and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Membercare Invoices Property
     - Membercare Data Type


HubSpot Quotequotetemplateassociationtype to Membercare Companycategories
-------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a Membercare Companycategories.

Once a link between a HubSpot Quotequotetemplateassociationtype and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - Membercare Companycategories Property
     - Membercare Data Type


HubSpot Company to Membercare Countries
---------------------------------------
Every HubSpot Company will be synchronized with a Membercare Countries.

Once a link between a HubSpot Company and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Membercare Countries Property
     - Membercare Data Type
   * - properties.country
     - name
     - "string"
   * - properties.industry
     - name
     - "string"
   * - properties.state
     - name
     - "string"
   * - properties.type
     - name
     - "string"

