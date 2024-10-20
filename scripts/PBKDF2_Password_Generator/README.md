
# PBKDF2 Password Generator

This project contains a simple implementation of password generation using the PBKDF2 (Password-Based Key Derivation Function 2) algorithm with HMAC-SHA256. PBKDF2 is widely used to hash passwords securely by combining the password with a cryptographic salt and performing multiple iterations of a hash function. This process makes brute-force and dictionary attacks computationally expensive.

## Features

- **Cryptographically secure**: Utilizes `PBKDF2-HMAC-SHA256`, a highly secure key derivation algorithm.
- **Salting**: Adds a unique, random salt to each password, preventing attacks against reused passwords.
- **Multiple iterations**: The use of 100,000 iterations makes password hashing computationally expensive for attackers.
- **Customizable**: The number of iterations, salt, and derived key length (dklen) can be adjusted as needed.

## Requirements

This implementation uses Python's built-in libraries, so no external dependencies are required.

## Usage

### Function: `generate_pbkdf2_password`

```python
def generate_pbkdf2_password(secret, salt=None, iterations=100000, dklen=16):
    if salt is None:
        salt = os.urandom(16)
    return hashlib.pbkdf2_hmac('sha256', secret.encode(), salt, iterations, dklen).hex()
```

### Parameters:
- **`secret`** (str): The input password or secret to be hashed.
- **`salt`** (bytes, optional): A cryptographic salt. If no salt is provided, a 16-byte random salt is generated.
- **`iterations`** (int, optional): The number of hashing iterations to perform. The default is 100,000, which is a reasonable balance between security and performance.
- **`dklen`** (int, optional): The desired length (in bytes) of the derived key. The default is 16 bytes.

### Return:
- **`hex`**: A hexadecimal string representing the derived password hash.

### Example Usage:

```python
print(generate_pbkdf2_password("user-secret"))
```

The function will print a derived password hash, for example:

```
4f9c2b5d9ab47a3f776e5d1b2a47a3bc
```

### Explanation:

- **PBKDF2-HMAC-SHA256**: This is a key derivation function that applies HMAC (Hash-based Message Authentication Code) using SHA256 as the underlying hash function. It is designed to be computationally expensive to slow down brute-force attacks.
- **Salt**: A random 16-byte value (generated using `os.urandom(16)`) that is mixed with the secret to ensure that identical passwords hash to different values. This prevents attackers from precomputing hash values for common passwords (rainbow table attacks).
- **Iterations**: The secret and salt are hashed repeatedly (100,000 times by default) to further increase the computation time required for each password, making brute-force attacks significantly harder.
- **Key length**: The final output is a 16-byte string, which is then converted to hexadecimal for readability.

## Customization

- **Salt length**: You can customize the length of the salt by modifying the `os.urandom(16)` part of the code, where `16` represents the salt size in bytes.
- **Number of iterations**: Adjust the number of iterations to increase security, but be mindful that higher iteration counts also increase the computation time.
- **Derived key length (dklen)**: The length of the output hash can be adjusted by modifying the `dklen` argument.

### Security Considerations

- **High iteration count**: The default of 100,000 iterations provides a good level of security for most use cases. For applications requiring higher security, you can increase this value, though at the cost of performance.
- **Salt**: Always use a unique salt for each password to ensure security, especially when storing multiple password hashes.

## License

This code is free to use and distribute under the MIT License.
