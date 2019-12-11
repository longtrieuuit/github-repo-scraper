import requests
import json

class RepoScraper:
    def get_repos(self, username):
        main_req = requests.get(f'https://api.github.com/users/{username}/repos')
        data = main_req.json()

        for i in range(0, len(data)):
            lic = 'No license' if not data[i]['license'] else data[i]['license']['name']
            repo_lang_req = requests.get(f'https://api.github.com/repos/{username}/'+data[i]['name']+'/languages')
            repo_lang_data = repo_lang_req.json()

            print('Name: ' + str(data[i]['name']))
            print('ID: ' + str(data[i]['id']))
            print('Private? ' + str(data[i]['private']))
            print(f'License: {lic}')
            print('Language(s): ' + str(', '.join(repo_lang_data.keys())))

            print(20*'-')
        return

repositories = RepoScraper()
repositories.get_repos('devharry2019')



