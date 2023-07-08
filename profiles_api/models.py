from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class UserProfileManager(models.Manager):
    """Manager for user profiles"""
    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email) #normalize email address
        user = self.model(email=email,name=name)

        user.set_password(password) #set password
        user.save(using=self._db) #save user object

        return user
    
    def create_superuser(self,email,name,password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email,name,password)

        user.is_superuser = True #is_superuser is created by PermissionsMixin
        user.is_staff = True #is_staff is created by PermissionsMixin
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """"Database model for users in the system"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) #user is active or not
    is_staff = models.BooleanField(default=False) #user is staff or not

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    
    def __str__(self):
        """Return string representation of our user"""
        return self.email