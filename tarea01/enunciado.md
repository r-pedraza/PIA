---
title: "Cómo crear una cuenta en GitHub y tu primer repositorio"
subtitle: "Unidad 1 · Tutorial paso a paso"
module: "Programación de Inteligencia Artificial"
code: "PIA · Tarea 1"
author: "Raúl Pedraza León"
date: "2026-11-03"
---

## Resultados de aprendizaje

La unidad de trabajo 01 del módulo no lista resultados de aprendizaje expresos,
solo objetivos. Se recogen literalmente los indicados en el documento
«PIA01.- Introducción a la programación de inteligencia artificial», que son los
que se pueden comprobar con este tutorial:

- Conocer los elementos con los que se relaciona un programador de inteligencia
  artificial en su recorrido por el ecosistema actual.
- Distinguir los distintos espacios al alcance del alumnado en función de la
  etapa laboral o de aprendizaje.
- Identificar los factores más decisivos en el desarrollo de la carrera
  profesional como técnico de inteligencia artificial.

Git y GitHub corresponden al primero de esos elementos: la comunidad y el
ecosistema de herramientas con los que se comparte y publica código.

## Apartado 1. Qué es Git y qué es GitHub

Git es un sistema de control de versiones: guarda el historial de cambios de un
proyecto y permite volver atrás, trabajar en paralelo y fusionar aportaciones.
GitHub es un servicio en la nube que aloja repositorios Git y añade la parte
social y de colaboración (perfiles, incidencias, revisiones de código y forks).

El repositorio es la carpeta del proyecto más su historial. Todo lo demás
—cuenta, repositorio remoto y copia local— se construye alrededor de esa idea.

El tutorial recorre el proceso completo que pide el enunciado: crear la cuenta,
crear el primer repositorio, subir a él este documento en PDF y, por último,
enlazarlo con el equipo para poder trabajar desde la terminal.

## Apartado 2. Crear una cuenta en GitHub

### Paso 1 · Abrir la página de registro

Se accede a **https://github.com** y se pulsa **Sign up**, en la esquina superior
derecha. La página principal ofrece además el campo de correo y el botón
**Sign up for GitHub**, que llevan al mismo formulario.

![Página principal de GitHub, con el botón «Sign up» en la esquina superior derecha y el campo de correo en el centro](capturas/git-1-portada.png){: .media }

### Paso 2 · Rellenar el formulario de alta

El formulario pide cuatro datos y permite adelantar este paso usando una cuenta
de Google o de Apple. Los cuatro campos son:

- **Email**: el correo con el que se verificará la cuenta.
- **Password**: contraseña. GitHub exige un mínimo de 8 caracteres si incluye un
  número y una minúscula, o 15 caracteres en cualquier combinación.
- **Username**: nombre de usuario público. Solo admite caracteres alfanuméricos
  o un guion simple, y no puede empezar ni terminar por guion.
- **Your Country/Region**: país, obligatorio por motivos de cumplimiento.

Se recomiendan dos precauciones: generar una contraseña única para GitHub
—mejor con un gestor de contraseñas y de al menos 15 caracteres— y escribir bien
el correo, porque la cuenta no se activa hasta verificarlo.

![Formulario «Sign up for GitHub» con los campos de correo, contraseña, nombre de usuario y país](capturas/git-2-alta.png){: .media }

### Paso 3 · Comprobar el nombre de usuario

Mientras se escribe, GitHub marca en verde que el nombre está disponible y
bloquea el correo con el que se ha iniciado sesión si se ha usado un proveedor
externo. Conviene elegir un nombre reconocible y estable, porque formará parte de
la dirección de todos los repositorios.

![Formulario con el nombre de usuario ya validado y el país seleccionado](capturas/git-3-validacion.png){: .media }

Al pulsar **Create account** GitHub envía un código de verificación al correo
indicado. Hasta introducirlo no se puede entrar en el panel.

### Paso 4 · Omitir la personalización de la cuenta

Tras verificar el correo, GitHub pregunta para qué se va a usar la cuenta (si se
es alumno o profesor, cuántos años se llevan programando, para qué se quiere usar
y con qué herramientas). Es un cuestionario opcional que solo sirve para
personalizar las recomendaciones.

El enunciado pide omitirlo: se pulsa **skip personalization**, el enlace que
aparece en la parte inferior de la pantalla, y se pasa directamente al panel.

![Paso previo de personalización, con el enlace «skip personalization» en la parte inferior de la pantalla](capturas/git-4-panel.png){: .media }

### Paso 5 · El panel de usuario

Ya en el *dashboard*, la columna izquierda muestra los repositorios —de momento,
«No repositories found»— y el centro ofrece distintas formas de empezar. La más
directa para este tutorial es **Create project**, pero también se puede crear el
repositorio desde el menú superior.

![Panel de GitHub después del primer acceso, todavía sin repositorios](capturas/git-4-panel.png){: .media }

## Apartado 3. Crear el primer repositorio

### Paso 6 · Abrir «New repository»

En la barra superior se pulsa el botón **+** y se elige **New repository**. Las
otras opciones del mismo menú crean incidencias, *gists*, organizaciones o
proyectos; el repositorio es la segunda.

![Menú desplegable del botón «+», con la opción «New repository» resaltada](capturas/git-5-nuevo-repositorio.png){: .media }

### Paso 7 · Configurar el repositorio

El formulario se divide en dos bloques:

- **General**: *Owner* (la cuenta propietaria), *Repository name* y
  *Description*. El nombre debe ser corto y fácil de recordar.
- **Configuration**: visibilidad (**Public** o **Private**), **Add README**,
  **Add .gitignore** y **Add license**.

Para un primer repositorio de pruebas, lo más sencillo es un nombre descriptivo,
visibilidad pública si el contenido no es sensible, README activado —explica el
proyecto y GitHub lo muestra en la portada del repositorio— y `.gitignore`
adecuado al lenguaje. La licencia se puede añadir más adelante.

![Formulario «Create a new repository» con los bloques General y Configuration](capturas/git-6-crear-repositorio.png){: .media }

Al pulsar **Create repository** el repositorio queda creado y accesible en
`https://github.com/<usuario>/<nombre>`.

## Apartado 4. Añadir el archivo PDF al repositorio

El enunciado pide que el primer contenido del repositorio sea un PDF con una
breve explicación de cómo se ha hecho el proceso. Puede ser este mismo documento:
se genera con la plantilla del módulo y se sube a GitHub.

### Paso 8 · Subir el PDF desde la web

Se abre el repositorio recién creado y se pulsa **Add file → Upload files**. Se
arrastra el PDF —o se selecciona con **choose your files**—, se escribe un mensaje
de confirmación, por ejemplo «Añadir el tutorial en PDF», y se pulsa
**Commit changes**. El archivo queda visible en la lista del repositorio.

### Paso 9 · Subir el PDF desde la terminal

Si el repositorio ya está clonado, el mismo resultado se consigue con tres
comandos:

```sh
cp PIA01-Tarea.pdf ruta/ai/repositorio/
git add PIA01-Tarea.pdf
git commit -m "Añadir el tutorial en PDF"
git push
```

Con esto el repositorio contiene el README creado en el paso anterior y el PDF con
la explicación.

## Apartado 5. Enlazar el repositorio con el equipo

Crear el repositorio en la web es el primer paso; para trabajar desde el equipo
hay que clonarlo y autenticarse. Se necesitan Git instalado y una terminal.

### Paso 10 · Comprobar Git y clonar

```sh
git --version
git clone https://github.com/<usuario>/<nombre>.git
cd <nombre>
```

`git clone` descarga el repositorio completo con su historial en una carpeta
local. A partir de ahí, los tres comandos del ciclo básico son:

```sh
git status                 # qué archivos han cambiado
git add .                  # preparar los cambios
git commit -m "mensaje"    # guardarlos en el historial local
git push                   # subirlos a GitHub
```

### Paso 8 · Autenticación

GitHub ya no acepta la contraseña de la cuenta para operaciones de Git desde la
terminal. Hay dos vías:

- **HTTPS con token**: se genera un *personal access token* en *Settings →
  Developer settings → Personal access tokens* y se usa como contraseña cuando
  Git la pida.
- **SSH**: se genera una clave con `ssh-keygen -t ed25519 -C "correo"` y se sube
  la clave pública en *Settings → SSH and GPG keys*.

El token y la clave privada son credenciales personales: no se comparten ni se
suben al repositorio.

## Conclusión

El flujo completo queda en tres piezas: una cuenta en GitHub, un repositorio
creado en la web y una copia local enlazada por `git clone`. Con eso ya se puede
versionar el código de las prácticas del módulo y publicarlo, que es la base para
las unidades siguientes, donde el trabajo se apoya en librerías y servicios
externos.

## Fuentes

- GitHub Docs. *Creating a strong password*.
  https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-strong-password
- GitHub Docs. *Signing up for a new GitHub account*.
  https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github
- GitHub Docs. *Creating a repository*.
  https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
- GitHub Docs. *About authentication to GitHub*.
  https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github
- Git. *git-clone documentation*. https://git-scm.com/docs/git-clone
- Junta de Extremadura, Avanza. *PIA01 · Introducción a la programación de
  inteligencia artificial* (material de la unidad 1).
