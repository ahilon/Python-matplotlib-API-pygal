import requests
import pygal
from pygal.style import LightenStyle as LS , LightColorizedStyle as LCS

#wykonanie wywołania API i zachowanie otrzymanej odpowiedzi.
url = 'https://api.github.com/search/repositories?q=python&sort=stargazers'
r = requests.get(url)
print("kod stanu: ", r.status_code)
#Umieszczenie odpowiedzi API w zmiennej
response_dict = r.json()
print("Całkowita liczba repozytoriów:", response_dict['total_count'])

#Przetworzenie informacji o repozytoriach.
repo_dicts = response_dict['items']
print("Liczba zwróconych repozytoriów: ", len(repo_dicts))

# Przetworzenie wybranych informacji o repozytoriach
print("\nWybrane informacje o repozytoriach: ")
for repo_dict in repo_dicts:

    print("Nazwa:", repo_dict["full_name"])
    print('Właściciel"', repo_dict['owner']['login'])
    print('Gwiazdki:', repo_dict["stargazers_count"])
    print('Repozytorium:', repo_dict["html_url"])
    print('Utworzone:', repo_dict['created_at'])
    print('Uaktualnione:', repo_dict['updated_at'])
    print('Opis:', repo_dict['description'])


names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['full_name'])

    plot_dict = {
        'value' : repo_dict['stargazers_count'],
        'label' : repo_dict['description'],
        'xlink' : repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)
# Utworzenie wizualizacji.
my_style = LS('#336699', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.force_uri_protocol = 'http'
chart.title = "Oznaczone największą ilością gwiazdek projekty związane z językami programowania w serwisie github"
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')


