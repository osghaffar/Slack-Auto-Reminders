# Slack-Auto-Reminders
A fairly simple program that sends automated reminders to members 3 days (or however many days) before their exam date.

Compiled a list of every active member's exam dates, along with their unique Slack ID, into a CSV file like so:

| ID     | Exam 1      | Exam 2      | Exam 3      |
|------- |------------ |------------ | ------------|
| 12345  | 2019-01-07  | 2019-01-11  | 2019-01-15  |
| 13254  | 2019-01-07  | 2019-01-10  | 2019-01-15  |
| 54321  | 2019-01-08  | 2019-01-10  | 2019-01-17  |

The program first uses the Pandas library to find all dates that match 3 days from today (in other words, a person that has an exam in 3 days). It then returns their IDs, converts it to a string format, and stores it into an array.

This array is then passed into the function that utilizes the Slack API to send messages to each person respectively. The message is customizable.

The program can be used in conjunction with crontab for full automation.
