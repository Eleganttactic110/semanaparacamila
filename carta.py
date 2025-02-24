import os
import webbrowser

# Enlaces de las imágenes de cada día de la semana
images = {
    "lunes": "https://i.ytimg.com/vi/4LMBhhzSl4w/maxresdefault.jpg",
    "martes": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVtXyutRHrQhzIYlEXTLkMgkKpGbu0YFiSYw&s",
    "miércoles": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSusIP0bUgq_-smQex6XL9PXrDKEFmcy33ag&s",
    "jueves": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDSINWclB0NvDZTx2SMSGZJn_0b-373nllkw&s",
    "viernes": "https://i.pinimg.com/originals/b2/62/34/b26234bbaaee98c5fe99c45f193d65d3.jpg",
    "sábado": "https://cdn.pensador.com/es/imagenes/paso-por-aqui-para-desear-que-todo-lo-que-te-pase-hoy-sea-bueno.jpg",
    "domingo": "https://cdn.pensador.com/es/imagenes/feliz-domingo-tomate-el-dia-para-recargar-las-pilas-y-prepararte-para-una-semana-increible.jpg"
}

# Nombres de los archivos de video de cada día de la semana
videos = {
    "lunes": "lunes.mp4",
    "martes": "martes.mp4",
    "miércoles": "miercoles.mp4",
    "jueves": "jueves.mp4",
    "viernes": "viernes.mp4",
    "sábado": "sabado.mp4",
    "domingo": "domingo.mp4"
}

# Código para generar el archivo HTML
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Para Camila</title>
    <style>
        body {{
            position: relative;
            text-align: center;
            font-family: Arial, sans-serif;
            color: darkred; /* Texto en color negro */
        }}
        .background {{
            background: url('{background_gif_url}') no-repeat center center fixed;
            background-size: cover;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0.5; /* Ajustar opacidad para decolorar */
        }}
        .overlay {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(255, 255, 255, 0.1); /* Capa semitransparente */
            z-index: 1;
        }}
        .content {{
            position: relative;
            z-index: 2;
        }}
        .corner-img {{
            position: fixed;
            width: 100px;
            height: 100px;
        }}
        #top-left {{
            top: 10px;
            left: 10px;
        }}
        #top-right {{
            top: 10px;
            right: 10px;
        }}
        #bottom-left {{
            bottom: 10px;
            left: 10px;
        }}
        #bottom-right {{
            bottom: 10px;
            right: 10px;
        }}
        .days img {{
            margin: 10px;
            width: 120px; /* Tamaño uniforme */
            height: auto; /* Mantener la proporción */
            cursor: pointer;
            display: inline-block;
        }}
        .hidden {{
            display: none;
        }}
        #back-button {{
            position: fixed;
            top: 20px;
            left: 120px; /* Movido ligeramente a la derecha */
            cursor: pointer;
            padding: 10px 20px;
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            border-radius: 5px;
            text-align: center;
        }}
        h1 {{
            font-size: 3em;
            margin-top: 70px;
        }}
        h2 {{
            font-size: 2em;
            font-weight: bold;
            color: darkblue; /* Color diferente para h2 */
            margin-top: 20px;
        }}
        p {{
            font-size: 1.2em;
            color: black; /* Color diferente para p */
        }}
        .video-container {{
            display: none;
        }}
        .video-container.active {{
            display: block;
        }}
    </style>
</head>
<body>
    <div class="background"></div>
    <div class="overlay"></div>
    <div class="content">
        <h1>↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑<br>❤Para usted de todo corazón❤</h1>
        <p>🌹Gracias por ver esto y por su tiempo🌹. 👆El mensaje encima de las flechas también es para usted👆. Por favor, haga clic en el corazón para ver el contenido.</p>
        <img src="{envelope_image_url}" alt="Sobre" onclick="openMenu()" style="cursor: pointer; width: 200px; margin-top: 1px;">
        <p>🌹Usted siempre será la más hermosa y la mejor mujer del mundo. La quiero mucho y cuídese siempre. Nunca olvide que estoy incondicionalmente para usted🌹</p>

        <div id="menu" class="hidden">
            <h2>💌Dedicatorias para su semana💌</h2>
            <div class="days">
                {days_images}
            </div>
            <p>💕Le deseo lo mejor en esta semana, recuerde que es mu capaz y se que con su dedicación llegara lejos💕 <br>
            Por favor HAGA CLIK en las imagenes cada dia de la semana para ver que contiene</p>
        </div>

        <img src="https://i.pinimg.com/originals/57/6b/57/576b57e2feea6d162fdae45e8300cf78.gif" id="top-left" class="corner-img">
        <img src="https://i.pinimg.com/originals/57/6b/57/576b57e2feea6d162fdae45e8300cf78.gif" id="top-right" class="corner-img">
        <button id="back-button" onclick="goBack()">Regresar</button>

        <script>
            function openMenu() {{
                document.getElementById('menu').classList.remove('hidden');
                document.querySelectorAll('.video-container').forEach(el => el.classList.remove('active'));
            }}

            function showContent(day) {{
                document.querySelectorAll('.video-container').forEach(el => el.classList.remove('active'));
                document.getElementById(day).classList.add('active');
                document.getElementById('menu').classList.add('hidden');
            }}

            function goBack() {{
                document.querySelectorAll('.video-container').forEach(el => el.classList.remove('active'));
                document.getElementById('menu').classList.remove('hidden');
            }}
        </script>

        <div id="content-container">
            {days_content}
        </div>
    </div>
</body>
</html>
"""

days = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
days_images = ""
days_content = ""

for day in days:
    days_images += f'<img src="{images[day]}" alt="{day}" onclick="showContent(\'{day}\')">'
    days_content += f'''
    <div id="lunes" class="video-container">
        <h2>💖Dedicatoria de lunes para la más amable y talentosa de las mujeres💖.</h2>
        <video width="420" height="340" controls>
            <source src="lunes.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <p>🌅 Que este lunes te llene de energía y entusiasmo para comenzar la semana con fuerza. ¡Tú puedes con todo!. Simepre cuente conmigo incondicionalmente y luche por sus sueños 💪</p>
        <p>Comienza la semana, me gustaria estar ahi con usted ayudandola y apoyandola siempre, si le soy honesto sineto que soy mas fuerte cuando estoy cerca de usted o cuando me da sus palabras de animo, asi que que opina de: yo contigo y tu conmigo (asi se llama la canción)<p>
    </div>
    <div id="martes" class="video-container">
        <h2>💖Dedicatoria de martes para la más amable y talentosa de las mujeres💖.</h2>
        <video width="420" height="340" controls>
            <source src="martes.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <p>🌟 Este martes es una nueva oportunidad para continuar con tus sueños y metas. ¡No te detengas!. Para mi usted es muy importante y me gusta verla luchar por lo qu quiere y me hace admirarla aun mas🚀</p>
        <p>Cree que los humanos lleguemos a marte? No lo se, pueden pasar millones de años, pero si se que mi cariño y respeto por usted es real y que aunque pasen los años nunca la voy a olvidar asi que espero le guste esta canción<p>
    </div>
    <div id="miercoles" class="video-container">
        <h2>💖Dedicatoria de miercoles para la más amable y talentosa de las mujeres💖.</h2>
        <video width="420" height="340" controls>
            <source src="miercoles.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <p>🌈 Ya estamos a mitad de semana. Sigue adelante con determinación y una sonrisa. Su esfuerzo tendra muy buenos resultados, usted llegara lejos, que Dios siempre la bendiga 🌞</p>
        <p>Ya es mitad de semana como pasa el tiempo, siga adelnate usted puede, capaz tiene prueba mañana o deberes asi que gracias por ver esto. estaba pensando y capaz este ocupada y no me dejn entrar a su universidad para ir a verla, pero podria entrar a su corazón? Aún recuerdo la invitación que le hice y espero pronto poder salir ocn usted y de eso se trata la canción<p>
    </div>
    <div id="jueves" class="video-container">
        <h2>💖Dedicatoria de jueves para la más amable y talentosa de las mujeres💖.</h2>
        <video width="420" height="340" controls>
            <source src="jueves.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <p>💫 Este jueves es perfecto para reflexionar sobre tus logros y planear nuevos objetivos. ¡Sigue brillando!, siga siendo la luz que destaca en todo el mundo🌟</p>
        <p>Ya mismo se acaba la semana, espero este bien, y si tiene problemas cuenta conmigo en las buenas y en las malas, sabe extraño hablar con usted y es pro eso esta canción<p>
    </div>
    <div id="viernes" class="video-container">
        <h2>💖Dedicatoria de viernes para la más amable y talentosa de las mujeres💖.</h2>
        <video width="420" height="340" controls>
            <source src="viernes.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <p>🎉 ¡Es viernes! Disfruta de tus logros de la semana y relájate. Te mereces un descanso. 🍹 Talvez si tiene tiempo podria llamarla?</p>
        <p>Esta canción que le dedico es debido al tiempo que paso en el cual pues no pude vovler a verla ni hablar con usted o peor aun decirle lo que siento, quiero que sepa que nunca la voy a olvidar que es un sueño para mi poder volver a hablar con usted<p>
    </div>
    <div id="sabado" class="video-container">
        <h2>💖Dedicatoria de sabado para la más amable y talentosa de las mujeres💖.</h2>
        <video width="420" height="340" controls>
            <source src="sabado.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <p>🌺 Que este sábado te traiga paz, amor y momentos inolvidables. Aprovecha al máximo tu tiempo. ⏳ Disfrute de sus hobbies o actividades que le gusten para relajarse</p>
        <p>Ya es sabado vale descanzar, no le he preguntado si le gusta bailar? jajaj pero bueno esta canción cumple dos funciones decirle como me siento pensandola y asi mismo alegrarle con un poco de cumbia la vida😁<p>
    </div>
    <div id="domingo" class="video-container">
        <h2>💖Dedicatoria de domingo para la más amable y talentosa de las mujeres💖.</h2>
        <video width="420" height="340" controls>
            <source src="domingo.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <p>🌷 Tómate este domingo para recargar energías y prepararte para una semana increíble. ¡Te lo mereces! 🌞 Una nueva semana se aproxima podria llamarla para desearle lo mejor? Siempre la pienso y le deseo que siga adelante y sus metas y sueños se cumplan</p>
        <p>La canción que le dedico para este domingo pues es en base a la superación y que se que nada es facil en la vida y bueno en general siempre hay obstaculos, pero que en cualquier aspecto de su vida que se presenten estos obstaculos no se olvide de seguir adelante, confiar en Dios y luchar. Siempre voy a confiar en usted y apoyarla<p>
    </div>
    '''

html_file_name = "para_camila.html"
with open(html_file_name, "w", encoding="utf-8") as file:  # Especificar la codificación UTF-8
    file.write(html_content.format(
        background_gif_url="https://i.makeagif.com/media/2-14-2021/MAfEOC.gif",
        envelope_image_url="https://www.canalgif.net/Gifs-animados/Amor/Corazones/Gif-animado-Corazon-357.gif",
        days_images=days_images,
        days_content=days_content
    ))

print("Archivo HTML generado exitosamente.")

# Abre el archivo HTML en una pestaña del navegador
file_path = os.path.abspath(html_file_name)
webbrowser.open(f"file://{file_path}")
