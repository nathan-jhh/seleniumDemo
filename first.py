import time
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys

def sleep(sec):
    time.sleep(sec)

user_name = ['张三','张四','陈一','张王八','李五']

driver = webdriver.Firefox()
driver.get(url)
elem1 = driver.find_element_by_id("username")
elem1.send_keys(username)
elem2 = driver.find_element_by_id("password")
elem2.send_keys(password)
elem3 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/input[4]")
elem3.click() #登录

sleep(2)
#信息管理
elem4 = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/span[5]/a")
elem4.click()

sleep(2)
#添加效益（物流试验系统）
elem5 = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/table/tbody/tr[2]/td[8]/a[5]")
elem5.click()

sleep(2)
#使用机时
elem6 = driver.find_element_by_id("machineUseInfo")
elem6.click()

sleep(2)
i = 5
j = 0
k = 2
am_start_time = datetime.strptime('2017-10-18 09:00:00', '%Y-%m-%d %H:%M:%S')
am_end_time = datetime.strptime('2017-10-18 11:00:00', '%Y-%m-%d %H:%M:%S')
pm_start_time = datetime.strptime('2017-10-18 15:00:00', '%Y-%m-%d %H:%M:%S')
pm_end_time = datetime.strptime('2017-10-18 17:00:00', '%Y-%m-%d %H:%M:%S')

while i > 0:

    #添加使用机时
    elem7 = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/span[1]/input")
    elem7.click()

    sleep(2)

    js1 = "$('input[id=dateOfBegin]').attr('readonly',false)"  # jQuery，设置为false
    js2 = "$('input[id=dateOfEnd]').attr('readonly',false)"  # jQuery，设置为false
    driver.execute_script(js1)  #调用js方法
    driver.execute_script(js2)
    if k % 2 == 0:
        driver.find_element_by_id('dateOfBegin').send_keys(am_start_time.strftime('%Y-%m-%d %H:%M:%S'))
        driver.find_element_by_id('dateOfEnd').send_keys(am_end_time.strftime('%Y-%m-%d %H:%M:%S'))

    if k % 2 != 0:
        driver.find_element_by_id('dateOfBegin').send_keys(pm_start_time.strftime('%Y-%m-%d %H:%M:%S'))
        driver.find_element_by_id('dateOfEnd').send_keys(pm_end_time.strftime('%Y-%m-%d %H:%M:%S'))

        am_start_time += timedelta(days=1)
        am_end_time += timedelta(days=1)
        pm_start_time += timedelta(days=1)
        pm_end_time += timedelta(days=1)

    k += 1

    driver.find_element_by_name("entity.user").send_keys(user_name[j])
    if j == 4:
        j = -1
    j += 1

    #提交
    elem8 = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/form/table/tfoot/tr/th/input")
    elem8.click()

    #延时
    sleep(4)

    #返回
    elem9 = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/table/tfoot/tr/th/input")
    elem9.click()

    sleep(4)

    i -= 1

#driver.close()