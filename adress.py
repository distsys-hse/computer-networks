def h(host):
    octet = 255
    return "{}.{}.{}.{}".format((host >> 24) & octet,
                                (host >> 16) & octet, 
                                (host >> 8)  & octet, 
                                 host        & octet)

def r(mask):
    ans = 0
    i = 0
    while (mask > 0):
        ans |= (((mask & 1) ^ 1) << i)
        i += 1
        mask >>= 1
    return ans

def count(adress):
    host, mask = adress.split("/")
    mask = (1 << 32) - (1 << (32 - int(mask)))
    host = list(map(int, host.split('.')))
    host = (host[0] << 24) + (host[1] << 16) + (host[2] << 8) + host[3]
    print("Маска: {}".format(h(mask)))
    print("Адрес сети: {}".format(               h(   host & mask             )))
    print("Широковещательный адрес: {}".format(  h(   host | r(mask)          )))
    print("Наименьший адрес хоста: {}".format(   h(   (host & mask) + 1       )))
    print("Наибольший адрес хоста: {}".format(   h(   (host | (r(mask))) - 1  )))
    print("Число хостов в подсети: {}".format(          r(mask) - 1            ))
    print("Следующая подсеть: {}".format(        h(   (host | r(mask)) + 1    )))



"""
    Хост вводится в формате 192.168.12.13/27, где 27 - это количество единичных бит в маске.
    В конкретном случае маска равна 255.255.255.224 
"""
print("Посмотри формат ввода")
count(input("Введите хост: "))
