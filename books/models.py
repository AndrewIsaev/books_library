from django.db import models


# Create your models here.
class Books(models.Model):
    """
    Model to store information about books.

    Attributes:
    title (CharField): The title of the book (maximum 255 characters).
    author (ForeignKey): A foreign key linked to the "Authors" model, representing the book's author.
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


class Comments(models.Model):
    """
    A Django model representing comments associated with books.

    This model stores comments made by users on specific books. It includes
    fields for the book the comment is related to, the user who made the comment,
    the comment text, and the timestamp of when the comment was created.

    Attributes:
        book (ForeignKey): The book to which the comment is related.
        user (ForeignKey): The user who made the comment.
        text (TextField): The text content of the comment.
        created_at (DateTimeField): The timestamp of when the comment was created.

    Methods:
        __str__(): Returns a string representation of the comment, which combines
        the username of the user who made the comment and the creation timestamp.

    Meta:
        verbose_name (str): A human-readable name for a single comment.
        verbose_name_plural (str): A human-readable name for the collection of comments.
    """

    book = models.ForeignKey(
        "books.Books",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    user = models.ForeignKey("core.User", on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.user.username) + str(self.created_at)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
