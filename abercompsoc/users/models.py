from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, ManyToManyField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    roles = ManyToManyField("users.Role")

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        if self.get_full_name() != "":
            return self.get_full_name()
        return super(User, self).__str__()

    def is_aber_student(self):
        return self.emailaddress_set.filter(verified=True, email__endswith="@aber.ac.uk").exists()


class Role(Model):
    name = CharField("Role Name", max_length=255)

    def __str__(self):
        return self.name.title()
