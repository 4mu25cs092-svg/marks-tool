"""Read KEY=value settings from a .env file."""
def load_env(path=".env"):
settings = {}
with open(path) as handle:
for line in handle:
line = line.strip()
if not line or line.startswith("#"):
continue
key, _, value = line.partition("=")
settings[key.strip()] = value.strip()
return settings
