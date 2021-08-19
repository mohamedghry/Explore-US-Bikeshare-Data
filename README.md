# Overview
In this project, Python is used to explore data related to bicycle-sharing systems for three major cities in the United States — Chicago, New York City, and Washington.

- The source code takes in raw input from the user to create an interactive experience.
- According to the user input, the code will import the data and output descriptive statistics.

<p>&nbsp;</p>

# Bike Share Data
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by [Motivate](https://www.motivateco.com/ "Motivate"), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

<p>&nbsp;</p>

# The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same **core six (6)** columns:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

- Gender
- Birth Year

![](https://video.udacity-data.com/topher/2018/March/5aa771dc_nyc-data/nyc-data.png)
<p align="center">
<i>Data for the first 10 rides in the new_york_city.csv file</i>
</p>


The original files are much larger and messier, and you don't need to download them, but they can be accessed here if you'd like to see them ([Chicago](https://www.divvybikes.com/system-data "Chicago"), [New York City](https://www.citibikenyc.com/system-data "New York City"), [Washington](https://www.capitalbikeshare.com/system-data "Washington")). These files had more columns and they differed in format in many cases. Some [data wrangling](https://en.wikipedia.org/wiki/Data_wrangling "data wrangling") has been performed to condense these files to the above core six columns to make your analysis and the evaluation of your Python skills more straightforward. In the Data Wrangling course that comes later in the Data Analyst Nanodegree program, students learn how to wrangle the dirtiest, messiest datasets, so don't worry, you won't miss out on learning this important skill!

<p>&nbsp;</p>

# Statistics Computed
You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:

## #1 Popular times of travel (i.e., occurs most often in the start time)

most common month
most common day of week
most common hour of day
## #2 Popular stations and trip

most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)
## #3 Trip duration

total travel time
average travel time
## #4 User info

counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)

<p>&nbsp;</p>

# The Files
To answer these questions using Python, you will need to write a Python script. To help guide your work in this project, a template with helper code and comments is provided in a <span>bikeshare.py</span> file, and you will do your scripting in there also. You will need the three city dataset files too:

- chicago.csv
- new_york_city.csv
- washington.csv