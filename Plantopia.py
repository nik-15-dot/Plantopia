    #1st phase:
import random
    #2nd phase:
class Plant:
    def __init__(self,name,harvest_yield):
        self.name = name
        self.harvest_yield = harvest_yield
        self.growth_stages=["seed","sprout","seedling","mature"]
        self.current_growth_stage="seed"
        self.harvestable=False 
    def grow(self):
        current_index= self.growth_stages.index(self.current_growth_stage)
        if self.current_growth_stage==self.growth_stages[-1]:
            print(f"{self.name} is rocking its ultimate plant glow-up!")
        elif current_index<len(self.growth_stages)-1:
            self.current_growth_stage=self.growth_stages[current_index+1]
            if self.current_growth_stage=="mature":
                self.harvestable=True
                print(f"{self.name} has grown to {self.current_growth_stage} stage!")
            else:
                print(f"{self.name} has grown to {self.current_growth_stage} stage!")
                 
            
    def harvest(self):
        if self.harvestable:
            self.havestable=False
            print(f"Harvested {self.harvest_yield} units from {self.name}!")
            return self.harvest_yield
        else:
            print(f"{self.name} is not ready for harvest yet!")
            return None
        
    #3rd phase
class Tomato(Plant):
    def __init__(self):
        super().__init__("Tomato",10)

class Potato(Plant):
    def __init__(self):
        super().__init__("Potato",5)
        self.growth_stages=["Seed Potato","Sprouting","Vegetative Growth","Tuber Initiation","Tuber Bulking","Harvest"]
class Carrot(Plant):
    def __init__(self):
        super().__init__("Carrot",10)
        self.growth_stages=["Seed","Germination","Vegetative Growth","Root Enlargement","Maturation","Harvest"]
     #4th phase    
def select_items(items):
    if type(items) == dict:
        item_list =list(items.keys())
    elif type(items)==list:
        item_list=items
    else:
        print("Invalid items type")
        return None
    if not item_list:
        print("no items available to select.")
        return None
    for i in range(len(item_list)):
        try:
            item_name=item_list[i].name
        except:
            item_name=item_list[i]
        print(f"{i+1}. {item_name}")
    while True:
        user_input=input("select an item by number:")
        try:
            user_input=int(user_input)
            if 0<user_input<=len(item_list):
                return item_list[user_input-1]
            else:
                print("Invalid selection,try again.")
        except:
            print("Invalid input,please enter a number.")


    #5th phase
class Gardener:
        plant_dict={"Tomato":Tomato,"Potato":Potato,"Carrot":Carrot}
        def __init__(self,name):
            self.name=name
            self.planted_plants=[]
            self.inventory={}
            
        def plant(self):
            selected_plant= select_items(self.inventory)
            if selected_plant in self.inventory and self.inventory[selected_plant]>0:
                self.inventory[selected_plant]-=1
                if self.inventory[selected_plant]==0:
                    del self.inventory[selected_plant]
                new_plant=self.plant_dict[selected_plant]()
                self.planted_plant.append(new_plant)
                print(f"{self.name} planted a {selected_plant}!")
            else:
                print(f"{self.name} doesnt have any {selected_plant} to plant!")

        def tend(self):
            if not self.planted_plants:
                print("empty garden vibes… no plants to tend to 🌱")
                return
            
            for plant in self.planted_plants:
                if plant.harvestable:
                    print(f"{plant.name} time to snatch the harvest 😎")
                else:
                    plant.grow()
                    print(f"{plant.name} has grown to {plant.current_growth_stage} stage!")

        def harvest(self):
            harvestable_plants = [plant for plant in self.planted_plants if plant.harvestable]
            if not harvestable_plants:
                print(f"Bruh, {self.name} got *zero rizz* in the garden… no plants ready to glow up 🌱")
                return

            selected_plant = select_items(harvestable_plants)  
            if selected_plant and selected_plant.harvestable:
                harvest_amount = selected_plant.harvest()
                if selected_plant.name in self.inventory:  
                    self.inventory[selected_plant.name] += harvest_amount
                else:
                    self.inventory[selected_plant.name] = harvest_amount
                    print(f"You harvested a {selected_plant.name}!")
                    self.planted_plants.remove(selected_plant)  
            else:
                print(f"Chill, you can’t bag that plant yet chief 🌱")

        def forage_for_seeds(self):
            seed=random.choice(list(self.plant_dict.keys()))
            if seed in self.inventory:
                self.inventory[seed]+=1
            else:
                self.inventory[seed]=1
            print(f"{self.name} found a {seed} seed!")
        
    #6th phase
all_plant_types = ["Tomato", "Potato", "Carrot"]
valid_commands = ["plant", "tend", "harvest", "forage", "help", "quit"]

    # Print welcome message
print("\n"*2)
print("█" * 30)
print("█" + " " * 58 + "█")
print(" Pull up, bestie! You just entered PLANTOPIA")
print("█" + " " * 58 + "█")
print("█" * 60)
print()

print(" Yo rizzler! Welcome to the giga-chad garden \n"
      "Plant seeds, vibe hard, watch ‘em glow up \n")

print()




    #Create gardener
gardener_name = input("👀 Yo, who dis? Drop ya govy name, plant parent 🌱✨: ")
print(f"Welcome, {gardener_name}! Let's get gardening!\nType 'help' for a list of commands.")
gardener = Gardener(gardener_name)

    #7th phase
while True:
    player_action = input(" what’s the move chief? ")
    player_action = player_action.lower()
    if player_action in valid_commands:
        if player_action == "plant":
            gardener.plant()
        elif player_action == "tend":
            gardener.tend()
        elif player_action == "harvest":
            gardener.harvest()
        elif player_action == "forage":
            gardener.forage_for_seeds()
        elif player_action == "help":
            print("*** Commands ***")
            for command in valid_commands:
                print(command)
        elif player_action == "quit":
            print(" Bye bestieee! Don’t let the plants ghost you ")
            break
    else:
        print("Invalid command.")






            