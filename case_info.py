from selenium.webdriver.common.by import By

# 计费设置
billing_setupInfo = {
    'key':{
        'description':u'功能描述',
        'locator': (By.ID, 'id'),
        'value': 1,
    },
    'bk':{
        'description':u'每办一张会员卡需交开卡费',
        'locator': (By.ID, 'bk'),

    },
}

# 功能设置
funciton_setupInfo = {
    'billingMolde_centralized':{
        'description':u'计费模式-集中式',
        'locator': (By.ID, 'id'),
        'action':'click'
    },
    'billingMolde_distributed_with_password':{
        'description':u'计费模式-分布式()',
        'locator': (By.XPATH, '有密码')
        'action':'click'
    },
    'billingMolde_distributed_without_password':{
        'description': u'计费模式-分布式',
        'locator': (By.XPATH, '无密码')
        'action': 'click'
    },
}


billing_setupInfo = {
    # 计费设置
    'setup_bk': u'每办一张会员卡需交开卡费：', # unsigned_int, 2
    'setup_bkf': u'每补办一张会员卡需交补卡费：', # unsigned_int, 2
    'setup_yj': u'每开一张普通卡需交押金：', # unsigned_int, 2
    'setup_ptk_kkf': u'每办一张普通卡需交开卡费：', # unsigned_int, 2
    'setup_DefMoney': u'开卡费默认值：', # unsigned_int, 2
    'setup_GPSW': u'开卡默认密码：', # string, 8
    'setup_MinAddMny': u'会员,充值最低金额：', # unsigned_int, 5
    'setup_MinAddMny2': u'普通卡，充值最低金额：', # unsigned_int, 5
    'setup_MaxAddMny': u'会员，充值最高金额：', # unsigned_int, 5
    'setup_MaxAddMny2': u'普通卡：', # unsigned_int, 5
    'setup_OpenMemMin': u'办理会员必须充值：', # unsigned_int, 5
    'setup_OpenMemJL': u'会员开卡赠送奖励：', # unsigned_int, 5
    'setup_TiXing': u'客户端即将到时提醒：', # unsigned_int, 3
    'setup_CSJF': u'超过按一小时计算', # unsigned_int, [1,59]
    'setup_MemFreeUse': u'会员上机时间不足限时不计费', 'setup_MemFreeUse_val': u'限时设置', # unsigned_int, [2,10]
    'setup_Less2m': u'非会员上机时间不足限时不计费', 'setup_FreeMin': u'限时设置', # unsigned_int, [2,10]
    'setup_AutoCheckOut': u'客户端失去联系后自动结账', 'setup_AutoCheckOut_val': u'结账时间', # unsigned_int, 3
    'setup_AutoCheck': u'客户端失去联系后开始提示', 'setup_AutoCheck_val': u'提示时间', # unsigned_int, 3
    'setup_UseRandomPsw': u'开卡使用随机密码',
    'setup_FirstNotHandsel': u'会员第一次开卡时不按奖励设置赠送',
    'setup_LskFxf': u'允许免收预交款上机',
    # 功能设置
    '//*[@id="setupForm"]/div/div/div[1]/div[1]/div[2]/div[3]/label/div/input': u'计费模式',
    '//*[@id="setupForm"]/div/div/div[1]/div[2]/div[2]/div[1]/input': u'重启客户端后的处理方式:',
    'setup_TimeCtr': u'系统时间保护',
    'setup_SysTimeChk': u'系统时间监视',
    'setup_bChkTcpConnet': u'打开Tcp/IP协议废弃连接智能回收机制',
    'setup_CheckOutActive': u'会员上机结账后必须激活才能继续使用',
    'setup_ptkisout': u'禁止普通卡在客户端自助结帐',
    'setup_txtk': u'普通卡结账余额为零自动退卡',
    'setup_outs': u'结帐后立即关机',
    'setup_ClientChangComputer': u'禁止非会员客户端换机',
    'setup_MemberChangComputer': u'禁止会员客户端换机',
    'setup_CltAreaChangCom': u'禁止客户端跨区换机',
    'setup_ChangeComConfirm': u'客户端换机前须经客户确认',
    'setup_chkMemcardSFZHts': u'开卡时提示证件号码重复',
    'setup_bAutoFill': u'客户端登陆，卡号自动补足10位',
    'setup_CanCancelActive': u'会员卡激活后可以取消激活',
    'setup_bCltChangeName': u'客户端电脑名出现重名，自动重启',
    'setup_bBrushCrdList': u'刷卡排队',
    'setup_bUnidiedtime': u'统一使用主收银机时间来计算',
    'setup_bUnUseableTime': u'不使用会员有效期标志',
    'setup_UnShowPoint': u'客户端不显示积分',
    'setup_ExitCardFeeTrunc': u'普通卡退卡只退整元(向下取整)',
    # 包时段设置
    'setup_rebaoye': u'返还包时段内已按标准费率扣除的费用',
    'setup_UseAward': u'允许使用奖励金额转包时段',
    'setup_Buffet': u'允许客户端自助开包时段',
    'setup_ReFee': u'包时段内如果结账就重新计费',
    'setup_txjz': u'包时段到时后全部结账',
    'setup_bAutoFeeMode': u'自动包时段垮区换机统一计费方式',
    'setup_ZDBY': u'自动转包时段',
    'setup_AddMonenyTX': u'会员转包时段前必须充值，设置提前充值时间：',
    '//*[@id="setupForm"]/div/div[8]/div[2]/input': u'分钟', # unsigned_int, 3
    # 其它功能设置
    'setup_CardOut': u'拔卡不结账',
    'setup_ReissueMem_CheckSFZH': u'补卡时需效验身份证号是否相同',
    'setup_UseJLFirst': u'计算费率优先扣奖励',
    'setup_PercentNum': u'比例设置：',
    '//*[@id="setupForm"]/div/div/div/div/div[4]/div[2]/label[1]/div/input': u'按收银台',
    '//*[@id="setupForm"]/div/div/div/div/div[4]/div[2]/label[2]/div/input': u'按收银员',
    '//*[@id="setupForm"]/div/div/div/div/div[4]/div[2]/label[3]/div/input': u'按收银台或收银员',
    'setup_CardStockAccountSp': u'交班时，不显示和不统计实名注册卡的销售金额。',
    'setup_WebPayAccountSp': u'龙管家与龙付通数据分离 (在【交班】和【老板查账】中将不体现龙付通数据)',

    # 数据库备份设置
    'setup_BackupPath': u'数据库备份保存路径设置', # string, 200
    'setup_AutoBackUp': u'数据库定时备份',
    'setup_AutoBackUp_val': u'备份间隔时间：', # unsigned_int, 8
    # 收银台白名单

    # 龙付通设置
    'longPayAccount': u'龙付通账号:', # string 30
    'LongPayPws2': u'龙付通登录密码:', # string 20
    '//*[@id="setupForm"]/div/div/div[1]/div/div/div[2]/div[3]/div/button': u'注册账号',
    'LONGPAY_AUTOBOX': u'龙付通按现金账户支付方式,现金账户不足时,自动弹出现金账户充值框。',
    'Account_JL_Mode1': u'奖励不足扣除时,余额不能转账现金账户。',
    '//*[@id="setupForm"]/div/div/div[3]/div/div/div[2]/div[1]/label/div/input': u'启用标准',
    '//*[@id="setupForm"]/div/div/div[3]/div/div/div[2]/div[3]/label/div/input': u'不启用标准',
    # 客户端设置
    'setup_CltShut': u'客户端分钟,无人使用自动关机', # unsigned_int [1,60] setup_CltShut必须小于setup_CltTurn
    'setup_CltTurn': u'客户端分钟,连不上服务端就锁屏', # unsigned_int [1,60] setup_CltTurn必须大于setup_CltShut
    'setup_CltHintTime': u'客户端分钟,提示一次“余额不足”',
    'setup_openfile': u'用户上机即执行指定程序:', # string 50
    'setup_VoiceSet_val': u'客户端音量控制，设置客户端音量为最大音量的:', # unsigned_int [1,100]
    'setup_HideDisk_val': u'隐藏磁盘', # string 50
    # 客户端设置2
    '//*[@id="setup_CltWelcome"]': u'客户端欢迎词' # string, 20, 分号'；'替换为'，'
}