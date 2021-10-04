from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('유저'))
    nickname = models.CharField(_('닉네임'), max_length=30)
    phone_number = models.CharField(_('핸드폰 번호'), max_length=11)
    birth_date = models.DateField(_("생일"))

    class Meta:
        db_table = "PROFILE"

    def __str__(self):
        return self.nickname

    def get_short_nickname(self):
        return self.nickname[:5]
