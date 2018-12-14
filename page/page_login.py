"""
提示：
1.类名
为大驼峰模块名(去掉下划线)
2.每一步操作，为单独的方法
核心：page页面对象要集成Base

"""

import page
from base.base import Base


class PageLogin(Base):

    # 输入用户名
    def page_username(self, usernames):
        self.base_input(page.loc_username, usernames)

    # 输入密码
    def page_pwd(self, pwd):
        self.base_input(page.loc_password, pwd)

    # 点击登录
    def page_click(self):
        self.base_click(page.loc_click)































