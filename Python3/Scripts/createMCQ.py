from xlsxwriter import Workbook
from random import choice, randint
from requests import get
from bs4 import BeautifulSoup 

class Generate:
    def data(website) -> list:
        _ansDict:dict = {"A":0, "B":1, "C":2, "D":3}
        data = get(website).content
        soup = BeautifulSoup(data, 'html5lib')
        questions:list=soup.findAll("span", attrs = {'class':'ques'})
        questionsL:list = list()
        optionsL:list = list()
        answersL:list = list()
        for question in questions:
            questionsL.append(question.text.replace("\xa0", "").replace("\n",""))
        options:list = soup.findAll("p", attrs = {'class':'options'})
        for option in options:
            optionsL.append([i[3:] for i in option.text.split("\n") if i])
        answers:list = soup.findAll("div", attrs={'class':"showanswer"})
        for answer in answers:
            answersL.append(_ansDict.get(answer.text.split("Explanation")[0].split(":")[1].strip()))

        res:list = list()
        for i in range(len(questionsL)):
            _list:list = [questionsL[i], optionsL[i][0], optionsL[i][1], optionsL[i][2], optionsL[i][3]]
            _list = ["*"+j if j==optionsL[i][answersL[i]] else j for j in _list]
            _list.append(choice(['Easy', 'Moderate', 'Difficult']))
            _list.append(str(randint(1,5)))
            _list.append("")
            _list.append("")
            _list.append("")
            _list.append("")
            _list.append("")
            res.append(_list)    
        return res

class Write:
    def toXLSX(data:list):
        workbook = Workbook('output/mcq_1.xlsx')
        worksheet = workbook.add_worksheet()
        row = col= 0
        for item in data:
            for i in range(len(item)):
                worksheet.write(row, col+i, item[i])
            row += 1
        workbook.close()
        return "Done"


def main() -> None:
    websites:list = ["https://letsfindcourse.com/cloud-computing/aws-mcq-questions-and-answers", "https://letsfindcourse.com/cloud-computing/amazon-web-services-mcq-questions-and-answers"]
    dataL:list = [["question", "option", "option", "option", "option", "difficulty", "score","label", "label", "hint", "correct_answer_feedback", "incorrect_answer_feedback"],]
    for website in websites:
        dataL += Generate.data(website)
    print(Write.toXLSX(dataL))

if __name__ == "__main__":
    main()
    