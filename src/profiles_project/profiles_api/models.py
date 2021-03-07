from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    # Helps django work with our custom user model.
    def create_user(self, email, name, password=None):
        #Creates new user profile object
        if not email:
            raise ValueError('Users must have an email address')
        email =self.normalize_email(email) #normalize email address
        user = self.model(email=email, name=name)
        user.set_password(password) #will encrypt password into hash
        user.save(using=self._db) #save to database
        return user
    
    def create_superuser(self, email, name, password):
        #creates and save new superuser with given details
        user = self.create_user(email, name, password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    #Respents a 'UserProfile' inside our system
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        #Used to get full name
        return self.name
    def get_short_name(self):
        #Used to get short name
        return self.name
    def __str__(self):
        #used it when needs to convert the object to a string
        return self.email