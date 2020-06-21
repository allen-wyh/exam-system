from django.db import models

# Create your models here.
class BusinessAccountInfo(models.Model):
    """ 出题帐户类 """

    INTERNET = 0
    FINANCE = 1
    ENERGY = 2
    INFRASTRUCTURE = 3
    TRANSPORTATION = 4
    COMMUNICATION = 5

    TYPE_CHOICES = (
        (INTERNET, '互联网'),
        (FINANCE, '金融'),
        (ENERGY, '能源'),
        (INFRASTRUCTURE, '基础建设'),
        (TRANSPORTATION, '交通'),
        (COMMUNICATION, '通信')
    )

    # 帐户信息
    email = models.CharField(u'邮箱', max_length=40, blank=True, null=True, help_text=u'邮箱', db_index=True, unique=True)

    # 公司信息
    company_name = models.CharField(u'公司名称', max_length=60, blank=True, null=True, help_text=u'公司名称')
    company_type = models.IntegerField(u'公司类型', choices=TYPE_CHOICES, default=INTERNET, help_text=u'公司类型')
    company_description = models.TextField(u'公司描述', blank=True, null=True, help_text=u'公司描述')
    company_username = models.CharField(u'法人代表', max_length=32, blank=True, null=True, help_text=u'公司联系人')
    company_phone = models.CharField(u'联系电话', max_length=16, blank=True, null=True, help_text=u'公司联系电话', db_index=True)
    company_location = models.TextField(u'公司位置', blank=True, null=True, help_text=u'公司联系地址')

    class Meta:
        verbose_name = u'出题账户'
        verbose_name_plural = u'出题账户'

class BusinessAppInfo(models.Model):
    """ 应用信息类 """


    # APP 配置信息
    app_name = models.CharField(u'应用名', max_length=40, blank=True, null=True, help_text=u'应用名')
    app_description = models.TextField(u'应用描述', blank=True, null=True, help_text=u'应用描述')

    class Meta:
        verbose_name = u'应用信息'
        verbose_name_plural = u'应用信息'

class AppConfigInfo(models.Model):
    """ 应用配置信息类 """

    app_name = models.CharField(u'应用名', max_length=40, blank=True, null=True, help_text=u'应用名')

    # 文案配置
    rule_text = models.TextField(u'比赛规则', max_length=255, blank=True, null=True, help_text=u'比赛规则')

    # 显示信息
    is_show_userinfo = models.BooleanField(u'展示用户表单', default=False, help_text=u'是否展示用户信息表单')
    userinfo_fields = models.CharField(u'用户表单字段', max_length=128, blank=True, null=True, help_text=u'需要用户填写的字段#隔开')
    userinfo_field_names = models.CharField('用户表单label', max_length=128, blank=True, null=True, help_text=u'用户需要填写的表单字段label名称')
    option_fields = models.CharField(u'下拉框字段', max_length=128, blank=True, null=True, help_text=u'下拉框字段选项配置，#号隔开，每个字段由:h和，号组成。 如 option1:吃饭，喝水，睡觉#option2:上班，学习，看电影')

    class Meta:
        verbose_name = u'应用配置信息'
        verbose_name_plural = u'应用配置信息'

    class UserInfoImage(models.Model):
        """
        用户表单图片配置类
        """

        uii_name = models.CharField(u'配置名称', max_length=32, blank=True, null=True, help_text=u'信息图片配置名称')
        # 用户信息
        name = models.CharField(u'姓名', max_length=60, blank=True, null=True, help_text=u'姓名')
        sex = models.CharField(u'性别', max_length=60, blank=True, null=True, help_text=u'性别')
        age = models.CharField(u'年龄', max_length=60, blank=True, null=True, help_text=u'年龄')
        phone = models.CharField(u'手机号', max_length=60, blank=True, null=True, help_text=u'电话')
        wxid = models.CharField(u'微信号', max_length=60, blank=True, null=True, help_text=u'微信号')
        email = models.CharField(u'邮箱', max_length=60, blank=True, null=True, help_text=u'邮箱')
        pid = models.CharField(u'身份证号', max_length=60, blank=True, null=True, help_text=u'身份证号')
        graduated_from = models.CharField(u'毕业院校', max_length=60, blank=True, null=True, help_text=u'毕业院校')
        address = models.CharField(u'地址', max_length=60, blank=True, null=True, help_text=u'联系地址')
        resume = models.CharField(u'简历', max_length=60, blank=True, null=True, help_text=u'简历')

        class Meta:
            verbose_name = u'用户信息图片配置'
            verbose_name_plural = u'用户信息图片配置'
