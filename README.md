## How to preview the site

* Create a python3 virtual environment and activate it:

    ```python3 -m venv .python_env```

    ```. .python_env/bin/activate```

     ```pip install --upgrade pip```

    ```pip install wheel```

    ```pip install -r requirements.txt```

Ubuntu specific installation:

  - ``sudo apt install pandoc``
  - ``sudo apt install texlive-latex-base``
  - ``sudo apt install texlive-latex-recommended``


Note that pydata-sphinx-theme requires minimum python 3.7!

* Run ```make html```
* Open ```_build/html/index.html``` in your browser or ```cd _build/html && python3 -m http.server``` to get search summaries

MacOS specific installation:

  - ``brew install pandoc mactex``

Tip: If the ```make html``` command fails, it may be that you need to install some additional
    applications. You can look at the "before_install" section in the ".travis.yml" file to see
    which applications are required.

Use ```SPHINXOPTS= make html_no_saas``` instead of ```make html``` to build the html for the docs without the saas content (requires installation of pandoc locally).
