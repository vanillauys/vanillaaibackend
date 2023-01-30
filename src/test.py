from youtube.youtube import Youtube
from ai.transcribe import WhisperAI
from ai.gpt import DavinciAI
from ai.dalle import DalleAI


yt = Youtube()
ws = WhisperAI()
dv = DavinciAI()
dl = DalleAI()


def main():
    code, response, title = yt.download_audio('https://www.youtube.com/watch?v=8nHBGFKLHZQ')

    print(code, response)

    code, text, err = ws.transcribe_audio(f'videos/{title}')

    print(code, err)

    code, response, data = dv.summarize(text)

    print(code, data)

if __name__ == '__main__':
    main()
