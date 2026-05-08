import hashlib
from .hash_algorithm import HashAlgorithm

class SHA1Hash(HashAlgorithm):
    @property
    def name(self) -> str:
        return "SHA-1"

    def hash(self, text: str) -> str:
        return hashlib.sha1(text.encode('utf-8')).hexdigest()