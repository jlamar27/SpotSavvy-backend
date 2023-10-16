import environ  
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY=env('SECRET_KEY')
DATABASE_URL=env('DATABASE_URL')

print(DATABASE_URL)