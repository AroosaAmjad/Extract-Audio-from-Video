import moviepy.editor

cvt_video = moviepy.editor.VideoFileClip("Time to take you file name")
ext_audio = cvt_video.ext_audio
ext_audio.write_audiofile("audio_extarcted.mp3")