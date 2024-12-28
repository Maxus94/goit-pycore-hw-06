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
        digits = re.findall(r"\d", self.value)
        if len(self.value) == 10 and len (digits) == 10:
            super().__init__(value)            
        else:
            raise ValueError("Phone number must have 10 digits")        
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
        
    def add_phone(self, phone):        
        self.phones.append(phone)
        print(self.phones)

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else: 
            print('Such phone number does not exist')

    def edit_phone(self, phone, new_phone):
        if phone in self.phones:
            self.phones.remove(phone)
            self.phones.append(new_phone)
        else: 
            print('Such phone number does not exist')


    def __str__(self):
        # return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    def __init__(self):    
        self.data = {}
    
    def add_record(self, record):        
        self.data[record.name.value] = record        
    def find(self, name):        
        print(self.data)
        return(self.data[name])
    def delete(self, name):
        self.data.pop(name)
               
    def __str__(self):        
        # text = ''
        # for name, record in self.data.items():
        #     text = text + str(record.name.value)
        # print(text)

        # return f"Record name: {self.data}"
        return f"Record name: {self.data.record.name.value}, phones: {'; '.join(p for p in self.phones)}"

book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
# print(john_record)
book.add_record(john_record)
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)
for name, record in book.data.items():
    print(record)

john = book.find("John")
print("Print", john)
print(book)
book.delete("Jane")
print(book)