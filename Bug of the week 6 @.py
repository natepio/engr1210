# bug_week6.py
# BUG OF THE WEEK - Week 6: User Input and while Loops
#
# INSTRUCTIONS: This file has 4 bugs in it.
# Bug 1: Find with the console error message.
# Bug 2: Find with the VS Code Debugger.
# Bug 3: Find with the VS Code Debugger - WARNING: infinite loop risk.
# Bug 4: Can ONLY be found by running a complete set of TEST CASES.

# ============================================================
# THE PROGRAM: a simple sandwich order system
# Customers enter sandwich orders one at a time.
# The system processes orders, tracks what's been made,
# and applies a discount for large orders (5 or more).
# ============================================================

# ============================================================
# BUG 1 - Find with: console error message
# ============================================================
print("--- Sandwich Order System ---")
num_orders = int(input("How many sandwiches would you like to order? ")) # FIXED: added int() - input() is always a string

if num_orders > 0: # FIXED: now int > int works
    print(f"Great! Let's get started on {num_orders} sandwiches.")
else:
    print("No sandwiches ordered.")

# ============================================================
# BUG 2 - Find with: VS Code Debugger
# ============================================================
print("\n--- Processing Orders ---")
sandwich_queue = ["turkey", "veggie", "roast beef", "grilled cheese"] # FIXED: was "grilled chese"
finished = []

while sandwich_queue:
    current = sandwich_queue.pop(0)
    finished.append(current)
    print(f" Made: {current}")

print("\n--- Completed Orders ---")
for sandwich in finished:
    print(f" {sandwich.title()}")

# ============================================================
# BUG 3 - Find with: VS Code Debugger (INFINITE LOOP RISK)
# ============================================================
print("\n--- Order Counter (max 3) ---")
max_orders  = 3
order_count = 0
active      = True

while active:
    print(f" Order #{order_count + 1} received.")
    order_count += 1 # FIXED: this line was missing - order_count stayed 0 forever
    if order_count == max_orders:
        active = False

# ============================================================
# BUG 4 - Find with: TEST CASES (boundary + empty categories)
# ============================================================
# This section applies a bulk discount: orders of 5 or more
# sandwiches get 20% off.

# STEP 2: Design and run these test cases
# | Test Case          | qty | order_total | Expected           |
# | A: Clearly above   | 8   | 40.00       | 20% off -> $32.00  |
# | B: Clearly below   | 3   | 15.00       | No discount        |
# | C: BOUNDARY (exact)| 5   | 25.00       | 20% off -> $20.00  | <- THIS ONE FAILS WITH > 5
# | D: One below bdry  | 4   | 20.00       | No discount        |
# | E: EMPTY (zero qty)| 0   | 0.00        | No discount        |

print("\n--- Discount Calculator ---")
order_total = 25.00
qty         = 5  # change this when running test cases

if qty >= 5:  # FIXED: was qty > 5 - should be >= 5 for "5 or more"
    discount     = order_total * 0.20
    final_total  = order_total - discount
    print(f" Qty: {qty} | Bulk discount applied!")
    print(f" Original: ${order_total:.2f} -> Final: ${final_total:.2f}")
else:
    print(f" Qty: {qty} | No discount. Total: ${order_total:.2f}")