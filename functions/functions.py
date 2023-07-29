from web3 import Web3, contract
from abi import contract_abi
import random
import time
from settings import *
import decimal as dc
from helpers import wait_gas # !RM

web3 = Web3(Web3.HTTPProvider(RPC))
contract_address = web3.to_checksum_address(contract_address)
contract = web3.eth.contract(contract_address, abi=contract_abi)



def random_sleep():
    sleep_duration = random.randint(from_sec, to_sec)
    print(f"Sleeping for {sleep_duration} seconds")
    time.sleep(sleep_duration)

def deposit(min_val, max_val, pvt_key):
	random_sleep()

	if CHECK_GWEI == True:  # !RM
		wait_gas()  # !RM смотрим газ, если выше MAX_GWEI, ждем #!RM

	web3 = Web3(Web3.HTTPProvider(RPC))
	address = web3.eth.account.from_key(pvt_key).address
	value_eth = "{:.8f}".format(random.uniform(min_val, max_val))
	value_wei = web3.to_wei(value_eth, 'ether')

	transaction = contract.functions.deposit().build_transaction({
		'from': web3.to_checksum_address(address),
		'value': value_wei,
		'gasPrice': web3.to_wei(0.25, 'gwei'),
		'nonce': web3.eth.get_transaction_count(web3.to_checksum_address(address))
	})
	transaction['gas'] = int(web3.eth.estimate_gas(transaction))
	signed_txn = web3.eth.account.sign_transaction(transaction, pvt_key)
	transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()

	return print(f"{address} | Deposited {value_eth} ETH | Hash: {transaction_hash}")

def deposit_swap(keep_value_from,keep_value_to,pvt_key):
	random_sleep()

	if CHECK_GWEI == True:  # !RM
		wait_gas()  # !RM смотрим газ, если выше MAX_GWEI, ждем #!RM

	web3 = Web3(Web3.HTTPProvider(RPC))
	address = web3.eth.account.from_key(pvt_key).address
	balance = check_balance_wallet(pvt_key)
	keep_value = round(random.uniform(keep_value_from, keep_value_to), 7) #RM
	value_eth = "{:.8f}".format(balance - dc.Decimal(keep_value))
	value_wei = web3.to_wei(value_eth, 'ether')

	transaction = contract.functions.deposit().build_transaction({
		'from': web3.to_checksum_address(address),
		'value': value_wei,
		'gasPrice': web3.to_wei(0.25, 'gwei'),
		'nonce': web3.eth.get_transaction_count(web3.to_checksum_address(address))
	})
	transaction['gas'] = int(web3.eth.estimate_gas(transaction))
	signed_txn = web3.eth.account.sign_transaction(transaction, pvt_key)
	transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()

	return print(f"{address} | Deposited {value_eth} ETH | Hash: {transaction_hash}")


def withdraw(pvt_key):
	random_sleep()

	if CHECK_GWEI == True:  # !RM
		wait_gas()  # !RM смотрим газ, если выше MAX_GWEI, ждем #!RM

	web3 = Web3(Web3.HTTPProvider(RPC))
	address = web3.eth.account.from_key(pvt_key).address
	contract = web3.eth.contract(contract_address, abi=contract_abi)
	balance = contract.functions.getBalance().call({'from': address})

	transaction = contract.functions.withdraw(balance).build_transaction({
		'from': web3.to_checksum_address(address),
		'value': 0,
		'gasPrice': web3.to_wei(0.25, 'gwei'),
		'nonce': web3.eth.get_transaction_count(web3.to_checksum_address(address))
	})
	transaction['gas'] = int(web3.eth.estimate_gas(transaction))
	signed_txn = web3.eth.account.sign_transaction(transaction, pvt_key)
	transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()

	return print(f"{address} | Withdrawed {web3.from_wei(balance, 'ether')} ETH | Hash: {transaction_hash} ")


def withdraw_swap(keep_value_from, keep_value_to, pvt_key):
	random_sleep()

	if CHECK_GWEI == True:  # !RM
		wait_gas()  # !RM смотрим газ, если выше MAX_GWEI, ждем #!RM

	web3 = Web3(Web3.HTTPProvider(RPC))
	contract_balance = web3.from_wei(check_balance(pvt_key), "ether")
	address = web3.eth.account.from_key(pvt_key).address
	keep_value = random.uniform(keep_value_from,keep_value_to)
	value_to_withdraw = contract_balance - dc.Decimal(keep_value) # balance minus value
	balance = web3.to_wei(value_to_withdraw, 'ether')

	transaction = contract.functions.withdraw(balance).build_transaction({
		'from': address,
		'value': 0,
		'gasPrice': web3.to_wei(0.25, 'gwei'),
		'nonce': web3.eth.get_transaction_count(address)
	})
	transaction['gas'] = int(web3.eth.estimate_gas(transaction))
	signed_txn = web3.eth.account.sign_transaction(transaction, pvt_key)
	transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()

	return print(f"{address} | Withdrawed {web3.from_wei(balance, 'ether')} ETH | Hash: {transaction_hash} ")


def check_balance(pvt_key): # Contract balance
	web3 = Web3(Web3.HTTPProvider(RPC))
	contract = web3.eth.contract(contract_address, abi=contract_abi)
	address = web3.eth.account.from_key(pvt_key).address
	balance = contract.functions.getBalance().call({'from': address})
	print(f"""{address} | Balance on contract {web3.from_wei(balance, 'ether')}""")
	return balance


def check_balance_wallet(pvt_key): # ZkEra balance
	# we are using here pvt key and afterwards the function to get wallet for getting balance of native (eth)
	web3 = Web3(Web3.HTTPProvider(RPC))
	address = web3.eth.account.from_key(pvt_key).address
	return web3.from_wei(web3.eth.get_balance(address),"ether")

