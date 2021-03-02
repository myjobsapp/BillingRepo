from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import User
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email,full_name, password=None,is_staff=False,is_admin=False,is_active=True, ):  #if we have required fields then it must be menti here.Bt in this case our reqrd filds are empty
        if not email:
            raise ValueError('User must have Email')
        if not password:
            raise ValueError('User must havepasword')
        if not full_name:
            raise ValueError('User must have full name')

        user_obj=self.model(
            email=self.normalize_email(email),
            full_name=full_name
        )
        user_obj.set_password(password)
        user_obj.staff =is_staff
        user_obj.admin = is_admin
        user_obj.active =is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staff_user(self, email,full_name, password=None):
        user=self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email,full_name, password=None):
        user=self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user

class User(AbstractBaseUser):
    email=models.EmailField(unique=True)
    full_name=models.CharField(max_length=100,null=True,blank=True)
    active=models.BooleanField(default=True) ## can login
    staff=models.BooleanField(default=False) ## staff user non superuser
    admin=models.BooleanField(default=False) #superuser
    timestamp=models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD='email'   #replace email with username for username to be

    ##Fields required wheen user is created
    REQUIRED_FIELDS=['full_name']

    objects=UserManager()
    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.email

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    def has_perm(self, perm ,obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)