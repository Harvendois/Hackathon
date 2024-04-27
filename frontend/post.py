from nicegui import ui


def post_page():
    # NOTE dark mode will be persistent for each user across tabs and server restarts
    # ui.dark_mode().bind_value(app.storage.user, "dark_mode")
    # ui.checkbox("dark mode").bind_value(app.storage.user, "dark_mode")

    # w-full class is 100% width
    ui.add_head_html("""
    
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        
        <link rel="icon" href="images/logo.png" type="image/icon type">

        <style>
            .body{
                font-family: SF Pro KR, SF Pro Text, SF Pro Icons, Apple Gothic, HY Gulim, MalgunGothic, HY Dotum, Lexi Gulim, Helvetica Neue, Helvetica, Arial, sans-serif;
            }
            .nav_bar{
                height:fit-content;     
            }
            nav{
                width: 100%;
                height: fit-content;
                margin: auto;
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                z-index: 3;
            }
            #navbar_brand{
                color: #4593fc;
                font-weight: bold;
                transition: 1s;
            }
            #navbar_brand:hover{
                color: plum;
                transition: 1s;
            }
            .nav-item{
                margin: 0 10px;
                cursor: pointer;
                color: black;
                font-weight: bold;
            }
            .nav-item:hover{
                color: blue;
                transition: 0.5s;
                background-color: lightgray;
            }
                         
            .welcome-section{
                padding-top: 5vh;
            }

            .wrapper_div{
                display: flex;
                justify-content: center;
                align-items: center;
                width: 100%;
                
                margin: 0 auto;
                height: 10vh;
                background-color: #4593fc;
            }
            
            .content_wrapper{
                margin-top: 5vh;
            }

            .left_bar{
                height: 30vh;
                margin-top: 10vh;
                margin-left:2vh;
                width: 100%;
                position: sticky;
                top: 15vh;
            }
            .right_bar{
                height: 50vh;
            }
            .internship_wrapper{
                
            }         
            .internships{
                width:60%;
                border-radius: 10px;
                background-color: lightgray;
                border: 1px solid black;
                margin: 0 auto;
            }
            .tabs{
                cursor: pointer;
                text-align: center;
                font-weight: bold;
                font-size: 20px;
                max-height: 5vh;
            }
                                 


                         
                                    /*footer*/
            footer{
                padding-top: 20px;
                width: 100%;
                height: auto;
                /*background-color: rgb(255, 213, 255, 0.2);*/
                background-color: #4593fc;
                color: white;
                font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                font-size: 17px;
            }
            footer > div{
                height: 100%;
                display: flex;
                flex-flow: column nowrap;
                justify-content: center;
                align-items: center;
            }
            #socialmedia_wrapper{
                width: 60%;
                height: auto;
                display: flex;
                flex-flow: row nowrap;
                justify-content: center;
                align-items: center;

            }
            #linkedin, #instagram, #notion, #github{
                border-radius: 50%;
                width: 30px;
                height: 30px;
                margin: 0px 10px;
                margin-bottom: 20px;
            }
            #linkedin{
                background: url('C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\linkedin.png') 50% 50\% /100% 100\%;
            }
            #instagram{
                background: url('C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\instagram.png') 50% 50\% /100% 100\%;
            }
            #notion{
                background: url('C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\notion.png') 50% 50\% /100% 100\%;
            }
            #github{
                background: url('C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\github.png') 50% 50\% /105% 105\%;
            }


        </style>                         
""")

    ui.page_title("IGC: I Got Career")

    # navigation bar
    with ui.grid(columns="1fr").classes("w-full nav_bar"):

        async def getDate():
            time = await ui.run_javascript("new Date().toLocaleString()")
            return time

        ui.html("""<nav class="navbar navbar-expand-md" style="position:fixed; left: 20px; background-color: rgba(255,255,255,0.9)">
        
        <!-- Toggler/collapsibe Button -->
       <a class="navbar-brand" id="navbar_brand" href="#"> I Got Career </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="">
            <span class="navbar-toggler-icon"></span>
        </button>
        
        <!-- Navbar links -->
        <div class="justify-content-end" id="">
            <ul class="navbar-nav">
                <li class="nav-item" onclick="scrollToSection('#hero')">Main</li>
                <li class="nav-item" onclick="scrollToSection('#experience')">My Page</li>                    
            </ul>
            
        </div>
    </nav>""")

    

    # main content
    with ui.grid(columns="1fr 5fr").classes("w-full gap-5 content_wrapper"):
        # tabs section
        with ui.grid(rows="1fr 1fr 1fr 1fr ").classes("gap-2 left_bar"):
            ui.html('<div class="tabs" >My Profile</div>').classes("border p-1")
            ui.html('<div class="tabs" >Events</div>').classes("border p-1")
            ui.html('<div class="tabs" >Employers</div>').classes("border p-1")
            ui.html('<div class="tabs" >Career Center</div>').classes("border p-1")

        # CRUD section
        with ui.grid(rows="60px 1fr").classes("gap-3 internship_wrapper"):
            ui.html(
                '<div class="" style="font-size:30px; text-align:center">Recruitment Post</div>'
            ).classes("")
            with ui.card().tight().classes("right_bar border p-1"):
                with ui.grid(rows='3fr 1fr 3fr').classes("gap-3"):
                    with ui.grid(columns='1fr 1fr').classes("gap-3"):
                        with ui.label('Post Title').classes("border p-1"):
                            ui.input(placeholder="Company Name").classes("border p-1")
                        with ui.label('Post Description').classes("border p-1"):
                            ui.input(placeholder="Job Title").classes("border p-1")                       
                        with ui.label('Post Description').classes("border p-1"):
                            ui.input(placeholder="Job Description").classes("border p-1")

    # footer
    with ui.grid(columns="1fr").classes("w-full"):
        ui.html("""
                <footer>
            <div id="footer">
                <div><i class="fa-solid fa-gear"></i> I Got Career <i class="fa-solid fa-code"></i></div>
                <p style="font-size: 30px;">Make IGC Great Again?</p>
                <div id="socialmedia_wrapper">
                    <a href="https://kr.linkedin.com/in/jungha-j-cho-895211126"><div id="linkedin"></div></a>
                    <a href="https://www.instagram.com/chojungha98/"><div id="instagram"></div></a>
                    <a href="https://www.notion.so/Jungha-s-Home-ea8f7f7e75cd49ffa21bca0988bc71f8"><div id="notion"></div></a>
                    <a href="https://github.com/Harvendois?tab=repositories"><div id="github"></div></a>
                </div>
                <p>Hardcoded by myself &#169; JunghaCho in 2024</p>
                <p>Design Motivated from Matt Farley</p>
            </div>
        </footer>
""").classes("border p-1")
