from collections import Counter
from collections import defaultdict

users = [
    { "id" : 0, "name" : "Hero" },
    { "id" : 1, "name" : "Dunn" },
    { "id" : 2, "name" : "Sue" },
    { "id" : 3, "name" : "Chi" },
    { "id" : 4, "name" : "Thor" },
    { "id" : 5, "name" : "Clive" },
    { "id" : 6, "name" : "Hicks" },
    { "id" : 7, "name" : "Devin" },
    { "id" : 8, "name" : "Kate" },
    { "id" : 9, "name" : "Klein" },
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

friendships2 = {user['id'] : [] for user in users}

# перебрать список и занести всех друзей
for i, j in friendships:
    friendships2[i].append(j)
    friendships2[j].append(i)


# Число друзей
def number_of_friends(user):
    """Сколько друзей есть у пользователя user?"""
    user_id = user["id"]
    friend_ids = friendships2[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users) # Суммарное число связей - 24

num_users = len(users) # Длина списка пользователей
avg_connections = total_connections / num_users # Среднее количество людей

# Создать список в формате (id пользователя, число друзей)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)


# Исследователи данных, которых вы должны знать
# Список id друзей пользователя user (Плохой вариант)
def foaf_ids_bad(user):
    # foaf означает друг друга
    return [foaf_id 
            for friend_id in friendships2[user["id"]]
            for foaf_id in friendships2[friend_id]]
    return [foaf["id"]
            for friend in users["friends"]
            for foaf in friend["friends"]]

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships2[user_id]
        for foaf_id in friendships2[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendships2[user_id]
    )

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "skipy"),
    (2, "numpy"), (2, "statmodels"), (2, "pandas"), 
    (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"), 
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intellegent"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

# Исследватели данных, которым нравится целевая тема target_interest
def data_dcientists_who_like(target_interest):
    """Отыскать id всех пользователей, которым нравится одна тема"""
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]

user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(
        interested_user_id 
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )


words_and_counts = Counter(word
                            for user, interest in interests
                            for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)