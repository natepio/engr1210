# bug_week4 (1).py
# BUG OF THE WEEK - Week 4: if Statements   (Test-Case Edition)
# =========================================================================
# This file has FOUR bugs. Every one of them RUNS without crashing and prints
# something -- which is exactly the trap. "It ran" does not mean "it works."
# You find these bugs the way engineers really do: with TEST CASES.
# A test case is just a known INPUT plus the OUTPUT you EXPECT for it.
# Run the code, compare the ACTUAL output to what you expected, and every
# mismatch is a bug.
# The sneaky part: some bugs are only wrong for CERTAIN inputs.
# HOW TO WORK THROUGH IT
#  1. Run the file. Each section prints its result for every test input.
#  2. Go to that section's TEST CASE TABLE and fill in ACTUAL, then PASS/FAIL.
#  3. Each FAIL points at the bug. Fix the code, re-run, and confirm every
#     row now PASSES.
#  4. Add at least TWO of your own test cases to each list
#  5. For Bug 3, practice the VS Code debugger
# =========================================================================

# =========================================================================
# BUG 1 - Grade Checker
# Category: test-case-triggered. Hint: test grades right ON the cutoffs.
# =========================================================================
print("--- Grade Checker ---")

grades_to_test = [95, 90, 85, 80, 72, 100, 79]  # <- added 2 own: 100 and 79

for grade in grades_to_test:
    if grade >= 90:
        result = "You got an A!"
    elif grade >= 80:  # FIXED BUG 1: was "grade > 80" - should be >= 80
        result = "You got a B!"
    else:
        result = "Keep working at it."
    print(f"  grade {grade} -> {result}")

# TEST CASE TABLE  (fill in ACTUAL, then mark PASS or FAIL)
#  INPUT | EXPECTED             | ACTUAL               | PASS?
#  95    | You got an A!        | You got an A!        | PASS
#  90    | You got an A!        | You got an A!        | PASS
#  85    | You got a B!         | You got a B!         | PASS
#  80    | You got a B!         | You got a B!         | PASS - BUG WAS HERE, was FAIL
#  72    | Keep working at it.  | Keep working at it.  | PASS
#  100   | You got an A!        | You got an A!        | PASS <- add your own
#  79    | Keep working at it.  | Keep working at it.  | PASS <- add your own

# =========================================================================
# BUG 2 - User Check
# Category: test-case-triggered. A warning should appear ONLY for users who
# are NOT on the list. Hint: test a user who SHOULD be allowed AND one who
# should NOT -- one test case alone won't reveal this one.
# =========================================================================
print("\n--- User Check ---")
approved_users = ["admin", "natalie", "carlos", "priya"]

users_to_test = ["admin", "guest", "natalie", "hacker", "carlos", "bob"]  # <- added 2 own

for current_user in users_to_test:
    if current_user in approved_users:
        print(f"  Welcome, {current_user}!")  # FIXED BUG 2: was WARNING, swapped
    else:
        print(f"  WARNING: '{current_user}' is not an approved user!")  # FIXED: was Welcome

# TEST CASE TABLE  (fill in ACTUAL, then mark PASS or FAIL)
#  INPUT   | EXPECTED                                  | ACTUAL                                  | PASS?
#  admin   | Welcome, admin!                           | Welcome, admin!                           | PASS - BUG WAS HERE
#  guest   | WARNING: 'guest' is not an approved user! | WARNING: 'guest' is not an approved user! | PASS
#  natalie | Welcome, natalie!                         | Welcome, natalie!                         | PASS - BUG WAS HERE
#  hacker  | WARNING: 'hacker' is not an approved user!| WARNING: 'hacker' is not an approved user!| PASS
#  carlos  | Welcome, carlos!                          | Welcome, carlos!                          | PASS <- add your own
#  bob     | WARNING: 'bob' is not an approved user!   | WARNING: 'bob' is not an approved user!   | PASS <- add your own

# =========================================================================
# BUG 3 - Stage of Life
# Category: logic error -- easiest to SEE in the debugger.
# Put a breakpoint on the first 'if', Step Over (F10), and watch which branch
# runs for a teenager. Also test one age from EVERY stage.
# =========================================================================
print("\n--- Stage of Life ---")

ages_to_test = [1, 5, 12, 13, 15, 19, 20, 45, 2, 65]  # <- added 2 own: 2 and 65

for age in ages_to_test:
    if age < 2:
        stage = "infant"
    elif age < 13:
        stage = "child"
    elif age < 20:  # FIXED BUG 3: was "age < 13" duplicate, should be < 20
        stage = "teenager"
    else:
        stage = "adult"
    print(f"  age {age} -> {stage}")

# TEST CASE TABLE  (fill in ACTUAL, then mark PASS or FAIL)
#  INPUT | EXPECTED | ACTUAL   | PASS?
#  1     | infant   | infant   | PASS
#  5     | child    | child    | PASS
#  12    | child    | child    | PASS
#  13    | teenager | teenager | PASS - BUG WAS HERE, was child
#  15    | teenager | teenager | PASS - BUG WAS HERE
#  19    | teenager | teenager | PASS - BUG WAS HERE
#  20    | adult    | adult    | PASS
#  45    | adult    | adult    | PASS
#  2     | child    | child    | PASS <- add your own - boundary infant/child
#  65    | adult    | adult    | PASS <- add your own

# =========================================================================
# BUG 4 - Pizza Topping Checker
# Category: test-case-triggered. Hint: test the SAME real topping typed with
# different capitalization, plus a topping that is not on the menu.
# =========================================================================
print("\n--- Pizza Topping Checker ---")
available_toppings = ["Pepperoni", "Mushrooms", "Green Peppers", "Olives"]

requests_to_test = ["Pepperoni", "Mushrooms", "mushrooms", "Pineapple", "PEPPERONI", "green peppers"]  # <- added 2 own

for requested_topping in requests_to_test:
    if requested_topping.lower() == available_toppings[0].lower():  # FIXED BUG 4: added .lower() for case-insensitive
        print("  Adding pepperoni.")
    elif requested_topping.lower() == available_toppings[1].lower():
        print("  Adding mushrooms.")
    elif requested_topping.lower() == available_toppings[2].lower():
        print("  Adding green peppers.")
    elif requested_topping.lower() == available_toppings[3].lower():
        print("  Adding olives.")
    else:
        print(f"  Sorry, we don't have {requested_topping}.")

# TEST CASE TABLE  (fill in ACTUAL, then mark PASS or FAIL)
#  INPUT         | EXPECTED                        | ACTUAL                        | PASS?
#  Pepperoni     | Adding pepperoni.               | Adding pepperoni.               | PASS
#  Mushrooms     | Adding mushrooms.               | Adding mushrooms.               | PASS
#  mushrooms     | Adding mushrooms.               | Adding mushrooms.               | PASS - BUG WAS HERE, was Sorry
#  Pineapple     | Sorry, we don't have Pineapple. | Sorry, we don't have Pineapple. | PASS
#  PEPPERONI     | Adding pepperoni.               | Adding pepperoni.               | PASS <- add your own - uppercase test
#  green peppers | Adding green peppers.           | Adding green peppers.           | PASS <- add your own - lowercase test

# =========================================================================
# WHEN YOU ARE DONE
#  [x] Every table has ACTUAL filled in and PASS/FAIL marked
#  [x] You added at least two of your own test cases to each section
#  [x] You fixed each bug and re-ran until every row PASSES
#  [x] For each bug you can say (a) which test case exposed it and
#      (b) why the original code was wrong
#
# Bug 1: test case 80 exposed it. > 80 vs >= 80 - off-by-one/boundary error
# Bug 2: test cases admin/natalie exposed it. Messages were inverted - logic error
# Bug 3: test cases 13/15/19 exposed it. elif age < 13 duplicated - teenager never reachable
# Bug 4: test case mushrooms (lowercase) exposed it. == is case-sensitive - needs .lower()
# =========================================================================