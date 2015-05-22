from utils.log import logger
import utils.loginit

from module import moge

@logger
def hoge():
    print("main_hoge!!")

if __name__ == '__main__':
    hoge()
    instance_m = moge.moge()
    instance_m.toge(1)

