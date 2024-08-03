# import speech_recognition as sr
#
#
# # Создаем объект распознавателя речи
# recognizer = sr.Recognizer()
#
# # Загружаем аудио файл
# audio_file = sr.AudioFile('URecorder_20240721_122302.wav')
#
# # Распознаем речь из аудио файла
# with audio_file as source:
#     audio_data = recognizer.record(source)
#     text = recognizer.recognize_google(audio_data, language="ru-RU")
#     print(text)
# Выводим текст
# print(text)

# import speech_recognition as sr
#
# r = sr.Recognizer()
#
# with sr.Microphone() as source:
#     print('say something')
#     audio = r.listen(source)
#     voice_data = r.recognize_google(audio, language="ru-RU")
#     print(voice_data)


import speech_recognition as sr
r = sr.Recognizer()
harvard = sr.AudioFile('URecorder_20240721_122302.wav')
with harvard as source:
    audio = r.record(source)
print(r.recognize_google(audio))