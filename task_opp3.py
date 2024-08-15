from task_opp1 import MagicalContact

class MagicalCreature(MagicalContact):

    def __init__(self,species,is_tame,name,email,phone_number):
        super().__init__(name,email,phone_number)
        self.__species=species
        self.__is_tame=is_tame

    def get_species(self):
        return self.__species
    
    def is_tame(self):
        return self.__is_tame
    
    def describe(self):
        super().describe()
        # print("name + " + self.__name + "mail ")
        print("species:"+self.__species+" "+ "is tame"+self.__is_tame)
