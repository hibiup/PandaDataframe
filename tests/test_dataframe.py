from unittest import TestCase

import pandas as pd

class testFilter(TestCase):
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
    
    def test_build_random_df(self):
        '''
        * 10 Minutes to Pandas:
          http://pandas.pydata.org/pandas-docs/stable/10min.html

        * Time Series Data Virtualization with Python: 
          https://machinelearningmastery.com/time-series-data-visualization-with-python/
        '''
        import numpy as np
        from matplotlib import pyplot

        # generate a 5 x 4 DF with randon number
        date_range = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
        df1 = pd.DataFrame(np.random.randn(len(date_range), 4), 
                          index=date_range, 
                          columns=list('ABCD'))
        print(df1)

        df2 = pd.DataFrame(np.random.randn(10, 4))
        print(df2)

        # Save to figure
        ax = df2.plot()
        fig = ax.get_figure()
        fig.savefig('/tmp/dataframe.png')
        # Show out
        pyplot.show()
    
    def test_build_series(self):
        import numpy as np
        from matplotlib import pyplot

        s1 = pd.Series([x for x in range(6)], index=pd.date_range('20130102', periods=6))
        print(s1)

        date_range = pd.date_range('3/6/2012 00:00', periods=50, freq='D')
        s2 = pd.Series(np.random.randn(len(date_range)), index=date_range)
        print(s2)

        # Save to figure
        #ax = s2.plot(style='k.')
        ax = s2.hist()
        fig = ax.get_figure()
        fig.savefig('/tmp/series.png')
        # Show out
        pyplot.show()

