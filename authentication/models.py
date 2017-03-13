from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from core.models import TimestampedModel
import jwt
