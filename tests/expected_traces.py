CALL_TRACE_EXPECTED_OUTPUT = """
CALL: 0xF2Df0b975c0C9eFa2f8CA0491C2d1685104d2488 [194827 gas]
├── CALL: 0xBcF7FFFD8B256Ec51a36782a52D0c34f6474D951.<0x61d22ffe> [168423 gas]
│   └── CALL: 0x274b028b03A250cA03644E6c578D81f019eE1323.<0x8f27163e> [160842 gas]
├── CALL: 0xBcF7FFFD8B256Ec51a36782a52D0c34f6474D951.<0x61d22ffe> [116942 gas]
│   └── CALL: 0x274b028b03A250cA03644E6c578D81f019eE1323.<0x8f27163e> [114595 gas]
└── CALL: 0xBcF7FFFD8B256Ec51a36782a52D0c34f6474D951.<0xb9e5b20a> [93421 gas]
    ├── CALL: 0x274b028b03A250cA03644E6c578D81f019eE1323.<0x8f27163e> [91277 gas]
    ├── CALL: 0x274b028b03A250cA03644E6c578D81f019eE1323.<0x90bb7141> [46476 gas]
    └── CALL: 0x274b028b03A250cA03644E6c578D81f019eE1323.<0x90bb7141> [23491 gas]
"""
STATIC_TRACE_EXPECTED_OUTPUT = (
    "STATICCALL: 0x274b028b03A250cA03644E6c578D81f019eE1323.<0x7007cbe8> [369688 gas]"
)
DELEGATECALL_TRACE_EXPECTED_OUTPUT = (
    "DELEGATECALL: 0xaa1A02671440Be41545D83BDDfF2bf2488628C10.<0x70a08231> [161021 gas]"
)
PARITY_CALL_TRACE_EXPECTED_OUTPUT = """
CALL: 0xFEB4acf3df3cDEA7399794D0869ef76A6EfAff52.<0x6a761202> [1481991 gas]
└── DELEGATECALL: 0xd9Db270c1B5E3Bd161E8c8503c55cEABeE709552.<0x6a761202> [1475675 gas]
    └── DELEGATECALL: 0x40A2aCCbd92BCA938b02010E17A5b8929b49130D.<0x8d80ff0a> [1419469 gas]
        ├── CALL: 0x93A62dA5a14C80f265DAbC077fCEE437B1a0Efde.<0x78e32e26> [40542 gas]
        │   └── CALL: 0x19D3364A399d251E894aC732651be8B0E4e85001.<0xa9059cbb> [33288 gas]
        │       └── DELEGATECALL: 0xe11ba472F74869176652C35D30dB89854b5ae84D.<0xa9059cbb> [30216 gas]
        ├── CALL: 0x19D3364A399d251E894aC732651be8B0E4e85001.<0x2e1a7d4d> [186144 gas]
        │   └── DELEGATECALL: 0xe11ba472F74869176652C35D30dB89854b5ae84D.<0x2e1a7d4d> [185575 gas]
        │       ├── STATICCALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x70a08231> [2602 gas]
        │       ├── STATICCALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x70a08231> [602 gas]
        │       ├── STATICCALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x70a08231> [602 gas]
        │       ├── STATICCALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x70a08231> [602 gas]
        │       ├── STATICCALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x70a08231> [602 gas]
        │       ├── CALL: 0x3D6532c589A11117a4494d9725bb8518C731f1Be.<0x2e1a7d4d> [114610 gas]
        │       │   ├── STATICCALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x70a08231> [2602 gas]
        │       │   ├── STATICCALL: 0xdA816459F1AB5631232FE5e97a05BBBb94970c95.<0x70a08231> [6545 gas]
        │       │   │   └── DELEGATECALL: 0x9C13e225AE007731caA49Fd17A41379ab1a489F4.<0x70a08231> [3873 gas]
        │       │   ├── STATICCALL: 0xdA816459F1AB5631232FE5e97a05BBBb94970c95.<0x99530b06> [17589 gas]
        │       │   │   └── DELEGATECALL: 0x9C13e225AE007731caA49Fd17A41379ab1a489F4.<0x99530b06> [17423 gas]
        │       │   │       └── STATICCALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x70a08231> [2602 gas]
        │       │   ├── STATICCALL: 0xdA816459F1AB5631232FE5e97a05BBBb94970c95.<0x313ce567> [1900 gas]
        │       │   │   └── DELEGATECALL: 0x9C13e225AE007731caA49Fd17A41379ab1a489F4.<0x313ce567> [1734 gas]
        │       │   ├── CALL: 0xdA816459F1AB5631232FE5e97a05BBBb94970c95.<0xe63697c8> [45266 gas]
        │       │   │   └── DELEGATECALL: 0x9C13e225AE007731caA49Fd17A41379ab1a489F4.<0xe63697c8> [45082 gas]
        │       │   │       ├── STATICCALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x70a08231> [602 gas]
        │       │   │       ├── STATICCALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x70a08231> [602 gas]
        │       │   │       └── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [9074 gas]
        │       │   ├── STATICCALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x70a08231> [602 gas]
        │       │   └── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [23374 gas]
        │       ├── STATICCALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x70a08231> [602 gas]
        │       ├── STATICCALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x70a08231> [602 gas]
        │       └── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        ├── CALL: 0x93A62dA5a14C80f265DAbC077fCEE437B1a0Efde.<0x78e32e26> [32304 gas]
        │   └── CALL: 0xdA816459F1AB5631232FE5e97a05BBBb94970c95.<0xa9059cbb> [30345 gas]
        │       └── DELEGATECALL: 0x9C13e225AE007731caA49Fd17A41379ab1a489F4.<0xa9059cbb> [30167 gas]
        ├── CALL: 0xdA816459F1AB5631232FE5e97a05BBBb94970c95.<0x2e1a7d4d> [31960 gas]
        │   └── DELEGATECALL: 0x9C13e225AE007731caA49Fd17A41379ab1a489F4.<0x2e1a7d4d> [31788 gas]
        │       ├── STATICCALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x70a08231> [602 gas]
        │       ├── STATICCALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x70a08231> [602 gas]
        │       └── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [3474 gas]
        ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x095ea7b3> [24514 gas]
        ├── CALL: 0xD152f549545093347A162Dce210e7293f1452150.<0xc73a2d60> [391427 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x23b872dd> [26675 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [25374 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [25374 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [25374 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [25374 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [25374 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [25374 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [25374 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        │   ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [25374 gas]
        │   └── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0xa9059cbb> [8274 gas]
        ├── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x095ea7b3> [24514 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xb6b55f25> [22394 gas]
        │   └── CALL: 0x6B175474E89094C44Da98b954EedeAC495271d0F.<0x23b872dd> [9575 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [31472 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        ├── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
        └── CALL: 0x60c7B0c5B3a4Dc8C690b074727a17fF7aA287Ff2.<0xc355f343> [26672 gas]
"""
PARITY_CREATE_TRACE_EXPECTED_OUTPUT = """
CALL: 0x76E2cFc1F5Fa8F6a5b3fC4c8F4788F0116861F9B.<0x61b69abd> [417274 gas]
├── CREATE: 0xFEB4acf3df3cDEA7399794D0869ef76A6EfAff52
└── CALL: 0xFEB4acf3df3cDEA7399794D0869ef76A6EfAff52.<0xb63e800d> [327242 gas]
    └── DELEGATECALL: 0x34CfAC646f301356fAa8B21e94227e3583Fe3F5F.<0xb63e800d> [325506 gas]
"""
PARITY_SELFDESTRUCT_TRACE_EXPECTED_OUTPUT = """
CALL: 0x863DF6BFa4469f3ead0bE8f9F2AAE51c91A907b4.<0xcbf0b0c0> [85402 gas]
└── SELFDESTRUCT: 0x863DF6BFa4469f3ead0bE8f9F2AAE51c91A907b4
"""
PARITY_REVERT_TRACE_EXPECTED_OUTPUT = """
CALL: [reverted] 0xFEB4acf3df3cDEA7399794D0869ef76A6EfAff52.<0x6a761202>
└── DELEGATECALL: 0xd9Db270c1B5E3Bd161E8c8503c55cEABeE709552.<0x6a761202>
"""
PARITY_OUT_OF_GAS_TRACE_EXPECTED_OUTPUT = """
CALL: [reverted] 0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9.<0xa9059cbb>
└── DELEGATECALL: 0xC13eac3B4F9EED480045113B7af00F7B5655Ece8.<0xa9059cbb>
"""
PARITY_CREATE_REVERT_TRACE_EXPECTED_OUTPUT = """
CALL: [reverted] 0xa5409ec958C83C3f309868babACA7c86DCB077c1.<0xddd81f82>
└── CREATE
"""
PARITY_REVERT_TRACE_WITH_MESSAGE_EXPECTED_OUTPUT = """
CALL: [reverted] 0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45.<0x5ae401dc>
└── DELEGATECALL: 0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45.<0x472b43f3>
    ├── CALL: 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2.<0xd0e30db0> [23974 gas]
    ├── CALL: 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2.<0xa9059cbb> [8062 gas]
    ├── STATICCALL: 0x5bE7632014b307Bd29304BBCeAb6478a89Fa7384.<0x70a08231> [6676 gas]
    ├── STATICCALL: 0x2c6b0aA42D4FCB880F5fFFfbD0e39e4b48548C1E.<0x0902f1ac> [2504 gas]
    ├── STATICCALL: 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2.<0x70a08231> [534 gas]
    ├── CALL: 0x2c6b0aA42D4FCB880F5fFFfbD0e39e4b48548C1E.<0x022c0d9f> [119936 gas]
    │   ├── CALL: 0x5bE7632014b307Bd29304BBCeAb6478a89Fa7384.<0xa9059cbb> [95819 gas]
    │   ├── STATICCALL: 0x5bE7632014b307Bd29304BBCeAb6478a89Fa7384.<0x70a08231> [2676 gas]
    │   └── STATICCALL: 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2.<0x70a08231> [534 gas]
    └── STATICCALL: 0x5bE7632014b307Bd29304BBCeAb6478a89Fa7384.<0x70a08231> [2676 gas]
"""
