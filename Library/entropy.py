import math

def calculate_password_entropy(password):
    charset_size = len(set(password))
    entropy = math.log2(charset_size) * len(password)
    return entropy

password = input("Enter your password: ")
entropy = calculate_password_entropy(password)
print("Entropy: ", entropy)
