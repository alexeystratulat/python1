import numpy as np


def t4_1():
    nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
    print(nat.replace("FastEthernet", "GigabitEthernet"))
t4_1()


def t4_2():
    mac = "AAAA:BBBB:CCCC"
    print(mac.replace(":", "."))
t4_2()

def t4_3():
    config = "switchport trunk allowed vlan 1,3,10,20,30,100"
    print(config.split()[-1].split(","))

t4_3()

def t4_4():
    vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
    result = (np.unique(sorted(vlans)))
    print(result)
t4_4()

def t4_5():
    command1 = "switchport trunk allowed vlan 1,2,3,5,8"
    command2 = "switchport trunk allowed vlan 1,3,8,9"
    result = np.intersect1d(command1.split()[-1].split(","), command2.split()[-1].split(","))
    print(result)
t4_5()

def t4_6():
    print("test")


t4_6()

def t4_7():
    print("test")


t4_7()

def t4_8():
    print("test")


t4_8()