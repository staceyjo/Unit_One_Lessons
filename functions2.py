def get_daily_special(todays_date):
    current_season = get_season(todays_date)

    if current_season == "Spring":
        special = "Eggplants"
    elif current_season == "Summer":
        special = "Blueberres"
    elif current_season == "Fall":
        special = "Sweet Potatoes"
    else:
        special = "Oranges"

    day_of_week = get_day_of_week(todays_date)

    if day_of_week == "Saturday" or day_of_week == "Sunday":
        special = f"Weekend {special}"

    return special