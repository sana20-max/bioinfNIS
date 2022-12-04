from random import randint

def dnk(len_mol, time, mass_one):
    total1 = 1
    for i in range(time):
        nukl_num = randint(50, 100)
        total1 = len_mol * nukl_num
        len_mol = total1
    total_mass = len_mol * 2 * mass_one
    return total_mass

print(dnk(121024, 10800, 345))