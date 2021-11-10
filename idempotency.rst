How to handle non-idempotent systems 
====================================
	

Within a Sesam node, there is typically a set of source and target systems. 
These systems read and write data either into or out of a given dataflow defined in Sesam pipes.
It is important to recognize that reading and writing data from and to a given system can result in different behavior. 
Therefore, we will now discuss a term called idempotency.
Operations can be divided into idempotent and non-idempotent. These are quite different in terms of behavior:
	

Idempotent operations have no side-effects if performed multiple times, i.e.: Reading data from a source system and displaying the result.
	

Non-idempotent operations, however, can evaluate differently if performed multiple times, i.e.: Writing a change to a bank account. 
In essence, you should be aware of how your source and/or target system will respond when provided with data multiple times. Know your systems.
	

Non-idempotent APIs (REST or SOAP):
--------------------------------------------------
The problem with non-idempotent systems is that you can get different results every time you use an operation against them. 

Trying to update an entity/record in a RESTful system using the POST method will fail, since the POST method will add a new record. The record that was intended to be updated is still unchanged.
Same will happen every time a POST is used. The POST method is non-idempotent. 

Using the PUT method will ensure that the record you wanted to update is overwritten by the data provided in the PUT. 
Every time PUT is used this will happen. PUT is an idempotent method.

To cope with the non-idempotency within a POST method, one must build functionality that brings idempotency into the equation to avoid unexpected results. 
This, however, adds complexity. 
 
To solve this for a RESTful system, we must first check if there is similar data residing in the system we are using. 
This can be done using the GET method. If the result from the GET shows that no such data exists – we can go on using the POST method. 
However, if the result from the GET method shows related data residing in the system – we must take a slight detour using the DELETE method to delete existing data before using the POST method. After deletion, we are safe to do a POST and write the current shape of the data. 


Transactional APIs or program execution:
----------------------------------------
Transactional APIs are APIs that are not based on sending data using REST or SOAP (PUT, POST), but more on calling programs (drivers) with different methods (new, find, change, delete or query) 
or calling modules from microservices (programs). These programs/modules might have non-idempotency built into them due to system design. 
Behind these programs/modules a relational database might be used. But the system doesn't used the relational database in way that one normally would expect. 
The system might use a business rule-based approach of retrieving and updating data, that depends on function, data, and defined business rules within the system. An example of such systems might be a core banking system – which handles different type products (accounts, cards, loans, cash pools etc.). And they might also be certain business rules applied to different account products. All this must be considered when communicating with such systems. The same function might seem idempotent for one type of product, but non-idempotent for another.
 

Databases:
--------------
In and of itself, a relational database is idempotent, but in practice it might be a good idea to check if a record is present or not anyway. 
In some systems records can be active within a timeframe. 

And due to business rules within an application it is not straightforward to either use UPDATE or INSERT. 
Using UPDATE on existing data might in some cases be judicially illegal due to requirements of audit trail or validity of features of a product. 
E.g., interest rates. You cannot change interest rates to a mortgage immediately (especially when they are increased) – 
you must insert a new record for the new interest rate from a certain date into to the future. 
But the old record will stop you from inserting new interest rates valid from a date in the future.
So, what do we then? We cannot insert data, and we cannot update existing data?
	 
The answer: To insert a new record might require setting the existing record to obsolete(passive) to get a successful insert of a new record. 
The recommended practice is to SELECT the record that fits the data you want to insert. 
We set the existing record to become passive from a certain date in the future (set the to-date as the same date as the from-date of the new data record). 
We have updated the active record with an end-date (still active) and inserted a new record that will automatically be active at a future date.
	

If the data doesn't exist, INSERT can be used without any problem. If data exists, you will get an error from the server saying data already present. 
To handle this, first use UPDATE to set the currently data to obsolete(passive) and then do the insert.
	

Same approach might be useful for old hierarchical database systems as well.

Conclusion:
-----------------
It is a good practice to analyze the target systems on how they are functioning. Are they built with functionality which resembles non-idempotency? 
This will ensure you don't get surprises and unexpected results caused by non-idempotency or non-idempotency-like behavior. 
