
def getHtmlContent(groupLink):
    return f'''
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <style>
                body{{
                    margin: 0;
                }}
                .container{{
                    color: black;
                    background-color: white;
                    font-family: Calibri, sans-serif;
                    padding: 40px;
                    text-align: left;
                }}
                .icon{{
                    height: 150px;
                    margin: auto;
                    display: block;
                }}
                h1{{
                    color: black;
                    text-transform: uppercase;
                    text-align: center;
                }}
                button{{
                    border: none;
                    display: block;
                    padding: 10px 15px;
                    margin: auto;
                    cursor:pointer;
                    border-radius:10px;
                    background-color:#1ea851;
                    font-size:20px;
                }}
                p{{
                    font-size: 18px;
                    color: black;
                }}
            </style>
        </head>
        <body>
        <div class="container">
            <img class="icon" src="https://i.ibb.co/Wg3dkTz/423240183-361800789943947-8451744917290406324-n-removebg-preview.png" alt="423240183-361800789943947-8451744917290406324-n-removebg-preview" border="0"></a>
            <h1>Welcome to the Dev Day'24 team</h1>
            <p>
                Excited to have you join Developers' Day 2024! Attached is your official appointment letter. Click below to instantly join our WhatsApp group. Happy coding!
            </p>
            <button>
                <a href="https://chat.whatsapp.com/FiYIc117ELX1PjQzIDaDcW" style="color: white; text-decoration: none;">Whatsapp group</a> 
            </button>
        </div>
        </body>
    </html>
    '''