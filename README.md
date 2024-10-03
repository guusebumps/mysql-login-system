
# MySQL Login System (PyQt5)

This project is a simple and secure login system built using PyQt5 for the graphical interface and MySQL for the database backend. The system supports user registration and authentication with secure password storage and validation.

## Features

- **User Registration**: Allows users to create new accounts.
- **User Login**: Validates user credentials to log in.
- **Password Security**: Ensures passwords are securely stored in the database.
- **Error Handling**: Provides feedback for incorrect login or registration issues.
- **Database Integration**: Uses MySQL for storing user data.

## Requirements

To run this project, you'll need the following:

- **Python 3.x**
- **PyQt5**: For creating the graphical user interface.
- **MySQL Server**: To manage the user data.
- **Python Libraries**:
  - `mysql-connector-python`
  - `PyQt5`
  - `colorama`

Install the necessary Python libraries using:

```bash
pip install mysql-connector-python PyQt5 colorama
```

## Files

- **initial_screen.ui**: The UI file for the initial screen.
- **login_screen.ui**: The UI file for the login screen.
- **register_screen.ui**: The UI file for the registration screen.
- **main_screen.ui**: The UI file for the main screen after login.

## Database Setup

Before running the application, you need to set up the MySQL database:

1. Install and configure MySQL on your machine.
2. Create a database named `login`:

   ```sql
   CREATE DATABASE login;
   ```

3. Create the `login` table:

   ```sql
   USE login;

   CREATE TABLE IF NOT EXISTS login (
       id INT NOT NULL AUTO_INCREMENT,
       email VARCHAR(110) NOT NULL,
       username VARCHAR(45) NOT NULL,
       password VARCHAR(45) NOT NULL,
       birth_date DATE NULL,
       PRIMARY KEY (id)
   ) DEFAULT CHARACTER SET = utf8mb4;
   ```

4. Update your MySQL credentials in the code if necessary.

## Running the Application

Once the database is set up and the UI files are in place, you can run the application by executing the Python script:

```bash
python main.py
```

### Functionalities

- **Initial Screen**: Choose between logging in or registering.
- **Login**: Input your username and password to authenticate.
- **Register**: Create a new user account with a username, email, and password.
- **Main Screen**: After logging in, the main screen will display the username of the logged-in user.

### Screen Navigation

- The user can navigate between the initial, login, and registration screens easily.
- Error messages are displayed for invalid input or mismatched passwords.

## Future Improvements

- **Session Management**: Add functionality for maintaining user sessions.
- **Password Encryption**: Enhance password storage security with hashing.
- **Password Recovery**: Allow users to recover or reset their passwords.
- **User Profile**: Add the ability for users to update their information.
