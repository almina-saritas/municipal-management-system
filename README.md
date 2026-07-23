# 🏛️ Municipal Management System (CLI)

An Object-Oriented Programming (OOP) project built with Python to efficiently manage municipal personnel, departmental structures, and public infrastructure assets.

---

## 🌟 Key Features

* **Advanced OOP Concepts:**
  * **Encapsulation:** Protects sensitive data like salary info using private attributes (`__salary`) and `@property` getters/setters with validation.
  * **Inheritance:** Extends base `Personnel` class to specialized roles (`SoftwareDeveloper`, `FieldWorker`).
* **Dunder (Magic) Methods:**
  * Uses `__str__` for formatted representation.
  * Implements `__len__` to track total staff directly via `len(system)`.
  * Overloads `__add__` operator for easy calculation of combined asset values.
* **Financial Calculations:** Dynamic methods to calculate total salary budget and asset valuation across the organization.

---

## 🛠️ Tech Stack & Concepts

* **Language:** Python 3.x
* **Core Concepts:** Object-Oriented Programming (OOP), Data Encapsulation, Method Overriding, Operator Overloading.

---

## 🚀 How to Run

1. Clone or download this repository.
2. Run the main script in your terminal:

```bash
python main.py
