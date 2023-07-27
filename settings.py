#--CONFIG--#

#Insert Private keys in keys.txt; One key per line | Приватные ключи в созданный файл keys.txt. По 1 в строку, не должны начинаться с 0x

CHECK_GWEI  = True # True / False. если True, тогда будем смотреть base gwei, и если он больше MAX_GWEI, скрипт будет ожидать снижения газа #!RM
MAX_GWEI    = 16 # gas в gwei (смотреть здесь : https://etherscan.io/gastracker) #!RM

from_sec = 1       #|Wait from N seconds between transactions | Минимальное значение "ждать от N sec между транзакиями". Для рандомного выбора
to_sec = 100	   #|Wait to N seconds between transactions | Максиимальное значение "спать до N sec между транзакциями". Для рандомного выбора
eth_min = 0.0001   #|Min ETH quantity for deposit | Значение ETH минимального депозита. Для рандомного выбора
eth_max = 0.0001   #|Max ETH quantity for deposit | Значение ETH максимального депозита. Для рандомного выбора

contract_address = "0xBd31E4c755580e97C54d6Ac55AD7B6Ae0D6bEFbb" #|Contract address. DO NOT CHANGE if own contract is not deployed | Адрес контракта. НЕ МЕНЯТЬ если не свой не деплоили


RPC = "https://mainnet.era.zksync.io" #|RPC for web3 provider. DO NOT CHANGE if you dont have own RPC | RPC web3 провайдера. НЕ МЕНЯТЬ если нет своей
#----------#

swap_all_balance = True #flag True / False
keep_value_from = 0.0008   # от скольки монет оставлять
keep_value_to   = 0.0009  # до скольки монет оставлять
#----------#

