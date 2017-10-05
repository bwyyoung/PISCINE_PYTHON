from Page import Page
import elements as e
from elem import Text

if __name__ == '__main__':
	p = Page(e.Html([e.Head(e.Title(Text('Ex00 : Markdown Cheatsheet.') ) ),
			e.Body(e.Div(e.P(Text("Markdown est un langage de balisage \
			léger créé par John Gruber en 2004. Son but est d'offrir \
			une syntaxe facile à lire et à écrire. Un document formaté \
			selon Markdown devrait pouvoir être publié comme tel, en texte, \
			sans donner l’impression qu’il a été marqué par des balises ou \
			des instructions de formatage. Un document rédigé en Markdown peut \
			être converti facilement en HTML. Bien que la syntaxe Markdown ait \
			été influencée par plusieurs filtres de conversion de texte existants \
			vers HTML — dont Setext1, atx2, Textile, reStructuredText, \
			Grutatext3 et EtText4 —, la source d’inspiration principale est \
			le format du courrier électronique en mode texte."))))]))

	p.write_to_file('index.html')
