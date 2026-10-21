# Evolutionary Algorithms

Python exercises and experiments completed as part of an **Evolutionary Algorithms** course. The repository currently covers data visualization, random number generation, and random search for numerical and combinatorial optimization problems.

## Topics

- Creating line plots, scatter plots, and contour plots with Matplotlib.
- Reading and writing CSV files with pandas.
- Working with arrays and numerical operations using NumPy.
- Generating random integers, floating-point numbers, and permutations.
- Using random seeds to reproduce results.
- Evaluating candidate solutions and selecting the best result found.
- Searching for low-conflict solutions to a 4×4 Sudoku puzzle.

## Repository contents

### Lab 00 — Python tools and visualization

| File | Description |
| --- | --- |
| `AE_Lab00/zad1.py`–`zad5.py` | Basic line and scatter plots, including multiple data series. |
| `AE_Lab00/zad6.py` | Read CSV data and display a scatter plot of coordinates. |
| `AE_Lab00/zad7.py` | Export a sample dataset to `wyniki.csv`. |
| `AE_Lab00/zad8.py` | Convert a pandas DataFrame to a NumPy array. |
| `AE_Lab00/zad9.py` | A random number generator wrapper with seed control and permutation generation. |
| `AE_Lab00/requirements.txt` | Pinned Python dependencies. |

### Lab 01 — Random search

| File | Description |
| --- | --- |
| `AE_Lab01/Zad1.py` | Sample 20 random integers from `[0, 100]` and select the one with the highest function value. |
| `AE_Lab01/Zad2.py` | Evaluate 67 random integer pairs from `[0, 100]²` and visualize the search space using a contour plot. |
| `AE_Lab01/Zad4.py` | Generate and evaluate up to 100 candidate solutions for a 4×4 Sudoku puzzle. |
| `AE_Lab01/czteroku_11.csv` | Input Sudoku puzzle, with `0` representing an empty cell. |
| `AE_Lab01/Wynik.txt` | Saved Sudoku candidates and their error scores. |

The numerical search exercises maximize the following functions:

**One variable:**

```text
f(x) = sin(x / 10) · sin(x / 200)
```

**Two variables:**

```text
f(x₁, x₂) = sin(0.05x₁) + sin(0.05x₂)
            + 0.4 · sin(0.15x₁) · sin(0.15x₂)
```

For Sudoku, each candidate preserves the original clues and fills empty cells with random values from `1` to `4`. Its score counts rows, columns, and 2×2 blocks containing repeated values. Lower scores are better; a score of `0` means a valid solution. The script keeps the best candidate and stops early if it finds a valid solution.

## Getting started

Use Python 3 with NumPy, pandas, and Matplotlib. The supplied dependency file also includes additional packages used by the lab environment.

### 1. Clone the repository

```bash
git clone https://github.com/TomieRR/Evolutionary_Algorithms.git
cd Evolutionary_Algorithms
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r AE_Lab00/requirements.txt
```

### 4. Run an exercise

Run scripts from their respective lab directories so that relative paths to CSV and output files resolve correctly.

For example, to display the CSV coordinate plot:

```bash
cd AE_Lab00
python zad6.py
```

To run the Sudoku experiment from the repository root:

```bash
cd AE_Lab01
python Zad4.py
```

The Sudoku script prints the best candidate and overwrites `Wynik.txt` with the candidates evaluated during the run. Plotting exercises open a Matplotlib window and require a graphical environment.

## Notes

- These are standalone learning exercises, organized by lab.
- Filenames, comments, and console messages are mostly in Polish. `zad` / `Zad` is short for *zadanie* (exercise).
- Random search results can differ between runs and do not guarantee an optimal or valid solution within the sampling budget.
- The current search exercises use independent random sampling; selection across generations, crossover, and mutation are not implemented yet.
