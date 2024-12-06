##############################
Background Story of Sesam Talk
##############################

In 2022, we set out to explore the potential of Sesam Data Hub to establish a “plug and play” data synchronization service for SaaS business applications. This service would enable users and system owners to seamlessly onboard their systems, facilitating communication between them. In today’s competitive business landscape, organizations often favor best-of-breed solutions over comprehensive legacy business suites. However, seamless data flow across systems typically requires integration expertise and substantial project investments. Our objective was to identify ways to reduce these barriers, both technically and cost-effectively, for organizations seeking improved data quality, consistency, and reduced manual data entry. While the service would not encompass every system property, it would focus on Master Data and other core data types. This concept was christened Sesam Talk. 

Connectors
==========
To facilitate seamless communication between systems, Sesam Talk necessitated a standardized connection method. Consequently, we developed specialized connectors for each system. The connectors where primarily focused on the SaaS systems’ API endpoints, webhooks, authentication mechanisms, and other relevant functionalities. 

Data Model
==========
To ensure the concept’s functionality in a multi-tenant environment, we established a standardized data model that would be accessible to all tenants, irrespective of the systems they utilized. The final model employed for Sesam Talk was derived from the definitions provided by Wikidata. Wikidata is a document-oriented database that specializes in items, which represent any type of topic, concept, or object. Each item is assigned a unique and persistent identifier.

Data Mapping
============
The data mapping component was responsible for mapping the properties of each SaaS system to the Sesam Talk data model and vice versa. This process included providing semantic context and descriptions for each of systems data properties, thereby enabling multilevel differentiation between all data across all systems. 

Tooling
=======
With the model and mapping established all information required to create the data flow was now available. In Sesam Talk we used the data supplied by the model and the mapping in order to automate the creation of configurations for all mapped systems. 

Sesam Talk in practice
======================
Upon onboarding a tenant’s SaaS system to Sesam Talk, the infrastructure automatically deployed the readily available configurations configured for that tenant in real-time. The data was then collected, transformed into our Seasm Talk model and combined with similar data from the tenant’s other systems. 

Once onboarded Sesam Talk applied a “latest version wins”-policy. This meant if full records or record properties existed in several of the tenant’s systems – the latest version of that data would propagate to the other systems as either new or updated records. 

These concepts of multimaster and multidirectional synchronization combined with the established infrastructure allowed Sesam Talk to seamlessly connect new systems to a tenant through a fully automated process as well as ensuring the highest available data quality across all connected systems. 


