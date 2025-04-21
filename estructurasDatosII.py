import queue

#miCola = queue.Queue()           # Creamos una cola FIFO
#miCola = queue.LifoQueue()       # Creamos una cola LIFO

#miCola = queue.PriorityQueue()      # Creamos una cola con prioridad Priority

# Insertamos elementos en la cola

#miCola.put((3, "Madrid"))                    #  Insertamos elementos en la cola
#miCola.put((1, "Bogotá"))                   #  Insertamos elementos en la cola
#miCola.put((2, "Mexico DF"))         #  Insertamos elementos en la cola

miCola =queue.Queue(4)          # Creamos una cola FIFO con un tamaño maximo de 4 elementos

miCola.put("Madrid")
miCola.put("Bogotá")
miCola.put("Mexico DF")
miCola.put("Buenos Aires")

print(miCola.full())                # Verificamos si la cola esta llena

#print(miCola.get())               #  Obtenemos el primer elemento de la cola si es FIFO si es LIFO obtenemos el ultimo
                                    #si la cola es Priority obtenemos el elemento con mayor prioridad, en este caso es (1, Bogotá)

print("A continuacion se imprimen los elementos restantes en la cola")

for elemento in miCola.queue:
    print(elemento)

print("---------------------------------------------------")

while not miCola.empty():           # Verificamos si la cola esta vacia
    print(miCola.get())             # Obtenemos el primer

