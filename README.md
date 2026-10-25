# Pokémon to Programmer 🐍

![Pokémon to Programmer cover](%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2%E0%B8%9B%E0%B8%812.jpg)

**Learn Python from the beginning, one executable example at a time.**

Pokémon to Programmer is a beginner-friendly collection of Python lessons in **Jupyter notebooks**. The learning material is available in English. Open the notebooks, read a concept, run its examples, and change the code to see how Python behaves. No programming experience is required.

> **What this repository is:** Two introductory Python lesson notebooks with short exercises and examples. It is not currently an installable Pokémon game, an automated course platform, or a complete advanced-Python curriculum.

## Quick start: Google Colab (no installation)

1. Open **[Lesson 1 in Google Colab](https://colab.research.google.com/github/teammagick/pokemon-to-programmer/blob/main/Python_1_lecture_code.ipynb)**.
2. Sign in to Google if Colab asks you to.
3. Read the first explanation, then press the **▶ Run** button beside a code cell (or press **Shift + Enter**).
4. Read the output directly below the cell. Change a value, run the cell again, and compare the result.
5. Continue from top to bottom. When you are ready, open **[Lesson 2 in Google Colab](https://colab.research.google.com/github/teammagick/pokemon-to-programmer/blob/main/Python_2_lecture_code.ipynb)**.
6. To keep your changes, choose **File → Save a copy in Drive**. Your edits to a Colab copy do not change this GitHub repository.

Google Colab requires a web browser and internet connection. You do not need to install Python locally to use the links above.

## Run locally with JupyterLab

You need **Python 3** and **Git**. The notebooks use Python's standard library; no additional third-party Python libraries are needed for the examples. JupyterLab is required only to open and run the `.ipynb` files locally.

### 1. Download the lessons

```bash
git clone https://github.com/teammagick/pokemon-to-programmer.git
cd pokemon-to-programmer
```

Alternatively, click **Code → Download ZIP** on GitHub, extract it, and open a terminal in the extracted directory.

### 2. Create an isolated Python environment

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyterlab ipykernel
```

**Windows PowerShell:**

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install jupyterlab ipykernel
```

If PowerShell blocks activation, use Command Prompt and run `.venv\Scripts\activate.bat`, or follow the Python documentation for virtual environments. Do not weaken system security settings just for this project.

### 3. Start the notebooks

```bash
jupyter lab
```

JupyterLab should open in your browser. Select `Python_1_lecture_code.ipynb`, choose the Python 3 kernel if prompted, and execute cells with **Shift + Enter**. Later, open `Python_2_lecture_code.ipynb`. To stop JupyterLab, return to the terminal and press **Ctrl + C**. To leave the virtual environment, run `deactivate`.

## Learning path

| Order | Notebook | Topics |
| --- | --- | --- |
| 1 | [Python_1_lecture_code.ipynb](Python_1_lecture_code.ipynb) | `print()`, text and separators, arithmetic, operator precedence, comparisons, Boolean logic, data types, type conversion, string case methods, and common errors |
| 2 | [Python_2_lecture_code.ipynb](Python_2_lecture_code.ipynb) | Variables, f-strings, user input, lists and list methods, `len()`/`min()`/`max()`/`sum()`, tuples, sets, set operations, and dictionaries |

The notebooks are designed to be read **in order**. Each code cell is a small demonstration, and some later cells depend on variables created earlier. If a cell reports that a variable is undefined, run the preceding cells or restart the kernel and use **Run All**.

## How to study effectively

1. **Predict:** Before running a cell, guess what it will display.
2. **Execute:** Press Shift + Enter and compare the output with your prediction.
3. **Modify:** Change a string, number, comparison, or collection item, then rerun the cell.
4. **Explain:** Say what changed and why. Consult the official [Python tutorial](https://docs.python.org/3/tutorial/) when a concept is unfamiliar.
5. **Practice:** Make your own copy or add a new cell and solve a small variation without looking at the original.

### Practice challenges

- **After Lesson 1:** Print a trainer name, calculate the cost of three Poké Balls, and use Boolean expressions to check whether a trainer meets a chosen level requirement.
- **After Lesson 2:** Store Pokémon names in a list, add a new name with `append()`, use a set to eliminate duplicates, and build a dictionary mapping each Pokémon name to a level.
- **Stretch goal:** Ask for a Pokémon name with `input()` and display its level using an f-string. Remember: `input()` always returns a string until you convert it.

These challenges are suggested exercises; the repository does not include an automatic grader.

## Common issues

| Problem | What to do |
| --- | --- |
| `python` or `python3` not found | Install Python 3 from [python.org](https://www.python.org/downloads/), reopen your terminal, and check `python3 --version` (macOS/Linux) or `py -3 --version` (Windows). |
| `jupyter` not found | Activate `.venv` and run `python -m pip install jupyterlab ipykernel`; then run `python -m jupyterlab`. |
| A variable is undefined (`NameError`) | Run the earlier cell that defines it, or restart the kernel and run cells from the top. |
| A cell prompts for input | Enter a value and press Enter. If a number is expected, enter a valid number. |
| A cell raises an error after you uncomment a line | Some sections intentionally show invalid code. Read the adjacent explanation and comment the line out again to continue. |
| A tuple or set operation fails | Check the data type and the method being used: tuples are immutable; `remove()` on a set raises `KeyError` for a missing item. |

## Repository contents

```text
pokemon-to-programmer/
├── Python_1_lecture_code.ipynb  # Lesson 1: Python fundamentals
├── Python_2_lecture_code.ipynb  # Lesson 2: variables and collections
├── mix.gif                     # Demonstration animation
├── mix.mp4                     # Demonstration video
├── หน้าปก2.jpg                 # Cover image (original filename retained)
└── README.md                   # This guide
```

![Demo animation](mix.gif)

The media files are illustrative assets; they are **not required** to run the lessons. The original image filename is retained so existing links remain valid.

## Notes for contributors

- Keep lessons approachable to beginners, and use clear English in headings, comments, and displayed messages.
- Preserve the notebook cell structure and executable Python examples wherever possible.
- Comment out intentionally broken snippets, explain the expected exception, and make each demonstration safe to skip.
- Avoid committing notebook execution outputs or local virtual environments.
- Test notebook edits with a Python 3 kernel and verify that examples still illustrate the stated concept.

## Further learning

After completing both notebooks, continue with the official [Python tutorial](https://docs.python.org/3/tutorial/) and [Python standard-library documentation](https://docs.python.org/3/library/). Try extending the practice challenges into a small command-line Pokédex.

---

**Pokémon to Programmer** is an educational Python notebook collection. Pokémon is a trademark of its respective owners; this project is an independent learning resource and is not presented as an official Pokémon product.
