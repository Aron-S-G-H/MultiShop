from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, phone, fullname, password=None):
        """
        Creates and saves a User with the given email, phone
        and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            fullname=fullname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, fullname, password=None):
        """
        Creates and saves a superuser with the given email, phone
        and password.
        """
        user = self.create_user(
            email,
            password=password,
            phone=phone,
            fullname=fullname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='آدرس ایمیل', max_length=255, unique=True,)
    phone = models.CharField( verbose_name='شماره همراه', max_length=12, unique=True)
    fullname = models.CharField( verbose_name='نام کامل', max_length=60)
    is_active = models.BooleanField(verbose_name='مشتری', default=True)
    is_admin = models.BooleanField(verbose_name='ادمین', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'fullname']
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    
class Otp(models.Model):
    email = models.EmailField()
    fullname = models.CharField(max_length=50)
    phone = models.IntegerField()
    password = models.CharField(max_length=60)
    code = models.SmallIntegerField()
    token = models.CharField(max_length=121)
    expiratione_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'رمز یک بار مصرف'
        verbose_name_plural = 'رمزهای یک بار مصرف'

    def __str__(self):
        return self.email
