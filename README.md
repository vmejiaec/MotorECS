# MotorECS
Motor de Videojuegos con patrón de diseño ECS Entity-Component-System

## ¿Qué es ECS?
ECS (Entity-Component-System) es un patrón de diseño utilizado para estructurar los juegos (especialmente motores de juegos) de forma que:

Separas los datos de comportamiento.

Facilitas el reuso, composición y optimización del código.

## Componentes principales
### 1. Entity (Entidad)
Qué es: una entidad es solo un identificador (como un número o un objeto vacío).

Ejemplo: 
```
player = Entity(1)
```
No contiene datos ni lógica.

## 2. Component (Componente)
Qué es: una estructura de datos (no comportamientos).

Ejemplo: un componente Position tendría x y y; un componente Velocity tendría vx y vy.
```
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```     
Las entidades se “componen” de componentes.

### 3. System (Sistema)
Qué es: una lógica que actúa sobre un conjunto de entidades que tienen ciertos componentes.

Ejemplo: un MovementSystem actualiza la posición de todas las entidades que tienen Position y Velocity.
```
def update_movement(entities, dt):
    for e in entities:
        if e.has(Position) and e.has(Velocity):
            e[Position].x += e[Velocity].vx * dt
            e[Position].y += e[Velocity].vy * dt
```
## ¿Por qué usar ECS?
Modularidad: agregas o quitas funcionalidades a una entidad simplemente agregando o quitando componentes.

Flexibilidad: puedes crear nuevas entidades combinando componentes de diferentes maneras.

Rendimiento: es ideal para procesamiento en paralelo o con cache-friendly data layout (más importante en motores grandes como Unity o Godot).
