# 7-days-weather-forecast-imd
 Get real-time -7days forecast through indian metrological department API

# steps to setup the project directory in your local machine
### 1.Install python 3.10 or later (make sure to install stable version)
### 2. Create a Virtual Environment (Optional, but recommended)
#### 2.1)for windows    use command in your project directory
         python -m venv weatherenv
#### 2.2) Activating the virutal environment
        weatherenv\scripts\activate
  #### here weatherenv is the name of your virtual environment
### 3) Installing packages required
###### 3.1) use command below in your project directory to packages to your virtual environment (after creation of virtual environment is recomended for error free excution)
            Command: pip install -r requirements.txt

### 4) Step to start fast api server 
#### 4.1) use command below to host the fast api on your local machine 
          Command : uvicorn app:app --reload
   ###### now you can vist http://127.0.0.1:8000 
   ######  on which your application is running
### 5) to get weather report enter /id of your required city to get 7 Day's forecast

#### 5.1) go to url : http://127.0.0.1:8000/43181 
   ######    the above url fetches weather data of vijayawada for next 7 Days ..
   ######      you can replace the IMD weather code on your choice to get report of your location
### 6) To get IMD weather code of your location
##### search in any web search engine as "IMD weather code for \<your location\>"
###### Replace "\<your location\>" with your desired location
     
