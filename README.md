
# Interest Calculator (Fixed & Varying Rates)

A Python project that calculates and plots **simple** and **compound** interest over time, for both:
- A single fixed annual rate  
- A different rate each year (varying rates)

---

## 📌 Overview

This project began as a straightforward “compound vs. simple interest” graph, then evolved into a robust tool that:
1. Accepts a principal amount \(P\) and time period \(T\) (in years).  
2. Handles a **fixed annual rate** \(R_t\) (compounded semi-annually).  
3. Handles **varying annual rates**—one rate per year (also compounded semi-annually).  
4. Computes four series:
   - Fixed-rate Compound Interest  
   - Fixed-rate Simple Interest  
   - Varying-rate Compound Interest  
   - Varying-rate Simple Interest  

The final result is a single plot showing all four curves over \(T\) years.

---

## ⚙️ Features

- **User Inputs**  
  - Principal \(P\) (integer)  
  - Time \(T\) (integer, in years)  
  - A list of \(T\) annual rates (for the varying-rate scenario)  
  - A single fixed annual rate \(R_t\)  
  - Compounding frequency \(n\) (e.g. 2 for semi-annual)

- **Calculations**  
 Formulas (ASCII)

Varying-rate Simple Interest:
A\_vary\_SI(year) = P + sum(P \* r\_i / 100) for i = 1 to year

Varying-rate Compound Interest (compounded n times per year):
P₀ = P
Pᵢ = Pᵢ₋₁ \* (1 + rᵢ / (100 \* n)) ^ n

Fixed-rate Simple Interest:
A\_fixed\_SI(year) = P + (P \* R \* year / 100)

Fixed-rate Compound Interest (compounded n times per year):
A\_fixed\_CI(year) = P \* (1 + R / (100 \* n)) ^ (n \* year)


- **Plotting**  
  - Uses `matplotlib` to produce a single graph with:  
    - Green: Fixed-rate Compound  
    - Red: Fixed-rate Simple  
    - Blue: Varying-rate Compound  
    - Brown: Varying-rate Simple  

---

## 🚀 How to Use

1. **Clone or Download** this repository.  
2. Make sure you have Python 3.x and `matplotlib` installed:
   ```bash
   pip install matplotlib


3. **Run the script**:

   ```bash
   python interest_calculator.py
   ```

4. **Follow prompts**:

   * Enter principal amount (e.g. `100`)
   * Enter time in years (e.g. `10`)
   * Enter each year’s rate when prompted (e.g. `10` for Year 1, `11` for Year 2, …, `19` for Year 10)
   * Enter the fixed rate (e.g. `20`)
   * Enter compounding frequency (for semi-annual, type `2`)

5. **See the output**
   A pop-up window will show the four interest curves over the specified time period.


---

## 🔮 Future Improvements

* **CSV/Excel Export**: Save yearly values to a file for further analysis.
* **User Input Validation**: Reject negative rates or non-numeric entries.
* **Graph Customization**:

  * Add color/marker options.
  * Toggle on/off specific curves.
* **GUI Version**: Use `tkinter` or `PyQt` for a graphical front end.
* **Extend to Other Compounding Frequencies**: Quarterly, monthly, daily.

---

## 🎓 Why This Matters

* **Self-Directed Learning**: You’ll have a concrete Python + Math project to showcase—even “small” projects count.
* **Problem-Solving Story**: The commit history and notes document how you debugged subtle financial-math bugs.
* **Demonstrates Applied Skills**: Combines loops, indexing, data structures, function logic, and plotting in a real-world context.

Feel free to copy, fork, and build on this code. Any feedback or pull requests are welcome!

---

