# Flask Token Authentication
An implementation of Token authentication in Flask using [Json Web Tokens](https://jwt.io/introduction)

## Overview

Instead of the traditional approach of database-stored token authentication, JWTs allow for authentication
without the need for persisting tokens and querying a database, saving storage space and response time.

### Classic approach
![Classic sequence diagram](images/classic-sequence-diagram.png?raw=true "Title")

### JWT-based approach
![JWT sequence diagram](images/jwt-sequence-diagram.png?raw=true "Title")


## Setup
1. Clone the library
```
git clone https://github.com/alielbashir/flask-token-auth
```

2. Download the app's dependencies
```
python -m pip install -r requirements
```

## Usage
Run the server
```
python app.py
```
