import requests
import json

class RepoScraper:
    def get_repos(self, username):
        main_req = requests.get(f'https://api.github.com/users/{username}/repos')
        data = main_req.json()

        for i in range(0, len(data)):
            lic = 'No license' if not data[i]['license'] else data[i]['license']['name']
            langs = data[i]['language']

            print(str(data[i]['name'])+'| id: '+str(data[i]['id'])+', private: '+str(data[i]['private'])+f', licence: {lic}, langs: {langs}, stars: '+str(data[i]['stargazers_count']))
            print(100*'-')

        return
        
repositories = RepoScraper()
repositories.get_repos('devharry2019')


https://api.github.com/users/devharry2019/followers

https://api.github.com/users/devharry2019/following

