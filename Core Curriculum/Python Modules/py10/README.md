*This project was developed as part of the 42 curriculum by cabboud.*

# FuncMage

Functional programming in Python, covering lambdas, higher-order functions, closures, `functools`, and decorators.

## Cheat Sheet

| Concept               | Summary                                         |
| --------------------- | ----------------------------------------------- |
| `lambda`              | Short anonymous function                        |
| `map()`               | Transforms every element                        |
| `filter()`            | Keeps elements matching a condition             |
| `sorted()`            | Returns a new sorted list                       |
| First-class functions | Functions can be passed, stored, and returned   |
| Higher-order function | Takes or returns a function                     |
| `Callable`            | Type hint for callable objects                  |
| `callable()`          | Checks if an object is callable                 |
| Closure               | Inner function remembers outer variables        |
| `nonlocal`            | Modifies an enclosing variable                  |
| `reduce()`            | Combines values into one result                 |
| `partial()`           | Pre-fills function arguments                    |
| `lru_cache()`         | Caches function results                         |
| `singledispatch()`    | Selects implementation by first argument's type |
| Decorator             | Adds behavior to a function                     |
| `@wraps`              | Preserves function metadata                     |
| Decorator factory     | Creates decorators with arguments               |
| `@staticmethod`       | Method without `self`                           |

## Exercises

| #  | Exercise        | Main Concepts                                      |
| -- | --------------- | -------------------------------------------------- |
| 00 | Lambda Sanctum  | `lambda`, `map`, `filter`, `sorted`                |
| 01 | Higher Realm    | First-class & higher-order functions, `Callable`   |
| 02 | Memory Depths   | Closures, scope, `nonlocal`                        |
| 03 | Ancient Library | `reduce`, `partial`, `lru_cache`, `singledispatch` |
| 04 | Master's Tower  | Decorators, `args/kwargs`, `wraps`, factories      |

## Key Concepts

**00 — Lambda Sanctum**

* `map()` and `filter()` are lazy; use `list()` when needed.
* `sorted()` creates a new list, while `.sort()` modifies the original.

**01 — Higher Realm**

* `Callable` is a type hint; `callable()` is a runtime check.
* A higher-order function takes **or** returns a function.

**02 — Memory Depths**

* Use `nonlocal` to modify an enclosing variable.
* Closures can provide private state without using a class.

**03 — Ancient Library**

* `lru_cache()` works best with pure functions.
* `partial()` binds arguments in order.
* `singledispatch()` uses the type of the first argument.

**04 — Master's Tower**

* `@decorator` is equivalent to `func = decorator(func)`.
* Use `*args, **kwargs` to support different function signatures.
* `@wraps` preserves function metadata.
* Decorator factories follow: `factory → decorator → wrapper`.
