from unittest import TestCase

import pandas as pd

class testDataFrameMask(TestCase):
    def test_masking(self):
        df = pd.read_csv("tests/data/data.csv")
        print(df.shape)
        self.assertEqual((24, 4), df.shape)

        df_masked = df[df.TXN_TYP_GRP == 'DRAFT']
        print(df_masked.shape)
        self.assertEqual((21, 4), df_masked.shape)

        df_masked = df[df.TXN_TYP_GRP == 'WIRE PAYMENT']
        print(df_masked.shape)
        self.assertEqual((3, 4), df_masked.shape)

    def test_loc(self):
        df = pd.read_csv("tests/data/data.csv")

        # loc() is not index based
        top_3_lines = df.loc[0:2,['TXN_TYP_GRP', 'FIELD_B']]
        print(top_3_lines)

        # iloc() is index based
        top_2_lines = df.iloc[0:2,[1, 3]]
        print(top_2_lines)
        
        # first argument of loc() can be condition
        B6_lines = df.loc[df.FIELD_B=='B6',['TXN_TYP_GRP', 'FIELD_B']]
        print(B6_lines)

        # replace 'B6' to 'B7'
        df.loc[df.FIELD_B=='B6',['FIELD_B']]='B7'
        print(df.loc[:,['FIELD_B']])