# 配置数据  爱克登录
from selenium.webdriver.common.by import By

loc_username = By.ID, "com.vcooline.aike:id/etxt_username"
loc_password = By.ID, "com.vcooline.aike:id/etxt_pwd"
loc_click = By.ID, "com.vcooline.aike:id/btn_login"

# 配置数据    搜索
local_sous = By.ID, "com.android.settings:id/search"
local_box = By.ID, "android:id/search_src_text"
local_back = By.CLASS_NAME, "android.widget.ImageButton"
