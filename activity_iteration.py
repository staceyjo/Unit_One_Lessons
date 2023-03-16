amandas_data = {
        "watched": [
            {"title": "Land Before Time"},
            {"title": "Spirited Away" },
        ],
        "friends": [
            { "watched": [
                    {"title": "Lord of the Rings"},
                    {"title": "Parasyte" }
                ]
            },
            {  "watched": [ 
					{"title": "Harry Potter"},
                    {"title": "Ready Player One" }
            	]
            }
        ]
    }

# Another solution:
#1. Print the friends list

friends_list = []
for friend in amandas_data["friends"]:
    friends_list.append(friend)

#2. Print each title value in the second dictionary of the friends list

for movie in friends_list[-1]["watched"]:
    print(movie["title"])

print(friends_list)