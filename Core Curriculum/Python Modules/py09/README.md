*This project was developed as part of the 42 curriculum by cabboud*

# 42beirut-py09-Cosmic Data

In this module, we will explore  the core features of **Pydantic v2** through space-themed validation problems.

## Exercise 0 – Space Station Data

**Concepts Covered**

* Creating data models using `BaseModel`
* Applying validation rules with `Field()`
* Working with default and optional fields
* Automatically converting values to `datetime`
* Handling `ValidationError`

**Key Features**

* Validating string lengths
* Validating numeric ranges
* Using default values such as `is_operational`
* Defining optional fields such as `notes`

---

## Exercise 1 – Alien Contact Logs

**Concepts Covered**

* Using enumerations with `Enum`
* Implementing custom validation with `@model_validator(mode="after")`

---

## Exercise 2 – Space Crew Management

**Concepts Covered**

* Creating nested Pydantic models
* Working with lists of models
* Implementing validation for more complex data structures

---

Overall, these exercises provide a gradual introduction to Pydantic. They demonstrate how it can be used to validate basic data, apply specific business rules, and handle complex nested structures while producing clear and informative validation errors.

