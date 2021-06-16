
.. _sesam-in-the-wild-novice-6-2:

Sesam in the Wild: Novice
-------------------------

.. _novice-topic-6-2:

Novice topic
~~~~~~~~~~~~


.. _creating-mapping-data-for-enrichment-6-2:

Creating mapping data for enrichment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usually an entity with its given properties will convey a concept. Imagine pulling data from a Customer relationship management (CRM) system. The inbound pipe that pulls data from this CRM system is called ``salesforce-person``. If you were to look at the entities in the dataset of this pipe, you will usually be able to understand what the data is all about. For brevity, only one entity is shown below:

.. code-block:: json
	
	{
	  "_id": "salesforce-person:Tordenskjold Skipskaptajnson - Sesam Expert",
	  "salesforce-person:Age": 32,
	  "salesforce-person:CurrentProfession": "Sesam Expert",
	  "salesforce-person:EmployeeStatus": 0,
	  "salesforce-person:EmployeeTime": "5 years",
	  "salesforce-person:FormerProfession": "Semiprofessional footballer",
	  "salesforce-person:Fullname": "Tordenskjold Skipskaptajnson",
	  "salesforce-person:Gender": "Male",
	  "salesforce-person:Nickname": "Joe"

	}  

Which could be semantically defined as an object which is concerned with personal data. This definition is a very general one, as personal data can be many things. Meanwhile, for this specific entity, you could say that it is about the person Tordenskjold Skipskaptajnson whose age is 32 and who has been a Sesam Expert for 5 years. Previously, it seems he persued a career as a footballer, albeit he did not succeed in doing that given his current employment. This is a more detailed semantic definition of the above object.

The above description of the entity is a semantic categorization, as we define its meaning based on our understanding of the words that make up the entity. Albeit, from a semantic point of view, in terms of what can immediately be told from looking at the current state of the data, it seems that one of the properties can only be somewhat vaguely understood. Namely the property ``salesforce-person:EmployeeStatus``. ``EmployeeStatus`` with the value ``0`` can mean many things. In such scenarios you might need to define sub-concepts that will allow you to increase the immediate semantic meaning. 

Imagine you are in charge of sending out salaries for the next month, albeit you are not sure whether or not Tordenskjold Skipskaptajnson is actually an active employee, and so should receive his registered salary. To solve this, you recognize that you need to enrich your data to increase the semantic meaning of the property ``salesforce-person:EmployeeStatus``. This could for example be done by having a mapping dataset containing a semantic description for a range of integers, i.e:

.. code-block:: json
	
	[{
		"_id": "0",
	  "EmployeeStatus": 0,
	  "Description": "On Leave"
	},
	{
		"_id": "1",
	  "EmployeeStatus": 1,
	  "Description": "Active"
	},
	{
		"_id": "2",
	  "EmployeeStatus": 2,
	  "Description": "InActive"
	},
	{
		"_id": "3",
	  "EmployeeStatus": 3,
	  "Description": "Future Employee"
	}]  

Then, if we use a ``hops`` function, we can merge the two datasets on ``EmployeeStatus``. In DTL, this could look like the following:

.. code-block:: json
	
	["merge",
    ["hops", {
      "datasets": ["map-salesforce-person-status md"],
      "where": [
        ["eq", "_S.salesforce-person:EmployeeStatus", "md.EmployeeStatus"] 
      ],
      "return": ["dict", "EmployeeStatusDescription", "md.map-salesforce-person-status:Description"]
    }]
  ]

And would produce the following changes to the dataset produced by the pipe ``salesforce-person``:

.. code-block:: json

	{
	  "_id": "salesforce-person:Tordenskjold Skipskaptajnson - Sesam Expert",
	  "salesforce-person:Age": 32,
	  "salesforce-person:CurrentProfession": "Sesam Expert",
	  "salesforce-person:EmployeeStatus": 0,
	  "map-salesforce-person-status:EmployeeStatusDescription": "On Leave",
	  "salesforce-person:EmployeeTime": "5 years",
	  "salesforce-person:FormerProfession": "Semiprofessional footballer",
	  "salesforce-person:Fullname": "Tordenskjold Skipskaptajnson",
	  "salesforce-person:Gender": "Male",
	  "salesforce-person:Nickname": "Joe"
	}  

As can be seen from the above result, we are now able to tell that Tordenskjold Skipskaptajnson is currently "On Leave", which means that he should not be paid his monthly salary. In addition, this might also mean that he, against the odds, is again persuing a career in football.

The above example shows how a scenario might arise where you need to create sub-concepts of your data to get the required knowledge needed to handle your data appropriately.  


.. _tasks-for-sesam-in-the-wild-novice-6-2:

Tasks for Sesam in the Wild: Novice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
