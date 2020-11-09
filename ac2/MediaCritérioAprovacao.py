nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
frequencia = float(input())

mediaBruta = (nota1 * 2 + nota2 * 2 + nota3 * 3) / 7
media = round(mediaBruta,1)

freq = frequencia * 100

print('Frequencia: %.f%%' % freq)
print('Media:', media)

if freq < 75:
    print('Aluno reprovado por faltas!')
else:
    if media > 9:
        print('Aluno aprovado com louvor!')
    elif media >= 6 and media <= 9:
        print('Aluno aprovado!')
    elif media >=4 and media < 6:
        print('Aluno de rec!')
    elif media < 4:
        print('Aluno reprovado!')