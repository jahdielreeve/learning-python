## ✨ Operators

`//` → Integer division (drops decimals)

**Table: Math Operators**

| Operator | Operation | Example | Result |
|---------|-----------|---------|--------|
| `**` | Exponentiation | `2 ** 3` | 8 |
| `%` | Modulus / Remainder | `22 % 8` | 6 |
| `//` | Integer Division | `22 // 8` | 2 |
| `/` | Division | `22 / 8` | 2.75 |
| `*` | Multiplication | `3 * 5` | 15 |
| `-` | Subtraction | `5 - 2` | 3 |
| `+` | Addition | `2 + 2` | 4 |

---

## 🔤 Data Types

- **Concatenate strings** → `"hello" + "world"`
- **Replicate strings** → `"ha" * 5`

---

## 📦 Variables

Variables behave like **boxes in memory** that store values.

### 🟢 Initialization  
First time a value is stored.

### 🔄 Overwriting  
Assigning a new value replaces the old one.

Example:
```python
spam = "Hello"
spam = "Goodbye"
```

### 🏷️ Variable Naming Rules
✔️ Valid Names

- current_balance
- currentBalance
- account4
- _42
- TOTAL_SUM
- hello

❌ Invalid Names

- current-balance (no hyphens)
- current balance (no spaces)
- 4account (cannot start with number)
- 42 (numbers alone not allowed)
- TOTAL_$UM (no special chars like $)
- 'hello' (no quotes in variable names)