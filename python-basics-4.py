#!/usr/bin/env python
# coding: utf-8

# # Object-Oriented-Programming (OOP)

# ## Tasks Today:
# 
#    
# 
# 1) <b>Creating a Class (Initializing/Declaring)</b> <br>
# 2) <b>Using a Class (Instantiating)</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Creating One Instance <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Creating Multiple Instances <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #1 - Create a Class 'Car' and instantiate three different makes of cars <br>
# 3) <b>The \__init\__() Method</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) The 'self' Attribute <br>
# 4) <b>Class Attributes</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Initializing Attributes <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Setting an Attribute Outside of the \__init\__() Method <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Setting Defaults for Attributes <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Accessing Class Attributes <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Changing Class Attributes <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) In-Class Exercise #2 - Add a color and wheels attribute to your 'Car' class <br>
# 5) <b>Class Methods</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Creating <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Calling <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Modifying an Attribute's Value Through a Method <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Incrementing an Attribute's Value Through a Method <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) In-Class Exercise #3 - Add a method that prints the cars color and wheel number, then call them <br>
# 6) <b>Inheritance</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax for Inheriting from a Parent Class <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) The \__init\__() Method for a Child Class (super()) <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Defining Attributes and Methods for the Child Class <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Method Overriding <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) In-Class Exercise #4 - Create a class 'Ford' that inherits from 'Car' class and initialize it as a Blue Ford Explorer with 4 wheels using the super() method <br>
# 7) <b>Classes as Attributes</b> <br>
# 8) <b>Exercises</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Exercise #1 - Turn the shopping cart program from yesterday into an object-oriented program <br>

# ## Creating a Class (Initializing/Declaring)
# <p>When creating a class, function, or even a variable you are initializing that object. Initializing and Declaring occur at the same time in Python, whereas in lower level languages you have to declare an object before initializing it. This is the first step in the process of using a class.</p>

# In[2]:


class Car():
    wheels = 4
    color = 'blue'


# ## Using a Class (Instantiating)
# <p>The process of creating a class is called <i>Instantiating</i>. Each time you create a variable of that type of class, it is referred to as an <i>Instance</i> of that class. This is the second step in the process of using a class.</p>

# ##### Creating One Instance

# In[3]:


ford = Car()

print(ford.color)


# ##### Creating Multiple Instances

# In[ ]:


chevrolet = Car()
honda = Car()
porsche = Car()


# ##### In-Class Exercise #1 - Create a Class 'Car' and Instantiate three different makes of cars

# In[6]:


class Car():
    wheels = 4
    color = 'red'
    doors ='suicide'
rollsroyce = Car()
print(rollsroyce.doors)


# ## The \__init\__() Method <br>
# <p>This method is used in almost every created class, and called only once upon the creation of the class instance. This method will initialize all variables needed for the object.</p>

# In[14]:


class Car():
    engine = '4.7L' #global within class -any method inside the class can call upon this variable
    
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels
mazda = Car('black',4)
subaru = Car('blue', 3)
print(subaru.color)


# ##### The 'self' Attribute <br>
# <p>This attribute is required to keep track of specific instance's attributes. Without the self attribute, the program would not know how to reference or keep track of an instance's attributes.</p>

# In[ ]:


# see above


# ## Class Attributes <br>
# <p>While variables are inside of a class, they are referred to as attributes and not variables. When someone says 'attribute' you know they're speaking about a class. Attributes can be initialized through the init method, or outside of it.</p>

# ##### Initializing Attributes

# In[16]:


# see above

class Toy():
    kind = 'car' #this is called a constant
    
    def __init__(self, rooftop, horn, wheels):
        self.rooftop = rooftop # these are the actual attributes
        self.horn = horn 
        self.wheels = wheels
tonka_truck= Toy(1,1,4)# one roof/horn, 4 wheels
hotwheels_truck = Toy(1,4,18)
print(hotwheels_truck.wheels)


# ##### Accessing Class Attributes

# In[ ]:


# See Above
# ie (hotwheels_truck.wheels)


# ##### Setting Defaults for Attributes

# In[18]:


class Car():
    engine = '4.7L'
    
    def __init__(self, wheels):
        self.wheels = wheels
        self.color = 'blue'
honda = Car(4)
print(honda.color)


# ##### Changing Class Attributes <br>
# <p>Keep in mind there are global class attributes and then there are attributes only available to each class instance which won't effect other classes.</p>

# In[20]:


jeep = Car(8)

print(f'before change: {jeep.color}')
jeep.color = 'white'
print(f'\nafter change: {jeep.color}')


# In[ ]:





# ##### In-Class Exercise #2 - Add a doors and seats attribute to your 'Car' class then print out two different instances with different doors and seats

# In[23]:


class Car():
    def __init__(self,doors,seats):
        self.doors = doors
        self.seats = seats
beetle = Car(2,5)
mini_van = Car(4,7)
print(beetle.seats)
print(mini_van.doors)


# ## Class Methods <br>
# <p>While inside of a class, functions are referred to as 'methods'. If you hear someone mention methods, they're speaking about classes. Methods are essentially functions, but only callable on the instances of a class.</p>

# ##### Creating

# In[1]:


class ShoppingBag():
    """
        the ShoppingBag class will have handles, capacity, and
        items to place inside. 
        
        attributes for the class:
        - handles: expected to be an integer
        - capacity: expected to be a string OR an integer
        - items: expected to be a list
    """
    def __init__(self,handles,capacity,items):
        self.handles = handles
        self.capacity = capacity
        self.items = items
    #write a method that shows the items in our ShoppingBag / this is out item list 
    def showShoppingBag(self):
        print("you have items in your bag!")
        for item in self.items:
            print(item)
    #show the capacity of ShoppingBag - how much?
    def showCapacity(self):
        print(f' your capacity is: {self.capacity}')
        
    # add item(s) to the item list for the ShoppingBag
    def addToShoppingBag(self):
        products = input('what would you like to add? ')
        self.items.append(products)
        
    #change the capacity of the ShoppingBag
    def changeBagCapacity(self, capacity):
        self.capacity = capacity
    
    #increase the capacity of the ShoppingBag by defauly amount that we set to 10
    def increaseCapacity(self, changed_capacity = 10):
        if self.capacity == isinstance(self.capacity,str):
            print("we can not add that at this time")
        else:
            self.capacity += changed_capacity
    


# ##### Calling

# In[25]:


# See Above
#so far, we created the idea of ShoppingBag
wholeFoods_bag = ShoppingBag(2,10,[])

#create a function to ru;n the ShoppingBag methods on out wholeFoods_bag instance
#def run():
#    while True:
#        response = input('what do you want to do? add/show/quit ')
        
#        if response.lower()== 'quit':
            wholeFoods_bag.showShoppingBag()
#            print('thanks for shopping!')
#            break
#        elif response.lower() == 'add':
#            wholeFoods_bag.addToShoppingBag()
#        elif response.lower()== 'show':
            wholeFoods_bag.showShoppingBag()
#        else:
#            print('try another command')
#run()


# ##### Modifying an Attribute's Value Through a Method

# In[27]:


# show the capacity
wholeFoods_bag.showCapacity()
print(' capacity AFTER the change...')
wholeFoods_bag.changeBagCapacity(40)
wholeFoods_bag.showCapacity()


# ##### Incrementing an Attribute's Value Through a Method

# In[30]:


wholeFoods_bag.showCapacity()
print(' after increase: ')
wholeFoods_bag.increaseCapacity()
wholeFoods_bag.showCapacity()


# ##### In-Class Exercise #3 - Add a method that takes in three parameters of year, doors and seats and prints out a formatted print statement with make, model, year, seats, and doors

# In[ ]:


# Create class with 2 paramters inside of the __init__ which are make and model

# Inside of the Car class create a method that has 4 parameter in total (self,year,door,seats)

# Output: This car is from 2019 and is a Ford Expolorer and has 4 doors and 5 seats

class NewCar():
    
    def __init__(self,make,model):
        self.make = make 
        self.model = model
    def CarInfo(self,year=2019,doors=4,seats=5):

        print('This car is from {0} and is a {1} {2} and has {3} doors and {4} seats'.format(year,self.make,self.model,doors,seats))
nc = NewCar('ford','explorer')
nc.CarInfo()


# ## Inheritance <br>
# <p>You can create a child-parent relationship between two classes by using inheritance. What this allows you to do is have overriding methods, but also inherit traits from the parent class. Think of it as an actual parent and child, the child will inherit the parent's genes, as will the classes in OOP</p>

# ##### Syntax for Inheriting from a Parent Class

# In[ ]:


# create a parent class and call it Animal 
class Animal():
    acceleration = 9.8
    
    def __init__(self, name, species, legs=4):
        self.name = name
        self.species= species
        self.legs = legs
        
    #generic parent method - this is not overriding anything 
    def makeSound(self):
        print('make some generic sound')
#now we are making our chuld class.. Dog

class Dog(Animal):
    speed = 15
    
    def printInfo(self):
        print('the dog has {self.speed}mph in speed and {self.acceleration}')
#creation of our grand child class -- mutt

class Mutt(Dog):
    color = "tan"
    
    #override the ANIMAL class - using the Dog clas to overwrite the __init)) from Animal
    def __init__(self, name, species, eye_color, legs=4):
        Dog.__init__(self, name, species,legs)
        self.eye_color = eye_color
    
    #override the makeSound method (which is coming from...ANIMAL)
    def makeSound(self):
        noise = 'bark'
        return noise
lassie = Dog('Lassie', 'Dog')
basic_animal = Animal ('generic animal name', 'generic animal species')
buster = Mutt('Buster','mut','brown')

print(buster.makeSound())
print(bustser.acceleration())


# ##### The \__init\__() Method for a Child Class - super()

# In[ ]:


class Puppy(Dog):
    color ='black and brown'
    
    #override the animal class init(via dog class)
    def __init__(self, name, soecies, eye_color, legs =4):
        super().__init__(name, species,legs)
        self.eye_color = eye_color
        
    #override the makeSound method 
     def makeSound(self):
        noise = 'bark'
        return noise
lassie = Dog('Lassie', 'Dog')
basic_animal = Animal ('generic animal name', 'generic animal species')
buster = Mutt('Buster','mut','brown')

print(buster.makeSound())
print(bustser.acceleration())


# ##### Defining Attributes and Methods for the Child Class

# In[ ]:


# See Above


# ##### Method Overriding

# In[ ]:


# See Above


# ## Classes as Attributes <br>
# <p>Classes can also be used as attributes within another class. This is useful in situations where you need to keep variables locally stored, instead of globally stored.</p>

# In[ ]:


class Battery():
    volts = 7.8
    
    def __init__(self, cells):
        self.cells = cells

class Car():
    def __init__(self, year, make, model, battery):
        self.year = year
        self.make = make
        self.model = model
        self.battery = battery
    def printInFo(self):
        return f'{self.year}{self.make}{self.model}{self.battery.cells}

my_battery = Battery(20)
    
telsa = Car(2019, 'Tesla','Model X', my_battery)
print(tesla.battery.cells)
telsa.printInFo()


# # Exercises

# ### Exercise 1 - Turn the shopping cart program from yesterday into an object-oriented program
# 
# The comments in the cell below are there as a guide for thinking about the problem. However, if you feel a different way is best for you and your own thought process, please do what feels best for you by all means.

# In[ ]:


# Create a class called cart that retains items and has methods to add, remove, and show
class ShoppingCart():
    def __init__(self):
        self.total = 0 
        self.items = {}
    
    def add_items(self,item_name,quantity,price):
        self.total = (quantity * price)
        self.items = {item_name : quantity}

    def remove_items(self,item_name,quantity,price):
        self.total -= (quantity * price)
        if quantity > self.items [item_name]:
            del self.items
        self.items[item_name]-= quantity
    
    def show_items(self,item_name,quantity,price):
        return self.items   


# ### Exercise 2 - Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case

# In[ ]:


class One_String():
    def __init__(self):
        self.str_one = " "
    
    def get_string(self):
        self.str_one = input()

    def print_string(self):
        print(self.str_one.upper)

