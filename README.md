<div align="center">
  <h1>User registration in microservice with FastAPI</h1>
</div>

# Introduction

This repository contains a base project to develop a microservice with FastAPI. The objective of this repository is to structure a base project in FastAPI. This project establishes the necessary folder structure for the domain and services layers, in addition to the tests, in this way, the development stage is simplified so that it focuses on what is really necessary.

# Table of Contents

- [Install dependencies](#install-dependencies)
- [Set environment variables](#set-environment-variables)
- [Create Models](#create-models)
- [Migrations](#migrations)
  - [Create migrations](#create-migrations)
    - [Automatic](#automatic)
    - [Manual](#manual)
  - [Apply migrations](#apply-migrations)
  - [Downgrade migrations](#downgrade-migrations)
- [API entrypoints](#api-entrypoints)
- [Schemas](#schemas)
- [Run server](#run-server)
  - [Development](#development)
  - [Production](#production)
- [Test](#tests)

# Docker

To create de docker image variables must be determined:

```bash
SECRET="my-secret-key"
DEFAULT_EXPIRATION_TIME=30
ALGORITHM = "HS256"
```

After the variables are determined you can build the image:

```bash
docker build -t image_name .
```

To execute the new image you must use the variables determined before:

```bash
docker run -d -e SECRET="my-secret-key" -e DEFAULT_EXPIRATION_TIME=30 -e ALGORITHM="HS256" --name tokenizer -p 80:80 tokenizer
```