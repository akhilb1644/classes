class Person:
    def __init__(self,firstName,lastName,birthplace,id):
        self.firstName = firstName
        self.lastName = lastName
        self.birthplace = birthplace
        self.id = id
        
    def show_id(func):
        def reg(self,*args,**kwargs):
            print("\nYour ID has been shown.")
            func(self,*args,**kwargs)
        return reg
    
    @show_id # This is a decorator
    def take_debt(self,dollars):
        print(f"A debt of ${dollars} has been taken out.")
    
    @show_id # This is a decorator
    def fly_to_paris(self):
        print("I am flying to Paris.")
        
    def print_details(self):
        print(f"My name is {self.firstName.title()} {self.lastName.title()} and I was born in the {self.birthplace}. My ID is {self.id}.")
