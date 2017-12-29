lang = 'python'
skills = [lang, 'javascript', 'ruby']

print('single quoted')
print("double quoted")
print("""Multi
  Lines.""")
print('Hello from, ' + 'the other side!')

# String Methods

print(lang.lower())
print(lang.upper())
print(lang.capitalize())
print(' python '.strip())
print(lang.isalpha())
print(lang.isdigit())
print(lang.isspace())
print(lang.startswith('py'))
print(lang.endswith('on'))
print(lang.find('th'))
print(lang.replace('thon', ''))
print(lang.split('thon'))
print(', '.join(skills))

# String Slices

print(lang[0:2])
print(lang[2:])
print(lang[:])
print(lang[-1])
print(lang[-1:])
print(lang[:-1])

# String %

print("%d skills: %s and %s and %s" % (3, lang, skills[1], skills[2]))

# Format Function

print("skills: {0}, and {1}".format(lang, skills[1])) 
print(f"skills: {lang}, and {skills[2]}")
