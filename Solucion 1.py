import time 

def espectaculo_zoo(n, m, k, animales, grandezas, apertura, partes):
    animales_grandezas = list(zip(animales, grandezas))
    
    def ordenar(escenas):
        count = [0] * (max(grandezas) + 1)
        for escena in escenas:
            for animal in escena:
                count[grandezas[animales.index(animal)]] += 1
        
        escenas_ordenadas = []
        for i in range(len(count)):
            for j in range(count[i]):
                escenas_ordenadas.append([animal for animal in animales if grandezas[animales.index(animal)] == i])
        
        return escenas_ordenadas
    
    def ordenar_por_grandeza(escenas):
        escenas_ordenadas = []
        for escena in escenas:
            count = [0] * (max(grandezas) + 1)
            for animal in escena:
                count[grandezas[animales.index(animal)]] += 1
            
            sorted_escena = []
            for i in range(len(count)):
                for j in range(count[i]):
                    sorted_escena.append(animales[grandezas.index(i)])
            
            escenas_ordenadas.append(sorted_escena)
        
        return escenas_ordenadas
    

    apertura_ordenada = ordenar_por_grandeza(apertura)
    

    partes_ordenadas = []
    for parte in partes:
        parte_ordenada = ordenar_por_grandeza(parte)
        partes_ordenadas.append(parte_ordenada)
    
    participacion_animales = {}
    for parte in [apertura] + partes:
        for escena in parte:
            for animal in escena:
                if animal in participacion_animales:
                    participacion_animales[animal] += 1
                else:
                    participacion_animales[animal] = 1
    
    max_participacion = max(participacion_animales.values())
    animales_max_participacion = [animal for animal, participacion in participacion_animales.items() if participacion == max_participacion]
    
    min_participacion = min(participacion_animales.values())
    animales_min_participacion = [animal for animal, participacion in participacion_animales.items() if participacion == min_participacion]
    
    suma_total_grandezas = sum(grandezas)
    promedio_grandezas = suma_total_grandezas / (m * k)
    
    print("El orden en el que se debe presentar el espectáculo es:")
    print("apertura =", apertura_ordenada)
    for i, parte in enumerate(partes_ordenadas, start=1):
        print("parte{} =".format(i), parte)
    print("El animal que participó en más escenas dentro del espectáculo fue", animales_max_participacion, "con", max_participacion, "escenas.")
    print("El animal que participó en menos escenas dentro del espectáculo fue", animales_min_participacion, "con", min_participacion, "escenas.")
    print("La escena de menor grandeza total fue la escena", apertura_ordenada[0])
    print("La escena de mayor grandeza total fue la escena", apertura_ordenada[-1])
    print("El promedio de grandeza de todo el espectáculo fue de", promedio_grandezas)

def medir_tiempo(n, m, k, animales, grandezas, apertura, partes):
    inicio = time.time()
    espectaculo_zoo(n, m, k, animales, grandezas, apertura, partes)
    fin = time.time()
    tiempo_total = fin - inicio
    print("La función espectaculo_zoologico se ejecutó en", tiempo_total, "segundos")

# Ejemplo
n = 20
m = 10
k = 10

animales = ["tigre", "león", "jirafa", "elefante", "rinoceronte", "hipopótamo", "cebra", "cocodrilo", "mono", "gorila", "oso", "serpiente", "águila", "loro", "pavo", "ballena", "delfín", "orca", "tiburón", "pingüino"]
grandezas = [5, 6, 4, 7, 8, 3, 2, 6, 5, 7, 4, 3, 2, 4, 3, 9, 8, 6, 7, 5]

apertura = [
    ["león", "tigre", "jirafa", "elefante", "rinoceronte"],
    ["hipopótamo", "cebra", "cocodrilo", "mono", "gorila"],
    ["oso", "serpiente", "águila", "loro", "pavo"],
    ["ballena", "delfín", "orca", "tiburón", "pingüino"],
    ["tigre", "jirafa", "elefante", "rinoceronte", "león"],
    ["cebra", "cocodrilo", "mono", "gorila", "hipopótamo"],
    ["serpiente", "águila", "loro", "pavo", "oso"],
    ["delfín", "orca", "tiburón", "pingüino", "ballena"],
    ["jirafa", "elefante", "rinoceronte", "león", "tigre"],
    ["cocodrilo", "mono", "gorila", "hipopótamo", "cebra"]
]

partes = [
    [["tigre", "jirafa", "elefante", "rinoceronte", "león"], ["hipopótamo", "cebra", "cocodrilo", "mono", "gorila"]],
    [["serpiente", "águila", "loro", "pavo", "oso"], ["ballena", "delfín", "orca", "tiburón", "pingüino"]],
    [["león", "tigre", "jirafa", "elefante", "rinoceronte"], ["delfín", "orca", "tiburón", "pingüino", "ballena"]],
    [["oso", "serpiente", "águila", "loro", "pavo"], ["hipopótamo", "cebra", "cocodrilo", "mono", "gorila"]],
    [["tigre", "jirafa", "elefante", "rinoceronte", "león"], ["ballena", "delfín", "orca", "tiburón", "pingüino"]],
    [["cebra", "cocodrilo", "mono", "gorila", "hipopótamo"], ["serpiente", "águila", "loro", "pavo", "oso"]],
    [["serpiente", "águila", "loro", "pavo", "oso"], ["hipopótamo", "cebra", "cocodrilo", "mono", "gorila"]],
    [["delfín", "orca", "tiburón", "pingüino", "ballena"], ["león", "tigre", "jirafa", "elefante", "rinoceronte"]],
    [["jirafa", "elefante", "rinoceronte", "león", "tigre"], ["cocodrilo", "mono", "gorila", "hipopótamo", "cebra"]],
    [["hipopótamo", "cebra", "cocodrilo", "mono", "gorila"], ["serpiente", "águila", "loro", "pavo", "oso"]]
]



medir_tiempo(n, m, k, animales, grandezas, apertura, partes)