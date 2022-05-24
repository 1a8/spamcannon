import base64

import random
import secrets
from concurrent.futures import as_completed

import requests
from requests_futures.sessions import FuturesSession


file = open('data/names.txt', 'r', encoding='utf-8')
USERS = file.read().splitlines()
file.close()


def generate_env() -> list:
    """Create a list of spoofed Windows environment variables

    :return: a variable-length list of fake environment strings
    :rtype: list
    """

    user = random.choice(USERS)
    values = [
        str(random.choice(list(range(2, 257, 2)))),
        'C:\\ProgramData',
        f'C:\\Users\\{user}\\AppData\\Roaming',
        'C:\\Program Files\\Common Files',
        'C:\\Program Files (x86)\\Common Files',
        'C:\\Program Files\\Common Files',
        user,
        'C:\\Windows\\system32\\cmd.exe',
        'C:\\Windows\\System32\\Drivers\\DriverData',
        'C:',
        f'\\Users\\{user}',
        f'C:\\Users\\{user}\\AppData\\Local',
        f'\\\\{user}',
        str(random.choice(list(range(2, 33, 2)))),
        f'C:\\Users\\{user}\\OneDrive',
        'Windows_NT',
    ]

    qty = random.randint(12, 255)
    length = random.randint(4, 255)
    random_strings = [secrets.token_hex(length) for _ in range(qty)]
    values.extend(random_strings)
    random.shuffle(values)
    sample_qty = random.randint(10, qty)
    return random.sample(values, sample_qty)


def encode_env(env: list) -> str:
    """Convert a list of fake environment variable strings to a single space-delimited base64 encoded string

    :param env: list of fake strings
    :type env: list
    :return: base64 encoded string
    :rtype: str
    """

    s = ' '.join(env) + ' '  # Add terminal whitespace because homeboy is a noob
    byte_str = s.encode()
    b64_byte_str = base64.b64encode(byte_str)
    return b64_byte_str.decode('ascii')


def build_url() -> str:
    """Build a URL string comprised of the scheme, netloc, and path.
    Path is built from base64-encoded fake environment variable strings

    :return: URL with base64-encoded data attached
    :rtype: str
    """

    env = generate_env()
    b64_str = encode_env(env)
    return f'https://anti-theft-web.herokuapp.com/hacked/{b64_str}'


def send_requests(n: int) -> int:
    """Send n requests to the server and return the number of errors.

    :param n: number of requests to send at a time
    :type n: int
    :return: error count
    :rtype: int
    """

    errors = 0
    session = FuturesSession()
    futures = [session.get(build_url()) for _ in range(n)]

    for future in as_completed(futures):
        try:
            future.result()
        except requests.exceptions.ConnectionError:
            errors += 1

    return errors
