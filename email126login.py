# coding=utf-8
'''
Created on 2016-7-20
@author: Jennifer
Project:简单元素操作登录126邮箱，元素的clear()，send_keys(),click()操作
在定位的时候发现有些元素定位不到，最后发现有iframe，frame中实际上是嵌入了另一个页面。
如果iframe有name或id的话，直接使用switch_to_frame("name值")或switch_to_frame("id值")，
这是最理想的方法，也是最简单好用的方法。
'''
from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get(r'http://www.126.com/')  #字符串加r，防止转义。
time.sleep(3)

print '开始登录邮箱'

try:
    assert '126' in driver.title    #title是变量，不能title()
except AssertionError:
    print "error：网址输入不正确"
else:
    print "记录日志：网址输入正确"

#    driver.switch_to_frame('x-URS-iframe')  #跳转到iframe框架
    driver.switch_to.frame('x-URS-iframe')   #同上面语句一样，跳转到iframe框架
    username=driver.find_element_by_name('email')
    username.clear()
    username.send_keys('用户名')
    time.sleep(0.1)
    
    userpasswd=driver.find_element_by_name('password')
    userpasswd.clear()
    userpasswd.send_keys('密码')
    time.sleep(0.1)
    
    loginbt=driver.find_element_by_id('dologin')
    loginbt.click()
    time.sleep(3)
    
    try:
        assert '网易邮箱' in driver.title
    except AssertionError:
        print '邮箱登录失败'
    else:
        print '邮箱登录成功'
    
finally:
    #操作：收信，暂不写例子了
    driver.quit()
    
print '测试结束'

