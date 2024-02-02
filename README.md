# Stadiums Review App

The Stadiums Review App is a Flask-based web application that allows users to view stadium information and leave reviews for stadiums. The application uses SQLite for storing stadium data and user reviews. It also includes user authentication and authorization features, where only administrators can add, remove, or edit stadium information.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Database](#database)
- [Admin Access](#admin-access)

## Features

- View a list of stadiums with their information.
- Leave reviews for stadiums when logged in.
- User authentication and authorization.
- Admin-only access to add, remove, or edit stadium information.

## Getting Started

Follow these instructions to set up and run the Stadiums Review App on your local machine.

### Prerequisites

Before you begin, make sure you have the following prerequisites installed:

- Python (>=3.6)
- Flask
- Flask-SQLAlchemy
- Flask-Migrate

### Installation

1. Clone the repository:

    git clone https://github.com/yourusername/stadiums-review-app.git

2. Create a .env file with the following content:

    SECRET_KEY=fjlhfewfhewkjfhwefewfkjbvdcsakdlwkjwodcvckxk

3. Run the app.py


### Usage
Access the application in your web browser.
Browse the list of stadiums.
Log in or register to leave reviews.


### Database
The application uses SQLite for the database. The database schema and migrations are managed using Flask-Migrate.

### Admin Access
To access admin features (adding, removing, or editing stadiums), use the following credentials:

Username: admin
Password: admin
