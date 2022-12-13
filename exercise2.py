class Animal:
    
    name = "Buddy"
    
    def __init__(self, eats, sleeps, plays, energy=10):
        self.eats = eats
        self.plays = plays
        self.sleeps = sleeps 
        self.energy = energy
        
    def rests(self, minutes):
        unit_increase = minutes + 1 
        self.energy += unit_increase +1 #self.gas_level = self.gas_level - unit_decrease
        print(f"{self.name} now has an energy level of {self.energy}")
        
    def ingests(self, food):
        unit_increase = food + 1
        self.energy += unit_increase +1
        print(f"{self.name} now has an energy level of {self.energy}")
        
    def exerts(self, minutes):
        unit_decrease = minutes - 1
        self.energy -= unit_decrease -1 #self.gas_level = self.gas_level - unit_decrease
        print(f"{self.name} now has an energy level of {self.energy}")
              
buddy = Animal('4', '5', '6')

buddy.rests(5)              
buddy.ingests(10)
buddy.exerts(20)
    