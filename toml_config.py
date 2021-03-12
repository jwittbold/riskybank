"""Load configuration from .toml file."""
import toml

# Reads local 'config.toml' file, parses key/value pairs to be loaded as a dictionary for database credentials
with open('config.toml', 'r') as f:
    db_url = toml.load(f, _dict=dict)

