
# MySQL Login System

This project implements a simple and secure login system using MySQL as the database backend and Python as the programming language. The system ensures user authentication through secure password storage, providing a robust base for web applications or any other platform requiring user login functionality.

## Features

- **User Registration**: Create new accounts with secure password hashing.
- **User Login**: Authenticate users against the MySQL database.
- **Password Encryption**: Ensures passwords are stored securely using hashing algorithms.
- **Error Handling**: User-friendly error messages for incorrect login attempts or registration errors.
- **Database Management**: Includes SQL script for creating the necessary database and tables.

## Requirements

To run this project, ensure you have the following installed:

- Python 3.x
- MySQL server
- Python libraries:
  - `mysql-connector-python`
  - `bcrypt`

You can install the required libraries using pip:

```bash
pip install mysql-connector-python bcrypt
```

## Getting Started

### Database Setup

1. Install and configure a MySQL server.
2. Create a database named `login_system` and a table for storing users:
   
   ```sql
   CREATE DATABASE login_system;
   
   USE login_system;
   
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) NOT NULL UNIQUE,
       password VARCHAR(255) NOT NULL
   );
   ```

3. Ensure your MySQL server is running and you have the correct credentials.

### Configuration

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/guusebumps/sistema-de-login-mysql.git
   cd sistema-de-login-mysql
   ```

2. Open `config.py` and update the MySQL connection details:

   ```python
   db_config = {
       'host': 'localhost',
       'user': 'your_mysql_username',
       'password': 'your_mysql_password',
       'database': 'login_system'
   }
   ```

### Running the Application

Once your database is set up and your configuration is complete, you can run the Python script:

```bash
python main.py
```

### Functionalities

- **Register**: Enter a username and password to create a new account.
- **Login**: Authenticate with an existing username and password.

## Future Improvements

- **Session Management**: Add session handling to maintain user login state across different pages.
- **Email Verification**: Implement email confirmation during the registration process.
- **Password Recovery**: Provide users with the option to reset their password via email.


