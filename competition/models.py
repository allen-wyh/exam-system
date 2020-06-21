from django.db import models

# Create your models here.
from django.utils import timezone


class CompetitionKindInfo(models.Model):
    """比赛类别信息类"""

    IT_ISSUE = 0
    EDUCATION = 1
    CULTURE = 2
    GENERAL = 3
    INTERVIEW = 4
    REAR = 5
    GEO = 6
    SPORT = 7

    KIND_TYPES = (
        (IT_ISSUE, u'技术类'),
        (EDUCATION, u'教育类'),
        (CULTURE, u'文化类'),
        (GENERAL, u'常识类'),
        (GEO, u'地理类'),
        (SPORT, u'体育类'),
        (INTERVIEW, u'面试题')
    )

    account_id = models.CharField(u'出题账户id', max_length=32, blank=True, null=True, help_text=u'商家账户唯一标识', db_index=True)
    app_id = models.CharField(u'应用id', max_length=32, blank=True, null=True, help_text=u'应用唯一标识', db_index=True)
    bank_id = models.CharField(u'题库id', max_length=32, blank=True, null=True, help_text=u'题库唯一标识', db_index=True)
    kind_type = models.IntegerField(u'比赛类型', default=IT_ISSUE, choices=KIND_TYPES, help_text=u'比赛类型')
    kind_name = models.CharField(u'比赛名称', max_length=32, blank=True, null=True, help_text=u'竞赛类别名称')

    sponsor_name = models.CharField(u'赞助商名称', max_length=60, blank=True, null=True, help_text=u'赞助商名称')

    total_score = models.IntegerField(u'总分数', default=0, help_text=u'总分数')
    question_num = models.IntegerField(u'题目个数', default=0, help_text=u'出题数量')

    # 周期相关
    cop_startat = models.DateTimeField(u'比赛开始时间', default=timezone.now, help_text=u'比赛开始时间')
    period_time = models.IntegerField(u'答题时间', default=60, help_text=u'答题时间(min)')
    cop_finishat = models.DateTimeField(u'比赛结束时间', blank=True, null=True, help_text=u'比赛结束时间')

    # 参与相关
    total_partin_num = models.IntegerField(u'总参与人数', default=0, help_text=u'总参与人数')

    class Meta:
        verbose_name = u'比赛类别信息'
        verbose_name_plural = u'比赛类别信息'

class BankInfo(models.Model):
    """
    题库信息类
    """

    IT_ISSUE = 0
    EDUCATION = 1
    CULTURE = 2
    GENERAL = 3
    INTERVIEW = 4
    REAR = 5
    GEO = 6
    SPORT = 7

    BANK_TYPES = (
        (IT_ISSUE, u'技术类'),
        (EDUCATION, u'教育类'),
        (CULTURE, u'文化类'),
        (GENERAL, u'常识类'),
        (GEO, u'地理类'),
        (SPORT, u'体育类'),
        (INTERVIEW, u'面试题')
    )

    uid = models.CharField(u'用户id', max_length=32, blank=True, null=True, help_text=u'用户唯一标识', db_index=True)
    account_id = models.CharField(u'商家id', max_length=32, blank=True, null=True, help_text=u'商家账户唯一标识', db_index=True)
    bank_name = models.CharField(u'题库名称', max_length=40, blank=True, null=True, help_text=u'题库名称')

    choice_num = models.IntegerField(u'选择题数', default=0, help_text=u'选择题数')
    fillinblank_num = models.IntegerField(u'填空题数', default=0, help_text=u'填空题数')
    bank_type = models.IntegerField(u'题库类型', default=IT_ISSUE, choices=BANK_TYPES, help_text=u'题库类型')
    kind_num = models.IntegerField(u'比赛使用次数', default=0, help_text=u'比赛使用次数')
    partin_num = models.IntegerField(u'总答题人数', default=0, help_text=u'总答题人数')

    class Meta:
        verbose_name = u'题库'
        verbose_name_plural = u'题库'

class ChoiceInfo(models.Model):
    """
    选择题信息类
    """

    QUESTION_TYPE = 'choice'

    TXT = 1
    IMG = 2
    AUDIO = 3

    CONTENT_TYPE = (
        (TXT, u'文本'),
        (IMG, u'图片'),
        (AUDIO, u'音频'),
    )

    bank_id = models.CharField(u'题库id', max_length=32, blank=True, null=True, help_text=u'题库唯一标识', db_index=True)
    ctype = models.IntegerField(u'题目类型', choices=CONTENT_TYPE, default=TXT, help_text=u'题目类型')
    question = models.CharField(u'问题', max_length=255, blank=True, null=True, help_text=u'题目')
    answer = models.CharField(u'答案', max_length=255, blank=True, null=True, help_text=u'答案')
    item1 = models.CharField(u'选项1', max_length=255, blank=True, null=True, help_text=u'选项一')
    item2 = models.CharField(u'选项2', max_length=255, blank=True, null=True, help_text=u'选项二')
    item3 = models.CharField(u'选项3', max_length=255, blank=True, null=True, help_text=u'选项三')
    item4 = models.CharField(u'选项4', max_length=255, blank=True, null=True, help_text=u'选项四')
    source = models.CharField(u'出处', max_length=255, blank=True, null=True, help_text=u'出处')

    class Meta:
        verbose_name = u'选择题'
        verbose_name_plural = u'选择题'

class FillInBlankInfo(models.Model):
    """
    填空题信息类
    """

    QUESTION_TYPE = 'fillinblank'

    TXT = 1
    IMG = 2
    AUDIO = 3

    CONTENT_TYPE = (
        (TXT, u'文本'),
        (IMG, u'图片'),
        (AUDIO, u'音频'),
    )

    bank_id = models.CharField(u'题库id', max_length=32, blank=True, null=True, help_text=u'题库唯一标识', db_index=True)
    ctype = models.IntegerField(u'题目类型', choices=CONTENT_TYPE, default=TXT, help_text=u'题目类型')
    question = models.CharField(u'问题', max_length=255, blank=True, null=True, help_text=u'题目')
    answer = models.CharField(u'答案', max_length=255, blank=True, null=True, help_text=u'答案')
    source = models.CharField(u'出处', max_length=255, blank=True, null=True, help_text=u'出处')

    class Meta:
        verbose_name = u'填空题'
        verbose_name_plural = u'填空题'

class CompetitionQAInfo(models.Model):
    """答题记录信息类"""

    UNCOMPLETED = 0
    COMPLETED = 1
    OVERTIME = 2

    STATUS_CHOICES = (
        (UNCOMPLETED, u'未完成'),
        (COMPLETED, u'已完成'),
        (OVERTIME, u'超时')
    )

    status = models.IntegerField(u'答题状态', choices=STATUS_CHOICES, default=0, help_text=u'答题状态')
    kind_id = models.CharField(u'比赛id', max_length=32, blank=True, null=True, help_text=u'比赛类别唯一标识', db_index=True)
    qa_id = models.IntegerField(u'问题id', blank=True, null=True, help_text=u'QA 唯一标识', db_index=True)
    uid = models.CharField(u'用户id', max_length=32, blank=True, null=True, help_text=u'用户唯一标识', db_index=True)

    # 问题答案相关
    qsrecord = models.TextField('问题记录', max_length=10000, blank=True, null=True, help_text=u'问题记录')
    asrecord = models.TextField('答案记录', max_length=10000, blank=True, null=True, help_text=u'答案记录')
    aslogrecord = models.TextField('答案提交记录', max_length=10000, blank=True, null=True, help_text=u'答案提交记录')

    # 耗费时间相关
    started_stamp = models.BigIntegerField(u'开始时间戳', default=0, help_text=u'开始时间戳(毫秒)')
    finished_stamp = models.BigIntegerField(u'结束时间戳', default=0, help_text=u'结束时间戳(毫秒)')
    expend_time = models.IntegerField(u'耗时', default=0, help_text=u'耗费时间(毫秒)')

    started = models.BooleanField(u'已开始', default=False, help_text=u'是否开始', db_index=True)
    finished = models.BooleanField(u'已结束', default=False, help_text=u'是否结束', db_index=True)

    # 得分相关
    correct_num = models.IntegerField(u'正确数', default=0, help_text=u'答对数量')
    incorrect_num = models.IntegerField(u'错误数', default=0, help_text=u'答错数量')
    correct_list = models.CharField(u'正确答案列表', max_length=10000, blank=True, null=True, help_text=u'正确答案列表')
    wrong_list = models.CharField(u'错误答案列表', max_length=10000, blank=True, null=True, help_text=u'错误答案列表')
    total_num = models.IntegerField(u'总数', default=0, help_text=u'总共数量')
    score = models.FloatField(u'得分', default=0, help_text=u'分数')

    class Meta:
        verbose_name = u'比赛问题记录'
        verbose_name_plural = u'比赛问题记录'