# ============================================================
# ENGR1210 - Morse Code Translator Project
# Week 6 Lab: User Input and while Loops
# Chapter 7 - Python Crash Course, 3rd Edition
# ============================================================

# --- Carried forward: build both lookup dictionaries from the codebook -------
CODEBOOK = [
    ('A', '.-'),   ('B', '-...'), ('C', '-.-.'), ('D', '-..'),  ('E', '.'),
    ('F', '..-.'), ('G', '--.'),  ('H', '....'), ('I', '..'),   ('J', '.---'),
    ('K', '-.-'),  ('L', '.-..'), ('M', '--'),   ('N', '-.'),   ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),  ('S', '...'),  ('T', '-'),
    ('U', '..-'),  ('V', '...-'), ('W', '.--'),  ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'),
]
ENCODE_MAP = {letter: pattern for (letter, pattern) in CODEBOOK}
# Reverse map for decoding: pattern -> letter (both maps are given to you).
DECODE_MAP = {pattern: letter for (letter, pattern) in CODEBOOK}

DOT_MS = 100  # base unit, carried forward (boundaries are multiples of it)

# ======================================================================
# SECTION 1 - ANCHOR
# ======================================================================
print("=" * 52)
print("SECTION 1: ANCHOR - An Interactive Encoder")
print("=" * 52)
print("Type a message to encode. Type 'quit' to stop.\n")

# Q1. Sentinel value is 'quit'. If we forgot break, it would be an infinite loop asking forever.
# Q2. We use text.lower() == 'quit' so QUIT, Quit, qUiT all work - case-insensitive.
# Q3. input() always returns a string, so "5" is not 5. For numbers we must do int() and handle ValueError.

while True:
    text = input("Message> ")
    if text.lower() == 'quit':
        print("Goodbye!")
        break  # leave the while loop

    encoded = []
    for character in text.upper():
        if character == ' ':
            encoded.append('/')
        else:
            encoded.append(ENCODE_MAP.get(character, '?'))
    print(f"  Morse: {' '.join(encoded)}\n")

# ======================================================================
# SECTION 2 - GUIDED
# ======================================================================
print("\n" + "=" * 52)
print("SECTION 2: GUIDED - Classify Received Signal Durations")
print("=" * 52)

pulse_durations = [55, 105, 180, 240, 300]  # measured ON times (ms)
gap_durations   = [90, 150, 320, 480, 700]  # measured OFF times (ms)

print("\nPulse (LED ON) classification:")
for duration in pulse_durations:
    # TODO: if duration < DOT_MS * 2 -> 'dot', else -> 'dash'. Print it.
    if duration < DOT_MS * 2:
        kind = "dot"
    else:
        kind = "dash"
    print(f"  {duration:4}ms -> {kind}")

print("\nGap (LED OFF) classification:")
for duration in gap_durations:
    # TODO: use if / elif / else with the two boundaries above to set 'kind'
    if duration < DOT_MS * 2:
        kind = "symbol_gap"
    elif duration < DOT_MS * 5:
        kind = "letter_gap"
    else:
        kind = "word_gap"
    print(f"  {duration:4}ms -> {kind}")

# ======================================================================
# SECTION 3 - EXTENSION
# ======================================================================
print("\n" + "=" * 52)
print("SECTION 3: EXTENSION - An Encode / Decode Menu")
print("=" * 52)

while True:
    print("\n1) Encode text -> Morse")
    print("2) Decode Morse -> text")
    print("3) Quit")
    choice = input("Choose 1-3> ")

    if choice == '1':  # encode text -> Morse
        text = input("Text to encode> ")
        encoded = []
        for character in text.upper():
            if character == ' ':
                encoded.append('/')
            else:
                encoded.append(ENCODE_MAP.get(character, '?'))
        print(f"  Morse: {' '.join(encoded)}")

    elif choice == '2':  # decode Morse -> text
        morse = input("Morse to decode (space-separated, / for space)> ")
        tokens = morse.split(' ')
        decoded_chars = []
        for token in tokens:
            if token == '/':
                decoded_chars.append(' ')
            else:
                decoded_chars.append(DECODE_MAP.get(token, '?'))
        print(f"  Text: {''.join(decoded_chars)}")

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please choose 1, 2, or 3.")

# ======================================================================
# SECTION 4 - STRETCH
# ======================================================================
print("\n" + "=" * 52)
print("SECTION 4: STRETCH - Robust Numeric Input")
print("=" * 52)

# Validation loop - catching error with try/except is safer because user can type anything.
# If we trusted first input, program would crash on "five". With try/except we stay in loop until valid.

count = 0
while True:
    user_input = input("How many times should I repeat the message?> ")
    try:
        count = int(user_input)
        if count > 0:
            break
        else:
            print("Please enter a whole number greater than 0.")
    except ValueError:
        print(f"'{user_input}' is not a valid number. Try again.")

# Once we have valid count, encode a fixed message and print that many times
fixed_message = "HELLO WORLD"
encoded = []
for character in fixed_message:
    if character == ' ':
        encoded.append('/')
    else:
        encoded.append(ENCODE_MAP.get(character, '?'))
morse_message = ' '.join(encoded)

print(f"\nRepeating '{fixed_message}' ({morse_message}) {count} times:")
for i in range(count):
    print(f"{i+1}: {morse_message}")

