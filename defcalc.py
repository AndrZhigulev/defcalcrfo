def def_facing_to_in_game(def_facing):
    """Преобразование DefFacing в InGame_DefFacing"""
    if def_facing <= 0:
        return 0  # Избегаем деления на ноль или отрицательных значений
    in_game_def_facing = (100 / def_facing) ** (10 / 13) + 0.5
    return int(round(in_game_def_facing))  # Округляем до ближайшего целого

def in_game_to_def_facing(in_game_def_facing):
    """Преобразование InGame_DefFacing в DefFacing"""
    if in_game_def_facing <= 0.5:
        return float('inf')  # Если значение меньше или равно 0.5, DefFacing становится бесконечным
    def_facing = 100 / ((in_game_def_facing - 0.5) ** (13 / 10))
    return def_facing

# Интерактивный калькулятор
while True:
    print("\nВыберите действие:")
    print("1. Перевести DefFacing в InGame_DefFacing")
    print("2. Перевести InGame_DefFacing в DefFacing")
    print("3. Выйти")
    
    choice = input("Введите номер действия (1/2/3): ")
    
    if choice == '1':
        try:
            def_facing = float(input("Введите значение DefFacing: "))
            in_game_def_facing = def_facing_to_in_game(def_facing)
            print(f"InGame_DefFacing: {in_game_def_facing}")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")
    
    elif choice == '2':
        try:
            in_game_def_facing = int(input("Введите значение InGame_DefFacing: "))
            def_facing = in_game_to_def_facing(in_game_def_facing)
            if def_facing == float('inf'):
                print("DefFacing: Бесконечность (значение слишком маленькое)")
            else:
                print(f"DefFacing: {def_facing:.2f}")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
    
    elif choice == '3':
        print("Выход из программы.")
        break
    
    else:
        print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")