class Duck: 
    def quack(self): 
        print ("Quaaaaaaack! from DUCK class") 
    def feathers (self): 
        print ("The duck has white and grey feathers from DUCK class") 
    
class Person(Duck): 
    def quack (self): 
        print ("The person class imitates a duck from PERSON class") 
    def feathers (self): 
        print ("The person takes a feather from the ground and shows it from PERSON class") 
    def name (self):
        print ("John Smith from PERSON class") return "" 
def in_the_forest():
    person = Person() # created an object for Person Class
    duck=Duck() # created an object for Duck class 
    
    person.quack()
    person.feathers()
    person.name() 
    print("------------------------------")
    
    
    
    duck.quack()
    duck.feathers()
 in_the_forest()