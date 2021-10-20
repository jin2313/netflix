from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
# class UserManager(BaseUserManager):
#     def create_user(self, id, password=None):
#         if not id:
#             raise ValueError('id는 필수입니다.')
#         user = self.model(id=id)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_super_user(self, id, password):
#         user = self.create_user(id=id, password=password)
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
#
#
# class User(AbstractBaseUser):
#     id = models.CharField('', max_length=20, null=False, primary_key=True)
#     # password = models.CharField('', max_length=20, null=False)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     # confirm_password = models.CharField('', max_length=20, null=False)
#
#     objects = UserManager()
#     USERNAME_FIELD = 'id'
#
#     def __str__(self):
#         return self.id
#
#
# def has_perm(self, perm, obj=None):
#     return True
#
#
# def has_module_perms(self, app_label):
#     return True
#
#
# @property
# def is_staff(self):
#     return self.is_admin