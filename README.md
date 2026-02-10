# 🔐 RSA Algorithm Implementation (Python)

A simple and educational **Python implementation of the RSA public-key cryptography algorithm**.  
This project demonstrates **RSA key generation, encryption, and decryption** using **basic number theory concepts**.

It is created as a **learning and academic project** to understand how **public-key cryptography** works internally, not as a production-ready security system.

---

## 🧱 Project Structure

```bash
rsa-algorithm-python/
│
├── app.py            # RSA algorithm implementation (CLI based)
├── LICENSE           # Project license
└── README.md         # Project documentation
```

---

## ✨ Features

### 🔑 RSA Key Generation
- Accepts two prime numbers as input
- Computes modulus (n) and Euler’s Totient (φ)
- Automatically selects a valid public exponent (e)
- Computes private exponent (d) using modular inverse

### 🔒 Encryption
- Encrypts a numeric message using the public key
- Uses efficient modular exponentiation

### 🔓 Decryption
- Decrypts the encrypted message using the private key
- Verifies correctness of the RSA algorithm flow

### 🧮 Educational Focus
- Clear, readable logic
- Minimal dependencies
- Ideal for students and beginners in cryptography

---

## 🛠 Technologies Used

| Technology             | Role                        |
| ---------------------- | --------------------------- |
| **Python 3**           | Core programming language   |
| **math.gcd**           | Valid public key selection  |
| **Modular Arithmetic** | RSA encryption & decryption |

---

## 📌 Purpose of This Project

This project is built to:
  - Understand RSA public-key cryptography
  - Learn Euler’s Totient function
  - Practice modular arithmetic
  - Demonstrate encryption and decryption flow
  - Strengthen fundamentals of computer security

> ⚠️ This project is intended strictly for learning and demonstration purposes.

---

## ▶️ How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ShakalBhau0001/rsa-algorithm-python.git
```

### 2️⃣ Navigate to the project folder
```bash
cd rsa-algorithm-python
```

### 3️⃣ Run the program
```bash
python app.py
```

### 4️⃣ Follow the prompts
- Enter two prime numbers
- Enter a numeric message smaller than `n`
- View generated keys, encrypted message, and decrypted output

---

## ⚠️ Limitations

- Uses small prime numbers (not secure)
- No prime number validation
- No padding schemes (e.g., OAEP)
- CLI-based interaction only
- Not suitable for real-world cryptographic use

---

## 🌟 Future Improvements

- Add prime number validation
- Support larger primes
- Implement padding schemes
- Add file encryption support
- Create GUI version
- Improve error handling

---

## ⚠️ Disclaimer

This implementation is created **for educational and learning purposes only.**
It does **not provide real-world cryptographic security** and must not be used in production systems or for protecting sensitive data.

---

## 🪪 Author

> **Shakal Bhau**

> GitHub: [ShakalBhau0001](https://github.com/ShakalBhau0001)

---
