# Factory Method

- Define an interface for object creation.
- Provides different ways to define the object to be returned.

## Intent

### Problem

- Code dependency of no-general entity classes.
- Decentralized creation of specialized entities.

### Solution

- Separates the object creation from other logics.
- Replaces the object creation by **Factory** method.
- The Factory returns a **Product** object of appropriate type and with correct parameters.

## Motivation

- Decouple the **Product** creation from its use logic.
- Make easy the implementation of new **Products**.

## Structure

1. The **Product** declares an interface (**Abstract Products**), which is common to all objects that can be produced by the creator and its subclasses.
2. **Concrete Products** are different implementations of the product interface.
3. The **Creator** class declares the factory method that returns new product objects.

  1. The factory method returns an **Abstract Product**.
  2. The factory method can be implemented by **inheritance** (overriding the base class method) or **decision tree** (processing parameters to define **Concrete Product** type).
  3. The **Product** creation is not the primary responsibility of the creator.
  4. **Products** can be created or reused from cache or **Product Pool**.

4. **Creators** can be implemented as an **Abstract Class** to force the re-implementation of **Factory Method** by the **Concrete Creators**.

![Factory Method Structure](images/factory_method_structure.png)

## Applicability

- Use the Factory Method when:

  - You don’t know beforehand the exact types and dependencies of the objects your code should work with.
  - You want to provide users of your library or framework with a way to extend its internal components.
  - You want to save system resources by reusing existing objects instead of rebuilding them each time (**Product Pool**).

## Implementation steps

1. Make all products follow the same interface. This interface should declare methods that make sense in every product.
2. Add an empty factory method inside the creator class. The return type of the method should match the common product interface.
3. In the creator’s code find all references to product constructors. One by one, replace them with calls to the factory method, while extracting the product creation code into the factory method. Maybe it might be necessary to add a temporary parameter to the factory method to control the type of returned product.
4. Now, create a set of creator subclasses for each type of product listed in the factory method. Override the factory method in the subclasses and extract the appropriate bits of construction code from the base method.
5. If there are too many product types and it doesn’t make sense to create subclasses for all of them, you can reuse the control parameter from the base class in subclasses.
6. If, after all of the extractions, the base factory method has become empty, you can make it abstract. If there’s something left, you can make it a default behavior of the method.

## Pros and Cons

| Pros                                                                                                                                      | Cons                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| Avoid tight coupling between the creator and the concrete products.                                                                       | The code may become more complicated. |
| **Single Responsibility Principle**. It moves the product creation code into one place in the program, making the code easier to support. | -                                     |
| **Open/Closed Principle**. It introduces new types of products into the program without breaking existing client code.                    | -                                     |

## Code Examples

- Complexity: **★☆☆**
- Popularity: **★★★**
- Usage: High level of flexibility.
- Identification: Creation methods.
- P.S.: For this example, use the following imports:

```python
from __future__ import annotations
from abc import ABC, abstractmethod
```

### Abstract Creator

- The **Abstract Creator Class** (`Creator(ABC)`) declares the **Factory Method** (`factory_method(self)`) that is supposed to return an object of a **Product Class**. The **Creator's subclasses** usually provide the implementation of this method.
- The **Abstract Creator Class** (`Creator(ABC)`) may provide some the default implementation of the **Factory Method** (`factory_method(self)`), which can be abstract.
- The **Creator**'s primary responsibility is not creating products. Usually, it contains some core business logic that relies on **Product** objects, returned by the factory method. Subclasses can indirectly change that business logic by overriding the factory method and returning a different type of product from it.

```python
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass
    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
```

### Concrete Creators

- **Concrete Creators Classes** (`ConcreteCreator1(Creator)` and `ConcreteCreator2(Creator)`) override the factory method in order to change the resulting product's type.
- The signature of the method still uses the abstract product type, even though the **Concrete Product** is actually returned from the method. This way the **Creator** can stay independent of **Concrete Product Classes** (`ConcreteProduct1(Product)` and `ConcreteProduct2(Product)`).

```python
class ConcreteCreator1(Creator):
    def factory_method(self) -> ConcreteProduct1:
        return ConcreteProduct1()
```

```python
class ConcreteCreator2(Creator):
    def factory_method(self) -> ConcreteProduct2:
        return ConcreteProduct2()
```

### Abstract Product (Product Interface)

- The **Product Interface** (`Product(ABC)`) declares the operations that all concrete products must implement.

```python
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass
```

### Concrete Products

- **Concrete Products** provide various implementations of the **Product Interface**.

```python
class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"
```

```python
class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"
```

### Client Code

- The client code works with an instance of a **Concrete Creator**, albeit through its base interface. As long as the client keeps working with the creator via the base interface, you can pass it any creator's subclass.

```python
def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")
```

### Output

- Execute the following script to run the example:

```shell
➜  design_patterns python3 main.py
```

```plain
App: Launched with the ConcreteCreator1.
Client: I'm not aware of the creator's class, but it still works.
Creator: The same creator's code has just worked with {Result of the ConcreteProduct1}

App: Launched with the ConcreteCreator2.
Client: I'm not aware of the creator's class, but it still works.
Creator: The same creator's code has just worked with {Result of the ConcreteProduct2}
```
