import streamlit as st

tab1, tab2 = st.tabs(["NCT DREAM", "Quotes"])

with tab1:
   st.header("What's about NCT DREAM?")
   st.image("dream beatbox.jpg", width=720)
   st.subheader(':blue[NCT DREAM (เกาหลี: 엔시티 드림, ไทย: เอ็นซีทีดรีม)]')
   st.caption("""
   เป็นกลุ่มบอยแบรนด์ชายในประเทศเกาหลีใต้ ยูนิตนี้เปิดตัวเมื่อวันที่ 18 สิงหาคม 2016 ด้วยเพลงน่ารักสดใสสมวัยอย่าง ‘Chewing Gum’ 
   โดยที่ในตอนนั้นมีสมาชิกทั้งหมด 7 คน ได้แก่ **มาร์ค (Mark)**, **แฮชาน (Haechan)**, **แจมิน (Jaemin)**, **เจโน่ (Jeno)**, **เหรินจวิ้น (Renjun)**, **เฉินเล่อ (Chenle)** และ**จีซอง (Jisung)** 
   โดยมีระบบวงที่เป็นเอกลักษณ์ คือ ***การเข้าศึกษา-จบการศึกษา*** เหมือนกับโรงเรียนมัธยมเมื่อสมาชิกมีอายุเกาหลีไม่เกิน 20 ปี (อายุสากล 19 ปี) จะถูกแยกตัวจาก NCT ยูนิต Dream เพื่อที่จะไปเข้าร่วมกับ NCT ในยูนิตใหม่ ทำให้สมาชิกจะอยู่ในยูนิตนี้ได้สูงสุดเพียงแค่ 6 ปีเท่านั้น 
   แต่ในวันที่ 14 เมษายน 2020 SM Entertainment 
   ได้ประกาศยกเลิกระบบการเข้าศึกษา-จบการศึกษา ทำให้มาร์คที่จบการศึกษาไปเมื่อ 2018 ได้กลับมาเข้าร่วมกลุ่มอีกครั้ง ในตอนนั้นเรียกเสียงฮือฮาเป็นอย่างมากกับคอนเซ็ปต์ของเด็ก ๆ ที่สุดแสนจะน่ารักน่าเอ็นดู แต่ก็เกิดเหตุไม่คาดฝันในการคัมแบ็คครั้งต่อมา เนื่องจากแจมินได้มีอาการป่วย 
   ทำให้ไม่สามารถมาทำกิจกรรมกับวงต่อได้ จึงเหลือสมาชิกเพียงแค่ 6 คน โดยที่วงยังคงคัมแบ็คด้วยเพลง ‘My First and Last’ และ ‘We Young’ หลังจากนั้นแจมินก็ได้กลับมาคัมแบ็คด้วยกันอีกครั้งในเพลง ‘Go’ ซึ่งเป็นส่วนหนึ่งในโปรเจกต์ NCT 2018 นอกจากนี้
   Nct dream ยังเป็นยูนิตย่อยที่แยกตัวมาจาก NCT และมีคอนเซ็ปต์ประจำวงเป็นของตัวเอง บางสมาชิกอย่าง มาร์ค และแฮชาน
   จะได้เข้าร่วมกับยูนิตอื่น ๆ เช่น NCT U, NCT 127 หรือวงอื่น ๆ นอกเหนือจากนี้ตามคอนเซ็ปต์ที่ได้รับ
   หากสมาชิกคนใดที่มีคอนเซ็ปต์เข้ากับเพลงในยูนิตนั้น ๆ จะได้เข้าร่วมและโปรโหมด                               
   """)

   st.subheader(':blue[ข้อมูลพื้นฐาน]')
   st.caption("**ประเทศ** : โซล, เกาหลีใต้")
   st.caption('**แนวเพลง** : K-pop, Hip-Hop, R&B, Funk, Teen pop')
   st.caption('**ค่ายเพลง** : SM Entertainment')
   st.caption('**แยกตัวมาจาก** : NCT (NCT DREAM เป็นยูนิตย่อย)')
   st.caption('**ชื่อแฟนคลับ** : NCTzen (อ่านว่า “เอ็นซีทีเซน”)')


   st.subheader(' ', divider='red')

   st.subheader(':blue[อัลบั้ม/ผลงานเพลง]')
   st.caption("Chewing Gum - The 1st Single (2016)")
   st.caption("The First - The 1st Single Album (2017)")
   st.caption("We Young - The 1st Mini Album (2017)")
   st.caption("We Boom - The 3rd Mini Album (2019)")
   st.caption("THE DREAM SHOW - The 1st Live Album (2020)")
   st.caption("Hot Sauce - The 1st Album (2021)")
   st.caption("Hello Future - The 1st Album Repackage (2021)")
   st.caption("Glitch Mode - The 2nd Album (2022)")
   st.caption("Beatbox - The 2nd Album Repackage (2022)")
   st.caption("ISTJ - The 3rd Album (2023)")

   st.subheader(':blue[Top 3 เพลงยอดฮิตของ NCT DREAM]')
   st.caption(""" - :green[오르골 (Life Is Still Going On)]
Hello Future - The 1st Album Repackage""")
   
   video_url = "https://youtu.be/aq2epFJ4fR4?feature=shared"
   st.video(video_url)

   st.caption(""" - :green[BOOM]
We Boom - The 3rd Mini Album""")
   
   video_url = "https://youtu.be/X-iJZ0gfKPo?feature=shared"
   st.video(video_url)

   st.caption(""" - :green[Candy]
Candy - Winter Special Mini Album""")

   video_url = "https://youtu.be/zuoSn3ObMz4?feature=shared"
   st.video(video_url)

   st.subheader(':blue[ช่องทางแพลตฟอร์มต่าง ๆ]')

   youtube_link = "https://www.youtube.com/@NCTDREAM"
   st.markdown(f"Youtube NCT DREAM : [www.youtube.com/@NCTDREAM]({youtube_link})", unsafe_allow_html=True)

   twitter_link = "https://x.com/NCTsmtown_DREAM?s=20"
   st.markdown(f"NCT DREAM Twitter : [@NCTsmtown_DREAM]({twitter_link})", unsafe_allow_html=True)

   instagram_link = "https://x.com/NCTsmtown_DREAM?s=20"
   st.markdown(f"NCT DREAM Instagram : [nct_dream]({instagram_link})", unsafe_allow_html=True)


with tab2:
   st.header(":blue[Quotations by Members]")

   col1, col2 = st.columns(2)

with col1:
   st.header(" ")
   st.image("F4YCFS9b0AE76-k.png", width=300)
with col2:
   st.header(" ")
   st.subheader("**Mark Lee**")
   st.caption("""You're doing fine, sometimes you're doing better
              sometimes you're doing worse, but at the end ***it's you.***
              I want you to feel yourself grow
              and just to love yourself""")

with col1:
   st.header(" ")
   st.subheader("**Huang Renjun**")
   st.caption("""It's not good to laugh at someone.
              ***Don't use someone's*** weakness as a joke.""")
with col2:
   st.header(" ")
   st.image("F4YCH9qbgAEQ51M.png", width=300)

with col1:
   st.header(" ")
   st.image("F4YNrOQXkAAthJW.jpg", width=300)
with col2:
   st.header(" ")
   st.subheader("**Lee Jeno**")
   st.caption("""***Dream high.*** Instead of satisfies of what I've done,
              I said this to myself ‘No, this isn't enough’""" )

with col1:
   st.header(" ")
   st.subheader("**Lee Haechan**")
   st.caption("""There are many people in the world who hate me, 
              I'll spend my time only for those who like me. If you like me 
              you won't regret it. If you trust me, I'll bring you more 
              ***happiness***.""")
with col2:
   st.header(" ")
   st.image("F4YODGnXwAA6Sv9.jpg", width=300)

with col1:
   st.header(" ")
   st.image("F4YOP0MXcAAPwNX.jpg", width=300)
with col2:
   st.header(" ")
   st.subheader("**Na Jaemin**")
   st.caption("""Treasure yourself well, so you can spread more love to 
              those people around you. That's why ***yourself always comes first***""")

with col1:
   st.header(" ")
   st.subheader("**Zhong Chenle**")
   st.caption("When you chink positively, ***everything gets better.***")

with col2:
   st.header(" ")
   st.image("F4YOVnCWIAAGXqH.jpg", width=300)

with col1:
   st.header(" ")
   st.image("F4YObLOXEAExhKM.jpg", width=300)

with col2:
   st.header(" ")
   st.subheader("**Park Jisung**")
   st.caption("Don't only smile when you're happy. But ***smile to be happy.***")