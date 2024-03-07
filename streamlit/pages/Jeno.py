import streamlit as st
import time

# Set up the Streamlit app
st.set_page_config(page_title="Lee Jeno", page_icon=":hamster:", layout="wide")

if st.button('Talk'):
    st.toast('Who- who are you?')
    time.sleep(2.0)
    st.toast("Just kidding LOLLOL")
    time.sleep(2.0)
    st.toast("My name's Jeno")
    time.sleep(2.0)
    st.toast("Nice to meet yooouuu")
    time.sleep(2.0)

# Display centered text
st.markdown("""
<style>
.centered {
  text-align: center;
}
</style>
<div class="centered">
  <h1 style="color:#0072C6;">JENO</h1>
  <p>NCT DREAM</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
   st.header(" ")
   st.header(" ")
   st.image("Fzo0dmaagAQOM8s.jpg", width=300)

   instagram_link = "https://www.instagram.com/leejen_o_423?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="
   st.markdown(f"Instagram : [leejen_o_423]({instagram_link})", unsafe_allow_html=True)

with col2:
   st.header(" ")
   st.header(" ")
   st.caption("""Lee Jeno (อี เจโน่) หรือที่รู้จักกันในชื่อ เจโน่ NCT หนุ่มตาสระอิ เดบิวต์ครั้งแรกในเพลง "Chewing Gum" 
              เจโน่มีความสามารถเฉพาะตัวทั้งด้านการร้อง การเต้น รวมไปถึงการถ่ายโฆษณา เมื่อได้ทำงานรวมกับเพื่อนร่วมวงแล้ว ทำให้ NCT DREAM กลายเป็นวงที่ได้รับความรักจากแฟน ๆ มากที่สุดวงหนึ่ง 
              ภายในปี 2020 เจโน่ก็ได้เดบิวต์อีกครั้งภายใต้ยูนิต NCT U ที่เป็นส่วนหนึ่งในโปรเจ็กต์ "NCT Resonance" ในเพลง "Misfit" 
              และได้รับเสียงตอบรับที่ดีจากแฟนคลับมากมาย ทั้งนี้เจโน่ยังมีส่วนร่วมในการเขียนเนื้อเพลง "[Dear Dream](https://youtu.be/4j_HQoJOeTg?si=AwW1pYOVxRiKEZxN)" 
              และ "[We Go up](https://youtu.be/LV1Es22E0RI?si=SFcIQqqprk2HYVAj)" ร่วมกับสมาชิก มาร์ค, แจมิน และจีซอง ตั้งแต่นั้นเจโน่ก็ได้ร่วมเขียนเนื้อเพลงต่อ ๆ มาของ NCT DREAM 
              """)
   
   st.caption("""เมื่อวันที่ 13 กันยายน เจโน่กลายเป็นศิลปินเคป็อปคนแรกที่เป็นนายแบบเปิดงานนิวยอร์กแฟชั่นวีค
              ให้กับ Peter Do's spring 2023 collection ซึ่งเป็นส่วนหนึ่งของความร่วมมือกับ SM Entertainment 
              """)
   
   st.image('FB_PETERDO_Header.jpg', caption='ขอบคุณภาพจาก THE KRAZE')

   st.caption("""นอกจากทำงานให้กับบริษัทแล้ว ในเดือนพฤษภาคม ปี 2019 เจโน่และเพื่อนในวงที่เรียนด้วยกันมาอย่างแจมินก็ได้ไปเป็นอาสาสมัครจิตอาสาเยี่ยมเด็ก ๆ ที่อาศัยอยู่ในสลัม ประเทศอินโดนีเซีย 
              โดยร่วมมือกับองค์กรพัฒนาเอกชน Good Neighbors และมูลนิธิ Gugah Nurani Indonesia """)

with col3:
   st.header(" ")
   st.header(" ")
   st.caption("**ชื่อจริง** : 이제노 Lee Jeno (อี เจโน่)")
   st.caption("**ชื่อเกาหลี/สเตจเนม** : 제노 Jeno (เจโน่)")
   st.caption("**เกิด** : 23 เมษายน ค.ศ. 2000 (พ.ศ. 2543)")
   st.caption("**บ้านเกิด** : อินชอน ประเทศเกาหลีใต้")
   st.caption("**สัญชาติ** : เกาหลีใต้")
   st.caption("**การศึกษา** : จบจาก School of Performing Arts Seoul (SOPA)")
   st.caption("**ตำแหน่ง** : ลีดแร็ปเปอร์ / ลีดแดนซ์ / ซับโวคอล")
   st.caption("**ส่วนสูง** : 176.8 cm")
   st.caption("**หมู่เลือด** : A")
   st.caption("**ยูนิต** : NCT DREAM, NCT U")

   st.subheader(' ', divider='red')

   st.header("FANCAM")

   st.caption(" - [MPD직캠] 엔시티 드림 제노 직캠 4K :green['ISTJ' (NCT DREAM JENO FanCam)] | @MCOUNTDOWN_2023.7.27")
   video_url = "https://youtu.be/BQ-WmA1XE5E?si=kg-eW5lVizRnNORo"
   st.video(video_url)

   st.caption(" - [MPD직캠] 엔시티 드림 제노 직캠 4K :green['Candy' (NCT DREAM JENO FanCam)] | @MCOUNTDOWN_2022.12.29")
   video_url = "https://youtu.be/hhhXXI2QsGM?si=vNyW29U9U9fDOYpz"
   st.video(video_url)