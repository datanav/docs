Datatypes with lists of linked objects
======================================

Some datatypes contain a list of related objects in them. E.g. in Tripletex an order contains a list of orderline identifiers, but not any data about the orderline itself. We handle this by setting up a three step collect pipeline. First we have an ``-all`` pipe that uses ``create-child`` for each of the lines in the order. Then we have an ``-all2`` pipe that emits these children and in the ``-collect`` pipe we look up each of these identifiers. This pattern could probaby be improved a bit.
