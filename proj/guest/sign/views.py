from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):

    return render(request, "index.html")
    #return HttpResponse("Hello , Django")

#登录动作
def login_action(request):

    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None:   #username == 'admin' and password == 'admin123':
            auth.login(request,user)
            request.session['user'] = username
            #return HttpResponse("Login success!")
            #return HttpResponseRedirect('/event_manage/')
            response = HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user',username,3600) #添加cookie信息到浏览器
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})

# 发布会管理
@login_required
def event_manage(request):
    #username = request.COOKIES.get('user','')  #读取浏览器cookie
    event_list = Event.objects.all()
    username = request.session.get('user','') #读取浏览器session
    return render(request,"event_manage.html",{'user':username,"events":event_list})

#发布会名称搜索
@login_required
def search_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get("name","")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request,"event_manage.html",{"user":username,"events":event_list})

#嘉宾管理
@login_required
def guest_manage(request):
    guest_list = Guest.objects.all().order_by(field_names=id)
    username = request.session.get('user', '')
    paginator = Paginator(guest_list,2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username, "guests": contacts})

#嘉宾名称搜索
@login_required
def search_realname(request):
    username = request.session.get('user','')
    search_name = request.GET.get("realname", "")
    guest_list = Guest.objects.filter(realname__contains = search_name).order_by()
    paginator = Paginator(guest_list,2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username,"guests": contacts})

#签到页面
@login_required
def sign_index(request, eid):
    event = get_object_or_404(Event, id=eid)
    total_guest = len(Guest.objects.filter(event_id=eid))
    signed_guest = len(Guest.objects.filter(event_id=eid, sign='1'))
    return render(request, 'sign_index.html', {'event': event,'total_guest': total_guest,'signed_guest': signed_guest})

#签到动作
@login_required
def sign_index_action(request, eid):
    event = get_object_or_404(Event, id=eid)
    phone = request.POST.get('phone','')
    total_guest = len(Guest.objects.filter(event_id=eid))
    signed_guest = len(Guest.objects.filter(event_id=eid, sign='1'))
    # print(phone)
    try:
        Guest.objects.get(phone=phone)
    except Guest.DoesNotExist:
        return render(request, 'sign_index.html', {'event':event, 'hint': 'phone error.',\
                                                   'total_guest': total_guest,'signed_guest': signed_guest})
    try:
        Guest.objects.get(phone=phone, event_id=eid)
    except Guest.DoesNotExist:
        return render(request, 'sign_index.html', {'event':event, 'hint':"event id or phone error.",\
                                                   'total_guest': total_guest,'signed_guest': signed_guest})
    result = Guest.objects.get(phone=phone, event_id=eid)
    if result.sign:
        return render(request, 'sign_index.html', {'event':event, 'hint':'user has sign in.',\
                                                   'total_guest': total_guest,'signed_guest': signed_guest})
    else:
        Guest.objects.filter(phone=phone,event_id=eid).update(sign='1')
        signed_guest += 1
        return render(request, 'sign_index.html', {'event': event, 'hint': 'sign in success.', 'guest': result,\
                                                   'total_guest': total_guest, 'signed_guest': signed_guest})

#退出登录
@login_required
def logout(request):
    auth.logout(request)          # 退出登录
    response = HttpResponseRedirect('/index/')
    return response