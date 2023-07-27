TG_TOKEN = 'your_tgbot_token' # создать можешь здесь : https://t.me/BotFather
TG_ID = 0 # узнать можешь здесь : https://t.me/getmyid_bot

API_0x = 'b2f0f80e-7767-4c8f-8c5f-78548e8f3141' # получить api key от 0x здесь : https://dashboard.0x.org/apps

# меняем рпс на свои
DATA = {
    'ethereum': {'rpc': 'https://rpc.ankr.com/eth', 'scan': 'https://etherscan.io/tx', 'token': 'ETH', 'chain_id': 1},

    #    'optimism'      : {'rpc': 'https://rpc.ankr.com/optimism', 'scan': 'https://optimistic.etherscan.io/tx', 'token': 'ETH', 'chain_id': 10},
    'optimism': {'rpc': 'https://optimism.meowrpc.com', 'scan': 'https://optimistic.etherscan.io/tx', 'token': 'ETH','chain_id': 10},
    #    'optimism'      : {'rpc': 'https://optimism-mainnet.public.blastapi.io', 'scan': 'https://optimistic.etherscan.io/tx', 'token': 'ETH','chain_id': 10},
    #    'optimism'      : {'rpc': 'https://rpc.optimism.gateway.fm', 'scan': 'https://optimistic.etherscan.io/tx', 'token': 'ETH','chain_id': 10},
    #    'optimism'      : {'rpc': 'https://optimism.api.onfinality.io/public', 'scan': 'https://optimistic.etherscan.io/tx', 'token': 'ETH', 'chain_id': 10},

    #    'bsc'           : {'rpc': 'https://rpc.ankr.com/bsc', 'scan': 'https://bscscan.com/tx', 'token': 'BNB', 'chain_id': 56},
    'bsc': {'rpc': 'https://binance.nodereal.io', 'scan': 'https://bscscan.com/tx', 'token': 'BNB', 'chain_id': 56},
    #    'bsc'           : {'rpc': 'https://bsc-dataseed1.ninicoin.io', 'scan': 'https://bscscan.com/tx', 'token': 'BNB', 'chain_id': 56},
    #    'bsc'           : {'rpc': 'https://bsc.rpc.blxrbdn.com', 'scan': 'https://bscscan.com/tx', 'token': 'BNB', 'chain_id': 56},
    #    'bsc'           : {'rpc': 'https://bsc-dataseed1.defibit.io', 'scan': 'https://bscscan.com/tx', 'token': 'BNB', 'chain_id': 56},

    #    'polygon'       : {'rpc': 'https://rpc.ankr.com/polygon', 'scan': 'https://polygonscan.com/tx', 'token': 'MATIC', 'chain_id': 137},
    #    'polygon'       : {'rpc': 'https://polygon-mainnet.g.alchemy.com/v2/cNqx6RC6tko8TO-H_cUVa7Oma0bvWqy_', 'scan': 'https://polygonscan.com/tx', 'token': 'MATIC', 'chain_id': 137},
    #    'polygon'       : {'rpc': 'https://polygon.llamarpc.com', 'scan': 'https://polygonscan.com/tx', 'token': 'MATIC', 'chain_id': 137},
    'polygon': {'rpc': 'https://polygon-bor.publicnode.com', 'scan': 'https://polygonscan.com/tx', 'token': 'MATIC', 'chain_id': 137},
    #    'polygon'       : {'rpc': 'https://polygon.rpc.blxrbdn.com', 'scan': 'https://polygonscan.com/tx', 'token': 'MATIC', 'chain_id': 137},

    'polygon_zkevm': {'rpc': 'https://zkevm-rpc.com', 'scan': 'https://zkevm.polygonscan.com/tx', 'token': 'ETH', 'chain_id': 1101},

    #    'arbitrum'      : {'rpc': 'https://rpc.ankr.com/arbitrum', 'scan': 'https://arbiscan.io/tx', 'token': 'ETH', 'chain_id': 42161},
    'arbitrum': {'rpc': 'https://arbitrum-one.publicnode.com', 'scan': 'https://arbiscan.io/tx', 'token': 'ETH', 'chain_id': 42161},
    #    'arbitrum'      : {'rpc': 'https://arbitrum.api.onfinality.io/public', 'scan': 'https://arbiscan.io/tx', 'token': 'ETH', 'chain_id': 42161},
    #    'arbitrum'      : {'rpc': 'https://arb-mainnet-public.unifra.io', 'scan': 'https://arbiscan.io/tx', 'token': 'ETH', 'chain_id': 42161},

    #    'avalanche'     : {'rpc': 'https://rpc.ankr.com/avalanche', 'scan': 'https://snowtrace.io/tx', 'token': 'AVAX', 'chain_id': 43114},
    'avalanche': {'rpc': 'https://avalanche-c-chain.publicnode.com', 'scan': 'https://snowtrace.io/tx', 'token': 'AVAX', 'chain_id': 43114},
    #    'avalanche'     : {'rpc': 'https://avalanche.blockpi.network/v1/rpc/public', 'scan': 'https://snowtrace.io/tx', 'token': 'AVAX','chain_id': 43114},
    #    'avalanche'     : {'rpc': 'https://api.avax.network/ext/bc/C/rpc', 'scan': 'https://snowtrace.io/tx', 'token': 'AVAX','chain_id': 43114},

    #    'fantom'        : {'rpc': 'https://rpc.ankr.com/fantom', 'scan': 'https://ftmscan.com/tx', 'token': 'FTM', 'chain_id': 250},
    'fantom': {'rpc': 'https://rpcapi.fantom.network', 'scan': 'https://ftmscan.com/tx', 'token': 'FTM', 'chain_id': 250},
    #    'fantom'        : {'rpc': 'https://1rpc.io/ftm', 'scan': 'https://ftmscan.com/tx', 'token': 'FTM', 'chain_id': 250},
    #    'fantom'        : {'rpc': 'https://fantom.publicnode.com', 'scan': 'https://ftmscan.com/tx', 'token': 'FTM', 'chain_id': 250},

    'nova': {'rpc': 'https://nova.arbitrum.io/rpc', 'scan': 'https://nova.arbiscan.io/tx', 'token': 'ETH', 'chain_id': 42170},

    'zksync': {'rpc': 'https://mainnet.era.zksync.io', 'scan': 'https://explorer.zksync.io/tx', 'token': 'ETH',  'chain_id': 324},

    'celo': {'rpc': 'https://1rpc.io/celo', 'scan': 'https://celoscan.io/tx', 'token': 'CELO', 'chain_id': 42220},
    #    'celo'          : {'rpc': 'https://forno.celo.org', 'scan': 'https://celoscan.io/tx', 'token': 'CELO', 'chain_id': 42220},

    #    'gnosis'        : {'rpc': 'https://rpc.ankr.com/gnosis', 'scan': 'https://gnosisscan.io/tx', 'token': 'xDAI', 'chain_id': 100},
    'gnosis': {'rpc': 'https://rpc.gnosis.gateway.fm', 'scan': 'https://gnosisscan.io/tx', 'token': 'xDAI',  'chain_id': 100},
    #    'gnosis'        : {'rpc': 'https://gnosis-mainnet.public.blastapi.io', 'scan': 'https://gnosisscan.io/tx', 'token': 'xDAI', 'chain_id': 100},
    #    'gnosis'        : {'rpc': 'https://xdai-rpc.gateway.pokt.network', 'scan': 'https://gnosisscan.io/tx', 'token': 'xDAI', 'chain_id': 100},

    'core': {'rpc': 'https://rpc.coredao.org', 'scan': 'https://scan.coredao.org/tx', 'token': 'CORE', 'chain_id': 1116},
    #    'core': {'rpc': 'https://rpc-core.icecreamswap.com', 'scan': 'https://scan.coredao.org/tx', 'token': 'CORE','chain_id': 1116},

    'harmony': {'rpc': 'https://api.harmony.one', 'scan': 'https://explorer.harmony.one/tx', 'token': 'ONE',  'chain_id': 1666600000},

    'moonbeam'      : {'rpc': 'https://rpc.ankr.com/moonbeam', 'scan': 'https://moonscan.io/tx', 'token': 'GLMR', 'chain_id': 1284},

    'moonriver'     : {'rpc': 'https://moonriver.public.blastapi.io', 'scan': 'https://moonriver.moonscan.io/tx', 'token': 'MOVR', 'chain_id': 1285},
}

# апи ключи от бирж. если биржей не пользуешься, можно не вставлять
CEX_KEYS = {
    'binance': {'api_key': 'i17s0tSqQIcRejyUt9AHEbFZdBbSEHgeoqyK9c95O8ToEHVNvr5kuGM1aSktA2p0', 'api_secret': 'gjgc5SevgejZPfouXTlWKxnOkVOjDymnUwcUtgufRNtGdzQ7euqVVaDEcPNJ3Uvi'},
    'mexc': {'api_key': 'your_api_key', 'api_secret': 'your_api_secret'},
    'kucoin': {'api_key': 'your_api_key', 'api_secret': 'your_api_secret', 'password': 'your_api_password'},
    'huobi': {'api_key': 'ht4tgq1e4t-6d011e97-f13fc395-494bf', 'api_secret': '35530736-175f7ec7-78c4f61c-dcb04'},
    'bybit': {'api_key': 'GeYKst1GydU9eXdodb', 'api_secret': '48HnpfBcGNEQ2MaB2hnRPKUqVCV6fAMU77u2'},
}

# можешь записать любое кол-во аккаунтов, сделал таким образом чтобы постоянно данные от новых акков не вводить, а просто вызывать по имени аккаунта
OKX_KEYS = {
    'account_1': {'api_key': '4deef4a8-843a-49b8-bda3-78b724bbfb09', 'api_secret': '367905B878A1529755F47DBB8FBEAC41', 'password': '@PZ*JQS85hewq', },
    'account_2': {'api_key': 'your_api_key', 'api_secret': 'your_api_secret', 'password': 'your_api_password', },
}