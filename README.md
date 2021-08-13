## How to preview the site

* Create a python3 virtual environment and activate it:

    ```python3 -m venv .python_env```

    ```. .python_env/bin/activate```

     ```pip install --upgrade pip```

    ```pip install wheel```

    ```pip install -r requirements.txt```

* Run ```make html```
* Open ```_build/html/index.html``` in your browser

Tip: If the ```make html``` command fails, it may be that you need to install some additional
    applications. You can look at the "before_install" section in the ".travis.yml" file to see
    which applications are required.
