import time

start = time.gmtime(0)
t = time.time()
print("Seconds since ", end=" ")
print(time.gmtime(0).strftime("%B %d %Y"), end=": ")
print(f"{t:,} or {t:.2e} in scientific notation")
print(time.strftime("%b %d %Y"))
