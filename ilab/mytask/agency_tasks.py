#-*- coding: utf-8 -*-
from .models import AgencyTask


class TaskAddItem(AgencyTask):
    """
    增加房源量类型任务父类
    子类需要属性:
    max_percent
    min_percent
    """
    def __init__(self, *args, **kwargs):
        super(TaskAddItem, self).__init__(*args, **kwargs)
        self.task_alert_text_format = u"发布%s套以上的房源，当前套餐的人均房源量为%s套，您还差很多哦"

    @property
    def online_item_count(self):
        """在线房源量"""
        return 0

    @property
    def package_max_item_count(self):
        """在线房源量上限"""
        return 20

    @property
    def is_done(self):
        """
        判断条件:
        在线房源量 占 在线房源量上限 的 min% - max%
        """
        if self.max_percent > self.online_item_count * 1.0 / self.package_max_item_count >= self.min_percent:
            return False
        return True

    @property
    def alert_text(self):
        """
        提示文字:
        发布*套以上的房源，当前套餐的人均房源量为*套（当前套餐的90%），您还差很多哦
        """
        return self.task_alert_text_format % (
            int(self.package_max_item_count * self.max_percent),
            int(self.package_max_item_count * 0.9)
        )

    @property
    def done_text(self):
        return "恭喜您已发布%s套房源，要继续努力哦" % self.online_item_count


class TaskAddItem1(TaskAddItem):
    def __init__(self, *args, **kwargs):
        super(TaskAddItem1, self).__init__(*args, **kwargs)
        self.task_weight = 2
        self.task_name = "增加房源量1"
        self.max_percent = 0.2
        self.min_percent = 0.0


class TaskAddItem2(TaskAddItem):
    def __init__(self, *args, **kwargs):
        super(TaskAddItem2, self).__init__(*args, **kwargs)
        self.task_weight = 5
        self.task_name = "增加房源量2"
        self.max_percent = 0.4
        self.min_percent = 0.2


class TaskAddItem3(TaskAddItem):
    def __init__(self, *args, **kwargs):
        super(TaskAddItem3, self).__init__(*args, **kwargs)
        self.task_weight = 7
        self.task_name = "增加房源量3"
        self.max_percent = 0.6
        self.min_percent = 0.4


class TaskAddItem4(TaskAddItem):
    def __init__(self, *args, **kwargs):
        super(TaskAddItem4, self).__init__(*args, **kwargs)
        self.task_weight = 10
        self.task_name = "增加房源量4"
        self.max_percent = 0.8
        self.min_percent = 0.6


class TaskAddPicItem(AgencyTask):
    """
    增加多图房源量类型任务父类
    子类需要属性:
    max_percent
    min_percent
    """
    def __init__(self, *args, **kwargs):
        super(TaskAddPicItem, self).__init__(*args, **kwargs)

    @property
    def online_pic_item_count(self):
        """在线多图房源量"""
        return 0

    @property
    def online_item_count(self):
        """在线房源量"""
        return 20

    @property
    def is_done(self):
        """
        判断条件:
        在线多图房源 占 在线房源 的 min% - max0%
        """
        if self.online_item_count == 0:
            return False
        if self.max_percent > self.online_pic_item_count * 1.0 / self.online_item_count >= self.min_percent:
            return False
        return True


class TaskAddPicItem1(TaskAddPicItem):
    def __init__(self, *args, **kwargs):
        super(TaskAddPicItem1, self).__init__(*args, **kwargs)
        self.task_weight = 3
        self.task_name = "增加多图房源1"
        self.max_percent = 0.6
        self.min_percent = 0.0

    @property
    def alert_text(self):
        """
        提示文字:
        你只有*套房源添加了图片，多图房源的点击量比无图房源点击量平均高51.2%。
        """
        return "你只有%s房源添加了图片，多图房源的点击量比无图房源点击量平均高51.2%%。" % self.online_pic_item_count


class TaskAddPicItem2(TaskAddPicItem):
    def __init__(self, *args, **kwargs):
        super(TaskAddPicItem2, self).__init__(*args, **kwargs)
        self.task_weight = 9
        self.task_name = "增加多图房源2"
        self.max_percent = 0.9
        self.min_percent = 0.6

    @property
    def alert_text(self):
        """
        提示文字:
        还有*套房源没有添加图片，多图房源的点击量比无图房源点击量平均高51.2%。
        """
        return "还有%s套房源没有添加图片，多图房源的点击量比无图房源点击量平均高51.2%%。" % (
            self.online_item_count - self.online_pic_item_count
        )


def gen_tasks(user):
    task_class_list = [
        TaskAddItem1,
        TaskAddItem2,
        TaskAddItem3,
        TaskAddItem4,
        TaskAddPicItem1,
        TaskAddPicItem2,
    ]
    task_obj_list = [i(user) for i in task_class_list]
    task_obj_list = [i for i in task_obj_list if not i.is_done]
    task_obj_list.sort(key=lambda i: i.weight)
    return task_obj_list
