# -*- coding: UTF-8 -*-

# 001

operations.skip_to_home(browser)
operations.skip_to_setting_page(browser, path=[u'系统设置', u'计费设置'])

cmd = " select IntValue from branchstore_setupparam " + \
      " where branchstore_no = " + login_info['branchstore_no'] + \
      " and param_name = " + "'bk'"

# 每办一张会员卡需交开卡费
expected_result = {
    'case_no': 0001,
    'setup_key': 'bk',
    'setup_value': random_int(1, 100),
    'pre_setup_value': db.query(cmd)[0][0],
    'left_desc': u'每办一张会员卡需交卡费：',
    'right_desc': u'元',
}
widget = MyWidget(browser, **expected_result)
actual_result = {
    'pre_setup_value': widget.setup_value,
}
widget.set(expected_result['setup_value'])
operations.save_settings(browser)


# 收集结果
def collect_result_info(widget, db):
    actual_result = {
        'setup_value': db.query(cmd)[0][0],
        'left_desc': widget.left_desc,
        'right_desc': widget.right_desc,
    }
    return actual_result

from time import sleep

sleep(1) # 等待数据写入数据库
actual_result.update(collect_result_info(widget, db))

# 检查结果
print expected_result
print actual_result
from my_result_processor import check_result

check_result(expected_result, actual_result)

# 002



