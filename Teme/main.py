import math
#TEMA 2
lista=[7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
lista.sort()
print('lista ordonata: ',lista)
lista.sort(reverse=True)
print('lista ordonata descendent: ',lista)
lista_pare=lista[0::2]
lista_impare=lista[1::2]
print('nr pare: ',lista_pare)
print('nr impare: ',lista_impare)
lista_multiplu3=lista[1::3]
print('nr multiplu 3: ',lista_multiplu3)


#TEMA 3
def suma(*args, **kwargs):
    s=0
    for i in args:
        if type(i) is int or type(i) is float:
            s=s+i
    return s

print(f"Sum = {suma(1, 5, -3, 'abc', [12, 56, 'cad'])}")
print(f"Sum = {suma()}")
print(f"Sum = {suma(2, 4, 'abc', param_1=2)}")


def recursiva(nr):
    if nr==0:
        return 0
    return nr+recursiva(nr-1)
print("recursiva:",recursiva(6))

def recursiva_para(nr):
    if nr==0:
        return 0
    if nr%2==0:
        return nr+recursiva_para(nr-1)
    return recursiva_para(nr-1)
print("recursiva para :",recursiva_para(6))


def recursiva_impara(nr):
    if nr==0:
        return 0
    if nr%2!=0:
        return nr+recursiva_impara(nr-1)
    return recursiva_impara(nr-1)
print("recursiva impara :",recursiva_impara(6))

def read_from_keyboard():
    element=input()
    if element.isnumeric():
        val=float(element)
        if val - math.floor(val) == 0:
            return math.floor(val)
    return 0
i=0
while i<5:
    print(read_from_keyboard())
    i+=1