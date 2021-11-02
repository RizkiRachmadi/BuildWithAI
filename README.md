# BuildWithAI
This is our proposed idea for the challenge 1 from BuildWithAI Hackathon : Digital Education

# Problem Statement
Digital Learning & Education
The Pandemic has impacted education - classes have moved online, students have been isolated on screens and coping with this change. Despite the challenges, the digital school has the potential to transform education. How can we empower students and teachers in this new digital school paradigm?

## Our Approach:
1. Pandemic has created a condition where the mental health from the students in a worse condition. Out of all the mental health condition, ASD (Autism Spectrum Disorder) is one with the highest occurance that happen in the children - adolescent
2. With current situation, many parents are not able to send their children to their usual learning facility, and only a few knew how to handle the special need from their children.
3. Previous approach only detecting ASD as Autism or Not. This is highly misleading, because ASD has many sub-types as well as personal traits that differentiate it from one children with the other.
4. Online learning has the potential to help the family in order to access a broad and educaitonal content.
5. Combining this idea, we proposed to create an automatic classifier to help the parents determine what kind of ASD that happened in their children. We also build a recommender engine that could gives advice to them regarding what topic and what courses that best suitable to teach to them.

## Scope:
1. ASD classification : ASD is only one of the subtypes from mental health problem. As the first step, we will focused to help the children with this trait, because it's common occurance.
2. AQ 10 + BAPQ Quotient : There are many ways to detect ASD, ranging from simple question to complex image classification. We aim to make our system become easy to access, without any additional devices. To fulfill this goal, we choose to use quotient method, where we combine AQ 10 quotient (to detect ASD) with BAPQ quotient (to detect the personality trait)
3. Udemy-based Course : There are many kinds of online learning sources, but for our prototype, we are focusing Udemy based courses

## Data Gathering:
We proposed a new way to handle ASD children in our research by using three kinds of dataset:
1. AQ-10 Quotient : We will used this dataset to detect the autism tendency from the children
2. BAPQ Quotient : We will used this to determine the mental tendency that accompany the children (Aloof, Rigid, Pragmatic)
3. Udemy Course : To build our recommender engine, we used the course dataset from Udemy, consist of the title, rating, and the topic from the course.

## Data Analysis:
Data Analysis:
We conclude that previous research only used 1 type of quotient to determine the autism level from the children, which is why we proposed to use the
combination of 2 quotient:

1. We provide a several set questions that the children/parents/teacher must answer
2. The answer will be weighted, reversed (if needed), and scored to get the level of autism as well as the personality disorder
3. Based on the classification result, we will suggest what kind of subject or topic that is suitable for the children
4. Our recommender engine could assist to suggest what kind of course that the children could took provided by Udemy.

## Additional Info:
1. To make our model is more suitable to use in the community, we choose to integrate it with Streamlit to make the recommender engine is easier to access
[![Streamlit.jpg](https://i.postimg.cc/x8cNTZnx/Streamlit.jpg)](https://postimg.cc/9wHQLJ4Z)
2. We build another dashboard using JS, which could be accessed through this link : http://autisapp.projekbareng.com/
[![Dashboard.jpg](https://i.postimg.cc/CKVghrjF/Dashboard.jpg)](https://postimg.cc/fV5F5K2F)
