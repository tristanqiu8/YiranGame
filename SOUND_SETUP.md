# Duck Game Sound Setup Guide

To enable sounds in the game, you need to prepare the following audio files:

## Required Directory Structure
```
game_demo/
├── duck_game.py
├── sounds/              # Create this folder
│   ├── collect.wav      # Collection sound effect
│   └── background.mp3   # Background music
└── SOUND_SETUP.md
```

## Audio File Requirements

### 1. Collection Sound Effect (collect.wav)
- Format: WAV
- Duration: 0.5-1 second
- Suggested sounds: coin pickup, bubble pop, or cheerful ding
- Volume: Will be set to 50% in game

### 2. Background Music (background.mp3)
- Format: MP3
- Duration: 2-5 minutes (will loop)
- Style: Cheerful, light, game-like music
- Volume: Will be set to 30% in game

## How to Enable Sounds

1. Create a `sounds` folder in the game directory
2. Add your audio files with the exact names: `collect.wav` and `background.mp3`
3. Edit `duck_game.py` and uncomment the following lines (remove the # and adjust indentation):
   - Lines 36-37 for collection sound
   - Lines 44-46 for background music

## Free Sound Resources
- Freesound.org - Free sound effects (requires account)
- OpenGameArt.org - Free game music and sounds
- Zapsplat.com - Free sounds with account
- Pixabay.com - Royalty-free music and sounds

## Troubleshooting
- If sounds don't work, check console for error messages
- Ensure pygame mixer is properly installed
- Verify file names match exactly (case-sensitive)
- Check audio file formats are supported by pygame