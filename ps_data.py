def add_preference(preferences, category, value):
    preferences = {
        "name": "My Name",
        "is_morning_person": True,
        "is_night_owl": True,
        "fav_song_title": None,
        "num_of_household_members": 1
    }
    preferences.update({category: value})
    print(preferences)
    return preferences
add_preference({},"test cat", "test val")

#  solution did not want to update the dictionary, only return the new entry
def add_preference(preferences, category, value):
    preferences[category] = value
    return preferences