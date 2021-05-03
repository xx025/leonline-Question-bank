# 读文件夹文件，获取文件名列表
import json
import os
from time import sleep

u_list = []
for filename in os.listdir("tiku/"):
    u_list.append('{}'.format(filename[:-5]))

danxiangxuanze = []
shifei = []
duoxianxuanze = []
# 读文件
for filename in u_list:
    with open('tiku/{}.json'.format(filename), 'r', encoding='utf8') as f:
        load_dict = json.load(f)
    for k in load_dict["questionBank"]:
        if k["questionType"] == "单项选择题":
            danxiangxuanze.extend(k["question"])
        elif k["questionType"] == "是非题":
            shifei.extend(k["question"])
        elif k["questionType"] == "多项选择题":
            duoxianxuanze.extend(k["question"])
        else:
            print(k["questionType"])
            print(k["question"])
#
# print(duoxianxuanze)
# print(danxiangxuanze)
# print(shifei)

alldi = {"danxuan": danxiangxuanze, "duoxianxuanze": duoxianxuanze, "shifei": shifei}

with open('tiku_a.md', 'w', encoding='utf8') as f:
    for s, j in alldi.items():
        for k in j:
            # print(i)
            questionTitle = k['questionTitle']
            questionSolution = k['questionSolution']
            testQuestionAnswers = k['testQuestionAnswers']
            print(questionTitle, file=f)
            print(str(questionSolution).replace("\r", "").replace("\n", ""), file=f)
            for k in testQuestionAnswers:
                if k['isCorrect'] != '0':
                    # print()
                    print("正确文本：" + k['optionContent'], file=f)
            kk = [i['optionName'] + i["optionContent"] for i in testQuestionAnswers]
            print('\n'.join(kk), file=f)

            print("\n-------------", file=f)
