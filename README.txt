Stephanie M. Ramos Camacho


En esta asignación tuvimos que simular 3 algoritmos de reemplazo de páginas para obtener conocimiento y experiencia en la administración de memoria para sistemas operativos y otras aplicaciones. Los algoritmos a implementar son: Optimal Replacement Algorithm, Second Chance Algorithm y Working Set Clock Replacement Algorithm.



test1.txt, test2.txt, test3.txt y test4.txt son 4 files que se usó de prueba para los algoritmos (cabe recalcar que no da el mismo número de page faults que se supone, pero está bastante cerca).


IMPORTANTE: Ninguno de los algoritmos da el resultado esperado, al menos hay una idea de lo que se supone que haga, más el algoritmo de Working Set Clock Replacement Algorithm NO corre.

optimal.py
El Optimal Replacement Algorithm debe recibir como parámetro el número de páginas de memoria física y el archivo de secuencia de acceso. Este programa se ejecutará dos veces, el primer tiempo como simulación para aprender cuál es la entrada y la segunda vez para realizar el algoritmo. Para correr el programa se necesita que se escriba de esta manera:
python optimal.py 10 test1.txt
10 es el número de páginas que desea darle y test1.txt es el file de pruba a ejecutarse dentro del progrma. (Para que esto salga tiene que ponerse el path donde está guardado dichos files).

second.py
El Second Chance Algorithm debe recibir como parámetro el número de páginas de memoria física y el archivo de secuencia de acceso. Este programa mantendrá un valor que esperará hasta que se llame dos veces a la página para enviarla al final de la lista (lo que significa que se cargó más recientemente) y cuando no tenga más espacio eliminará el primer elemento de la lista (el significado es el más antiguo cargado) y agregue el nuevo al final.
Para correr el programa se necesita que se escriba de esta manera:
python second.py 10 test1.txt
10 es el número de páginas que desea darle y test1.txt es el file de pruba a ejecutarse dentro del progrma. (Para que esto salga tiene que ponerse el path donde está guardado dichos files).

wsclock.py
El Working Set Clock Replacement Algorithm debe recibir como parámetro el número de las páginas de la memoria física, el tau y el archivo de secuancia de acceso. Se ejecutará un puntero como un reloj para verificar más eficientemente con la página y cuándo se puede modificar.
Para correr el programa se necesita que se escriba de esta manera:
python wsclock.py 10 5 test1.txt
10 es el número de páginas que desea darle, el 5 es el tau que se le va a mandar y test1.txt es el file de pruba a ejecutarse dentro del progrma. (Para que esto salga tiene que ponerse el path donde está guardado dichos files).
