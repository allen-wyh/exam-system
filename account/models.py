from django.db import models

# Create your models here.
class Profile(models.Model):
    """用户信息类"""

    WX_USER = 1
    GUEST_USER = 2
    NORMAL_USER = 3
    COMPANY_USER = 4

    USER_SRC = (
        (WX_USER, u'微信授权用户'),
        (GUEST_USER, u'游客用户'),
        (NORMAL_USER, u'普通用户'),
        (COMPANY_USER, u'机构用户'),
    )

    MALE = 1
    FEMALE = 0

    GENDER = (
        (MALE, u'男'),
        (FEMALE, u'女'),
    )

    UNVERIFIED = 0
    ACTIVATED = 1
    DISABLED = 2
    DELETED = 3
    ASSIGN = 4

    USER_STATUS = (
        (UNVERIFIED, u'未验证'),
        (ACTIVATED, u'已激活'),
        (DISABLED, u'已禁用'),
        (DELETED, u'已删除'),
        (ASSIGN, u'已分配'),
    )

    # 用户相关
    # choise 的值 是元组，也可以是列表，在数据库中以数字展现，前端表单中以内容显示。
    user_src = models.IntegerField(u'用户来源', choices=USER_SRC, default=GUEST_USER, help_text=u'用户来源', db_index=True)
    user_status = models.IntegerField(u'用户状态', choices=USER_STATUS, default=ACTIVATED)

    # 用户基本信息
    wechat_number = models.CharField(u'微信号', max_length=32, blank=True, null=True, help_text=u'用户微信号')
    name = models.CharField(u'姓名', max_length=32, blank=True, null=True, help_text=u'用户姓名', db_index=True)
    email = models.CharField(u'邮箱', max_length=40, blank=True, null=True, help_text=u'用户邮箱', db_index=True)
    sex = models.IntegerField(u'性别', choices=GENDER, default=MALE, help_text=u'用户性别')
    age = models.IntegerField(u'年龄', default=0, help_text=u'用户年龄')
    nickname = models.CharField(u'昵称', max_length=32, blank=True, null=True, help_text=u'用户昵称')
    avatar = models.CharField(u'头像地址', max_length=60, blank=True, null=True, help_text=u'用户头像')
    phone = models.CharField(u'手机号', max_length=11, blank=True, null=True, help_text=u'用户电话', db_index=True)
    country = models.CharField(u'国家', max_length=32, blank=True, null=True, help_text=u'用户国家')
    province = models.CharField(u'省份', max_length=32, blank=True, null=True, help_text=u'用户省份')
    city = models.CharField(u'城市', max_length=32, blank=True, null=True, help_text=u'用户城市')
    location = models.CharField(u'地址', max_length=60, blank=True, null=True, help_text=u'用户地址')
    # 会员相关
    is_upgrade = models.IntegerField(u'是否升级会员', default=0, help_text=u'是否升级会员')
    upgrade_time = models.DateTimeField(u'会员升级时间', blank=True, null=True, help_text=u'升级日期')
    expire_time = models.DateTimeField(u'会员过期时间', blank=True, null=True, help_text=u'过期时间')
    upgrade_count = models.IntegerField(u'会员升级次数', default=0, help_text=u'升级次数')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = u'用户信息'

    def __str__(self):
        return f'微信号：{self.wechat_number}, 姓名：{self.name}, 年龄：{self.age}, 性别：{self.age}, ' \
               f'邮箱：{self.email}, 昵称：{self.nickname}, 手机号：{self.phone}, ' \
               f'国家：{self.country}, 省份：{self.province}, 城市：{self.city}, 地址:{self.location}'


class UserInfo(models.Model):
    """
    用户填写的表单信息类
    """

    # 标识
    kind_id = models.CharField(u'比赛id', max_length=32, blank=True, null=True, help_text=u'比赛唯一标识', db_index=True)
    uid = models.CharField(u'用户id', max_length=32, blank=True, null=True, help_text=u'用户唯一标识', db_index=True)
    # 基本信息
    name = models.CharField(u'姓名', max_length=24, blank=True, null=True, help_text=u'name/姓名')
    sex = models.CharField(u'性别', max_length=1, blank=True, null=True, help_text=u'sex/性别')
    age = models.IntegerField(u'年龄', default=0, blank=True, null=True, help_text=u'age/年龄')
    phone = models.CharField(u'手机号', max_length=11, blank=True, null=True, help_text=u'phone/手机号')
    wechat_number = models.CharField(u'微信号', max_length=24, blank=True, null=True, help_text=u'wxid/微信号')
    email = models.CharField(u'邮箱', max_length=60, blank=True, null=True, help_text=u'email/邮箱')
    pid = models.CharField(u'身份证号', max_length=18, blank=True, null=True, help_text=u'pid/身份证号')
    graduated_from = models.CharField(u'毕业院校', max_length=60, blank=True, null=True, help_text=u'graduated_from/毕业院校')
    address = models.CharField(u'地址', max_length=60, blank=True, null=True, help_text=u'address/联系地址')

    class Meta:
        verbose_name = u'用户登记信息'
        verbose_name_plural = u'用户登记信息'

    def __str__(self):
        return f'姓名：{self.name}, 性别：{self.sex}, 年龄：{self.age}, 手机号：{self.phone}, 微信号：{self.wechat_number}, ' \
               f'邮箱：{self.email}, 身份证号：{self.pid}, 毕业院校：{self.graduated_from}, 地址：{self.address}'
