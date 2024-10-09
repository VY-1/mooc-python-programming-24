# TEE RATKAISUSI TÄHÄN:

class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def product(self, n: int):
        return self.products[n - 1][0]

    def number(self, n: int):
        return self.products[n - 1][1]

    def __iter__(self):
        self.n = 0

        return self     #returns reference object as iterator is implemented with the same class definition

    def __next__(self):
        if self.n < len(self.products):
            product = self.products[self.n]  # product at index n
            self.n += 1  # increment index by 1
            return product  # return product
        else:
            raise StopIteration  # Raise StopIterration when all products have been traversed


if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.add("bananas", 10)
    shopping_list.add("apples", 5)
    shopping_list.add("pineapple", 1)

    for product in shopping_list:
        print(f"{product[0]}: {product[1]} units")
