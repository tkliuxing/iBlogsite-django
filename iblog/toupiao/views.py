#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from iblog.toupiao.models import TouPiao, TouPiaoXiang, TouPiaoJiLu
from iblog.shortcuts.ajax import ajax_success, ajax_error


def toupiao(request, template):
    C = {}
    toupiaos = TouPiao.objects.all().order_by('-start_date')
    p = Paginator(toupiaos, 10)
    try:
        page = p.page(int(request.GET.get('p', 1)))
    except:
        page = p.page(1)
    C['toupiaos'] = page.object_list
    C['pagination'] = page
    return render(request, template, C)


def create_xiangmu(request, toupiao_id):
    return redirect("toupiao")


def plus_one(request, toupiaoxiang_id):
    xiangmu = get_object_or_404(TouPiaoXiang, pk=toupiaoxiang_id)
    jilu = TouPiaoJiLu(
        username="test",
        xiangmu=xiangmu,
        toupiao=xiangmu.toupiao,
        ip_address=request.META.get('REMOTE_ADDR', '0.0.0.0')
    )
    try:
        jilu.save()
    except:
        return ajax_error(u"您已经投票过了!")
    xiangmu.count = xiangmu.count+1
    xiangmu.save()
    return ajax_success()
