import speech_recognition as sr

recognizer = sr.Recognizer()

# 무한 루프로 계속해서 음성 인식을 시도
while True:
    with sr.Microphone() as source:
        print("말하세요 (종료하려면 '종료'라고 말하세요):")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="ko-KR")
            print(f"당신이 말한 것: {text}")

            # 종료 명령어 확인
            if text == "종료":
                print("프로그램을 종료합니다.")
                break
        except sr.UnknownValueError:
            print("음성을 인식할 수 없습니다.")
        except sr.RequestError as e:
            print(f"API 요청 에러; {e}")