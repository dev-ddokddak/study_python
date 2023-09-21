import speech_recognition as sr

# 인식기 초기화
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("말하세요:")
    audio = recognizer.listen(source)

    try:
        # Google Web 음성 API를 사용하여 인식
        print("당신이 말한 것: " + recognizer.recognize_google(audio, language="ko-KR"))
    except sr.UnknownValueError:
        print("음성 인식 실패")
    except sr.RequestError as e:
        print(f"API 요청 실패; {e}")