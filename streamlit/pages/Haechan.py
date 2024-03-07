import streamlit as st
import time

# Set up the Streamlit app
st.set_page_config(page_title="Centered Text Example", page_icon=":guardsman:", layout="wide")

if st.button('Talk'):
    st.toast('HI! am Haechan!')
    time.sleep(2.0)
    st.toast("H-A-E-C-H-A-N")
    time.sleep(2.0)
    st.toast("HAECHAN!")
    time.sleep(2.0)
    st.toast("Thank you! LOL")
    time.sleep(2.0)

# Display centered text
st.markdown("""
<style>
.centered {
  text-align: center;
}
</style>
<div class="centered">
  <h1 style="color:#0072C6;">HAECHAN</h1>
  <p>NCT 127, NCT DREAM</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
   st.header(" ")
   st.header(" ")
   st.image("Fzo0nNgaYAAAhLR.jpg", width=300)

   instagram_link = "https://www.instagram.com/haechanahceah?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="
   st.markdown(f"Instagram : [haechanahceah]({instagram_link})", unsafe_allow_html=True)

with col2:
   st.header(" ")
   st.header(" ")
   st.caption("""Lee Donghyeok (อี ดงฮยอก) หรือชื่อที่แฟนคลับเรียกกันว่า แฮชาน/full sun บุคคลที่มีเสียงร้องอันเป็นเอกลักษณ์ และไลน์เต้นที่มีเสน่ห์ดึงดูดสายตาจนใครเห็นก็ต้องร้องโห ในปี 2013 แฮชานเข้าร่วม SM Entertainment หลังจากผ่านการออดิชั่น SM Saturday Open (ซึ่งว่ากันว่าเป็นการออดิชั่นประจำสัปดาห์ในวันเสาร์ที่ใคร ๆ ก็บอกว่าโหดที่สุด) 
              แฮชานได้ร้องเพลง "Baby" โดย Justin Bieber, "Hello" โดย Huh Gak และ "Ugly Duckling" โดย Son Seung-yeon ซึ่งแน่นอนว่าเขาได้ผ่านการออดิชั่น 
              ต่อมาในวันที่ 17 กรกฎาคม 2014 แฮชานได้ถูกแนะนำให้เป็น SM Rookies ที่เป็นทีมฝึกก่อนจะได้เดบิวต์ 
              สองปีต่อมา แฮชานได้ถูกเปิดตัวในฐานะสมาชิกของยูนิตย่อยของ NCT นั่นคือ NCT 127 และปล่อยซิงเกิลแรก "[Fire Truck](https://youtu.be/_psXn_VJ_AE?si=3j29qPZibBkfyE5z)" 
              """)

   st.caption("""และในปีเดียวกันนั้น แฮชานได้เดบิวต์อีกครั้งในนามของ NCT DREAM ซึ่งเป็นยูนิตย่อยของ NCT ด้วยเพลง "[Chewing Gum](https://youtu.be/fwmvF5ffmhg?si=cJCNTGf9MqVSCrCo)" ในวันที่ 25 สิงหาคมเช่นเดียวกับมาร์ค 
              เนื่องด้วยมีงานและกิจกรรมในวงที่เยอะ ทำให้แฮชานเองต้องทำงานหนักขึ้นเพราะต้องโปรโหมดและทำเพลงให้กับทั้งสองยูนิต 
              จึงส่งผลให้ในช่วงธันวาคมของปี 2018 ถูกประกาศว่าแฮชานกระดูกหน้าแข้งหักขณะเตรียมตัวสำหรับทัวร์ Neo City-The Origin tour (2019-2020) และได้หยุดกิจกรรมทุกอย่างเพื่อฟื้นตัว 
              หลังจากที่แฮชานได้ห่างหายเพื่อรักษาตัว เขาก็ได้ปรากฏตัวในคอนเสิร์ตของ NCT 127 อักครั้ง นอกจากทั้งสองยูนิตนี้แล้ว แฮชานยังได้เข้าร่วมอีกหนึ่งยูนิตคือ NCT U 
              โดยเปิดตัวในซิงเกิล "Coming Home" ภายใต้โปรเจ็กต์ SM Station """)

   st.caption("""นอกเหนือจากการร้องและเต้นแล้ว แฮชานยังทำหน้าที่ได้ดีในเรื่องของวาไรตี้ สามารถบอกได้ตรงนี้ว่าไม่มีตายไมค์แน่นอน ทุก ๆ ครั้งที่มี content วาไรตี้โชว์ 
              แฮชานก็มักจะทำหน้าที่ดำเนินรายการได้ดีเสมอโดยเฉพาะการเล่นมุขตลก ๆ 
              อีกทั้งยังมีรายการพอดแคสต์ของแฮชานเองที่มีชื่อรายการว่า "[37.5MHz HAECHAN Radio](https://youtube.com/playlist?list=PLBRtRCOH3eXGL4YIwnormpseLhBg-Xyad&si=8LFBOsd961IfttbL)" ที่จะเชิญเหล่าสมาชิกต่าง ๆ ในวงมาร่วมพูดคุยกัน""")

   st.caption("""รวมไปถึงโคฟเวอร์เพลงต่าง ๆ เช่นเพลง [Mistletoe โดย Justin bieber](https://youtu.be/PBBriDzbV4k?si=4CbA8yPDrQoVottk) ที่ได้มีการร้องคู่กับมาร์ค 
              และแฮชานยังได้ร้องเพลงประกอบละคร "Ply Friends: Seoyeon University Class of '22" ที่มีชื่อเพลงว่า "Good Person" อีกด้วย """)
   
   video_url = "https://youtu.be/MMJ_uIw02U8?feature=shared"
   st.video(video_url)

with col3:
   st.header(" ")
   st.header(" ")
   st.caption("**ชื่อจริง** : 이동혁 Lee Donghyuk (อี ดงฮยอก)")
   st.caption("**ชื่อเกาหลี/สเตจเนม** : 해찬 Haechan (แฮชาน)")
   st.caption("**เกิด** : 6 มิถุนายน ค.ศ. 2000 (พ.ศ. 2543)")
   st.caption("**บ้านเกิด** : กรุงโซล ประเทศเกาหลีใต้")
   st.caption("**สัญชาติ** : เกาหลีใต้")
   st.caption("**การศึกษา** : จบจาก School of Performing Arts Seoul (SOPA)")
   st.caption("**ตำแหน่ง** : เมนโวคอล")
   st.caption("**ส่วนสูง** : 174 cm")
   st.caption("**หมู่เลือด** : AB")
   st.caption("**ยูนิต** : NCT 127, NCT DREAM")

   st.subheader(' ', divider='red')

   st.header("FANCAM")

   st.caption(" - [페이스캠4K] 엔시티 드림 해찬 :green['ISTJ' (NCT DREAM HAECHAN FaceCam)] @SBS Inkigayo")
   video_url = "https://youtu.be/hExYUh6-uNE?si=vn4XmcxmrCGibYwW"
   st.video(video_url)

   st.caption(" - [4K] 231202 :green[NCT DREAM Poison (모래성) 해찬 HAECHAN FOCUS] @ MMA 2023")
   video_url = "https://youtu.be/hTFy_3mgMqc?si=2xLzFcHlWgj4S1SS"
   st.video(video_url)