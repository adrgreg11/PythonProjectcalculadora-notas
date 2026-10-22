# Practica Guiada Git, Github 
# Antonio De Castro

1. ¿Por qué es mejor hacer dos commits pequeños que uno grande con todo?
Dos commits pequeños son más fáciles de revisar y corregir.


2. Escribe un ejemplo de mensaje de commit malo y explica por qué lo es. 
“Cambios” es un mal mensaje porque no explica qué se hizo. 


3. ¿Qué ventaja tiene trabajar en una rama en lugar de directamente en main? 
Rama: haces cambios aparte y los incorporas a main cuando estén listos.


4. ¿Qué es una fusión fast-forward y por qué se ha producido aquí?
Fast-forward: Git adelanta main porque no hubo cambios nuevos en esa rama.


5. ¿Por qué Git no pudo fusionar automáticamente esta vez y sí en la fase 5?
Git no pudo fusionar porque ambas ramas cambiaron la misma parte del archivo.


6. ¿Qué habría pasado si hubieras pulsado Accept Theirs?
Accept Theirs habría conservado la versión de la otra rama en ese conflicto.


7. En un equipo, ¿por qué conviene hacer Update Project antes de empezar a trabajar cada día?
Conviene hacer Update Project para traer los cambios recientes del equipo antes de empezar. Así reduces conflictos y trabajas con la versión más actual del proyecto.


8. ¿Qué aporta una pull request frente a fusionar directamente en local como en la fase 5? 
Permite revisar y comprobar los cambios antes de fusionarlos.


9. ¿Por qué el commit hecho después de crear la PR apareció en ella sin hacer nada más? 
Aparece automáticamente porque la PR sigue la rama y sus cambios.


10. ¿Qué diferencia hay entre Pop y Apply al recuperar un stash?
Apply recupera los cambios del stash y lo conserva. Pop los recupera y luego elimina el stash si se aplicaron correctamente.


11. ¿Por qué pudiste recuperar borrador.txt si Git nunca lo había guardado?
El stash guardó borrador.txt aunque aún no estuviera en un commit.
