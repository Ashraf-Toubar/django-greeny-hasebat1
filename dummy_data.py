'''
1
    1 : python + sqlite
    2 : python + orm
    
'''

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()


from products.models import Product, Brand, Category
import random
from faker import Faker 

def seed_category(n):
    fake = Faker()
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg','6.jpg', '7.jpg']
    
    for _ in range(n):
        name = fake.name()
        image = f"category/{images[random.randint(0, 6)]}"
        Category.objects.create(
            name = name,
            image = image,
        )
    
    print(f'Suuccessfully Seeded {n} Category')
    
    
def seed_brand(n):
    fake = Faker()
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg','6.jpg', '7.jpg']
    
    for _ in range(n):
        name = fake.name()
        image = f"category/{images[random.randint(0, 6)]}"
        Brand.objects.create(
            name = name,
            image = image,
            category = Category.objects.get(id=random.randint(1, 10)),
        )
    print(f'Suuccessfully Seeded {n} Brand')
     

def seed_products(n):
    fake = Faker()
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg','6.jpg', '7.jpg','8.jpg']
    flag_type = ['New', 'Feature', 'Sale']
    
    for _ in range(n):
        name = fake.name()
        subtitle = fake.text(max_nb_chars=500)
        sku = random.randint(1000, 100000)
        description = fake.text(max_nb_chars=10000)
        price = round(random.uniform(20.99, 99.99),2)
        image = f"products/{images[random.randint(0, 7)]}"
        flag = flag_type[random.randint(0, 2)]
        quantity = random.randint(1, 100)
       
        Product.objects.create(
            name = name,
            subtitle = subtitle,
            sku = sku,
            desc = description,
            price = price,
            image = image,
            flag = flag,
            quantity = quantity,
            brand = Brand.objects.get(id=random.randint(1, 10)),
            category = Category.objects.get(id=random.randint(1, 10))
            )
    print(f'Successfully Seeded {n} Product')

#seed_category(10)
#seed_brand(10)
seed_products(1000)