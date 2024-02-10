"""Conceptual Example."""
from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """Abstract Factory."""

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        """Abstract Product A Creation Method."""

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        """Abstract Product B Creation Method."""


class ConcreteFactory1(AbstractFactory):
    """Concrete Factory 1."""

    def create_product_a(self) -> ConcreteProductA1:
        """Product A1 Creation Method."""
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductB1:
        """Product B1 Creation Method."""
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """Concrete Factory 2."""

    def create_product_a(self) -> ConcreteProductA2:
        """Product A2 Creation Method."""
        return ConcreteProductA2()

    def create_product_b(self) -> ConcreteProductB2:
        """Product B2 Creation Method."""
        return ConcreteProductB2()


class AbstractProductA(ABC):
    """Abstract Product A (Product A Interface)."""

    @abstractmethod
    def useful_function_a(self) -> str:
        """Abstract Operation A Method."""


class ConcreteProductA1(AbstractProductA):
    """Concrete Product A1."""

    def useful_function_a(self) -> str:
        """Concrete Operation A1 Method."""
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
    """Concrete Product A2."""

    def useful_function_a(self) -> str:
        """Concrete Operation A2 Method."""
        return "The result of the product A2."


class AbstractProductB(ABC):
    """Abstract Product B (Product B Interface)."""

    @abstractmethod
    def useful_function_b(self) -> None:
        """Abstract Operation B Method."""

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """Another Abstract Operation B Method."""


class ConcreteProductB1(AbstractProductB):
    """Concrete Product B1."""

    def useful_function_b(self) -> str:
        """Concrete Operation B1 Method."""
        return "The result of the product B1."

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        """Another Abstract Operation B1 Method."""
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    """Concrete Product B2."""

    def useful_function_b(self) -> str:
        """Concrete Operation B2 Method."""
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """Another Abstract Operation B2 Method."""
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"


def client_code(factory: AbstractFactory) -> None:
    """Do comething as Client."""
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())
