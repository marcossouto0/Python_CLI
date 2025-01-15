from typing import Callable
from os import system
from colorama import init, Fore

init(autoreset=True)

class CLI:

    def __init__(self, title: str = "Main Menu", main_menu: bool = True):
        self.options: list[list[str, Callable[[], None]]] = []
        self.title = title
        self.main_menu = main_menu

    def __line(self, size: int = 42):
        """Returns a line of dashes of the given size."""
        return '-' * size

    def __choose(self):
        """Prompts the user to choose an option and returns the chosen index."""
        while True:
            try:
                n: int = int(input(Fore.YELLOW + 'Choose an option: '))

            except (ValueError, TypeError):
                print(Fore.RED + 'ERROR! Invalid input. Please enter a number.')

            except KeyboardInterrupt:
                print(Fore.RED + '\nUser interrupted')
                exit()

            else:
                if n == 0 or 1 <= n <= len(self.options):
                    return n
                else:
                    print(Fore.RED + 'ERROR! Choose a valid option')

    def add_options(self, title: str, function: Callable[[], None]):
        """Adds an option to the menu."""
        self.options.append([title, function])

    def run(self):
        """Runs the CLI menu."""
        system('cls')
        if not self.options:
            print(Fore.RED + 'No options added')
            if self.main_menu:
                input(Fore.YELLOW + 'Press enter to exit...')
                return
            else:
                input(Fore.YELLOW + 'Press enter to go back...')
                return

        print(Fore.CYAN + self.__line())
        print(Fore.CYAN + self.title.center(42))
        print(Fore.CYAN + self.__line())

        for i, (title, _) in enumerate(self.options):
            print(Fore.GREEN + f'{i + 1} - {title:>38}')

        if not self.main_menu:
            print(Fore.GREEN + f'0 - {"Back":>38}')

        if self.main_menu:
            print(Fore.GREEN + f'0 - {"Exit Program":>38}')

        print(Fore.CYAN + self.__line())

        choose = self.__choose()

        if choose == 0 and self.main_menu:
            exit()

        if choose == 0 and not self.main_menu:
            return

        if choose:
            self.options[choose - 1][1]()
            self.run()
        return


if __name__ == "__main__":
    main = CLI()
    calc = CLI("Calculator", False)

    def sum():
        a = int(input('First number: '))
        b = int(input('Second number: '))
        print(f'The sum of {a} + {b} is {a + b}')
        input('Press enter to go back...')

    calc.add_options("Sum", sum)

    main.add_options("Calculator", calc.run)
    main.run()
