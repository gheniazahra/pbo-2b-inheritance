import hashlib
from .hash_algorithm import HashAlgorithm

class MD5Hash(HashAlgorithm):
    @property
    def name(self) -> str:
        return "MD5"

    def hash(self, text: str) -> str:
        return hashlib.md5(text.encode('utf-8')).hexdigest()