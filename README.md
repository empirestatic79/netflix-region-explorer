# &#x09;			    ***NETFLIX REGION EXPLORER***





## **What it does:**

* #### This code is nothing but a Command-Line tool which lets you search or see through 4 different regions. Although the data I entered is 4 years old from 2022 as that was the only good available data I could find anywhere. 



## **Why I Built it:**



* #### The only reason why I built this is because I love shows and especially those in Netflix, and a lot of the times I cant find many shows in my specific region. So For my first every project I decided to make this only using simple core Python, Pandas and RapidFuzz.



## **Tools Used:**

1. #### Pandas helped in adding and reading the data which was in the form of a CSV File. It was also useful in Filtering the movies and shows when searching through all those regions.



#### 2\. The RapidFuzz helped a LOT as many times due to typos or even a simple non upper-case letter can cause an Syntax Error. RapidFuzz got rid of that problem and it even with a small typo it would give a match score with all the Movies/Shows in the entire Database. It would only give those Movies/Shows which has a score of >=80. 





#### 3\. The Core Python helped in Defining normal functions which were overall needed to run the code like IF-ELSE, DEF() and PRINT() etc etc.





## **Data Source:**

* #### I took the Data (CSV Files) from Kaggle. Well it was just a single file containing lots of countries. So i filtered it and made 4 separate files for 4 separate countries "https://www.kaggle.com/code/lucifierx/netflix/input" this is the exact place I took it from.



## ***HOW TO RUN IT:***

#### 

#### git clone https://github.com/empirestatic79/netflix-region-explorer.git

#### cd netflix-region-explorer





#### Install Requirements:

#### Pip install -r requirements.txt 



#### RUN: python -m src.cli 



