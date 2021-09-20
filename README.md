# LSTM-Neural-Networks-and-ARIMA-for-Stock-Prediction
LSTM Neural Networks and ARIMA for Stock Prediction
### Credit: Nikhil Sharma, Siddhaling Urolagin
Historical prices of commodities or stock indexes can help us understand the way the commodity/stock has performed over the past and can help us also predict its price in the near future. We can use this data to our advantage apply various time series models depending on whether it is univariate or multivariate. “The accurate prediction of trends in stock price can not only help investors avoid and control risks in time, but also have important guiding significance in reducing investment losses.”[1]. Auto-Regressive Moving average is known for univariate time series predictions with average accuracy of 80 % .ARIMA-GARCH/APARCH family of models, using the Box-Jenkins methodology are often used to forecast the movement of stock prices.[2] The disadvantages of these models are that they are based on historical prices and tend to indicate the trend at a later stage after the movement has already been taken. Recent development in computational power and advancements in neural networks/deep learning  have helped us up bring models which have accuracy to 98% .
“In financial time series, the data often show a strong correlation, and historical information also has very high value in application”.[3] Long Short term memory part of re-current neural network works by plugging together input from next layer to earlier nodes thereby allowing it to have backward travel in a feedforward network.

## Data Source Exhibition
We will be using stock prices of Apple Inc. in the dataset which is taken from yahoo finance computed daily. Our dataset is containing stock prices for roughly past 10 years from Feb 2009 to Feb 2019.

![image](https://user-images.githubusercontent.com/33411128/134021058-f2ec0c32-c704-4a8a-99bb-991609ffd222.png)

![image](https://user-images.githubusercontent.com/33411128/134021090-eee6c94e-b3b2-4e94-8de7-e3a33e6d1473.png)

Model Summary:
![image](https://user-images.githubusercontent.com/33411128/134021262-7066a807-971f-4cc5-a3f6-49a969598ee1.png)

Line Plot of Actual VS Predicted Set

![image](https://user-images.githubusercontent.com/33411128/134021343-ec2e9050-ad04-4c40-9db4-b54380b30e2d.png)

Line Plot of Actual VS Predicted Set

![image](https://user-images.githubusercontent.com/33411128/134021462-ce0a9f73-4e04-4558-816c-ac4009b7e329.png)

## Forecasting by Using LSTM

![image](https://user-images.githubusercontent.com/33411128/134021556-541de90d-d695-4e1b-be3f-2de6ff5ff099.png)

Training Phase

![image](https://user-images.githubusercontent.com/33411128/134021604-777d59f2-c0d7-4253-9502-b746e192ce9e.png)

Line Plot of Actual VS Predicted LSTM

![image](https://user-images.githubusercontent.com/33411128/134021723-137e1423-2467-48cc-b36d-5e255d31b191.png)



# Further Projects and Contact
www.researchreader.com

https://medium.com/@dr.siddhaling

Dr. Siddhaling Urolagin,\
PhD, Post-Doc, Machine Learning and Data Science Expert,\
Passionate Researcher, Deep Learning, Machine Learning and applications,\
dr.siddhaling@gmail.com



References
[1]: Shui-Ling YU and Zhe Lia,*Stock Price Prediction Based on ARIMA-RNN Combined Model, 2017 4th International Conference on Social Science (ICSS 2017) , ISBN: 978-1-60595-525-4
[2]: Derek LAM , Lincoln College , Time Series Modelling of Monthly WTI Crude Oil Returns, 2017
[3]: Shui-Ling YU and Zhe Lia,*Stock Price Prediction Based on ARIMA-RNN Combined Model, 2017 4th International Conference on Social Science (ICSS 2017) , ISBN: 978-1-60595-525-4



