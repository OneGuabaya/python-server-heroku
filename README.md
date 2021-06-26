# What is this repo
It's basically the code of [this article](https://data-addict.com/retrieve-datas-from-postgresql-to-google-sheets-with-heroku-for-free/).
The main goal is to create a Heroku a global controller to retrieve datas from postgreSQL to your Google Sheets spreadsheet.

# How to use it
Just fork the project, and deploy it on Heroku as described on the above article.

# What should I change on the code
Go to `app.py` file > change the global variables with your own:
```
DB_NAME
DB_USERNAME
DB_PASSWORD
```

Consider changing them with some functions if the (DB_NAME,DB_USERNAME,DB_PASSWORD) are not the same depending on your database connection string.

# Cautions
- Once this repo is forked, please keep it as a PRIVATE repo, otherwise it will leak your own database password
- Enabling https by having CORS parts code in `app.py` + creating both files `cert.pem` and `key.pem` is not mandatory
- Don't use this as production server, it's only for demonstration purpose.

# How to run it locally
```
git clone https://github.com/jadynekena/python-server-heroku
cd python-server-heroku
python app.py
```

Then go to `http(s)//127.0.0.1:5000/<YOUR-DB-HOST>/<YOUR-SQL-STATEMENT>/[true]`.
## Important note
- The last parameter is set to `true` if your SQL statement is not a SELECT one.
- Force to https if you enabled CORS. Bypass all security alerts while it's a self-generated certificate, run on localhost.
