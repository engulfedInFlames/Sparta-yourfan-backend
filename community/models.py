from django.db import models
from django.conf import settings
from django_bleach.models import BleachField
from youtube.models import Channel

class Board(models.Model):
    class RankKindChoices(models.TextChoices):
        DIAMOND = (
            "diamond",
            "다이아몬드",
        )
        GOLD = (
            "gold",
            "골드",
        )
        SILVER = (
            "silver",
            "실버",
        )
        BRONZE = (
            "bronze",
            "브론즈",
        )

    channel = models.ForeignKey(Channel, related_name="channel_board", on_delete=models.CASCADE)
    board_channel_id = models.CharField(max_length=30,blank=True, null=True)
    rank = models.CharField(
        max_length=25,
        choices=RankKindChoices.choices,
        default="bronze",
    )
    is_active = models.BooleanField(default=True)



class Post(models.Model):
    board = models.ForeignKey("community.Board", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = BleachField(allowed_tags=[
        'p', 'b', 'i', 'u', 'em', 'strong', 'a',
        'img', 'h3', 'h4', 'h5', 'h6'])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey("community.Post", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = BleachField(allowed_tags=[
        'p', 'b', 'i', 'u', 'em', 'strong', 'a',
        'img', 'h3', 'h4', 'h5', 'h6'])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
