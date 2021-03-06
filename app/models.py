from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from .choices import SEX_TYPE 
from simple_history import register

register(User)


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,  password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        swappable = 'AUTH_USER_MODEL'

    email = models.EmailField(_('email address'), max_length=254, unique=True)
    first_name = models.CharField(_('first name'), max_length=30)
    middle_name = models.CharField(_('middle name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    sex = models.CharField(_('sex'), max_length=1, choices=SEX_TYPE)
    date_of_birth = models.DateField(_('date of birth'), null=True)
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the user can log into admin'))
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)


    slug = models.SlugField(max_length=100, unique=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        unique_together = ('first_name', 'middle_name', 'last_name', 'date_of_birth', 'sex',)

    def get_full_name(self):
        full_name = '%s %s' %(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    class Meta:
        permissions = (
            ('view_task', 'View task'),

        )

    def save(self, *args, **kwargs):
        import pdb; pdb.set_trace()
        if not self.id:
            full_name_slug = '%s %s %s' %(self.last_name, self.middle_name, self.first_name) 
            self.slug = slugify(full_name_slug)
        super(CustomUser, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})
