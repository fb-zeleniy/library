from django.core.validators import MinLengthValidator
from django import forms
from .models import Book, Review


class BookForm(forms.ModelForm):
    slug = forms.SlugField(
        label="Уникальный идентификатор",
        help_text="Уникальный идентификатор книги, используемый в URL",
        max_length=10,
        required=True,
        error_messages={
            "max_length": "Уникальный идентификатор не должен превышать 10 символов.",
        }
    )

    name = forms.CharField(
        label="Название книги",
        max_length=200,
        validators=[MinLengthValidator(2)],
        error_messages={
            "validators": "Минимальная длина названия книги — 2 символа.",
        }
    )

    author = forms.CharField(
        label="Автор книги",
        max_length=100,
    )

    genre = forms.CharField(
        label="Жанр книги",
        widget=forms.TextInput(attrs={"size": 40, "placeholder": "Введите жанр книги"}),
    )

    year = forms.DateField(
        label="Год выпуска",
        widget=forms.SelectDateWidget(years=range(1900, 2025)),
    )

    class Meta:
        model = Book
        fields = ['slug', 'name', 'genre', 'author', 'year']


class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(
        label='Ваша оценка',
        widget=forms.RadioSelect(choices=Review.RATING_CHOICES),
    )

    class Meta:
        model = Review
        fields = ('rating', 'comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Ваш отзыв (необязательно)'}),
        }
