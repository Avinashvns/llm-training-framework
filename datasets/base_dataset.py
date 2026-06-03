from abc import ABC, abstractmethod
from typing import Any


class BaseDataset(ABC):
    """
    Base abstraction for all datasets used in the framework.

    Every dataset implementation must inherit from this class
    and implement the required methods.
    """

    @abstractmethod
    def __len__(self) -> int:
        """
        Return total number of samples in dataset.
        """
        raise NotImplementedError

    @abstractmethod
    def __getitem__(self, index: int) -> Any:
        """
        Return a single sample from dataset.
        """
        raise NotImplementedError