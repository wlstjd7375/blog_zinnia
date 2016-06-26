from django.db import models

# JJJ
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.core import validators

class MyUserManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self, username, email, name, url, intro, password, **extra_fields):
		# Creates and saves a User with the given username, email and password.
		if not username:
			raise ValueError('The given username must be set')
		user = self.model(
			username=username,
			email=self.normalize_email(email),
			name=name,
			url=url,
			intro=intro,
			**extra_fields
		)
		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_user(self, username, email, name, url, intro, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(username, email, name, url, intro, password, **extra_fields)

	def create_superuser(self, username, email, name, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_admin', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')
		if extra_fields.get('is_admin') is not True:
			raise ValueError('Superuser must have is_admin=True.')
		return self._create_user(username, email, name, '', '', password, **extra_fields)


class MyUser(AbstractBaseUser,  PermissionsMixin):
	username = models.CharField(
		'username',
		max_length=30,
		unique=True,
		help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
		validators=[
		validators.RegexValidator(
			r'^[\w.@+-]+$',
			'Enter a valid username. This value may contain only '
			'letters, numbers ' 'and @/./+/-/_ characters.'
		),],
		error_messages={
			'unique': "A user with that username already exists.",
		},
	)
	name = models.CharField('name', max_length=30, blank=True)
	email = models.EmailField('email address', blank=True)
	url = models.CharField('url', max_length=100, blank=True)
	intro = models.TextField('intro', blank=True)

	profile = models.ImageField(
		null=True,
		blank=True,
		upload_to='image/profile/',
	)

	is_active = models.BooleanField('is active', default=True)
	is_admin = models.BooleanField('is admin', default=False)
	is_staff = models.BooleanField('is staff', default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'name']

	def get_full_name(self):
		# The user is identified by their email address
		return self.name

	def get_short_name(self):
		# The user is identified by their email address
		return self.name

	def __str__(self):
		return self.name

