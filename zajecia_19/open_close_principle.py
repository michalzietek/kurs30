import abc


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price





# zly przyklad
# class Order:
#     def __init__(self, items, discount_type):
#         self.items = items
#         self.discount_type = discount_type
#
#     def calculate_order_value(self):
#         total = sum(item.price for item in self.items)
#         if self.discount_type == "premium":
#             return total * 0.7
#         elif self.discount_type == "standard":
#             return total * 0.9
#         elif self.discount_type == "gift card":
#             return total - 50
#
class Order:
    def __init__(self, items, discount):
        self.items = items
        self.discount = discount

    def calculate_order_value(self):
        total = sum(item.price for item in self.items)
        return self.discount.calculate(total)


class Discount(abc.ABC):
    @abc.abstractmethod
    def calculate(self, order_value):
        raise NotImplementedError()


class PremiumDiscount(Discount):
    def calculate(self, order_value):
        return order_value * 0.7


class StandardDiscount(Discount):
    def calculate(self, order_value):
        return order_value * 0.9


class GiftCardDiscount(Discount):
    def __init__(self, gift_card_value):
        self.gift_card_value = gift_card_value

    def calculate(self, order_value):
        return order_value - self.gift_card_value


class VeteranDiscount(Discount):
    def __init__(self, id_card):
        self.id_card = id_card

    def check_id_card(self):
        pass

    def calculate(self, order_value):
        self.check_id_card()
        return order_value * 0.1





order = Order(items=[Item("ksiazka", 50), Item("pilka", 30)], discount=GiftCardDiscount(gift_card_value=20))
print(order.calculate_order_value())
order = Order(items=[Item("ksiazka", 50), Item("pilka", 30)], discount=StandardDiscount())
print(order.calculate_order_value())