# Default length for shorten url
SHORTEN_URL_LENGTH = 6

# Number of attempts to create a short link of the given length which does not collide with any other in the DB
MAX_GENERATE_SHORT_URL_ATTEMPTS = 100

# If MAX_GENERATE_SHORT_URL_ATTEMPTS is reached, then the SHORTEN_URL_LENGTH is incremented but not higher than this value - MAX_SHORTEN_URL_LENGTH
MAX_SHORTEN_URL_LENGTH = 7

SHORTENED_LINK_PREFIX = "http://localhost:8005/shrt/"
