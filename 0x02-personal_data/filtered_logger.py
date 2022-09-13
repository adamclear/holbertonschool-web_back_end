#!/usr/bin/env python3
''' This module contains the class RedactingFormatter and other functions
related to its use. '''
import re
from typing import List


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
