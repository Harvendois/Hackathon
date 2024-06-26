from nicegui import ui


def main_page():
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
            .navbar{
                height:fit-content;     
                position:fixed; 
                top:0;
                height: 9vh;
                background-color: rgba(0,33,71,0.9);
                z-index: 5;
                border-radius: 10px;
                
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
            .navbar-brand{
                color: white;
                font-weight: bold;
                transition: 1s;
                margin-left: 10px;
            }
            .navbar-brand:hover{
                color: yellow;
                transition: 1s;
                scale: 1.05;
            }
            .nav-item{
                margin: 0;
                cursor: pointer;
                color: white;
                font-weight: bold;
            }
            .nav-item-wrapper{
                margin-right: 75%;
                
            }
            .logo_image{
                width: 50px;
                height: 50px;
                margin-left: 10px;
            }
                     
            .nav-item:hover{
                color: yellow;
                transition: 0.5s;
                scale: 1.05;
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
                background-color: white;
            }
            .welcome, .events{
                height: 20vh;
            }
            .search_bar{
                background-color: white;
                border-radius: 20px;
                width: 20%;
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
                height: 175vh;
            }         
            .internships{
                width:60%;
                border-radius: 10px;
                background-color: lightgray;
                border: 1px solid black;
                margin: 0 auto;
            }
                     
            .title{
                font-size:30px; 
                text-align:center;
            }
            .tabs{
                cursor: pointer;
                text-align: center;
                font-weight: bold;
                font-size: 20px;
                height:7vh;
                border-radius: 10px;
                padding-bottom:10px;
            }
            .tabs:hover{
                color: yellow;
                transition: 0.5s;
                background-color: #002147;
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
                font-size: 15px;
                color: black;
                height: auto;
            }
            .profile_photo{
              
                border-radius: 50%;
                width: 100px;
                height: 100px;
                margin: 10px -40px 0 auto;
                z-index: 2;
                border: 1px solid black;
                transition: 0.5s ease-in-out;
            }
            .profile_photo:hover{
                transform: scale(1.2);
            }
                     
            .mask{
                width: 100%;
                height: 30vh;
                background-color: #002147;
                border-radius: 5px;
            }
                         
            #skills{
                margin-top: 0vh;
                margin-left: 72vh;
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

                      
                         
                         /*footer*/
.footer{
    margin-top: 10vh;
    padding-top: 20px;
    width: 100%;
    height: auto;
    /*background-color: rgb(255, 213, 255, 0.2);*/
    background-color: #002147;
    color: white;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    font-size: 17px;
    border-radius: 10px;
}

.socialmedia_wrapper{
    width: 60%;
    height: auto;
    display: flex;
    flex-flow: row nowrap;
    justify-content: center;
    align-items: center;
    margin-left: 52vh;

}
.linkedin, .instagram, .notion, .github{
    border-radius: 50%;
    width: 30px;
    height: 30px;
    margin: 0px 10px;
}


        </style>                         
""")

    ui.page_title("IGC: I Got Career")

    # navigation bar
    with ui.grid(columns="1fr").classes("w-full nav_bar"):

        async def getDate():
            time = await ui.run_javascript("new Date().toLocaleString()")
            return time

        with ui.grid(columns="1fr").classes("w-full navbar"):
            with ui.grid(columns="1fr"):
                 ui.label("I Got Career").classes("navbar-brand font-bold text-2xl")
            with ui.grid(columns="1fr 1fr").classes("justify-content-end nav-item-wrapper"):
                with ui.link(target="#").classes("nav-item !no-underline text-black"):
                    ui.label("Main").classes("nav-item")
                with ui.link(target="#").classes("nav-item !no-underline text-black"):
                    ui.label("My Page").classes("nav-item").on('click', lambda: ui.notify('Feature Currently Developing...'))


    # welcome and events
    with ui.grid(columns="2fr 3fr").classes("welcome-section w-full gap-2"):
        with ui.grid(columns="1fr 4fr").classes("w-full"):
            ui.image(
                "C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\yejun.jpg"
            ).classes("profile_photo")
            
            with ui.grid(columns="1fr").classes("w-full text_wrapper"):
                with ui.grid(rows="1fr 1fr 1fr").classes("w-full self_description"):
                    ui.label('Welcome Yejun Lee!').classes("about_text")
                    ui.label('📌 Status: Enrolled, Spring 2024').classes("about_text")
                    ui.label('🎓 Education: Stony Brook University, B.E.').classes("about_text")

        with ui.link(target="https://www.superookie.com/jobs/6620d4568b129f64f86e6912"):
            ui.image(
                "C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\event_banner.jpg"
            ).classes("events border p-1")

    # search bar
    with ui.grid(columns="1fr").classes("wrapper_div gap-2"):
        ui.input(placeholder="Search Any Internship!").props(
            "rounded outlined dense"
        ).classes("search_bar")

    # main content
    with ui.grid(columns="1fr 5fr").classes("w-full gap-5 tab_wrapper"):
        # tabs section
        with ui.grid(rows="1fr 1fr 1fr 1fr ").classes("gap-2 left_bar"):
            with ui.link(target="#internship").classes('!no-underline text-black'):
                ui.label('🏢 Internships/Jobs').classes("border p-1 tabs")
            with ui.link(target="#skills").classes('!no-underline text-black'):
                ui.label('🥇 Events').classes("border p-1 tabs")
            with ui.link(target="#employers").classes('!no-underline text-black'):
                ui.label('💰 Employers').classes("border p-1 tabs").on('click', lambda: ui.notify('Feature Currently Developing...'))
            with ui.link(target="#career_center").classes('!no-underline text-black'):
                ui.label('💁 Career Center').classes("border p-1 tabs").on('click', lambda: ui.notify('Feature Currently Developing...'))


        # internships section
        with ui.grid(rows="60px 1fr 1fr 1fr").classes("gap-3 internship_wrapper"):
            ui.label('🏢 Internships').classes('title')
            with ui.grid(columns="1fr 1fr").classes("internships_wrapper"):
                # internship 1
                with ui.link(
                    target="https://jobs.louisvuitton.com/en/search-page/job/2024-retail-management-trainee-south-korea-seoul-dom-880093"
                ).classes('!no-underline text-black'):
                    with ui.card().tight().classes("right_bar border p-1"):
                        with ui.image(
                            "C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\job-retail.jpg"
                        ):
                            ui.badge('SUNY Korea',color='blue').props('floating')
                        with ui.card_section():
                            ui.label('Retail Management Trainee / Louis Vuitton').classes('underline font-bold')
                            ui.label('App. Due: ~04/30 / Paid Full-Time')
                            ui.label('Location: Seoul, Korea')
                            ui.label('Job Description: ')
                            ui.button.default_props("rounded outline")
                            ui.button("English").classes('mt-2')
                            ui.button("Korean").classes('mt-2')
                            ui.button("Fashion Business Management").classes('mt-2')

                # internship 2
                with ui.link(
                    target="https://join.deloitte.co.kr/WiseRecruit2/User/RecruitView.aspx?ridx=2508"
                ).classes('!no-underline text-black'):
                    with ui.card().tight().classes("right_bar border p-1"):
                        with ui.image(
                            "C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\deloitte-logo.png"
                        ):
                            ui.badge('George Mason',color='green').props('floating')
                        with ui.card_section():
                            ui.label('Marketing Data Analysis Intern / Deloitte').classes('underline font-bold')
                            ui.label('App. Due: ~05/03 / Paid Full-Time')
                            ui.label('Location: Seoul, Korea')
                            ui.label('Job Description: ')
                            ui.button.default_props("rounded outline")
                            ui.button("English").classes('mt-2')
                            ui.button("Korean").classes('mt-2')
                            ui.button("Computational Data Science").classes('mt-2')


                # internship 3
                with ui.link(
                    target="https://www.superookie.com/jobs/662709078b129f7000361c89"
                ).classes('!no-underline text-black'):
                    with ui.card().tight().classes("right_bar border p-1"):
                        with ui.image(
                            "C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\lg.png"
                        ):
                            ui.badge('George Mason',color='green').props('floating')
                        with ui.card_section():
                            ui.label('Digital-Content Social Crew Intern / Superookie').classes('underline font-bold')
                            ui.label('App. Due: ~05/01 / Paid part-Time')
                            ui.label('Location: Seoul, Korea')
                            ui.label('Job Description: ')
                            ui.button.default_props("rounded outline")
                            ui.button("English").classes('mt-2')
                            ui.button("Korean").classes('mt-2')
                            ui.button("Business Management").classes('mt-2')
                
                # internship 4
                with ui.link(
                    target="https://www.superookie.com/jobs/6620d4568b129f64f86e6912"
                ).classes('!no-underline text-black'):
                    with ui.card().tight().classes("right_bar border p-1"):
                        with ui.image(
                            "C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\tiktok.webp"
                        ):
                            ui.badge('Utah Asia',color='red').props('floating')
                        with ui.card_section():
                            ui.label('Talent Acquisition Intern 2024 / Superookie').classes('underline font-bold')
                            ui.label('App. Due: ~05/17 / Paid Full-Time')
                            ui.label('Location: Seoul, Korea')
                            ui.label('Job Description: ')
                            ui.button.default_props("rounded outline")
                            ui.button("English").classes('mt-2')
                            ui.button("Korean").classes('mt-2')
                            ui.button("Communication").classes('mt-2')

                # internship 5
                
                with ui.link(
                    target="https://www.peoplenjob.com/jobs/5620255?type=intern"
                ).classes('!no-underline text-black'):
                    with ui.card().tight().classes("right_bar border p-1"):
                        with ui.image(
                            "C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\innomotics.png"
                        ):
                            ui.badge('Ghent Univ.',color='blue').props('floating')
                        with ui.card_section():
                            ui.label('Project manager Intern / Innomotics').classes('underline font-bold')
                            ui.label('App. Due: ~05/23 / Paid Full-Time')
                            ui.label('Location: Seoul, Korea')
                            ui.label('Job Description: ')
                            ui.button.default_props("rounded outline")
                            ui.button("English").classes('mt-2')
                            ui.button("Korean").classes('mt-2')
                            ui.button("Business Economics").classes('mt-2')

                # internship 6
                with ui.link(
                    target="https://sunykoreacdc.youcanbook.me/"
                ).classes('!no-underline text-black'):
                    with ui.card().tight().classes("right_bar border p-1"):
                        with ui.image(
                            "C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\header.jpg"
                        ):
                            ui.badge('SUNY Korea',color='blue').props('floating')
                        with ui.card_section():
                            ui.label('Career Development Center / SUNY Korea').classes('underline font-bold')
                            ui.label('App. Due: ~05/30 / Paid part-Time')
                            ui.label('Location: Seoul, Korea')
                            ui.label('Job Description: ')
                            ui.button.default_props("rounded outline")
                            ui.button("English").classes('mt-2')
                            ui.button("Korean").classes('mt-2')
                            ui.button("All students in SUNY").classes('mt-2')
    # mask for section
    with ui.grid(columns="1fr").classes("mask"):
        ui.label('🥇 Events').classes('title text-white')
    
    # section
    ui.html('''
    <section id="skills">
            <div id="skills_wrapper">
                <div class="skill_wrapper" id="eng_skills">
                  <div class="text_wrapper">
                    <p class="skill_emoji">&#128261;</p>
                    <p class="skill_title">Employers(Company)</p>
                    <p class="skill_title">Samsung</p>
                    <p class="skill_title">Apple</p>
                    <p class="skill_title">Toss</p>
                    <p class="skill_title">Naver</p>
                    <p class="skill_title">Gen.G Esports</p>
                    <p class="skill_title">Tiktok Korea</p>
                    </ul>
                  </div>
                </div>
                <div class="skill_wrapper" id="dev_skills">
                  <div class="text_wrapper">
                    <p class="skill_emoji">&#128187;</p>
                    <p class="skill_title">Popular Job Postings</p>
                    <br>
                    <p class="skill_title">TOSS Payments</p>
                    <p class="skill_desc">Software Engineer Intern, Korea</p>
                    <p class="skill_title">Gen.G Esports</p>
                    <p class="skill_desc">Digital Marketing Manager, Korea</p>
                    <p class="skill_title">TikTok</p>
                    <p class="skill_desc">Communication Intern, Korea</p>
                    </ul>
                </div>
                </div>
                <div class="skill_wrapper" id="gen_skills">
                  <div class="text_wrapper">
                    <p class="skill_emoji">&#128204;</p>
                    <p class="skill_title">Career Events</p>
                    <a href="https://forms.office.com/pages/responsepage.aspx?id=6nChzQVnykCl_7YjdLY8eYDzKYiysTNJiXbKMr1-Tg1UNFEySUUyTVpCS0NORU8zR003VkhGMkhNOS4u"><p class="skill_desc"> RSVP Link </p></a>
                    <p class="skill_desc">Useful tips for career preparation</p>
                    <p class="skill_title">"Spring 2024 Internship Panel"</p>
                    <ul class="skill_list">
                        <li>Date: April.3 (Wed.)</li>
                        <li>Time: 12:10 p.m. - 1:30 p.m.</li>
                        <li>Location: SUNY Korea C 103</li>
                    </ul>
                  </div>
                </div>
            </div>
        </section>
''')

    # footer
    with ui.grid(columns="1fr").classes("w-full footer"):
        
        with ui.grid(columns="1fr").classes("w-full"):
            ui.label("I Got Career").classes("text-center font-bold text-2xl")
            ui.label("Make IGC Great Again?").classes("text-center text-3xl")
            with ui.grid(rows="1fr 1fr 1fr 1fr").classes("w-50 socialmedia_wrapper"):
                with ui.link(target="https://kr.linkedin.com/in/jungha-j-cho-895211126"):
                    ui.image("C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\linkedin.png").classes("linkedin")
                with ui.link(target="https://www.instagram.com/chojungha98/"):
                    ui.image("C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\instagram.png").classes("instagram")
                with ui.link(target="https://www.notion.so/Jungha-s-Home-ea8f7f7e75cd49ffa21bca0988bc71f8"):
                    ui.image("C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\notion.png").classes("notion")
                with ui.link(target="github.com/Harvendois?tab=repositories"):
                    ui.image("C:\\Users\\Jungha Cho\\git\\Hackathon\\frontend\\images\\github.png").classes("github")
            ui.label("Copyright of © HawonsMuffins in 2024").classes("text-center")
            ui.label("Design by HawonsMuffins").classes("text-center")
