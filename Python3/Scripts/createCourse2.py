from xlsxwriter import Workbook
from random import choice, randint
from faker import Faker

faker:Faker = Faker('en_IN')

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
        "Author" : "danger",
        "Topics/Subtopics" : "no-value",
        "Delivery Mode" : "required",
}
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
    def __init__(self, count):
        self.fieldname = [field for field in list(fields.keys()) if not fields[field] == 'danger']
        self.courseName = str(count)+"-"+choice(['python', 'C', 'Node', 'Rust', 'Golang', 'Julia', 'Erlang'])+"-"+str(randint(10,1000))
        self.catagoryCode = choice(['c2201703', 'c2950227', 'c4518942', 'c4805786', 'c8221767'])
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

    def __call__(self)-> list:
        self._dataList:list = list()
        for field in self.fieldname:
            if fields[field] == "required": self._dataList.append(self._dataDict[field])
            elif fields[field] == "no-value": self._dataList.append("")
        return self._dataList

class Write:
    def toXLSX(data:list):
        workbook = Workbook('output/course_1.xlsx')
        worksheet = workbook.add_worksheet()
        row = col= 0
        for item in data:
            for i in range(len(item)):
                worksheet.write(row, col+i, item[i])
            row += 1
        workbook.close()
        return "Done"

def main():
    count:int = Utils.input.Integer("How many tables do you want: ")
    if not count: 
        print("No value provided. Seted to 2.")
        count:int = 2
    dataL:list = [[field for field in list(fields.keys()) if not fields[field] == 'danger'],]
    for _ in range(count):
        generator:Generator = Generator(_+1)
        _list:list = generator()
        dataL.append(_list)
    Write.toXLSX(dataL)
    print ('Done')
    
if __name__ == "__main__": main()
