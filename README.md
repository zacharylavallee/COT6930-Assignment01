# COT6930-Assignment01

Response Time and Quality Analysis 

* Authors: [Zachary Lavallee](http://www.linkedin.com/in/zacharynlavallee)
* Academic Supervisor: [Dr. Fernando Koch](http://www.fernandokoch.me)

# Research Question 

How does variability of Temperature, Context Size, and Prediction Length affect response time and quality?  

## Arguments

#### What is already known about this topic

* Temperature controls the randomness of the model's output.
  * A higher temperature makes the response more creative.
  * A lower temperature makes the response more deterministic.
* Context size sets the number of tokens the model considers when generating a response.
  * Determines how much prior conversation or text the model remembers.
* Prediction length limits the maximum number of tokens generated in the response.
  * A lower limit results in shorter responses, while a higher limit allows for more detailed answers

#### What this research is exploring

* I am using the Chain-of-Thought prompt template.
* I am exploring how variability of the three values affect response generation time and quality.

#### Implications for practice

* Optimization of the use of a model to answer specific questions and receive desired details from a prompt.
* Optimization of resources, not increasing values unnecessarily at the cost or time and resources it takes to produce a response.

# Research Method

To perform this experiment, I used the template code provided for the assignment and modified it to generate a set of responses, adjusting one, two, or all three variables at a time to observe their effects. Once the results were generated locally, I used AI to help analyze the results using a rubric to grade each response.

### Scoring Criteria

* Completeness (**0-5 points**)   
* Accuracy (**0-5 points**)  
* Depth & Context (**0-5 points**)  
* Clarity & Readability (**0-5 points**)  
* Usefulness & Application (**0-5 points**)  

# Results

Based on the results below, Context Size and Prediction Length have the largest effects on response time and response quality. However, high values in these two fields do not guarantee a higher quality score but do increase the probability of achieving one.

| Variation Type  | Temperature | Context Size | Prediction Length | Response Time (Seconds) | Score |
|----------------|------------|--------------|--------------------|---------------|---------------------|
| Baseline       | 1.0        | 100          | 100                | 3.733         | 22 |
| Temperature    | 0.5        | 100          | 100                | 2.963         | 22 |
| Temperature    | 1.0        | 100          | 100                | 2.849         | 20 |
| Temperature    | 1.5        | 100          | 100                | 2.84          | 22 |
| Context Size   | 1.0        | 500          | 100                | 3.757         | 20 |
| Context Size   | 1.0        | 5000         | 100                | 3.831         | 19 |
| Context Size   | 1.0        | 50000        | 100                | 2.217         | 16 |
| Prediction Length | 1.0     | 100          | 200                | 6.718         | 24 |
| Prediction Length | 1.0     | 100          | 1000               | 4.785         | 22 |
| Prediction Length | 1.0     | 100          | 5000               | 6.843         | 24 |
| Two Variables  | 0.5        | 500          | 100                | 3.761         | 20 |
| Two Variables  | 1.0        | 5000         | 100                | 3.78          | 21 |
| Two Variables  | 1.5        | 50000        | 100                | 4.249         | 21 |
| Three Variables | 0.5       | 500          | 200                | 6.426         | 22 |
| Three Variables | 1.0       | 5000         | 1000               | 15.327        | 24 |
| Three Variables | 1.5       | 50000        | 5000               | 13.667        | 21 |

# Further research

Further research would benefit from a larger collection of data. More data and variability in each of the three values would help provide a more comprehensive view on how to optimize these parameters for obtaining desired information from an AI model.








