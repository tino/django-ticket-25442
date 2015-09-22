# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "DROP TABLE auth_user_user_permissions;"
            "DROP TABLE auth_group_permissions;"
            "DROP TABLE auth_user_groups;"
            "DROP TABLE auth_group;"
            "DROP TABLE auth_permission;"
            "DROP TABLE auth_user;"
        )
    ]
