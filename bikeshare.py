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
    city=input('\n please enter the city ...').lower()
    while city not in CITY_DATA.keys():
        
        if city.lower() == 'chicago':
            city=pd.read_csv('chicago.csv') 
        elif city.lower() == 'new york':
            city=pd.read_csv('new_york_city.csv')
        elif city.lower() == 'washington':
            city=pd.read_csv('washington.csv')
        else:
            print("enter correct answer")
            city=input('\n please enter the city ...').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    Month = {'january', 'febreuary', 'march', 'april', 'may', 'june',"all"}
    # month=''
    month=input("please enter month from jan to june ..\n")
    while month not in Month:
      print("enter correct answer")
      month=input("please enter month from jan to june ..\n")
        
       
    
                  

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    Day = {"sunday", "monday", "tuesday", "wednesday", "thursday", "friday", 'saturday','all'}
    day=input("enter the day..\n")
    while day not in Day:
        print('enter correct answer')
        day=input("enter the day..\n")
        
        
        


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
    df =pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        Month = ['january', 'february', 'march', 'april', 'may', 'june','all']
        month = Month.index(month) + 1
       
    
        

    # filter by day
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    pop_month =df['month'].mode()[0]
    print("popular month :",pop_month)
    

    # TO DO: display the most common day of week
    pop_day = df['day_of_week'].mode()[0]
    print("popular day is :",pop_day)

    # TO DO: display the most common start hour
    pop_hour = df['hour'].mode()[0]
    print("popular hour is:", pop_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station =df['Start Station'].mode()[0]
    print('common start station : ',common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('common end station :',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]


    print(f"\nThe most frequent combination of trips are from {combo}.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print("total duration",total_duration)
    
    # TO DO: display mean travel time
    mean_of_Trip=df['Trip Duration'].mean()
    print("mean is :",mean_of_Trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print("user type is :{}".format(user_type))

    # TO DO: Display counts of gender
    try:
     gender = df['Gender'].value_counts()
     print(f"gender is :{gender}")

    

    
    # TO DO: Display earliest, most recent, and most common year of birth
    
     earliest = df['Birth Year'].min()
     recent = df['Birth Year'].max()
     common_year = df['Birth Year'].mode()[0]
     print("\nThe earliest : ",earliest, "\n\nThe most recent : ",recent ,"\n\nThe most common: ",common_year)
    except:
      print("")

    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    # print(df)
def display_raw_data(df):
    """The fuction takes the name of the city produced by the get_filters fuction as input and returns the raw data of that city as chunks of 5 rows based upon user input.
    """

    print('\nRaw data is available to check... \n')

    # setting counter for the rows 
    start_loc = 0

    # collecting user input
    display_opt = input('To View the availbale raw data in chuncks of 5 rows type: Yes \n').lower()

   # Validating user input
    while display_opt not in ['yes', 'no']:
        print('That\'s invalid choice, pleas type yes or no')
        display_opt = input('To View the availbale raw data in chuncks of 5 rows type: Yes \n').lower()

    # action based on yes 
    while display_opt == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc+=5
        display_opt = input('Do you want to display 5 more rows? yes or no: ').lower()

   # action based on no
    if display_opt == 'no':
        print('\nExiting..')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # print(city, month, day, "\n")
        # print(df.head())
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
