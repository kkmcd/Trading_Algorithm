
# coding: utf-8

# In[3]:


def cal_upper(price):
    increment = price * 0.3
    upper_price = price+increment
    return upper_price

def cal_lower(price):
    decrement = price * 0.3
    lower_price = price - decrement
    return lower_price

author = "pyStock"

def run():
    print(cal_upper(100000))
    print(cal_lower(10000))
    print(__name__)

#Module이 제대로 동작하는지 확인하기 위해서 testcode를 실행시킴
#python Stock을 통해서 실행시키면 run이 실행안됨. but python 시키고 import Stock하면 아래의 run이 실행됨
if __name__ == '__main__':
    run()

