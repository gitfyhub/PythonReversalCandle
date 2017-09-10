# Program to Track Reversal Candles

"""
9/10/2017
"""

import datetime
import pandas_datareader.data as web

START = datetime.datetime(2017, 6, 1)
END = datetime.datetime(2017, 9, 7)
STOCKDATA = web.DataReader("SPY", 'google', START, END)

STOCKDATA_1 = (
            (STOCKDATA.High > STOCKDATA.Close) & 
            (STOCKDATA.High > STOCKDATA.Open) &
            (STOCKDATA.High > STOCKDATA.Low) &
            (STOCKDATA.Close >= STOCKDATA.Low) & 
            (STOCKDATA.Open > STOCKDATA.Low) & 
            (STOCKDATA.Open > STOCKDATA.Close) &
            # Specific criteria:
            ( (STOCKDATA.Close) < ((((STOCKDATA.High + STOCKDATA.Low)/2)+STOCKDATA.Low)/1.9999) )
            #( (STOCKDATA.Close) < (247.849) )
            #( (STOCKDATA.Close) < (STOCKDATA.Low/1200) ) # return no results
            #( (STOCKDATA.Close) < ( (STOCKDATA.High + STOCKDATA.Low)/2) ) # returns results
            )
print STOCKDATA_1
