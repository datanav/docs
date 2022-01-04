Non-idempotency
===============

Within a Sesam node, there is typically a set of source and target systems.
These systems read and write data either into or out of a given dataflow defined in Sesam pipes.
It is important to recognize that reading and writing data from and to a given system can result in different behavior.
Therefore, we will now discuss a term called idempotency.

Operations can be divided into idempotent and non-idempotent. These are quite different in terms of behavior:

- Idempotent operations have no side-effects if performed multiple times, i.e.: Reading data from a source system and displaying the result.
- Non-idempotent operations, however, can evaluate differently if performed multiple times, i.e.: Writing a change to a bank account.

In essence, you should be aware of how your source and/or target system will respond when provided with data multiple times. Know your systems.


The Challenge
-------------
The challenge with non-idempotent systems is that you can get different results every time you use an operation against them. As an example, imagine trying to update a record in a RESTful system using the POST method. The POST method will add a new record which can be challenging in that the new record might look different in terms of payload with regards to the already existing payload of the record in question. As such, the POST method is non-idempotent and the record that was to be updated remains unchanged. However, using the PUT method will ensure that the record you want to update will be overwritten by the data provided in the payload. Every time PUT is used this will happen. Therefore, PUT is an idempotent method.

To cope with the non-idempotency within a POST method, it is imoortant to build functionality that brings idempotency into the equation in order to avoid unexpected results. This, however, adds complexity. As an example, imagine solving this for a RESTful API:

- Initially check if there is similar data residing in the API. This can be done using the GET method.
- If the result from the GET shows that no such data exists, use a POST method and create a new record.
- However, if the result from the GET method shows related data residing in the system, you should first use the DELETE method to delete existing data followed by the POST method to create a new record.

As outlined in the example, complexity increases when coping with non-idempotent systems.


Piece of Advice
---------------
It is good practice to analyze the target systems on how they are functioning, i.e. are they built with functionality which resembles non-idempotency?

Making sure the answer to that question is correct, surprises and unexpected results caused by non-idempotency or non-idempotent-like behavior can be avoided.
