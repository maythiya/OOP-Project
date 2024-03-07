import streamlit as st
import time

# Set up the Streamlit app
st.set_page_config(page_title="Park Jisung", page_icon=":hamster:", layout="wide")

if st.button('Talk'):
    st.toast('Hello~~')
    time.sleep(2.0)
    st.toast("I am maknae")
    time.sleep(2.0)
    st.toast('Jisung~~~')
    time.sleep(2.0)

# Display centered text
st.markdown("""
<style>
.centered {
  text-align: center;
}
</style>
<div class="centered">
  <h1 style="color:#0072C6;">JISUNG</h1>
  <p>NCT DREAM</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3= st.columns(3)

with col1:
   st.header(" ")
   st.header(" ")
   st.image("Fzo0s4UaUAcWchT.jpg", width=300)

   instagram_link = "https://www.instagram.com/the__and.y?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="
   st.markdown(f"Instagram : [the__and.y]({instagram_link})", unsafe_allow_html=True)

with col2:
   st.header(" ")
   st.header(" ")
   st.caption("""Park Jisung (พัก จีซอง) หรือที่รู้จักกันในนามน้องเล็กสุดของ NCT DREAM หรือ Jisung (지성) เป็นนักเต้นหลัก แร็ปเปอร์ และนักร้อง 
              เดบิวต์ครั้งแรกในฐานะสมาชิกของยูนิต NCT DREAM ในเพลง "Chewing Gum" ในปี 2019 จีซองได้เดบิวต์ในฐานะศิลปินเดี่ยวด้วยซิงเกิล "Back to School" 
              ซึ่งขึ้นถึงอันดับสามใน Gaon Digital Chart จีซองได้ออกมินิอัลบั้มและซิงเกิ้ลหลายชุดที่ได้รับเสียงวิจารณ์ชื่นชม รวมไปถึงการเข้าร่วม "Dancing High" 
              ซึ่งในตอนนั้นจีซองหวังว่าจะสร้างสายสัมพันธ์และรู้จักเพื่อนมากมาย เนื่องจากจีซองทำงานตั้งแต่อายุยังน้อย ทำให้เขาติดต่อกับผู้คนในสภาพแวดล้อมทางสังคมอื่น ๆ เช่น โรงเรียนได้ยาก 
              และตัวจีซองเองเคยบอกว่าเขาไม่มีเพื่อนที่โรงเรียนเลยยกเว้นพี่ ๆ ในวง""")

   video_url = "https://youtu.be/J1qRfvccaiA?feature=shared"
   st.video(video_url)

   st.caption("""ด้วนไลน์เต้นที่เป็นเอกลักษณ์แล้ว นอกจากนี้จีซองยังร้องเพลงโคฟเวอร์เดี่ยว และกับสมาชิกในวงอย่างเฉินเล่อร่วมร้องโคฟเวอร์ด้วยกัน 
              """)
   
   video_url = "https://youtu.be/T3IkMH76XoA?feature=shared"
   st.video(video_url)

   video_url = "https://youtu.be/KEaHI-_H_6Q?feature=shared"
   st.video(video_url)

with col3:
   st.header(" ")
   st.header(" ")
   st.caption("**ชื่อจริง** : 박지성 Park Jisung (พัก จีซอง)")
   st.caption("**ชื่อเกาหลี/สเตจเนม** : 지성 Jisung (จีซอง)")
   st.caption("**เกิด** : วันอังคารที่ 5 กุมภาพันธ์ 2002 (พ.ศ. 2545)")
   st.caption("**บ้านเกิด** : กรุงโซล ประเทศเกาหลีใต้")
   st.caption("**สัญชาติ** : เกาหลีใต้")
   st.caption("**การศึกษา** : ได้ลาออกจากโรงเรียนมัธยมต้นกิรึม และสอบเทียบ (ปัจจุบันจบมัธยมปลายแล้ว)")
   st.caption("**ตำแหน่ง** : เมนแดนซ์ / ซับแร็ปเปอร์ / ซับโวคอล")
   st.caption("**ส่วนสูง** : 180 cm")
   st.caption("**หมู่เลือด** : O")
   st.caption("**ยูนิต** : NCT DREAM, NCT U")

   st.subheader(' ', divider='red')

   st.header("FANCAM")

   st.caption(" - [MPD직캠] 엔시티 드림 제노 직캠 4K :green['ISTJ' (NCT DREAM JENO FanCam)] | @MCOUNTDOWN_2023.7.27")
   video_url = "https://youtu.be/BQ-WmA1XE5E?si=kg-eW5lVizRnNORo"
   st.video(video_url)

   st.caption(" - [MPD직캠] 엔시티 드림 제노 직캠 4K :green['Candy' (NCT DREAM JENO FanCam)] | @MCOUNTDOWN_2022.12.29")
   video_url = "https://youtu.be/hhhXXI2QsGM?si=vNyW29U9U9fDOYpz"
   st.video(video_url)