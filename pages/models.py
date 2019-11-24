from django.db import models


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

class Match(models.Model):
    id = models.IntegerField(primary_key=True)
    datetime = models.DateTimeField()
    queue = models.IntegerField()
    p1_duel_tier = models.IntegerField()
    p1_win_status = models.CharField(max_length=6)
    p1_god = models.ForeignKey(God, on_delete=models.CASCADE, related_name="p1_god")
    p1_active_1 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="p1_active_1")
    p1_active_2 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="p1_active_2")
    p1_item_1 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="p1_item_1")
    p1_item_2 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="p1_item_2")
    p1_item_3 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="p1_item_3")
    p1_item_4 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="p1_item_4")
    p1_item_5 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="p1_item_5")
    p1_item_6 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="p1_item_6")
    p1_name = models.CharField(max_length=80)
    p2_duel_tier = models.IntegerField()
    p2_win_status = models.CharField(max_length=6)
    p2_god = models.ForeignKey(God, on_delete=models.CASCADE, related_name="p2_god")
    p2_active_1 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="p2_active_1")
    p2_active_2 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="p2_active_2")
    p2_item_1 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="p2_item_1")
    p2_item_2 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="p2_item_2")
    p2_item_3 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="p2_item_3")
    p2_item_4 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="p2_item_4")
    p2_item_5 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="p2_item_5")
    p2_item_6 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="p2_item_6")
    p2_name = models.CharField(max_length=80)


    def __str__(self):
        return f'<Match Record> Match Id: {self.id} Player1: {p1_name}, {p1_god.name}, {p1_win_status}' \
               f' | Player2: {p2_name}, {p2_god.name}, {p2_win_status}'