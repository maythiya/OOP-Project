import streamlit as st
import time 

# Set up the Streamlit app
st.set_page_config(page_title="Huang RenJun", page_icon=":fox_face:", layout="wide")

if st.button('Talk'):
    st.toast('Hello')
    time.sleep(2.0)
    st.toast("I'm a gentle men")
    time.sleep(2.0)
    st.toast('RENJUN~', icon='🎉')
    time.sleep(2.0)

# Display centered text
st.markdown("""
<style>
.centered {
  text-align: center;
}
</style>
<div class="centered">
  <h1 style="color:#0072C6;">RENJUN</h1>
  <p>NCT DREAM</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
   st.header(" ")
   st.header(" ")
   st.image("Fzo0We-aUAALKsf.jpg", width=300)

   instagram_link = "https://www.instagram.com/yellow_3to3?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="
   st.markdown(f"Instagram : [yellow_3to3]({instagram_link})", unsafe_allow_html=True)

with col2:
   st.header(" ")
   st.header(" ")
   st.caption("""Huang Renjun (หวง เหรินจวิ้น) สมาชิกของบอยแบนด์ชาวจีน NCT ภายใต้สังกัด SM Entertainment หรือที่หลาย ๆ คนรู้จักในนาม อินจุน/เหรินจวิ้น NCT บุคคลที่มีเสียงร้องเป็นเอกลักษณ์และไม่เหมือนใคร 
              อินจุนริ่มต้นที่จะทำตามความฝันของตัวเองด้วยการเข้ามาออดิชันกับ SM Global Audition ที่เมืองเสิ่นหยาง ประเทศจีน ไม่นานอินจุนก็ได้รับเข้าไปเป็นเด็กฝึกของค่าย SM Entertainment ในปี 2015 
              อินจุนเป็นหนึ่งในสมาชิกสี่คนของ NCT ที่ไม่ได้เป็นส่วนหนึ่งของ SM Rookies ก่อนวงจะเดบิวต์ ต่อมาอินจุนก็ได้เดบิวต์ครั้งแรกในเพลง "Chewing Gum" ตำแหน่งเมนโวคอล และซับแดนซ์ อีกทั้งยังเป็นดีเจและนักแสดง ต่อมาในช่วงวันที่ 14 มีนาคม 2018 NCT ได้เปิดตัวอัลบั้มเต็มชุดแรกโดยมีอินจุนเป็นส่วนหนึ่งของโปรเจ็กต์ขนาดใหญ่นี้ ที่จะรวมทุกกลุ่มย่อยทั้งหมดเข้าด้วยกันในโปรเจ็กต์ที่ชื่อว่า "NCT 2018 Empathy" 
              วันที่ 12 ตุลาคม 2020 อินจุนได้เดบิวต์อีกครั้งภายใต้ยูนิต NCT U จากโปรเจ็กต์ "NCT Resonance" ในเพลง "From Home" ซึ่งเป็นที่ฮือฮาอย่างมากในตอนนั้น ไม่ว่าจะด้วยเสียงร้องและการแสดงเอ็มวีที่ทำให้เข้าถึงอารมณ์เป็นอย่างดี อินจุนมีความสามารถที่หลากหลายทั้งด้านร้องเพลง เต้น และวาดภาพ ทั้งนี้อินจุนยังเคยเป็นดีเจวิทยุของ TBS Radio ตั้งแต่วันที่ 5 สิงหาคม 2019 ถึงวันที่ 11 ตุลาคม 2020
              รวมไปถึงร่วมแต่งเพลงในอัลบั้ม ISTJ อย่าง "Like We Just Met" """)
   
   video_url = "https://youtu.be/eA9pwL-8wJw?feature=shared"
   st.video(video_url)

   st.caption("นอกเหนือจากนี้อินจุนได้มีอีกหลากหลายเพลงที่โคฟเวอร์ เช่น なんでもないや (아무것도 아니야) (RADWIMPS) และ golden hour (JVKE)")

   video_url = "https://youtu.be/kBVdYh5G6cc?feature=shared"
   st.video(video_url)

   video_url = "https://youtu.be/qYXgudKV7fI?feature=shared"
   st.video(video_url)

with col3:
   st.header(" ")
   st.header(" ")
   st.caption("**ชื่อจริง** : 黄仁俊 Huang RenJun (หวง เหรินจวิ้น)")
   st.caption("**ชื่อเกาหลี** : 황인준 Hwang Injun (ฮวัง อินจุน)")
   st.caption("**เกิด** : พฤหัสบดีที่ 23 มีนาคม 2000 (พ.ศ. 2543)")
   st.caption("**บ้านเกิด** : จี๋หลิน สาธารณรัฐประชาชนจีน")
   st.caption("**สัญชาติ** : จีน")
   st.caption("**การศึกษา** : จบจากโรงเรียนดนตรีร่วมสมัยที่ปักกิ่ง")
   st.caption("**ตำแหน่ง** : เมนโวคอล / ซับแดนซ์")
   st.caption("**สูง** : 171 cm")
   st.caption("**หมู่เลือด** : O")
   st.caption("**ยูนิต** : NCT DREAM, NCT U")

   st.subheader(' ', divider='red')

   st.header("FANCAM")

   st.caption(" - [K-Fancam] 엔시티 드림 런쥔 직캠 :green['ISTJ' (NCT DREAM RENJUN Fancam) @뮤직뱅크(Music Bank)]")
   video_url = "https://youtu.be/fAneh1lcWWY?si=D8nvwSakwXryjUiV"
   st.video(video_url)

   st.caption(" - [4K] 231202 MMA 멜론 뮤직 어워드 런쥔 :green[(RENJUN) 직캠 - Poison (모래성)]")
   video_url = "https://youtu.be/r1SERVVSPWU?si=BhbGUFnvIP1R9xL3"
   st.video(video_url)
