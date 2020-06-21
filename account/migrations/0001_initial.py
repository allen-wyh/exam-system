# Generated by Django 2.2.12 on 2020-06-18 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_src', models.IntegerField(choices=[(1, '微信授权用户'), (2, '游客用户'), (3, '普通用户'), (4, '机构用户')], db_index=True, default=2, help_text='用户来源', verbose_name='用户来源')),
                ('user_status', models.IntegerField(choices=[(0, '未验证'), (1, '已激活'), (2, '已禁用'), (3, '已删除'), (4, '已分配')], default=1, verbose_name='用户状态')),
                ('wechat_number', models.CharField(blank=True, help_text='用户微信号', max_length=32, null=True, verbose_name='微信号')),
                ('name', models.CharField(blank=True, db_index=True, help_text='用户姓名', max_length=32, null=True, verbose_name='姓名')),
                ('email', models.CharField(blank=True, db_index=True, help_text='用户邮箱', max_length=40, null=True, verbose_name='邮箱')),
                ('sex', models.IntegerField(choices=[(1, '男'), (0, '女')], default=1, help_text='用户性别', verbose_name='性别')),
                ('age', models.IntegerField(default=0, help_text='用户年龄', verbose_name='年龄')),
                ('nickname', models.CharField(blank=True, help_text='用户昵称', max_length=32, null=True, verbose_name='昵称')),
                ('avatar', models.CharField(blank=True, help_text='用户头像', max_length=60, null=True, verbose_name='头像地址')),
                ('phone', models.CharField(blank=True, db_index=True, help_text='用户电话', max_length=11, null=True, verbose_name='手机号')),
                ('country', models.CharField(blank=True, help_text='用户国家', max_length=32, null=True, verbose_name='国家')),
                ('province', models.CharField(blank=True, help_text='用户省份', max_length=32, null=True, verbose_name='省份')),
                ('city', models.CharField(blank=True, help_text='用户城市', max_length=32, null=True, verbose_name='城市')),
                ('location', models.CharField(blank=True, help_text='用户地址', max_length=60, null=True, verbose_name='地址')),
                ('is_upgrade', models.IntegerField(default=0, help_text='是否升级会员', verbose_name='是否升级会员')),
                ('upgrade_time', models.DateTimeField(blank=True, help_text='升级日期', null=True, verbose_name='会员升级时间')),
                ('expire_time', models.DateTimeField(blank=True, help_text='过期时间', null=True, verbose_name='会员过期时间')),
                ('upgrade_count', models.IntegerField(default=0, help_text='升级次数', verbose_name='会员升级次数')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_id', models.CharField(blank=True, db_index=True, help_text='比赛唯一标识', max_length=32, null=True, verbose_name='比赛id')),
                ('uid', models.CharField(blank=True, db_index=True, help_text='用户唯一标识', max_length=32, null=True, verbose_name='用户id')),
                ('name', models.CharField(blank=True, help_text='name/姓名', max_length=24, null=True, verbose_name='姓名')),
                ('sex', models.CharField(blank=True, help_text='sex/性别', max_length=1, null=True, verbose_name='性别')),
                ('age', models.IntegerField(blank=True, default=0, help_text='age/年龄', null=True, verbose_name='年龄')),
                ('phone', models.CharField(blank=True, help_text='phone/手机号', max_length=11, null=True, verbose_name='手机号')),
                ('wechat_number', models.CharField(blank=True, help_text='wxid/微信号', max_length=24, null=True, verbose_name='微信号')),
                ('email', models.CharField(blank=True, help_text='email/邮箱', max_length=60, null=True, verbose_name='邮箱')),
                ('pid', models.CharField(blank=True, help_text='pid/身份证号', max_length=18, null=True, verbose_name='身份证号')),
                ('graduated_from', models.CharField(blank=True, help_text='graduated_from/毕业院校', max_length=60, null=True, verbose_name='毕业院校')),
                ('address', models.CharField(blank=True, help_text='address/联系地址', max_length=60, null=True, verbose_name='地址')),
            ],
            options={
                'verbose_name': '用户登记信息',
                'verbose_name_plural': '用户登记信息',
            },
        ),
    ]
