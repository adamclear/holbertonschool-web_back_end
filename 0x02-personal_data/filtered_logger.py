#!/usr/bin/env python3
''' This module contains the class RedactingFormatter and other functions
related to its use. '''
import logging
import mysql.connector
import os
import re
from typing import List


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        ''' Class initialization. '''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        ''' Formats the log record. '''
        return filter_datum(self.fields,
                            self.REDACTION,
                            super().format(record),
                            self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    ''' Returns a log message with sensitive data obfuscated. '''
    return re.sub(
        '|'.join(f"(?<={field}=).*?(?={separator})" for field in fields),
        redaction,
        message
    )


def get_logger() -> logging.Logger:
    ''' Creates and defines a logger. '''
    user_data = logging.getLogger('user_data')
    user_data.setLevel(logging.INFO)
    user_data.propagate = False
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(RedactingFormatter(PII_FIELDS))
    user_data.addHandler(streamHandler)
    return user_data


def get_db() -> mysql.connector.connection.MySQLConnection:
    ''' Establishes connection to the database. '''
    return mysql.connector.connect(
        host=os.environ.get('PERSONAL_DATA_DB_HOST'),
        database=os.environ.get('PERSONAL_DATA_DB_NAME'),
        user=os.environ.get('PERSONAL_DATA_DB_USERNAME'),
        password=os.environ.get('PERSONAL_DATA_DB_PASSWORD')
    )


def main():
    ''' Retrieves all rows in the users table and displays them. '''
    db = get_db()
    log = get_logger()
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users;')
    for row in cursor:
        log.warning('; '.join(f'{key}={value}' for key, value in row.items()))
    db.close()


if __name__ == '__main__':
    main()
