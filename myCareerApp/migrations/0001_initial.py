# Generated by Django 3.0.8 on 2020-08-05 14:17

from django.db import migrations, models
import myCareerApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10, verbose_name='아이디')),
                ('user_password', models.CharField(max_length=15, verbose_name='비밀번호')),
                ('name', models.CharField(max_length=10, verbose_name='이름')),
                ('image', models.TextField(null=True, verbose_name='프로필 사진')),
                ('tel', models.CharField(max_length=12, verbose_name='전화번호')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='이메일')),
                ('birth', models.TextField(null=True, verbose_name='생년월일')),
                ('tech', models.TextField(null=True, verbose_name='기술')),
                ('intro', models.TextField(blank=True, default='안녕하세요', null=True, verbose_name='자기소개')),
                ('career', models.TextField(null=True, verbose_name='경력')),
                ('kakaoId', models.TextField(null=True, verbose_name='카카오톡아이디')),
                ('github_url', models.TextField(null=True, verbose_name='깃허브')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(default='', max_length=200, verbose_name='프로젝트 이름')),
                ('project_des', models.TextField(default='', verbose_name='프로젝트 설명')),
                ('project_url', models.TextField(default='', verbose_name='프로젝트 링크')),
                ('project_img', models.TextField(null=True, verbose_name='프로젝트 사진')),
                ('project_id', models.IntegerField(default='', verbose_name='프로젝트 번호')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', myCareerApp.models.UserManager()),
            ],
        ),
    ]
