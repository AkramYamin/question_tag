#### -- Project Status: [Active]

## Project Intro/Objective
The purpose of this project is to predict the most relevent tag or topic for a question or text depends on pre-defined tags. 

### Methods Used
* Machine Learning
* Data Visualization
* Linear Support Vector Machine

### Technologies
* Python3 
* MySql
* Pandas, jupyter
* Flask

## Project Description
using this code you can create tag prediction model, the main alg. used is Linear Support Vector Machine, and for database  i used mysql.connector lib 
after training and create this prediction model you can deply it as flask app, to get best accurace you can automate the training process (use all data for training  give us more accurace).

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data that used in stackoverflow example available [here](https://storage.googleapis.com/tensorflow-workshop-examples/stack-overflow-data.csv).

    *to get faster training process you can download data set one, and in examples/stackoverflow_data_example.py change the data source to your local dataset*

3. Data transfaring/database fetching scripts are being kept [here](https://github.com/AkramYamin/question_tag/blob/master/src/utils/dto.py)
4. Data pre-processing/transformation scripts are being kept [here](https://github.com/AkramYamin/question_tag/tree/master/src/processing)
5. model training and saving as pickle file are being kept [here](https://github.com/AkramYamin/question_tag/tree/master/src/modelling)


## run the example 
  after install requered libs, to create model using stackoverflow data use this :
  ```
  $ python3 examples/stackoverflow_data_example.py 
  ```
  ![alt text](https://github.com/AkramYamin/question_tag/blob/master/data/imgs/stackoverflow_run_example.png)
  
  to run api that provides prediction service using stackoverflow trained model use this :
  ```
  $ python3 predictor_api.py 
  ```
  ![alt text](https://github.com/AkramYamin/question_tag/blob/master/data/imgs/predictor_api%20run%20example.png)
  
## test api using postman 
  after run predictor_api.py 
  create post request to localhost:5000/tags and add json object to request body
  
  ![alt text](https://github.com/AkramYamin/question_tag/blob/master/data/imgs/postman_api_test.png)

  
  in console you can see request status 200 and prediction result is correct 
  
  ![alt text](https://github.com/AkramYamin/question_tag/blob/master/data/imgs/postman%20api%20result.png)

  
