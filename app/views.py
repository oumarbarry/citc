from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

def home(request):
	latest_events = Events.objects.all().order_by('date_pub')[:4]
	latest_news = News.objects.all().order_by('date_pub')[:4]
	latest_temoignages = Temoignages.objects.all().order_by('date_pub')[:3]
	mod_banner = HomeContainer.objects.get(id=1)
	mod_sec_banner = HomeContainer.objects.get(id=2)
	mod_brand_banner = HomeContainer.objects.get(id=3)
	return render(request, 'app/home.html', locals())

def formations(request):
	add_liste_f = ModifierListeFormation.objects.get(id=1)
	return render(request, 'app/formations.html', locals())

def detail_formation(request, titre):
	add_detail_f = get_object_or_404(ModifierDetailFormation, id_formation=titre)
	#add_detail_f = ModifierDetailFormation.objects.get(id_formation=titre)
	return render(request, 'app/detail_formation.html', locals())

def events(request):
	mod_grille = ModifierGrille.objects.get(id=1)
	all_events = Events.objects.all().order_by('date_pub')
	paginator = Paginator(all_events, 20)
	page = request.GET.get('page')
	try:
		all_events = paginator.page(page)
	except PageNotAnInteger:
		all_events = paginator.page(1)
	except EmptyPage:
		all_events = paginator.page(paginator.num_pages)

	return render(request, 'app/events.html', locals())

def single_events(request, titre):
	event = get_object_or_404(Events, id_events=titre)
	return render(request, 'app/single_events.html', locals())

def news(request):
	mod_grille = ModifierGrille.objects.get(id=2)
	all_news = News.objects.all().order_by('date_pub')
	paginator = Paginator(all_news, 20)
	page = request.GET.get('page')
	try:
		all_news = paginator.page(page)
	except PageNotAnInteger:
		all_news = paginator.page(1)
	except EmptyPage:
		all_news = paginator.page(paginator.num_pages)

	return render(request, 'app/news.html', locals())

def single_news(request, titre):
	news = get_object_or_404(News, id_news=titre)
	return render(request, 'app/single_news.html', locals())

def citc(request, titre):
	#mod_citc = Presentation.objects.get(id_citc=titre)
	mod_citc = get_object_or_404(Presentation, id_citc=titre)
	return render(request, 'app/citc.html', locals())