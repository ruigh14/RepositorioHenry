import subprocess
SEG=[(0.0,9.22),(12.30,19.26),(24.70,28.48),(33.00,34.84),(38.50,41.30),(41.40,48.70),(51.26,52.98),(52.96,57.30),(67.55,71.90)]
FONT="/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
f=[]
for i,(a,b) in enumerate(SEG):
    f.append(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v{i}];[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={b-a-0.04:.2f}:d=0.04[a{i}]")
n=len(SEG)
f.append("".join(f"[v{i}][a{i}]" for i in range(n))+f"concat=n={n}:v=1:a=1[cv][ca]")
E="enable='lt(t,3.4)'"
f.append(f"[cv]drawbox=x=90:y=252:w=900:h=112:color=0x0E0F10@0.88:t=fill:{E},"
         f"drawtext=fontfile={FONT}:text='¿TENÉS MÁS DE 40?':fontcolor=white:fontsize=74:x=(w-text_w)/2:y=272:{E}[hv]")
f.append("[1:v]scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0x0d1416,setsar=1,format=yuv420p,trim=0:2.5,setpts=PTS-STARTPTS,fade=t=in:d=0.4[end]")
f.append("anullsrc=r=48000:cl=stereo,atrim=0:2.5[sil]")
f.append("[hv]format=yuv420p,setsar=1[hv2];[hv2][ca][end][sil]concat=n=2:v=1:a=1[ov][oa]")
subprocess.run(["ffmpeg","-v","error","-y","-i","in.mp4","-loop","1","-framerate","30","-i","/home/user/RepositorioHenry/pack-renova/pack_1.png","-filter_complex",";".join(f),
     "-map","[ov]","-map","[oa]","-r","30","-c:v","libx264","-preset","medium","-crf","19","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-movflags","+faststart","corto.mp4"],check=True)
