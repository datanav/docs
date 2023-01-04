Source with parameterized input pattern
---------------------------------------

Fetch more data based on some input source, requires rescan all the time. Quick summary is to have one pipe fetch the ids, then have another pipe that reads those ids and typically does a rest-transform for each id. Partial rescans might be used if you can limit the number of parameters you need to fetch.
