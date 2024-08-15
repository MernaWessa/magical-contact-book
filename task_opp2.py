from task_opp1 import MagicalContact


class WizardOrWitch(MagicalContact):

    def __init__(self,core,wood,length,house,name,email,phone_number):
        super().__init__(name,email,phone_number)
        self.__wand={
            "core":core,
            "wood":wood,
            "length":length

        }
        self.__house=house
    
    def get_wand(self):
        return self.__wand["core"] +" " + self.__wand ["wood"]+" "+self.__wand["length"]
    
    def get_house(self):
        return self.__house
    
    def describe(self):
        super().describe()
        print("wand: "+self.__wand["core"] +" " + self.__wand ["wood"]+" "+self.__wand["length"])
        print("house:"+self.__house)

        
    

