import random


class User:
    def __init__(self, name):
        self.cards = []
        self.name = name
        self.deck_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "король", "дама", "валет", "туз"]

    def random_cards(self):
        user_cards = random.choice(self.deck_list)
        self.deck_list.remove(user_cards)
        return user_cards

    def sum_points(self, sum_user=0):
        for i_cards in self.cards:
            if isinstance(i_cards, int):
                sum_user += i_cards
            elif i_cards in ["король", "дама", "валет"]:
                sum_user += 10
            else:
                if sum_user + 11 <= 21:
                    sum_user += 11
                else:
                    sum_user += 1
        if sum_user > 21:
            sum_user = "Сгорел"
        return sum_user

    def print_cart(self):
        print(f"На руках y {self.name} следующие карты: {self.cards}")

    def game(self, count_cards, indicat):
        for _ in range(count_cards):
            new_cart = self.random_cards()
            self.cards.append(new_cart)
            if indicat == 1:
                print(f"Пришла карта: {new_cart}")
                self.print_cart()

    def print_answer(self, user_sum, computer_sum):
        if user_sum == computer_sum:
            print("Ничья")
        elif isinstance(user_sum, str) and isinstance(computer_sum, int):
            print("Победил компьютер.")
        elif isinstance(computer_sum, str) and isinstance(user_sum, int):
            print(f"Победа {user_1.name}")
        elif user_sum > computer_sum:
            print(f"Победа {user_1.name}")
        else:
            print("Победил компьютер.")

    def print_cart_user(self, user_sum):
        print(f"Карты {self.name}: {self.cards}. Сумма баллов: {user_sum}.")

    def game_user(self, count_cards, indic):
        self.game(count_cards, indic)
        if indic == 1:
            add_cart = input("Берем карту? ")
            if add_cart.lower() in ["yes", "1", "да", "ok", "ок"]:
                return True
        return False


user_1 = User("Миша")
computer = User("Компьютер")
computer.deck_list = user_1.deck_list
count = 2
while True:
    answer = user_1.game_user(count, 1)
    computer.game_user(count, 2)
    if answer:
        count = 1
    else:
        sum_cart_user = user_1.sum_points()
        sum_computer = computer.sum_points()
        user_1.print_answer(sum_cart_user, sum_computer)
        user_1.print_cart_user(sum_cart_user)
        computer.print_cart_user(sum_computer)
        break

# зачёт!
