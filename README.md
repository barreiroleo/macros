<!-- LTeX: language=en-US -->
<div align="center">
<h1>macros</h1
<h6>Running macros written in python scripts using xdotool</h6>
<h6>
🚧 I will not actively development this tool for now.<br>
Maybe you want checkout <a href="https://github.com/autokey/autokey">Autokey</a>
</h6>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![x11](https://img.shields.io/badge/--F28834?style=for-the-badge&logo=x.org&logoColor=ffffff)
</div>

# Table of Contents
- [Features](#features)
- [Macros in action](#macros-in-action)
    - [LTeX_extra.nvim](#ltex_extranvim)
- [To-do list](#to-do-list)

## Features

I write this tool for running and recording complex demos from terminal. At moment has capabilities for basic stuff like:
- Get active window
- Select window
- Send key pressing by sync way with custom delays.
- Logging stuff for tracking your scripts.
- Specific actions for resizing selected windows.
- Toggling recording for OBS (ctrl+r shortcut used).

The architecture isn't good structured for multiple purposes. I want refactoring for extensibility in a future, I don't have time now.

## Macros in action

### [LTeX_extra.nvim](https://github.com/barreiroleo/ltex_extra.nvim)

https://user-images.githubusercontent.com/48270301/177694689-b6b12b4a-3981-47fe-aa88-567697f797bd.mp4

https://user-images.githubusercontent.com/48270301/177694714-2f9d7477-26b6-4bf5-a47e-63ce2f82d76a.mp4

https://user-images.githubusercontent.com/48270301/177694724-736159ab-c202-4325-ad23-405c76676b79.mp4

https://user-images.githubusercontent.com/48270301/177694740-bc8bdb4c-0f6b-4f63-98af-54ec23196f27.mp4

## To-do list
- [ ] Write the docs.
