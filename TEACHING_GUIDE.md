# Teaching Design · Pokémon to Programmer

## Purpose

Pokémon to Programmer is a progressive, self-directed programming education repository. The Pokémon metaphor stands for **skill evolution**. It should support the learning identity, not distract from the actual programming.

The current scope is two introductory Python notebooks and a cumulative Pokédex capstone. The project's longer-term ambition is broader than this implemented scope; avoid claiming that future lessons or automatic grading already exist.

## The five-part teaching routine: PRIMM

Every substantial concept should provide a scaffolded **Predict → Run → Investigate → Modify → Make** path:

1. **Predict:** Ask the learner to commit to an output or behavior before running the example.
2. **Run:** Present a short working demonstration with visible output.
3. **Investigate:** Ask a causal question—how does the operation change a value, type, or program state?
4. **Modify:** Require a small variation on the worked example and compare outcomes.
5. **Make:** Give an independent challenge with a precise observable success criterion and useful feedback.

Do not make the learner search for hidden knowledge. When a MAKE task uses a brand-new API or concept, first add an explanation and worked example. A stretch task can introduce unfamiliar tools if clearly labeled.

## Content rules

- Each topic starts with one small objective and ends with one independent checkpoint.
- Keep concept introductions brief. Prefer examples where the learner can change one thing and observe the effect.
- Never confuse **running a cell** with **mastery**.
- Keep intentionally invalid snippets commented out. State the expected exception and invite learners to uncomment them deliberately.
- Checkpoints should start incomplete, print a reminder, and provide a helpful assertion when attempted. A learner can then run the whole notebook without unfinished exercises crashing it.
- Avoid revealing solutions directly above a MAKE task; tests may show expected results, but questions should encourage actual use of the target operation.
- Include a comparison between what a learner predicted and what actually happened.
- Mix new and old skills in review questions. A successful first attempt does not imply long-term retention.
- Use clear and technically precise English in explanations, code comments, and displayed labels.
- Avoid framework and package dependencies in entry-level Python notebooks unless pedagogically necessary.

## Learner experience

### Lesson structure

```text
Concept objective
    -> Predict
    -> Worked example / Run
    -> Investigate
    -> Modify
    -> Independent MAKE checkpoint
    -> Explanation/reflection
    -> Delayed mixed review
```

### Mastery and retention

Track five states: Encountered, Understood, Applied, Independent, and Retained. Use actual output or explanations to justify the latter three. There is no automated student account or persistence system in the current repository; the [Learning Journal](LEARNING_JOURNAL.md) is the tracking tool.

Recommended recall checkpoints: same day, next day, 3 days, and 7 days. Adjust according to demonstrated recall. Keep one mixed retrieval task per study session after the initial session.

### Feedback design

- Prefer feedback that indicates *what* to review: type mismatch, wrong list order, missing key, case-sensitive comparison.
- On a failure, encourage reading the assertion message and forming a hypothesis before retrying.
- A high-quality check accepts correct solutions regardless of irrelevant formatting choices.
- Avoid giving away the solution merely by confirming whether the code executed.

## Suggested curriculum expansion (not yet implemented)

1. Control flow: if/elif/else
2. Repetition: for and while loops
3. Functions, parameters, return values, scope
4. Strings, slicing, files, JSON
5. Exceptions and structured debugging
6. Modules, tests, and package basics
7. Small command-line projects
8. Object-oriented programming and more advanced Python tools

These should use the same PRIMM and mastery structure. Grow the independent Pokédex project as new topics are taught.

## Quality assurance

Run `python3 scripts/validate_notebooks.py` after changing notebooks. This checks JSON structure, Python syntax in code cells, and the presence of guided learning checkpoints. It does **not** prove all interactive exercises are pedagogically correct or that every cell executes successfully with arbitrary student input. Always manually work through newly created activities in a Python 3 kernel.
