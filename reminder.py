import pandas as pd
from datetime import date, timedelta
from slackclient import SlackClient

slack_token = SlackToken #enter your slack token here
sc = SlackClient(slack_token)

df = pd.read_csv("/Users/Documents/slackIDS.csv")

today = date.today() #2019-01-04
checkdate = str(today + timedelta(days=3)) #2019-01-07
print("Date to check for: ", checkdate)

#use the pandas query function to locate which exam dates are == to the date we want
#this format can be used for however many columns there are
ID = df[df['Exam 1'] == checkdate]['ID']
ID2 = df[df['Exam 2'] == checkdate]['ID']
ID3 = df[df['Exam 3'] == checkdate]['ID']

#store the returned IDs into an array
IDs = [ID, ID2, ID3]
IDs = pd.concat(IDs)

#convert this array to string format
userID = IDs.astype(str).values.tolist()

print("Sending to these IDs:")

#for loop continues for the length of the array userID
for i in range(len(userID)):
    print(userID[i])
    sc.api_call(
            "chat.postMessage",
            channel = userID[i],
            text = "You have an exam coming up in 3 days!",
            username = "Exam Reminders"
    )
    
