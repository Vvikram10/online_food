from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('User email is must')
        
        if not username:
            raise ValueError('User must have username')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,first_name,last_name,username,email,password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    VENDOR = 1
    CUSTOMER = 2
    ROLE_CHOICES = (
        (VENDOR,'Vendor'),
        (CUSTOMER,'Customer'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=12,blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,blank=True,null=True)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_joined = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Check if the user has a specific permission"
        return self.is_superuser or super().has_perm(perm, obj)

    def has_module_perms(self, app_label):
        "Check if the user has access to a specific app"
        return self.is_superuser or super().has_module_perms(app_label)
    
    def get_role(self):
        if self.role == 1:
            user_role = 'Vendor'
        elif self.role == 2:
            user_role = 'Customer'  # Corrected assignment
        else:
            user_role = 'Unknown'  # Handle cases where role is not 1 or 2
        return user_role

    


class UserProfile(models.Model):
    user = models.OneToOneField("User", verbose_name=("User"), on_delete=models.CASCADE,blank=True,null=True)
    profile_picture = models.ImageField(upload_to='users/profile_picture',blank=True,null=True)
    cover_photo = models.ImageField(upload_to='users/cover_photo',blank=True,null=True)
    address_line_1 = models.CharField(max_length=50,blank=True,null=True)
    address_line_2 = models.CharField(max_length=50,blank=True,null=True)
    country = models.CharField(max_length=15,blank=True,null=True)
    pin_code = models.CharField(max_length=6,blank=True,null=True)
    latitude = models.CharField(max_length=20,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email    



