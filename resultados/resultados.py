from random import randint

print('Digite o seu nome: ')
nome = input()

print('Informe sua idade: ')
idade = int(input())

print('Seleciona o time 1: ')
print('1.  São Paulo')
print('2.  Santos')
print('3.  Flamengo')
print('4.  Corinthians')
print('5.  Palmeiras')
print('6.  Confiança')
print('7.  Atlético MG')
print('8.  Internacional')
print('9.  Cruzeiro')
print('10. Vasco')
time1 = int(input())

print('Seleciona o time 2: ')
print('1.  São Paulo')
print('2.  Santos')
print('3.  Flamengo')
print('4.  Corinthians')
print('5.  Palmeiras')
print('6.  Confiança')
print('7.  Atlético MG')
print('8.  Internacional')
print('9.  Cruzeiro')
print('10. Vasco')
time2 = int(input())


# Area do time 1 São Paulo
if (time1==time2):
  print('Não é possivel o confronto entre o mesmo time O.o')
elif (time1==1) and (time2==2):
  print('Confronto: São Paulo x Santos')
  print(f'São Paulo {randint(0,5)} x {randint(0,5)} Santos ')
elif (time1 == 1) & (time2 == 3):
  print('Confronto: São Paulo x Flamengo')
  print(f'São Paulo {randint(0,5)} x {randint(0,5)} Flamengo')
elif (time1==1) & (time2==4):
    print('Confronto: São Paulo x Corinthians')
    print(f'São paulo {randint(0,5)} x {randint(0,5)} Corinthians')
elif (time1==1) & (time2==5):
    print('Confronto: São Paulo x Palmeiras')
    print(f'São Paulo {randint(0,5)} x {randint(0,5)} Palmeiras')
elif (time1==1) & (time2==6):
    print('Confronto: São Paulo x Confiança')
    print(f'São Paulo {randint(0,5)} x {randint(0,5)} Confiança')
elif (time1==1) & (time2==7):
    print('Confronto: São Paulo x Atlético MG')
    print(f'São Paulo {randint(0,5)} x {randint(0,5)} Atlético MG')
elif (time1==1) & (time2==8):
    print('Confronto: São Paulo x Internacional')
    print(f'São Paulo {randint(0,5)} x {randint(0,5)} Internacional')
elif (time1==1) & (time2==9):
    print('Confronto: São Paulo x Cruzeiro')
    print(f'São Paulo {randint(0,5)} x {randint(0,5)} Cruzeiro')
elif (time1==1) & (time2==10):
    print('Confronto: São Paulo x Vasco')
    print(f'São Paulo {randint(0,5)} x {randint(0,5)} Vasco')

# Area do time 1 Santos

elif (time1==2) and (time2==1):
    print('Confronto: Santos x São Paulo')
    print(f'Santos {randint(0,5)} x {randint(0,5)} São Paulo')
elif (time1==2) & (time2==3):
    print('Confronto: Santos x Flamengo')
    print(f'Santos {randint(0,5)} x {randint(0,5)} Flamengo')
elif (time1==2) & (time2==4):
    print('Confronto: Santos x Corinthians')
    print(f'Santos {randint(0,5)} x {randint(0,5)} Corinthians')
elif (time1==2) & (time2==5):
    print('Confronto: Santos x Palmeiras')
    print(f'Santos {randint(0,5)} x {randint(0,5)} Palmeiras')
elif (time1==2) & (time2==6):
    print('Confronto: Santos x Confiança')
    print(f'Santos {randint(0,5)} x {randint(0,5)} Confiança')
elif (time1==2) & (time2==7):
    print('Confronto: Santos x Atlético MG')
    print(f'Santos {randint(0,5)} x {randint(0,5)} Atlético MG')
elif (time1==2) & (time2==8):
    print('Confronto: Santos x Internacional')
    print(f'Santos {randint(0,5)} x {randint(0,5)} Internacional')
elif (time1==2) & (time2==9):
    print('Confronto: Santos x Cruzeiro')
    print(f'Santos {randint(0,5)} x {randint(0,5)} Cruzeiro')
elif (time1==2) & (time2==10):
    print('Confronto: Santos x Vasco')
    print(f'Santos {randint(0,5)} x {randint(0,5)} Vasco')

# Area do time 1 Flamengo

elif (time1==3) & (time2==4):
    print('Confronto: Flamengo x Corinthians')
    print(f'Flamengo {randint(0,5)} x {randint(0,5)} Flamengo')
elif (time1==3) & (time2==5):
    print('Confronto: Flamengo x Palmeiras')
    print(f'Flamengo {randint(0,5)} x {randint(0,5)} Corinthians')
elif (time1==3) & (time2==6):
    print('Confronto: Flamengo x Confiança')
    print(f'Flamengo {randint(0,5)} x {randint(0,5)} Palmeiras')
elif (time1==3) & (time2==7):
    print('Confronto: Flamengo x Atlético MG')
    print(f'Flamengo {randint(0,5)} x {randint(0,5)} Confiança')
elif (time1==3) & (time2==8):
    print('Confronto: Flamengo x Internacional')
    print(f'Flamengo {randint(0,5)} x {randint(0,5)} Atlético MG')
elif (time1==3) & (time2==9):
    print('Confronto: Flamengo x Cruzeiro')
    print(f'Flamengo {randint(0,5)} x {randint(0,5)} Internacional')
elif (time1==3) & (time2==10):
    print('Confronto: Flamengo x Vasco')
    print(f'Flamengo {randint(0,5)} x {randint(0,5)} Cruzeiro')

# Area do time 1 Corinthians

elif (time1==4) & (time2==5):
    print('Confronto: Corinthians x Palmeiras')
    print(f'Flamengo {randint(0,5)} x {randint(0,5)} Palmeiras')
elif (time1==4) & (time2==6):
    print('Confronto: Corinthians x Confiança')
    print(f'Flamengo {randint(0,5)} x {randint(0,5)} Confiança')
elif (time1==4) & (time2==7):
    print('Confronto: Corinthians x Atlético MG')
    print(f'Flamengo {randint(0,5)} x {randint(0,5)} Atlético MG')
elif (time1==4) & (time2==8):
    print('Confronto: Corinthians x Internacional')
    print(f'Flamengo {randint(0,5)} x {randint(0,5)} Internacional')
elif (time1==4) & (time2==9):
    print('Confronto: Corinthians x Cruzeiro')
    print(f'Flamengo {randint(0,5)} x {randint(0,5)} Cruzeiro')
elif (time1==4) & (time2==10):
    print('Confronto: Corinthians x Vasco')
    print(f'Flamengo {randint(0,5)} x {randint(0,5)} Vasco')







