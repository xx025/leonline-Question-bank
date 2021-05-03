from time import sleep

from selenium import webdriver

from selenium import webdriver

option = webdriver.ChromeOptions()

driver = webdriver.Chrome(chrome_options=option)  # 调用带参数的谷歌浏览器

driver.get("https://study.leonline.cn/login.html")  # 榜单地址

# 你的账号：xxxx
# 你的密码：XXXx

id = '11122222222'
passWord = '123456'


def login(id, password):
    userinput = driver.find_element_by_css_selector(".user_name input")
    userinput.click()
    userinput.send_keys(id)

    passinput = driver.find_element_by_css_selector(".user_pass input")
    passinput.click()
    passinput.send_keys(password)

    loginBtn = driver.find_element_by_css_selector(".user_btn a")
    loginBtn.click()


login(id, passWord)

driver.implicitly_wait(10)

sleep(3)

driver.execute_script('document.querySelector(".user_setting").style.display="block"')

driver.find_element_by_css_selector(".user_setting ul a").click()

driver.find_elements_by_css_selector("#accordion li a")[1].click()

testlist = driver.find_elements_by_css_selector(".tree_content ul li a")

lent = testlist.__len__()


def getqq(listq):
    # danxuan = [
    #     {
    #         "qestion": "xxxxx",
    #         "slect": {"A": "",
    #                   "B": "",
    #                   "C": "",
    #                   "C": ""
    #                   },
    #         "tips": "",
    #         "ans": ""
    #     }
    # ]
    danxuan = []
    for i in listq:
        question=i.find_element_by_css_selector('.test_tit em').get_attribute('textContent')
        print(question)
        # slect=i.find_elements_by_css_selector()


for i in range(lent):
    js = 'document.querySelectorAll(".tree_content ul li a")[{}].click()'.format(i)
    sleep(2)
    driver.execute_script(js)
    lli = driver.find_elements_by_css_selector('.test_tit')
    getqq(lli)
    sleep(2)

    driver.execute_script('document.querySelectorAll("#main a")[1].click()')
    break
