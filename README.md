# COT6930-Assignment01
## Zachary Lavallee


### Target: ollama
### Model: llama3.2:latest
### Prompt template: Chain-of-Thought
### Prompt: 
    Step 1: Define personal privacy. 
    Step 2: Define national security. 
    Step 3: Identify conflicts. 
    Step 4: Suggest a balance.
    answer: What is the ideal balance between personal privacy and national security in the digital age?

### Experimental Use Case:
   * Evaluate and grade the responses llama3.2:latest generates while modifying the fields: 
     * temperature
     * num_ctx
     * num_predict


# Scoring Criteria

### 1. Completeness (**0-5 points**)   

### 2. Accuracy (**0-5 points**)  

### 3. Depth & Context (**0-5 points**)  

### 4. Clarity & Readability (**0-5 points**)  

### 5. Usefulness & Application (**0-5 points**)  

# Experiment Results

# Experiment Results

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





