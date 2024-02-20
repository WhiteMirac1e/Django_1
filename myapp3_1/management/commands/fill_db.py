from random import choices
from typing import Any

from django.core.management.base import BaseCommand, CommandParser
from myapp3_1.models import Author, Post

LOREM = """ipsum dolor sit amet consectetur adipisicing elit. Laboriosam voluptate debitis aspernatur repudiandae voluptas dolorem asperiores blanditiis similique. Pariatur animi fuga earum assumenda facere asperiores voluptas quo voluptates recusandae molestias?
Corporis, quaerat? Earum cupiditate nihil molestias quam facere culpa neque aut quis voluptatibus architecto vel saepe eligendi sit hic odio mollitia delectus, beatae praesentium consectetur accusantium? Libero accusamus veritatis quisquam.
Ratione veritatis ad odit, minus eligendi provident voluptatum, odio doloribus molestias dolores rem cum cupiditate! Provident vero, rerum ut error quam cupiditate saepe odit tempora quia amet dolore ullam numquam.
Eius voluptates ipsa iste, aliquid tenetur ad quam odit laboriosam earum officia culpa magnam laudantium minima maiores amet, sint cupiditate perspiciatis quibusdam. Voluptatem mollitia odit, inventore illo recusandae dolorem hic?
Enim molestias debitis officia non ullam itaque asperiores voluptatum quidem reiciendis earum commodi, pariatur dicta doloribus dignissimos dolorum libero harum nulla eligendi mollitia omnis nobis. Accusantium, repudiandae. Nemo, ut quisquam!
Dolor, vitae saepe quas sequi cumque alias labore corporis, error in quos quae eaque non recusandae deserunt provident ipsum odit laudantium libero rerum laboriosam perspiciatis? Aspernatur hic ipsa fugit quasi.
Molestias harum, dicta ut quo cupiditate eligendi? Ipsam, aliquid doloribus mollitia, quia neque porro facere provident molestiae totam perferendis aspernatur, quaerat harum modi. Dignissimos pariatur sed rem temporibus saepe in."""



class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User count')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=" ".join(choices(text, k=64)),
                    author=author
                )
                post.save()