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
```

> Note:  One drawback of this method includes the API key being available to hackers who may know how to break into containerized processes.
