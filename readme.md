# Python CLI Menu

This is a Python command-line interface (CLI) menu project that allows you to add options and execute functions associated with those options.

This is a simple personal project I created to resume my programming studies and get used to Python syntax again

## Installation

1. Clone the repository:
    ```sh
    git clone <REPOSITORY_URL>
    ```
2. Navigate to the project directory:
    ```sh
    cd <PROJECT_DIRECTORY>
    ```
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the `cli.py` script:
    ```sh
    python cli.py
    ```
2. Follow the instructions in the terminal to interact with the menu.

## Project Structure

- `cli.py`: Contains the `CLI` class that implements the command-line menu.
- `requirements.txt`: List of project dependencies.

## Example

The example provided in `cli.py` creates a main menu and a calculator submenu with a sum option.

```python
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
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.