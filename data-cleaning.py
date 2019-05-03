import csv
import pandas as pd
myfile=open('emails.csv','r')


df=pd.read_csv(myfile)

train_df=df[:685]
df=df[685:]


cv_df=df[:342]
df=df[342:]

test_df=df[:341]
df=df[341:]

temp_df=df[:2752]
frames=[train_df,temp_df]
train_df=pd.concat(frames)
df=df[2752:]


temp_df=df[:804]
frames=[cv_df,temp_df]
cv_df=pd.concat(frames)
df=df[804:]


frames=[test_df,df]
test_df=pd.concat(frames)


train_df.to_csv('train-data.csv')
cv_df.to_csv('cv-data.csv')
test_df.to_csv('test-data.csv')

print(train_df)
print(cv_df)
print(test_df)


