- create superuser
./manage.py createsuperuser

- create group
./manage.py shell
from django.contrib.auth.models import Group, Permission
g = Group.objects.create(name='super_user')
g.save()

BONUS : HTTPS
