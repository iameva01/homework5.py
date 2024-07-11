immutable_var = (1, 2, 3.3, 'sheep', True)
print(immutable_var)
print(immutable_var[-1])
print(immutable_var[:2])
print(immutable_var[::-1])

#immutable_var[2] = 7 Кортеж, в отличие от списка, является упорядоченной и неизменяемой коллекцией, поэтому для кортежа возможны такие команды, как сложение и умножение, или если кортеж содержит в себе изменяемую часть(напр. список) - она будет поддаваться изменению
immutable_var_2 = (False, 6, 8.8) * 7
print(immutable_var_2)
immutable_var_3 =(['cow', 'horse'], 'bear')
immutable_var_3 [0][0] = 'duck'
print(immutable_var_3)
#immutable_var_3 [1][0] = 'wolf' Не можем изменять часть кортежа
#print(immutable_var_3)

mutable_list = ['whale', 'dolphin', 'octupus']
print(mutable_list)
mutable_list [1] = 'shrimp'
print(mutable_list)