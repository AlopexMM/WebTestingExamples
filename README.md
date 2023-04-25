# WebTestingExamples

This is a testing automation project using Python and Pytest

Pages covered:

- Wikipedia

# Wikipedia

## Index page

[Index screenshot](C:\\Users\\mario\\PycharmProjects\\WebTestingExamples\\pages_pictures\\wikipedia.org.png)

Here the test is center on check some languages texts and search box

TODO put a tabel with the id of the test and what is tested

| ID | Test Name                    | Test Steps                                                                | Test Data | Test Expected Results                           | Test Result |
|----|------------------------------|---------------------------------------------------------------------------|-----------|-------------------------------------------------|-------------|
| W1 | Get to Wikipedia             | Get www.wikipedia.org                                                     |           | Should be on Wikipedia page                     | Pass        |
| W2 | Spanish and English language | Get www.wikipedia.org, then look for the language Spanish and English     |           | Should be the words English and Español present | Pass        |
| W3 | Input box                    | Get www.wikipedia.org, then look for the search box                       |           | Should be a search box present                  | Pass        |
| W4 | Search pc                    | Get www.wikipedia.org, then input pc inside search box and send enter key | pc        | Should be redirect to the pc search result      | Pass        |