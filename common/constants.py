# Authentication
PASSWORD_MINIMUM_LENGTH = 8
PASSWORD_MAXIMUM_LENGTH = 100
PASSWORD_HASH_METHOD = 'pbkdf2:sha256'
SALT_LENGTH = 16
EMAIL_MAXIMUM_LENGTH = 254
JWT_ALGORITHM = 'HS256'
JWT_LIFESPAN = 7

# Regex
EMAIL_PATTERN = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
PASSWORD_PATTERN = r'^(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])(?!.*[\s])(?=.{8,})'
