# clean conll files

with open('id-ud-dev.conllu') as f: 
	content = f.readlines()

content = [x for x in content if not x.startswith('#')]

with open('indonesian-dev.conllu', 'w') as p:
	p.write("".join(content))