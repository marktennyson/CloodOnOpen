from faker import Faker
from csv import DictWriter
from random import choice, randint
from pandas import read_csv
from os import remove


fields = {
"Name" : "required",
"UserName" : "required",
"Email" : "required",
"Phone" : "required",
"Country Code" : "required",
"Timezone" : "required",
"Affiliate" : "required",
"Share instructor" : "danger",
"LearnerGroups" : "required",
"DateOfBirth" : "required",
"UserType" : "danger",
"Groups" : "danger",
"Address1" : "required",
"Address2" : "required",
"City" : "required",
"State" : "required",
"Pincode" : "required",
"Designation" : "required",
"DateOfJoining" : "required",
"EmployeeBand" : "required",
}

fake:Faker = Faker('en_IN')

class Utils:
    class input:
        def Integer(msg:str=str()) -> int:
            try: return int(input(msg).strip())
            except: return 0
        def String(msg:str=str(), required:bool=False) -> str: 
            while True:
                inp = input(msg).strip() 
                if required and not inp: continue
                else: break
            return inp.strip()  
    def lenSolver(data:str) -> str:
        if not len(data) > 1: return "0"+data
        else: return data
    def addrToCity(addr:str) -> str:
        return addr.replace(",","\n").split("\n")[-1][:-7].strip()

class Generator:
    def __init__(self) -> None:
        self.randomEmailDomain:list = ['gmail.com', 'yahoo.com', 'outlook.com', 'rediffmail.com', 'protonmail.com']
        self.randomState:list = ['West Bengal', 'Karnataka', 'Maharashtra', 'Bihar', 'Jharkhand', 'Odisha', 'kerala', 'Tamilnadu']
        self.randomMobileNoHead:list = [995, 700, 881, 914, 955, 963, 986]
        self.name:str = fake.name()
        self.username:str = "_".join(self.name.lower().split(" "))
        self.email:str = self.username+str(randint(1000,9999))+"@"+choice(self.randomEmailDomain)
        self.phone:str = str(choice(self.randomMobileNoHead))+str(randint(1111111, 9999999))
        self.countryCode:str = "IN"
        self.timeZone:str = "Asia/Kolkata"
        self.affiliate:str = choice(['Asia', 'India', 'test'])
        self.learnerGroups:str = choice(['sales', 'operations', 'support', 'finance', 'hr'])
        self.dob:str = '"{}"'.format(str(randint(1990,2000))+"-"+Utils.lenSolver(str(randint(1,12)))+"-"+Utils.lenSolver(str(randint(1,28))))
        self.permanentAddress:str = fake.address()
        self.localAddress:str = fake.address()
        self.pinCode:str = self.permanentAddress[-6:]
        self.city:str = Utils.addrToCity(self.permanentAddress)
        self.state:str = choice(self.randomState)
        self.shareInstructor:str = 'no'
        self.userType:str = 'staff'
        self.groups = choice(['instructor', 'Content Manager', 'Affiliate Manager'])
        self.Designation = choice(['Engineer', 'Doctor', 'Pilot', 'Priest', 'Thief', 'Robber'])
        self.dateOfJoining =  '"{}"'.format(str(randint(2020,2021))+"-"+Utils.lenSolver(str(randint(1,12)))+"-"+Utils.lenSolver(str(randint(1,28))))
        self.employeeBand = "empb-"+str(randint(10,99))
        self._dataDict:dict = {
            "Name" : self.name,
            "UserName" : self.username,
            "Email" : self.email,
            "Phone" : self.phone,
            "Country Code" : self.countryCode,
            "Timezone" : self.timeZone,
            "Affiliate" : self.affiliate,
            "LearnerGroups" :self.learnerGroups,
            "DateOfBirth" : self.dob,
            "Address1" : self.permanentAddress.replace("\n", " "),
            "Address2" : self.localAddress.replace("\n", " "),
            "City" : self.city,
            "State" : self.state,
            "Pincode" : self.pinCode,
            "Share instructor" : self.shareInstructor,
            "UserType": self.userType,
            "Groups" : self.groups,
            "Designation" : self.Designation,
            "DateOfJoining" : self.dateOfJoining,
            "EmployeeBand" : self.employeeBand,
        }
    def __call__(self, userType:str)-> dict:
        # if userType == 'staff': self._dataDict.update
        fieldList:list = list(fields.keys())
        _dict:dict = dict()
        for items in fieldList:
            if fields.get(items).lower() == 'danger':continue
            if self._dataDict.get(items): _dict.update({items:self._dataDict.get(items)})
            else: _dict.update({items:Utils.input.String("{0} fields has no automated script to generate the value. You must need to put it manually.\nEnter the value of {0} for {1} here: ".format(items, self.name))})
            if not _dict.get(items) and fields.get(items).lower() == "required": 
                Utils.input.String("{0} is the required field. You must need to enter a value for it.\nEnter the value of {0} for {1}here: ".format(items, self.name), True)
        return _dict
        
class Write:
    def toXLSX(data:list) -> None:
        csvFileName:str = "learnerOrstaff.csv"
        xlsxFileName:str = "learnerOrstaff.xlsx"
        fieldnames:list = list(fields.keys())
        for field in fieldnames:
            if fields.get(field).lower() == "danger": fieldnames.remove(field)
        with open(csvFileName, 'w') as f:
            writer:DictWriter = DictWriter(f, fieldnames=list(data[0].keys()))
            writer.writeheader()
            for _dict in data:
                writer.writerow(_dict)
        read_csv(csvFileName).to_excel(xlsxFileName, index=None, header=True)
        # remove(csvFileName)
        return None

def main():
    count:int = Utils.input.Integer("How many tables do you want: ")
    if not count: 
        print("No value provided. Seted to 2.")
        count:int = 2
    dataL:list = list()
    for _ in range(0,count):
        generator:Generator = Generator()
        _dict:dict = generator(type)
        dataL.append(_dict)
    Write.toXLSX(dataL)
    print ('Done')

if __name__ == "__main__":   
    main()        