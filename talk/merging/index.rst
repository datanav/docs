.. _merging:

===============
Merging of data
===============


Introduction
------------

In Sesam Talk, the concept of merging is the process of joining data from two or more datatypes from different systems. The merging of datatypes is important during the initial onboarding of systems as this allows us to reduce the number of duplicate data being inserted into the different systems.

Merging criteria
----------------

One frequent challenge with synchronizing data between systems is the creation of unnecessary duplicates, I.e., how do we know a contact from **System A** does not already exist in **System B**?   

To remedy this situation, we have what we refer to as *merge criterion* between different datatypes. These merge criterion connect data across your systems before we synchronize data to minimize the risk of duplicate creation. For more information about the merge criterion in your specific system please visit the :ref:`supported_systems` section.

Keeping track of inserted data
------------------------------

In addition to merge criteria, Sesam Talk also keeps tracks of the data we create in your system. This means if you create a customer in **System A** that we synchronize to **System B**, these two organizations are linked, regardless of if they share a merge criteria. 


.. admonition::  Note:
   
   * Not all your data might have these merge criteria populated, i.e., you might have **System A** entities that exist in **System B** from before, but without matching merge criteria. In these cases, we would create duplicates for these.  
   * Should entities from the same system share a merge criteria, i.e. two companies share an email, they will be treated as the same company and be synchronized. This will happen regardless of how many systems are connected.


Company duplicates when onboarding Hubspot
---------------------------------------------------

In Talk, there are no identifiers/merge criterions defined for Hubspot Companies. Therefore onboarding Hubspot and another system containing companies with a lot of the same companies will result in a lot of duplicate companies, as we have no identifier to merge overlapping companies by. There is how ever a way that we reccomend in order to avoid duplicates.  

Hubspot has a native **Deduplication functionality** that allows the users to merge duplicate companies. In order to utilize this in the best possible way - follow theese instructions:

#. Ensure that "Sharing of data" is enabled for the Company datatype in the Talk Management Console for Hubspot, and that the other system(s) have disabled "Sharing of data" for the same datatype. This will allow Talk to collect all companies from all systems and store them in Hubspot - creating duplicates in Hubspot where the same company is registered in several systems.
#. Use the Hubspot deduplication feature to merge/combine companies that logically are the same company. `Hubspot Documentation <https://knowledge.hubspot.com/records/merge-records>`_  
#. Email support@sesam.io and let us know that you are done with your clean-up. 

We will then run some backend processes and ensure that the objects that have been merged in Hubspot also merge within Talk and start sharing of Company data to the other systems as well. **The result** of this would be that Company information about a company that was present in Hubspot and another system prior to the Talk onboarding would be shared, and update the company information in both systems - **without generating duplicate records of this company.**  

The **merging of companies in Hubspot is primarily a way to combine different companies/objects based on their system IDs.** It does not controll what information that Talk will retain as the most accurate data. In Talk, **the most recently updated property is considered to be the most accurate one**, and will update older versions of this property. 

**Example:** After onboarding of Hubspot and another system you might end up with a company named "Twitter" and another one named "X" in Hubspot. These are in reality the same company, and you choose to merge "X" into "Twitter" in Hubspot. 

When you do this in Hubspot, the result would be that union of these companies would be named "Twitter" in Hubspot. Talk will pick up that the two companies have merged, but since "X" is a newer name - we consider this name to be **more correct** than "Twitter" and update the company name to "X". The same principle will apply for all properties that we synchronise (besides properties not containing any values - as "old properties" are consideres more correct than "empty properties"). 


.. admonition::  Note:
   
    If you have Hubspot Operations Professional or Enterprise (license level), you can use “bulk-merge” and avoid dealing with each company individually. Hubspot recommends that the domain/URL is included on the companies as this will make the bulk merging easier and more automatic (website/domain/url populated in both Hubspot and your other system).  
 

