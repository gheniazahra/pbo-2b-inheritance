from .hash_algorithm import HashAlgorithm

class HashManager:
    def __init__(self, algorithm: HashAlgorithm = None):
        # Sesuai dengan '- algorithm: HashAlgorithm' (private/protected attribute)
        self._algorithm = algorithm

    def set_algorithm(self, algo: HashAlgorithm):
        """Sesuai dengan '+ set_algorithm(algo: HashAlgorithm)'"""
        self._algorithm = algo

    def generate_hash(self, text: str) -> str:
        """Sesuai dengan '+ generate_hash(text: str) -> str'"""
        if not self._algorithm:
            raise ValueError("Algoritma hash belum diatur!")
        
        # Memanggil method hash() dari objek algoritma yang sedang di-set
        return self._algorithm.hash(text)