import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    inner_qs = Blog.objects.filter(name__contains='Путешествия')
    entries = Entry.objects.filter(blog__in=inner_qs)
    print(inner_qs)
    print(entries)

    print(Entry.objects.filter(number_of_comments__gt=10))

    import datetime

    print(Entry.objects.filter(pub_date__gte=datetime.date(2023, 6, 1)))
    print(Entry.objects.filter(number_of_comments__gt=10).filter(rating__lt=4))

    print(Entry.objects.filter(headline__lte="М"))

    print(Entry.objects.filter(headline__startswith='Как'))