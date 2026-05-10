# Reflection — TDD & the Agile Manifesto through FizzBuzz

## 1. How did "Intentional Programming" influence the design of the function?

Writing the test first forced a public API decision *before* any implementation
existed. The very first test —
`self.assertEqual(fizzbuzz(1), "1")` — fixed three things at once:

- the function is named `fizzbuzz` and lives at module level (importable, not
  buried in a class);
- it takes a single integer argument;
- it returns a **string**, not a number — so callers can print the sequence
  uniformly without having to coerce types themselves.

Had I written the production code first, I would probably have returned an
`int` for numbers and a `str` for "Fizz"/"Buzz", and a caller would have had to
deal with the mixed type. The test made me choose a single, expressive return
type up front. That is Agile Principle 9 ("continuous attention to technical
excellence") in action: the test is a tiny design document that pushed me to
the simpler, more consistent contract.

## 2. In what ways did the unit tests act as "compileable and executable documentation"?

The test file reads like a specification of the rules of the game:

- `test_returns_number_as_string_for_one` and `..._for_two` document the
  default case (return the number as a string).
- `test_returns_fizz_for_three` / `..._for_six` document that "divisible by 3"
  is the rule, not "equal to 3".
- `test_returns_buzz_for_five` / `..._for_ten` do the same for 5.
- `test_returns_fizzbuzz_for_fifteen` / `..._for_thirty` document the
  combined rule and pin down the *exact* spelling "FizzBuzz" (not "Fizz Buzz",
  not "BuzzFizz").
- `test_full_sequence_first_fifteen` is the canonical example from the brief
  encoded as an executable assertion — anyone changing the code will know
  immediately if they break the sequence shown to the customer.

Unlike a comment or a wiki page, this documentation cannot rot silently:
if someone changes the behaviour, the test fails on the next run. That is the
"compileable and executable" property Robert Martin describes — the docs and
the code can never disagree without somebody being told about it.

## 3. Did the green test suite give "the confidence to refactor"? How does this support "Responding to change over following a plan"?

Yes — and the refactor in Phase 4 is the proof. After Phase 3 the logic was a
single `if n % 3 == 0` followed by `return str(n)`. Adding Buzz and FizzBuzz
naively would have produced a nested ladder:

```python
if n % 3 == 0 and n % 5 == 0: return "FizzBuzz"
elif n % 3 == 0:              return "Fizz"
elif n % 5 == 0:              return "Buzz"
else:                          return str(n)
```

Instead, with a green bar in hand, I rewrote the body to build the result by
concatenation:

```python
word = ""
if n % 3 == 0: word += "Fizz"
if n % 5 == 0: word += "Buzz"
return word or str(n)
```

The "FizzBuzz" case now falls out for free from the first two rules — Agile
Principle 10, "maximize the amount of work not done". I was willing to make
that change *only* because the 9 tests would catch any regression in under a
second. Without them I would have left the uglier version in place out of
fear.

This is exactly what "Responding to change over following a plan" means in
practice: the plan said "add Buzz and FizzBuzz", but the design *changed* mid-
phase because the tests gave me a safety net. Plans describe the destination;
tests give you the freedom to choose a better road on the way there.
