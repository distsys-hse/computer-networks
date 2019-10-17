message = input("message: ")
pol = input("polynom: ") #порождающий полином
tp = len(pol) - 1

message += '0' * tp
m = int(message, 2)
p = int(pol, 2)
it = 1 << (len(message))

i = 1

lp = len(pol)

while (it > (1 << (lp - 1))):
    while (it > m):
        it >>= 1

    dp = p * (it >> (lp - 1))
    if (dp == 0):
        break
    print(f"--- Round {i} ---")
    print("M(x):", bin(m)[2:])
    print("G(x):", bin(p)[2:])
    print("X(x):", bin(dp)[2:])
    m ^= dp
    i += 1

print("checksum:", bin(m)[2:].lstrip('0'))
