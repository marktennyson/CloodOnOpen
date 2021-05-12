from faker import Faker
from csv import DictWriter
from random import choice, randint
from pandas import read_csv
from os import remove

fields = {
        "Course Name": "required",
        "Category Code" : "required",
        "Sub Category Code" : "no-value",
        "Course Code" : "required",
        "Description" : "required",
        "Duration(days)" : "required",
        "Image Link" : "no-value",
        "Format" : "danger",
        "Objective" : "danger",
        "Prerequisites" : "danger",
        "Learning Outcomes" : "danger",
        "Class Size" : "danger",
        "Author" : "no-value",
        "Topics/Subtopics" : "no-value",
        "Delivery Mode" : "required",
}

faker:Faker = Faker()

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
            return inp 

class Generator:
    def __init__(self):
        self.courseName = choice(['python', 'C', 'Node', 'Rust', 'Golang', 'Julia', 'Erlang'])+"-"+str(randint(10,1000))
        self.catagoryCode = choice(['c1378225', 'c178380', 'c235536', 'c2550147', 'c3116925', 'c3621971'])
        self.subCatagoryCode = " "
        self.courseCode = self.courseName.lower()+str(randint(1,999))
        self.description = faker.sentence()
        self.duration = choice(['90', '60', '45', '75', '120', '30', '80'])
        self.imageLink = "https://fakeimg.pl/200x100/?retina=1&text={}&font=noto".format(self.courseName)
        self.format = choice(['frmt1', 'frmt2', 'frmt3', 'frmt4', 'frmt5', 'frmt6', 'frmt7', 'frmt8'])
        self.Objective = None
        self.Prerequisites = None
        self.learningOutcome = None
        self.classSize = str(randint(100,1000))
        self.Author = choice(['Aniket Sarkar', 'Mark Tennyson', 'Gargi Modak'])
        self.deliveryMode = choice(['Self-Study'])
        self.topicsAndsubtopics = self.courseName+"-top-1[subtopic-1, subtopic-2]"+","+self.courseName+"-top-2[subtopic-3, subtopic-4]"
        self._dataDict:dict = {
            "Course Name": self.courseName,
            "Category Code" : self.catagoryCode,
            "Sub Category Code" : self.subCatagoryCode,
            "Course Code" : self.courseCode,
            "Description" : self.description,
            "Duration(days)" : self.duration,
            "Image Link" : self.imageLink,
            "Format" : self.format,
            "Objective" : self.Objective,
            "Prerequisites" : self.Prerequisites,
            "Learning Outcomes" : self.learningOutcome,
            "Class Size" : self.classSize,
            "Topics/Subtopics" : self.topicsAndsubtopics,
            "Delivery Mode" : self.deliveryMode,
            "Author" : self.Author,
        }

    def __call__(self)-> dict:
        fieldList:list = list(fields.keys())
        _dict:dict = dict()
        for items in fieldList:
            if fields.get(items).lower() == 'danger': continue
            if self._dataDict.get(items): _dict.update({items:self._dataDict.get(items)})
            else: _dict.update({items:Utils.input.String("{0} fields has no automated script to generate the value. You must need to put it manually.\nEnter the value of {0} for {1} here: ".format(items, self.courseName))})
            if not _dict.get(items) and fields.get(items).lower() == "required": Utils.input.String("{0} is the required field. You must need to enter a value for it.\nEnter the value of {0} for {1}here: ".format(items, self.courseName), True)
            if fields.get(items).lower() == "no-value": _dict.update({items:""})
        return _dict
        
class Write:
    def toXLSX(data:list) -> None:
        csvFileName:str = "course.csv"
        xlsxFileName:str = "course.xlsx"
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
        _dict:dict = generator()
        dataL.append(_dict)
    Write.toXLSX(dataL)
    print ('Done')

if __name__ == "__main__":   
    main() 