==============================
HubSpot to MemberCare Dataflow
==============================

Generated: 2024-09-13 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to MemberCare Companies
---------------------------------------
Every HubSpot Company will be synchronized with a MemberCare Companies.

Once a link between a HubSpot Company and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - properties.name
     - companyName
     - "string"
   * - properties.website
     - url
     - "string"


HubSpot Contact to MemberCare Persons
-------------------------------------
Every HubSpot Contact will be synchronized with a MemberCare Persons.

Once a link between a HubSpot Contact and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - id
     - addresses.id
     - "string"
   * - properties.city
     - addresses.postalCode.city
     - "string"
   * - properties.country
     - addresses.country.id
     - "string"
   * - properties.date_of_birth
     - birthDate
     - "string"
   * - properties.email
     - socialSecurityNumber.number (Dependant on having wd:Q1273217 in socialSecurityNumber.iso2Letter)
     - "string"
   * - properties.firstname
     - firstname
     - "string"
   * - properties.lastname
     - lastname
     - "string"
   * - properties.zip
     - addresses.postalCode.zipCode
     - "string"


HubSpot Contactcompanyassociation to MemberCare Persons
-------------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a MemberCare Persons.

Once a link between a HubSpot Contactcompanyassociation and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - MemberCare Persons Property
     - MemberCare Data Type


HubSpot Contactcompanyassociationtype to MemberCare Companycategories
---------------------------------------------------------------------
Every HubSpot Contactcompanyassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Contactcompanyassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot Deal to MemberCare Invoices
-----------------------------------
Every HubSpot Deal will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Deal and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - MemberCare Invoices Property
     - MemberCare Data Type
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
     - deliverProductsTo.addresses.addressLineOne
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.addressType
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.attention
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.careOf
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.country
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.end
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.floor
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.formattedAddress
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.id
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.lastChange
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.letter
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.location
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.municipality
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.number
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.postOfficeBox
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.postalCode
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.start
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.street
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.streetAndZipOneLine
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.suite
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.url
     - "string"
   * - properties.dealstage
     - deliverProductsTo.addresses.zipCityCountry
     - "string"
   * - properties.dealstage
     - deliverProductsTo.anonymizedOn
     - "string"
   * - properties.dealstage
     - deliverProductsTo.businessNumbers.debtorLink
     - "string"
   * - properties.dealstage
     - deliverProductsTo.businessNumbers.productionNumber
     - "string"
   * - properties.dealstage
     - deliverProductsTo.businessNumbers.registrationNumberCVR
     - "string"
   * - properties.dealstage
     - deliverProductsTo.businessNumbers.registrationNumberNorwegianCompanyNumber
     - "string"
   * - properties.dealstage
     - deliverProductsTo.businessNumbers.registrationNumberSwedishCompanyNumber
     - "string"
   * - properties.dealstage
     - deliverProductsTo.businessNumbers.registrationNumberVAT
     - "string"
   * - properties.dealstage
     - deliverProductsTo.businessNumbers.registrationNumbersRUT
     - "string"
   * - properties.dealstage
     - deliverProductsTo.businessNumbers.registrationNumbersSE
     - "string"
   * - properties.dealstage
     - deliverProductsTo.businessNumbers.url
     - "string"
   * - properties.dealstage
     - deliverProductsTo.closeDate
     - "string"
   * - properties.dealstage
     - deliverProductsTo.closeReason.description
     - "string"
   * - properties.dealstage
     - deliverProductsTo.closeReason.id
     - "string"
   * - properties.dealstage
     - deliverProductsTo.closeReason.url
     - "string"
   * - properties.dealstage
     - deliverProductsTo.closeReason.valid
     - "string"
   * - properties.dealstage
     - deliverProductsTo.contacts.end
     - "string"
   * - properties.dealstage
     - deliverProductsTo.contacts.id
     - "string"
   * - properties.dealstage
     - deliverProductsTo.contacts.lastChange
     - "string"
   * - properties.dealstage
     - deliverProductsTo.contacts.start
     - "string"
   * - properties.dealstage
     - deliverProductsTo.contacts.type
     - "string"
   * - properties.dealstage
     - deliverProductsTo.contacts.url
     - "string"
   * - properties.dealstage
     - deliverProductsTo.contacts.value
     - "string"
   * - properties.dealstage
     - deliverProductsTo.customFieldValues
     - "string"
   * - properties.dealstage
     - deliverProductsTo.dafualtPayerRule
     - "string"
   * - properties.dealstage
     - deliverProductsTo.debtorAccountNumber
     - "string"
   * - properties.dealstage
     - deliverProductsTo.defaultAddressType
     - "string"
   * - properties.dealstage
     - deliverProductsTo.defaultPayerLink
     - "string"
   * - properties.dealstage
     - deliverProductsTo.ean
     - "string"
   * - properties.dealstage
     - deliverProductsTo.einvoiceEan
     - "string"
   * - properties.dealstage
     - deliverProductsTo.einvoiceEmail
     - "string"
   * - properties.dealstage
     - deliverProductsTo.emailForInvoices
     - "string"
   * - properties.dealstage
     - deliverProductsTo.externalId
     - "string"
   * - properties.dealstage
     - deliverProductsTo.financeType
     - "string"
   * - properties.dealstage
     - deliverProductsTo.honorific
     - "string"
   * - properties.dealstage
     - deliverProductsTo.invoiceDistributionPreference
     - "string"
   * - properties.dealstage
     - deliverProductsTo.invoicesLink
     - "string"
   * - properties.dealstage
     - deliverProductsTo.lastChange
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberType
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.affiliateDate
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.affiliationReason 
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.affiliationSource 
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.applicationDate
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.applicationProcessDate
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.applicationStatus
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.applicationStatusComment
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.closeDate
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.description
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.disaffiliateDate
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.disaffiliateReason 
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.enableGeographic
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.feeExempt
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.id
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.member 
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.membershipCategory 
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.membershipWeights 
     - "string"
   * - properties.dealstage
     - deliverProductsTo.memberships.url
     - "string"
   * - properties.dealstage
     - deliverProductsTo.name
     - "string"
   * - properties.dealstage
     - deliverProductsTo.name1
     - "string"
   * - properties.dealstage
     - deliverProductsTo.name2
     - "string"
   * - properties.dealstage
     - deliverProductsTo.sendInvoicesTo
     - "string"
   * - properties.dealstage
     - deliverProductsTo.sendMailTo
     - "string"
   * - properties.dealstage
     - deliverProductsTo.socialSecurityNumber.iso2Letter
     - "string"
   * - properties.dealstage
     - deliverProductsTo.socialSecurityNumber.number
     - "string"
   * - properties.dealstage
     - deliverProductsTo.url
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
     - sendInvoiceTo.addresses.addressDescription
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.addressLineOne
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.addressType
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.attention
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.careOf
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.country
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.end
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.floor
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.formattedAddress
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.id
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.lastChange
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.letter
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.location
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.municipality
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.number
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.postOfficeBox
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.postalCode
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.start
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.street
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.streetAndZipOneLine
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.suite
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.url
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.addresses.zipCityCountry
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.anonymizedOn
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.businessNumbers.debtorLink
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.businessNumbers.productionNumber
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.businessNumbers.registrationNumberCVR
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.businessNumbers.registrationNumberNorwegianCompanyNumber
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.businessNumbers.registrationNumberSwedishCompanyNumber
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.businessNumbers.registrationNumberVAT
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.businessNumbers.registrationNumbersRUT
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.businessNumbers.registrationNumbersSE
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.businessNumbers.url
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.closeDate
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.closeReason.description
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.closeReason.id
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.closeReason.url
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.closeReason.valid
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.contacts.end
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.contacts.id
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.contacts.lastChange
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.contacts.start
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.contacts.type
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.contacts.url
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.contacts.value
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.customFieldValues
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.dafualtPayerRule
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.debtorAccountNumber
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.defaultAddressType
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.defaultPayerLink
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.ean
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.einvoiceEan
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.einvoiceEmail
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.emailForInvoices
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.externalId
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.financeType
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.honorific
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.invoiceDistributionPreference
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.invoicesLink
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.lastChange
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberType
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.affiliateDate
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.affiliationReason 
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.affiliationSource 
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.applicationDate
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.applicationProcessDate
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.applicationStatus
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.applicationStatusComment
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.closeDate
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.description
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.disaffiliateDate
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.disaffiliateReason 
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.enableGeographic
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.feeExempt
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.id
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.member 
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.membershipCategory 
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.membershipWeights 
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.memberships.url
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.name
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.name1
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.name2
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.sendInvoicesTo
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.sendMailTo
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.socialSecurityNumber.iso2Letter
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.socialSecurityNumber.number
     - "string"
   * - properties.dealstage
     - sendInvoiceTo.url
     - "string"
   * - properties.dealstage
     - source
     - "string"
   * - properties.dealstage
     - url
     - "string"


HubSpot Dealcompanyassociation to MemberCare Invoices
-----------------------------------------------------
Every HubSpot Dealcompanyassociation will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Dealcompanyassociation and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - MemberCare Invoices Property
     - MemberCare Data Type


HubSpot Dealcompanyassociationtype to MemberCare Companycategories
------------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Dealcompanyassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot Dealcontactassociation to MemberCare Invoices
-----------------------------------------------------
Every HubSpot Dealcontactassociation will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Dealcontactassociation and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - MemberCare Invoices Property
     - MemberCare Data Type


HubSpot Dealcontactassociationtype to MemberCare Companycategories
------------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Dealcontactassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot Lineitem to MemberCare Invoices
---------------------------------------
Every HubSpot Lineitem will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Lineitem and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - properties.description
     - invoiceItems.description
     - "string"
   * - properties.price
     - invoiceItems.unitPrice
     - "string"
   * - properties.quantity
     - invoiceItems.quantity
     - "string"


HubSpot Lineitemdealassociation to MemberCare Invoices
------------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Lineitemdealassociation and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - toObjectId (Dependant on having wd:Q190581 in sesam_simpleAssociationTypes)
     - id
     - "string"


HubSpot Lineitemdealassociationtype to MemberCare Companycategories
-------------------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Lineitemdealassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot Lineitemquoteassociation to MemberCare Invoices
-------------------------------------------------------
Every HubSpot Lineitemquoteassociation will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Lineitemquoteassociation and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - toObjectId (Dependant on having wd:Q190581 in sesam_simpleAssociationTypes)
     - id
     - "string"


HubSpot Lineitemquoteassociationtype to MemberCare Companycategories
--------------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Lineitemquoteassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot Product to MemberCare Products
--------------------------------------
Every HubSpot Product will be synchronized with a MemberCare Products.

Once a link between a HubSpot Product and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - properties.name
     - name
     - "string"


HubSpot Quote to MemberCare Invoices
------------------------------------
Every HubSpot Quote will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Quote and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - MemberCare Invoices Property
     - MemberCare Data Type


HubSpot Quotecompanyassociation to MemberCare Invoices
------------------------------------------------------
Every HubSpot Quotecompanyassociation will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Quotecompanyassociation and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - MemberCare Invoices Property
     - MemberCare Data Type


HubSpot Quotecompanyassociationtype to MemberCare Companycategories
-------------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Quotecompanyassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot Quotecontactassociation to MemberCare Invoices
------------------------------------------------------
Every HubSpot Quotecontactassociation will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Quotecontactassociation and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - MemberCare Invoices Property
     - MemberCare Data Type


HubSpot Quotecontactassociationtype to MemberCare Companycategories
-------------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Quotecontactassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot Quotedealassociation to MemberCare Invoices
---------------------------------------------------
Every HubSpot Quotedealassociation will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Quotedealassociation and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - toObjectId (Dependant on having wd:Q190581 in sesam_simpleAssociationTypes)
     - id
     - "string"


HubSpot Quotedealassociationtype to MemberCare Companycategories
----------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Quotedealassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot Quotequotetemplateassociation to MemberCare Invoices
------------------------------------------------------------
Every HubSpot Quotequotetemplateassociation will be synchronized with a MemberCare Invoices.

Once a link between a HubSpot Quotequotetemplateassociation and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - toObjectId (Dependant on having wd:Q190581 in sesam_simpleAssociationTypes)
     - id
     - "string"


HubSpot Quotequotetemplateassociationtype to MemberCare Companycategories
-------------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a MemberCare Companycategories.

Once a link between a HubSpot Quotequotetemplateassociationtype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


HubSpot User to MemberCare Persons
----------------------------------
Every HubSpot User will be synchronized with a MemberCare Persons.

Once a link between a HubSpot User and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - email
     - socialSecurityNumber.number (Dependant on having wd:Q28378282 in socialSecurityNumber.iso2Letter)
     - "string"


HubSpot Company to MemberCare Countries
---------------------------------------
Every HubSpot Company will be synchronized with a MemberCare Countries.

Once a link between a HubSpot Company and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - MemberCare Countries Property
     - MemberCare Data Type
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

