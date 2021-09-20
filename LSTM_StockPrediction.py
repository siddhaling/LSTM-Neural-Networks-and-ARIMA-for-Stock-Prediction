import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'AAPL.csv',usecols=['Date','Adj Close'],parse_dates = ['Date']
                )
df.index = pd.DatetimeIndex(df.Date)

df['Adj Close'].plot()
#### LSTM Part:
>training = df.iloc[:2048,1:2].values
>from sklearn.preprocessing import MinMaxScaler
>scaler = MinMaxScaler(feature_range=(0,1))
>training_scaled = scaler.fit_transform(training)
>x_train1 = []
>y_train1 = []

>for i in range(60,len(training_scaled)):
    x_train1.append(training_scaled[i-60:i,0])
    y_train1.append(training_scaled[i,0])
>x_train1, y_train1 = np.array(x_train1), np.array(y_train1)
x_train1 = np.reshape(x_train1,(x_train1.shape[0],x_train1.shape[1],1))
>from keras.models import Sequential
>from keras.layers import Dense
>from keras.layers import LSTM
>from keras.layers import Dropout
Building our model :-
#initialize model
new_model = Sequential()

#layer 1 of LSTM
new_model.add(LSTM(units=50,return_sequences=True,input_shape=(x_train1.shape[1],1)))
new_model.add(Dropout(0.2))

#layer 2 of LSTM
new_model.add(LSTM(units=50,return_sequences=True))
new_model.add(Dropout(0.2))

#layer 3 of LSTM
new_model.add(LSTM(units=50,return_sequences=True))
new_model.add(Dropout(0.2))

#layer 4 of LSTM
new_model.add(LSTM(units=50))
new_model.add(Dropout(0.2))

#Output layer of model
new_model.add(Dense(units=1))

#compiling the model
new_model.compile(optimizer='adam',loss='mean_squared_error')
inputs1 = total1[len(total1)-len(df_test1)-60:].values
inputs1 = inputs1.reshape(-1,1)
inputs1.shape
x_test5 =[]
for i in range(60,588):
    x_test5.append(inputs1[i-60:i,0])

x_test5 = np.array(x_test5)
predicted1 = scaler.inverse_transform(predicted1)

%matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6
y = df_test1['Close']
x= df_test1['Date']
plt.plot(x,y,c='r',label='Actual')
plt.plot(predicted1,c='b')
plt.show()
plt.legend()
plt.xticks(rotation=45)
plt.legend()

