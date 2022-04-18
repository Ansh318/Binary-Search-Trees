# Decison Trees and Bias
This project focuses on zip files, modules, object oriented programming, and trees. I have created one tree.py file. For testing, I have used the .zip files, tester.py, and expected.json.

# Background
Sadly, there is a long history of lending discrimination based on race in the United States. In some cases, lenders have literally drawn red lines on a map around certain neighbourhoods where they would not offer loans, based on the racial demographics of those neighbourhoods (read more about redlining here: https://en.wikipedia.org/wiki/Redlining). If you're interested as to how redlining can still be seen today, here is an article discussing similar behaviors seen in the insurance industry: https://www.propublica.org/article/minority-neighborhoods-higher-car-insurance-premiums-white-areas-same-risk

In 1975, congress passed the Home Mortgage Disclosure Act (HDMA), to bring more transparency to this injustice (https://en.wikipedia.org/wiki/Home_Mortgage_Disclosure_Act). The idea is that banks must report details about loan applications and which loans they decided to approve. In this project, we'll be analyzing HDMA data from Wisconsin, Illinois, and Louisiana: https://www.consumerfinance.gov/data-research/hmda/historic-data/.

As data scientists, a real concern we must consider is whether our models show bias. If we train our models to mimic human behavior, will they pickup on human bias? If we don't base our models on sufficient dataset, will they overgeneralize? In this project, we'll be providing several files describing decision trees. Decisions trees are a kind of model that can output things like approve/deny on a row-by-row basis. Your job will be to write Python code to load and run the decision trees. At least one of them is racially biased, and you'll be asked to write a function that exposes this.

# Decision Tree
The DTree will provide a means of predicting whether or not an applicant should have their loan accepted. DTree class will inherit from SimplePredictor which will predict if a loan should be approved or denied.

dtree.readTree(reader, path) will take a file name that will be read from a zip via the reader and build a decision tree using its contents. 

  - dtree.predict(data) will return True for loan approved and False 
  - tree.getDisapproved() will return the number of applicants disapproved


## Authors

- [@AnshAgarwal](https://www.github.com/Ansh318)


