from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, middle_name, last_name, sex, date_of_birth, is_staff, is_superuser, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            sex=sex,
            date_of_birth=date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, middle_name, last_name, sex, date_of_birth, password):
        user = self.create_user(email,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            sex=sex,
            date_of_birth=date_of_birth
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user
