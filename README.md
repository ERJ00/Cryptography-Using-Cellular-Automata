# Cryptography using Cellular Automata

**Authors**: E.P.R. Jr, J.P.H.G., J.P.F., S.M.D.B.

This repository contains an innovative cryptographic approach leveraging **Rule 30 Cellular Automata** for secure encryption and decryption. By generating dynamic keys from an initial configuration, this method ensures enhanced security, simplicity, and computational efficiency.

## Key Features

- **Dynamic Key Generation**: Employs Rule 30 to generate unique, complex keys across multiple generations, ensuring high entropy and unpredictability.
- **Efficient Encryption/Decryption**: Uses bitwise XOR operations on binary-encoded plaintext for secure and reversible data transformation.
- **Scalable and Lightweight**: Optimized for both small and large datasets, with low computational overhead suitable for real-time applications.

## Methodology

1. **Initial Key Setup**: Start with a user-defined binary key (up to 10 digits).
2. **Rule 30-Based Key Evolution**: Generate successive generations of keys using cellular automata rules.
3. **Plaintext Conversion**: Convert plaintext characters into binary representations (8-bit ASCII).
4. **Encryption/Decryption**: Apply the XOR operation with generated keys for secure data transformation.

## Performance Highlights

- **Fast Key Generation**: Capable of generating thousands of keys in milliseconds.
- **Scalable Processing**: Handles text sizes from small to large efficiently.
- **Reversible Encryption**: The XOR-based approach ensures reliable decryption using the same key sequence.

## Applications

Ideal for scenarios requiring:
- Lightweight, secure encryption mechanisms.
- Real-time cryptographic processes.
- Enhanced data security with dynamic key rotation.

## References

This project builds on foundational work in cellular automata and cryptography, including studies on Rule 30's chaotic behavior and its potential in secure key generation.

## Future Work

- Explore resistance to various cryptographic attacks.
- Extend to more complex or hybrid cellular automata systems for added security.
- Optimize implementation for further performance gains.
