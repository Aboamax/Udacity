import time
import pandas as pd
import numpy as np




CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('please enter a city name (chicago, new york city or washington): ').lower()
    while city not in (CITY_DATA.keys()):
        print('The name of city not avilable!')
        city = input('please renter the correct city name: ').lower()

    #get user input filter by month , day or both
    filter = input('Do you like to see results by month, day, both or none?: ').lower()
    while filter not in (['month','day', 'both', 'none']):
        print('please enter a valid filter')
        filter = input(' month, day, both or none?  ').lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('Select a month from "january to june" or select "all" : ').lower()
    while month not in months:
        print("The month name you'hv been enter incorrect!!")
        month = input("!!select 'january', 'february', 'march', 'april', 'may', 'june, all',").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','saturday', 'sunday', 'monday','tuesday','wednesday','thursday', 'friday']
    day= input('which day? : ').lower()
    while day not in days:
        print('The day name is incorrect!:')
        day= input('Please entre (saturday sunday .......... friday or all: ').lower()

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
    # load my data from previous data
    df= pd.read_csv(CITY_DATA[city])

    #to convert the start time column to datetime by to_datetime fun
    df['Start Time']= pd.to_datetime(df['Start Time'])

    # make tow new columns contain month & day_of_week and hour
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour']= df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """
    Displays statistics on
    the most frequent times
    of travel.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    com_month = df['month'].mode()[0]
    print('The most common month is :',com_month)


    # TO DO: display the most common day of week
    com_day = df['day_of_week'].mode()[0]
    print('The most common day is :', com_day)


    # TO DO: display the most common start hour
    comm_hour = df['hour'].mode()[0]
    print('The most common hour is :',comm_hour )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics
    on the most popular
    stations and trip.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    com_start_station = df['Start Station'].mode()[0]
    count_1 = df['Start Station'].value_counts()[0]
    print('The common used start station is :', com_start_station , '    its number = ', count_1)

    # TO DO: display most commonly used end station
    print('The common used End station is :', df['End Station'].mode()[0], '      its number = ',df['End Station'].value_counts()[0]) # Directly printed withot varible assignment

    # TO DO: display most frequent combination of start station and end station trip
    combination_start_end = (df['Start Station'] + df['End Station']).mode()[0]
    count_2 =(df['Start Station'] + df['End Station']).value_counts()[0]
    print('The most frequent combination of Start & End station is :', combination_start_end,'\n its number = ',count_2)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_duration_hours = df['Trip Duration'].sum()/3600 # I have no idea about what the unit of time shoud be displayed , so I set time as hours
    print('Totla duratin is =',Total_duration_hours,"hours" )

    # TO DO: display mean travel time
    Mean_travel_time = df['Trip Duration'].mean()/3600
    print('The mean of trip time =', Mean_travel_time ,"hours" )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    Users_type = df['User Type'].value_counts()
    print(f'The count of user type is\n :{Users_type}')

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('\n The count of gender\n', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('\nThe earliest birth day =',int(df['Birth Year'].min()))
        print('\nThe most recent birth day =',int(df['Birth Year'].max()))
        print('\nThe common birth day =',int(df['Birth Year'].mode()))
    else:
        print('Ohh, no birth year in this dataset !!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def disply_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data == 'no':
         print(df.iloc[0:5])
         start_loc += 5
         view_data = input("Do you wish to continue?: ").lower()
         if view_data == 'no':
             break


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        disply_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
