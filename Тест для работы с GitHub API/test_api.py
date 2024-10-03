import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Переменные окружения
GITHUB_API_URL = "https://api.github.com"
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")

# Заголовки для авторизации
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def test_create_repo():
    """Тест для создания репозитория"""
    url = f"{GITHUB_API_URL}/user/repos"
    data = {
        "name": REPO_NAME,
        "description": "Test repo for API automation",
        "private": False
    }
    response = requests.post(url, json=data, headers=HEADERS)
    assert response.status_code == 201, f"Ошибка создания репозитория: {response.json()}"

def test_check_repo_exists():
    """Тест для проверки наличия репозитория"""
    url = f"{GITHUB_API_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}"
    response = requests.get(url, headers=HEADERS)
    assert response.status_code == 200, f"Репозиторий не найден: {response.json()}"

def test_delete_repo():
    """Тест для удаления репозитория"""
    url = f"{GITHUB_API_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}"
    response = requests.delete(url, headers=HEADERS)
    assert response.status_code == 204, f"Ошибка удаления репозитория: {response.json()}"
