from random import randint

from faker import Faker
from faker.generator import random


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_recipe():
    return {
        'id': random.randint(0, 600),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': random.randint(0,100),
        'preparation_time_unit': 'Minutos',
        'servings': random.randint(0,100),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time_between(start_date="-6y", end_date="now"),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': random.choice(
                ["Café da manhã", "Almoço", "Jantar", "Lanche"]
                )
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }
    }



if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())
