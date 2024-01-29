import logging
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

if 1:
    import sys
    sys.path.insert(1, 'src')

from litehtmlpy import litehtmlpy
#litehtmlpy.debuglog(1)
