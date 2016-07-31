# Sound Wave Generator

This app produces sound waves of frequency you wish.

If you want to generate audio waves of frequency 432 MHz:

```python
python generate.py 432 > wave432.wav
# Ctrl+C after you think the duration is fine.

# If you want to convert wav to mp3:
ffmpeg -i wave432.wav -codec:a libmp3lame -qscale:a 2 wave432.mp3
```
