import streamlit as st
from streamlit_webrtc import webrtc_streamer
from PIL import Image

st.title('2023 Ford Mustang')

st.header('The Iconic Muscle Car')
col1, col2 = st.columns([3,1])
with col1:
    talk_to_agent = st.checkbox('Need to talk to an agent?')
    if talk_to_agent:
        webrtc_streamer(key="sample", 
        rtc_configuration={  
            "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
        }

    image = Image.open('mustang.jpeg')
    st.image(image, caption='The Iconic Muscle Car', use_column_width=True)

    st.write("""
    The Ford Mustang is an American muscle car icon. First introduced in 1964, the Mustang has been one of Ford's most popular and recognizable models. 
    For 2023, the Mustang continues to deliver powerful performance, retro-inspired styling, and advanced technology features.
    """)

    st.header('Key Specs')
    st.write("""
    - 5.0L V8 engine with up to 480 horsepower 
    - 0-60 mph in under 4 seconds
    - 6-speed manual or 10-speed automatic transmission
    - RWD or AWD drivetrain options
    - EPA fuel economy up to 18 mpg city / 25 mpg highway
    """)  

    st.header('Styling and Design')
    st.write("""
    The new Mustang features the classic fastback silhouette along with modern details like LED lighting and 19-inch alloy wheels.
    Inside, the Mustang offers a driver-focused cockpit with leather seats, crisp digital displays, and the latest SYNC infotainment system. 
    """)

    st.header('Take it for a Test Drive')
    st.write("""
    The 2023 Ford Mustang delivers an exhilarating driving experience thanks to its powerful engines, precise handling, and snarling exhaust note.
    Contact our sales team today to schedule a test drive and feel the thrill of driving this iconic muscle car yourself.
    """)

with col2:
    st.header('Newport Ford')
    st.image('Ford-Motor-Company-Logo.png')
    st.write("""
    ### Hours:             
    9am - 8pm\n
    Mon-Sat
    """)

    st.write("""
    ### Location:
    Newport Ford\n
    123 Auto Drive\n
    Newport, RI 02840

    ### Contact:
    - Phone Sales: 401-555-1234
    - Phone Service: 401-555-5678
    - Email: sales@newportford.com
    """)
    
    st.write("""
    ### Driving Directions:
    - From Providence, take I-95 South 
    - Take Exit 5 Newport/Jamestown
    - Turn left onto RI-138
    - Drive 3 miles and turn right on Auto Drive
    - Newport Ford is on the right
    """)
