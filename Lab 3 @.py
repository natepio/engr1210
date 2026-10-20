# ============================================================
# ENGR1210 - Morse Code Translator Project
# Week 3 Lab: Working with Lists (Loops, Tuples, Comprehensions)
# Chapter 4 - Python Crash Course, 3rd Edition
#
# Standalone script. Still no functions and no imports.
# New tools this week: for loops, tuples, range(), list comprehensions.
# (Note: 'if' statements arrive in Week 4 - so this week we encode words
# that contain only known letters and no spaces. Handling spaces and
# unknown characters is exactly what next week's 'if' will add.)
# ============================================================

# ============================================================
# SECTION 1 - ANCHOR
# ============================================================
print("=" * 52)
print("SECTION 1: ANCHOR - Tuples and Looping the Codebook")
print("=" * 52)

# Last week we kept letters and patterns in two separate lists that had to
# stay aligned. This week we pair them up using TUPLES. A tuple is a fixed
# little group of values: ('A', '.-') keeps the letter and its pattern
# locked together so they can never drift apart.
#
# CODEBOOK is now ONE list of (letter, pattern) tuples.

CODEBOOK = [
    ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'),
    ('F', '..-.'), ('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'),
    ('K', '-.-'), ('L', '.-..'), ('M', '--'), ('N', '-.'), ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
    ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'),
]

# A for loop visits every tuple. We "unpack" each tuple into two names at
# once: letter, pattern. No more index bookkeeping.
print("\nThe full codebook (first 8 rows):")
print(f" {'Letter':<8}{'Pattern'}")
print(" " + "-" * 18)
for letter, pattern in CODEBOOK[:8]: # slice: just the first 8
    print(f" {letter:<8}{pattern}")

print(f"\nThe codebook has {len(CODEBOOK)} entries.")

# -- ANCHOR QUESTIONS ------------------------------------------
# Q1. Why is a tuple ('A', '.-') safer here than a list ['A', '.-']?
# Q2. "for letter, pattern in CODEBOOK" unpacks each tuple into two names.
# How is that different from "for entry in CODEBOOK"?
# Q3. CODEBOOK[:8] is a slice. What would CODEBOOK[-3:] give you?

# A1: Tuple is immutable - you can't accidentally change it. A codebook entry should NEVER change.
# A list ['A', '.-'] could be mutated like entry[1] = '...' and corrupt the codebook.
# Tuples lock them together.

# A2: for entry in CODEBOOK -> entry is one tuple ('A','.-'), you'd need entry[0], entry[1]
# for letter, pattern in CODEBOOK -> Python unpacks it for you directly into two variables, cleaner.

# A3: CODEBOOK[-3:] gives the last 3 entries: [('X','-..-'), ('Y','-.--'), ('Z','--..')]

# ============================================================
# SECTION 2 - GUIDED
# ============================================================
print("\n" + "=" * 52)
print("SECTION 2: GUIDED - Encode a Whole Word with a Loop")
print("=" * 52)

# We keep the parallel lists too, because the quickest no-'if' lookup is
# still letters.index(). A LOOP now does for a whole word what you did by
# hand last week.
letters = [pair[0] for pair in CODEBOOK] # comprehension: pull out letters
patterns = [pair[1] for pair in CODEBOOK] # comprehension: pull out patterns

word = "HELLO" # only known letters, no spaces (see header note)

encoded = []
# TODO: loop over each character in 'word'. For each one, find its position
# with letters.index(character), grab patterns[position], and append
# that to 'encoded'.

# Hint:
# for character in word:
# position = letters.index(character)
# encoded.append(patterns[position])

# (write your loop here)
for character in word:
    position = letters.index(character)
    encoded.append(patterns[position])

print(f"\nEncoding '{word}':")
print(f" result -> {encoded}")
# Expected once complete: ['....', '.', '.-..', '.-..', '---']

# ============================================================
# SECTION 3 - EXTENSION
# ============================================================
print("\n" + "=" * 52)
print("SECTION 3: EXTENSION - Comprehensions and Why Lookup Is Slow")
print("=" * 52)

# A list comprehension can filter while it builds. Worked example: collect
# the patterns for all the VOWELS in one line.
vowel_patterns = [pattern for (letter, pattern) in CODEBOOK if letter in 'AEIOU']
print(f"\nVowel patterns (A,E,I,O,U): {vowel_patterns}")

# -- YOUR EXTENSION --------------------------------------------
# Every lookup above scans the lists from the start until it finds a match.
# Show how slow that can get: use a loop to count how many tuples Python
# must check before it reaches 'Z' (the last letter).
# Hint: start a counter at 0; loop over CODEBOOK adding 1 each time; you
# can stop early with 'break' once letter == 'Z'.
# (Week 5: a dictionary finds any letter in ONE step, no scanning.)

# TODO: count and print the number of comparisons needed to reach 'Z'
comparisons = 0
for letter, pattern in CODEBOOK:
    comparisons += 1
    if letter == 'Z':
        break

print(f"\nTo find 'Z', Python had to check {comparisons} tuples")
print(f" That's a linear search - O(n). For 26 letters it's 26 checks.")

# ============================================================
# SECTION 4 - STRETCH
# ============================================================
print("\n" + "=" * 52)
print("SECTION 4: STRETCH - Codebook Statistics")
print("=" * 52)

# Using loops and/or comprehensions only:
# 1. Find the SHORTEST pattern(s) and the LONGEST pattern(s) in the
# codebook, and which letters they belong to. (len() of each pattern.)
# 2. Compute the AVERAGE pattern length across all 26 letters.
# 3. Use range(len(CODEBOOK)) to print the codebook as a numbered list:
# 1. A.-
# 2. B -...
# (This is the index-based loop style from p. 60-62.)

# TODO: implement the stretch challenge here

# 1. Shortest / Longest
all_lengths = [len(pattern) for letter, pattern in CODEBOOK]
min_len = min(all_lengths)
max_len = max(all_lengths)

shortest = [(letter, pattern) for letter, pattern in CODEBOOK if len(pattern) == min_len]
longest = [(letter, pattern) for letter, pattern in CODEBOOK if len(pattern) == max_len]

print(f"\nShortest length is {min_len}: {shortest}")
print(f"Longest length is {max_len}: {longest}")

# 2. Average length
total_len = sum(len(pattern) for letter, pattern in CODEBOOK)
average = total_len / len(CODEBOOK)
print(f"\nAverage pattern length: {average:.2f} symbols")
print(f" total symbols: {total_len} over {len(CODEBOOK)} letters")

# 3. Numbered list using range(len(CODEBOOK))
print(f"\nNumbered codebook:")
for i in range(len(CODEBOOK)):
    letter, pattern = CODEBOOK[i]
    print(f" {i+1:>2}. {letter} {pattern}")

# Bonus explanation for checklist:
# Linear search gets slower as data grows because it scans from start.
# If we had 10,000 symbols, finding 'Z' could take 10,000 checks.
# Dictionaries in Week 5 do it in ~1 check no matter the size.

# ============================================================
# CHECKLIST
# [ ] ANCHOR: ran the codebook table; answered Q1-Q3
# [ ] GUIDED: 'HELLO' encodes to ['....', '.', '.-..', '.-..', '---']
# [ ] EXTENSION: counted the comparisons needed to reach 'Z'
# [ ] STRETCH: (optional) shortest/longest/average + numbered list
# [ ] I can explain why linear search gets slower as data grows
#
# LOOKING AHEAD - Week 4
# Next week you learn IF / ELIF / ELSE. That lets you handle the messy
# cases this week skipped: spaces between words, lowercase input, and
# characters that aren't in the codebook at all.
# ============================================================

