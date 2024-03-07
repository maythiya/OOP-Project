import streamlit as st
import time

if st.button('Talk'):
    st.toast('Hi!')
    time.sleep(2.0)
    st.toast("I'm Mark")
    time.sleep(2.0)
    st.toast('So...')
    time.sleep(2.0)
    st.toast("You can mark me in your heart LOL")
    time.sleep(2.0)
    st.toast("Alright, alright")
    time.sleep(2.0)
    st.toast("I'm glad to see you here")
    time.sleep(2.0)
    st.toast("Let's know me!")
    time.sleep(2.0)

st.markdown("""
<style>
.centered {
  text-align: center;
}
</style>
<div class="centered">
  <h1 style="color:#0072C6;">MARK</h1>
  <p>NCT 127, NCT DREAM</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3= st.columns(3)

with col1:
   st.header(" ")
   st.header(" ")
   st.image("FzjrUMhWcAISy2D.jpg", width=300)

   instagram_link = "https://www.instagram.com/onyourm__ark?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="
   st.markdown(f"Instagram : [onyourm__ark]({instagram_link})", unsafe_allow_html=True)

with col2:
   st.header(" ")
   st.header(" ")
   st.caption("""Mark Lee (มาร์ค ลี) หรือที่รู้จักกันว่า มาร์ค NCT หนุ่มน้อยมากความสามารถและเดบิวต์มากที่สุดในวงรวมถึง 4 ครั้ง โดยที่มีตำแหน่งเป็นลีดเดอร์ (เฉพาะใน NCT DREAM) เมนแร็ปเปอร์ เมนแดนซ์ ซับโวคอล และนักแต่งเพลงชาวเกาหลี 
              เเต่เติบโตที่แคนาดาเป็นที่รู้จักในนามสมาชิกบอยแบนด์ของ NCT และกลุ่มย่อย NCT U, NCT 127 และสมาชิกของ NCT DREAM 
              มาร์คเป็นคนที่มีความสามารถรอบด้าน เรียกได้ว่าครบครันทั้งร้อง เต้น แร็ป มาร์คออดิชั่นผ่านจาก SM Global Audition ที่แวนคูเวอร์ประเทศแคนาดา และใช้เวลาในการเป็นเด็กฝึกนานถึง 4 ปี ถึงจะได้เดบิวต์ 
              และในที่สุดมาร์คก็ได้เดบิวต์ครั้งแรกในฐานะสมาชิกของวง NCT ยูนิต NCT U ด้วยเพลง 
              "[The 7th Sense](https://youtu.be/3UGMDJ9kZCA?si=YEMl9O7LI-NVz4J-)" 
              เมื่อวันที่ 8 เม.ย. 2016 """)

   st.caption("""และถัดมาได้สามเดือน มาร์คก็ได้เดบิวต์อีกรอบฐานะสมาชิก NCT 127 ในเพลง "[Fire Truck](https://youtu.be/_psXn_VJ_AE?si=3j29qPZibBkfyE5z)" เมื่อวันที่ 7 ก.ค. 2016 """)

   st.caption("""ไม่กี่เกือนต่อมาก็ได้เดบิวต์ในนาม NCT DREAM ในเพลง 
              "[Chewing Gum](https://youtu.be/fwmvF5ffmhg?si=5bEbhqT3P9MVLJ1J)" เมื่อวันที่ 25 ส.ค. 2016 และได้เปิดตัวเป็นหนึ่งในสมาชิกของ "[ซูเปอร์เอ็ม (SuperM)](https://th.wikipedia.org/wiki/%E0%B8%8B%E0%B8%B9%E0%B9%80%E0%B8%9B%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B9%80%E0%B8%AD%E0%B9%87%E0%B8%A1)" เมื่อวันที่ 4 ตุลาคม 2019 
              จึงเกิดเป็นฉายาว่า "อายุน้อยร้อยยูนิต" เนื่องด้วยความสามารถที่หลากหลายของมาร์คโดยเฉพาะการแร็ป ทำให้มาร์คได้เข้าร่วมการแข่งขันในรายการไฮสกูลแร็ปเปอร์ และเป็น Brand Ambassador ของแบรนด์ชื่อดังอย่าง Polo Ralph Lauren 
              พร้อมทั้งมาร์คยังมีเพลงเดี่ยวที่แต่งด้วยตัวเองอย่างเพลง "Child" และ "Golden Hour" 
              """)
   
   video_url = "https://youtu.be/VbIf3z2SqHg?feature=shared"
   st.video(video_url)

   video_url = "https://youtu.be/EUsUqd20c_k?feature=shared"
   st.video(video_url)
   
   st.caption("""แน่นอนว่ามีร้องก็ต้องมีแร็ป อีกทั้งมาร์คยังเคยแต่งเนื้อเพลงท่อนแร็ปเองในท่อนต่าง ๆ ของบางเพลง และเพลงแร็ปสั้น ๆ ที่ร่วมทำกับจอห์นนี่ NCT อย่างเพลง "QTAH" อีกด้วย """)

   video_url = "https://youtu.be/9GrtC5Z4r5w?feature=shared"
   st.video(video_url)

with col3:
   st.header(" ")
   st.header(" ")
   st.caption("**ชื่อจริง** : 이마크 Mark Lee (มาร์ค ลี)")
   st.caption("**ชื่อเกาหลี/สเตจเนม** : 이민형 Lee MinHyung (อี มินฮย็อง) / Mark (มาร์ค)")
   st.caption("**เกิด** : จันทร์ที่ 2 สิงหาคม ค.ศ. 1999 (พ.ศ. 2542)")
   st.caption("**บ้านเกิด** : แวนคูเวอร์ ประเทศแคนาดา")
   st.caption("**สัญชาติ** : แคนาดา")
   st.caption("**การศึกษา** : จบจาก School of Performing Arts high school (SOPA)")
   st.caption("**ตำแหน่ง** : ลีดเดอร์ / เมนแร็ปเปอร์ / เมนแดนซ์ / ซับโวคอล")
   st.caption("**ส่วนสูง** : 174 cm")
   st.caption("**หมู่เลือด** : A")
   st.caption("**ยูนิต** : NCT 127, NCT DREAM, NCT U")

   st.subheader(' ', divider='red')

   st.header("FANCAM")

   st.caption(" - [K-Fancam] 엔시티 드림 마크 직캠 :green['ISTJ' (NCT DREAM MARK Fancam) @뮤직뱅크(Music Bank)]")
   video_url = "https://youtu.be/IoUXYQ2ie0o?si=ctTZuGmsemhKLqtm"
   st.video(video_url)

   st.caption(" - [안방1열 직캠4K] 엔시티 127 마크 :green['Fact Check (불가사의; 不可思議)' (NCT 127 MARK FanCam) @SBS Inkigayo]")
   video_url = "https://youtu.be/iBA7IzoI54o?si=nrasXSHSP-5-E-Ff"
   st.video(video_url)
