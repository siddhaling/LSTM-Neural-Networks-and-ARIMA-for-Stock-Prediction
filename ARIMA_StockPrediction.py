#### ARIMA Part 
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'AAPL.csv',usecols=['Date','Adj Close'],parse_dates = ['Date']
                )
df.index = pd.DatetimeIndex(df.Date)

df['Adj Close'].plot()
from pyramid.arima import auto_arima

stepwise_model = auto_arima(df1['Adj Close'], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)

print(stepwise_model.aic())

train = df1['Adj Close'].loc['2017-03-01':'2018-03-31']
test = df1['Adj Close'].loc['2018-03-31':]

train_dec18 = df1[‘Adj Close’].loc[‘2017-03-01’:’2018-12-31’]
test_dec18 = df1[‘Adj Close’].loc[‘2018-12-31’]

stepwise_model.fit(train_dec18)
plt.plot(test_nov18)
plt.plot(forecast3)

plt.xlabel(‘Date’)
plt.ylabel(‘Price AAPL’)
plt.title(‘Actual Vs Forecast’)
plt.plot(test,label=’Actual’)
plt.plot(forecast, label =’Forecast’)
plt.grid()
plt.legend()
plt.xticks(rotation=45)

