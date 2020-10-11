import os
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader(__name__, 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

def screen_cleaner(flag):
    if flag:
        os.system('cls' if os.name == 'nt' else 'clear')

def render_template(context=None, template='default.jinja.2', cls=True):
    if not context:
        context = {}
    screen_cleaner
    template = env.get_template(template)
    print(template.render(**context))