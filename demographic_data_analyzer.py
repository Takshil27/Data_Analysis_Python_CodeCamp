import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/TAKSHIL/Downloads/US_Adult_Income_1617_1.csv")

# Number of people of each race
race_count = df['race'].value_counts()
print("Number of people of each race:")
print(race_count)

# Average age of men
average_age_men = df[df['sex'] == 'Male']['age'].mean()
print("\nAverage age of men:", average_age_men)

# Percentage of people with Bachelor's Degree
total_people = len(df)
bachelors_count = (df['education'] == 'Bachelors').sum()
percentage_bachelors = (bachelors_count / total_people) * 100
print("\nPercentage of people with Bachelor's Degree:", percentage_bachelors)

# Percentage of people with advanced education (>50K)
advanced_education = ['Bachelors', 'Masters', 'Doctorate']
adv_edu_df = df[df['education'].isin(advanced_education)]
adv_edu_rich = adv_edu_df[adv_edu_df['salary'] == '>50K']
percentage_adv_edu_rich = (len(adv_edu_rich) / len(adv_edu_df)) * 100
print("\nPercentage with advanced education earning >50K:", percentage_adv_edu_rich)

# Percentage of people without advanced education earning >50K
non_adv_edu_df = df[~df['education'].isin(advanced_education)]
non_adv_edu_rich = non_adv_edu_df[non_adv_edu_df['salary'] == '>50K']
percentage_non_adv_edu_rich = (len(non_adv_edu_rich) / len(non_adv_edu_df)) * 100
print("\nPercentage without advanced education earning >50K:", percentage_non_adv_edu_rich)

# Minimum number of hours worked per week
min_hours = df['hours-per-week'].min()
print("\nMinimum hours worked per week:", min_hours)

# Percentage of people who work minimum hours and earn >50K
min_workers = df[df['hours-per-week'] == min_hours]
rich_min_workers = min_workers[min_workers['salary'] == '>50K']
rich_percentage_min_workers = (len(rich_min_workers) / len(min_workers)) * 100
print("\nPercentage of people working minimum hours earning >50K:", rich_percentage_min_workers)

# Country with highest percentage of people earning >50K
country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack().fillna(0)
highest_earning_country = (country_salary['>50K'] * 100).idxmax()
highest_percentage = (country_salary['>50K'] * 100).max()
print("\nCountry with highest percentage of >50K earners:", highest_earning_country)
print("Highest percentage:", highest_percentage)

# Most popular occupation for those earning >50K in India
india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
most_popular_occupation_india = india_rich['occupation'].value_counts().idxmax()
print("\nMost popular occupation for >50K earners in India:", most_popular_occupation_india)
ss
