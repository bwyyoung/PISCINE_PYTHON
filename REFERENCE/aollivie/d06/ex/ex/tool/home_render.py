from .Rendu import Rendu
from django.shortcuts import render, HttpResponse
from .TipForm import TipForm
from ..models import Tip
import json
import ast

def home_render(request):
    r = Rendu(request)
    if request.method == 'POST':
        # print(request.POST)
        if request.user and request.user.is_authenticated:
            form = TipForm(request.POST)
            if form.is_valid():
                tip = form.save(commit=False)
                tip.auteur = request.user.username
                tip.save()
            for k, v in request.POST.items():
                if v == 'Delete':
                    try:
                        tip = Tip.objects.get(id=k)
                        if tip:
                            tip.delete()
                            print('delete !!!!!!!')
                    except Exception as e:
                        pass
                if v == 'Upvote':
                    tip = Tip.objects.get(id=k)
                    check = False
                    if tip.upvotes != None:
                        print('tip:', tip.upvotes)

                        list_u = ast.literal_eval(tip.upvotes)
                        print('up:', list_u)
                        print('user:', request.user.username)
                        if type(list_u) is list:
                            i = 0

                            for v in list_u:
                                if v == request.user.username:
                                    list_u.pop(i)
                                    check = True
                                i += 1
                    else:
                        list_u = []
                    if check == False:
                        list_u.append(str(request.user.username))
                    print('list_u:', list_u)
                    tip.upvotes = str(list_u)
                    # tip.upvotes = json.dumps(list_u)

                    if tip.downvotes != None:
                        list_p = ast.literal_eval(tip.downvotes)
                        if type(list_p) is list:
                            i = 0
                            for v in list_p:
                                if v == request.user.username:
                                    list_p.pop(i)
                                i += 1
                    else:
                        list_p = []
                    tip.downvotes = str(list_p)
                    tip.save()

                if v == 'Downvote':
                    tip = Tip.objects.get(id=k)

                    if tip.upvotes != None:
                        # print(tip.upvotes)

                        list_u = ast.literal_eval(tip.upvotes)

                        if type(list_u) is list:
                            i = 0
                            for v in list_u:
                                if v == request.user.username:
                                    list_u.pop(i)
                                i += 1
                    else:
                        list_u = []
                    tip.upvotes = str(list_u)

                    if tip.downvotes != None:
                        list_p = ast.literal_eval(tip.downvotes)

                        if type(list_p) is list:
                            i = 0
                            check = False
                            for v in list_p:
                                if v == request.user.username:
                                    list_p.pop(i)
                                    check = True
                                i += 1
                            if check == False:
                                list_p.append(request.user.username)
                    else:
                        list_p = []
                        list_p.append(request.user.username)
                    tip.downvotes = str(list_p)

                    tip.save()
    if request.user and request.user.is_authenticated:
        r.do_form_tip()
    r.do_tip_list()
    return r.do_render()
