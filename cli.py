from typing import Callable, List, Tuple
from os import system, name
from colorama import init, Fore

init(autoreset=True)

class CLI:

    def __init__(self, title: str = "Main Menu", main_menu: bool = True):
        self.options: List[Tuple[str, Callable[[], None]]] = []
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
                if 0 <= n < len(self.options)+1:
                    return n
                else:
                    print(Fore.RED + 'ERROR! Option out of range. Please choose a valid option.')

            except (ValueError, TypeError):
                print(Fore.RED + 'ERROR! Invalid input. Please enter a number.')

            except KeyboardInterrupt:
                print(Fore.RED + '\nUser interrupted')
                exit()

    def add_options(self, title: str, function: Callable[[], None]):
        """Adds an option to the menu."""
        self.options.append((title, function))

    def display_menu(self) -> None:
        """Displays the menu."""
        system('cls' if name == 'nt' else 'clear')
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

    def run(self) -> None:
        """Runs the CLI menu."""
        if not self.options:
            print(Fore.RED + 'No options added')
            input(Fore.YELLOW + 'Press enter to exit...')
            return

        while True:
            self.display_menu()
            choice = self.__choose()

            if choice == 0:
                if self.main_menu:
                    break
                else:
                    return

            self.options[choice - 1][1]()


if __name__ == "__main__":
    main = CLI()
    calc = CLI("Calculator", False)

    def sum():
        while True:
            try:
                a = int(input('First number: '))
                b = int(input('Second number: '))
                break
            except (ValueError, TypeError):
                print(Fore.RED + 'ERROR! Invalid input. Please enter a number.')
        print(f'The sum of {a} + {b} is {a + b}')
        input('Press enter to go back...')

    calc.add_options("Sum", sum)

    main.add_options("Calculator", calc.run)
    main.run()
