from recordclass import recordclass

from pyxenoverse.bsa.types import BaseType

BSAType14 = recordclass('BSAType14', [
    'i_00',
    'i_04',
    'i_08',
    'i_12',
    'i_16',
    'i_20',
    'i_24',
    'i_28',
    'i_32',
    'i_36',
    'i_40',
    'i_44',
    'i_48',
    'i_52',
    'i_56',
    'i_60',
    'i_64',
    'i_68',
    'i_72',
    'i_76',
    'i_80',
    'i_84',
])


# Type 14
class Type14(BaseType):
    type = 14
    bsa_record = BSAType14
    byte_order = 'I'*22  # 22 "I" make 88 bytes
    size = 88

    def __init__(self, index):
        super().__init__(index)
