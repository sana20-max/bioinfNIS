from random import randint

def dnk(len_mol, time, mass_one):
    count = 0
    nukl_num = 0
    while count<=time:
        nukl_num += randint(50, 100)
        count += 1
    total_mass = (len_mol*2+nukl_num)*mass_one
    return total_mass

print(dnk(121024, 10800, 345))
