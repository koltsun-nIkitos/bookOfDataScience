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


print(num_friends_by_id)
