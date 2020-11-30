
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.total_withdraw = 0

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount) is True:
            self.ledger.append({'amount': -(amount), 'description': description})
            self.balance -= amount
            self.total_withdraw += amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, other):
        if self.check_funds(amount) is True:
            self.withdraw(amount, "Transfer to " + other.name)
            other.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        return self.balance >= amount

    def __repr__(self):
        output = "{:*^30}".format(self.name) + '\n'
        for item in self.ledger:
            output += "{:23}{:>7.2f}".format(item['description'][:23], item['amount']) + '\n'
        output += "Total:{:7.2f}".format(self.balance) 
        return output




def create_spend_chart(categories):
    output = "Percentage spent by category\n"
    num_dash = 1 + (len(categories) * 3)

    total_withdraw = 0
    for category in categories:
        total_withdraw += category.total_withdraw

    percentages = []
    for category in categories:
        percentage = (category.total_withdraw / total_withdraw) * 100
        percentages.append(percentage)

    counter = 100
    while counter >= 0:
        output += "{:3d}|".format(counter)
        for percentage in percentages:
            status = 'o' if percentage >= counter else ' '
            output += ' ' + status + ' '
        output += ' \n'
        counter -= 10

    output += "{}{}{}".format(' ' * 4, '-' * num_dash, '\n')
    
    max_len = 0
    for category in categories:
        if len(category.name) > max_len:
            max_len = len(category.name)
    
    for num in range(max_len):
        output += ' ' * 4   
        for i in range(len(categories)):
            name = categories[i].name
            letter = name[num] if num < len(name) else ' '
            output += " {} ".format(letter)

        output += ' '
        if num != max_len - 1:
            output += '\n' 

    return output


