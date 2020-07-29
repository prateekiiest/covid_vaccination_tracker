# Hackathon 2020

## Introduction
For our project, we have decided to design a system for distributing a potential COVID-19 vaccine within the Indian state of Karnataka. Since the vaccine cannot be delivered to everyone in need instantly, it is important to develop a priority system such that those who are most in need of the vaccine can get attended to first.

We have outline a solution for the vaccine distribution into a few straightfoward steps:
1.  Collect Data Set from Vaccine Candidates
2.  Generate Group Classifier
3.  Determine Most At-Risk People
4.  Compile a List of the Most At-Risk Wards
5.  Send Incoming Batch of Vaccines to Most High-Risk Ward

## Data Generation
As a proof of concept of our solution, we have generated a sample data set of 1000 different vaccine candidates along with relevant data (age, occupation, existing medical conditions, etc.). In order to generate a large enough yet realistic data set, we implemented a few different strategies.

First, we scraped a webpage containing Karnataka's various pincodes/locatlities and assigned them to newly generated vaccine candidates. Next, we assigned each candidate an age based on the normal age distribution for a given population. Each candidate was then assigned an occupation from a set of common occupations within the state of Karantaka, or "None" in some cases ("None" was assigned with a certain probability based on the given candidate's age). Finally, we assigned random candidates a value of "Y" or "N" for recent travel, and then used this response as well as the rate of infection in their pincode to generate a probability for if that person has come into contact with someone who had the virus within the last 2 weeks.

Combining these data points with a handful of others for each individual, we garnered sufficient data to feed into an ML model interpret this data and determine who was at the highest mortality risk of COVID-19.