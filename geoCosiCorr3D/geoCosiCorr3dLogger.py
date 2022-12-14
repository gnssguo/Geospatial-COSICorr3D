"""
# Author : Saif Aati
# Contact: SAIF AATI  <saif@caltech.edu> <saifaati@gmail.com>
# Copyright (C) 2022
"""
import logging
import os, sys
from geoCosiCorr3D.geoCore.constants import SOFTWARE
from datetime import datetime



class geoCosiCorr3DLog:
    def __init__(self, log_prefix: str, log_dir:str= None):
        if log_dir is None:
            log_dir  = SOFTWARE.LOGDIR
        # GENERATION_TIME = Time(Time.now(), format='isot', scale='utc')
        now = datetime.now()
        GENERATION_TIME = now.strftime("%m-%d-%Y-%H-%M-%S")
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler(os.path.join(log_dir, log_prefix + "_" + GENERATION_TIME + '.log')),
                logging.StreamHandler(sys.stdout)
            ]
        )
