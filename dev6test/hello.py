# -*- coding: utf-8 -*-
'''示例测试用例
'''
#2019/03/21 QTAF自动生成

from dev6lib.testcase import Dev6TestCase

class HelloTest(Dev6TestCase):
    '''示例测试用例
    '''
    owner = "root"
    timeout = 5
    priority = Dev6TestCase.EnumPriority.High
    status = Dev6TestCase.EnumStatus.Design
    
    def run_test(self):
        self.log_info("hello testcase")
        self.assert_equal(True, True)
    
if __name__ == '__main__':
    HelloTest().debug_run()

