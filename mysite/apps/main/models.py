from django.db import models

class Answer(models.Model):
    answer_text = models.CharField('Відповідь', max_length = 300)

    def __str__(self):
        return self.answer_text

class Value(models.Model):
    value = models.CharField('Відповідь', max_length = 100)

    def __str__(self):
        return self.value
