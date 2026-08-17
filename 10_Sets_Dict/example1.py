usuarios_registrados = ["Luis", "Ana", "Pedro", "Carlos", "Luis", "Ana"]
usuarios_activos = ["Ana", "Carlos", "Maria", "Pedro"]

registrados = set(usuarios_registrados)
activos = set(usuarios_activos)
#Qué usuarios están registrados y activos.
#Qué usuarios están registrados pero no activos.
#Qué usuarios están activos pero no registrados.

registrados_activos = registrados & activos
registrados_noactivos = registrados - activos
activos_noregistrados = activos - registrados