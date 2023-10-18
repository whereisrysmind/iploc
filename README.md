# Introduction

This package offers tools for gathering information about IP addresses, using the IPStack API

## Quickstart

### Install toolchain

```bash
poetry install

# or

make install
```

### Run Unit Tests

```bash
make unittest
```

### Set up your .env File

Required valued include:

* `IPSTACK_API_HOST`
* `IPSTACK_API_KEY`

**See [Example Env File](.env.example)**

### Run Functional Tests

```bash
make functest
```

> Requires .env

### Activate Env and Run CLI Tool
```
poetry shell
python main.py 8.8.8.8  
```

## Run with Docker

For convenience sake, this tool has been packed as a docker container.

Execute the CLI tool as a docker container (container name ` whereisrysmind/iploc`) followed by the desired ip address as a positionl arg. See the example below:

```bash
docker run whereisrysmind/iploc:latest 8.8.8.8

> 40.5369987487793 -82.12859344482422
```

The response will return the values directly to the terminal standard out in the form of 'latitude longintude', separated only by a space. This is so the utility can be executed from the context of a unit env, and the result easily piped to another tool.

> Note:  One drawback of this method includes the API key being available to hackers who may know how to break into containerized processes.

## Code Structure

settings.py - Sets up env variables, and specifies required values with Pydantic.
main.py - Defines CLI Tool Entrypoints using Click.
src/schemas.py - Define data structures used by the tool with Pydantic.
src/ipstack.py - Define IPStack Client class
tests/ - Contains unit and functional tests.