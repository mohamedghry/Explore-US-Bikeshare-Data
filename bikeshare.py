import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nPlease select the city you\'d like to see data for (Chicago - New York city - Washington):\n').lower()
    while city not in CITY_DATA:
        city = input('\nInvalid entry\nPlease enter a city from the choices above:\n').lower()

    # get user input for month (all, january, february, ... , june)
    month = input('\nWould you like to filter data by date? If so, please enter a month (January through June), or enter "all" for no filter:\n').lower()
    
    while month not in MONTH_DATA:
        month = input('\nInvalid entry, please enter a month (January through June), or type "all" for no filter:\n').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nWould you like to filter data by a certain week day? If so, Please enter a day (Monday through Sunday), or enter "all" for no filter:\n').lower()
    
    while day not in DAY_DATA:
        day = input('Invalid entry, please enter a day, or enter "all" for no filter:\n').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.DataFrame(pd.read_csv(CITY_DATA[city]))
    
    # converting date columns into datetime format for data extraction
    df['Start Time'] = pd.to_datetime(df['Start Time'], format= '%Y-%m-%d %H:%M:%S')
    df['End Time'] = pd.to_datetime(df['End Time'], format= '%Y-%m-%d %H:%M:%S')
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month = MONTH_DATA.index(month)
        df = df.loc[df['month'] == month]

    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print("Most common month:\n" + MONTH_DATA[most_common_month].title())
    
    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("Most common day:\n" + most_common_day)
    
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    # shows the output hour in AM/PM format
    if popular_hour < 12:
        print('Most common start hour:\n', popular_hour, 'AM')
    elif popular_hour >= 12:
        if popular_hour > 12:
            popular_hour -= 12
        print('Most common start hour:\n', popular_hour, 'PM')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most popular start station: \n", popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most popular end station: \n", popular_end_station)

    # display most frequent combination of start station and end station trip
    trip_combination = df['Start Station'] + " to " +  df['End Station']
    common_trip_combination = trip_combination.mode()[0]
    print("Most popular trip from start to end:\n {}".format(common_trip_combination)) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    m, s = divmod(total_travel_time, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    total_travel_time = "\nTotal trip duration: %02d days %02d hrs %02d min %02d sec" % (d, h, m, s)
    print(total_travel_time, '\n')


    # display mean travel time \ format time in days, hours, minutes, and seconds
    mean_travel_time = df['Trip Duration'].mean()
    m, s = divmod(mean_travel_time, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)   
    mean_travel_time = "\nMean travel time: %02d days %02d hrs %02d min %02d sec" % (d, h, m, s)
    print(mean_travel_time, '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:\n", user_types)

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(' ' * 40)
        print('Counts of users by gender:')
        print(gender)
    except:
        print('Counts of users by gender:\nSorry, no gender data available for this city')

    # Display earliest, most recent, and most common year of birth
    try:
        oldest = df['Birth Year'].min()
        youngest = df['Birth Year'].max()
        common = df['Birth Year'].mode()
        print(' ' * 40)
        print('Counts of users by birth year:')
        print('Oldest user(s) birth year: ', int(oldest))
        print('Youngest user(s) birth year: ', int(youngest))
        print('Most common birth year: ', int(common))
    except:
        print('Counts of users by birth year:\nSorry, no birth year data available for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    # Ask user if they want to see individual trip data.
    start_data = 0
    end_data = 5
    df_length = len(df.index)
    
    while start_data < df_length:
        raw_data = input("\nWould you like to see some lines of raw data? Enter 'yes' or 'no'.\n")
        if raw_data.lower() == 'yes':
            
            print("\nDisplaying 5 rows of raw data.\n")
            if end_data > df_length:
                end_data = df_length
            print(df.iloc[start_data:end_data])
            start_data += 5
            end_data += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()