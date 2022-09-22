Avoid unnecessary load on source systems
----------------------------------------

For sources that support incremental sync and where pulling all the data might incur additional cost, system instability or other problems, your first pipe in Sesam should just make a clean copy of the data. You should add namespaces and do any other transformations in a secondary pipe, so that you are able to modify these transformations later without causing unnecessary load on the source system.
