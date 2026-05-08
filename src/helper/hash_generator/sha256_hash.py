import hashlib
from .hash_algorithm import HashAlgorithm

class SHA256Hash(HashAlgorithm):
    @property
    def name(self) -> str:
        return "SHA-256"

    def hash(self, text: str) -> str:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()