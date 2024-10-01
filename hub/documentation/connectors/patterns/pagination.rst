Pagination
==========

Pagination in an API is a technique used to split large sets of data into smaller, manageable chunks. Instead of returning all data in one response (which can be slow and resource-intensive), the API delivers it in "pages," making the responses faster and easier to handle reducing the load on the API server.

Key concepts
------------
Key concepts in pagination:

1. Page Size (Limit): Specifies the number of records per page.
    * Example: ``?limit=10`` (returns 10 records).
2. Page Number/Offset: Indicates which page of data you're requesting.
    * Example: ``?page=2`` (fetches the second page).
    * Or ``?offset=10&limit=10`` (fetches the next set of 10 records, starting from record 11).
3. Next/Previous Links: APIs often return links to the next page to simplify navigation including a token to use in the next API call.
    * Based on the API this information might be included in the response header or body or none of them. for example, Shopify includes this information in the response header but HubSpot includes it in the response body. but webCRM does not return back page info.

Pagination patterns
-------------------
There are two common pagination patterns:

1. Offset-based pagination: Uses an offset to specify the starting point of the data set.
    * Example: ``?offset=10&limit=10`` (fetches the next set of 10 records, starting from record 11).
2. Cursor-based pagination: Uses a cursor to specify the starting point of the data set.
    * Example: ``?cursor=eyJpZCI6IjEw``
    * The cursor is a unique identifier for a specific record in the data set. The API uses this identifier to fetch the next set of records.

Implementing pagination in a connector
--------------------------------------
When building a connector, it's headeressential to implement pagination correctly. Here are some best practices:

1. Use the page size (limit) parameter to control the number of records per page.
    * define ``"page_size": <page_size>``, in the system configuration. page_size of 100 is a common default.
2. Use the page or offset parameter to specify which page of data you're requesting. update url in system configuration:
    * Example: ``"url": "https://api.example.com/v1/data?limit={{page_size}}"``
3. Include next link in the response to simplify navigation. Update next_page_link in system configuration:
    * Use Jinja conditional statements to check if the next link is available.
    * Example: ``"next_page_link": "{%if (headers.link.next is defined)%}{{headers.link.next}}{%endif%}"``
    * Some APIs don't return back next page link (e.g. webCRM). In this case you might need to use previous API call parameters to retrieve next page (depends on how the API supports it)
4. Implement termination conditions to stop fetching data when there are no more pages.
    * Example: ``"next_page_termination_strategy": ["next-page-link-empty", "empty-result", "not-full-page"]``

Example: system config with pagination
--------------------------------------

::

   "<datatype>-list": {
      "id_expression": "{{ <datatype> }}",
      "method": "GET",
      "next_page_link": "{%if (headers.link.next is defined)%}{{headers.link.next}}{%endif%}",
      "next_page_termination_strategy": [
        "next-page-link-empty"
      ],
      "page_size": 100,
      "url": "https://api.example.com/v1/data?limit={{page_size}}"
    }

Example: system config with pagination (incrementing previous parameter)
------------------------------------------------------------------------

::

   "<datatype>-list": {
      "id_expression": "{{ <datatype> }}",
      "method": "GET",
      "next_page_link": "<query_endpoint>",
      "next_page_termination_strategy": [
        "next-page-link-empty"
      ],
      "params": {
        "Page": "{% if previous_params.Page is not defined %}1{% else %}{{ previous_params.Page|int+1|int }}{% endif %}",
        "Size": 100
      },
      "url": "https://api.example.com/v1/data?limit={{page_size}}"
    }