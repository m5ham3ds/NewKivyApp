from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
import requests
from PIL import Image
import os
import re
from moviepy.editor import ImageSequenceClip, AudioFileClip
from bs4 import BeautifulSoup
import json
from io import BytesIO
import google.generativeai as genai
class ContentCreationApp(BoxLayout):

    def __init__(self, **kwargs):
        super(ContentCreationApp, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # إضافة شريط التحميل
        self.progress_bar = ProgressBar(max=100)
        self.add_widget(self.progress_bar)

        # حقول إدخال لمفاتيح API و Voice ID
        self.gemini_key = TextInput(hint_text="أدخل مفتاح جيميناي", size_hint=(1, None), height=40)
        self.eleven_key = TextInput(hint_text="أدخل مفتاح الفن لابس", size_hint=(1, None), height=40)
        self.voice_id = TextInput(hint_text="أدخل Voice ID", size_hint=(1, None), height=40)  # تم إضافة هذا الحقل
        self.add_widget(self.gemini_key)
        self.add_widget(self.eleven_key)
        self.add_widget(self.voice_id)

        # قائمة منسدلة لاختيار نوع المحتوى
        self.content_types = Spinner(
            text="اختر نوع المحتوى",
            values=[ "معلومات عامة انجليزي", "معلومات عامة عربي", "شرح مواقع تعمل بذكاء الاصطناعي", "أفكار و مقترحات لعمل محتوى على النت", "فيديوهات مضهكة ", "توب 10", "توب 5", "مراجعة هواتف", "مراجعة برامج", "قصص غامض ومثيرة", "قصص تحقيق وجريمه" ],
            size_hint=(1, None), height=40
        )
        self.add_widget(self.content_types)

        # قائمة منسدلة لاختيار أبعاد الصورة
        self.image_sizes = Spinner(
            text="اختر أبعاد الصورة",
            values=["1080x1920", "1920x1080"],
            size_hint=(1, None), height=40
        )
        self.add_widget(self.image_sizes)

        # زر لإنشاء المحتوى
        self.create_btn = Button(text="إنشاء المحتوى", size_hint=(1, None), height=40)
        self.create_btn.bind(on_press=self.create_content)  # ربط الضغط على الزر مع وظيفة إنشاء المحتوى
        self.add_widget(self.create_btn)

        # إضافة حقل لاختيار مدة الفيديو
        self.video_duration = TextInput(hint_text="أدخل مدة الفيديو بالثواني", size_hint=(1, None), height=40)
        self.add_widget(self.video_duration)

        # زر لحفظ الإعدادات
        self.save_settings_btn = Button(text="حفظ الإعدادات", size_hint=(1, None), height=40)
        self.save_settings_btn.bind(on_press=self.save_settings)
        self.add_widget(self.save_settings_btn)

        # زر لإضافة محتوى جديد
        self.add_content_btn = Button(text="إضافة محتوى جديد", size_hint=(1, None), height=40)
        self.add_content_btn.bind(on_press=self.add_content)
        self.add_widget(self.add_content_btn)

        # زر لعرض المحتويات المضافة
        self.show_content_btn = Button(text="عرض المحتويات المضافة", size_hint=(1, None), height=40)
        self.show_content_btn.bind(on_press=self.show_added_content)
        self.add_widget(self.show_content_btn)

    def generate_script(self, api_key, content_type):
        # توليد نص الاسكربت بناءً على نوع المحتوى المختار
        try:
            prompt_map = {
    "معلومات عامة انجليزي": "Well, connect all search engines in the world and write me a script in English, talking about information, discoveries, civilizations, technology, customs, companies, businesses and projects in a professional manner. Also, make the beginning of the video enthusiastic and exciting to attract the viewer. And I finished the video by inviting the viewer to like the video and subscribe to the channel.",
    "معلومات عامة عربي": "Well, connect all search engines in the world and write me a script in Arabic, talking about information, discoveries, civilizations, technology, customs, companies, businesses and projects in a professional manner. Also, make the beginning of the video enthusiastic and exciting to attract the viewer. And I finished the video by inviting the viewer to like the video and subscribe to the channel.", 
    "شرح مواقع تعمل بذكاء الاصطناعي": "Well, connect all search engines in the world and write me a script in English, talking about an artificial intelligence site, to make a video montage, create a full website, blogs, write an article, and create professional posts in a professional way. Also, make the beginning of the video enthusiastic and exciting to attract the viewer. And I finished the video by inviting the viewer to like the video and subscribe to the channel.", 
    "أفكار و مقترحات لعمل محتوى على النت": "Well, connect all the search engines in the world and write me a script in English that talks about ideas and suggestions for creating content on the Internet and social media platforms in a professional way. Also, make the beginning of the video enthusiastic and exciting to attract the viewer. And I finished the video by inviting the viewer to like the video and subscribe to the channel.",  
    "فيديوهات ههه": "Well, connect all the search engines in the world and write me a script in English, talking about funny and fun videos in a professional way. Also, make the beginning of the video enthusiastic and exciting to attract the viewer. And I finished the video by inviting the viewer to like the video and subscribe to the channel.",
    "توب 10": "Well, connect all the search engines in the world and write me a script in English. It talks about making top10 videos. One of the top ten things, for example, are the top ten projects, the best ten Cyprus, the best ten cars, the best ten buildings in the world or the best. Ten airports and so on professionally. Also, make the beginning of the video enthusiastic and exciting to attract the viewer. And I finished the video by inviting the viewer to like the video and subscribe to the channel.",
    "توب 5": "Well, connect all search engines in the world and write me a script in English. It talks about making top5 videos. One of the top five things. Airports and so on professionally. Also, make the beginning of the video enthusiastic and exciting to attract the viewer. And I finished the video by inviting the viewer to like the video and subscribe to the channel.",
    "مراجعة هواتف": "Well, connect all the search engines in the world and write me a script in English, talking about a review of the new phones and computers. Every time I update the text, I make a different phone or computer references in a professional way. Also, make the beginning of the video enthusiastic and exciting to attract the viewer. And I finished the video by inviting the viewer to like the video and subscribe to the channel.",  
    "مراجعة برامج": "Well, connect all search engines in the world and write me a script in English, talking about making videos, explaining different and new programs and applications in a professional way. Also, make the beginning of the video enthusiastic and exciting to attract the viewer. And I finished the video by inviting the viewer to like the video and subscribe to the channel.", 
    "قصص غامض ومثيرة": "Well, connect all the search engines in the world and write me a script in English that talks about making mysterious and exciting stories that contain mystery and an exciting plot in a professional way. Also, make the beginning of the video enthusiastic and exciting to attract the viewer. And I finished the video by inviting the viewer to like the video and subscribe to the channel.",
    "قصص تحقيق وجريمه": "Well, connect all the search engines in the world and write me a script in English that talks about making investigation stories and a crime that contains mystery and an exciting plot in a professional way. Also, make the beginning of the video enthusiastic and exciting to attract the viewer. And I finished the video by inviting the viewer to like the video and subscribe to the channel.",
                # إضافة بقية المطالبات حسب الحاجة
            }

            prompt = prompt_map.get(content_type)
            if not prompt:
                return ""

            # استخدام نموذج التوليد للحصول على النص
            response = "Generated text"  # يُستبدل بالنداء الحقيقي للـ API
            return response
        except Exception as e:
            print(f"Error generating script: {e}")
            return ""

    def clean_script(self, script):
        # تنظيف النص من السطور غير المرغوبة
        lines = script.split('\n')
        cleaned_lines = [line for line in lines if not any(word in line.lower() for word in ['مشهد', 'صورة', 'لقطة'])]
        return '\n'.join(cleaned_lines)

    def generate_voiceover(self, script, api_key, voice_id):
        # توليد التعليق الصوتي من النص باستخدام API Eleven Labs
        try:
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": api_key
            }
            data = {
                "text": script,
                "model_id": "eleven_multilingual_v2",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.5
                }
            }
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            output_audio_filename = 'arabic_voiceover.mp3'
            with open(output_audio_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            return output_audio_filename
        except Exception as e:
            print(f"Error generating voiceover: {e}")
            return None

    def extract_arabic_key_terms(self, script):
        # استخراج الكلمات المفتاحية العربية من النص للبحث عن الصور
        words = re.findall(r'\b[\u0600-\u06FF]+\b', script)
        return list(set(words))

    def download_images_from_bing(self, query, num_images, folder):
        # تحميل الصور من Bing بناءً على الاستعلام
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        search_url = f"https://www.bing.com/images/search?q={query}&FORM=HDRSC2"
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        image_elements = soup.find_all('a', {'class': 'iusc'})

        os.makedirs(folder, exist_ok=True)
        image_count = 0

        for i, img_element in enumerate(image_elements):
            if image_count >= num_images:
                break
            m = img_element.get('m')
            if m:
                m = json.loads(m)
                img_url = m['murl']

                if img_url:
                    try:
                        img_data = requests.get(img_url, headers=headers, timeout=10).content
                        img = Image.open(BytesIO(img_data))
                        img = self.resize_and_crop_image(img)
                        img_filename = os.path.join(folder, f'image_{image_count + 1}.png')  # حفظ بصيغة PNG
                        img.save(img_filename, format='PNG', quality=95)
                        image_count += 1
                        print(f"Downloaded {img_filename}")
                    except Exception as e:
                        print(f"Failed to download image {i + 1}: {e}")

    def resize_and_crop_image(self, img):
        # تعديل حجم الصورة لتناسب الأبعاد المستهدفة
        selected_size = self.image_sizes.text
        target_size = (1080, 1920) if selected_size == "1080x1920" else (1920, 1080)

        img_ratio = img.width / img.height
        target_ratio = target_size[0] / target_size[1]

        if img_ratio > target_ratio:
            new_width = int(img.height * target_ratio)
            left = (img.width - new_width) // 2
            img = img.crop((left, 0, left + new_width, img.height))
        else:
            new_height = int(img.width / target_ratio)
            top = (img.height - new_height) // 2
            img = img.crop((0, top, img.width, top + new_height))

        img = img.resize(target_size, Image.LANCZOS)
        return img

    def create_video(self, image_folder, audio_filename):
        # إنشاء فيديو من الصور والصوت
        try:
            image_files = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(".png")]
            clip = ImageSequenceClip(image_files, fps=1)
            audio = AudioFileClip(audio_filename)
            video_duration = int(self.video_duration.text or 10)  # استخدام مدة الفيديو المحددة من قبل المستخدم
            video = clip.set_duration(video_duration).set_audio(audio)
            video.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac")
        except Exception as e:
            print(f"Error creating video: {e}")

    def create_content(self, instance):
        # الوظيفة الرئيسية لإنشاء المحتوى
        self.progress_bar.value = 10  # تحديث شريط التحميل
        gemini_api_key = self.gemini_key.text
        eleven_labs_api_key = self.eleven_key.text
        voice_id = self.voice_id.text
        content_type = self.content_types.text

        # توليد النص
        script = self.generate_script(gemini_api_key, content_type)
        if not script:
            self.show_popup("لا يوجد نص لتوليد المحتوى.")
            return

        self.progress_bar.value = 30  # تحديث شريط التحميل

        # تنظيف النص
        cleaned_script = self.clean_script(script)
        
        # توليد التعليق الصوتي
        voiceover_filename = self.generate_voiceover(cleaned_script, eleven_labs_api_key, voice_id)
        if not voiceover_filename:
            self.show_popup("خطأ في توليد التعليق الصوتي.")
            return

        self.progress_bar.value = 50  # تحديث شريط التحميل

        # استخراج الكلمات المفتاحية
        key_terms = self.extract_arabic_key_terms(cleaned_script)

        # تحميل الصور لكل كلمة مفتاحية
        for term in key_terms:
            self.download_images_from_bing(term, num_images=2, folder="visual")

        self.progress_bar.value = 75  # تحديث شريط التحميل

        # إنشاء الفيديو
        try:
            self.create_video("visual", voiceover_filename)
            self.show_popup("تم إنشاء المحتوى بنجاح!")
        except Exception as e:
            self.show_popup(f"حدث خطأ أثناء إنشاء الفيديو: {e}")

        self.progress_bar.value = 100  # تحديث شريط التحميل

    def save_settings(self, instance):
        # حفظ الإعدادات الحالية
        settings = {
            "gemini_key": self.gemini_key.text,
            "eleven_key": self.eleven_key.text,
            "voice_id": self.voice_id.text,
            "content_type": self.content_types.text,
            "image_size": self.image_sizes.text,
            "video_duration": self.video_duration.text
        }
        with open("settings.json", "w") as settings_file:
            json.dump(settings, settings_file)
        self.show_popup("تم حفظ الإعدادات بنجاح.")  # إرسال إشعار للمستخدم

    def add_content(self, instance):
        # إضافة محتوى جديد
        content_popup = Popup(title='إضافة محتوى جديد', size_hint=(0.9, 0.9))
        content_layout = BoxLayout(orientation='vertical')
        
        content_name_input = TextInput(hint_text="اسم نوع المحتوى", size_hint=(1, None), height=40)
        content_text_input = TextInput(hint_text="النص لإرساله إلى API جيميناي", size_hint=(1, None), height=40)
        
        add_content_button = Button(text="إضافة المحتوى", size_hint=(1, None), height=40)
        add_content_button.bind(on_press=lambda x: self.add_custom_content(content_name_input.text, content_text_input.text, content_popup))
        
        content_layout.add_widget(content_name_input)
        content_layout.add_widget(content_text_input)
        content_layout.add_widget(add_content_button)
        
        content_popup.content = content_layout
        content_popup.open()

    def add_custom_content(self, name, text, popup):
        # حفظ المحتوى المضاف
        custom_content = {
            "name": name,
            "text": text
        }
        try:
            with open("custom_content.json", "a") as content_file:
                json.dump(custom_content, content_file)
                content_file.write("\n")
            self.show_popup("تمت إضافة المحتوى بنجاح.")
            popup.dismiss()
        except Exception as e:
            self.show_popup(f"خطأ في إضافة المحتوى: {e}")

    def show_added_content(self, instance):
        # عرض المحتويات المضافة وتعديلها
        try:
            with open("custom_content.json", "r") as content_file:
                contents = content_file.readlines()

            content_popup = Popup(title='المحتويات المضافة', size_hint=(0.9, 0.9))
            content_layout = BoxLayout(orientation='vertical')

            for content in contents:
                content_data = json.loads(content)
                content_label = Label(text=f"الاسم: {content_data['name']} - النص: {content_data['text']}", size_hint=(1, None), height=40)
                content_layout.add_widget(content_label)

            content_popup.content = content_layout
            content_popup.open()
        except Exception as e:
            self.show_popup(f"خطأ في عرض المحتويات: {e}")

    def show_popup(self, message):
        # عرض نافذة منبثقة مع رسالة
        popup = Popup(title='إشعار', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

class MyApp(App):
    def build(self):
        return ContentCreationApp()

if __name__ == '__main__':
    MyApp().run()