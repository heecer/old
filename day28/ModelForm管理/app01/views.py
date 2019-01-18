from django.shortcuts import render, HttpResponse, redirect
from django import forms
from app01 import models

from django.forms import Form, fields, widgets
from django.forms import ModelForm

import os,time,json

# Create your views here.

class LoginModelForm(ModelForm):
    '''创建数据表单类'''

    class Meta:
        model = models.User  # 数据表对象
        fields = '__all__'  # 数据表所有的字段
        # exclude = ['id']    # 排除字段
        # labels = {'name':'用户名'}
        # help_texts = {'name':'输入用户名'}   # 提示信息
        # widgets = {'name':forms.widgets.Textarea(attrs={'class':'c1'})} #自定义插件
        # error_messages = {
        #     '__all__':{},
        #     'email':{'required':'邮箱不能为空',
        #              'invalid':'邮箱格式错误',}
        # } #错误信息
        # field_classes = {'email':forms.fields.URLField}     # 自定义字段
        # localized_fields = {}   #时区本地化


class LoginForm(Form):
    '''登录表单'''
    # 用户标签
    name = fields.CharField(label='用户名',
                            max_length=32,
                            widget=widgets.Input(attrs={'class': 'user'}),
                            error_messages={'required': '用户名不能为空',
                                            'max_length': '不能超过32个字符'})
    # 密码标签
    password = fields.CharField(label='密码',
                                max_length=16,
                                min_length=6,
                                widget=widgets.PasswordInput(attrs={'class': 'pwd'}),
                                error_messages={'required': '密码不能为空',
                                                'min_length': '不能小于6个字符',
                                                'max_length': '不能大于16个字符', })
    # 邮箱标签
    email = fields.EmailField(label='邮箱',
                              error_messages={'required': '邮箱不能为空',
                                              'code': '邮箱格式不对'})
    # 验证码标签
    # code = fields.ChoiceField(label='验证码',
    #                           choices=models.App.objects.values_list('id','user_app'))
    # def __init__(self,*args, **kwargs):
    #     '''自动更新加载'''
    #     super(LoginForm,self).__init__(*args, **kwargs)
    #     self.fields['code'].choices = models.App.objects.values_list('id','app_name')


def index(request):
    '''index请求处理'''
    # GET请求处理
    if request.method == 'GET':
        LF_obj = LoginModelForm()  # modelform类对象
        return render(request, 'index.html', {'LF_obj': LF_obj})
    # POST请求
    elif request.method == 'POST':
        LF_obj = LoginModelForm(request.POST)
        if LF_obj.is_valid():  # 请求数据验证
            # models.User.objects.create(**LF_obj.cleaned_data) # 创建数据到数据库里
            LF_obj.save()  # 保存数据
            return redirect('http://www.baidu.com')
        else:
            return render(request, 'index.html', {'LF_obj': LF_obj})


def userInfo(request):
    user_list = models.User.objects.all().select_related('user_type')
    return render(request, 'userInfo.html', {'user_list': user_list})


def userEdit(request, nid):
    if request.method == 'GET':
        user_obj = models.User.objects.filter(id=nid).first()
        LF_obj = LoginModelForm(instance=user_obj)
        return render(request, 'user_edit.html', {'LF_obj': LF_obj, 'id': nid})
    elif request.method == 'POST':
        # 提交数据到当前对象表中进行更新
        user_obj = models.User.objects.filter(id=nid).first()
        LF_obj = LoginModelForm(request.POST, instance=user_obj)
        if LF_obj.is_valid():
            LF_obj.save()
        else:
            print(LF_obj.errors.as_json())
        return render(request, 'user_edit.html', {'LF_obj': LF_obj})


def ajax_request(request):
    return render(request, 'ajax_request.html')


def ajax_view(request):
    print(request.POST)
    import json, time
    time.sleep(1)
    ret = {'status': True, 'data': request.POST.get('url', None)}
    # ret = {'status': True, 'data': 'OK'}
    return HttpResponse(json.dumps(ret))


def upload_file(request):
    return render(request, 'upload_file.html')


def upload(request):
    '''上传文件'''
    from django.core.files.uploadedfile import InMemoryUploadedFile
    import os
    if request.method == 'POST':
        file = request.FILES.get('file')
        file_path = os.path.join('static/upload/', file.name)
        f = open(file_path, 'wb')
        for i in file.chunks():
            f.write(i)
        f.close()
        # return HttpResponse('上传完成')
        import json
        ret = {'status': True, 'data': file_path}
        # ret = {'status': True, 'data': 'OK'}
        return HttpResponse(json.dumps(ret))


def checkcode(request):
    return render(request, 'checkcode.html')


from io import BytesIO
from app01.check_code import create_validate_code


def check_code(request):
    '''生成验证码图片'''
    stream = BytesIO()
    img, code = create_validate_code()
    print(img, code)
    img.save(stream, 'PNG')
    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())


def validatecode(request):
    '''验证码验证'''
    if request.method == 'POST':
        code = request.POST.get('check_code')
        print(code)
        if code.upper() == request.session['CheckCode'].upper():
            return HttpResponse('验证成功')
        else:
            return redirect('/checkcode/')


def kindeditor(request):
    '''kindeditor文本编辑器'''
    return render(request, 'kindeditor.html')


def upload_img(request):
    '''后台上传文件处理，并返回'''
    import os, json
    img = request.FILES['imgFile']
    file_path = os.path.join('static/upload/', img.name)
    f = open(file_path, 'wb')
    for i in img.chunks():
        f.write(i)
    f.close()
    dict = {
        'error': 0,
        'url': '/' + file_path,
        'message': '上传失败',
    }
    return HttpResponse(json.dumps(dict))


def file_manager(request):
    """
    文件空间管理
    :param request:
    :return:
    """
    dic = {}
    root_path = 'E:/老男孩/day28/ModelForm管理'  #访问文件夹根目录
    static_root_path = '/static/'
    request_path = request.GET.get('path')
    if request_path:
        abs_current_dir_path = os.path.join(root_path, request_path)

        move_up_dir_path = os.path.dirname(request_path.rstrip('/'))
        print(abs_current_dir_path,move_up_dir_path,end='/n')
        dic['moveup_dir_path'] = move_up_dir_path + '/' if move_up_dir_path else move_up_dir_path

    else:
        abs_current_dir_path = root_path
        dic['moveup_dir_path'] = ''

    dic['current_dir_path'] = request_path
    dic['current_url'] = os.path.join(static_root_path, request_path)

    file_list = []
    for item in os.listdir(abs_current_dir_path):
        abs_item_path = os.path.join(abs_current_dir_path, item)
        a, exts = os.path.splitext(item)
        is_dir = os.path.isdir(abs_item_path)
        if is_dir:
            temp = {
                'is_dir': True,
                'has_file': True,
                'filesize': 0,
                'dir_path': '',
                'is_photo': False,
                'filetype': '',
                'filename': item,
                'datetime': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getctime(abs_item_path)))
            }
        else:
            temp = {
                'is_dir': False,
                'has_file': False,
                'filesize': os.stat(abs_item_path).st_size,
                'dir_path': '',
                'is_photo': True if exts.lower() in ['.jpg', '.png', '.jpeg'] else False,
                'filetype': exts.lower().strip('.'),
                'filename': item,
                'datetime': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getctime(abs_item_path)))
            }

        file_list.append(temp)
    dic['file_list'] = file_list
    return HttpResponse(json.dumps(dic))