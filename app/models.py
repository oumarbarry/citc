from django.db import models
from django.utils import timezone

class ModifierDetailFormation(models.Model):
	id_formation = models.CharField('Id de la formation', max_length=100, primary_key=True, default='')
	title = models.CharField('Titre de la formation', max_length=200)
	head = models.TextField('En-tête (Ruban)')
	body_tr = models.TextField('Contenu des rubriques du Ruban')
	def __str__(self):
		return 'Permet de modifier en detail le contenu de la formation : ' + self.title

	class Meta:
		verbose_name_plural = "Modifier le contenu d'une formation en particulier"

class ModifierListeFormation(models.Model):
	head = models.TextField('En-tête (Ruban) de la liste des formations')
	body_tr = models.TextField('Contenu de la liste des formations')
	def __str__(self):
		return "Permet d'ajouter de nouvelles formations à la liste des formations du CITC"

	class Meta:
		verbose_name_plural = "Modifier la liste des formations du CITC" 

class Events(models.Model):
	id_events = models.CharField("Id de l'Evenement", max_length=100, primary_key=True)
	title = models.CharField('Titre', max_length=200)
	date_pub = models.DateField('Date de publication', default=timezone.now)
	date_time_event = models.DateTimeField("Date et Heure de l'evenement", null=True, blank=True) 
	place_event = models.CharField("Lieu de l'evenement", max_length=200)
	resume_event = models.TextField('Resumé')
	detail_event = models.TextField("Detail")
	def __str__(self):
		return '"'+self.title+'"' + ", publié le " + str(self.date_pub)

	class Meta:
		verbose_name_plural = "Liste des Evenements"

class News(models.Model):
	id_news = models.CharField("Id de l'Article", max_length=100, primary_key=True, default='')
	title = models.CharField('Titre', max_length=200)
	thumb = models.CharField('Thumnail', max_length=300, default='')
	img = models.CharField('Image', max_length=300)
	date_pub = models.DateField('Date de publication', default=timezone.now)
	publisher = models.CharField('Auteur/Publieur', max_length=200)
	resume_news = models.TextField('Resume')
	detail_news = models.TextField('Article complet')
	def __str__(self):
		return "Article : " +'"'+self.title+'"' + ", publié le " + str(self.date_pub)

	class Meta:
		verbose_name_plural = "Listes des News (Articles)"

class ModifierGrille(models.Model):
	title = models.CharField('Titre (Events/News)', max_length=200)
	content = models.TextField('Contenu')
	def __str__(self):
		return str(self.id) +'-'+ 'Permet de modifier la grille bootstrap de la page : ' + self.title

	class Meta:
		verbose_name_plural = "Modifier la grille bootstrap (de news et/ou events)"

class Presentation(models.Model):
	id_citc = models.CharField('Id de la page', max_length=100, primary_key=True, default='')
	title = models.CharField('Titre de la page', max_length=200)
	content_citc = models.TextField('Contenu de la page')
	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = "CITC"

#class Active(models.Model):
	#id_active = models.CharField(max_length=100, primary_key=True, default='')
	#content_active = models.TextField()

class HomeContainer(models.Model):
	title = models.CharField('Titre du Container', max_length=200, default='')
	banner_content = models.TextField('Son Contenu')
	def __str__(self):
		return str(self.id) + '-' + self.title
	class Meta:
		verbose_name_plural = "Modification de certains 'Containers' de la page d'Accueil"

class Temoignages(models.Model):
	content = models.TextField('Contenu du Temoignage')
	name = models.CharField('Nom Complet du Temoigneur', max_length=200)
	degree = models.CharField("Son Niveau d'étude", max_length=200)
	img = models.CharField('Sa Photo de Profil', max_length=300)
	date_pub = models.DateField('Date de publication du Temoignage', default=timezone.now)
	def __str__(self):
		return str(self.id) + '-Temoignage de : ' + self.name

	class Meta:
		verbose_name_plural = "Liste des Temoignages"