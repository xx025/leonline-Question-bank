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
    for i in load_dict["questionBank"]:
        if i["questionType"] == "单项选择题":
            danxiangxuanze.append(i["question"])
        elif i["questionType"] == "是非题":
            shifei.append(i["question"])
        elif i["questionType"] == "多项选择题":
            duoxianxuanze.append(i["question"])
        else:
            print(i["questionType"])
            print(i["question"])

# print(duoxianxuanze)
# print(danxiangxuanze)
# print(shifei)

from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')  # chrome插件路径
driver.maximize_window()

driver.implicitly_wait(10)


def login(id, password):
    userinput = driver.find_element_by_css_selector(".user_name input")
    userinput.click()
    userinput.send_keys(id)

    passinput = driver.find_element_by_css_selector(".user_pass input")
    passinput.click()
    passinput.send_keys(password)

    loginBtn = driver.find_element_by_css_selector(".user_btn a")
    loginBtn.click()


driver.get("https://study.leonline.cn/login.html")  # 榜单地址

id = input("输入手机号")  # 你的账号：xxxx
passWord = '123456'  # 你的密码：XXXx15266938297
login(id, passWord)  # 登录
sleep(3)
driver.find_elements_by_css_selector(".nav_box a")[3].click()
sleep(3)
# driver.close()
driver.find_element_by_css_selector(".btn_begin").click()
sleep(3)
driver.find_elements_by_css_selector('.browser_btn')[1].click()

sleep(3)
driver.find_element_by_css_selector('#snap').click()

sleep(3)
driver.find_element_by_css_selector(".theImgsBottom span").click()



driver.find_element_by_css_selector("test_type")

