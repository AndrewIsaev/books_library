from django.db import models


# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey("books.Authors", on_delete=models.CASCADE)
    year = models.DateField()
    description = models.TextField(blank=True)
    cover = models.ImageField

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Authors(models.Model):
    name = models.CharField(max_length=255)
    birthday_date = models.DateField()
    biography = models.TextField(blank=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
