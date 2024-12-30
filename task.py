from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value        

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    def __init__(self, value):
        if value:
            super().__init__(value)
        else:
            print("Name is compulsory")
    

class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        digits = re.findall(r"\d", value)        
        if len(value) == 10 and len(digits) == 10:
            super().__init__(value)            
        else:
            raise print("Phone number must have 10 digits")                

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
        
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):                
        phone_found = False
        for phone_num in self.phones:            
            if phone_num.value == phone:                
                self.phones.remove(phone_num)
                phone_found = True        

        if not phone_found:
            print(f"Phone number {phone} does not exist")

    def edit_phone(self, phone, new_phone):                
        phone_found = False
        for phone_num in self.phones:            
            if phone_num.value == phone:                
                self.phones.remove(phone_num)
                self.phones.append(Phone(new_phone))
                phone_found = True            

        if not phone_found:
            print('Such phone number does not exist')     

    def __str__(self):        
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    def __init__(self):    
        self.data = {}
    
    def add_record(self, record):        
        self.data[record.name.value] = record        
    def find(self, name):                
        return(self.data[name])
    def delete(self, name):
        self.data.pop(name)

    def __str__(self):        
        rec='Your address book:\n'
        for name, record in self.items():
            rec = rec + str(record) + '; \n'
        return rec

# book = AddressBook()
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# book.add_record(john_record)
# jane_record = Record("Jane")
# jane_record.add_phone("9879547210")
# book.add_record(jane_record)
# jan_record = Record("Jan")
# jan_record.add_phone("9876543219")
# book.add_record(jan_record)
# john = book.find("John")
# print(john)
# john.edit_phone("1234567890", "1112223333")
# john.add_phone("5555555585")
# john.remove_phone("5555555555")
# print(john)
# print(book)
# book.delete("Jane")
# print(book)