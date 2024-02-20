#!/usr/bin/env python3
"""
function called filter_datum:
 -returns the log message obfuscated
 ARGS:
    -fields: list of tsrings representing all fields to obfuscate
    -redaction:string represent what field will be  obfuscated
    -message:  string represent the log line
    -separator: str rep that guide in char separation in msg
Use regex to replace occurance of certain field vals
filter_datum is less than 5 line
uses re.sub to perfom subsititution with single regex
"""
import re
import logging
import csv
import os
import mysql.connector
import mysql.connector
from filtered_logger import get_logger, PII_FIELDS
from get_db import get_db
import bcrypt


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        return super(RedactingFormatter, self).format(record)

    def filter_datum(fields, redaction, message, separator):
        return re.sub(separator.join(fields), redaction, message)

    def get_logger():
        logger = logging.getLogger('user_data')
        logger.setLevel(logging.INFO)
        logger.propagate = False

        handler = logging.StreamHandler()
        formatter = RedactingFormatter(PII_FIELDS)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger

    def get_db():
        db_username = os.environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
        db_password = os.environ.get('PERSONAL_DATA_DB_PASSWORD', '')
        db_host = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
        db_name = os.environ['PERSONAL_DATA_DB_NAME']

        db_connection = mysql.connector.connect(
            user=db_username,
            password=db_password,
            host=db_host,
            database=db_name
        )

        return db_connection

    def main():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users")

        logger = get_logger()
        for row in cursor:
            message = "; ".join(f"{field}={value}"
                                for field, value in
                                zip(cursor.column_names, row))
            logger.info(message)

    def hash_password(password: str) -> bytes:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed

    def is_valid(hashed_password: bytes, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


if __name__ == "__main__":
    main()
