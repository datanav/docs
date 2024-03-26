========================
SuperOffice to  Dataflow
========================

Generated: 2024-03-26 00:00:04

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to  Kunde
-----------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a  Kunde must be established.

A SuperOffice Contact will merge with a  Kunde if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Kunde Property
   * - Emails.Value
     - Epost

Once a link between a SuperOffice Contact and a  Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Kunde:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Kunde Property
     -  Data Type
   * - Address.Postal.Address1
     - Gateadresse
     - "string"
   * - Address.Postal.Address1
     - Leveringsadresse
     - "string"
   * - Address.Postal.Address1
     - Postadresse
     - "string"
   * - Address.Postal.Address2
     - Gateadresse
     - "string"
   * - Address.Postal.Address2
     - Leveringsadresse2
     - "string"
   * - Address.Postal.Address2
     - Postadresse
     - "string"
   * - Address.Postal.City
     - LevPoststed
     - "string"
   * - Address.Postal.City
     - Poststed
     - "string"
   * - Address.Postal.Zipcode
     - LevPostNr
     - "string"
   * - Address.Postal.Zipcode
     - Postnr
     - "string"
   * - Address.Street.Address1
     - Gateadresse
     - "string"
   * - Address.Street.Address1
     - Leveringsadresse
     - "string"
   * - Address.Street.Address1
     - Postadresse
     - "string"
   * - Address.Street.Address2
     - Gateadresse
     - "string"
   * - Address.Street.Address2
     - Leveringsadresse2
     - "string"
   * - Address.Street.Address2
     - Postadresse
     - "string"
   * - Address.Street.City
     - LevPoststed
     - "string"
   * - Address.Street.City
     - Poststed
     - "string"
   * - Address.Street.Zipcode
     - LevPostNr
     - "string"
   * - Address.Street.Zipcode
     - Postnr
     - "string"
   * - ContactId
     - Id
     - "string"
   * - Emails.Value
     - Epost
     - "string"
   * - Name
     - Navn
     - "string"
   * - OrgNr (Dependant on having NO in Country.TwoLetterISOCountryDependant on having NO in Country.TwoLetterISOCountryDependant on having wd:Q11994066 in Country.TwoLetterISOCountryDependant on having wd:Q11994066 in Country.TwoLetterISOCountry)
     - Organisasjonsnummer
     - "string"
   * - OrgNr (Dependant on having wd:Q852835 in Country.TwoLetterISOCountry)
     - sesam_kundeId
     - "string"
   * - Phones.Value
     - Telefon
     - "string"
   * - Urls.Value
     - Url
     - "string"


SuperOffice Person to  Ansatt
-----------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a  Ansatt must be established.

A SuperOffice Person will merge with a  Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Ansatt Property
   * - Emails.Value
     - Epost

Once a link between a SuperOffice Person and a  Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Ansatt:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Ansatt Property
     -  Data Type
   * - Address.Street.Address1
     - Adresse
     - "string"
   * - Address.Street.City
     - Poststed
     - "string"
   * - Address.Street.Zipcode
     - Postnummer
     - "string"
   * - BirthDate
     - Fodt
     - "string"
   * - Contact.ContactId
     - AvdelingId
     - "string"
   * - Contact.ContactId
     - Tittel
     - "string"
   * - Contact.ContactId
     - sesam_ansattId
     - "integer"
   * - Firstname
     - Fornavn
     - "string"
   * - Lastname
     - Etternavn
     - "string"
   * - MobilePhones.Value
     - Mobil
     - "string"
   * - PersonId
     - Id
     - "integer"
   * - PrivatePhones.Value
     - TlfPrivat
     - "string"


SuperOffice User to  Ansatt
---------------------------
Before any synchronization can take place, a link between a SuperOffice User and a  Ansatt must be established.

A SuperOffice User will merge with a  Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     -  Ansatt Property
   * - personEmail
     - Epost

Once a link between a SuperOffice User and a  Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a  Ansatt:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     -  Ansatt Property
     -  Data Type
   * - contactId
     - AvdelingId
     - "string"
   * - contactId
     - Tittel
     - "string"
   * - contactId
     - sesam_ansattId
     - "integer"
   * - firstName
     - Fornavn
     - "string"
   * - lastName
     - Etternavn
     - "string"
   * - personEmail
     - Epost
     - "string"


SuperOffice Project to  Prosjekt
--------------------------------
Every SuperOffice Project will be synchronized with a  Prosjekt.

Once a link between a SuperOffice Project and a  Prosjekt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Project and a  Prosjekt:

.. list-table::
   :header-rows: 1

   * - SuperOffice Project Property
     -  Prosjekt Property
     -  Data Type
   * - Associate.AssociateId
     - AnsvarligId
     - "integer"
   * - Name
     - Navn
     - "string"

