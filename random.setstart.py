import random
s = random.getstate()
print(random.randint(1,10))
print(random.random())
print(random.random())

random.setstate(s)
print(random.randint(1,10))
print(random.random())
print(random.random())
#Метод setstate() модуля random используется в сочетании с 
# методом getstate(). После использования
# метода getstate() для захвата состояния генератора случайных
# чисел метод setstate() используется для восстановления 
# состояния генератора случайных чисел до указанного состояния.