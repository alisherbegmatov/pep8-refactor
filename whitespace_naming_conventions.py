# By Kami Bigdely
# PEP8 - whitespaces and variable names.
class pizza:
    def __init__(obj, breadType, cheeseType, meatType, toppings, size):
        obj.breadType = breadType
        obj.cheeseType = cheeseType
        obj.meatType = meatType
        obj.toppings = toppings
        obj.size = size

    @classmethod
    def chicagoPizza(classType, size):
        bread = 'deep-dish bread'
        cheese = 'mozzarella cheese'
        meatType = 'Italian sausage'
        toppings = ['green bell pepper', 'mushroom',
                    'chunky tomato sauce', 'onion']
        return classType(bread, cheese, meatType, toppings, size)

    @classmethod
    def californiaPizza(ct, meatType, size):
        bread = 'thin crust'
        CHEESE = 'feta cheese'
        toppings = ['garlic', 'spinach', 'broccoli',
                    'olives', 'red onion', 'red bell pepper']
        return ct(bread, CHEESE, meatType, toppings, size)

    def printInfo(obj):
        print('bread type is: ', obj.breadType)
        print('cheese type is: ', obj.cheeseType)
        print('meat type is: ', obj.meatType)
        print('Toppings are: ', end='')
        print(', '.join(map(str, obj.toppings)))


myPizza = pizza.californiaPizza('chicken', 'large')
myPizza.printInfo()
