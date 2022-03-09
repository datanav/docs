FROM python:3.8.12-slim-bullseye
LABEL maintainer="Morten Frellumstad"

WORKDIR /docs
RUN apt-get update \
 && apt-get install --no-install-recommends -y \
      pandoc \
      graphviz \
      imagemagick \
      make \
      git \
      latexmk \
      lmodern \
      fonts-freefont-otf \
      texlive-latex-recommended \
      texlive-latex-extra \
      texlive-fonts-recommended \
      texlive-fonts-extra \
      texlive-lang-cjk \
      texlive-lang-chinese \
      texlive-lang-japanese \
      texlive-luatex \
      texlive-xetex \
      xindy \
      tex-gyre \
 && apt-get autoremove \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /docs
RUN python3 -m pip install --no-cache-dir -U pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt    # Sphinx==4.4.0 Pillow

ENV VIRTUAL_ENV=""
CMD ["make", "html"]