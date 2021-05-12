from random import choice, randint
from xlsxwriter import Workbook
from faker import Faker

faker:Faker = Faker()

fields = {
        "Category Name" : "required",
        "Category Code" : "required",
        "Description" : "required",
        "Subcategories" : "non-required",
        "Image Link" : "required",
}

class Generate:
    def __init__(self):
        self.catagoryName = choice(['catcol1', 'catcol2', 'catcol3', 'catcol4', 'catcol5'])
        self.catagoryCode = self.catagoryName[0]+str(randint(111111,9999999))
        self.Description = "description"+str(randint(99999,8745667786))
        self.subCatagory = str()
        # self.imageLink = "https://fakeimg.pl/200x100/?retina=1&text={}&font=noto".format(self.catagoryName)
        self.imageLink = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png"
    def __call__(self) -> list:
        _listData:list = [self.catagoryName, self.catagoryCode, self.Description, self.subCatagory, self.imageLink]
        return _listData

class Write:
    def toXLSX(DataL:list):
        workbook = Workbook('output/cat01.xlsx')
        worksheet = workbook.add_worksheet()
        row = 0
        col = 0
        for item in DataL:
            
            worksheet.write(row, col, item[0])
            worksheet.write(row, col+1, item[1])
            worksheet.write(row, col+2, item[2])
            worksheet.write(row, col+3, item[3])
            worksheet.write(row, col+4, item[4])
            row += 1
        workbook.close()

def main():
    count = input("How many tables do you want :")
    if not count : count = 2
    _data:list = [list(fields.keys())]
    for _ in range(int(count)):
        generate = Generate()
        _data.append(generate())
    Write.toXLSX(_data)
    print ("Done")

if __name__ == "__main__":
    main()