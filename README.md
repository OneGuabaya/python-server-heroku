# What is this repo
It's basically the code of [this article](https://data-addict.com/retrieve-datas-from-postgresql-to-google-sheets-with-heroku-for-free/).
The main goal is to create a Heroku a global controller to retrieve datas from postgreSQL to your Google Sheets spreadsheet.

# How to use it
Just fork the project, and deploy it on Heroku as described on the article.

# What should I change on the code
Go to `app.py` file > change the global variables with your own:
```
DB_NAME
DB_USERNAME
DB_PASSWORD
```

Consider changing them with some functions if the (DB_NAME,DB_USERNAME,DB_PASSWORD) are not the same depending on your database connection string.
