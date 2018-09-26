# Appliance Data Analysis

[![Build Status](https://travis-ci.com/SamuelHornsey/data-science-portfolio.svg?branch=master)](https://travis-ci.com/SamuelHornsey/data-science-portfolio)
There are 2 main parts to this repo;

1. Jupyter Notebook with data analysis about Appliance energy usage data.
2. Web app with the ML model being used in production

It is recommended to run this app in a virtual environment. Dependencies can be installed using;

```console
pip install -r requirements.txt
```

## How to run the Notebook

To run the notebook;

```console
bash ./bin/notebook.sh
```

## How to run the Web App

There are two ways to run the web app. For development and testing use;

```console
bash ./bin/redis.sh
bash ./bin/web.sh
bash ./bin/celery.sh
```

For a production system;

```console
docker-compose up -d
```