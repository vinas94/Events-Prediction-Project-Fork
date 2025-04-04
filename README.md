# README

## Dataset Overview

The dataset used in this project contains the following columns:

- **event_time**: The timestamp of the event.
- **product_id**: The unique identifier for the product.
- **category_id**: The unique identifier for the product category.
- **category_code**: The hierarchical category code for the product.
- **brand**: The brand of the product.
- **price**: The price of the product.
- **user_id**: The unique identifier for the user.
- **user_session**: The session identifier for the user.
- **event_type**: The type of event (view, cart, purchase).

This dataset provides a comprehensive view of user interactions with products, enabling analysis of user behavior, product trends, and more.

After cleaning the unique entries per column:

- event_time       501143
- product_id        24255
- category_id         260
- category_code       104
- brand               728
- price              9478
- user_id          224971
- user_session     273421
- event_type            3

---

## Table of Contents

1. [Project Scope](#project-scope)
2. [Proposed Path](#proposed-path)
3. [Data Preprocessing](#data-preprocessing)
4. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
5. [Modeling and Predictions](#modeling-and-predictions)
6. [Conclusion](#conclusion)

---

## Project Scope

The goal of this project is to analyze user interactions with products and derive actionable insights. The scope includes:

- Understanding user behavior patterns.
- Predicting future user actions based on historical data.
- That make event_type the target column. Is a user "viewing", "adding to cart" or finally "purchasing" will be the main question to answer based on all the other columns.

---

## Path

1. **Data Cleaning**: Handle missing values, duplicates, and inconsistent data.
2. **Exploratory Data Analysis (EDA)**: Visualize and summarize the dataset to uncover trends and patterns.
3. **Feature Engineering**: Create new features to enhance model performance.
4. **Model Development**: Build and evaluate predictive models.
5. **Insights and Recommendations**: Provide actionable insights based on the analysis.


## Proposed Steps

##### One Hot Encoding

- None

One hot encoding could be suitable for the event_type column. But since we will use event_type as our target the classification models would be able to handle three numbers.

##### Vectorization

- category_code, brand, product_id, category_id

Vectorization would be useful for object columns category_code and brand columns. Furthermore, I would suggest to transform product_id and category_id into into object type and vectorize as well. Think of product_id as a product name.

Proposed method would be tf.keras.layers.TextVectorization.

Tokenization, Stemmisation, Lemmisation, removing StopWords etc. is not needed, it is already cleaned. We also do not need sentiment analysis or similarity checks.
The purpose of vectorisation is to avoid one hot fix encoding and create a mapping.

##### Dealing with class imbalance

- view        458082
- cart         34668
- purchase     23105

Proposal would be to use Tomek Links to reduce the views.

We could also check:
-  if any outliers could be deleted
- maybe group produdcts with low count as "other" or get rid of them
- any other ideas?
- most users never purchase... 

##### Scaling

- price

We could check if a method of scaling could be applied to price. It would depend on the model if it makes a difference.

##### New columns

The new columns would be based on user_id:

- previous_total_view_count [int]
- previous_view_of_product_id_count [int]
- previous_total_cart_count [int]
- previous_cart_of_product_id_count [int]
- previous_total_purchase_count [int]
- previous_purchase_of_product_id_count [int]
- time_since_last_view [float]
- time_since_last_view_product_id [float]
- time_since_last_cart [float]
- time_since_last_cart_product_id [float]
- time_since_last_purchase [float]
- time_since_last_purchase_product_id [float]
- count_of_event_in_same_session [int]
- total_sessions [int]
- total_sessions_product_id [int]

Time could be in minutes and float? Maybe some min max scaling?

#### EDA (Explorative Data Analysis)
Once the new columns exist, we should split the users into three groups "only view", "only up until cart" and "purchasers" to plot some distributions or frequency tables or correlations compare different behavioral patterns.

#### Deleting columns

- user_id, session_id

Once the new columns have been created, these two columns could be deleted.

#### Train & Test Split

The time of the events ranges from 2020-09-24 11:57:26+0000 until 2021-02-28 23:59:09+0000. Suggestion would be 70% train and 30% test split according to time.

##### Models

- Try out some classification model (sklearn) (similar to the Iris flower dataset)
- Try out some neural network (tf) (similar to MNIST)