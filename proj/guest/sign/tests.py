from django.test import TestCase  #Client
from sign.models import Event,Guest
from django.contrib.auth.models import User


# Create your tests here.
# 测试数据库
class ModuleTest(TestCase):

    def setUp(self):
        Event.objects.create(id=6,name='oneplus 7 Event',status=True,limit=2000,\
                             address="SZ",start_time="2019-10-31 14:14:00")

        Guest.objects.create(realname='ErHa',phone='123123321',email='ErHa@mail.com',\
                             sign=False,event_id=6)

    def test_event_module(self):

        result = Event.objects.get(name='oneplus 7 Event')
        self.assertEqual(result.address, 'SZ')
        self.assertTrue(result.status)

    def test_guest_module(self):

        result = Guest.objects.get(phone='123123321')
        self.assertEqual(result.realname, 'ErHa')
        self.assertFalse(result.sign)

class IndexPageTest(TestCase):

    # def setUp(self):          # 默认调用的是django.test.Client类的方法
        # self.client = Client()

    def test_index_page_renders_index_template(self):
        '''测试index视图'''
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class LoginActionTest(TestCase):
    '''测试登录动作'''

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')

    def test_add_admin(self):
        '''测试添加用户'''
        user = User.objects.get(username='admin')
        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.email, 'admin@mail.com')

    def test_login_action_username_password_null(self):
        '''用户名密码为空'''
        test_data = {'username': '','password': ''}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"username or password error!", response.content)

    def test_login_action_username_password_error(self):
        '''用户名密码错误'''
        test_data = {'username': 'ABC', 'password': '1241'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error!', response.content)

    def test_login_action_success(self):
        '''登录成功'''
        test_data = {'username': 'admin', 'password': 'admin123456'}
        response = self.client.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 302)

class EventManageTest(TestCase):
    '''发布会管理测试'''

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(name='iphone11', limit=2000, address='shenzhen', status=1,start_time='2019-10-31 12:40:00')
        self.login_user = {'username': 'admin', 'password': 'admin123456'}

    def test_event_manage_success(self):
        '''测试发布会iPhone11'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/event_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'iphone11',response.content)
        self.assertIn(b'shenzhen', response.content)

    def test_event_manage_seatch_success(self):
        '''测试发布会搜素'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/search_name/', {'name': 'iphone11'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'iphone11',response.content)
        self.assertIn(b'shenzhen', response.content)


class GuestManageTest(TestCase):
    '''嘉宾管理测试'''

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(id=1, name='P30', limit=3000, address='SZ', status=1, start_time='2019-11-05 15:00:00')
        Guest.objects.create(realname='andy',phone='12345',email='andy@mail.com',sign=0,event_id=1)
        self.login_user = {'username':'admin', 'password': 'admin123456'}

    def test_guest_manage_success(self):
        '''测试嘉宾信息:Andy'''
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/guest_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'andy', response.content)
        self.assertIn(b'12345', response.content)

    def test_guest_manage_search_success(self):
        '''测试搜素嘉宾信息'''
        response = self.client.post('/login_action/',data=self.login_user)
        response = self.client.post('/search_realname/', {'realname': 'andy'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'andy', response.content)
        self.assertIn(b'12345', response.content)

class SignIndexActionTest(TestCase):
    """发布会签到测试"""

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(id=1, name='iphone11', limit=2000, status=1,
            start_time='2019-11-11 12:00:00')
        Event.objects.create(id=2, name='oneplus', limit=2000, status=1,
                             start_time='2019-11-12 12:00:00')
        Guest.objects.create(realname='shing',phone='123456',email='shing@mail.com',
                             sign=0, event_id=1)
        Guest.objects.create(realname='hoho',phone='123457',email='hoho@mail.com',
                             sign=1, event_id=2)
        self.login_user = {'username': 'admin', 'password': 'admin123456'}

    def test_sign_action_phone_null(self):
        """测试手机号为空"""
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/sign_index_action/1/', {'phone': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'phone error.', response.content)

    def test_sign_index_action_phone_or_event_id_error(self):
        """手机号或发布会id错误"""
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/sign_index_action/2/', {'phone': '123456'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'event id or phone error.', response.content)

    def test_sign_index_action_user_sign_has(self):
        """用户已签到"""
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/sign_index_action/2/', {'phone': '123457'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'user has sign in.',response.content)

    def test_sign_index_action_success(self):
        """签到成功"""
        response = self.client.post('/login_action/', data=self.login_user)
        response = self.client.post('/sign_index_action/1/', {'phone': '123456'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'sign in success.', response.content)
