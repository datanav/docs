Privacy Portal Features
=======================

https://sesam.io/privacy/howitworks/technical-features.html

There are a number of core privacy requirements and Data Subject rights that the Sesam platform delivers on. The following diagram illustrates the core capabilities and flows in a Sesam iPaaS and Data Access Portal solution.

.. image:: https://sesam.io/images/TechnicalDescriptionandFeatures.jpg
  :width: 400
  :alt: Alternative text


Right of Access
^^^^^^^^^^^^^^^^
One of the most fundamental rights in the regulation, is the right of the data subject to get full transparency into all information that a controller has stored about that subject.

Sesam delivers on this right by collecting all data from systems that contain personal data into the datahub. Data about the same Data Subject is then connected together into a single data record. When the Data Subject requests their data via the Data Access Portal a unique private public key pair is generated. The private key is kept in the browser and the public key is uploaded to the portal where it is used to encrypt the Data Subject data record in the datahub. The encrypted record is then stored in the data access portal and delivered to the Data Subjects browser where the private key is used to decrypt the data.

Consent management
^^^^^^^^^^^^^^^^
A Data Subject has the right to review and modify the consents given to a controller. Sesam provides this by allowing the controller to define a privacy definition of the different data types and purposes that exist. These are loaded into Sesam and automatically configured in the Data Access Portal so that a Data Subject can see exactly what processing is occurring on what data. In addition, some processing activities are marked as needing consent. The Data Access Portal dynamically reconfigures based on the data definition provided to give the Data Subject a user interface where they can retract or grant their consent.

Right to be Forgotten
^^^^^^^^^^^^^^^^
A Data Subject should be able to request that they are ‘forgotten’ by a data controller. While data governed by contractual basis cannot be forgotten, data that has been provided by the user must be erased or anonymized when it´s no longer necessary in relation to the purposes for which they where collected and no other legal basis exists, or when consent is withdrawn. Sesam allows the Data Subject to request to be forgotten through the Data Access Portal. This request is collected as data in the Sesam datahub. Sesam knows which personal data is governed by consent and which systems it has come from. It can either send an automated request to the system to update the subject’s data, or it can initiate a workflow process that removes the data from that system. This is a great example of Sesam making non-compliant systems privacy compliant.

Right to Rectification
^^^^^^^^^^^^^^^^
Similar to the right to be forgotten, a Data Subject must be able request corrections to data that has been provided. The Sesam data access portal provides a web interface to allow Data Subjects to request corrections to specific data fields, e.g. email address, phone number etc.

This request is stored in Sesam and can then either be automatically updated in the source system or be used to initiate a manual workflow. Manual workflows are sometimes needed when some verification of the data should be performed.

Right to Portability
^^^^^^^^^^^^^^^^
The right to portability states that a Data Subject should be able to retrieve their data in a machine readable format. The Sesam datahub stores the data it retrieves from different systems as JSON and can also produce data in RDF format. A Data Subject can download this data via the data access portal. The same mechanism to secure the data is used as when viewing the HTML version.

Communication of personal data breach
^^^^^^^^^^^^^^^^
When a personal data breach is detected and likely to result in high risk for the data subjects, the organization shall communicate the breach to the individuals affected. Sesam supports this process by knowing which data subjects have data in affected systems. This allows for only those users to be notified. As part of the notification, the users are NOT sent the data affected, but instead are sent a link to log into the secure Data Access portal. Once in the portal they can see which data has been affected by the breach.

Data Discovery
^^^^^^^^^^^^^^^^
Analyzing business processes and looking at application UIs gives an idea about where personal data is located, but only by looking at the actual databases or files can organizations be sure where personal data is stored. Sesam provides a data discovery component that finds which tables and files contains personal data. Structured databases are scanned to find PII data based on data patterns, naming and other methods. Once these data tables are located, they can be automatically pulled into the Sesam datahub to be delivered via the data access portal. Personal data in files is located by using the structured data as the basis for searching in indexed documents to locate sets of documents that contain personal data.

Anonymisation
^^^^^^^^^^^^^^^^
Anonymisation is crucial in both updating existing systems after a user asks to be forgotten and also for being able to keep data for other processing activities that do not require further consent, such as analytics and machine learning. Sesam can process streams of personal data with third party services that can anonymise data. This process is statistically impossible to reverse to discover the original identity of a data subject.

AGILE DELIVERY OF MULTI-LEVEL INSIGHTS FROM ALL YOUR ENTERPRISE DATA
^^^^^^^^^^^^^^^^
The Sesam iPaaS offering will help you quickly deliver the best results with the lowest costs. Data Hub and spokes architecture for immediate sharing between all systems.