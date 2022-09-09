import logging


def create_log(name='mylog', level='DEBUG', filename='log.log', sh_level='DEBUG', fh_level='DEBUG'):
    # 1、创建日志收集器
    log = logging.getLogger(name)
    # 2、设置日志收集器的等级
    log.setLevel(level)
    # 3、创建输出渠道
    sh = logging.StreamHandler()
    fh = logging.FileHandler(filename, encoding='utf-8')

    # 4、设置输出等级
    sh.setLevel(sh_level)
    fh.setLevel(fh_level)
    # 5、绑定到日志收集器
    log.addHandler(sh)
    log.addHandler(fh)
    # 6、创建日志格式
    log_format = logging.Formatter('%(asctime)s-[%(filename)s-->LINE:%(lineno)d]-%(levelno)s:%(message)s')
    fh.setFormatter(log_format)
    sh.setFormatter(log_format)
    # 返回一个日志收集器
    return log
