#FutureTime.py
#Name: Salsabiel Khair Allah
#Date: Sep.6
#Assignment: Lab 2

#datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print(currentHour, currentMinute) # this is just for checking, can be removed later

  #Ask user for hours
  add_hours = int(input("Enter number of hours to add: "))

  #Ask user for minutes
  add_minutes = int(input("Enter number of minutes to add: "))

  #Calculate total minutes and handle overflow
  total_minutes = currentMinute + add_minutes
  futureMinute = total_minutes % 60
  extra_hours = total_minutes // 60

  #Calculate total hours and handle overflow (24-hour format)
  total_hours = currentHour + add_hours + extra_hours
  futureHour = total_hours % 24

  #Output the future time in standard format "HH:MM"
  print("Future time:", f"{futureHour:02}:{futureMinute:02}")


if __name__ == '__main__':
  main()

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
