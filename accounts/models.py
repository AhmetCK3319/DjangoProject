from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):

    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('user must have an email adress')
        if not username:
            raise ValueError('user must have an username')

        user=self.model(
        email = self.normalize_email(email),
        first_name = first_name,
        last_name = last_name,
        username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,first_name,last_name,username,password,email):
        #superuser oluştururken sorulan soruların ayarlandığı yer

        user = self.create_user(
        email = self.normalize_email(email),
        first_name = first_name,
        last_name = last_name,
        username = username,
        password = password,

        )
        user.is_admin=True
        user.is_staff=True
        user.is_active=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):

    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50,unique=True)
    email           = models.EmailField(max_length=50,unique=True)
    phone_number    = models.CharField(max_length=50)

    ##### required ####

    date_joined     = models.DateTimeField(auto_now_add=True)
    last_joined     = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)

    ########################################################
    # createsuperuser çalıştığı zaman sorulacak sorular
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username']
    #########################################################
    
    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        # Bu fonksiyon, kullanıcının belirli bir izne sahip olup olmadığını kontrol eder.
        return self.is_admin

    def has_module_perms(self,add_label):
        # Bu fonksiyon, bir kullanıcının belirli bir modülün izinlerine sahip olup olmadığını kontrol eder.
        # return self.user_permissions.filter(content_type__app_label=add_label).exists() ==> olması gereken kod
        return True


class UserProfile(models.Model):
    user=models.OneToOneField(Account,on_delete=models.CASCADE)
    adress_line1=models.CharField(max_length=100,blank=True)
    adress_line2=models.CharField(max_length=100,blank=True)
    profile_picture=models.ImageField(blank=True,upload_to='images/users')
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)

    def __str__(self):
        return self.user.first_name
    
    def full_adress(self):
        return f'{self.adress_line1} {self.adress_line2}'
    