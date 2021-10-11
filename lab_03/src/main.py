from sortings import Sorting


def output_menu(chosen_sorting: str) -> None:
    print('\033[1mChoose one of the action:\033[0m\n'
          '\033[33m-----------------One sorting----------------\033[0m\n'
          '\033[0m1) Set the name of chosen sorting (\033[34mcomb, gnome, heap\033[0m)\n'
          f'2) Use chosen sorting (\033[34m{chosen_sorting}\033[0m)\n'
          f'3) Test sorting by random numbers (\033[34m{chosen_sorting}\033[0m)\n'
          '\033[33m-----------------All sorting----------------\033[0m\n'
          '4) Use all sorting (\033[34mcomb, gnome, heap\033[0m)\n'
          '5) Test all sorting by random numbers (\033[34mcomb, gnome, heap\033[0m)\n'
          '\033[33m--------------------------------------------\033[0m\n'
          '0) Exit\n')


def main() -> None:
    sorting = Sorting()
    algorithm = 'Not chosen'

    while True:
        output_menu(algorithm)
        command = input('Your command: ')
        if command == '1':
            name = input('Input name: ')
            if name in sorting.sorting:
                algorithm = name
                sorting.set_algorithm(name)
                print(f'\033[32mYou correctly choose another algorithm: "{name}"\033[0m\n')
            else:
                print('\033[31mWrong name!\033[0m\n')
        elif command == '2':
            if not sorting.name:
                print('\033[31mYou should choose the algorithm!\033[0m\n')
                continue
            try:
                input_array = list(map(int, input('Input array which you want to sort:\n').split()))
            except ValueError:
                print('There should be only numbers')
            else:
                sorting.execute(input_array)
                input_array = ' '.join([str(element) for element in input_array])
                print(f'Sorting array:\n{input_array}\n')
        elif command == '3':
            if not sorting.name:
                print('\033[31mYou should choose the algorithm!\033[0m\n')
                continue
            sorting.test_sorting()
        elif command == '5':
            tmp = sorting.name
            for name in sorting.sorting:
                sorting.set_algorithm(name)
                sorting.test_sorting()
            sorting.set_algorithm(tmp)

        elif command == '0':
            exit()
        else:
            print('\033[31mWrong command!\033[0m\n')


if __name__ == '__main__':
    main()
