'''
1.Creating and using a DatetimeIndex
'''
# Prepare a format string: time_format
time_format = '%Y-%m-%d %H:%M'

# Convert date_list into a datetime object: my_datetimes
my_datetimes = pd.to_datetime(date_list, format = time_format)

# Construct a pandas Series using temperature_list and my_datetimes: time_series
time_series = pd.Series(temperature_list, index=my_datetimes)

'''
2.Partial string indexing and slicing
'''
# Extract the hour from 9pm to 10pm on '2010-10-11': ts1
ts1 = ts0.loc['2010-10-11 21:00:00']

In [1]: ts1
Out[1]: 69.0

# Extract '2010-07-04' from ts0: ts2
ts2 = ts0.loc['2010-07-04']

In [2]: ts2
Out[2]:
Date
2010-07-04 00:00:00    77.6
2010-07-04 01:00:00    76.3
2010-07-04 02:00:00    75.5
2010-07-04 03:00:00    74.9
2010-07-04 04:00:00    74.6
2010-07-04 05:00:00    74.2
2010-07-04 06:00:00    74.4
2010-07-04 07:00:00    76.0
2010-07-04 08:00:00    79.0
2010-07-04 09:00:00    81.8
2010-07-04 10:00:00    84.6
2010-07-04 11:00:00    86.8
2010-07-04 12:00:00    88.9
2010-07-04 13:00:00    90.1
2010-07-04 14:00:00    91.1
2010-07-04 15:00:00    91.6
2010-07-04 16:00:00    91.5
2010-07-04 17:00:00    90.7
2010-07-04 18:00:00    89.5
2010-07-04 19:00:00    87.3
2010-07-04 20:00:00    84.0
2010-07-04 21:00:00    81.8
2010-07-04 22:00:00    80.0
2010-07-04 23:00:00    78.5
Name: Temperature, dtype: float64

# Extract data from '2010-12-15' to '2010-12-31': ts3
ts3 = ts0.loc['2010-12-15':'2010-12-31']

In [3]: ts3
Out[3]:
Date
2010-12-15 00:00:00    48.0
2010-12-15 01:00:00    47.2
2010-12-15 02:00:00    46.5
2010-12-15 03:00:00    46.0
2010-12-15 04:00:00    45.6
2010-12-15 05:00:00    45.3
2010-12-15 06:00:00    45.6
2010-12-15 07:00:00    45.0
2010-12-15 08:00:00    45.8
2010-12-15 09:00:00    49.1
2010-12-15 10:00:00    52.2
2010-12-15 11:00:00    54.9
2010-12-15 12:00:00    57.2
2010-12-15 13:00:00    58.9
2010-12-15 14:00:00    60.2
2010-12-15 15:00:00    60.9
2010-12-15 16:00:00    60.5
2010-12-15 17:00:00    59.1
2010-12-15 18:00:00    55.8
2010-12-15 19:00:00    52.5
2010-12-15 20:00:00    50.7
2010-12-15 21:00:00    49.6
2010-12-15 22:00:00    48.6
2010-12-15 23:00:00    47.7
2010-12-16 00:00:00    47.6
2010-12-16 01:00:00    46.7
2010-12-16 02:00:00    46.1
2010-12-16 03:00:00    45.6
2010-12-16 04:00:00    45.2
2010-12-16 05:00:00    44.8
                       ...
2010-12-30 18:00:00    54.1
2010-12-30 19:00:00    50.9
2010-12-30 20:00:00    49.0
2010-12-30 21:00:00    47.9
2010-12-30 22:00:00    46.9
2010-12-30 23:00:00    46.1
2010-12-31 00:00:00    46.1
2010-12-31 01:00:00    44.5
2010-12-31 02:00:00    44.1
2010-12-31 03:00:00    43.7
2010-12-31 04:00:00    43.5
2010-12-31 05:00:00    42.9
2010-12-31 06:00:00    43.0
2010-12-31 07:00:00    42.2
2010-12-31 08:00:00    42.5
2010-12-31 09:00:00    46.0
2010-12-31 10:00:00    49.4
2010-12-31 11:00:00    52.4
2010-12-31 12:00:00    54.7
2010-12-31 13:00:00    56.9
2010-12-31 14:00:00    58.2
2010-12-31 15:00:00    58.8
2010-12-31 16:00:00    58.8
2010-12-31 17:00:00    57.6
2010-12-31 18:00:00    54.3
2010-12-31 19:00:00    51.1
2010-12-31 20:00:00    49.0
2010-12-31 21:00:00    47.9
2010-12-31 22:00:00    46.9
2010-12-31 23:00:00    46.2
Name: Temperature, dtype: float64

'''
3.Reindexing the Index
'''
# Reindex without fill method: ts3
'''### Create a new time series ts3 by reindexing ts2 with the index of ts1 '''
ts3 = ts2.reindex(ts1.index)

In [2]: ts3
Out[2]:
2016-07-01     0.0
2016-07-02     NaN
2016-07-03     NaN
2016-07-04     1.0
2016-07-05     2.0
2016-07-06     3.0
2016-07-07     4.0
2016-07-08     5.0
2016-07-09     NaN
2016-07-10     NaN
2016-07-11     6.0
2016-07-12     7.0
2016-07-13     8.0
2016-07-14     9.0
2016-07-15    10.0
2016-07-16     NaN
2016-07-17     NaN
dtype: float64

# Reindex with fill method, using forward fill: ts4
ts4 = ts2.reindex(ts1.index,method='ffill')

In [2]: ts4
Out[2]:
2016-07-01     0
2016-07-02     0
2016-07-03     0
2016-07-04     1
2016-07-05     2
2016-07-06     3
2016-07-07     4
2016-07-08     5
2016-07-09     5
2016-07-10     5
2016-07-11     6
2016-07-12     7
2016-07-13     8
2016-07-14     9
2016-07-15    10
2016-07-16    10
2016-07-17    10
dtype: int64

# Combine ts1 + ts2: sum12
sum12 = ts1 + ts2

# Combine ts1 + ts3: sum13
sum13 = ts1 + ts3

# Combine ts1 + ts4: sum14
sum14 = ts1 + ts4

'''
4. Resampling and frequency
'''
# Downsample to 6 hour data and aggregate by mean: df1
df1 = df['Temperature'].resample('6h').mean()

# Downsample to daily data and count the number of data points: df2
df2 = df['Temperature'].resample('D').count()

print(df1)
print(df2)

'''
### 5. Separating and resampling
'''
'''### Extract temperature data for August: august '''
august = df['Temperature']['2010-August']

# Downsample to obtain only the daily highest temperatures in August: august_highs
august_highs = august.resample('D').max()

'''### Extract temperature data for February: february '''
february = df['Temperature']['2010-Feb']

# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('D').min()

'''
 6. Rolling mean and frequency
### Rolling means (or moving averages) are generally used to smooth out short-term fluctuations in time series data and highlight long-term trends.
'''
# Extract data from 2010-Aug-01 to 2010-Aug-15: unsmoothed
unsmoothed = df['Temperature']['2010-08-01':'2010-08-15']

'''### Apply a rolling mean with a 24 hour window: smoothed'''
smoothed = unsmoothed.rolling(window=24).mean()

# Create a new DataFrame with columns smoothed and unsmoothed: august
august = pd.DataFrame({'smoothed':smoothed, 'unsmoothed':unsmoothed})

# Plot both smoothed and unsmoothed data using august.plot().
august.plot()
plt.show()

'''
7. Resample and roll with it
'''
# Extract the August 2010 data: august
august = df['Temperature']['2010-08']

# Resample to daily data, aggregating by max: daily_highs
daily_highs = august.resample('D').max()

# Use a rolling 7-day window with method chaining to smooth the daily high temperatures in August
daily_highs_smoothed = daily_highs.rolling(window=7).mean()
print(daily_highs_smoothed)

<script.py> output:
    Date
    2010-08-01          NaN
    2010-08-02          NaN
    2010-08-03          NaN
    2010-08-04          NaN
    2010-08-05          NaN
    2010-08-06          NaN
    2010-08-07    95.114286
    2010-08-08    95.142857
    2010-08-09    95.171429
    2010-08-10    95.171429
    2010-08-11    95.157143
    2010-08-12    95.128571
    2010-08-13    95.100000
    2010-08-14    95.042857
    2010-08-15    94.971429
    2010-08-16    94.900000
    2010-08-17    94.857143
    2010-08-18    94.828571
    2010-08-19    94.814286
    2010-08-20    94.785714
    2010-08-21    94.757143
    2010-08-22    94.742857
    2010-08-23    94.714286
    2010-08-24    94.642857
    2010-08-25    94.542857
    2010-08-26    94.428571
    2010-08-27    94.271429
    2010-08-28    94.100000
    2010-08-29    93.914286
    2010-08-30    93.742857
    2010-08-31    93.571429
    Freq: D, Name: Temperature, dtype: float64

'''
8. Method chaining and filtering
'''
# Strip extra whitespace from the column names: df.columns
df.columns = df.columns.str.strip()

# Extract data for which the destination airport is Dallas: dallas
dallas = df['Destination Airport'].str.contains('DAL')

# Compute the total number of Dallas departures each day: daily_departures
'''### calling count() and sum() has major difference'''
daily_departures = dallas.resample('D').sum()

# Generate the summary statistics for daily Dallas departures: stats
stats = daily_departures.describe()

'''
9. Missing values and interpolation
'''
# Reset the index of ts2 to ts1, and then use linear interpolation to fill in the NaNs: ts2_interp
ts2_interp = (ts2.reindex(ts1.index)).interpolate(how='linear')

# Compute the absolute difference of ts1 and ts2_interp: differences
'''### warning: not (ts1-ts2_interp).np.abs()'''
differences = np.abs(ts1-ts2_interp)

# Generate and print summary statistics of the differences
print(differences.describe())

<script.py> output:
    count    17.000000
    mean      2.882353
    std       1.585267
    min       0.000000
    25%       2.000000
    50%       2.666667
    75%       4.000000
    max       6.000000
    dtype: float64

'''
10. Time zones and conversion
'''
# Buid a Boolean mask to filter out all the 'LAX' departure flights: mask
mask = df['Destination Airport'] == 'LAX'

# Use the mask to subset the data: la
la = df[mask]

# Combine two columns of data to create a datetime series: times_tz_none
times_tz_none = pd.to_datetime( la['Date (MM/DD/YYYY)'] + ' ' + la['Wheels-off Time'] )

# Localize the time to US/Central: times_tz_central
'''### attempt: times_tz_central = Series.dt.tz_localize(times_tz_none,'US/Central' )'''

times_tz_central = times_tz_none.dt.tz_localize('US/Central')

# Convert the datetimes from US/Central to US/Pacific
'''### attempt: times_tz_pacific = times_tz_central.dt.tz_convert('US/Central','US/Pacific')'''

times_tz_pacific = times_tz_central.dt.tz_convert('US/Pacific')

'''
11. Plotting time series, datetime indexing
'''
# Plot the raw data before setting the datetime index
df.plot()
plt.show()

# Convert the 'Date' column into a collection of datetime objects: df.Date
df.Date = pd.to_datetime(df.Date)

# Set the index to be the converted 'Date' column
'''### Inside the .set_index() method, you have to specify the column you want to use as the index - in this case, the 'Date' column.'''
df.set_index('Date',inplace=True)

# Re-plot the DataFrame to see that the axis is now datetime aware!
df.plot()
plt.show()

'''
12. Plotting date ranges, partial indexing
'''
# Plot the summer data
df.Temperature['2010-Jun':'2010-Aug'].plot()
plt.show()
plt.clf()

# Plot the one week data
df.Temperature['2010-06-10':'2010-06-17'].plot()
plt.show()
plt.clf()

df.Temperature['May 2010'].head()
