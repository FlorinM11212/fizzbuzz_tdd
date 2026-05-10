# FizzBuzz TDD

SWE6301 Agile Programming — Week 2 activity. FizzBuzz implemented using
Test-Driven Development (Red-Green-Refactor) and small, intentional Git commits.

## Files

- `fizzbuzz.py` — production logic (one function: `fizzbuzz(n)`).
- `test_fizzbuzz.py` — `unittest` test suite.
- `REFLECTION.md` — answers to the Phase 5 reflection questions.

## Run the tests

```bash
python -m unittest test_fizzbuzz.py -v
```

Expected output: `Ran 9 tests ... OK`.

## Commit progression

```
SETUP   -> initialize fizzbuzz project structure and test files
ADD     -> implement initial failing test and simplest logic for number 1
TEST    -> implement and pass divisible by 3 (Fizz) requirement
UPDATE  -> implement Buzz/FizzBuzz logic and refactor for simplicity
REFLECT -> analysis of TDD impact on design and documentation
```
