from environs import Env

# Create an instance of Env
env = Env()

# Read the environment variables from the .env file
env.read_env()

postgre_settings = {
    "pguser": env("PGUSER"),
    "pgpwd": env("PGPWD"),
    "pghost": env("PGHOST"),
    "pgport": env("PGPORT"),
    "pgdb": env("PGDB"),
}
