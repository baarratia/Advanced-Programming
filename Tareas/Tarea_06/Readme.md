Tarea 6
==========

Bienvenidos a la guia de usuario de Ichat beta:


***Instrucciones de uso:***

Para iniciar el programa, se debe ejecutar el archivo StartServer.py y el archivo Lobby.py por cada
usuario que se desee conectar, recomendamos probar con dos o 3 usuarios conectados, ya que si no
el chat puede ser un tanto solitario...

**Primeros Pasos:**


        Registrarse:   Como todo servicio de mensajer�a, Ichat pide a los usuarios registrarse
                       antes de poder usar sus servicios, por lo que al iniciar el programa
                       por primera vez, en la ventana inicial, de LogIn, se debe pinchar en
                       Registrar Nuevo Usuario.
                       Tras esto surgir� una nueva ventana, donde deber�s ingresar tus datos y
                       contrase�a. Recordar que Ichat es un servicio de mensajer�a auspiciado
                       por la PUC, por lo que tu nombre de usuario debe ser tu correo uc, es decir
                       debe terminar en "@puc.cl" o "@uc.cl", mientras que la contrase�a ingresada
                       debe tener al menos 8 car�cteres, una Mayuscula, M�nusculas y al menos 1
                       n�mero.


        Iniciar Sesi�n:  Si es primera vez que usas el programa, al momento de registrarte se iniciar�
                         la sesi�n autom�ticamente, en el caso de que est�s registrado de antes, deber�s
                         escribir tu correo uc y contrase�a, si estos son v�lidos el servidor te permitir�
                         iniciar sesi�n correctamente, y podr�s ingresar al Lobby del chat.
                         Como esta todav�a es una versi�n beta del programa, si te equivocas ingresando tus
                         datos, te mostratr� un mensaje de advertencia, pero al momento de intentar nuevamente
                         el programa no podr� acceder al servicio, por lo que en estos casos se recomienda
                         cerrar y volver a iniciar el archivo Lobby.py, para un correcto funcionamiento,
                         sentimos las molestias.

        Lobby:    En el Lobby podr�s encontrar toda la informaci�n y botones claves para tu interacci�n con
                  el programa y el resto de los usuarios. Cuenta con dos QListViews, una que muestra las
                  conversaciones y grupos activos, y otra que meustra los usuarios conectados.
                  Si un usuario te habla, su nombre aparecer� en la lista de conversaciones activas, y con
                  solo pinchar el nombre podr�s abrir la Ventana del chat correspondiente y poder comunicarte.
                  Si en cambio, eres alguien que toma la iniciativa, para iniciar una conversaci�n tu mismo
                  bastar� con presionar sobre el nombre de un usuario en la lista de usuarios conectados,
                  lo que generar� autom�ticamente un a pesta�a de conversaci�n.

                  Por otro lado, si eres un ser m�s sociable todav�a, y no te basta solo con hablar con una
                  persona, Ichat ofrece la opci�n de chats grupales. Basta con presionar el bot�n Nuevo Grupo
                  donde podr�s marcar a los usuarios actualmente conectados con los que deseas hablar, pero
                  siempre recuerda nombrar al grupo, ya que si no, no podr�s crearlo.
                  Con el grupo ya creado, podr�s contar con las mismas ventajas del chat entre dos personas,
                  pero incluyendo tantas personas como desees a la conversaci�n.

        Pesta�as de Chat:       Tanto en las pesta�as de chat b�sico como en las grupales los funcionamientos
                                son parecidos, escribe lo que deseas comunicar, presiona enviar y el destinatario
                                lo recibir�.
                                Adem�s estamos implementando una nueva tecnolog�a en colaboraci�n con Google (si,
                                Google), donde si quieres puedes escribir una palabra entre $$, por ejemplo,
                                si quieres mandr una imagen de Godzilla, basta con que escribas $$Godzilla$$
                                y tu destinatario se llevar� un gran susto, ya que aparecer� una imagen del
                                mismisimo en su pantalla, esta tecnoog�a est� a�n en desarrollo, por lo que
                                como compa��a pedimos paciencia, ya lanzaremos una actualizaci�n que mejore
                                el funcionamiento, agradecemos la comprensi�n de nuestro p�blico.

        Cerrar Sesi�n:      Como su nombre lo dice, este bot�n te permite cerrar sesi�n de nuestro servicio,
                            aunque todav�a no encontramos una raz�n por no estar todo el d�a conectado a esta
                            tan innovadora plataforma... (Perder�s tus conversaciones actuales si cierras sesi�n,
                            m�s razones por la que no cerrar nunca el programa...)


***Organizaci�n del C�digo***

La estructura creada est� bastante ordenada y separada por m�dulos por tem�tica para poder
hacer m�s f�cil la correcci�n por parte de los Ayudantes.


        Ichat.py:   Base de conectividad del programa, aqu� podremos encontrar las clases
                 Cliente y Servidor, con sus respectivos atributos, m�todos y se�ales
                 para poder interactuar correctamente con las interfaces.

        Manejo_de_informacion.py:       En este archivo podremos encontrar todo lo relacionado
                                        con la importante seguridad de nuestros usuarios, aqu�
                                        se maneja la creaci�n de nuevos usuarios, el cuidadoso
                                        guardado de sus contrase�as usando hash+salt para asegurarlas.
                                        Tambi�n es donde se comprueban que los datos ingresados
                                        por el usuario al momento de iniciar sesi�n se�n correctos
                                        y de ser as�, se pueda ingresar al servicio.
                                        En esta parte se usa regex (re) para el manejo de strings,
                                        tal como se pide.

        Buscar_Imagenes.py:     Como puede hacer suponer el nombre, este archivo se encarga de gurdar
                                las funciones que, dado el mensaje que se envia en un chat, verifican
                                si existe alguna palabra entre $$ y si es as�, usando request y la api
                                de google images, busca y descarga la imagen solicitada, retornando
                                el nombre de esta, para que luego la ventana de chat la pueda setear
                                como miniatura en la Qtextbrowser que poseen todos los chats.

        Lobby.py:     El lobby es tanto el centro de operaciones del usuario, como del programa, en este se
                   ejecutan todas las funciones y ventanas, y, como hab�a comentado antes, es necesaria la ejecuci�n
                   de este para poder iniciar el porgrama desde la perspectiva del usuario.

        StartServer.py:     Programa simple que importa y ejecuta el server, para que los usuarios puedan conectarse
                            al servicio.

         Otros:         El resto de los archivos son m�s que nada interfaces gr�ficas con sus respectivos botones
                        y se�ales conectadas y listas para aportar en el funcionamiento del programa.

Finalmente, ayudantes, no me dio el tiempo para poder adjuntar archivos (consideren que estamos en periodo de examenes
y hay que salvar todo...) pero nuestra compa��a espera mandar una actualizaci�n en un tiempo...
Otra cosa, para que no tengan que registrar varios usuarios para probar, dej� ya guardados unos usuarios de ejemplo
con los que se pueden conectar y probar, estos son:

ejemplo@uc.cl pass= Ejemplo123
ejemplo2@puc.cl pass = Ejemplo456
cbcornejo@uc.cl pass = Cata123
f@uc.cl pass = Francisco1
