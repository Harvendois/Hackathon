from fastapi import FastAPI
from nicegui import app, ui


def init(fastapi_app: FastAPI) -> None:
    @ui.page("/")
    def show():

        # NOTE dark mode will be persistent for each user across tabs and server restarts
        # ui.dark_mode().bind_value(app.storage.user, "dark_mode")
        # ui.checkbox("dark mode").bind_value(app.storage.user, "dark_mode")

         # w-full class is 100% width
        ui.add_head_html('''
    
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
                color: blueviolet;
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
                height: fit-content;
            }
            .welcome, .events{
                height: 20vh;
            }
            .search_bar{
                
                width: 300px;
            }
            .left_bar{
                height: 90vh;
                margin-top: 10vh;
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
                         
            .self_description, #academic_description{
                width: 100%;
                height: 80%;
                box-sizing: border-box;
                margin: 20px auto;
                z-index: 1;
                display: flex;
                flex-flow: column nowrap;
            }
            .about_text{
     
                display: flex;
                justify-content: center;
                text-align: center;
                font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
                font-weight: bold;
                font-size: 20px;
                color: black;
                height: auto;
            }
            .profile_photo{
              
                border-radius: 50%;
                width: 100px;
                height: 100px;
                margin: 10px auto 0 auto;
                z-index: 2;
                border: 1px solid black;
                transition: 0.5s ease-in-out;
            }
            .profile_photo:hover{
                transform: scale(1.2);
            }
                         
                         #skills{
    margin-top: 0vh;
    width: 100%;
    height: 45vh;
    background-color: white;
    display: flex;
    justify-content: center;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

            #skills_wrapper{
    width: 90%;
    height: auto;
    background-color: white;
    border-radius: 10px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    position: absolute;
    z-index: 2;
    margin-top: -20vh;
}
@media screen and ( 768px < width < 1080px){
    #skills{
        height: 35vh;
    }
    #skills_wrapper{
        margin-top: -15vh;
    }
}
@media screen and (max-width: 768px){
    #skills{
        height: 110vh;
    }
    #dev_skills,#gen_skills{
        border-left: 2px solid #E6ECF8;
        border-radius: 10px;
    }
    #eng_skills{
        border-right: 2px solid #E6ECF8;
        border-radius: 10px;
    }
    #skills_wrapper{
        grid-template-columns: repeat(1, 1fr);
    }
}
@media screen and (min-width: 1080px){
    #skills_wrapper{
        margin-top: -23vh;
    }
    #skills{
        height: 20vh;
    }
}
#skills_wrapper > div{
    height: auto;
    border-bottom: 2px solid #E6ECF8;
    border-right: 2px solid #E6ECF8;
}
#skills_wrapper > div:nth-child(1){
    border-left: 2px solid #E6ECF8;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
}
#skills_wrapper > div:nth-child(3){
    border-right: 2px solid #E6ECF8;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
}
/*skills content*/
.skill_title{
    font-size: larger;
    font-weight: bold;
}
.skill_wrapper{
    display: flex;
    flex-flow: column nowrap;
    align-items: center;
    height: auto;
    padding-top: 30px;
    padding-bottom: 30px;
}
.skill_list{
    list-style-type: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-flow: column nowrap;
    align-items: center;
}
.text_wrapper{
    width: 90%;
}
#skills_wrapper p{
    text-align: center;
}
#dev_skills img{
    width: 30px;
    height: 30px;
    margin: 0 auto;
}               

    .mask{
        width: 100%;
        height: 40vh;
        background-color: blueviolet;
        border-radius: 5px;
    }
            
                         

                         #projects{
    background: white;
    color: blueviolet; 
    padding-top: 10px;
    width: 100%;
    height: auto;
}



.project_wrapper{
    display: flex;
    flex-flow: row wrap;
    width: 100%;
    justify-content: space-evenly;
}

.projects{
    background-color: white;
    color: white;
    border: 1px solid #E6ECF8;
    border-radius: 10px;
    height: 270px;
    margin: 20px;
    flex: 0 0 400px;
    z-index: 1;
    transition: .5s;
    position: relative;
}
.project_hover{
    /*for itself*/
    transition: .5s ease-in-out;
    z-index: 2;
    opacity: 0;
    width: 400px;
    height: 270px;
    margin: 20px;
    border-radius: 10px;
    /*for children*/
    display: flex; 
    flex-flow: column nowrap;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    background: #141c3a;
    color: white;
    position: absolute;
}
.project_hover:hover{
    opacity: 1;
}
.project_text{
    text-align: center;
    width: 70%;
    margin-bottom: 5%;
}

/*specific traits*/
#project1{
    background: url('../Images/hero.png');
    background-size: cover;
    background-repeat: no-repeat;
}
#project2{
    background: url('../Images/openai.jpg');
    background-size: cover;
    background-repeat: no-repeat;
}
#project3{
    background: url('../Images/instagram.png');
    background-size: cover;
    background-repeat: no-repeat;
}
/*more projects button*/
#projects_button_wrapper{
    display: flex;
    flex-flow: row nowrap;
    justify-content: center;
    padding: 40px 0px;
}
#more_projects_button{
    background: #141c3a;
    color: white;
    border: black 2px solid;
    transition: .5s;
    
}
#more_projects_button:hover{
    background: white;
    color: black;
    border: black 2px solid;
    transition: 0.5s;
}
                         
                         /*footer*/
footer{
    padding-top: 20px;
    width: 100%;
    height: auto;
    /*background-color: rgb(255, 213, 255, 0.2);*/
    background-color: blueviolet;
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
''')

        ui.page_title('IGC: I Got Career')

       # navigation bar
        with ui.grid(columns='1fr').classes('w-full nav_bar'):
            
            async def getDate():
                time =  await ui.run_javascript('new Date().toLocaleString()')
                return time
            ui.html('''<nav class="navbar navbar-expand-md" style="position:fixed; left: 20px; background-color: rgba(255,255,255,0.9)">
        
        <!-- Toggler/collapsibe Button -->
       <a class="navbar-brand" id="navbar_brand" href="#"> I Got Career </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="">
            <span class="navbar-toggler-icon"></span>
        </button>
        
        <!-- Navbar links -->
        <div class="justify-content-end" id="">
            <ul class="navbar-nav">
                <li class="nav-item" onclick="scrollToSection('#hero')">Main</li>
                <li class="nav-item" onclick="scrollToSection('#about')">Internships</li>
                <li class="nav-item" onclick="scrollToSection('#projects')">Register Internship</li>
                <li class="nav-item" onclick="scrollToSection('#experience')">My Page</li>                    
            </ul>
            
        </div>
    </nav>''')

        # welcome and events
        with ui.grid(columns='2fr 3fr').classes('welcome-section w-full gap-2'):
            with ui.grid(columns='1fr 4fr').classes('w-full'):
                ui.image('C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\yejun.jpg').classes('profile_photo')
                ui.html('''
                    <div id="text_wrapper">

                <div class="self_description" id="basic_description">
                    <div class="about_text"><p>
                        
                        Welcome! Yejun Lee,<br />
                        &#128204; Status: Enrolled, Spring 2024 <br>
                        &#127891; Education: Stony Brook University, B.E. 
                    </p>
                    </div>
                </div>

            </div> 
                ''').classes('welcome border p-1')
                
            ui.image('C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\event_banner.jpg').classes('events border p-1')

        # search bar
        with ui.grid(columns='1fr').classes('wrapper_div gap-2'):
            ui.input(placeholder='Search Any Internship!').props('rounded outlined dense').classes('search_bar')

        # recommendation section mask 
        with ui.grid(columns='1fr').classes('w-full'):
            ui.html('<div class="mask"></div>').classes('')

        # recommendation section
        with ui.grid(columns='1fr').classes('w-full gap-2'):
            ui.html('''
                <section id="skills">
                <div id="skills_wrapper">
                <div class="skill_wrapper" id="eng_skills">
                  <div class="text_wrapper">
                    <p class="skill_emoji">&#128261;</p>
                    <p class="skill_title">Engineering Skills</p>
                    <p class="skill_desc">I am currently learning and researching about ML</p>
                    <p class="skill_title">Engineering Tools I Use</p>
                    <ul class="skill_list">
                        <li>NX10</li>
                        <li>MATLAB</li>
                        <li>R (Big Data Management)</li>
                    </ul>
                  </div>
                </div>
                <div class="skill_wrapper" id="dev_skills">
                  <div class="text_wrapper">
                    <p class="skill_emoji">&#128187;</p>
                    <p class="skill_title">Developer Skills</p>
                    <p class="skill_desc">I am delving into Machine Learning and Neural Networks.</p>
                    <p class="skill_title">Languages I Use</p>
                    <ul class="skill_list">
                        <li>Java & Spring</li>
                        <li>JavaScript (ES6, React JS)</li>
                        <li>Python (Pytorch)</li>
                        <li>OracleSQL XE</li>
                        <li>PL/SQL</li>
                        <li>HTML5&CSS3</li>
                    </ul>
                </div>
                </div>
                <div class="skill_wrapper" id="gen_skills">
                  <div class="text_wrapper">
                    <p class="skill_emoji">&#128204;</p>
                    <p class="skill_title">General Skills</p>
                    <p class="skill_desc">Past Experiences become Current Life Skills</p>
                    <p class="skill_title">Experience I Have</p>
                    <ul class="skill_list">
                        <li>Academic Writing</li>
                        <li>ChatGPT Prompt Engineering</li>
                        <li>Event Management</li>
                        <li>Interpreting/Translating</li>
                        <li>Leadership/Teamwork</li>
                        <li>Public Speaking</li>
                        <li>Teaching/Tutoring/Mentoring</li>
                    </ul>
                  </div>
                </div>
            </div>
            </section>
''')

        # main content
        with ui.grid(columns='1fr 3fr').classes('w-full gap-5'):
            # tabs section
            with ui.grid(rows='1fr 1fr 1fr 1fr 1fr ').classes('gap-2 left_bar'):
    
                ui.html('<div class="tabs" >Internships</div>').classes('border p-1')
                ui.html('<div class="tabs" >Jobs</div>').classes('border p-1')
                ui.html('<div class="tabs" >Events</div>').classes('border p-1')
                ui.html('<div class="tabs" >Mentoring</div>').classes('border p-1')
                ui.html('<div class="tabs" >Career Center</div>').classes('border p-1')

            # internships section
            with ui.grid(rows='60px 1fr 1fr 1fr').classes('gap-3 internship_wrapper'):
                ui.html('<div class="" style="font-size:30px; text-align:center">Internship Posts</div>').classes('')
                with ui.grid(columns='1fr 1fr').classes('internships_wrapper'):
                    
                    # internship 1
                    with ui.card().tight().classes('right_bar border p-1'):
                        ui.image('https://picsum.photos/id/684/640/360')
                        with ui.card_section():
                            ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')

                    # internship 2
                    with ui.card().tight().classes('right_bar border p-1'):
                        ui.image('https://picsum.photos/id/684/640/360')
                        with ui.card_section():
                            ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')
                    
                with ui.grid(columns='1fr 1fr').classes('internships_wrapper'):
                    
                    # internship 3
                    with ui.card().tight().classes('right_bar border p-1'):
                        ui.image('https://picsum.photos/id/684/640/360')
                        with ui.card_section():
                            ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')

                    # internship 4
                    with ui.card().tight().classes('right_bar border p-1'):
                        ui.image('https://picsum.photos/id/684/640/360')
                        with ui.card_section():
                            ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')

                with ui.grid(columns='1fr 1fr').classes('internships_wrapper'):
                    
                    # internship 5
                    with ui.card().tight().classes('right_bar border p-1'):
                        ui.image('https://picsum.photos/id/684/640/360')
                        with ui.card_section():
                            ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')

                    # internship 6
                    with ui.card().tight().classes('right_bar border p-1'):
                        ui.image('https://picsum.photos/id/684/640/360')
                        with ui.card_section():
                            ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')
                    

        # footer
        with ui.grid(columns='1fr').classes('w-full'):
            ui.html('''
                <footer>
            <div id="footer">
                <div><i class="fa-solid fa-gear"></i> Jungha's Website <i class="fa-solid fa-code"></i></div>
                <p style="font-size: 30px;">I try, just to try again.</p>
                <div id="socialmedia_wrapper">
                    <a href="https://kr.linkedin.com/in/jungha-j-cho-895211126"><div id="linkedin"></div></a>
                    <a href="https://www.instagram.com/chojungha98/"><div id="instagram"></div></a>
                    <a href="https://www.notion.so/Jungha-s-Home-ea8f7f7e75cd49ffa21bca0988bc71f8"><div id="notion"></div></a>
                    <a href="https://github.com/Harvendois?tab=repositories"><div id="github"></div></a>
                </div>
                <p>Hardcoded by myself &#169; JunghaCho in 2023</p>
                <p>Design Motivated from Matt Farley</p>
            </div>
        </footer>
''').classes('border p-1')


    ui.run_with(
        fastapi_app,
        mount_path="/",  # NOTE this can be omitted if you want the paths passed to @ui.page to be at the root
        storage_secret="pick your private secret here",  # NOTE setting a secret is optional but allows for persistent storage per user # noqa
    )

