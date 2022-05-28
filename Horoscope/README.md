# Data Access Pattern

---------------------------------------------------------

- In this project we have the business logic ( which is the Horoscope.py class)
```
    The horoscope class calculates whether a student has a good day
    or not
```
- We have the Data Sources which are a xml file or a sql lite local database
```
    SqlDaoFactory.py and XmlDaoFactory.py
```
- We can change Data Sources as we wish because it won't interfere with anything (we are using a data access object, in order to avoid tight coupling)
```
    We can add a new type of factory in DaoFactory.py class
```

## NOTE

---------------------------------
1. In order to run this program just:
    ```bash
        python3 -m main.py
    ```