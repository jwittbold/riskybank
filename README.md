# RiskyBank - Springboard Data Engineering OOP Project

RiskyBank is a simple mock ATM/Banking application run via the command line. 
The program takes members personal info and adds it to a PostgreSQL database. 
Members can open accounts and make various transactions such as deposits, withdrawals, balance inquiries, as well as submit applications for financial products such as  loans and credit cards. Member, Account, and Product database tables are all linked via SQLAlchemy Object Relational Mapping (ORM).

![RiskyBank Banner](/screenshots/riskybank_banner.png)

## Installation Requirements

RiskyBank is written in Python 3.8 and utilizes SQLAlchemy and a PostgreSQL database. To run RiskyBank on your machine you will first need to have the following software installed:

Python 3
https://www.python.org/downloads/

PostgreSQL
https://www.postgresql.org/download/

SQLAlchemy
```
pip install SQLAlchemy
```
psycopg2 
```
pip install psycopg2
```

Once the requisite software is installed, you can proceed to download the RiskyBank GitHub repository.

Upon download, locate the file 'config.toml', which you must modify to match your  own PostgreSQL login credentials.

![PostgresSQL Config](/screenshots/database_settings_example.png)

To run RiskyBank, open a new terminal window and navigate to the downloaded folder titled 'riskybank-master' containing all of the application module files. 

Launch Python and RiskyBank witht following command:
```
python3 main.py <kbd>Enter</kbd>
```

You should now be at the entrance of the program.


## Usage

RiskyBank takes users input to operate the program. Users are prompted with common questions regarding personal details for the purpose of opening a new account. 

![Member Info](/screenshots/jeffrey_lebowski.png)

New users are also required to open an account in order for their member info to be saved to the database.

![Mandatory Account](/screenshots/larry_sellers.png)



## Release History

* 0.1.0
    * Initial release.


## Meta

Jack Wittbold / jwittbold@gmail.com

Distributed under the MIT License. See ``LICENSE`` for more information.
