from django.shortcuts import render
from . models import Board

# Create your views here. # pk=고유번호

def diary(request) :
    if Board.objects.all() != None :
        boards = Board.objects.all()
        context = {"boards" : boards }
        return render(request, 'board/diary.html', context)
    else :
        return render(request, 'board/diary.html')

def board(request) :
    if request.method == 'POST' :
        title = request.POST.get('title')
        username = request.POST.get('username')
        content = request.POST.get('content')

        if request.session.get('user') == False :
            return render(request, "main/home.html")

        user = request.session['user']

        board = Board (
            title = title,
            username = username,
            content = content,
            User_info = user,
        )
        board.save()
        boards = Board.objects.all()
        context = {"boards" : boards}
        return render(request, 'board/diary.html', context)
    else :
        return render(request, 'board/board.html')

def board_one(request, pk) :
    board = Board.objects.get(pk=pk)
    context = {"board" : board}
    return render(request, "board/board_one.html", context)
    
def board_update(request, pk) :
    if request.POST.get("pwd") == Board.objects.get(pk=pk).password :
        if request.POST.get("title") and request.POST.get("username") and request.POST.get("content"):
            board.title = request.POST.get("title")
            board.username = request.POST.get("username")
            board.content = request.POST.get("content")
            board.save()
            return redirect('board', pk=board.id)
        else :
            board = Board.objects.get(pk = pk)
            context = {"board" : board}
            return render(request, "board/board.html", context)
    else :
        return redirect("board", pk=pk)

def board_delete(request, pk) :
    board = Board.objects.get(pk = pk)
    if request.POST.get("pwd") != board.password :
        return redirect(reverse("board", pk=pk))
    board.delete()
    return redirect(reverse("diary"))