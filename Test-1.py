import random
import time

def generate_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

while True:
    print(generate_ip())
    time.sleep(2)
    
