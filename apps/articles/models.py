from django.db import models

# Create your models here.
# Создаю первую модель, они создаются классами, принято писать в единственном числе
#Модель Статьи
class Article(models.Model):
	#Создаю поля Статьии заголовок. CharField == Varchar mysql
	article_title = models.CharField('Название статьи',max_length = 200)
	#Тип данных Textfield для набора текстов более 255 символов
	article_text = models.TextField('Текс Статьи')
	#Тип данных DateTimeField дата время
	pub_date = models.DateTimeField('Дата Публикации')

#Модель комментария
class Comment(models.Model):
	#Прикрепляем коммент к статье используя внешний ключ models.ForeignKey
	#Каскадное удалении всех комментарие в данной статье on_delete
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.CharField('имя автора',max_length = 50)
	comment_text = models.CharField('имя автора',max_length = 150)
