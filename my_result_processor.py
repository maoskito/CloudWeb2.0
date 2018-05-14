# -*- coding: UTF-8 -*-

import my_log

def check_result( expected_result, actual_result):
    for key in actual_result:
        actual_value = actual_result[key]
        expected_value = expected_result[key]

        if isinstance(actual_value, (int, long, float)):
            actual_value = str(actual_value)
        if isinstance(expected_value, (int, long, float)):
            expected_value = str(expected_value)

        if not actual_value == expected_value:
            my_log.case_logger.info('case{case_no} failed !'.format(case_no=expected_result['case_no']))
            print type(actual_value), type(expected_value)







