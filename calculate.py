def calculate():

  operation = input('''Введи дію, використовуючи відповідне число: 1 Додавання, 2 Віднімання, 3 Множення, 4 Ділення: ''')
  number_1 = int(input('Введи компонент 1: '))
  number_2 = int(input('Введи компонент 2: '))
  if operation == '1':
     print('{} + {} ='.format(number_1, number_2))
     print(number_1 + number_2)
  elif operation == '2':
     print('{} - {} = '.format(number_1, number_2))
     print(number_1 - number_2)
  elif operation == '3':
     print('{} * {} = '.format(number_1, number_2))
     print(number_1 * number_2)
  elif operation == '4':
      print('{} / {} = '.format(number_1, number_2))
      print(number_1 / number_2)
  
# Вызов функции calculate() вне функции
calculate( )