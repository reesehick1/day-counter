# def run_full_code():
#variables
notable_event = 0
notable_current = 0
gap_years = 0
gap_months = 0
gap_days = 0
month_gap = 1
month_index = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

#notable event
month = int(input("month of notable event as (00): "))
days = int(input("day of notable event as (00): "))
year = int(input("year of notable event as (0000): "))

if month <= 12:
    months = month_index[0:month - 1]
    for i in months:
        notable_event = notable_event + i
if days >= 1:
    notable_event = notable_event + days
if year >= 1:
    for i in range(year):
        notable_event = notable_event + 365

#current event
month_current = int(input("what is the current month as (00): "))
days_current = int(input("what is the current day as (00): "))
year_current = int(input("what is the current year as (0000): "))

if month_current <= 12:
    months_current = month_index[0:month_current - 1]
    for i in months_current:
        notable_current = notable_current + i
if days_current >= 1:
    notable_current = notable_current + days_current
if year_current >= 1:
    for i in range(year_current):
        notable_current = notable_current + 365

#times separate
print(notable_event)
print(notable_current)
time_since = notable_current - notable_event

#times together
'''print("it has been" + {str(time_since)})'''

#math for amount of time in years 
while time_since >= 365:
    gap_years = gap_years + 1 
    time_since = time_since - 365

#adding months
for i in range(12):
    if time_since >= month_index[0:month_gap]:
        gap_months = gap_months + 1
        month_gap = month_gap + 1

#adding days
gap_days = gap_days + time_since

print("The amount of time that has passed since the notable event is as "
    "(MM,DD,YYYY):")
print({gap_months} + {gap_days} + {gap_years})

# #code to run multiple times
# run_agian = input("would you like to run it again? y/n")

# if run_agian == "y":
#     run_full_code()
# elif run_agian == "n":
#     print("Thank you, have a good day")
# else:
#     print("ERROR")