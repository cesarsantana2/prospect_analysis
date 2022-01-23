# Python API example (Hexagonal Arch.)

## Overview

Example of an APP built using python3, following Hexagonal Architecture. All the calls made by it are using the Python requests_mock.  

## Instalation

To use this APP example you will setup your enviroment first. 

### Setup

I stronglly recommend to use the [pyenv](https://github.com/pyenv/pyenv) project in order to segregate all libs instaled when testing it. 

### Requiriments

Once you already have setup the enviroment, run the commend below to install all necessary library:

```bash
$ pip install -r requirements.txt
```

## Architecture

As was on said on a previous topic, this APP is following an Hexagonal Architecture model. See the image below:

![Hexagonal_Architecture](resources/hexag.jpg)




### Code Structure

```
.
├── src
|   └── prospect_analysis
│       ├── adapters
|           ├── http.py
|           └── __init__.py
│       ├── diplomat
|           ├── fixtures.py
│           ├── http_in.py
│           ├── http_out.py
|           └── __init__.py
│       ├── domain
│           ├── schema.py
|           └── source.py    
│       └── logic
|           └── national_records.py  
├── test
│   ├── adapters
|       ├── http_test.py
│   ├── diplomat
│   ├── domain
│   └── logic
|       └── national_records.py  
├── README.md
└── requirements.txt

```

## Testing

To ensure the application works correctly, we wrote some tests and tried to anticipate any problems that might appear.

### Running tests

To run the applcation tests make sure that you are at the root repository of it.

### Unit

To run

```bash

$ python3 -m unittest unit/adapters/http_test.py

```