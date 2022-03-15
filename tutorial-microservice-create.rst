Workflow
========
Microservices in Sesam run in docker containers. These containers run on our Sesam-node in what we call a system. Below is a visual representation of the flow of hosting our microservice in Sesam.

.. image:: images/getting-started/workflow-ms.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

We start by building a Docker image from our microservice. A Docker image is the blueprint for creating a container with our microservice.

The Docker image is then pushed up to a repository on Docker Hub (or any Docker platform. When hosted in the repository the image can be pulled by anyone with access.

Finally, we pull the image from our Docker Hub repository (although private repositories are also supported) and spin up a container on our Sesam node. The container is created from the image and started. The Docker-commands for this are performed by Sesam. We simply specify the location of the image on Docker Hub in our Sesam system configuration and the container is spun up automatically. Once the Docker image location is defined in the System config Sesam will spin up the correponding container automatically. Finally to transfer data between Sesam datahub and the microservice, we need an inbound pipe or endpoint pipe depending on solution. For example a SQL database sends data to a Sesam pipe via a default microservice available inside your Sesam node, and similarly for data going out of Sesam to target systems.

Microservices with Docker
=========================

First you need to sign up on `Docker <https://www.docker.com>`__ and create a new repository.

.. image:: images/getting-started/Docker-repo.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Then download `Docker Desktop <https://www.docker.com/get-started>`__.

You now need to download Python. Here we're using Python 3.6 but you can use any version after 3.5. Then install pip and Flask.

Flask is a web framework used by Pything to develop web services nad pip is a de facto standard package-management system used to install and manage software packages written in Python. If you need help with this, follow the instructions `here <https://pip.pypa.io/en/stable/installing/>`__ for pip and `here <https://flask.palletsprojects.com/en/1.0.x/installation/>`__ for Flask.

.. image:: images/getting-started/flaskInstall.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

First things first, we need to decice which IDE (integrated development environment) you want to use. In this exercise we will use *Pycharm*, but there are various other options so if you are currently using another one, that is not a problem.

You are now ready to create the microservice. We will generate a folder and a couple of files that a microservice always need to run. Firstly we need to create a **Dockerfile**. A `Dockerfile <https://docs.docker.com/develop/develop-images/dockerfile_best-practices/>`__ is a text file that Docker reads in from top to bottom. It contains instructions which informs Docker *how* the Docker image should get built. To read more about Docker, Docker image, Docker build, it is helpful to browse the `Docker documentation <https://docs.docker.com>`__ . In addition we need to generate the actual program which is stored in a python file (.py).

This is the program that actually runs inside Sesam and tells the system that it is connected to what needs to be done. In this example, it only sends 3 entities with embedded order data. In other cases, the MS must contain authentication to the system (eg basic auth or sql database), or in some cases we have to extract the data in the correct format (such as retrieving OData). All of these .py files (must not be .py, these are only python programs. It could have been .java for java programs, for example) are the "programs" that are running.

In addition we need requirements.txt file which tells the microservice file which libraries this program needs to run. In our example, we only run Flaks so we simply write it in in the following format:

`Flask==1.1.2``

If you want to know more about requirements.txt files, please click `here <https://pip.pypa.io/en/stable/user_guide/#requirements-files>`__


Now let us go through this step by step.

First thing we need is to create a new project in Pycharm. Name your project “Demo_MicroserviceProject”. The files we need to create the Microservices, will be stored inside the project.

Once we have this, we can start by adding the **"Dockerfile"**.

Inside your Demo_MicroserviceProject folder create a new file called "Dockerfile" and paste:

::

  FROM python:3-alpine

  RUN apk update

  RUN pip install --upgrade pip

  COPY ./service/requirements.txt /service/requirements.txt
  RUN pip install -r /service/requirements.txt
  COPY ./service /service

  EXPOSE 5000

  CMD ["python3", "./service/DemoMicroservice.py"]

Once Dockerfile is ready, we create a new folder called "service" inside your project root folder.

.. image:: images/getting-started/MSproject.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Next step is to create the "requirements.txt" inside the "service" folder and paste the following text inside it:

::

 Flask==1.0.2

 If you have a newer version of Flask, you put that in instead of 1.0.2.

Final part is the actual program. For this we create a python file, also in the "service" folder, named "DemoMicroservice.py" with the following code:

::

  from flask import Flask, jsonify

  app = Flask(__name__)

  orders = [
  {
      'id': 1,
      'Username': u'Unjudosely',
      'Orders': u'Thinkpad',
      'TotalSum': 8000
      },
      {
      'id': 2,
      'Username': u'Wimen1979',
      'Orders': u'MacbookPro',
      'TotalSum': 12000
      },
      { 'id': 3,
      'Username': u'Gotin1984',
      'Orders': u'Chormebook',
      'TotalSum': 10000
      }

  ]

  @app.route('/api/orders', methods=['GET'])
  def get_orders():
      return jsonify({'orders': orders})


  if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', port=5000)

.. image:: images/getting-started/DemoService.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Create an image of the microservice in PyCharm's terminal window or any other CLI that you prefer:

::

 docker build -t <docker_username>/<your_repository_name>:<tagname> .

To check that the you have created image run the command:

::

 docker images
