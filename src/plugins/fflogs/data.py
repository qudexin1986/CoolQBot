""" 一些数据
"""
boss_list = {
    (1045, 0): ['提坦妮雅歼殛战', '缇坦妮雅', '妖精', '极妖精', '妖灵王', '妖精王', '老婆', '10王'],
    (1046, 0): ['无瑕灵君歼殛战', '无瑕灵君', '肥宅', '极肥宅', '全能王'],
    (1049, 0): ['哈迪斯歼殛战', '哈迪斯', '老公'],
    (65, 100): ['伊甸希望乐园 觉醒之章1', 'E1', 'e1'],
    (66, 100): ['伊甸希望乐园 觉醒之章2', 'E2', 'e2'],
    (67, 100): ['伊甸希望乐园 觉醒之章3', 'E3', 'e3'],
    (68, 100): ['伊甸希望乐园 觉醒之章4', 'E4', 'e4'],
    (65, 0):   ['伊甸零式希望乐园 觉醒之章1', 'E1S', 'e1s', 'E1s', 'e1S'],
    (66, 0):   ['伊甸零式希望乐园 觉醒之章2', 'E2S', 'e2s', 'E2s', 'e2S'],
    (67, 0):   ['伊甸零式希望乐园 觉醒之章3', 'E3S', 'e3s', 'E3s', 'e3S'],
    (68, 0):   ['伊甸零式希望乐园 觉醒之章4', 'E4S', 'e4s', 'E4s', 'e4S'],
} # yapf: disable

job_list = {
    1:  ['占星术士', '占星'],
    2:  ['吟游诗人', '诗人'],
    3:  ['黑魔法师', '黑魔', '伏地魔', '永动机'],
    4:  ['暗黑骑士', '黑骑', '暗骑', 'DK'],
    5:  ['龙骑士', '龙骑', '躺尸龙', '擦炮工'],
    6:  ['机工士', '机工'],
    7:  ['武僧', '扫地僧', '猴子', '和尚'],
    8:  ['忍者', '兔忍', '火影'],
    9:  ['骑士', '圣骑', '奶骑'],
    10: ['学者', '小仙女', '死炎法师'],
    11: ['召唤师', '召唤'],
    12: ['战士', '战爹'],
    13: ['白魔法师', '白魔', '白膜', '投石机'],
    14: ['赤魔法师', '赤魔', '吃馍', '红色治疗'],
    15: ['武士', '侍'],
    16: ['舞者', '舞娘'],
    17: ['绝枪战士', '绝枪', '枪刃', '枪决战士'],
} # yapf: disable


def get_boss_info(name):
    """ 根据昵称获取 boss 的 ID 同时返回正式名称
    """
    for (boss_id, difficulty), nickname in boss_list.items():
        if name in nickname:
            return boss_id, difficulty, nickname[0]
    return None, None, None


def get_job_name(name):
    """ 将中文昵称转换成具体的 ID 同时返回正式名称
    """
    for job_id, nickname in job_list.items():
        if name in nickname:
            return job_id, nickname[0]
    return None, None