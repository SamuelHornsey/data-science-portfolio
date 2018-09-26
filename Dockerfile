# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:3.6-slim

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=portfolio-work Version=0.0.1

WORKDIR /app
ADD . /app

# Install C compiler
RUN apt-get update && apt-get -y install gcc g++

# Install uwsgi
RUN pip install uwsgi

# Using pip
RUN pip install flask pandas sklearn redis celery scipy

# Clean cache
RUN apt-get clean autoclean
RUN apt-get autoremove --yes
RUN rm -rf /var/lib/apt/

CMD [ "uwsgi", "--http", "0.0.0.0:5000", "--module", "run", "--callab", "app", "--processes", "4" ]

# Using pipenv:
#RUN python3 -m pip install pipenv
#RUN pipenv install --ignore-pipfile
#CMD ["pipenv", "run", "python3", "-m", "portfolio-work"]

# Using miniconda (make sure to replace 'myenv' w/ your environment name):
#RUN conda env create -f environment.yml
#CMD /bin/bash -c "source activate myenv && python3 -m portfolio-work"
