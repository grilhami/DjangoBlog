from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from app.core.models import TimestampedModel
import jwt


class UserManager(BaseUserManager, TimestampedModel):
	
	pass
	
class User(AbstractBaseUser, TimestampedModel):
	
	pass
