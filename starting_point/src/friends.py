def get_name(person):
    return person["name"]


def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]


def likes_to_eat(person, type_of_food):
    for snack in person["favourites"]["snacks"]:
        if snack == type_of_food:
            return True
    return False


def add_friend(person, friend):
    person["friends"].append(friend)


def remove_friend(person, friend):
    friend_index = person["friends"].index(friend)
    person["friends"].pop(friend_index)


def total_money(people):
    money = 0
    for person in people:
        money += person["monies"]
    return money


def l_money(lender, lendee, money):
    lender["monies"] -= money
    lendee["monies"] += money


def all_favourite_foods(list):
    favourite_foods = []
    for person in list:
        for snack in person["favourites"]["snacks"]:
            favourite_foods.append(snack)
    return favourite_foods


def find_no_friendends(list):
    people_with_no_friends = []
    for person in list:
        if len(person["friends"]) == 0:
            people_with_no_friends.append(person)
    return people_with_no_friends