import logging

def test():
    print('~' * 20)
    level = logging.getLevelName(logging.getLogger().getEffectiveLevel())
    print(level)
    logging.debug('debug message here..')
    logging.info('info message here..')
    logging.warning('warning message here..')
    logging.error('Error message here..')
    logging.critical('Critical message here..')
    print('~' * 20)

test()

rootlog = logging.getLogger()
print(f'Level : {logging.getLevelName(rootlog.getEffectiveLevel())}')

rootlog.setLevel(logging.DEBUG)
test()

#rootlog.setLevel(logging.CRITICAL)
#test()

#Log to file
handler = logging.FileHandler('test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
rootlog.addHandler(handler)
rootlog.setLevel(logging.DEBUG)
rootlog.debug('debug message here..')
rootlog.info('info message here..')
rootlog.warning('warning message here..')
rootlog.error('Error message here..')
rootlog.critical('Critical message here..')
