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
    # TO DO: get user input for city (chicago, new york city, or  washington). HINT: Use a while loop to handle invalid inputs
    
    city = input("Please enter a city name (Chicago, New York City, or Washington): ").lower()
    while city not in ["chicago", "new york city", "washington"]:
        print("Invalid input.")
        city = input("Please enter a valid city name: ").lower()
    print(city)

    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = input("Please enter a month (January, February, March, April, May, June, or enter 'all'): ").lower()
    while month not in ["january", "february", "march", "april", "may", "june", "all"]:
        print("Invalid input.")
        month = input("Please enter a valid month: ").lower()
    print(month)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input("Please enter a day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or enter 'all'): ").lower()
    while day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
        print("Invalid input.")
        month = input("Please enter a valid day: ").lower()
    print(day)


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
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    df["month"] = df['Start Time'].dt.month
    print("Most common month is", df["month"].mode()[0])
    
    
    # TO DO: display the most common day of week
    
    df["day_of_week"] = df['Start Time'].dt.day_name()
    print("Most common day is", df["day_of_week"].mode()[0])


    # TO DO: display the most common start hour
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most comon Start Hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most common start station is ", most_common_start_station)
    


    # TO DO: display most commonly used end station
    
    most_common_end_station = df['End Station'].mode()[0]
    print("Most common end station is ", most_common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    
    df["trip"] = df['Start Station'] + " to " + df['End Station']
    print("Most frequent combination of start station and end station trip is ", df["trip"].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_time = df["Trip Duration"].sum()
    print("Total trip duration is ", total_time/3600)


    # TO DO: display mean travel time
    
    avarage_time = df["Trip Duration"].mean()
    print("Avarage of trip duration is ", avarage_time/3600)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    print("Users count: \n", df["User Type"].value_counts())


    # TO DO: Display counts of gender
    
    if "Gender" in df.columns:
        print("Gender count: \n", df["Gender"].value_counts())
    else:
        print("Gender column is not found.")


    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_birth_year = int(df["Birth Year"].min())
        print("\n Earliest birth year is ", earliest_birth_year)
        recent_birth_year = int(df["Birth Year"].max())
        print("\n Recent birth year is ", recent_birth_year)       
        common_birth_year = int(df["Birth Year"].mode())
        print("\n Most common birth year is ", common_birth_year)
    else:
        print("Birth year column is not found.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_raw_data(df):
    """Displays raw data as per user input."""
    
    i = 0
    answer = input("Would you like to display 5 lines of raw data? Enter yes or no.\n").lower()
    pd.set_option("display.max_columns",None)

    while True:
        if answer == "no":
            break
        print(df[i:i+5])
        answer = input("Would you like to display another 5 lines of raw data? Enter yes or no.\n").lower()
        i += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
