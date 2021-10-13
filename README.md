# data-day-grind-2.0


## Images:

![gallery-3](https://user-images.githubusercontent.com/70055735/137084447-4c3c0072-8278-475f-82d2-5a548a68c86a.jpg)
![gallery-2](https://user-images.githubusercontent.com/70055735/137084450-4c26fb35-151d-48a3-b406-c7c7f977b5a9.jpg)
![gallery](https://user-images.githubusercontent.com/70055735/137084453-fc451468-fc05-4eda-9d14-6fe862aa633b.jpg)


## Inspiration
We are a team of students who regularly access courses from ed-tech websites. However, we are always confused while choosing a course, and we end up opening hundreds of tabs from different ed-tech companies to select 1 course. That's when we realized we could build a course aggregator!

## What it does
www.getmy.courses is a course aggregator that sources the best courses for you. When a user searches for a course, the website will process the search using natural language processing. The website has more than 49000 courses from 4 ed-tech companies:  Udemy, Coursera, Data Camp, and edX. Moreover, the website also has a chatbot to assist users with career advice and general course questions. 

## How we built it
We used Flask to create the website. We vectorized the text and found the cosine similarity between the input text and the course titles to find the top-recommended 8 courses. We used dialogue flow (Google Cloud) to create the chatbot. Additionally, we host our website using firebase, and we bought the domain from GoDaddy Registry. Lastly, we used several libraries to conduct data analysis and visualization: Latent Dirichlet Allocation (LDA), scikit-learn, matplotlib, etc. 

## Challenges we ran into
Our initial idea was to scrape websites the ed-tech websites. When we started, we realized ed-tech websites are developed using React, so web scraping libraries like Beautiful Soup can't scrape the websites. However, we realized we could use multiple datasets and use that data set to build an aggregator. 

## Accomplishments that we're proud of
We are proud that 50% of our team is participating for the first time, and we overcame the initial challenge (described in the Challenges we ran into section) we ran into. We are also proud that our team was from 3 regions, and we could effectively collaborate and work despite the timezone difference. 

## What's next for Get my course
We plan to add live scrapping so that the courses are displayed live rather than from a dataset. In the future, we hope to polish the UI making it more user-friendly. 

# Team members 
<ul>
<li> Kevin </li>
<li> Ahmed </li>
<li> Shloak </li>
<li> Bhavik </li>
</ul>  




