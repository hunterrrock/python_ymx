"""
logging：python自带的日志模块

日志 --》日志收集器--》输出渠道--》控制台或日志文件
日志收集器：设置收集日志的等级，可以控制收集的等级
    自带的日志收集器：root
    收集等级
    1.logging.getlogger:创建日志收集器
    创建日志收集器的时候不穿name参数，返回的是默认的收集器（root)
    传了name参数会创建一个新的日志收集器
    2.设置日志收集等级
    log.setLevel('DEBUG')
日志输出渠道：设置输出的日志等级，控制输出的等级
    1.创建一个日志输出渠道
        #输出到控制台：
        logging.StreamHandler()
        #输出到日志文件
        fh = logging.FileHandler(filename,encoding='utf-8')

    2.设置输出等级
        sh.setLevel('DEBUG')
    3.将输出渠道绑定到日志收集器上
        log.addHandler(sh)
日志输出格式：
logging.Formatter()
"""
import logging

#1.创建日志收集器
# 当getLogger方法不传入参数，默认返回root(默认的日志收集器）root的默认输出等级是WARNING
log = logging.getLogger('YAN')
#1.1设置日志收集器收集日志的等级
log.setLevel('DEBUG')

#2.设置输出日志的等级
#创建一个日志输出渠道
#2.1输出到控制台：
sh = logging.StreamHandler()
#2.2输出到日志文件：
fh = logging.FileHandler('yan.log', encoding='utf-8')
# 3.设置输出等级
sh.setLevel('DEBUG')
sh.setLevel('DEBUG')
# 4.将输出渠道绑定到日志收集器上
log.addHandler(sh)
log.addHandler(fh)

# 5.设置日志输出的格式
log_format = logging.Formatter('%(asctime)s-[%(filename)s-->LINE:%(lineno)d]-%(levelno)s:%(message)s')
# 6.将日志格式绑定到输出渠道
fh.setFormatter(log_format)


log.debug('------------debug--------------')
log.info('------------info--------------')
log.warning('------------warning--------------')
log.error('------------error--------------')
log.critical('------------critical--------------')

