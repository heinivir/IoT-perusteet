import time
time.sleep(0.1) # Wait for USB to become ready

print("Ready to go!")
print("Loop starting")

for i in range(10):
    print(f"Loop number: {i}")
    time.sleep(0.5)

print("Loop finished")