from django.db import models

from hirez_connect import TIER


class God(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    icon_url = models.CharField(max_length=255)


    def __str__(self):
        return f'<God Record> Name: {self.name}  id: {self.id}'


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    icon_url = models.CharField(max_length=255)


    def __str__(self):
        return f'<Item Record> Name: {self.name}  id: {self.id}'


class Build(models.Model):
    match_datetime = models.DateTimeField()
    queue = models.IntegerField()
    player_name = models.CharField(max_length=80)
    duel_tier = models.IntegerField()
    opponent_tier = models.IntegerField()
    winner = models.BooleanField()
    god = models.ForeignKey(God, on_delete=models.CASCADE, related_name="god")
    opponent = models.ForeignKey(God, on_delete=models.CASCADE, related_name="opponent")
    active_1 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="active_1")
    active_2 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="active_2")
    item_1 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_1")
    item_2 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_2")
    item_3 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_3")
    item_4 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_4")
    item_5 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_5")
    item_6 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_6")

    def __str__(self):
        player_name = self.player_name if self.player_name != "" else "Unknown"
        return f'<Build Record> Win?: {self.winner} Tier:{TIER[self.duel_tier]} Player:{player_name} ' \
               f'God:{self.god.name} Opponent:{self.opponent.name}'


class Match(models.Model):
    table_name = "matches"
    id = models.IntegerField(primary_key=True)
    match_datetime = models.DateTimeField()
    queue = models.IntegerField()
    p1_build = models.ForeignKey(Build, on_delete=models.CASCADE, related_name="p1_build")
    p2_build = models.ForeignKey(Build, on_delete=models.CASCADE, related_name="p2_build")

    def __str__(self):
        return f'<Match Record> Match Id: {self.id} Player1: name-{self.p1_build.player_name}, god-{self.p1_build.god.name}, winner-{self.p1_build.winner}' \
               f' | Player2: name-{self.p2_build.player_name}, god-{self.p2_build.god.name}, winner-{self.p2_build.winner}'

