message = input("message: ")
pol = input("polynom: ") #порождающий полином
tp = int(input("type: "))

message += '0' * tp
m = int(message, 2)
p = int(pol, 2)
it = 1 << (len(message))

print(bin(m), bin(p))
print(bin(it))

lp = len(pol)

while (it > (1 << (lp - 1))):
    while (it > m):
        it >>= 1
    dp = p * (it >> (lp - 1))
    print(bin(m))
    print(bin(it))
    print(bin(dp))
    m ^= dp

print(bin(m)[2:].lstrip('0'))
