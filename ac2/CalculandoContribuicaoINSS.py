salario = float(input())
des1 = salario - (salario * 8 / 100)
des2 = salario - (salario * 9 / 100)
des3 = salario - (salario * 11 / 100)

if salario <= 1751.81: 
    des1 = salario - des1
    print('Desconto do INSS: R$ {:.2f}'.format(des1))

elif salario >= 1751.81 and salario <= 2919.72:
    des2 = salario - des2
    print('Desconto do INSS: R$ {:.2f}'.format(des2))

elif salario >= 2919.73 and salario <= 5839.45:
    des3 = salario - des3
    print('Desconto do INSS: R$ {:.2f}'.format(des3))

else:
    print('Desconto do INSS: R$ {:.2f}'.format(642.34))