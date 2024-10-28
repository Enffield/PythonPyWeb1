import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    # from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag
    from apps.db_train.models import Author, AuthorProfile, Tag, Entry
    from django.db.models import Q, Max, Min, Avg, Count, Sum



    obj = Entry.objects.values_list('author__username')

    print(obj)

