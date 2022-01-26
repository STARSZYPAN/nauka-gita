lista={
    'piekarnia': ['bulki','chleb','paczek'],
    'warzywniak': ['buraki','facola','ziemniaki']

}
lista_dict=dict(lista)
print('Lista zakupow')
for sklep,rzeczy in lista_dict.items():
    print('ide do',(sklep.upper()),'kupuje',(rzeczy))
print('razem kupilem',len(rzeczy)*2,'rzeczy')

print("pozdrowienia dla mentora,dzięki za wsprcie")

