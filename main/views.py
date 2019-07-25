from django.shortcuts import render
from board.models import User_info
# Create your views here.

def home(request) :
    return render(request, 'main/home.html')

def login(request) :
    u_id = request.POST['user_id']
    pwd = request.POST['password']
    errMsg = ""
    print(u_id, pwd)
    if User_info.objects.filter(user_id=u_id, password=pwd)and request.session.get('user') == None :
        errMsg = "로그인 성공"
        request.session['user'] = User_info.objects.get(user_id=u_id, password=pwd)
        context = {"errMsg" : errMsg}
        return render(request, 'main/home.html', context)
    else :
        errMsg = "아이디 혹은 패스워드가 틀립니다."
        context = {"errMsg" : errMsg}
        return render(request, 'main/home.html', context)

def logout(request) :
    errMsg = ""
    if request.session.get('user') == False :
        errMsg = "로그인 정보가 없습니다."
        context = {"errMsg" : errMsg}
        return render(request, 'main/home.html', context)
    else :
        user = request.session.pop('user')
        request.session['user'] = None
        errMsg = "정상 로그아웃 되었습니다."
        context = {"errMsg" : errMsg}
        return render(request, 'main/home.html', context)

def user_create(request) :
    if request.method == 'POST' :
        u_id = request.POST['user_id']
        password = request.POST['password']
        errMsg = ""
        try :
            if User_info.objects.get(user_id = u_id) :
                errMsg = "회원가입 실패"
                context = {"errMsg" : errMsg}
                return render(request, "login/user_create.html", context)
        except :
            user_info = User_info(
                user_id = u_id,
                password = password
            )
            user_info.save()
            request.session['user'] = user_info
            errMsg = "회원가입 성공"
            context = {"errMsg" : errMsg}
            return render(request, "main/home.html", context)
    else :
        return render(request, "login/user_create.html")