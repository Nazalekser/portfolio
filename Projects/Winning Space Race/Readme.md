## Project Description

### Background and context:
* Space X has the best launch prices for Falcon 9 rockets ($62 million vs. $165 million USD for others) due to the reuse of the first stage
* Space Y wants to compete with Space X

### Problem:
* It is necessary to study the success stories Space X and the best possible launch sites so that Space Y will have lower failure rate
* The launch success rate may depend on many factors such as payload mass, orbit type, and so on. It may also depend on the location and proximities of a launch site, i.e., the initial position of rocket trajectories

### Methodology
* Data was collected from REST API and web scraping
* The collected data were cleaned up and converted into a format that can be summarized in the final data
* Perform exploratory data analysis (EDA) using visualization and SQL
* Perform interactive visual analytics using Folium and Plotly Dash
* Perform predictive analysis using classification models
* The collected data were splited, different classification models were built, and their accuracy was evaluated


### Conclusions:
* SPACE Y company might be advised to start by launching not very large loads, as they are the ones with the highest success rate based on the SPACE X story
* It should launch from the KSC-LC 39A launch site, which has had more successful launches than the others
* It should choose orbits with higher launch success rates: ORBIT GEO, HEO, SSO, ES-L1
* The longer SPACE Y takes to make launches, the higher its success rate will be
* Based on the history of SPACE X, our best model, the decision tree classifier, can predict the outcome of launches with about 94.4% accuracy
