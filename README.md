# Zomato-Restaurant-Rating-Prediction
![Untitled](https://user-images.githubusercontent.com/87753242/136727141-8f1e41df-aec4-4a82-b317-8fc9ca6c9b7b.png)

The main goal of this project is to perform extensive Exploratory Data Analysis(EDA) on
the Zomato Dataset and build an appropriate Machine Learning Model that will help
various Zomato Restaurants to predict their respective Ratings based on certain
features.

# Dataset
![zomato_csv](https://user-images.githubusercontent.com/87753242/136779926-06f8fc05-3c0c-4264-942a-0ab7ad15a223.png)

# Exploratory Data Analysis (EDA)
![eda1](https://user-images.githubusercontent.com/87753242/136730675-003bba71-d8ed-4bee-a7b8-e152deec01dd.png)
As per the data we can see that the Caffe Coffee Day has most number of famous chains in Bangalore
 
![eda2](https://user-images.githubusercontent.com/87753242/136746766-f1136ba9-ac58-4915-8acd-c9bc80c90efd.png)
Most number of restaurants are present in BTM area Bangalore

![eda3](https://user-images.githubusercontent.com/87753242/136747590-41ff3ac8-069f-43f1-b859-8e41d12d5229.png)
Most common type of restaurant is Quick Bites

![eda4](https://user-images.githubusercontent.com/87753242/136757319-1a80b14b-f0f2-41eb-a3cf-7933155ff713.png)
![eda5](https://user-images.githubusercontent.com/87753242/136757337-0c6147d4-2343-449e-a4c0-5a86891ae4fb.png)

Number of restaurants with online and table booking facilities
Graph shows us that not much restaurant provide table booking facility.

![eda6](https://user-images.githubusercontent.com/87753242/136770082-de0f97d4-180a-4f13-96ef-5d89bfab4460.png)

Table Booking vs Rate
Restaurants that provide table booking have higher rating.

![eda7](https://user-images.githubusercontent.com/87753242/136770184-57f1de0d-659c-4777-9339-843318a357e9.png)

Rating based on Location

![eda8](https://user-images.githubusercontent.com/87753242/136770408-194a5d42-d5ed-4749-8575-6b5634878720.png)

Rating based on type of restaurant

# Feature Engineering and Feature Selection

URL, Address and phone are not rerquired so we delete these columns.

# Model Training

We will use Supervised Machine Learning Regression Algorithums for the model building

Models Used :
1) Random Forest (R2 Score: 86%)
2) Extra Tree Regressor (R2 Score: 91%)

Mean Absolute Error: 0.05453119552879585

Mean Squared Error: 0.018097247846268164

Root Mean Squared Error: 0.13452601178310522

# Model Deployment

![predicted1](https://user-images.githubusercontent.com/87753242/136776312-b970f827-fa5e-42b3-b133-10b42214da1c.png)

Database Used for storing Data
1) MongoDB

Model is deployed on Amazon Web Services colud platform
Tools used in deployment
1) Flask
2) Putty
3) Putty gen
4) API is designed in HTML and CSS

Online Link: http://ec2-18-118-186-20.us-east-2.compute.amazonaws.com:8080

![predicted](https://user-images.githubusercontent.com/87753242/136776370-c5e6715a-aafa-4433-8f25-24e5721b9519.png)
