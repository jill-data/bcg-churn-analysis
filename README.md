# How price can affect customer churn

## Background

PowerCo is a major gas and electricity utility that supplies to corporate, SME (Small &
Medium Enterprise), and residential customers. The power-liberalization of the energy
market in Europe has led to significant customer churn, especially in the SME segment.
They have partnered with BCG to help diagnose the source of churning SME customers.

## Hypothesis

A fair hypothesis is that price changes affect customer churn. Therefore, it is helpful
to know which customers are more (or less) likely to churn at their current price, for
which a good predictive model could be useful. Moreover, for those customers that are at
risk of churning, a discount might incentivize them to stay with the client. They are
considering a 20% discount that is considered large enough to dissuade almost anyone
from churning (especially those for whom price is the primary concern).

## Approach

The above hypothesis can be formulated as a data science problem: Build a
predictive model to predict customer churn from their current information. Customer
information might include:

- Plan that they are currently on (perks, price, term length, etc.)
- Demographics (age, location, gender, etc.)
- Engagement history (customer lifetime, past interactions with the company, etc.)
- Churn data (whether they have churned)

Therefore, the key steps are as follows:

- Gather the identified data sources
- Identify what price sensitivity is
- Clean and process data
- Exploratory data analysis
- Feature engineering
- Build and evaluate predictive model to predict customer churn - In this case a logistic regressor
- Analyse the coefficient of the pricing variable to determine the effect of pricing on
  customer churn
- Evaluate business impact of the model
