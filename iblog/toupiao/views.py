#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
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
    if request.method != 'POST':
        return redirect('toupiao')
    new_xiangmu = request.POST.get('new')
    if not new_xiangmu:
        return ajax_error(u"请填写项目名称")
    toupiao = get_object_or_404(TouPiao, pk=toupiao_id)
    toupiaoxiang_name_list = toupiao.xiangmu.all().values_list(
        "name", flat=True)
    if new_xiangmu in toupiaoxiang_name_list:
        return ajax_error(u"该项目已存在")
    user_ip = request.META.get("REMOTE_ADDR", "0.0.0.0")
    xiangmu = TouPiaoXiang(
        toupiao=toupiao,
        name=request.POST.get('new', '未填写'),
        ip_address=user_ip,
    )
    try:
        xiangmu.save()
    except Exception as e:
        return ajax_error(unicode(e))
    return ajax_success()


def plus_one(request, toupiaoxiang_id):
    session_key = request.session.session_key
    xiangmu = get_object_or_404(TouPiaoXiang, pk=toupiaoxiang_id)
    if TouPiaoJiLu.objects.filter(toupiao=xiangmu.toupiao, session_key=session_key):
        return ajax_error(u"您已经投票过了!")
    jilu = TouPiaoJiLu(
        username="test",
        xiangmu=xiangmu,
        toupiao=xiangmu.toupiao,
        ip_address=request.META.get('REMOTE_ADDR', '0.0.0.0'),
        session_key=session_key,
    )
    jilu.save()
    xiangmu.count = xiangmu.count + 1
    xiangmu.save()
    return ajax_success()
