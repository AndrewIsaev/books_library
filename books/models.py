from django.db import models


# Create your models here.
class Books(models.Model):
    """
    Model to store information about books.

    Attributes:
    title (CharField): The title of the book (maximum 255 characters).
    author (ForeignKey): A foreign key linked to the "Authors" model, representing the book's author and using cascading deletion.
    year (PositiveSmallIntegerField): The year of the book's release.
    description (TextField): Description of the book (optional, can be blank).
    cover (ImageField): The book's cover image (optional, can be blank).

    Methods:
    __str__(): Returns a string representation of the object, which is the book's title.

    Meta:
    verbose_name (str): Human-readable singular name of the model.
    verbose_name_plural (str): Human-readable plural name of the model.
    """

    title = models.CharField(max_length=255)
    author = models.ForeignKey("books.Authors", on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to="covers/", blank=True, null=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Authors(models.Model):
    """
    Model for storing information about authors.

    Attributes:
    name (CharField): The name of the author (maximum 255 characters).
    birthday_date (DateField): The author's date of birth.
    biography (TextField): The author's biography (optional, can be blank).

    Methods:
    __str__(): Returns a string representation of the object, which is the author's name.

    Meta:
    verbose_name (str): Human-readable singular name of the model.
    verbose_name_plural (str): Human-readable plural name of the model.
    """

    name = models.CharField(max_length=255)
    birthday_date = models.DateField()
    biography = models.TextField(blank=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
