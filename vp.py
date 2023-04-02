user_data = {
    "friends": [
        {
            "watched": [
                {
                    "genre": "Fantasy",
                    "host": "netflix",
                    "rating": 4.8,
                    "title": "The Lord of the Functions: "
                    "The Fellowship of the "
                    "Function",
                },
                {
                    "genre": "Fantasy",
                    "host": "amazon",
                    "rating": 4.0,
                    "title": "The Lord of the Functions: " "The Return of the Value",
                },
                {
                    "genre": "Fantasy",
                    "host": "hulu",
                    "rating": 4.0,
                    "title": "The Programmer: An " "Unexpected Stack Trace",
                },
                {
                    "genre": "Horror",
                    "host": "netflix",
                    "rating": 3.5,
                    "title": "It Came from the Stack " "Trace",
                },
            ]
        },
        {
            "watched": [
                {
                    "genre": "Fantasy",
                    "host": "netflix",
                    "rating": 4.8,
                    "title": "The Lord of the Functions: "
                    "The Fellowship of the "
                    "Function",
                },
                {
                    "genre": "Fantasy",
                    "host": "hulu",
                    "rating": 4.0,
                    "title": "The Programmer: An " "Unexpected Stack Trace",
                },
                {
                    "genre": "Action",
                    "host": "amazon",
                    "rating": 2.2,
                    "title": "The JavaScript and the " "React",
                },
                {
                    "genre": "Intrigue",
                    "host": "hulu",
                    "rating": 2.0,
                    "title": "Recursion",
                },
                {
                    "genre": "Intrigue",
                    "host": "disney+",
                    "rating": 3.0,
                    "title": "Zero Dark Python",
                },
            ]
        },
    ],
    
    "subscriptions": ["netflix", "hulu"],
    
    "watched": [
        {
            "genre": "Fantasy",
            "host": "netflix",
            "rating": 4.8,
            "title": "The Lord of the Functions: The Fellowship of " "the Function",
        },
        {
            "genre": "Fantasy",
            "host": "netflix",
            "rating": 4.0,
            "title": "The Lord of the Functions: The Two " "Parameters",
        },
        {
            "genre": "Fantasy",
            "host": "amazon",
            "rating": 4.0,
            "title": "The Lord of the Functions: The Return of the " "Value",
        },
        {
            "genre": "Action",
            "host": "amazon",
            "rating": 2.2,
            "title": "The JavaScript and the React",
        },
        {"genre": "Intrigue", "host": "hulu", "rating": 2.0, "title": "Recursion"},
        {
            "genre": "Intrigue",
            "host": "disney+",
            "rating": 4.5,
            "title": "Instructor Student TA Manager",
        },
    ],
}


# ========================================= wave 05- # 1.  get_new_rec_by_genre ========== SJ

# def get_new_rec_by_genre(user_data):
#     watched = user_data["watched"]
#     if not watched: return []

#     fave_genre = get_most_watched_genre(user_data)
#     friend_movies = get_friend_movies(user_data)

#     recommended_movies = []
#     for movie in friend_movies:
#         if movie not in watched and movie["genre"] == fave_genre: 
#             recommended_movies.append(movie)
#     return recommended_movies



# ========================================= wave 05- # 2. get_rec_from_favorites ========== SJ


# def get_rec_from_favorites(user_data):
#     favorites = user_data["favorites"]
#     if not favorites: return []

#     friend_movies = get_friend_movies(user_data)
    
#     recommended_movies = []
#     for movie in favorites:
#         if movie not in friend_movies: recommended_movies.append(movie)
#     return recommended_movies