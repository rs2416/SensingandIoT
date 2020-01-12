<p align="center">
	<sub>Imperial College London<br>Dyson School of Design Engineering</sub>
</p>
<h1 align="center">
	  Sensing & IoT
</h1>


### Introduction

This project is a preliminary investigation to see if it is feasible to predict social related anxiety using heart rate (HR) and sweat response (EDA) data and machine learning techniques (binary classification problem). Physiological data was collected for 2 weeks, specifically during 5 anxiety inducing events which included 3 pitches, a job interview and a staff student committee meeting. This physiological data was labelled through collection of automatically collected contextual data such as calendar data (Google Calendar API), Global Positioning System (GPS) data and mobile phone speed (Followmee.com). The data was then cleaned and split into 70% train 30% test, and various classification algorithm such as SVM, Logistic Regression and Decision Tree were used to train predictive models. These models were then evaluated for performance using 7-fold Cross Validation. A website platform was then created using React JavaScript to express the benefits of prediction of anxiety and how the prediction can facilitate self-help activities.

<h4 align="left">
	<a href="https://github.com/rs2416/SensingandIoT/blob/master/Report.pdf">Read the full report</a>
  <br>
  <br>
</h4>


### 1. Sensing (Data Collection)

The `data_collection` folder contains example raw files collected, as well as the python scripts used to automate collection. 

#### File descriptions

> * **Web_Driver.py**       Collects of GPS and mobile speed data using a selenium webdriver. Data is collected from the last 24 hours from FollowMee.com.   
> * **Upload_GPS.py**        Uploads the GPS and mobile speed data CSV using the Google Sheets API. 
> * **CalendarAPI.py**     Collects calendar events for the next 15 hours using Google Calendar API and then pushes events to Google Sheets, using the API. 
> * **TracksExample.csv**   Final raw data file of GPS and mobile data for the 15 days of data collection. Longditude and Latitude was removed.
> * **CalendarData.csv**    Final raw data file of calendar data for the 15 days of data collection. Summary of events have been removed.
> * **EDA.csv**             Example sweat response data. 
> * **HR.csv**              Example heart rate data CSV.
> * **Web_Driver_Demo.mp4** Recording of webdriver downloading GPS and mobile speed CSV


**Dependencies**: selenium, chromedriver.exe, webdriver-manager, os,gspread, google-api-python-client, google-auth-httplib2, google-auth-oauthlib, gspread oauth2client, datetime, pickle and pygsheets. The script files which involve API requests will not run without the API keys and credentials files. These have not been committed to GitHub.

### 2. Internet of Things (Data Analysis and Website)

The `data_analysis` folder contains folders for the 5 days of anxiety inducing events which includes a `data_cleaning.ipynb` used to clean and label the data for each event and the notebook used to perform data analysis. 

#### File descriptions

> * **event/data_cleaning.ipynb**  Notebook used to clean and label data for each anxiety inducing event.
> * **data_analysis.ipynb**  Notebook used to perform data analysis, as well as training of 7 predictive models and evaluation of these models.
> * **Figures**  Folder with figure outputs from the data_analysis notebook.

**Dependencies**: numpy, pandas, matplotlib, sklearn, seaborn and scipy.

<p align="left">
	<a href="https://github.com/rs2416/SensingandIoT/blob/master/data_analysis/data_analysis.ipynb" target="_blank">View the data analysis notebook</a>
</p>

The `website` folder contains all the assets and React JavaScript code used to implement the website prototype.To view locally download folder and open command window in the folder and run the following code. 

```
$ npm install 
$ npm run start
```

### References

This project was powered by:

- [Google Calendar API](https://developers.google.com/calendar)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [Selenium Webdriver](https://selenium.dev/)
- [Shards Dashboard](https://github.com/DesignRevision/shards-dashboard-react)

### License

<a rel="license" href="http://creativecommons.org/licenses/by/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/">Creative Commons Attribution 3.0 Unported License</a>.
