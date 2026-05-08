from abc import ABC, abstractmethod

class HashAlgorithm(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Sesuai atribut '- name: str'"""
        pass

    @abstractmethod
    def hash(self, text: str) -> str:
        """Sesuai dengan '+ hash(text: str) -> str'"""
        pass