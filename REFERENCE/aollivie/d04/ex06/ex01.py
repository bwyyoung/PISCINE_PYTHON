from Page import Page
import elements as e
from elem import Text

if __name__ == '__main__':
    p = Page(e.Html([e.Head([e.Title(Text('{title}'))]), e.Body([e.Div(), e.Div()]) ] ))
    p.write_to_file('base.html')
