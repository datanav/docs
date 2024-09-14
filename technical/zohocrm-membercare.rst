==============================
ZohoCRM to MemberCare Dataflow
==============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to MemberCare Companies
---------------------------------------
Every ZohoCRM Account will be synchronized with a MemberCare Companies.

Once a link between a ZohoCRM Account and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - Account_Name
     - companyName
     - "string"
   * - Website
     - url
     - "string"


ZohoCRM Contact to MemberCare Persons
-------------------------------------
Every ZohoCRM Contact will be synchronized with a MemberCare Persons.

Once a link between a ZohoCRM Contact and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - First_Name
     - firstname
     - "string"
   * - Full_Name
     - name
     - "string"
   * - Last_Name
     - lastname
     - "string"
   * - Mailing_City
     - addresses.postalCode.city
     - "string"
   * - Mailing_Country
     - addresses.country.id
     - "string"
   * - Mailing_Zip
     - addresses.postalCode.zipCode
     - "string"
   * - Other_City
     - addresses.postalCode.city
     - "string"
   * - Other_Country
     - addresses.country.id
     - "string"
   * - Other_Zip
     - addresses.postalCode.zipCode
     - "string"
   * - id
     - addresses.id
     - "string"


ZohoCRM Deal to MemberCare Invoices
-----------------------------------
Every ZohoCRM Deal will be synchronized with a MemberCare Invoices.

Once a link between a ZohoCRM Deal and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - Probability
     - creationInfo
     - "string"
   * - Probability
     - creditedInvoiceId
     - "string"
   * - Probability
     - creditedInvoiceLink
     - "string"
   * - Probability
     - deliverProductsTo
     - "string"
   * - Probability
     - deliverProductsTo.addresses.addressDescription
     - "string"
   * - Probability
     - deliverProductsTo.addresses.addressLineOne
     - "string"
   * - Probability
     - deliverProductsTo.addresses.addressType
     - "string"
   * - Probability
     - deliverProductsTo.addresses.attention
     - "string"
   * - Probability
     - deliverProductsTo.addresses.careOf
     - "string"
   * - Probability
     - deliverProductsTo.addresses.country
     - "string"
   * - Probability
     - deliverProductsTo.addresses.end
     - "string"
   * - Probability
     - deliverProductsTo.addresses.floor
     - "string"
   * - Probability
     - deliverProductsTo.addresses.formattedAddress
     - "string"
   * - Probability
     - deliverProductsTo.addresses.id
     - "string"
   * - Probability
     - deliverProductsTo.addresses.lastChange
     - "string"
   * - Probability
     - deliverProductsTo.addresses.letter
     - "string"
   * - Probability
     - deliverProductsTo.addresses.location
     - "string"
   * - Probability
     - deliverProductsTo.addresses.municipality
     - "string"
   * - Probability
     - deliverProductsTo.addresses.number
     - "string"
   * - Probability
     - deliverProductsTo.addresses.postOfficeBox
     - "string"
   * - Probability
     - deliverProductsTo.addresses.postalCode
     - "string"
   * - Probability
     - deliverProductsTo.addresses.start
     - "string"
   * - Probability
     - deliverProductsTo.addresses.street
     - "string"
   * - Probability
     - deliverProductsTo.addresses.streetAndZipOneLine
     - "string"
   * - Probability
     - deliverProductsTo.addresses.suite
     - "string"
   * - Probability
     - deliverProductsTo.addresses.url
     - "string"
   * - Probability
     - deliverProductsTo.addresses.zipCityCountry
     - "string"
   * - Probability
     - deliverProductsTo.anonymizedOn
     - "string"
   * - Probability
     - deliverProductsTo.businessNumbers.debtorLink
     - "string"
   * - Probability
     - deliverProductsTo.businessNumbers.productionNumber
     - "string"
   * - Probability
     - deliverProductsTo.businessNumbers.registrationNumberCVR
     - "string"
   * - Probability
     - deliverProductsTo.businessNumbers.registrationNumberNorwegianCompanyNumber
     - "string"
   * - Probability
     - deliverProductsTo.businessNumbers.registrationNumberSwedishCompanyNumber
     - "string"
   * - Probability
     - deliverProductsTo.businessNumbers.registrationNumberVAT
     - "string"
   * - Probability
     - deliverProductsTo.businessNumbers.registrationNumbersRUT
     - "string"
   * - Probability
     - deliverProductsTo.businessNumbers.registrationNumbersSE
     - "string"
   * - Probability
     - deliverProductsTo.businessNumbers.url
     - "string"
   * - Probability
     - deliverProductsTo.closeDate
     - "string"
   * - Probability
     - deliverProductsTo.closeReason.description
     - "string"
   * - Probability
     - deliverProductsTo.closeReason.id
     - "string"
   * - Probability
     - deliverProductsTo.closeReason.url
     - "string"
   * - Probability
     - deliverProductsTo.closeReason.valid
     - "string"
   * - Probability
     - deliverProductsTo.contacts.end
     - "string"
   * - Probability
     - deliverProductsTo.contacts.id
     - "string"
   * - Probability
     - deliverProductsTo.contacts.lastChange
     - "string"
   * - Probability
     - deliverProductsTo.contacts.start
     - "string"
   * - Probability
     - deliverProductsTo.contacts.type
     - "string"
   * - Probability
     - deliverProductsTo.contacts.url
     - "string"
   * - Probability
     - deliverProductsTo.contacts.value
     - "string"
   * - Probability
     - deliverProductsTo.customFieldValues
     - "string"
   * - Probability
     - deliverProductsTo.dafualtPayerRule
     - "string"
   * - Probability
     - deliverProductsTo.debtorAccountNumber
     - "string"
   * - Probability
     - deliverProductsTo.defaultAddressType
     - "string"
   * - Probability
     - deliverProductsTo.defaultPayerLink
     - "string"
   * - Probability
     - deliverProductsTo.ean
     - "string"
   * - Probability
     - deliverProductsTo.einvoiceEan
     - "string"
   * - Probability
     - deliverProductsTo.einvoiceEmail
     - "string"
   * - Probability
     - deliverProductsTo.emailForInvoices
     - "string"
   * - Probability
     - deliverProductsTo.externalId
     - "string"
   * - Probability
     - deliverProductsTo.financeType
     - "string"
   * - Probability
     - deliverProductsTo.honorific
     - "string"
   * - Probability
     - deliverProductsTo.invoiceDistributionPreference
     - "string"
   * - Probability
     - deliverProductsTo.invoicesLink
     - "string"
   * - Probability
     - deliverProductsTo.lastChange
     - "string"
   * - Probability
     - deliverProductsTo.memberType
     - "string"
   * - Probability
     - deliverProductsTo.memberships.affiliateDate
     - "string"
   * - Probability
     - deliverProductsTo.memberships.affiliationReason 
     - "string"
   * - Probability
     - deliverProductsTo.memberships.affiliationSource 
     - "string"
   * - Probability
     - deliverProductsTo.memberships.applicationDate
     - "string"
   * - Probability
     - deliverProductsTo.memberships.applicationProcessDate
     - "string"
   * - Probability
     - deliverProductsTo.memberships.applicationStatus
     - "string"
   * - Probability
     - deliverProductsTo.memberships.applicationStatusComment
     - "string"
   * - Probability
     - deliverProductsTo.memberships.closeDate
     - "string"
   * - Probability
     - deliverProductsTo.memberships.description
     - "string"
   * - Probability
     - deliverProductsTo.memberships.disaffiliateDate
     - "string"
   * - Probability
     - deliverProductsTo.memberships.disaffiliateReason 
     - "string"
   * - Probability
     - deliverProductsTo.memberships.enableGeographic
     - "string"
   * - Probability
     - deliverProductsTo.memberships.feeExempt
     - "string"
   * - Probability
     - deliverProductsTo.memberships.id
     - "string"
   * - Probability
     - deliverProductsTo.memberships.member 
     - "string"
   * - Probability
     - deliverProductsTo.memberships.membershipCategory 
     - "string"
   * - Probability
     - deliverProductsTo.memberships.membershipWeights 
     - "string"
   * - Probability
     - deliverProductsTo.memberships.url
     - "string"
   * - Probability
     - deliverProductsTo.name
     - "string"
   * - Probability
     - deliverProductsTo.name1
     - "string"
   * - Probability
     - deliverProductsTo.name2
     - "string"
   * - Probability
     - deliverProductsTo.sendInvoicesTo
     - "string"
   * - Probability
     - deliverProductsTo.sendMailTo
     - "string"
   * - Probability
     - deliverProductsTo.socialSecurityNumber.iso2Letter
     - "string"
   * - Probability
     - deliverProductsTo.socialSecurityNumber.number
     - "string"
   * - Probability
     - deliverProductsTo.url
     - "string"
   * - Probability
     - eInvoiceInfo.accountingNo
     - "string"
   * - Probability
     - eInvoiceInfo.ean
     - "string"
   * - Probability
     - eInvoiceInfo.email
     - "string"
   * - Probability
     - eInvoiceInfo.reference
     - "string"
   * - Probability
     - eInvoiceInfo.requisitionNo
     - "string"
   * - Probability
     - eInvoiceInfo.url
     - "string"
   * - Probability
     - financeDate
     - "string"
   * - Probability
     - financeStatus
     - "string"
   * - Probability
     - incomeDate
     - "string"
   * - Probability
     - invoiceItems.buyer
     - "string"
   * - Probability
     - invoiceItems.buyer.addresses
     - "string"
   * - Probability
     - invoiceItems.buyer.anonymizedOn
     - "string"
   * - Probability
     - invoiceItems.buyer.businessNumbers
     - "string"
   * - Probability
     - invoiceItems.buyer.closeDate
     - "string"
   * - Probability
     - invoiceItems.buyer.closeReason
     - "string"
   * - Probability
     - invoiceItems.buyer.contacts
     - "string"
   * - Probability
     - invoiceItems.buyer.customFieldValues
     - "string"
   * - Probability
     - invoiceItems.buyer.dafualtPayerRule
     - "string"
   * - Probability
     - invoiceItems.buyer.debtorAccountNumber
     - "string"
   * - Probability
     - invoiceItems.buyer.defaultAddressType
     - "string"
   * - Probability
     - invoiceItems.buyer.defaultPayerLink
     - "string"
   * - Probability
     - invoiceItems.buyer.ean
     - "string"
   * - Probability
     - invoiceItems.buyer.einvoiceEan
     - "string"
   * - Probability
     - invoiceItems.buyer.einvoiceEmail
     - "string"
   * - Probability
     - invoiceItems.buyer.emailForInvoices
     - "string"
   * - Probability
     - invoiceItems.buyer.externalId
     - "string"
   * - Probability
     - invoiceItems.buyer.financeType
     - "string"
   * - Probability
     - invoiceItems.buyer.honorific
     - "string"
   * - Probability
     - invoiceItems.buyer.invoiceDistributionPreference
     - "string"
   * - Probability
     - invoiceItems.buyer.invoicesLink
     - "string"
   * - Probability
     - invoiceItems.buyer.lastChange
     - "string"
   * - Probability
     - invoiceItems.buyer.memberType
     - "string"
   * - Probability
     - invoiceItems.buyer.memberships
     - "string"
   * - Probability
     - invoiceItems.buyer.name
     - "string"
   * - Probability
     - invoiceItems.buyer.name1
     - "string"
   * - Probability
     - invoiceItems.buyer.name2
     - "string"
   * - Probability
     - invoiceItems.buyer.sendInvoicesTo
     - "string"
   * - Probability
     - invoiceItems.buyer.sendMailTo
     - "string"
   * - Probability
     - invoiceItems.buyer.socialSecurityNumber
     - "string"
   * - Probability
     - invoiceItems.buyer.url
     - "string"
   * - Probability
     - invoiceItems.creditedInvoiceItemId
     - "string"
   * - Probability
     - invoiceItems.creditedInvoiceLink
     - "string"
   * - Probability
     - invoiceItems.description
     - "string"
   * - Probability
     - invoiceItems.feeInfo.baseAmount
     - "string"
   * - Probability
     - invoiceItems.feeInfo.feeAmountInfo
     - "string"
   * - Probability
     - invoiceItems.feeInfo.period
     - "string"
   * - Probability
     - invoiceItems.feeInfo.rate
     - "string"
   * - Probability
     - invoiceItems.feeInfo.url
     - "string"
   * - Probability
     - invoiceItems.financeDimensions.department
     - "string"
   * - Probability
     - invoiceItems.financeDimensions.dimension3
     - "string"
   * - Probability
     - invoiceItems.financeDimensions.dimension4
     - "string"
   * - Probability
     - invoiceItems.financeDimensions.dimension5
     - "string"
   * - Probability
     - invoiceItems.financeDimensions.productIdentification
     - "string"
   * - Probability
     - invoiceItems.financeDimensions.url
     - "string"
   * - Probability
     - invoiceItems.id
     - "string"
   * - Probability
     - invoiceItems.invoiceLink
     - "string"
   * - Probability
     - invoiceItems.isCredited
     - "string"
   * - Probability
     - invoiceItems.quantity
     - "string"
   * - Probability
     - invoiceItems.sequence
     - "string"
   * - Probability
     - invoiceItems.subscriptionInfo.transactionEnd
     - "string"
   * - Probability
     - invoiceItems.subscriptionInfo.transactionStart
     - "string"
   * - Probability
     - invoiceItems.subscriptionInfo.url
     - "string"
   * - Probability
     - invoiceItems.totalPrice
     - "string"
   * - Probability
     - invoiceItems.totalVat
     - "string"
   * - Probability
     - invoiceItems.unitPrice
     - "string"
   * - Probability
     - invoiceItems.url
     - "string"
   * - Probability
     - invoiceTexts.invoiceLink
     - "string"
   * - Probability
     - invoiceTexts.label
     - "string"
   * - Probability
     - invoiceTexts.labelId
     - "string"
   * - Probability
     - invoiceTexts.url
     - "string"
   * - Probability
     - invoiceTexts.value
     - "string"
   * - Probability
     - payer.addresses.addressDescription
     - "string"
   * - Probability
     - payer.addresses.addressLineOne
     - "string"
   * - Probability
     - payer.addresses.addressType
     - "string"
   * - Probability
     - payer.addresses.attention
     - "string"
   * - Probability
     - payer.addresses.careOf
     - "string"
   * - Probability
     - payer.addresses.country
     - "string"
   * - Probability
     - payer.addresses.end
     - "string"
   * - Probability
     - payer.addresses.floor
     - "string"
   * - Probability
     - payer.addresses.formattedAddress
     - "string"
   * - Probability
     - payer.addresses.id
     - "string"
   * - Probability
     - payer.addresses.lastChange
     - "string"
   * - Probability
     - payer.addresses.letter
     - "string"
   * - Probability
     - payer.addresses.location
     - "string"
   * - Probability
     - payer.addresses.municipality
     - "string"
   * - Probability
     - payer.addresses.number
     - "string"
   * - Probability
     - payer.addresses.postOfficeBox
     - "string"
   * - Probability
     - payer.addresses.postalCode
     - "string"
   * - Probability
     - payer.addresses.start
     - "string"
   * - Probability
     - payer.addresses.street
     - "string"
   * - Probability
     - payer.addresses.streetAndZipOneLine
     - "string"
   * - Probability
     - payer.addresses.suite
     - "string"
   * - Probability
     - payer.addresses.url
     - "string"
   * - Probability
     - payer.addresses.zipCityCountry
     - "string"
   * - Probability
     - payer.anonymizedOn
     - "string"
   * - Probability
     - payer.businessNumbers.debtorLink
     - "string"
   * - Probability
     - payer.businessNumbers.productionNumber
     - "string"
   * - Probability
     - payer.businessNumbers.registrationNumberCVR
     - "string"
   * - Probability
     - payer.businessNumbers.registrationNumberNorwegianCompanyNumber
     - "string"
   * - Probability
     - payer.businessNumbers.registrationNumberSwedishCompanyNumber
     - "string"
   * - Probability
     - payer.businessNumbers.registrationNumberVAT
     - "string"
   * - Probability
     - payer.businessNumbers.registrationNumbersRUT
     - "string"
   * - Probability
     - payer.businessNumbers.registrationNumbersSE
     - "string"
   * - Probability
     - payer.businessNumbers.url
     - "string"
   * - Probability
     - payer.closeDate
     - "string"
   * - Probability
     - payer.closeReason.description
     - "string"
   * - Probability
     - payer.closeReason.id
     - "string"
   * - Probability
     - payer.closeReason.url
     - "string"
   * - Probability
     - payer.closeReason.valid
     - "string"
   * - Probability
     - payer.contacts.end
     - "string"
   * - Probability
     - payer.contacts.id
     - "string"
   * - Probability
     - payer.contacts.lastChange
     - "string"
   * - Probability
     - payer.contacts.start
     - "string"
   * - Probability
     - payer.contacts.type
     - "string"
   * - Probability
     - payer.contacts.url
     - "string"
   * - Probability
     - payer.contacts.value
     - "string"
   * - Probability
     - payer.customFieldValues
     - "string"
   * - Probability
     - payer.dafualtPayerRule
     - "string"
   * - Probability
     - payer.debtorAccountNumber
     - "string"
   * - Probability
     - payer.defaultAddressType
     - "string"
   * - Probability
     - payer.defaultPayerLink
     - "string"
   * - Probability
     - payer.ean
     - "string"
   * - Probability
     - payer.einvoiceEan
     - "string"
   * - Probability
     - payer.einvoiceEmail
     - "string"
   * - Probability
     - payer.emailForInvoices
     - "string"
   * - Probability
     - payer.externalId
     - "string"
   * - Probability
     - payer.financeType
     - "string"
   * - Probability
     - payer.honorific
     - "string"
   * - Probability
     - payer.invoiceDistributionPreference
     - "string"
   * - Probability
     - payer.invoicesLink
     - "string"
   * - Probability
     - payer.lastChange
     - "string"
   * - Probability
     - payer.memberType
     - "string"
   * - Probability
     - payer.memberships.affiliateDate
     - "string"
   * - Probability
     - payer.memberships.affiliationReason 
     - "string"
   * - Probability
     - payer.memberships.affiliationSource 
     - "string"
   * - Probability
     - payer.memberships.applicationDate
     - "string"
   * - Probability
     - payer.memberships.applicationProcessDate
     - "string"
   * - Probability
     - payer.memberships.applicationStatus
     - "string"
   * - Probability
     - payer.memberships.applicationStatusComment
     - "string"
   * - Probability
     - payer.memberships.closeDate
     - "string"
   * - Probability
     - payer.memberships.description
     - "string"
   * - Probability
     - payer.memberships.disaffiliateDate
     - "string"
   * - Probability
     - payer.memberships.disaffiliateReason 
     - "string"
   * - Probability
     - payer.memberships.enableGeographic
     - "string"
   * - Probability
     - payer.memberships.feeExempt
     - "string"
   * - Probability
     - payer.memberships.id
     - "string"
   * - Probability
     - payer.memberships.member 
     - "string"
   * - Probability
     - payer.memberships.membershipCategory 
     - "string"
   * - Probability
     - payer.memberships.membershipWeights 
     - "string"
   * - Probability
     - payer.memberships.url
     - "string"
   * - Probability
     - payer.name
     - "string"
   * - Probability
     - payer.name1
     - "string"
   * - Probability
     - payer.name2
     - "string"
   * - Probability
     - payer.sendInvoicesTo
     - "string"
   * - Probability
     - payer.sendMailTo
     - "string"
   * - Probability
     - payer.socialSecurityNumber.iso2Letter
     - "string"
   * - Probability
     - payer.socialSecurityNumber.number
     - "string"
   * - Probability
     - payer.url
     - "string"
   * - Probability
     - payments.amount
     - "string"
   * - Probability
     - payments.financeDimensions.department
     - "string"
   * - Probability
     - payments.financeDimensions.dimension3
     - "string"
   * - Probability
     - payments.financeDimensions.dimension4
     - "string"
   * - Probability
     - payments.financeDimensions.dimension5
     - "string"
   * - Probability
     - payments.financeDimensions.productIdentification
     - "string"
   * - Probability
     - payments.financeDimensions.url
     - "string"
   * - Probability
     - payments.financeStatus
     - "string"
   * - Probability
     - payments.id
     - "string"
   * - Probability
     - payments.invoiceId
     - "string"
   * - Probability
     - payments.invoiceLink
     - "string"
   * - Probability
     - payments.paymentDate
     - "string"
   * - Probability
     - payments.paymentIdentification
     - "string"
   * - Probability
     - payments.paymentSystemCardType
     - "string"
   * - Probability
     - payments.paymentType
     - "string"
   * - Probability
     - payments.shopOrderId
     - "string"
   * - Probability
     - payments.url
     - "string"
   * - Probability
     - payments.voucherNo
     - "string"
   * - Probability
     - recurringPaymentIdentification
     - "string"
   * - Probability
     - sendInvoiceTo
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.addressDescription
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.addressLineOne
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.addressType
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.attention
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.careOf
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.country
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.end
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.floor
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.formattedAddress
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.id
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.lastChange
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.letter
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.location
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.municipality
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.number
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.postOfficeBox
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.postalCode
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.start
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.street
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.streetAndZipOneLine
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.suite
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.url
     - "string"
   * - Probability
     - sendInvoiceTo.addresses.zipCityCountry
     - "string"
   * - Probability
     - sendInvoiceTo.anonymizedOn
     - "string"
   * - Probability
     - sendInvoiceTo.businessNumbers.debtorLink
     - "string"
   * - Probability
     - sendInvoiceTo.businessNumbers.productionNumber
     - "string"
   * - Probability
     - sendInvoiceTo.businessNumbers.registrationNumberCVR
     - "string"
   * - Probability
     - sendInvoiceTo.businessNumbers.registrationNumberNorwegianCompanyNumber
     - "string"
   * - Probability
     - sendInvoiceTo.businessNumbers.registrationNumberSwedishCompanyNumber
     - "string"
   * - Probability
     - sendInvoiceTo.businessNumbers.registrationNumberVAT
     - "string"
   * - Probability
     - sendInvoiceTo.businessNumbers.registrationNumbersRUT
     - "string"
   * - Probability
     - sendInvoiceTo.businessNumbers.registrationNumbersSE
     - "string"
   * - Probability
     - sendInvoiceTo.businessNumbers.url
     - "string"
   * - Probability
     - sendInvoiceTo.closeDate
     - "string"
   * - Probability
     - sendInvoiceTo.closeReason.description
     - "string"
   * - Probability
     - sendInvoiceTo.closeReason.id
     - "string"
   * - Probability
     - sendInvoiceTo.closeReason.url
     - "string"
   * - Probability
     - sendInvoiceTo.closeReason.valid
     - "string"
   * - Probability
     - sendInvoiceTo.contacts.end
     - "string"
   * - Probability
     - sendInvoiceTo.contacts.id
     - "string"
   * - Probability
     - sendInvoiceTo.contacts.lastChange
     - "string"
   * - Probability
     - sendInvoiceTo.contacts.start
     - "string"
   * - Probability
     - sendInvoiceTo.contacts.type
     - "string"
   * - Probability
     - sendInvoiceTo.contacts.url
     - "string"
   * - Probability
     - sendInvoiceTo.contacts.value
     - "string"
   * - Probability
     - sendInvoiceTo.customFieldValues
     - "string"
   * - Probability
     - sendInvoiceTo.dafualtPayerRule
     - "string"
   * - Probability
     - sendInvoiceTo.debtorAccountNumber
     - "string"
   * - Probability
     - sendInvoiceTo.defaultAddressType
     - "string"
   * - Probability
     - sendInvoiceTo.defaultPayerLink
     - "string"
   * - Probability
     - sendInvoiceTo.ean
     - "string"
   * - Probability
     - sendInvoiceTo.einvoiceEan
     - "string"
   * - Probability
     - sendInvoiceTo.einvoiceEmail
     - "string"
   * - Probability
     - sendInvoiceTo.emailForInvoices
     - "string"
   * - Probability
     - sendInvoiceTo.externalId
     - "string"
   * - Probability
     - sendInvoiceTo.financeType
     - "string"
   * - Probability
     - sendInvoiceTo.honorific
     - "string"
   * - Probability
     - sendInvoiceTo.invoiceDistributionPreference
     - "string"
   * - Probability
     - sendInvoiceTo.invoicesLink
     - "string"
   * - Probability
     - sendInvoiceTo.lastChange
     - "string"
   * - Probability
     - sendInvoiceTo.memberType
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.affiliateDate
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.affiliationReason 
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.affiliationSource 
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.applicationDate
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.applicationProcessDate
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.applicationStatus
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.applicationStatusComment
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.closeDate
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.description
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.disaffiliateDate
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.disaffiliateReason 
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.enableGeographic
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.feeExempt
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.id
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.member 
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.membershipCategory 
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.membershipWeights 
     - "string"
   * - Probability
     - sendInvoiceTo.memberships.url
     - "string"
   * - Probability
     - sendInvoiceTo.name
     - "string"
   * - Probability
     - sendInvoiceTo.name1
     - "string"
   * - Probability
     - sendInvoiceTo.name2
     - "string"
   * - Probability
     - sendInvoiceTo.sendInvoicesTo
     - "string"
   * - Probability
     - sendInvoiceTo.sendMailTo
     - "string"
   * - Probability
     - sendInvoiceTo.socialSecurityNumber.iso2Letter
     - "string"
   * - Probability
     - sendInvoiceTo.socialSecurityNumber.number
     - "string"
   * - Probability
     - sendInvoiceTo.url
     - "string"
   * - Probability
     - source
     - "string"
   * - Probability
     - url
     - "string"


ZohoCRM Account to MemberCare Countries
---------------------------------------
Every ZohoCRM Account will be synchronized with a MemberCare Countries.

Once a link between a ZohoCRM Account and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - Billing_Country
     - name
     - "string"
   * - Industry
     - name
     - "string"
   * - Shipping_Country
     - name
     - "string"


ZohoCRM Contact to MemberCare Countries
---------------------------------------
Every ZohoCRM Contact will be synchronized with a MemberCare Countries.

Once a link between a ZohoCRM Contact and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - Mailing_Country
     - name
     - "string"
   * - Other_Country
     - name
     - "string"

