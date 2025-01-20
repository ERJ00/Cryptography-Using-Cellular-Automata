![image](https://github.com/user-attachments/assets/9406aa3d-42e5-4b5f-a8d6-0948cbb0d0ce)


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

---

## How to Use the Program

### Prerequisites
1. **Python**: Ensure you have Python 3.x installed on your system.
2. **Dependencies**: Install required libraries by running:
   ```bash
   pip install PyQt5
   ```
3. **Download the Program**: Place the `cryptography.py` file in a working directory.

### Steps to Use
1. **Run the Program**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `cryptography.py`.
   - Execute the script with:
     ```bash
     python cryptography.py
     ```

2. **Program Interface**:
   - **Data Input**: Enter your text directly into the input box or use the "Browse" button to select a text file.
   - **Initial Key**: Input a binary string (e.g., `10101010`) in the "Key" field. This serves as the starting point for key generation.
   - **Cycle Count**: Specify the number of generations for dynamic key creation in the "Cycle" field.

3. **Process the Input**:
   - Click on **"Start Process"** to encrypt or decrypt the input data.
   - The program will:
     - Generate cryptographic keys using Rule 30.
     - Encrypt or decrypt the input using the generated keys.
     - Display results in the output box and log details in the log section.

4. **Output and Logs**:
   - **Encrypted/Decrypted Text**: View the processed data in the "Output" section.
   - **Logs**: View key generation and encryption steps in the log box.
   - A file named `processed_data.txt` will be saved in the same directory as the script with the processed data.

5. **Reset Inputs**:
   - Use the **"Reset"** button to clear all fields and prepare for new input.

### Notes
- **Binary Key Format**: Ensure the key is a binary string (e.g., `10101010`) of up to 10 characters.
- **Cycle Value**: Must be a positive integer.
- **Error Handling**: The program validates inputs and displays status messages for any issues (e.g., invalid file paths, missing inputs, or incorrect key formats)

---

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
