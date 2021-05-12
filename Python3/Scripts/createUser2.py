from xlsxwriter import Workbook
from random import choice, randint
from faker import Faker

fake:Faker = Faker('en_IN')


fields = {
    "EmpId":"danger",
    "Name" : "required",
    "UserName" : "required",
    "Email" : "required",
    "Phone" : "required",
    "Country Code" : "required",
    "Timezone" : "required",
    "Affiliate" : "optional",
    "Share instructor" : "optional",
    "LearnerGroups" : "danger",
    "DateOfBirth" : "required",
    "UserType" : "required",
    "Groups" : "required",
    "Address1" : "required",
    "Address2" : "required",
    "City" : "required",
    "State" : "required",
    "Pincode" : "required",
    "check" : "optional",
    "Designation" : "optional",
    "DateOfJoining" : "danger",
    "EmployeeBand" : "danger",
    "employeeType" : "optional"
}

class Utils:
    class input:
        def Integer(msg:str=str()) -> int:
            try: return int(input(msg).strip())
            except: return False
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

class Generate:
    def __init__(self):
        self.fieldname:list = [field for field in list(fields.keys()) if not fields[field] == 'danger']
        self.randomState:list = ['West Bengal', 'Karnataka', 'Maharashtra', 'Bihar', 'Jharkhand', 'Odisha', 'kerala', 'Tamilnadu']
        self.randomMobileNoHead:list = [995, 700, 881, 914, 955, 963, 986]
        self.employeeId = f"ncempid<{randint(999,9999)}>"
        self.name:str = fake.name()
        self.username:str = "_".join(self.name.lower().split(" "))
        self.email = choice(['aniketsarkarkorea@gmail.com', 'marktennyson1@yahoo.com', 'gargimodak08@gmail.com', 'aniketsarkar1998@yahoo.com', 'sarkar.raja123@gmail.com'])
        self.phone:str = str(choice(self.randomMobileNoHead))+str(randint(1111111, 9999999))
        self.countryCode:str = "IN"
        self.timeZone:str = "Asia/Kolkata"
        self.affiliate:str = choice(['mars', 'pluto'])
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
        # self._dataList:list = [self.name, self.username, self.email, self.phone, self.countryCode, self.timeZone, self.l]
        self._dataDict:dict = {
            "EmpId" : self.employeeId,
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
    def __call__(self)-> list:
        self._dataList:list = list()
        for field in self.fieldname:
            if fields[field] == "required": self._dataList.append(self._dataDict[field])
            elif fields[field] == "optional": self._dataList.append("")
        return self._dataList

class Write:
    @staticmethod
    def toXLSX(data:list):
        workbook = Workbook('output/useracc_2.xlsx')
        worksheet = workbook.add_worksheet()
        row = col= 0
        for item in data:
            for i in range(len(item)):
                worksheet.write(row, col+i, item[i])
            row += 1
        workbook.close()
        return "Done"

def main() -> None:
    count:int = Utils.input.Integer("How many tables do you want: ")
    if not count: 
        print("No value provided. Seted to 2.")
        count:int = 2
    dataL:list = [[field for field in list(fields.keys()) if not fields[field] == 'danger'],]
    for _ in range(0,count):
        generator:Generate = Generate()
        _list:list = generator()
        dataL.append(_list)
    Write.toXLSX(dataL)
    print ('Done')
    

if __name__ == "__main__": main()