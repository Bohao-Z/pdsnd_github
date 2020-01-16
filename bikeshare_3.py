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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter City; ')  # input city
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('Please try again: ') # check and re-input

    # get user input for month (all, january, february, ... , june)
    month = input('Enter Month: ') # input month
    while month.lower() not in ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 
                        'august', 'september', 'october', 'november', 'december']:
        month = input('Please try again: ') # check and re-input

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter Day: ')  # input day
    while day.lower() not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('Please try again:') # check and re-input

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
    month_data = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 
                        'august': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    city_data = { 'chicago': 'chicago.csv', 'new york': 'new_york_city.csv', 
                 'washington': 'washington.csv' }
    weekday_data = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4,
                'saturday': 5, 'sunday': 6}
    df = pd.read_csv(city_data[city.lower()])
    if month.lower() != 'all':
        df = df[pd.to_datetime(df['Start Time']).apply(lambda x: x.month) == month_data[month.lower()]]
    if day.lower() != 'all':
        df = df[pd.to_datetime(df['Start Time']).apply(lambda x: x.weekday()) == weekday_data[day.lower()]]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_data = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 
                  8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    month = pd.to_datetime(df['Start Time']).apply(lambda x: x.month).value_counts().idxmax()
    print('Month: ', month_data[month])

    # display the most common day of week
    weekday_data = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday',
                    5: 'Saturday', 6: 'Sunday'}
    weekday = pd.to_datetime(df['Start Time']).apply(lambda x: x.weekday()).value_counts().idxmax()
    print('Weekday: ', weekday_data[weekday])

    # display the most common start hour
    hour = pd.to_datetime(df['Start Time']).apply(lambda x: x.hour).value_counts().idxmax()
    print('Hour: ',hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Start station: ', df['Start Station'].value_counts().idxmax())


    # display most commonly used end station
    print('End station: ', df['End Station'].value_counts().idxmax())


    # display most frequent combination of start station and end station trip
    station = (df['Start Station'] + '?' + df['End Station']).value_counts().idxmax().split('?')
    print('Combination of start station and end station: ',station[0], ',', station[1])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time: ',np.sum(pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])))
    
    
    # display mean travel time
    print('Mean travel time: ',np.mean(pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())


    # Display counts of gender
    print(df['Gender'].value_counts())


    # Display earliest, most recent, and most common year of birth
    print('Earliest year of birth: ', int(df['Birth Year'].min()))
    print('Most recent year of birth: ', int(df['Birth Year'].max()))
    print('Most common year of birth: ', int(df['Birth Year'].value_counts().idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
