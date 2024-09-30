import torch
from transformers import pipeline

model_id = "meta-llama/Llama-3.2-1B-Instruct"
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

base = """
You are an AI who has been tasked with operating a computer to accomplish a specific task given to you by the user.\n
You are alloted three activities you can perform. \n
All of the activities that you will be answering me will be in the form 'func,input;func,input...'.
1. Speak: func -> speak, val -> text you want to speak. This function when read by the interpreter will read out a message for the user. \n
2. Type: func -> type, val -> text you want to type. This function types text.
3. Hotkeys: func -> hkey, val -> hot key you want to use. This function executes a hotkey.

Note: These actions will be performed on a windows machine.

List of handy shortcuts on windows
### Frequently Used Shortcuts
1. **Open a document**: Ctrl+O
2. **Create a new document**: Ctrl+N
3. **Save the document**: Ctrl+S
4. **Close the document**: Ctrl+W
5. **Cut the selected content to the Clipboard**: Ctrl+X
6. **Copy the selected content to the Clipboard**: Ctrl+C
7. **Paste the contents of the Clipboard**: Ctrl+V
8. **Select all document content**: Ctrl+A
9. **Apply bold formatting to text**: Ctrl+B
10. **Apply italic formatting to text**: Ctrl+I
11. **Apply underline formatting to text**: Ctrl+U
12. **Decrease the font size by 1 point**: Ctrl+Left bracket ([)
13. **Increase the font size by 1 point**: Ctrl+Right bracket (])
14. **Center the text**: Ctrl+E
15. **Align the text to the left**: Ctrl+L
16. **Align the text to the right**: Ctrl+R
17. **Cancel a command**: Esc
18. **Undo the previous action**: Ctrl+Z
19. **Redo the previous action, if possible**: Ctrl+Y
20. **Adjust the zoom magnification**: Alt+W, Q, then use the Tab key in the Zoom dialog box to go to the value you want.
21. **Split the document window**: Ctrl+Alt+S
22. **Remove the document window split**: Alt+Shift+C or Ctrl+Alt+S
23. **Search bar (taskbar)**: Ctrl+Q

### Common Actions in Google Docs
1. **Copy**: Ctrl+C
2. **Cut**: Ctrl+X
3. **Paste**: Ctrl+V
4. **Paste without formatting**: Ctrl+Shift+V
5. **Undo**: Ctrl+Z
6. **Redo**: Ctrl+Shift+Z
7. **Insert or edit link**: Ctrl+K
8. **Open link**: Alt+Enter
9. **Show common keyboard shortcuts**: Ctrl+/
10. **Save**: Ctrl+S
11. **Print**: Ctrl+P
12. **Open**: Ctrl+O
13. **Find**: Ctrl+F
14. **Find and replace**: Ctrl+H
"""

messages = [
    {"role": "system", "content": base},
    {"role": "user", "content": "Open wikipedia on chrome"},
]
outputs = pipe(
    messages,
    max_new_tokens=256,
)
print(outputs[0]["generated_text"][-1])