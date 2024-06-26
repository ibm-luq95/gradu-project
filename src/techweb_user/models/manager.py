# -*- coding: utf-8 -*-#
from random import randint

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Permission
from django.db import transaction
from django.db.models import Q
from django.db.models.aggregates import Count
from django.utils.translation import gettext as _

from core.models.querysets import BaseQuerySetMixin


class TechWebUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def get_queryset(self) -> BaseQuerySetMixin:
        queryset = BaseQuerySetMixin(self.model, using=self._db).filter(is_deleted=False)
        return queryset

    # def all(self) -> BaseQuerySetMixin:
    #     qs = self.get_queryset()
    #     return qs.filter(~Q(email="anonymoususer")).order_by("first_name")

    def create_user(self, employee_id, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        with transaction.atomic():
            # if not email:
            #     raise ValueError(_("The Email must be set"))
            # email = self.normalize_email(email)
            user = self.model(employee_id=employee_id, **extra_fields)
            user.set_password(password)
            user.save()
            # if user.user_type == "manager":
            #     Manager.objects.select_for_update().create(user=user)
            return user

    def create_superuser(self, employee_id, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        with transaction.atomic():
            extra_fields.setdefault("is_staff", True)
            extra_fields.setdefault("is_superuser", True)
            extra_fields.setdefault("is_active", True)
            development_admin_emails = ["admin@admin.com", "admin@admin.dev"]

            if extra_fields.get("is_staff") is not True:
                raise ValueError(_("Superuser must have is_staff=True."))
            if extra_fields.get("is_superuser") is not True:
                raise ValueError(_("Superuser must have is_superuser=True."))
            created_user = self.create_user(employee_id, password, **extra_fields)
            # developer_permission = Permission.objects.get(codename="developer_user")
            # created_user.user_permissions.add(developer_permission)
            return created_user

    def random(self):
        count = self.aggregate(count=Count("id"))["count"]
        random_index = randint(0, count - 1)
        return self.all()[random_index]
