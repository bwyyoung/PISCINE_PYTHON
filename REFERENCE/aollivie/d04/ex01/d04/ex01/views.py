from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def django(request):
    title = "Ex01 : Django, framework web."
    content = "Django est un framework open-source de développement web \
    en Python. Il a pour but de rendre le développement web 2.0 simple et \
    rapide. Pour cette raison, le projet a pour slogan « Le framework web pour \
    les perfectionnistes sous pression ». Développé en 2003 pour le journal \
    local de Lawrence (Kansas), Django a été publié sous licence BSD à partir \
    de juillet 2005. Depuis juin 2008, la Django Software Foundation s'occupe \
    du développement et de la promotion du framework. En plus de \
    cette promotion régulière, des conférences entre développeurs et \
    utilisateurs de Django sont organisées deux fois par an depuis 2008. \
    Nommées DjangoCon, une se déroule en Europe et l'autre aux États-Unis. \
    Plusieurs sites grand public sont désormais fondés sur le framework, \
    dont Pinterest4, Instagram5 ou encore Mozilla6."
    links = {
                'link1': 'http://localhost:8000/ex01/django', 'deslink1': 'Ex01 : Processus d’affichage d’une page statique',
                'link2': 'http://localhost:8000/ex01/affichage', 'deslink2': 'Ex01 : Processus d’affichage d’une page statique',
                'link3': 'http://localhost:8000/ex01/templates', 'deslink3': 'Ex01 : Moteur de template.',
            }
    style = 'ex01/style1.css'
    return render(request, 'ex01/rendu.html', {'title': title,
                                                'content': content,
                                                'links' : links,
                                                'style': style})

def affichage(request):
    title = 'Ex01 : Processus d’affichage d’une page statique.'
    content = 'Les objets HttpResponse standards sont des structures \
    statiques. Ils disposent d’un bloc de contenu pré-rendu au moment \
    de la construction de l’objet, et même si ce contenu peut être modifié, \
    il ne l’est pas dans une forme permettant d’effectuer aisément des \
     modifications. Cependant, il peut parfois être avantageux de permettre \
     à des décorateurs ou des intergiciels de modifier une réponse après sa \
     construction par la vue. Par exemple, on peut vouloir modifier le gabarit \
     utilisé ou ajouter des données supplémentaires dans le contexte. Les \
     objets TemplateResponse permettent justement de faire cela. Au contraire \
      des objets HttpResponse basiques, les objets TemplateResponse conservent \
      les informations de gabarit et de contexte fournis par la vue pour \
      produire la réponse. Le résultat final de la réponse n’est produit \
      qu’au dernier moment, plus tard dans le processus de réponse.'
    links = {
                'link1': 'http://localhost:8000/ex01/django', 'deslink1': 'Ex01 : Processus d’affichage d’une page statique',
                'link2': 'http://localhost:8000/ex01/affichage', 'deslink2': 'Ex01 : Processus d’affichage d’une page statique',
                'link3': 'http://localhost:8000/ex01/templates', 'deslink3': 'Ex01 : Moteur de template.',
            }
    style = 'ex01/style1.css'
    return render(request, 'ex01/rendu.html', {'title': title, 'content': content, 'links' : links, 'style':style})

def templates(request):
    title = 'Ex01 : Moteur de template.'
    content = "le moteur de templating de Django permet de manipuler des \
    variables au sein d'un contenu textuel.\
    if permet en fonction d'une condition d'avoir un comportement different.\
    for permet de repeter une action"
    links = {
                'link1': 'http://localhost:8000/ex01/django', 'deslink1': 'Ex01 : Processus d’affichage d’une page statique',
                'link2': 'http://localhost:8000/ex01/affichage', 'deslink2': 'Ex01 : Processus d’affichage d’une page statique',
                'link3': 'http://localhost:8000/ex01/templates', 'deslink3': 'Ex01 : Moteur de template.',
            }
    style = 'ex01/style2.css'
    return render(request, 'ex01/rendu.html', {'title': title, 'content': content, 'links' : links, 'style':style})
