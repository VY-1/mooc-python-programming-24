# Write your solution here:
def sort_by_remaining_stock(items: list):

    #function to return stock count
    def sort_by_stock(item: tuple):
        return item[2]

    #returns sorted items based on stock count
    return sorted(items, key=sort_by_stock)

if __name__=="__main__":
    products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)]

    for product in sort_by_remaining_stock(products):
        print(f"{product[0]} {product[2]} pcs")