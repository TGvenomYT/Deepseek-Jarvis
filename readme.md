# Jarvis Assistant

Jarvis Assistant is a personal assistant application that utilizes
the DeepSeek API to provide conversational capabilities and voice interaction features.
This project aims to create a seamless user experience by integrating text and voice commands.

#features

## Features

- **DeepSeek Integration**: Communicate with the ChatGPT API to receive intelligent responses.
- **Voice Interaction**: Use voice commands to interact with the assistant.
- **Environment Configuration**: Load environment variables for secure API key management.


## Project Structure

```
jarvis-assistant
├── src
│   ├── main.py               # Entry point of the application
│   ├── assistant.py          # Assistant class for handling user input
├── requirements.txt           # List of dependencies
└── README.md                # Project documentation
```
Available voice models
======================
languages and its indexes are as follows:

Voice 0: Afrikaans Voice 1: Amharic Voice 2: Aragonese Voice 3: Arabic Voice 4: Assamese Voice 5: Azerbaijani Voice 6: Bashkir Voice 7: Belarusian Voice 8: Bulgarian Voice 9: Bengali Voice 10: Bishnupriya Manipuri Voice 11: Bosnian Voice 12: Catalan Voice 13: Cherokee Voice 14: Chinese (Mandarin, latin as English) Voice 15: Chinese (Mandarin, latin as Pinyin) Voice 16: Czech Voice 17: Chuvash Voice 18: Welsh Voice 19: Danish Voice 20: German Voice 21: Greek Voice 22: English (Caribbean) Voice 23: English (Great Britain) Voice 24: English (Scotland) Voice 25: English (Lancaster) Voice 26: English (West Midlands) Voice 27: English (Received Pronunciation) Voice 28: English (America) Voice 29: English (America, New York City) Voice 30: Esperanto Voice 31: Spanish (Spain) Voice 32: Spanish (Latin America) Voice 33: Estonian Voice 34: Basque Voice 35: Persian Voice 36: Persian (Pinglish) Voice 37: Finnish Voice 38: French (Belgium) Voice 39: French (Switzerland) Voice 40: French (France) Voice 41: Gaelic (Irish) Voice 42: Gaelic (Scottish) Voice 43: Guarani Voice 44: Greek (Ancient) Voice 45: Gujarati Voice 46: Hakka Chinese Voice 47: Hawaiian Voice 48: Hebrew Voice 49: Hindi Voice 50: Croatian Voice 51: Haitian Creole Voice 52: Hungarian Voice 53: Armenian (East Armenia) Voice 54: Armenian (West Armenia) Voice 55: Interlingua Voice 56: Indonesian Voice 57: Ido Voice 58: Icelandic Voice 59: Italian Voice 60: Japanese Voice 61: Lojban Voice 62: Georgian Voice 63: Kazakh Voice 64: Greenlandic Voice 65: Kannada Voice 66: Korean Voice 67: Konkani Voice 68: Kurdish Voice 69: Kyrgyz Voice 70: Latin Voice 71: Luxembourgish Voice 72: Lingua Franca Nova Voice 73: Lithuanian Voice 74: Latgalian Voice 75: Latvian Voice 76: Māori Voice 77: Macedonian Voice 78: Malayalam Voice 79: Marathi Voice 80: Malay Voice 81: Maltese Voice 82: Myanmar (Burmese) Voice 83: Norwegian Bokmål Voice 84: Nahuatl (Classical) Voice 85: Nepali Voice 86: Dutch Voice 87: Nogai Voice 88: Oromo Voice 89: Oriya Voice 90: Punjabi Voice 91: Papiamento Voice 92: Klingon Voice 93: Polish Voice 94: Portuguese (Portugal) Voice 95: Portuguese (Brazil) Voice 96: Pyash Voice 97: Lang_Belta Voice 98: Quechua Voice 99: K'iche' Voice 100: Quenya Voice 101: Romanian Voice 102: Russian Voice 103: Russian (Latvia) Voice 104: Sindhi Voice 105: Shan (Tai Yai) Voice 106: Sinhala Voice 107: Sindarin Voice 108: Slovak Voice 109: Slovenian Voice 110: Lule Saami Voice 111: Albanian Voice 112: Serbian Voice 113: Swedish Voice 114: Swahili Voice 115: Tamil Voice 116: Telugu Voice 117: Thai Voice 118: Turkmen Voice 119: Setswana Voice 120: Turkish Voice 121: Tatar Voice 122: Uyghur Voice 123: Ukrainian Voice 124: Urdu Voice 125: Uzbek Voice 126: Vietnamese (Northern) Voice 127: Vietnamese (Central) Voice 128: Vietnamese (Southern) Voice 129: Chinese (Cantonese) Voice 130: Chinese (Cantonese, latin as Jyutping)

ENTER THE INDEX OF THE LANGUAGE YOU WANT TO USE IN LINE 17 OF THE CODE INSIDE "[]"





## Installation

1. Clone the repository:
   ```
   git clone https://github.com/TGvenomYT/Deepseek-Jarvis.git
   cd jarvis-assistant
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt

4. install PyAudio
```
   pip install PyAudio
   ```

4. Set up your environment variables 
   ```
   Line 35
   Authorization="your_deepseek_api_key"

   
   ```
