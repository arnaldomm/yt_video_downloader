from pytube import YouTube

# Terminal colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Path to save
path = './Downloads'

# Read URLs
lines = []
with open('urls.txt') as f:
    lines = f.readlines()

for url in lines:
    try:
        url = url.rstrip()
        yt = YouTube(url)
        st = yt.streams.filter(progressive=True, file_extension='mp4') # only progresive videos that contains the audio embedded
        st = st.get_highest_resolution() # get the highest resolution. For progressive videos, the maximun will be 720p
        st.download(path)
        print(f' {bcolors.OKGREEN}{url}{bcolors.ENDC}')
    except:
        print(f' {bcolors.FAIL}{url}{bcolors.ENDC}')