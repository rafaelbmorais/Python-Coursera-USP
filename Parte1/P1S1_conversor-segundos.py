#conversor de segundos

seg = int(input('Por favor, entre com o número de segundos que deseja converter: '))

d = seg//86400
restodia = seg%86400

h = restodia//3600
restohora = restodia%3600

min = restohora//60
restomin = restohora%3600

s = restomin//60
restoseg = restomin%60

print(d, 'dias,', h, 'horas,', min, 'minutos e', restoseg, 'segundos.')
	
