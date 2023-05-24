import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "Q": 4,
    "K": 6,
    "J": 8
}

symbol_value = {
    "A": 6,
    "Q": 4,
    "K": 3,
    "J": 2
}

def check_win(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines



def slot_spin(rows, cols, symbols):
    all_symbols = [] #list
    for symbol, symbol_count in symbols.items(): #iterate thru dictionary
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def print_slot_machine(columns):
    #transposing matrix
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): #enumerate -- get index of item
            if i != len(columns) -1: #dont print pipe last
                print(column[row], end = " | ")
            else:
                print(column[row], end="")
        
        print()


def deposit():
    while True:
        amount = input("Enter Deposit Amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Invalid amount.")
        else:
            print("Enter a number.")

    return amount

def get_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ") ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Invalid number of lines.")
        else:
            print("Enter a number")

    return lines

def get_bet():
    while True:
        amount = input("Enter Bet Amount per Line: $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Enter a number.")

    return amount

def spin(balance):
        
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Insufficient balance! (Balance: ${balance})")
        else:
            break

    print(f"Betting ${bet} on {lines} lines.\nTotal bet: ${total_bet}")

    slots = slot_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_win(slots, lines, bet, symbol_value)
    print(f"Win: ${winnings}")
    print(f"Winning lines: ", *winning_lines)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance: ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance) 
    
    print(f"Final balance ${balance}")

main()