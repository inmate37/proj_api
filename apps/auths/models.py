from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import BooleanField, DateTimeField, EmailField, QuerySet
from django.utils import timezone


class CustomUserManager(BaseUserManager):

    def create_user(
        self,
        email: str,
        password: str
    ) -> 'CustomUser':

        if not email:
            raise ValidationError('Email required')

        user: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email: str,
        password: str
    ) -> 'CustomUser':

        user: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_not_deleted(self) -> QuerySet['CustomUser']:
        return self.filter(
            datetime_deleted__isnull=True
        )

    def get_deleted(self) -> QuerySet['CustomUser']:
        return self.filter(
            datetime_deleted__isnull=False
        )


class CustomUser(
    AbstractBaseUser,
    PermissionsMixin,
):
    """CustomUser entity."""

    email = EmailField(
        'Почта/Логин', unique=True
    )
    is_active = BooleanField('Активность', default=True)
    is_staff = BooleanField('Статус менеджера', default=False)
    date_joined = DateTimeField(
        'Дата регистрации', default=timezone.now
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = (
            'date_joined',
        )
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
