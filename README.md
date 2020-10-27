# master-ipr (public)

- Asignatura: Introducción a la Planificación de Robots (IPR)

## Modifications
Se han realizado las siguientes modificaciones con respecto al código original:
- Implementación de algoritmos en un único .py (src/python/algorithms/pathfinding.py). En src/python/algorithms/main_bfs.py se encuentra el algoritmo bfs original.
- El algoritmo bfs se ha adaptado para una mayor optimización y, a su vez, se han implementado el algoritmo best first search.

Además, se han incluido los siguientes extras:
- Extra 1: Se ha implementado también el algoritmo depth first search (en el mismo .py)
- Extra 2: Se han creado dos mapas más (new_maps/*)
- Extra 3: Se ha implementado la opción de pasar como argumento el mapa, las coordenadas de inicio y fin, y el tipo de algoritmo que se quiere utilizar.
- Extra 4: Se calcula el tiempo de ejecución siempre que se hace uso de uno de los algoritmos y se muestra por pantalla después de mostrar la ruta final.
- Extra 5: Se han sustituido los caracteres del código original para que la visualización del mapa sea más sencilla.
- Extra 6: Todos los cambios en el código se han controlado con git y, finalmente, se ha subido a github el trabajo final: https://github.com/piedrahitacarol/master-ipr


#### Run
Para utilizar uno de los algoritmos en el map11, con inicio en (5,4) y fin en (13,20):

```
$ python pathfinding.py --map ROOT/master-ipr/map11/map11.csv --start_x 5 --start_y 4 --end_x 13 --end_y 20 --algorithm ALGORITMO
```

ROOT: Ruta donde se encuentra la carpeta master-ipr
ALGORITMO: Hay que elegir entre 'best', 'breadth' y 'depth'. En caso de no pasar este argumento, se utiliza por defecto el algoritmo best first search.
