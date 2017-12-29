skills = ['Python', 'Ruby', 'JavaScript']
more_skills = ['UX', 'Git', 'A11Y', 'Gulp']

print(len(skills))
print(skills[0], skills[-1])

# for, and in

for skill in skills:
  print(skill)
  
if 'Python' in skills:
  print('Got skill!')
  
for i in range(len(skills)):
  print(i)
  
# List Methods

skills.append(more_skills[0])
print(skills)

skills.insert(1, more_skills[1])
print(skills)

skills.extend(more_skills)
print(skills)

print(skills.index('Python'))

more_skills.sort()
print(more_skills)

more_skills.reverse()
print(more_skills)

skills.pop(0)
print(skills)

more_skills.remove('Gulp')
print(more_skills)

# List Slices

print(more_skills[1:-1])
print(more_skills[0:2])
