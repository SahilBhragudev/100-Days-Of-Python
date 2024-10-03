def life_in_weeks(age):
    print(f"Your age is {age}")
    current_age_in_weeks = age * 52
    print(f"Current Age in weeks is {current_age_in_weeks}")
    max_age_in_weeks = 90 * 52
    time_left = max_age_in_weeks - current_age_in_weeks
    print(f"Time left to live is {time_left}")
          
life_in_weeks(20)