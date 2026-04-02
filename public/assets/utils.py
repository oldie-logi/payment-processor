import hashlib
import hmac
import os
import secrets
import string
from typing import Dict, Optional


def generate_secure_token(length: int = 32) -> str:
    """
    Generates a cryptographically secure random token.

    Args:
        length: The desired length of the token.

    Returns:
        A random string of the specified length.
    """
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def hash_data(data: str) -> str:
    """
    Hashes the given data using SHA-256.

    Args:
        data: The data to be hashed.

    Returns:
        The SHA-256 hash of the data as a hexadecimal string.
    """
    hashed_data = hashlib.sha256(data.encode('utf-8')).hexdigest()
    return hashed_data


def verify_hmac(data: str, signature: str, secret_key: str) -> bool:
    """
    Verifies the HMAC signature of the given data against a secret key.

    Args:
        data: The data to verify.
        signature: The HMAC signature to compare against.
        secret_key: The secret key used to generate the signature.

    Returns:
        True if the signature is valid, False otherwise.
    """
    try:
        hmac_obj = hmac.new(secret_key.encode('utf-8'), data.encode('utf-8'), hashlib.sha256)
        expected_signature = hmac_obj.hexdigest()
        return hmac.compare_digest(signature, expected_signature)
    except Exception:
        return False


def load_environment_variable(key: str, default: Optional[str] = None) -> str:
    """
    Loads an environment variable.

    Args:
        key: The name of the environment variable.
        default: A default value to return if the variable is not set.

    Returns:
        The value of the environment variable, or the default value if not set.

    Raises:
        ValueError: If the environment variable is not set and no default value is provided.
    """
    value = os.environ.get(key)
    if value is None:
        if default is not None:
            return default
        raise ValueError(f"Environment variable '{key}' is not set.")
    return value


def validate_currency_code(currency_code: str) -> bool:
    """
    Validates that a currency code is a valid 3-letter ISO 4217 currency code.

    Args:
        currency_code: The currency code to validate.

    Returns:
        True if the currency code is valid, False otherwise.
    """
    if not isinstance(currency_code, str):
        return False
    if len(currency_code) != 3:
        return False
    if not currency_code.isalpha():
        return False
    if not currency_code.isupper():
        return False
    return True