def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    likes_food = False
    for snack in person["favourites"]["snacks"]:
        if snack == food:
            likes_food = True
        else:
            likes_food = False
    return likes_food