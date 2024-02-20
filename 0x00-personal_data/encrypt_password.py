#!/usr/bin/env python3
    """
User passwords should NEVER be stored in plain text in a database.
Implement a hash_password function that expects one string argument name password and returns a salted, hashed password, which is a byte string.
Use the bcrypt package to perform the hashing (with hashpw)._
"""
import bcrypt

def hash_password(password):
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the generated salt
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

def is_valid(hashed_password, password):
    # Validate the password against the hashed password
      return bcrypt.checkpw(password.encode(), hashed_password)