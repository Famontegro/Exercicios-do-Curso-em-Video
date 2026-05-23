print('Irei te dizer a área de uma parede e quantos litros de tinta você precisa para pinta-la')
n1 = float(input('Qual é a altura da parede em metros? '))
n2 = float(input('Qual é a largura da parede em metros? '))
a = n1 * n2
l = a / 2
print('A área de sua parede é de {:.1f} metros quadrados e você vai precisar de {:.1f} litros de tinta para pinta-la'.format(a, l))
