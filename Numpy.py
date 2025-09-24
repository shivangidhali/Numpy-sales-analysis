#Numpy simple project
#Step...1, Setup and generating data
import numpy as np
np.random.seed (42)
daily_sales = np.random.randint(150, 501, size = 31)
print("Generated daily sales data :")
print(daily_sales)

#Step....2, Basic statistical Analysis EDA
mean_sales = np.mean(daily_sales)
median_sales = np.median(daily_sales)
std_sales = np.std(daily_sales)
min_sales = np.min(daily_sales)
max_sales = np.max(daily_sales)
print("\n daily sales statistical")
print(f"average daily sales :{mean_sales:.2f}")
print(f"median daily sales :{median_sales:.2f}")
print(f"standard deviation :{std_sales:.2f}")
print(f"minimum sales :{min_sales}")
print(f"maximum sales :{max_sales}")

#step....3, Data filtering and insights
# Ques 1- Show the count of days with above average sales
# Ques 2- show the sales of days with above average sales
high_sales_days_data = daily_sales[daily_sales > mean_sales]
print("\n High performing days")
print(f"count of days with above average sales :{len(high_sales_days_data)}")
print(f"that days sales:{high_sales_days_data}")

#Ques 4- Show the count of target sales days (Target sales is 400 between 450)
#Ques 5- Show the Target sales of that days.

target_sales_days = daily_sales[(daily_sales >= 400) & (daily_sales <= 450)]
print("\n sales between 400 & 450")
print(f"count of days in Target range:{len(target_sales_days)}")
print(f"sales of that days:{target_sales_days}")

# Step....4, Data Transformation and Aggregations
# Devide all sales day week wise
sales_for_reshaping = daily_sales[: 28]
weekly_sales_data = sales_for_reshaping.reshape(4, 7)
print("\n weekly sales data")
print(weekly_sales_data)

#Show week wise total sales
weekly_totals = np.sum(weekly_sales_data, axis = 1)
print("\n weekly totals")
print(f"Total sales of 4 weeks: {weekly_totals}")
