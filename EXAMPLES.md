# Calculator Examples and Tutorials

A comprehensive guide to using the Simple Python Console Calculator with detailed walkthroughs, use cases, tips, and advanced examples.

## Table of Contents

- [Getting Started Walkthroughs](#getting-started-walkthroughs)
- [Common Use Cases](#common-use-cases)
- [Tips and Tricks](#tips-and-tricks)
- [Troubleshooting](#troubleshooting)
- [Advanced Examples](#advanced-examples)

## Getting Started Walkthroughs

### Walkthrough 1: Your First Addition

Let's start with a simple addition calculation. This walkthrough shows the most basic usage.

**Scenario**: You want to calculate 5 + 3

**Steps**:
1. Open your terminal and navigate to the calculator directory
2. Run the calculator:
   ```bash
   python3 calculator.py
   ```
3. When prompted, enter the first number:
   ```
   Enter the first number: 5
   ```
4. Enter the second number:
   ```
   Enter the second number: 3
   ```
5. Choose the operation:
   ```
   Enter an operation (+, -, *, /): +
   ```
6. View your result:
   ```
   Result: 5.0 + 3.0 = 8.0
   ```

**What You Learned**: The calculator displays results as floating-point numbers for consistency.

---

### Walkthrough 2: Working with Negative Numbers

The calculator handles negative numbers seamlessly!

**Scenario**: You need to calculate -10 + 25

**Steps**:
1. Start the calculator:
   ```bash
   python3 calculator.py
   ```
2. Enter the first number (negative):
   ```
   Enter the first number: -10
   ```
   *The calculator accepts the negative sign naturally*
3. Enter the second number:
   ```
   Enter the second number: 25
   ```
4. Choose addition:
   ```
   Enter an operation (+, -, *, /): +
   ```
5. Result:
   ```
   Result: -10.0 + 25.0 = 15.0
   ```

**Key Point**: Negative numbers work exactly like positive numbers—just include the minus sign!

---

### Walkthrough 3: Decimal Numbers

The calculator works great with decimal values too.

**Scenario**: Calculate 7.5 * 2.4

**Steps**:
1. Start the calculator
2. First number:
   ```
   Enter the first number: 7.5
   ```
3. Second number:
   ```
   Enter the second number: 2.4
   ```
4. Operation:
   ```
   Enter an operation (+, -, *, /): *
   ```
5. Result:
   ```
   Result: 7.5 * 2.4 = 18.0
   ```

**Tip**: The calculator handles both integers and decimals seamlessly using Python's float system.

---

## Common Use Cases

### Use Case 1: Quick Financial Calculations

**Scenario**: You're splitting a restaurant bill.

Total bill: $85.50, Split between 3 people

**Calculation Steps**:
```
=== Simple Console Calculator ===

Enter the first number: 85.50
Enter the second number: 3
Enter an operation (+, -, *, /): /

Result: 85.5 / 3.0 = 28.5
```

**Each person pays**: $28.50

---

### Use Case 2: Unit Conversions

**Scenario**: Convert 100 kilometers to an approximation in miles
(1 km ≈ 0.621371 miles)

**Calculation**:
```
=== Simple Console Calculator ===

Enter the first number: 100
Enter the second number: 0.621371
Enter an operation (+, -, *, /): *

Result: 100.0 * 0.621371 = 62.1371
```

**Result**: Approximately 62.14 miles

---

### Use Case 3: Calculating Discounts

**Scenario**: A store offers 25% off a $60 item. What's the discount amount?

**Calculation**:
```
=== Simple Console Calculator ===

Enter the first number: 60
Enter the second number: 0.25
Enter an operation (+, -, *, /): *

Result: 60.0 * 0.25 = 15.0
```

**Discount**: $15.00
**Final Price**: $60 - $15 = $45.00

---

### Use Case 4: Calculating Total Cost with Tax

**Scenario**: Item costs $50, tax rate is 8%

**Step 1 - Calculate tax amount**:
```
Enter the first number: 50
Enter the second number: 0.08
Enter an operation (+, -, *, /): *

Result: 50.0 * 0.08 = 4.0
```

**Step 2 - Calculate total (run calculator again)**:
```
Enter the first number: 50
Enter the second number: 4
Enter an operation (+, -, *, /): +

Result: 50.0 + 4.0 = 54.0
```

**Total with tax**: $54.00

---

### Use Case 5: Recipe Scaling

**Scenario**: A recipe calls for 2.5 cups of flour, but you want to make half the recipe.

**Calculation**:
```
=== Simple Console Calculator ===

Enter the first number: 2.5
Enter the second number: 0.5
Enter an operation (+, -, *, /): *

Result: 2.5 * 0.5 = 1.25
```

**You need**: 1.25 cups of flour

---

## Tips and Tricks

### Tip 1: Understanding Output Format

The calculator always displays results as decimal numbers (floats). For example:
- Input: `5` and `3` with operation `+`
- Output: `Result: 5.0 + 3.0 = 8.0`

Even though the result is a whole number, the `.0` is shown to indicate it's a float.

### Tip 2: Chaining Calculations

Want to perform multiple calculations? Run the calculator multiple times!

**Example**: Calculate (10 + 5) * 2

Step 1 - First calculation:
```
Enter the first number: 10
Enter the second number: 5
Enter an operation (+, -, *, /): +
Result: 10.0 + 5.0 = 15.0
```

Step 2 - Take the result (15) and run again:
```
python3 calculator.py
Enter the first number: 15
Enter the second number: 2
Enter an operation (+, -, *, /): *
Result: 15.0 * 2.0 = 30.0
```

**Final Result**: 30.0

### Tip 3: Input Flexibility

The calculator accepts various number formats:
- Integers: `5`, `100`, `-42`
- Decimals: `3.14`, `0.5`, `99.99`
- Scientific notation: `1e3` (equals 1000), `2.5e-2` (equals 0.025)
- Negative numbers: `-15`, `-3.14`, `-1e2`

### Tip 4: Operation Quick Reference

Remember these four operations:
- `+` (Plus) - Addition
- `-` (Minus) - Subtraction
- `*` (Asterisk) - Multiplication
- `/` (Slash) - Division

### Tip 5: Working with Large Numbers

The calculator handles very large numbers:
```
Enter the first number: 999999999
Enter the second number: 1000000
Enter an operation (+, -, *, /): *
Result: 999999999.0 * 1000000.0 = 9.99999999e+14
```

Large results are shown in scientific notation for readability.

### Tip 6: Precision in Decimal Calculations

When working with decimals, you may see precision artifacts:
```
Enter the first number: 0.1
Enter the second number: 0.2
Enter an operation (+, -, *, /): +
Result: 0.1 + 0.2 = 0.30000000000000004
```

This is normal in computer arithmetic and doesn't indicate an error. For financial calculations, round the result manually if needed.

---

## Troubleshooting

### Issue 1: "Invalid input! Please enter a valid number."

**Problem**: You entered something that isn't a valid number.

**Common Causes**:
- Typing letters instead of numbers: `five` instead of `5`
- Including extra characters: `$50` instead of `50`
- Space issues: ` 5` might work, but `5 5` will not
- Empty input: Just pressing Enter without typing anything

**Solutions**:
```
❌ Don't do this:
Enter the first number: abc

✅ Do this instead:
Enter the first number: 5
```

**Other valid inputs**:
- `5` ✓
- `5.5` ✓
- `-5` ✓
- `-5.5` ✓
- ` 5 ` ✓ (spaces are trimmed)
- `1e3` ✓ (scientific notation for 1000)

---

### Issue 2: "Invalid operation! Please choose from: +, -, *, /"

**Problem**: You entered an unsupported operation.

**Common Causes**:
- Using the wrong symbol: `x` instead of `*` for multiplication
- Using `^` instead of `*` for exponentiation (not supported)
- Typing the operation name: `plus` instead of `+`
- Typos: `--` instead of `-`

**Solutions**:
```
❌ Don't do this:
Enter an operation (+, -, *, /): x
Enter an operation (+, -, *, /): plus
Enter an operation (+, -, *, /): ^

✅ Do this instead:
Enter an operation (+, -, *, /): *
Enter an operation (+, -, *, /): +
Enter an operation (+, -, *, /): /
```

**Supported Operations Only**:
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division

---

### Issue 3: "Error: Division by zero is not allowed!"

**Problem**: You tried to divide by zero, which is mathematically undefined.

**Common Causes**:
- Accidentally entering `0` as the second number during division
- Misunderstanding the calculation
- Testing the calculator's error handling

**Solutions**:
```
❌ Don't do this:
Enter the first number: 10
Enter the second number: 0
Enter an operation (+, -, *, /): /
Error: Division by zero is not allowed!

✅ Do this instead:
Enter the first number: 10
Enter the second number: 2
Enter an operation (+, -, *, /): /
Result: 10.0 / 2.0 = 5.0
```

**Mathematical Note**: Division by zero has no defined value, so the calculator correctly rejects it with a clear error message.

---

### Issue 4: Unexpected Decimal Results

**Problem**: You expected an integer but got a decimal.

**Example**:
```
Enter the first number: 10
Enter the second number: 4
Enter an operation (+, -, *, /): /
Result: 10.0 / 4.0 = 2.5
```

**Explanation**: The calculator performs true division (not integer division), so 10 ÷ 4 = 2.5, not 2.

This is the correct mathematical result. If you need an integer, manually round or truncate:
- Round: 2.5 rounds to `2` or `3`
- Truncate: Drop the decimal to get `2`

---

### Issue 5: Python Not Found

**Problem**: You see `python3: command not found` or similar error.

**Solutions**:
1. Check Python installation:
   ```bash
   python3 --version
   ```
   
2. Try alternative commands:
   ```bash
   python calculator.py        # Some systems use 'python' not 'python3'
   ```

3. Install Python if needed (consult your system's package manager)

---

### Issue 6: File Not Found

**Problem**: `FileNotFoundError: No such file or directory: 'calculator.py'`

**Solutions**:
1. Verify you're in the correct directory:
   ```bash
   pwd  # Show current directory
   ls   # List files
   ```

2. Navigate to the calculator directory:
   ```bash
   cd path/to/githubRepo5thOct
   python3 calculator.py
   ```

3. Use the full path:
   ```bash
   python3 /home/username/githubRepo5thOct/calculator.py
   ```

---

## Advanced Examples

### Advanced Example 1: Calculating Average of Multiple Numbers

**Scenario**: Find the average of 10, 20, 30, 40

**Method**: (Sum all) ÷ (Count of numbers)

**Calculation Process**:

**Step 1** - Sum the first two numbers:
```
Enter the first number: 10
Enter the second number: 20
Enter an operation (+, -, *, /): +
Result: 10.0 + 20.0 = 30.0
```

**Step 2** - Add the third number:
```
python3 calculator.py
Enter the first number: 30
Enter the second number: 30
Enter an operation (+, -, *, /): +
Result: 30.0 + 30.0 = 60.0
```

**Step 3** - Add the fourth number:
```
python3 calculator.py
Enter the first number: 60
Enter the second number: 40
Enter an operation (+, -, *, /): +
Result: 60.0 + 40.0 = 100.0
```

**Step 4** - Divide by the count (4 numbers):
```
python3 calculator.py
Enter the first number: 100
Enter the second number: 4
Enter an operation (+, -, *, /): /
Result: 100.0 / 4.0 = 25.0
```

**Average**: 25.0

---

### Advanced Example 2: Compound Interest Calculation

**Scenario**: Calculate compound interest
Formula: A = P × (1 + r/n)^t
Where: P = Principal (1000), r = rate (0.05 for 5%), n = times compounded (1 for annually), t = years (3)

Simplified: A = 1000 × (1.05)^3

**Calculation Process**:

**Step 1** - Calculate (1 + 0.05):
```
Enter the first number: 1
Enter the second number: 0.05
Enter an operation (+, -, *, /): +
Result: 1.0 + 0.05 = 1.05
```

**Step 2** - Multiply by itself twice (approximating 1.05^3):
```
python3 calculator.py
Enter the first number: 1.05
Enter the second number: 1.05
Enter an operation (+, -, *, /): *
Result: 1.05 * 1.05 = 1.1025
```

**Step 3** - Multiply once more:
```
python3 calculator.py
Enter the first number: 1.1025
Enter the second number: 1.05
Enter an operation (+, -, *, /): *
Result: 1.1025 * 1.05 = 1.157625
```

**Step 4** - Multiply by principal:
```
python3 calculator.py
Enter the first number: 1000
Enter the second number: 1.157625
Enter an operation (+, -, *, /): *
Result: 1000.0 * 1.157625 = 1157.625
```

**Final Amount**: $1157.63 (after 3 years at 5% annual interest)

---

### Advanced Example 3: Calculating Discounted Price with Multiple Operations

**Scenario**: Original price $200, get 30% off, then add 8% tax
Final Price = (Original - Discount) + Tax

**Calculation Process**:

**Step 1** - Calculate 30% discount:
```
Enter the first number: 200
Enter the second number: 0.30
Enter an operation (+, -, *, /): *
Result: 200.0 * 0.30 = 60.0
```
Discount = $60

**Step 2** - Calculate price after discount:
```
python3 calculator.py
Enter the first number: 200
Enter the second number: 60
Enter an operation (+, -, *, /): -
Result: 200.0 - 60.0 = 140.0
```
Price after discount = $140

**Step 3** - Calculate 8% tax on discounted price:
```
python3 calculator.py
Enter the first number: 140
Enter the second number: 0.08
Enter an operation (+, -, *, /): *
Result: 140.0 * 0.08 = 11.2
```
Tax = $11.20

**Step 4** - Calculate final price:
```
python3 calculator.py
Enter the first number: 140
Enter the second number: 11.2
Enter an operation (+, -, *, /): +
Result: 140.0 + 11.2 = 151.2
```

**Final Price**: $151.20

---

### Advanced Example 4: BMI Calculation

**Scenario**: Calculate Body Mass Index (BMI)
Formula: BMI = weight (kg) / height² (m)

Given: Weight = 75 kg, Height = 1.75 m

**Calculation Process**:

**Step 1** - Calculate height squared:
```
Enter the first number: 1.75
Enter the second number: 1.75
Enter an operation (+, -, *, /): *
Result: 1.75 * 1.75 = 3.0625
```

**Step 2** - Divide weight by height²:
```
python3 calculator.py
Enter the first number: 75
Enter the second number: 3.0625
Enter an operation (+, -, *, /): /
Result: 75.0 / 3.0625 = 24.489795918367346
```

**BMI**: ~24.49

**Interpretation**:
- Under 18.5: Underweight
- 18.5–24.9: Normal weight ✓
- 25–29.9: Overweight
- 30+: Obese

---

### Advanced Example 5: Converting Temperature (Celsius to Fahrenheit)

**Scenario**: Convert 25°C to Fahrenheit
Formula: F = (C × 9/5) + 32

**Calculation Process**:

**Step 1** - Calculate 9/5:
```
Enter the first number: 9
Enter the second number: 5
Enter an operation (+, -, *, /): /
Result: 9.0 / 5.0 = 1.8
```

**Step 2** - Multiply Celsius by 1.8:
```
python3 calculator.py
Enter the first number: 25
Enter the second number: 1.8
Enter an operation (+, -, *, /): *
Result: 25.0 * 1.8 = 45.0
```

**Step 3** - Add 32:
```
python3 calculator.py
Enter the first number: 45
Enter the second number: 32
Enter an operation (+, -, *, /): +
Result: 45.0 + 32.0 = 77.0
```

**Result**: 25°C = 77°F

---

### Advanced Example 6: Creating a Simple Budget Calculator

**Scenario**: Track income and expenses
Income: $3000, Expenses: $2200, Calculate net income

**Calculation Process**:

**Step 1** - Calculate total after expenses:
```
Enter the first number: 3000
Enter the second number: 2200
Enter an operation (+, -, *, /): -
Result: 3000.0 - 2200.0 = 800.0
```

**Net Income**: $800.00

**Step 2** - Calculate savings percentage:
```
python3 calculator.py
Enter the first number: 800
Enter the second number: 3000
Enter an operation (+, -, *, /): /
Result: 800.0 / 3000.0 = 0.26666666666666666
```

**Savings Rate**: ~26.67% (0.267 × 100)

---

## Summary

The Simple Python Console Calculator is a powerful tool for quick calculations. Remember:

✓ **Do**:
- Use simple, clear input
- Handle errors gracefully
- Chain calculations for complex problems
- Round results for readability when needed

✗ **Don't**:
- Try to divide by zero
- Use unsupported operations
- Enter non-numeric values for numbers
- Forget that results are always floats

For more help, check the README.md or review the troubleshooting section above!
