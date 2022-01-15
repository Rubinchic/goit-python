from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = ""
ADMINS = []
IP = 'localhost'  # Тоже str, но для айпи адреса хоста
