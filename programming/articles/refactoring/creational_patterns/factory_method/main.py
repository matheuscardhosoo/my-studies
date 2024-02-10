"""Conceptual Example."""
from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """Abstract Creator."""

    @abstractmethod
    def factory_method(self):
        """Abstract Factory Method."""

    def some_operation(self) -> str:
        """Do something."""
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


class ConcreteCreator1(Creator):
    """Concrete Creator 1."""

    def factory_method(self) -> ConcreteProduct1:
        """Concrete Factory Method 1."""
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    """Concrete Creator 2."""

    def factory_method(self) -> ConcreteProduct2:
        """Concrete Factory Method 2."""
        return ConcreteProduct2()


class Product(ABC):
    """Abstract Product (Product Interface)."""

    @abstractmethod
    def operation(self) -> str:
        """Abstract Operation Method."""


class ConcreteProduct1(Product):
    """Concrete Product 1."""

    def operation(self) -> str:
        """Concrete Operation Method 1."""
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    """Concrete Product 2."""

    def operation(self) -> str:
        """Concrete Operation Method 2."""
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """Do comething as Client."""
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
