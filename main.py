from web3 import Web3
from abi import contract_abi
import random
import time
from settings import *
from functions import *
import decimal as dc


choice = int(input("\n----------------------\n1: deposit\n2: withdraw\n3: check contract balance\n4: check wallet balance\n5: deposit-withdraw loop\nChoice: "))

eth_min = float(eth_min)
eth_max = float(eth_max)
private_keys = []
failed_keys = []
web3 = Web3(Web3.HTTPProvider(RPC))
contract_address = web3.to_checksum_address(contract_address)
contract = web3.eth.contract(contract_address, abi=contract_abi)

def download_wallets():
	with open('keys.txt', 'r') as f:
		for line in f:
			line = line.strip()
			private_keys.append(line)
	return private_keys

def main():

	private_keys = download_wallets()

	if RANDOM_WALLETS == True: random.shuffle(private_keys)

	zero = 0

	if choice == 1: #DEPOSIT
		for key in private_keys:
			try:
				zero += 1
				print(f'{zero}/{len(private_keys)}')

				if swap_all_balance == True:
					deposit_swap(keep_value_from, keep_value_to, key)
				elif swap_all_balance == False:
					deposit(eth_min, eth_max, key)
				else:
					print("Something wrong with settings.py")

			except Exception as e:
				print(f"Transaction failed for private key: {key} | Error: {e}")
				failed_keys.append(key)



	elif choice == 2: #WITHDRAW
		for key in private_keys:
			try:
				zero += 1
				print(f'{zero}/{len(private_keys)}')

				if	swap_all_balance == True:
					withdraw_swap(keep_withdraw_value_from, keep_withdraw_value_to, key)
				elif swap_all_balance == False:
					withdraw(key)
				else:
					print("Something wrong with settings.py")

			except Exception as e:
				print(f"Transaction failed for private key: {key} | Error: {e}")
				failed_keys.append(key)


	elif choice == 3: #BALANCE ON CONTRACT
		for key in private_keys:
			try:
				check_balance(key)

			except Exception as e:
				print(f"Transaction failed for private key: {key} | Error: {e}")
				failed_keys.append(key)


	elif choice == 4: #BALANCE ON CHAIN
		for key in private_keys:
			try:
				print(f"""{web3.eth.account.from_key(key).address} | Balance on chain {"{:.8f}".format(check_balance_wallet(key))}""")

			except Exception as e:
				print(f"Transaction failed for private key: {key} | Error: {e}")
				failed_keys.append(key)


	elif choice == 5: #DEPOSIT-WITHDRAW LOOP
		Cycle = 1
		while Cycle < MAX_CYCLE:

			random.shuffle(private_keys)

			print(f"============== DEPOSIT CYCLE {Cycle} STARTED ==============")
			zero = 0

			for key in private_keys:
				try:
					zero += 1
					print(f'{zero}/{len(private_keys)}')

					if swap_all_balance == True:
						deposit_swap(keep_value_from, keep_value_to, key)
					elif swap_all_balance == False:
						deposit(eth_min, eth_max, key)

				except Exception as e:
					print(f"Transaction failed for private key: {key} | Error: {e}")
					failed_keys.append(key)

			print(f"============== DEPOSIT CYCLE {Cycle} FINISHED ==============")

			random.shuffle(private_keys)
			random_sleep()

			print(f"============== WITHDRAW CYCLE {Cycle} STARTED ==============")
			zero = 0

			for key in private_keys:
				try:
					zero += 1
					print(f'{zero}/{len(private_keys)}')

					if swap_all_balance == True:
						withdraw_swap(keep_withdraw_value_from, keep_withdraw_value_to, key)
					elif swap_all_balance == False:
						withdraw(key)
					else:
						print("Something wrong with settings.py")

				except Exception as e:
					print(f"Transaction failed for private key: {key} | Error: {e}")
					failed_keys.append(key)

			print(f"============== WITHDRAW CYCLE {Cycle} FINISHED ==============")

			Cycle += 1



	else:
		print(f"Wrong choice number. 1 | 2 | 3 | 4 | 5")




if __name__ == "__main__":
	main()
