
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)




operation = input('''Введи дію, використовуючи відповідне число: 1 Додавання, 2 Віднімання, 3 Множення, 4 Ділення: ''')
number_1 = int(input('Введи перше число: '))
number_2 = int(input('Введи друге число: '))

def calculate():
  if operation == '1':
    logger.info(f"Додаю:  {number_1} плюс {number_2} =  ")
    return number_1 + number_2
     
  elif operation == '2':
    logger.info(f"Від {number_1} відімаю {number_2} = ")  
    return number_1 - number_2

  elif operation == '3':
    logger.info(f"Множимо:  {number_1} на {number_2} = ")
    return number_1 * number_2

  elif operation == '4':
    if number_1 == 0:
         return print("На ноль ділити не можна")
    logger.info(f"Ділимо:  {number_1} на {number_2} = ")
    return number_1 / number_2
  
if __name__ == "__main__":

   print (calculate( ))
