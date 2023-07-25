#!/usr/bin/env python37
# _*_ coding:utf-8 _*_
"""
Author : 'Shining'
Date:2019-11-21
Describe:develop interface with auth
"""


from django.contrib import auth as django_auth
import base64
from django.http import JsonResponse
from sign.models import Event, Guest
from django.core.exceptions import ObjectDoesNotExist, ValidationError
import time, hashlib, json
from Crypto.Cipher import AES


# AES encrypt algo
BS = 16
unpad = lambda s : s[0: - ord(s[-1])]


def decryptBase64(src):
    return base64.urlsafe_b64decode(src)

def decryptAES(src, key):
    """analysis AES  secret"""
    src = decryptBase64(src)
    iv = b"1172311105789011"
    cryptor = AES.new(key, AES.MODE_CBC, iv)
    text = cryptor.decrypt(src).decode()
    return unpad(text).encode("utf-8")

def aes_encryption(request):

    app_key = b"W7v4D60fds2Cmk2U"

    if request.method == "POST":
        data = request.POST.get("data", '')
    else:
        return "error"

    # deciphering
    decode = decryptAES(data, app_key)
    # transfer to dict
    dict_data = json.loads(decode)
    return dict_data


# user authorize
def user_auth(request):
    get_http_auth = request.META.get('HTTP_AUTHORIZATION',b'')
    auth = get_http_auth.split()
    try:
        auth_parts = base64.b64decode(auth[1]).decode('utf8').partition(':')
    except IndexError:
        return 'null'
    username, password = auth_parts[0], auth_parts[2]
    user = django_auth.authenticate(username=username, password=password)
    if user is not None:
        django_auth.login(request,user)
        return "success"
    else:
        return 'fail'


# user sign and timestamp
def user_sign(request):

    if request.method == "POST":
        client_time = request.POST.get('time','')
        client_sign = request.POST.get('sign','')
    else:
        return "error"

    if client_time == '' or client_sign == '':
        return 'sign null'

    # server time
    now_time = time.time()
    server_time = str(now_time).split('.')[0]
    # get time sub
    time_difference = int(server_time) - int(client_time)
    if time_difference > 60:
        return 'timeout'

    # sign check
    md5 = hashlib.md5()
    sign_str = client_time + "&Guest-Bugmaster"
    sign_bytes_utf8 = sign_str.encode(encoding="utf8")
    md5.update(sign_bytes_utf8)
    server_sign = md5.hexdigest()

    if server_sign != client_sign:
        return 'sign fail'
    else:
        return 'sign success'


# add event interface with sign and timestamp
def sec_add_event(request):
    sign_result = user_sign(request)
    if sign_result == 'error':
        return JsonResponse({'status': 10011, 'message': 'request error'})
    elif sign_result == 'sign null':
        return JsonResponse({'status': 10012, 'message': 'user sign null'})
    elif sign_result == 'timeout':
        return JsonResponse({'status': 10013, 'message': 'user sign timeout'})
    elif sign_result == 'sign fail':
        return JsonResponse({'status': 10014, 'message': 'user sign error'})

    eid = request.POST.get('eid', '')
    name = request.POST.get('name', '')
    limit = request.POST.get('limit', '')
    status = request.POST.get('status', '')
    address = request.POST.get('address', '')
    start_time = request.POST.get('start_time', '')

    if eid == '' or name == ''or limit == ''or address == '' or start_time=='':
        return JsonResponse({'status':10021,'message': 'parameter error'})

    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status': 10022, 'message': 'event id already exists'})

    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({'status': 10023, 'message': 'event name already exists'})
    if status == '':
        status = 1

    try:
        Event.objects.create(id=eid, name=name, limit=limit,address=address,status=int(status),start_time=start_time )
    except ValidationError as e:
        print(e)
        error = 'start_time format error. It must be in YYYY-MM-DD HH:MM:SS format.'
        return JsonResponse({'status': 10024, 'message': error})
    return JsonResponse({'status': 200, 'message': 'add event success'})


# query event interface ----add user authorize
def get_event_list(request):
    auth_result = user_auth(request)
    if auth_result == "null":
        return JsonResponse({'status':10011, 'message':'user auth null'})

    elif auth_result == 'fail':
        return JsonResponse({'status':10012, 'message':'user auth fail'})

    eid = request.GET.get('eid', '')
    name = request.GET.get('name', '')

    if eid == '' and name == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})

    elif eid != '':
        event = {}
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})
        else:
            event['name'] = result.name
            event['limit'] = result.limit
            event['status'] = result.status
            event['address'] = result.address
            event['start_time'] = result.start_time
            return JsonResponse({'status': 200, 'message': 'success'})

    elif name != '':
        datas = []
        result = Event.objects.filter(name__contains=name)
        if result:
            for r in result:
                event = {}
                event['name'] = r.name
                event['limit'] = r.limit
                event['status'] = r.status
                event['address'] = r.address
                event['start_time'] = r.start_time
                datas.append(event)
            return JsonResponse({'status': 200,'message': 'success', 'data': datas})
        else:
            return JsonResponse({'status':10022, 'message': 'query result is empty'})


# query guest interface with AES encrypt
def get_guest_list(request):
    dict_data = aes_encryption(request)
    print(dict_data)
    if dict_data == "error":
        return JsonResponse({'status':10011, 'message':'request error'})

    # fetch eid and phone from dict_data
    eid = dict_data['eid']
    phone = dict_data['phone']

    if eid == '':
        return JsonResponse({"status": 10021, 'message': 'eid cannot be empty'})

    if eid != '' and phone == '':
        datas = []
        results = Guest.objects.filter(event_id=eid)
        if results:
            guest = {}
            for r in results:
                guest['realname'] = r.realname
                guest['phone'] = r.phone
                guest['email'] = r.email
                guest['sign'] = r.sign
                datas.append(guest)
            return JsonResponse({'status': 200, 'message': 'success', 'data': datas})
        else:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})

    if eid != '' and phone != '':
        guest = {}
        try:
            result = Guest.objects.get(phone=phone,event_id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})
        else:
            guest['realname'] = result.realname
            guest['phone'] = result.phone
            guest['email'] = result.email
            guest['sign'] = result.sign
            return JsonResponse({'status': 200, 'message': 'success', 'data': guest})

