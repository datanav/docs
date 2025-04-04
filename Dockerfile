FROM python:3.9.21-slim-bullseye AS build

# same packages and setup as the Github action

RUN apt-get update
RUN apt-get -y install  \
    texlive-latex-base  \
    texlive-latex-extra  \
    texlive-plain-generic  \
    lmodern  \
    texlive-fonts-recommended  \
    ghostscript

RUN apt-get -y install wget
RUN wget https://github.com/jgm/pandoc/releases/download/2.13/pandoc-2.13-1-amd64.deb && dpkg -i pandoc-2.13-1-amd64.deb

# needed for make
RUN apt-get -y install build-essential

WORKDIR /docs
COPY requirements.txt /docs
# to avoid build crash
RUN pip install -U pip setuptools==75.8.0
RUN pip install -r requirements.txt

# sphinx hits an infinite loop after "writing output" if ran on root
# TODO only copy the required files to avoid sphinx when just changing the nginx config
COPY . /docs

# required by sphinx
ENV VIRTUAL_ENV=""

RUN make html

# stage 2

FROM nginx:stable

COPY docker/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /docs/_build/html /usr/share/nginx/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
