import hashlib
from .hash_algorithm import HashAlgorithm

class SHA512Hash(HashAlgorithm):
    @property
    def name(self) -> str:
        return "SHA-512"

    def hash(self, text: str) -> str:
        return hashlib.sha512(text.encode('utf-8')).hexdigest()