from datetime import datetime
now=datetime.now()
print(f"Current date:{now:%Y-%m-%d}")
print(f"Current time:{now:%H:%M:%S}")