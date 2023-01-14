import requests
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .models import User
from backoff import on_exception, expo

class UserView(RetrieveAPIView):
    queryset = User.objects.all()

    @on_exception(expo, requests.exceptions.RequestException, max_tries=5)
    def get(self, request, username):
        user_url = f'https://api.github.com/users/{username}'
        user_response = requests.get(user_url)

        if user_response.status_code == 403:
            raise requests.exceptions.HTTPError(f"GitHub API rate limit exceeded: {user_response.json()}")
        elif user_response.status_code != 200:
            return Response({'error': 'Invalid GitHub username'}, status=404)
        elif user_response.status_code == 500:
            raise requests.exceptions.HTTPError(f"Internal Server Error: {user_response.json()}")
        user_data = user_response.json()
        repos_url = user_data['repos_url']
        repos_response = requests.get(repos_url)
        repos_data = repos_response.json()
        user_data['repositories'] = repos_data
        return Response(user_data)



