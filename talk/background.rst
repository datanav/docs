##############################
Background Story of Sesam Talk
##############################

In 2022, we set out to explore the potential of Sesam Data Hub to establish a “plug and play” data synchronization service for SaaS business applications. This service would enable users and system owners to seamlessly onboard their systems, facilitating communication between them. In today’s competitive business landscape, organizations often favor best-of-breed solutions over comprehensive legacy business suites. However, seamless data flow across systems typically requires integration expertise and substantial project investments. Our objective was to identify ways to reduce these barriers, both technically and cost-effectively, for organizations seeking improved data quality, consistency, and reduced manual data entry. While the service would not encompass every system property, it would focus on Master Data and other core data types. This concept was christened Sesam Talk. 


Sesam Talk Data Model
=====================
To ensure the concept’s functionality in a multi-tenant environment, we established a standardized data model that would be accessible to all tenants, irrespective of the systems they utilized. 

The final model employed for Sesam Talk was derived from the definitions provided by Wikidata. Wikidata is a document-oriented database that specializes in items, which represent any type of topic, concept, or object. Each item is assigned a unique and persistent identifier. 


Sesam Talk Connectors
=====================
To facilitate seamless communication between systems, Sesam Talk necessitated a standardized connection method. Consequently, we developed specialized connectors for each system, comprising two primary components: the technical connector and the data mapping component.

The technical connector primarily focused on the SaaS systems’ API endpoints, webhooks, authentication mechanisms, and other relevant functionalities. 

The data mapping component, on the other hand, was responsible for mapping the properties of each SaaS system to the Sesam Talk data model. This process also included providing semantic context and descriptions for the properties, thereby enabling differentiation between entities such as human objects from SaaS systems, categorizing them as customers, employees, or both, and distinguishing between suppliers and customers based on organizational data collected from systems. 


Sesam Talk in practice
======================
Upon onboarding a tenant’s SaaS system to Sesam Talk, the connector automatically generates Sesam Data Hub pipes and configuration for that tenant based on the mapping, semantic descriptions, and internal tooling. The data is collected, enriched, and placed into Globals as new objects or merged with existing objects that have been collected from other onboarded systems. 

When the same object has different property values in different systems, the newest update will “win” and propagate as an update to any other system that contains the property.

Sesam Talk had no limitations in terms of the number of systems that you could keep in sync. This enabled multi-master, multi-directional synchronization of data, a scenario where it does not matter where you make a change to an object; it will be synced to all other systems containing that object, as long as the target systems have the changed property associated with it. 
