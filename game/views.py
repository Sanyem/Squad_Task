from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

def get_ques(game):
    game_ques = GameQuestions.objects.filter(game=game)
    images={}
    for gq in game_ques:
        prim = gq.ques
        sec_images = Image.objects.filter(prim=prim,is_primary=False)
        images[prim] = sec_images
    # print(images)
    return images

def gen_ques(game):
    primary_images = Image.objects.filter(is_primary=True,consensus=False).order_by('?')[:5]
    print(primary_images)
    images = {}
    for prim in primary_images:
        sec_images = Image.objects.filter(prim=prim,is_primary=False)
        images[prim] = sec_images
        gq = GameQuestions()
        gq.game = game
        gq.ques = prim
        gq.save()
        # print(sec_images) 
    # print(primary_images)
    # print(images)
    return images

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def play(request):

    if request.method == "GET":
        try:
            user = request.user
            last_game = GameDetail.objects.filter(Q(user_1=user,res_u1=False) | Q(user_2=user,res_u2=False))
            print(last_game)
            if last_game.count() == 0:
                curr_game = GameDetail.objects.filter(Q(user_2__isnull=True) & ~Q(user_1=user))
                if curr_game.count() == 0:
                    print("curr")
                    game = GameDetail()
                    game.user_1 = user
                    game.save()
                    images = gen_ques(game)
                else:
                    game = GameDetail.objects.get(Q(user_2__isnull=True) & ~Q(user_1=user))
                    game.user_2 = user
                    game.save()
                    images = get_ques(game)
            else:
                print("last")
                game = GameDetail.objects.get(Q(user_1=user,res_u1=False) | Q(user_2=user,res_u2=False))
                print(game)
                images = get_ques(game)
            # print(images)
            
            return render(request, 'game/play.html',{"user":user,"game":game,"images":images})
            # return HttpResponse("Game")
        except Exception as e:
            print(e)
            return HttpResponse(e)
    
    if request.method=="POST":
        try:
            user = request.user
            gid = request.POST.get("game")
            game = GameDetail.objects.get(id=gid)
            game_ques = GameQuestions.objects.filter(game=game)
            for gq in game_ques:
                prim = gq.ques
                sec_images = Image.objects.filter(prim=prim,is_primary=False)
                for sec in sec_images:
                    sid = "secondary_"+str(sec.id)
                    res = request.POST.get(sid)
                    if res==1 or res=="1":
                        qr = QuesResponses()
                        qr.user = user
                        qr.game_ques = gq
                        qr.res = sec
                        qr.save()
            if game.user_1 == user:
                game.res_u1=True
            elif game.user_2 == user:
                game.res_u2=True
            game.save()
            if game.res_u1 and game.res_u2:
                user_1 = game.user_1
                user_2 = game.user_2
                for gq in game_ques:
                    u1 = QuesResponses.objects.filter(game_ques=gq,user=user_1).values_list('res')
                    u2 = QuesResponses.objects.filter(game_ques=gq,user=user_2).values_list('res')
                    # print(set(u1))
                    if set(u1) == set(u2) and bool(set(u1)):
                        prim = gq.ques
                        prim.consensus = True
                        prim.save()
                        res = QuesResponses.objects.filter(game_ques=gq,user=user_1)
                        for r in res:
                            sec = r.res
                            sec.consensus = True
                            sec.save()
                        user_1.score += 1
                        user_1.save()
                        user_2.score += 1
                        user_2.save()

            return HttpResponseRedirect(reverse('UserAuth:profile'))
        except Exception as e:
            print(e)
            return HttpResponse(e)
