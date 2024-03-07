import streamlit as st
import time

# Set up the Streamlit app
st.set_page_config(page_title="Centered Text Example", page_icon=":man:", layout="wide")

if st.button('Talk'):
    st.toast('I am Chenle')
    time.sleep(2.0)
    st.toast("But you can call me Daegal's father HAHAHA")
    time.sleep(2.0)
    st.toast("If you want to")
    time.sleep(2.0)
    st.toast("So. nice to meet you")
    time.sleep(2.0)

# Display centered text
st.markdown("""
<style>
.centered {
  text-align: center;
}
</style>
<div class="centered">
  <h1 style="color:#0072C6;">CHENLE</h1>
  <p>NCT DREAM</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
   st.header(" ")
   st.header(" ")
   st.image("FzjrkD1WAAAjdTn.jpg", width=300)

   instagram_link = "https://www.instagram.com/kh1000le?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="
   st.markdown(f"Instagram : [kh1000le]({instagram_link})", unsafe_allow_html=True)

with col2:
   st.header(" ")
   st.header(" ")
   st.caption("""Zhong Chenle (จง เฉินเล่อ) หรือที่รู้จักกันว่า เฉินเล่อ NCT เด็กชายชาวจีนที่ม่พร้อมกับพรสวรรค์มากมาย ก่อนที่เฉินเล่อจะได้เดบิวต์เป็น NCT 
              เฉินเล่อเป็นนักร้องอยู่แล้วในช่วงวัยเด็กของเขา โดยได้มีกรแสดงคอนเสิร์ตและรายการโทรทัศน์ต่าง ๆ ทั้งในจีนและต่างประเทศ 
              เมื่ออายุเก้าขวบ เฉินเล่อได้กลายเป็นนักร้องที่อายุน้อยที่สุดที่ได้รับเชิญให้แสดงเดี่ยวที่ Golden Hall of Vienna 
              และด้วยการทำงานเดี่ยวนั้นทำให้เฉินเล่อได้มีการออกอัลบั้มเป็นจำนวณสามอัลบั้มและจัดแสดงคอนเสิร์ตในรายการหนึ่งที่ประเทศจีน""")
    
   video_url = "https://youtu.be/_Xbq8IUqgtc?feature=shared"
   st.video(video_url)
  
   st.caption("""จากนั้นเมื่อเฉินเล่อายุสิบสี่ปี เขาก็ได้เซ็นสัญญากับทางค่าย SM Entertainment และย้ายไปเกาหลีใต้ในปี 2016 
              พร้อมกับเปิดตัวอย่างเป็นทางการในฐานะสมาชิกวง NCT DREAM ยูนิตย่อยของ NCT ในเพลง "Chewing Gum" และเป็นที่น่าตกใจเป็นอย่างมากเมื่อได้มารู้ว่า
              เฉินเล่อใช้เวลาในการเป็นเด็กฝึกเพียงแค่ 2 เดือนเท่านั้นก่อนเดบิวต์ """)

   st.caption("""อีกทั้งนอกเหนือจากนี้เฉินเล่อยังโคฟเวอร์เพลงลงในแพลตฟอร์มยูทูปที่ร้องร่วมกับจีซอง NCT อย่างเพลง YOUTH โดย Troye Sivan
              และอีกเพลงที่ได้ร่วมร้องกับคุน NCT มีชื่อเพลงว่า free love โดย HONNE""")

   video_url = "https://youtu.be/KEaHI-_H_6Q?feature=shared"
   st.video(video_url)

   video_url = "https://youtu.be/E_AYlWKqiic?feature=shared"
   st.video(video_url)

with col3:
   st.header(" ")
   st.header(" ")
   st.caption("**ชื่อจริง** : 钟辰乐 Zhong Chenle (จง เฉินเล่อ)")
   st.caption("**ชื่อเกาหลี/สเตจเนม** : 천러 Chenle (เฉินเล่อ)")
   st.caption("**เกิด** : 22 พฤศจิกายน ค.ศ. 2001 (พ.ศ. 2544)")
   st.caption("**บ้านเกิด** : เซี่ยงไฮ้ สาธารณรัฐประชาชนจีน")
   st.caption("**สัญชาติ** : จีน")
   st.caption("**การศึกษา** : จบจากโรงเรียนดนตรีร่วมสมัยปักกิ่ง")
   st.caption("**ตำแหน่ง** : เมนโวคอล")
   st.caption("**ส่วนสูง** : 176 cm")
   st.caption("**หมู่เลือด** : O")
   st.caption("**ยูนิต** : NCT DREAM")

   st.subheader(' ', divider='red')

   st.header("FANCAM")

   st.caption(" - [[안방1열 직캠4K] 엔시티 드림 천러 :green['Broken Melodies' (NCT DREAM CHENLE FanCam) @SBS Inkigayo 230625]")
   video_url = "https://youtu.be/6orpeaExCWU?si=l1CZD3pHI0SWZ17S"
   st.video(video_url)

   st.caption(" - [페이스캠4K] 엔시티 드림 천러 '고래' :green[(NCT DREAM CHENLE 'Dive Into You' FaceCam) │ @SBS Inkigayo_2021.05.16]")
   video_url = "https://youtu.be/0uwrNp4qOkA?si=MBArDmiMpnI37669"
   st.video(video_url)