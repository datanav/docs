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
   * Should entities form the same system share a merge critera, i.e. two companies share an email, they will be treated as the same company and be synchronized. 

