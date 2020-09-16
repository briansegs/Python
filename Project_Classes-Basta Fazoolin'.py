class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    print('{} menu is available from {} to {}'.format(self.name, self.start_time, self.end_time))
    return str(self.items)
       

  def calculate_bill(self, purchased_items):
    self.purchased_items = purchased_items
    total = 0 
    for item in self.purchased_items:
      total += self.items[item]
    return total



brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch_menu = Menu('brunch', brunch_items, 1100, 1600 )
#print(brunch_menu)

early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}
early_bird_menu = Menu('early_bird', early_bird_items, 1500, 1800)
#print(early_bird_menu)

dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}
dinner_menu = Menu('dinner', dinner_items, 1700, 2300)
#print(dinner_menu)

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids_menu = Menu('kids', kids_items, 1100, 2100)
#print(kids_menu)

#print(brunch_menu.calculate_bill(["pancakes", "home fries", "coffee"]))
#print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


class Franchise:
  def __init__(self, address, menus):
    assert isinstance(address, str)
    assert isinstance(menus, list)
    self.address = address
    self.menus = menus

  def __repr__(self):
    return "We are located at {}".format(self.address)

  def available_menus(self, time):
    assert isinstance(time, int)
    self.time = time
    for menu in self.menus:
      if self.time >= menu.start_time and self.time <= menu.end_time:
         print(menu)
   
     

flagship_store = Franchise("1232 West End Road", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
new_installment = Franchise("12 East Mulberry Street", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])

#print(flagship_store)
#print(new_installment)
#flagship_store.available_menus(1200)
print('-------------')
#new_installment.available_menus(1700)


class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

  def print_menu(self, index, time):
    self.franchises[index].available_menus(time)




business1 = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_menu = Menu('arepas', arepas_items, 1000, 2000)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

business2 = Business("Take a' Arepa", [arepas_place])

#print(arepas_place)
#arepas_place.available_menus(1700)

business2.print_menu(0, 1200)





