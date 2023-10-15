import re

pattern = r'^(?!.*(\d)\1{3})(?:[456]\d{3}-?\d{4}-?\d{4}-?\d{4})$'

print(*['Valid' if bool(re.match(pattern, input()))
      else 'Invalid' for _ in range(int(input()))], sep='\n')