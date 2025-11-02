# Book Collections API

### NOTEs 

- these commands below for now are for macos users only
- the package manager here is Pip, but you may want to use: Pipenv, Poetry or Conda

## Overview

This is just practice in making a simple Restful API using Python Flask with the CRUD HTTP methods for

- fetching and displaying all books in DB
- fetching a specific book based on ID (for now)
- Adding a new book to the DB
- Amending details of an existing book
- Deleting a book

## Installation

1) make sure you have Python3+, if not download from https://www.python.org/downloads/
2) create virtual env to host this API:

```
% python3 -m venv <name of virtual env>
% 
```
3) activate virtual env

```
% source ./bin/activate
(<name of virtual env>) -> % 
```

4) cd into that venv directory
5) clone repository from this github page
6) install dependencies via requirements.txt 

```
(<name of virtual env>) -> % pip install -r requirements.txt
```
7) make sure to manually test by having a rest client installed e.g. postman: https://www.postman.com/downloads/

## Setting up the DB

Data is stored and persisted in ./instance/database.db

```
(<name of virtual env>) -> % python create_db.py
```

NOTE: To delete the DB it will have to be done manually

```
(<name of virtual env>) -> %  rm ./instance/database.db
```

## starting server 

```
 (<name of virtual env>) -> % python main.py

```

### NOTE

main.py contains the entry for running api.py, but you may want to run it in a different way e.g. from the IDE

## Testing

[Postman collection:](https://links.getpostman.com/ls/click?upn=u001.F5oWY2bDM9VsP1yDsg8sVwbp02kBiB-2Brbep9vOjGrAuky9qiMFEKQ093BAloMZP7CKCBxG3x6tDVK-2Ft-2FRoBOuYT4qTY-2BmSGV0lMXmcrjNRR5vIKn7zzRrJyF6zxtBJuUv5TbdvzDzDQ8q1rSnRbBc3zUBMs3wh2DThahnOdd-2Bk4-3D3LC6_n-2BeqlLgD0qEaxBpsPuv9qwFtH8ct1MtdSJUnkABiW1dYLgvhNA9kjkUs5gxsvbhCWQJ2kUYYdvNqkt3apT58MFfArsNDyn1RAguc2tk4k5jcaGoFkeZKgLFFbj-2B9qs9ezMQP9geTj3TReCTS0xrL5-2Bhma1imS3hZAUs-2FsEcboXguKwDKnURqgiWdoSKIZFn3FeCaRsie641goTYBbybFQu4jlI1RMte31IFvCllOmZQVoRCeHQ271BJP4ypMwUrs9-2FnqxmDk-2BR3IClntFqpo7aCvRfVMW7FinLfLf-2BWl06DmRlMti9E2NXgIt4y4wf2eRjabWrz7lvO8JMOaJBe5DIwt63-2B2Tvepexyz-2Fvhq1uOlhl3npVkaNzIrCEvDzdF9gkDKSZuMeHev0E-2BGY5MO13uQFQ2XEgPyf5fnPQf-2FNNc-3D)





