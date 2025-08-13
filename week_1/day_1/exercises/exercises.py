# ------ Exercise 1
print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")
# ------ Exercise 2
print(pow(99 , 3) * 8 )
# ------ Exercise 3
user_name = input("Entrer votre nom : ")
if(user_name == 'othmane'):
    print("we have the same name ")
else : print('nice name')
# ------ Exercise 4
user_height = int(input("Enter your height in centemeter : ")) 
if(user_height >= 145):
    print("tall enough to ride")
else : print('need to grow some more to ride.')
# ------ Exercise 5
my_fav_numbers = {1,2}
my_fav_numbers.update({7,6})
print(my_fav_numbers)
mylist = list(my_fav_numbers)
mylist.remove(mylist[-1])
my_set = set(mylist)
print(my_set)
friend_fav_numbers = {5,6,3,2,9,10}
our_fav_numbers = friend_fav_numbers.union(my_set)
print(our_fav_numbers)
# ------ Exercise 6
# is not possible to add number in more values in tuple already declared

# ------ Exercise 7
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")
print(basket)
print(basket.count('Apples'))
basket.clear()

print(basket)
# ------ Exercise 8

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
pastrami = "Pastrami sandwich"

while(pastrami in sandwich_orders):
    sandwich_orders.remove(pastrami)
print(sandwich_orders)


finished_sandwiches = []

i = 0
while(len(sandwich_orders) > 0):
    finished_sandwiches.append(sandwich_orders[i])
    sandwich_orders.remove(sandwich_orders[i])

for sandwich in finished_sandwiches :
    print('I made your ' + sandwich)
