import streamlit as st
from PIL import Image
import json
import requests  # pip install requests
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
from pathlib import Path

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = "C:/Users/akash/Documents/akash_portfolio/Resume.pdf"

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Portfolio", page_icon=":blush:", layout="wide")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

 
lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_DMgKk1.json")
lottie_experience = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_3jmvq04g.json")
lottie_certificate = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_tbwqrxnz.json")
lottie_skills = load_lottieurl('https://assets9.lottiefiles.com/private_files/lf30_obidsi0t.json')
lottie_social = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_zwn6fmnu.json")
lottie_projects = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_cwA7Cn.json")


with open("C:/Users/akash/Documents/akash_portfolio/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
## Akash Kathole, B.Tech
#### *Resume* 

''')
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read() 
    

    

image = Image.open('C:/Users/akash/Documents/akash_portfolio/wwe.png')
st.image(image, width=200,clamp=True)
st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file,
        mime="application/octet-stream",
    )
st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Deep domain and technical experience in diverse technology platforms 
- Including Cloud, Analytics platform, Business Analytics, Machine Learning, Reinforcement learning, deep learning, cloud computing, web development, data mining
- Passion in AI field
''')



#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.youtube.com/channel/UCead4mOe2wXcjdo7_VaM6cg" target="_blank">Akash Kathole</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certificates">Certificates</a>
      </li>
      <li class = "nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')
st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    height= 200,
    width=700,
    key=None,
)

txt('**🏫 Computer Science and Engineering** (AI Technology), *Dr.Babasaheb Ambedkar Technical University*, India',
'2020-2024')
st.markdown('''
- GPA: `9.75`
- Learning in the Institute `PCET-Nutan College of Engineering and Research`.
- Learning Advanced Technology `Specalized AI`.
''')

txt('**🏫 Higher Secondary Certificate** (HSC),Savitribai Phule Pune University, India',
'2019-2020')
st.markdown('''
- Institute: Sant Bhagwan Baba Jr College.
- Percentage: `69%`
''')

txt('**🏫 Secondary School Certificate** (SSC), Sant Gadge Baba Amravati University, India',
'2017-2018')
st.markdown('''
- Institute: Harlalka English High School.
- Percentage: `88.40%`
''')

txt('**🏆 Achievement**','Entrance')
st.markdown('''
- Qualified Jee main
- Qualified Jee Advance
''')

#####################
st.markdown('''
## Work Experience
''')

st_lottie(
    lottie_experience,
    speed=1,
    reverse=False, 
    loop=True,
    quality="low", # medium ; high
    height= 300,
    width=800,
    key=None,
)

txt('**🚧 Weather Fighter Pvt.ltd**, Data Scientist',
'03/2022-Present')
st.markdown('''
- ● Weather Fighter is a protective coating specialist company based in Pune delivering premium coating services over the years. Our wide range of protective coating service caters to fulfill the need of industrial, petrochemical, commercial, and residential applications.
- ● Manage a team of data scientists, machine learning engineers and big data specialists
- ●Lead data mining and collection procedures
- ● Ensure data quality and integrity
- ● Interpret and analyze data problems
- ● Conceive, plan and prioritize data projects
- ● Build analytic systems and predictive models
- ● Test performance of data-driven products
- ● Visualize data and create reports
- ● Experiment with new models and techniques
- ● Align data projects with organizational goals
- ● Formulate and test hypotheses to evaluate business strategies and measure impact.

''')

txt('**🚧 LetsGrowMore**, Data Science Intern',
'12/2021-01/2022')
st.markdown('''
- ● Understanding what problems create consumer calls through data mining interaction records 
- ● Adaptthe latesttechnologies in modeling and data mining to design scientific tests to maximize dollars spent on new initiatives and marketing channels.
- ● Work together with a team of dedicated experts including researchers, developers, dev-ops engineers,and architects with a single goal of building best machine learning pipelines for a variety of use cases spanning commerce, financial markets, and procurement.
- ● Formulate and test hypotheses to evaluate business strategies and measure impact.

''')

txt('**🚧 TheSparksFoundation**, IOT & Computer Vision',
'08/2021-09/2021')
st.markdown('''
- ● Developing custom image processing algorithms and software. 
- ● Creating applications for facial and emotion recognition, automated optical inspection, etc.
- ● Developing advanced vision algorithms and applications for machine automation.
- ● Develop softwarefor IoT, Artificial Intelligence, and Machine learning Application.

''')

txt('**🚧 ShapeAI**, Social Media Manager',
'07/2021-10/2021')
st.markdown('''
- ● Look for unstructured and structured data to extract meaningful insights. Python, Spark, TensorFlow, Hadoop.
- ● Make adjustments in machine learning models.
- ● Communicate with clients and look for business solutions.
- ● Specialize in structured data only Assistin designing and implementing tech solution.
- ● Track and update business projects and growth.

''')

txt('**🚧 Fantastiqo**, Social Media Marketing',
'04/2021-5/2021')
st.markdown('''
- ● Work with the on-site Social Media Manager to create and implement campaigns.
- ● Develop content calendars on a weekly and monthly basis for company brands.
- ● Monitor analytics with social media team to identify viable ideas.
- ● Create engaging blog and social media content.
- ● Assist in the general distribution of press releases and media alerts.
- ● Provide support to our marketing team at live and online events.


''')

txt('**🚧 ShapeAI**, Business Development Intern',
'03/2021-10/2021')
st.markdown('''
- ● Analyze the trends in the market and the company's strategies to identify opportunities to cash in on.
- ● Reportrelevant findings from the strategies implemented and getthem approved by the company's senior management.
- ● Support the creation and presentation of new ideas to add value to our products to increase sales and company revenue.
- ● Analyze consumer behavior and anticipate market trends to develop solutions to consumer problems and needs.
- ● Perform and present competitor analysis to identify areas where our company can surpass the industry's competitors and forge ahead to gain increased market share.
- ● Analyze sales and trends to promote ideas for sustained revenue growth.


''')
txt('**🚧 DevTown**, Social Media Manager',
'07/2021-10/2021')
st.markdown('''
- ● To Increase brand awareness through the usage of social media platforms brand's editorial calendar and seek creative ways to spread the company's message or product. Monitor analytics with social media team to identify viable ideas.

''')

txt('**🚧 Quantium**, Data Analytics Virtual Experience Program',
'07/2021-08/2021')
st.markdown('''
- ● Quantium and take partin the challenging butfun work our data analysts do daily!
- ● learn practical skills such as data validation, data visualisation, statisticaltesting and more. After completing each module.
''')

txt('**🚧 Forage**, New World. New skills: Power BI Virtual Case Experience',
'07/2021-08/2021')
st.markdown('''
- ● Use powerful Data Analytics tools to help solve business problems.
- ● Learning to master Power BI.
- ● By empowering to identify patterns,risks and opportunities in data, work more efficiently.
- ● Be able to clearly visualize the value of data and turn it into convincing, actionable insights.


''')


txt('**🚧 JPMorgan Chase & Co.**, Global Finance and Business Management Virtual Experience Program',
'08/2022-09/2022')
st.markdown('''
- ● Data Analysis and Simple Visualization 
- ● Data Visualization Dashboard
- ● Storytelling with Powerpoint
- ● Concise Written Communication: Variance Commentary
- ● Concise Verbal Communication: Manager Update Video

''')


#####################
st.markdown('''
## Certificates
''')
st_lottie(
    lottie_certificate,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    height= 200,
    width=700,
    key=None,
)
txt4('LinkedIn', '📃Strategic Planning Foundations', 'https://bit.ly/3CVswwQ')
txt4('LinkedIn', '📃Financial Accounting Foundations', 'https://bit.ly/3Bc9aSJ')
txt4('Linkedin', '📃Customer Service Foundation','https://bit.ly/3CXmfRt')
txt4('Udemy', '📃Arduino Build your own IRON MAN Arm with Voice Recognition', 'https://bit.ly/3BmXsVP')
txt4('Udemy', '📃Machine learning from Basic to Advanced','https://bit.ly/3QhwMKe')
txt4('Udemy','📃Nanotechnology','https://bit.ly/3RixesK')
txt4('Quantium', '📃Data Analytics', 'https://bit.ly/3Qf1gfY')
txt4('J.P. Morgan Asset Management', '📃software Engineering', 'https://bit.ly/3AFHzbi')
txt4('PwC', '📃New world. New skills: Power BI Virtual Case Experience', 'https://bit.ly/3RxSieG')
txt4('Amazon Web Services (AWS)', '📃introduction Cyber security and cyber attacks', 'https://bit.ly/3RxSieG')
txt4('Amazon Web Services (AWS)', '📃Introduction to machine learning :arts a possible', 'https://bit.ly/3Bad4M7')
txt4('Amazon Web Services (AWS)', '📃Planning of Machine Learning Project', 'https://bit.ly/3Bad4M7')
txt4('Amazon Web Services (AWS)', '📃machine learning', 'https://bit.ly/3Bad4M7')
txt4('HP', '📃social media marketing', 'https://bit.ly/3egL7ZX')
txt4('Google Digital Garage', '📃the fundamentals of digital marketing', 'https://bit.ly/3KMS41h')
txt4('Career Development College London', '📃email marketing basics','https://bit.ly/3RtASjy')
txt4('Career Development College London', '📃work from home productivity','https://bit.ly/3ANufSd')
txt4('Skill Up', '📃foundation of artificial intelligence','https://bit.ly/3wVmGYy')
txt4('Cursa', '📃web development for beginners', 'https://bit.ly/3BmZq8F')
txt4('European Open University Network BV', '📃python data science', 'https://bit.ly/3CWt7OR')
txt4('chaos engineering practitioner', '📃Requirements to be Recognized as Gremlin', 'https://bit.ly/3CVvamg')
txt4('Udemy', '📃google analytics for beginners', 'https://bit.ly/3wY4nSx')
txt4('Digital 101', '📃NASSCOM FutureSkills', 'https://bit.ly/3Rxh2DS')
txt4('Skill Front', '📃Insurance Industry Fundamentals','https://bit.ly/3RjaWHo')
txt4('Skill Front', '📃Foundation of Business & Entrepreneurship','https://bit.ly/3q8qcLm')
txt4('Microsoft', '📃Minecraft Hour of Code','https://bit.ly/3RhywEB')
txt4('Eduonix Learning Solution', '📃Quick and Easy Guide to Microsoft Word', 'https://bit.ly/3KSR0c3')
txt4('Microsoft', '📃Code Jumper : An inclusive Physical coding language', 'https://bit.ly/3RFsXQ9')
txt4('devtown', '📃Completing 7 days Bootcamp on machine learning & Python','https://bit.ly/3erA8NC')
txt4('Esports:', '📃Esports: More than Just a game - Microsoft', 'https://bit.ly/3RFt3at')
txt4('Open P-Tech', '📃Cybersecurity Fundamentals','https://bit.ly/3D5jWLU')
txt4('IEEE Bombay', '📃Entrepreneurship Bootcamp', 'https://bit.ly/3DdTv7d')
txt4('Eduonix Learning Solution', '📃Quick and Easy Guide to Microsoft word', 'https://bit.ly/3wRAnaU+-1-')
txt4('Eduonix Learning Solution', '📃Complete Beginners Course to Master Microsoft Excel', 'https://bit.ly/3AKX6GR')

#####################
st.markdown('''
## Projects
''')
st_lottie(
    lottie_projects,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    height= 200,
    width=700,
    key=None,
)
st.markdown('''
            

- 🏆Bigmart Sales prediction
- 🏆Breast cancer
- 🏆Calories burnt prediction
- 🏆Car Price Prediction
- 🏆Covid19 deathrate analysis
- 🏆Covid cases Prediction
- 🏆Customer Segementation of KMeans
- 🏆Diabetis Prediction
- 🏆Divorse prediction
- 🏆Earthquake prediction
- 🏆French Books review
- 🏆Heart Disease Prediction
- 🏆House Price Prediction
- 🏆IPO prediction
- 🏆Iris data analysis
- 🏆Placement Analysis
- 🏆Prankinson’s Disease Prediction
- 🏆Sonar Rock Vs Mike Prediction
- 🏆Spam mail Prediction
- 🏆Stock_Prediction (Tata motors)
- 🏆Stock Prediction
- 🏆Student Performance
- 🏆Tabular Playground Series
- 🏆Titanic Survived Prediction
- 🏆Wine Quality Prediction
- 🏆Face detection
- 🏆Dogs vs Cats classification

''')

#####################
st.markdown('''
## Skills
''')

st_lottie(
    lottie_skills,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    height= 200,
    width=700,
    key=None,
)

txt3('Programming', '`Python`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `Streamlit`, `heroku`,`hodoop`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')
txt3('Reinforcement Learning','`Transfer Learning`,`msql`')
txt3('Cloud Computing','`aws`,`google cloud`,`azure`')
txt3('Commmunication skills','`Public Speaking _nptel`')
txt3('Financial Management','`Linkedin management`')
txt3('strategic planning','`project planning`')

#####################

st.markdown('''
## Social Media
''')
st_lottie(
    lottie_social,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    height= 200,
    width=700,
    key=None,
)

txt2('📱 LinkedIn', 'https://www.linkedin.com/in/akash-kathole-005125202')
txt2('📱 Twitter', 'https://twitter.com/akashkathole74')
txt2('📱 Youtube', 'https://www.youtube.com/channel/UCead4mOe2wXcjdo7_VaM6cg')
txt2('', 'https://www.youtube.com/channel/UCMec-aZFzp9FwDd5M7FKBYg')
txt2('📱 Githhub', 'https://github.com/akashkathole7')
txt2('📱 Stackoverflow', 'https://stackoverflow.com/users/17599238/akash-kathole')


#####################
