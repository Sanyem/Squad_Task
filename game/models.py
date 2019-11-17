from django.db import models
from django.conf import settings
from UserAuth.models import *

def upload_profile_pic_path(instance, filename):
    return f'Media/{filename}'

class Image(models.Model):
    pic = models.ImageField(upload_to = upload_profile_pic_path, default = 'Media/index.png')
    is_primary = models.BooleanField(default=False)
    prim = models.ForeignKey("self",on_delete=models.CASCADE,related_name="SecondaryRelation",null=True,blank=True)
    consensus = models.BooleanField(default=False)

    def __str__(self):
        return str( "Primary-->" +  str(self.is_primary) + "-->" + str(self.id))



class GameDetail(models.Model):
    user_1 = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,related_name="GameUser1",null=True)
    user_2 = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,related_name="GameUser2",null=True)
    res_u1 = models.BooleanField(default=False)
    res_u2 = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user_1) + "-->" + str(self.user_2)

class GameQuestions(models.Model):
    game = models.ForeignKey(GameDetail,on_delete=models.CASCADE,related_name="Game",null=False)
    ques = models.ForeignKey(Image,on_delete=models.CASCADE,related_name="GameQuestions",null=False)

    def __str__(self):
        return str(self.game) + "-->" + str(self.ques)

class QuesResponses(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="UserRes",null=False)
    game_ques = models.ForeignKey(GameQuestions,on_delete=models.CASCADE,related_name="GameRes",null=False)
    res = models.ForeignKey(Image,on_delete=models.CASCADE,related_name="Response",null=False)

    def __str__(self):
        return str(self.game_ques)
