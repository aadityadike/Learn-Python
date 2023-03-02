import random

# Global variable.
MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbol = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)

    columns = [[], [], []]
    for _ in range(cols):
        column = []
        current_symbols = all_symbol[:]
        for _ in range(rows):
            value = random.choice(all_symbol)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in column:
            if i != len(column) - 1:
                print(column[row], end="|")
            else:
                print(column[row], end="")
                
    print()

# Deposit amount in the Game.


def deposit():
    while True:
        amount = input("what would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("invalid deposit amount.")
        else:
            print("please enter a number.")
    return amount


# Number of lines you want to bet on.
def get_number_0f_line():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINE) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("please enter a digit.")

    return lines


# Putting money of each line.
def get_bet():
    while True:
        amount = input("what would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("please Enter a digit.")

    return amount


def main():
    balance = deposit()
    lines = get_number_0f_line()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(
                f"you don't have enough balance,your current balance is: {balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to : ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)


main()
