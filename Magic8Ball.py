#Magic8Ball.py
#Name: Salsabiel Khair Allah
#Date: Sep.6
#Assignment: Lab 2

#We will need random for this program, import to use this package.
#datetime will allow us to access the system date and time
import datetime
import random

def main():
    #getting current time from system, storing to variable
    now = datetime.datetime.now()
    currentHour = now.hour
    currentMinute = now.minute

    #(we don’t actually need the time for the Magic 8 Ball, but template requires it)
    print("Current time:", currentHour, ":", currentMinute)

    #Magic 8 Ball responses
    answers = [
      "As I see it, yes.",
      "Ask again later.",
      "Better not tell you now.",
      "Cannot predict now.",
      "Concentrate and ask again.",
      "Don’t count on it.",
      "It is certain.",
      "It is decidedly so.",
      "Most likely.",
      "My reply is no.",
      "My sources say no.",
      "Outlook not so good.",
      "Outlook good.",
      "Reply hazy, try again.",
      "Signs point to yes.",
      "Very doubtful.",
      "Without a doubt.",
      "Yes.",
      "Yes – definitely.",
      "You may rely on it."
    ]

    #Ask user for a question
    question = input("Ask the Magic 8 Ball a question: ")

    #Get random response
    response = random.choice(answers)

    #Output result
    print("Magic 8 Ball says:", response)


if __name__ == '__main__':
    main()
