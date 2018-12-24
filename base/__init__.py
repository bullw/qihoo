"""
1 搜索
"""
from selenium.webdriver.common.by import By

set_search = By.ID, "com.android.settings:id/search"  # 搜索按钮
set_text = By.ID, "android:id/search_src_text"  # 输入框定位
set_back = By.CLASS_NAME, "android.widget.ImageButton"