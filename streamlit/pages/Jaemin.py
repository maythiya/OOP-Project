import streamlit as st
import time

# Set up the Streamlit app
st.set_page_config(page_title="Centered Text Example", page_icon=":man:", layout="wide")

if st.button('Talk'):
    st.toast('Hi~')
    time.sleep(2.0)
    st.toast("I am a lovely princess")
    time.sleep(2.0)
    st.toast('Na Jaemin', icon='👑')
    time.sleep(2.0)
    st.toast("So sexyy~~~~")
    time.sleep(2.0)

# Display centered text
st.markdown("""
<style>
.centered {
  text-align: center;
}
</style>
<div class="centered">
  <h1 style="color:#0072C6;">JAEMIN</h1>
  <p>NCT DREAM</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
   st.header(" ")
   st.header(" ")
   st.image("FzjrWwbXgAYIflA.jpg", width=300)

   instagram_link = "https://www.instagram.com/na.jaemin0813?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="
   st.markdown(f"Instagram : [na.jaemin0813]({instagram_link})", unsafe_allow_html=True)


with col2:
   st.header(" ")
   st.header(" ")
   st.caption("""Na Jaemin (นา แจมิน) หรือเป็นที่รู้จัก แจมิน/นานา NCT SM เจอแจมินครั้งแรกและชวนให้มาออดิชั่นในตอนที่แจมินกำลังทำกิจกรรมอาสาสมัครอยู่ 
              จนกระทั่งได้เป็นเด็กฝึกภายใต้ต้นสังกัดของ SM Entertainment ในช่วงปี 2013 หลังจากฝึกฝนมาเป็นเวลาสามปี 
              แจมินก็ได้เดบิวต์ในฐานะสมาชิกวง NCT ยูนิต NCT DREAM ในเดือนสิงหาคม 2016 และแน่นอนว่าทำให้แจมินดังเป็นพลุแตกด้วยการกลายเป็นบุคคลที่ best-selling artists in South Korea 
              ในวันที่ 2 กุมภาพันธ์ 2017 ก่อนซิงเกิลที่สอง "[My First and Last](https://youtu.be/4pUc7SD0PmU?si=o5qcDLg2GLLN2DDG)" จะออกมา ได้มีการประกาศว่าแจมินต้องพักงานตลอดทั้งปีที่เหลือเพื่อพักฟื้นจากหมอนรองกระดูกเคลื่อนทับเส้นประสาท 
              จึงทำให้เหลือสมาชิกเพียงแค่ 6 คน และกลับมาอีกครั้งโดยเป็นส่วนหนึ่งของ NCT 2018 ซึ่งเป็นโปรเจ็กต์พิเศษที่เกี่ยวข้องกับสมาชิก NCT ทั้ง 18 คน และ comeback กับ NCT DREAM ในเพลง "GO" 
              """)
   
   video_url = "https://youtu.be/cD8SYW8rjaQ?feature=shared"
   st.video(video_url)

   st.caption("""และ NCT 2018 Empathy ซึ่งการกลับมาของแจมินนั้นนับได้ว่าเป็นการกลับมาที่ทั้งแฟน ๆ และสมาชิกของวงตั้งตารอคอยกันเป็นอย่างมากหลังจากที่แจมินได้เดบิวต์
              ต่อมาในปี 2018 แจมินได้ร่วมเป็นแขกรับเชิญในซีซันที่สองของ [My English Teen 100 Hours](https://www.youtube.com/results?search_query=My+English+Teen+100+Hours+jaemin) ทางช่อง tvN 
              ซึ่งเป็นรายการวาไรตี้ ที่จะนำแขกรับเชิญมาเรียนภาษาอังกฤษเป็นเวลา 7 ชั่วโมงของแต่ละวันในช่วงสองสัปดาห์ 
              ก่อนที่จะถูกส่งไปต่างประเทศเพื่อทดสอบทักษะภาษาอังกฤษในชีวิตจริง นอกจากนี้แจมินยังร่วมเขียนเนื้อเพลง "[Dear Dream](https://youtu.be/4j_HQoJOeTg?si=AwW1pYOVxRiKEZxN)", 
              "[We Go up](https://youtu.be/LV1Es22E0RI?si=SFcIQqqprk2HYVAj)" และอีกหลาย ๆ เพลงในอัลบั้ม 
              ในเดือนตุลาคม 2020 แจมินได้เปิดตัวอย่างเป็นทางการในฐานะสมาชิกของ NCT U ด้วยเพลง "Make A Wish (Birthday Song)" 
              """)
   
   video_url = "https://youtu.be/tyrVtwE8Gv0?feature=shared"
   st.video(video_url)

   st.caption("ในเดือนตุลาคม ปี 2021 แจมินปรากฏตัวบนปกนิตยสาร WWD Korea ซึ่งเผยแพร่ร่วมกับ Tom Ford และช่างภาพ Adam Katz Sinding")

   st.image('b63a6e2cfd8ea308fb9739fed551497c.jpg', caption='ขอบคุณภาพจาก ㅁㄴ🦋 on Twitter')

with col3:
   st.header(" ")
   st.header(" ")
   st.caption("**ชื่อจริง** : Na Jaemin (นา แจมิน)")
   st.caption("**ชื่อเกาหลี/สเตจเนม** : 재민 Jaemin (แจมิน)")
   st.caption("**เกิด** : 13 สิงหาคม ค.ศ. 2000 (พ.ศ. 2543)")
   st.caption("**บ้านเกิด** : ชอนจู ประเทศเกาหลีใต้")
   st.caption("**สัญชาติ** : เกาหลีใต้")
   st.caption("**การศึกษา** : จบจาก School of Performing Arts Seoul (SOPA)")
   st.caption("**ตำแหน่ง** : เซนเตอร์ / ซับแร็ปเปอร์ / ซับโวคอล")
   st.caption("**ส่วนสูง** : 177 cm")
   st.caption("**หมู่เลือด** : AB")
   st.caption("**ยูนิต** : NCT DREAM, NCT U")

   st.subheader(' ', divider='red')

   st.header("FANCAM")

   st.caption(" - [페이스캠4K] 엔시티 드림 재민 :green['ISTJ' (NCT DREAM JAEMIN FaceCam) @SBS Inkigayo 230723]")
   video_url = "https://youtu.be/sPFxaEIPmQo?si=T895JoVR3ebFjOFQ"
   st.video(video_url)

   st.caption(" - [입덕직캠] 엔시티 유 재민 직캠 4K :green['Make A Wish' (NCT U JAEMIN FanCam) | @MCOUNTDOWN_2020.10.15]")
   video_url = "https://youtu.be/-l2vJiHTDDU?si=V6mtraeGBHnfkSnG"
   st.video(video_url)