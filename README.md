# WebTestingExamples

This is a testing automation project using Python and Pytest

Pages covered:

- Wikipedia
- Twitter

# Wikipedia

## Index page

Here the test is center on check some languages texts and search box

| ID | Test Name                    | Test Steps                                                                | Test Data | Test Expected Results                           | Test Result |
|----|------------------------------|---------------------------------------------------------------------------|-----------|-------------------------------------------------|-------------|
| W1 | Get to Wikipedia             | Get www.wikipedia.org                                                     |           | Should be on Wikipedia page                     | Pass        |
| W2 | Spanish and English language | Get www.wikipedia.org, then look for the language Spanish and English     |           | Should be the words English and Español present | Pass        |
| W3 | Input box                    | Get www.wikipedia.org, then look for the search box                       |           | Should be a search box present                  | Pass        |
| W4 | Search pc                    | Get www.wikipedia.org, then input pc inside search box and send enter key | pc        | Should be redirect to the pc search result      | Pass        |


# Twitter

As a user i want to login using my user account and search for selenium account to see the Tweets
And make a tweet saying "Hello i am using #python #pytest and #selenium to make this tweet"

| ID | Test Name                        | Test Steps                                                     | Test Data                                                      | Test Expected Result                             | Test Result |
|----|----------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|--------------------------------------------------|-------------|
| T1 | Get to Twitter                   | Get to twitter.com                                             | twitter.com                                                    | Should be on Twitter                             | Passed      |
| T2 | Use a Google account to login    | Click on log in button                                         |                                                                |                                                  | Passed      |
|    |                                  | Then fill the user box on Sign in modal, click next button     | USER in env file                                               | Should appear password box                       | Passed      |
|    |                                  | Then fill the password box on Sign in modal, click next button | PASSWORD in env file                                           | Should appear second step sign in                | Passed      |
|    |                                  | Then write the code from authenticator (this is a manual step) |                                                                | Should sign in on Twitter correctly              | Passed      |
| T3 | Input in the search box selenium | Input selenium in search box                                   | selenium                                                       | Should dropdown a list with the possible results | Passed      |
|    |                                  | Then select @SeleniumHQ user                                   | @SeleniumHQ                                                    | Should appear the wall of Selenium user          | Passed      |
| T4 | Make a tweet                     | Click on Tweet button                                          |                                                                | Should appear a modal box to make the tweet      | Passed      |
|    |                                  | Input the text in the box                                      | Hello this tweet was made using #python #pytest and #selenium. |                                                  | Passed      |
|    |                                  | Click on tweet button in the modal                             |                                                                | Should appear the tweet in my board              | Passed      |


