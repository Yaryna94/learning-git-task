diapazon_list  = [number for number in range(1,101) if not number % 5]
print(f" Всі числа від 0 до 100 які діляться на 5 {diapazon_list} ")

squares = [number **3 for number in diapazon_list]
print(f"А це ті числа піднесені до 3 степеня {squares}")
