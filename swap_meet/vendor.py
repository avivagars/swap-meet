class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        categories = []
        for item in self.inventory:
            if item.category == category:
                categories.append(item)
        return categories

    def swap_items(self, vendor1, my_item, their_item):
        vendor1 = Vendor()
        self.inventory.add(my_item)
        self.inventory.remove(my_item)


        
