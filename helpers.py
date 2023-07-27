from settings import MAX_GWEI
from data.data import DATA

import time, json, requests
from loguru import logger
from web3 import Web3



list_send = []


def get_base_gas():
    try:

        web3 = Web3(Web3.HTTPProvider(DATA['ethereum']['rpc']))
        gas_price = web3.eth.gas_price
        gwei_gas_price = web3.from_wei(gas_price, 'gwei')

        return gwei_gas_price

    except Exception as error:
        logger.error(error)
        return get_base_gas()

def wait_gas():

    logger.info(f'check gas')
    while True:

        current_gas = get_base_gas()

        if current_gas > MAX_GWEI:
            logger.info(f'current_gas : {current_gas} > {MAX_GWEI}')
            time.sleep(30)
        else: break