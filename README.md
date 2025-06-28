# Password Cracker (Python)

this is a beginner-friendly Python project that cracks MD5 hashes using two common techniques: dictionary attack and bruteforce attack. This tool is useful for learning about password security, hashing algorithms, and basic cyber forensics.

---

## Features

- Cracks MD5 password hashes
- Two attack modes:
  - Dictionary Attack (using a wordlist)
  - Brute-force Attack (generates combinations of characters)
- Simple terminal-based interface
- Beginner-friendly, no external libraries required

---

## Project Structure
```bash
password-hash-cracker/
├── cracker.py # main script
├── wordlist.txt # sample wordlist for dictionary attack
└── README.md # documentation
```

---

## How It Works

### Dictionary Attack
Tries each word from a given wordlist and compares its hash to the target hash.

### Brute-force Attack
Generates all combinations of letters and digits (up to a given length) and hashes them to find a match.

---

## Requirements

- Python 3.x

---

## How to Run

1. **Clone the repository**:
```bash
git clone https://github.com/niklausss2811000/password-hash-cracker.git
cd password-hash-cracker
```

2. **Run the program**:
```bash
python3 cracker.py
```
3. **Follow the prompts**:
```bash
Enter the target MD5 hash

Choose the attack mode: dictionary or brute

Provide the wordlist file path (for dictionary attack), or enter the maximum password length (for brute-force attack)
```







