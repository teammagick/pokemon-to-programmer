# Pokémon to Programmer 🐍

![Pokémon to Programmer cover](%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2%E0%B8%9B%E0%B8%812.jpg)

**Evolve from a complete beginner into a confident programmer—one lesson, experiment, and challenge at a time.**

**Pokémon to Programmer** is a Pokémon-inspired **programming education repository**. The name captures its learning philosophy: begin your journey as a novice, master new skills through practice, and gradually "evolve" into a capable programmer. The emphasis is on real programming knowledge, hands-on experimentation, and steady improvement.

The current learning material consists of **two Python 3 lesson notebooks** and a **Pokédex capstone notebook**, all in English. You begin with the foundations, practice each idea, and finish by independently combining skills in a small, practical project. No prior programming experience is required.

### Learning philosophy

- **Start from zero:** Concepts are introduced in small, approachable steps.
- **Learn by doing:** Execute real code, inspect the output, and change examples to test your understanding.
- **Build mastery progressively:** Treat each new topic as a skill to practice before moving forward.
- **Put skills to use:** Apply lessons through small challenges and self-directed projects.
- **Keep evolving:** Use the fundamentals here as a foundation for increasingly complex programming topics.

The long-term goal is a learning path from **beginner to advanced programming**. The currently implemented notebooks form the **introductory Python stage**; additional programming topics will extend the curriculum over time.

> **For learners:** Start with Lesson 1 below, use the training checkpoints as you go, then complete Lesson 2 and the capstone. The README is a map; the notebooks contain the actual teaching and practice.

## Quick start: Google Colab (no installation)

1. Open **[Lesson 1 in Google Colab](https://colab.research.google.com/github/teammagick/pokemon-to-programmer/blob/main/Python_1_lecture_code.ipynb)**.
2. Sign in to Google if Colab asks you to.
3. Read the first explanation, then press the **▶ Run** button beside a code cell (or press **Shift + Enter**).
4. Read the output directly below the cell. Change a value, run the cell again, and compare the result.
5. Continue from top to bottom. Attempt each **Training Lab** before moving on. Then open **[Lesson 2 in Google Colab](https://colab.research.google.com/github/teammagick/pokemon-to-programmer/blob/main/Python_2_lecture_code.ipynb)**.
6. After Lesson 2, open the **[Pokédex capstone in Colab](https://colab.research.google.com/github/teammagick/pokemon-to-programmer/blob/main/Pokedex_capstone.ipynb)**.
7. To keep your answers, choose **File → Save a copy in Drive**. Your edits to a Colab copy do not change this GitHub repository.

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

JupyterLab should open in your browser. Select `Python_1_lecture_code.ipynb`, choose the Python 3 kernel if prompted, and execute cells with **Shift + Enter**. Later, open `Python_2_lecture_code.ipynb` and then `Pokedex_capstone.ipynb`. To stop JupyterLab, return to the terminal and press **Ctrl + C**. To leave the virtual environment, run `deactivate`.

## Learning path: your first evolution steps

| Order | Notebook | Topics |
| --- | --- | --- |
| 1 | [Python_1_lecture_code.ipynb](Python_1_lecture_code.ipynb) | `print()`, text and separators, arithmetic, operator precedence, comparisons, Boolean logic, data types, type conversion, string case methods, and common errors |
| 2 | [Python_2_lecture_code.ipynb](Python_2_lecture_code.ipynb) | Variables, f-strings, user input, lists and list methods, `len()`/`min()`/`max()`/`sum()`, tuples, sets, set operations, and dictionaries |
| 3 | [Pokedex_capstone.ipynb](Pokedex_capstone.ipynb) | A cumulative Pokédex built from dictionaries, lists, comparisons, formatting, and sets |

The notebooks are designed to be studied **in order**. Each lesson has worked demonstrations and independent self-checking training labs (20 in Lesson 1 and 10 in Lesson 2). Some cells depend on variables defined earlier. If a variable is undefined, run the preceding cells or restart the kernel and use **Run All**.

### How the teaching works: PRIMM

1. **Predict:** Decide what the code will do before running it.
2. **Run:** Execute the working demonstration and inspect the output.
3. **Investigate:** Explain *why* the output happened.
4. **Modify:** Change one feature of the code and rerun it.
5. **Make:** Complete a new task without copying the demonstration.

Training Lab code begins with an unfinished variable (`None`) or a `# TODO` comment. **Fill it in yourself** and rerun the cell. Unfinished checkpoints politely remind you to practice; attempted solutions are checked with `assert` and provide a pass/fail signal. A passed assertion shows the expected result, but you should also explain your approach to demonstrate understanding.

### How to make learning stick

After each study session, revisit one independent task from memory the next day, after 3 days, and after a week. If you struggle, review the relevant worked example and retest yourself on a different question. Record what you can do independently, mistakes worth reviewing, and your next review date in the **[Learning Journal](LEARNING_JOURNAL.md)**. This file is a reusable template, not a user account or automated progress tracker.

## Training method: how to study effectively

1. **Predict:** Before running a cell, guess what it will display.
2. **Execute:** Press Shift + Enter and compare the output with your prediction.
3. **Modify:** Change a string, number, comparison, or collection item, then rerun the cell.
4. **Explain:** Say what changed and why. Consult the official [Python tutorial](https://docs.python.org/3/tutorial/) when a concept is unfamiliar.
5. **Practice:** Make your own copy or add a new cell and solve a small variation without looking at the original.

### Training challenges

- **After Lesson 1:** Print a trainer name, calculate the cost of three Poké Balls, and use Boolean expressions to check whether a trainer meets a chosen level requirement.
- **After Lesson 2:** Store Pokémon names in a list, add a new name with `append()`, use a set to eliminate duplicates, and build a dictionary mapping each Pokémon name to a level.
- **Stretch goal:** Ask for a Pokémon name with `input()` and display its level using an f-string. Remember: `input()` always returns a string until you convert it.

The suggestions above are optional extensions. The 30 built-in Training Labs and Pokédex capstone have local `assert`-based self-checks. There is no hosted account system, automatic submission system, or persistent learner grading database.

## Common issues

| Problem | What to do |
| --- | --- |
| `python` or `python3` not found | Install Python 3 from [python.org](https://www.python.org/downloads/), reopen your terminal, and check `python3 --version` (macOS/Linux) or `py -3 --version` (Windows). |
| `jupyter` not found | Activate `.venv` and run `python -m pip install jupyterlab ipykernel`; then run `python -m jupyterlab`. |
| A variable is undefined (`NameError`) | Run the earlier cell that defines it, or restart the kernel and run cells from the top. |
| A cell prompts for input | Enter a value and press Enter. If a number is expected, enter a valid number. |
| A cell raises an error after you uncomment a line | Some sections intentionally show invalid code. Read the adjacent explanation and comment the line out again to continue. |
| A tuple or set operation fails | Check the data type and the method being used: tuples are immutable; `remove()` on a set raises `KeyError` for a missing item. |

## For contributors and reviewers

- [Teaching Guide](TEACHING_GUIDE.md): PRIMM lesson conventions, check design, mastery and future curriculum plans.
- [Notebook validator](scripts/validate_notebooks.py): validates structure and Python source and runs instructional cells with safe sample input.
- Run `python3 scripts/validate_notebooks.py` before committing. GitHub Actions also runs the check automatically on pull requests and pushes.

## Repository contents

```text
pokemon-to-programmer/
├── Python_1_lecture_code.ipynb  # Lesson 1: Python fundamentals
├── Python_2_lecture_code.ipynb  # Lesson 2: variables and collections
├── Pokedex_capstone.ipynb       # Cumulative beginner project
├── LEARNING_JOURNAL.md          # Spaced retrieval and progress template
├── TEACHING_GUIDE.md            # Teaching methods and contribution standards
├── scripts/validate_notebooks.py # Notebook checks
├── .github/workflows/notebook-checks.yml # Automated checks
├── mix.gif                     # Demonstration animation
├── mix.mp4                     # Demonstration video
├── หน้าปก2.jpg                 # Cover image (original filename retained)
└── README.md                   # This guide
```

![Demo animation](mix.gif)

The media files are illustrative assets; they are **not required** to run the lessons. The original image filename is retained so existing links remain valid.

## Notes for contributors

- Keep lessons approachable to beginners, and use clear English in headings, comments, and displayed messages.
- Keep the PRIMM structure, independent checkpoints, and learner feedback whenever adding new subjects.
- Preserve the notebook cell structure and executable Python examples wherever possible.
- Comment out intentionally broken snippets, explain the expected exception, and make each demonstration safe to skip.
- Avoid committing notebook execution outputs or local virtual environments.
- Test notebook edits with a Python 3 kernel and verify that examples still illustrate the stated concept.

## Further learning

After completing the notebooks and capstone, continue with the official [Python tutorial](https://docs.python.org/3/tutorial/) and [Python standard-library documentation](https://docs.python.org/3/library/). Try extending the practice challenges into a small command-line Pokédex.

---

**Pokémon to Programmer** is an independent, Pokémon-inspired educational project focused on learning to program. Pokémon is a trademark of its respective owners; this learning resource is not affiliated with or endorsed by the Pokémon rights holders.
