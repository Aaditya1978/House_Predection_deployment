# House_Predection_deployment
house Prediction Model Deployment Using Flask

In this Repository I have made a main file wich is the main flask file or the app file.It is app.py.It handles all the request for the server.
The Other important file is homeprices_model. It is the file in which I have Trained My model for predicting House Prices.It is The main MAchine Learning File.

The data on which my model is trained is homprices file which is the CSV file.

Now lin_reg.pkl , poly_reg.pkl and pca.pkl are the pickle files which are then read by our app file for predicting new prices.

After that the Template Folder has Our HTML files for webpage. It has two files one is index and other one is predict. The index file is our main home page file and the predict file is for getting the data.
The another Folder which is static has one image to display it on our webpage.

Now I have Deployed my web application on cloud using heroku platform which is very good one.
For Deploying our model on Heroku We need Two more files.
One is requirements.txt in which we write the reqiuired version of each module or library needed like Python , pandas, numpy etc.
The othe file is Procfile it tells the Heroku server that which file to run first or from which file server will start.
PLEASE NOTE :---
The Procfile name is case sensitive and also it should not have any extension . It means that it should be without any extension.So be careful :)


The Link To The website for my deployed Website is:---
https://house-prices-prediction-api.herokuapp.com/

If you like . Please Star my Repo :)
