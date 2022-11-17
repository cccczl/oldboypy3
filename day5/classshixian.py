class shuiguo():

    def __init__(self, name, color):
        self.name = name
        self.color = color



    def shelf_life(self):

        print(f"{self.name.title()} this is 7 day")

    def shuiguo_print(self):

        print(self.name, self.color)

    def __len__(self):
        return len(self.name)

my_shuiguo = shuiguo('apple' 'orangor', 'red' 'blue')
my_shuiguo.shelf_life()
my_shuiguo.shuiguo_print()
print(len(my_shuiguo))