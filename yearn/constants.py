from brownie import interface

CONTROLLER_INTERFACES = {
    "0x2be5D998C95DE70D9A38b3d78e49751F10F9E88b": interface.ControllerV1,
    "0x9E65Ad11b299CA0Abefc2799dDB6314Ef2d91080": interface.ControllerV2,
}

VAULT_INTERFACES = {
    "0x29E240CFD7946BA20895a7a02eDb25C210f9f324": interface.yDelegatedVault,
    "0x881b06da56BB5675c54E4Ed311c21E54C5025298": interface.yWrappedVault,
    "0xc5bDdf9843308380375a611c18B50Fb9341f502A": interface.yveCurveVault,
}

STRATEGY_INTERFACES = {
    "0x25fAcA21dd2Ad7eDB3a027d543e617496820d8d6": interface.StrategyVaultUSDC,
    "0xA30d1D98C502378ad61Fe71BcDc3a808CF60b897": interface.StrategyDForceUSDC,
    "0x1d91E3F77271ed069618b4BA06d19821BC2ed8b0": interface.StrategyTUSDCurve,
    "0xAa880345A3147a1fC6889080401C791813ed08Dc": interface.StrategyDAICurve,
    "0x787C771035bDE631391ced5C083db424A4A64bD8": interface.StrategyDForceUSDT,
    "0x932fc4fd0eEe66F22f1E23fBA74D7058391c0b15": interface.StrategyMKRVaultDAIDelegate,
    "0xF147b8125d2ef93FB6965Db97D6746952a133934": interface.CurveYCRVVoter,
    "0x112570655b32A8c747845E0215ad139661e66E7F": interface.StrategyCurveBUSDVoterProxy,
    "0x6D6c1AD13A5000148Aa087E7CbFb53D402c81341": interface.StrategyCurveBTCVoterProxy,
    "0x07DB4B9b3951094B9E278D336aDf46a036295DE7": interface.StrategyCurveYVoterProxy,
    "0xC59601F0CC49baa266891b7fc63d2D5FE097A79D": interface.StrategyCurve3CrvVoterProxy,
    "0x395F93350D5102B6139Abfc84a7D6ee70488797C": interface.StrategyYFIGovernance,
    "0xc8327D8E1094a94466e05a2CC1f10fA70a1dF119": interface.StrategyCurveGUSDProxy,
    "0x530da5aeF3c8f9CCbc75C97C182D6ee2284B643F": interface.StrategyCurveCompoundVoterProxy,
    "0x4720515963A9d40ca10B1aDE806C1291E6c9A86d": interface.StrategyUSDC3pool,
    "0xe3a711987612BFD1DAFa076506f3793c78D81558": interface.StrategyTUSDypool,
    "0xc7e437033D849474074429Cbe8077c971Ea2a852": interface.StrategyUSDT3pool,
}

VAULT_ALIASES = {
    "0x29E240CFD7946BA20895a7a02eDb25C210f9f324": "aLINK",
    "0x881b06da56BB5675c54E4Ed311c21E54C5025298": "LINK",
    "0x597aD1e0c13Bfe8025993D9e79C69E1c0233522e": "USDC",
    "0x5dbcF33D8c2E976c6b560249878e6F1491Bca25c": "curve.fi/y",
    "0x37d19d1c4E1fa9DC47bD1eA12f742a0887eDa74a": "TUSD",
    "0xACd43E627e64355f1861cEC6d3a6688B31a6F952": "DAI",
    "0x2f08119C6f07c006695E079AAFc638b8789FAf18": "USDT",
    "0xBA2E7Fed597fd0E3e70f5130BcDbbFE06bB94fe1": "YFI",
    "0x2994529C0652D127b7842094103715ec5299bBed": "curve.fi/busd",
    "0x7Ff566E1d69DEfF32a7b244aE7276b9f90e9D0f6": "curve.fi/sbtc",
    "0xe1237aA7f535b0CC33Fd973D66cBf830354D16c7": "WETH",
    "0x9cA85572E6A3EbF24dEDd195623F188735A5179f": "curve.fi/3pool",
    "0xec0d8D3ED5477106c6D4ea27D90a60e594693C90": "GUSD",
    "0x629c759D1E83eFbF63d84eb3868B564d9521C129": "curve.fi/compound",
}

CURVE_BTC_SWAPS = {
    "0x93054188d876f558f4a66B2EF1d97d16eDf0895B": "ren",
    "0x7fC77b5c7614E1533320Ea6DDc2Eb61fa00A9714": "sbtc",
    "0x4CA9b3063Ec5866A4B82E437059D2C43d1be596F": "hbtc",
}

DEPLOYED_BLOCKS = {
    "0x29E240CFD7946BA20895a7a02eDb25C210f9f324": 10599617,
    "0x881b06da56BB5675c54E4Ed311c21E54C5025298": 10604016,
    "0x597aD1e0c13Bfe8025993D9e79C69E1c0233522e": 10532708,
    "0x5dbcF33D8c2E976c6b560249878e6F1491Bca25c": 10559448,
    "0x37d19d1c4E1fa9DC47bD1eA12f742a0887eDa74a": 10603368,
    "0xACd43E627e64355f1861cEC6d3a6688B31a6F952": 10650116,
    "0x2f08119C6f07c006695E079AAFc638b8789FAf18": 10651402,
    "0xBA2E7Fed597fd0E3e70f5130BcDbbFE06bB94fe1": 10690968,
    "0x2994529C0652D127b7842094103715ec5299bBed": 10709740,
    "0x7Ff566E1d69DEfF32a7b244aE7276b9f90e9D0f6": 10734341,
    "0xe1237aA7f535b0CC33Fd973D66cBf830354D16c7": 10774489,
    "0x9cA85572E6A3EbF24dEDd195623F188735A5179f": 11026971,
    "0xec0d8D3ED5477106c6D4ea27D90a60e594693C90": 11065127,
}
