from task_opp1 import MagicalContact

class MagicalContactBook:
    def __init__(self,contacts):
        self.__contacts=contacts
        

    def add_contacts(self, contact):
        self.__contacts.append(contact) 
    
    def list_contacts(self):
        for i in range (len(self.__contacts)):
            self.__contacts[i].describe()
    def find_contacts(self,name):
        for i in range(len(self.__contacts)):
            if name== self.__contacts[i].name:
                 self.__contacts[i].describe()
                
