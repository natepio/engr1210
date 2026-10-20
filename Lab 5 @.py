# ============================================================
# ENGR1210 - Morse Code Translator Project
# Week 5 Lab: Dictionaries
# Chapter 6 - Python Crash Course, 3rd Edition
# ============================================================

# --- Carried forward: the codebook as (letter, pattern) tuples -------------
CODEBOOK = [
    ('A', '.-'),   ('B', '-...'), ('C', '-.-.'), ('D', '-..'),  ('E', '.'),
    ('F', '..-.'), ('G', '--.'),  ('H', '....'), ('I', '..'),   ('J', '.---'),
    ('K', '-.-'),  ('L', '.-..'), ('M', '--'),   ('N', '-.'),   ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),  ('S', '...'),  ('T', '-'),
    ('U', '..-'),  ('V', '...-'), ('W', '.--'),  ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'),
]

# ======================================================================
# SECTION 1 - ANCHOR
# ======================================================================
print("=" * 52)
print("SECTION 1: ANCHOR - The Encode Map")
print("=" * 52)

ENCODE_MAP = {letter: pattern for (letter, pattern) in CODEBOOK}

print(f"\nENCODE_MAP has {len(ENCODE_MAP)} entries.")
print(f"Looking up 'S': {ENCODE_MAP['S']}      (one step - no scanning!)")
print(f"Looking up 'O': {ENCODE_MAP['O']}")
print(f"Looking up '@': {ENCODE_MAP.get('@', '?')}  (.get returns '?' for unknowns)")

# Q1. Last week scanning list for 'Z' checked 26 entries. Dict checks 1 entry only.
#     Dict uses hashing so size doesn't slow it down - O(1) not O(n).
# Q2. ENCODE_MAP['@'] CRASHES with KeyError. .get('@','?') returns '?' safely.
#     Use [] when you expect key to exist, .get() when it might be missing.
# Q3. Dict can NEVER have parallel-list bug because key and value are locked together
#     as one pair. With two lists, if you insert/delete in one, they drift out of alignment.

# ======================================================================
# SECTION 2 - GUIDED
# ======================================================================
print("\n" + "=" * 52)
print("SECTION 2: GUIDED - The Decode Map and a Round Trip")
print("=" * 52)

# TODO Step 1: build DECODE_MAP by flipping ENCODE_MAP.
DECODE_MAP = {pattern: letter for letter, pattern in ENCODE_MAP.items()}

print(f"\nDECODE_MAP has {len(DECODE_MAP)} entries.")

# -- Encode a message using the dictionary ------------
message = "SOS"
encoded = []
for character in message.upper():
    if character == ' ':
        encoded.append(' ')
    else:
        encoded.append(ENCODE_MAP.get(character, '?'))
print(f"\nEncoded '{message}' -> {encoded}")

# -- Decode it back using the mirror dictionary ------------
# TODO Step 2: loop over 'encoded'
decoded_chars = []
for pattern in encoded:
    if pattern == ' ':
        decoded_chars.append(' ')
    else:
        decoded_chars.append(DECODE_MAP.get(pattern, '?'))

decoded = "".join(decoded_chars)
print(f"Decoded back  -> '{decoded}'")
# Expected once complete: 'SOS'

# ======================================================================
# SECTION 3 - EXTENSION
# ======================================================================
print("\n" + "=" * 52)
print("SECTION 3: EXTENSION - Round-Trip Check on a Phrase")
print("=" * 52)

phrase = "HI MOM"

encoded_phrase = []
for character in phrase.upper():
    if character == ' ':
        encoded_phrase.append(' ')
    else:
        encoded_phrase.append(ENCODE_MAP.get(character, '?'))
print(f"\nEncoded '{phrase}' -> {encoded_phrase}")

# -- YOUR EXTENSION - Decode encoded_phrase back --
decoded_phrase_chars = []
for pattern in encoded_phrase:
    if pattern == ' ':
        decoded_phrase_chars.append(' ')
    else:
        decoded_phrase_chars.append(DECODE_MAP.get(pattern, '?'))

decoded_phrase = "".join(decoded_phrase_chars)
print(f"Decoded back -> '{decoded_phrase}'")
print(f"Round trip matched? {decoded_phrase == phrase.upper()}")

# ======================================================================
# SECTION 4 - STRETCH
# ======================================================================
print("\n" + "=" * 52)
print("SECTION 4: STRETCH - Add the Digits, and Audit the Maps")
print("=" * 52)

# 1. Add digits 0-9
DIGITS = [
    ('0', '-----'), ('1', '.----'), ('2', '..---'), ('3', '...--'), ('4', '....-'),
    ('5', '.....'), ('6', '-....'), ('7', '--...'), ('8', '---..'), ('9', '----.'),
]
# Extend codebook and rebuild maps
EXTENDED_CODEBOOK = CODEBOOK + DIGITS
ENCODE_MAP = {letter: pattern for (letter, pattern) in EXTENDED_CODEBOOK}
DECODE_MAP = {pattern: letter for letter, pattern in ENCODE_MAP.items()}

print(f"\nAfter adding digits, ENCODE_MAP has {len(ENCODE_MAP)} entries")
print(f"DECODE_MAP has {len(DECODE_MAP)} entries")

# Test with "SOS 911"
test = "SOS 911"
enc_test = []
for c in test.upper():
    if c == ' ':
        enc_test.append(' ')
    else:
        enc_test.append(ENCODE_MAP.get(c, '?'))

dec_test_chars = []
for p in enc_test:
    if p == ' ':
        dec_test_chars.append(' ')
    else:
        dec_test_chars.append(DECODE_MAP.get(p, '?'))
dec_test = "".join(dec_test_chars)

print(f"Encoded '{test}' -> {enc_test}")
print(f"Decoded back -> '{dec_test}'")

# 2. Audit
print(f"\nAudit: len(ENCODE_MAP) == len(DECODE_MAP)? {len(ENCODE_MAP) == len(DECODE_MAP)}")
# If two different letters share same pattern, flipping dict will lose one entry
# because dict keys must be unique - last one wins, silently dropping earlier.
# That is why audit matters.

