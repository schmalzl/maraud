# maraud
*"In theory, theory and practice are the same. In practice, they’re not."* - **[Yoggi Berra](https://en.wikipedia.org/wiki/Yogi_Berra)**

----

[![Python - 3.13.7](https://img.shields.io/badge/Python-3.13.7-315C91?style=for-the-badge)](https://www.python.org/downloads/)
[![License - MIT](https://img.shields.io/badge/License-MIT-D1682C?style=for-the-badge)](https://choosealicense.com/licenses/mit/)
![Open Source](https://img.shields.io/badge/Open_Source-23A15C?style=for-the-badge)

<sub> This project is being actively updated and support/feedback from the community is much appreciated. You can share your issues and ideas in the maraud [Issue Tracker](https://github.com/schmalzl/maraud/issues).<br>You can also check out my youtube channel where i share the journey of marauds development.</sub>

### The Pitch
maraud is a free, open-source, and highly customizable command line tool for downloading songs in bulk from SoundCloud and YouTube. It is optimized for speed, efficiency, and controlled workflows, allowing users to queue, manage, and fetch large collections of music with minimal friction.

maraud is designed to enable fast, automated iterations of downloading while empowering power-users to create tailored workflows. It favors simplicity, customization, and performance over unnecessary complexity. Unlike higher-level GUI-based downloaders, maraud is laser-focused on being scriptable, extensible, and predictable. Features such as graphical frontends, auto-recommendations, or heavy external integrations are intentionally excluded to keep the tool lean and maintainable.

- Minimize setup and maintenance overhead
- Provide consistent, predictable results
- Simple interface with high customizability through configuration files
- Optimized for bulk operations and efficient downloads
- Portable, lightweight, and dependency-minimized
- Easy to hack, extend, and integrate into custom workflows
- Built for performance and tested against real-world bulk usage

### Installation
maraud is based on a cli-interface and intended for primary usage in the operating system terminal. This installation guide will focus on installing maraud to the Windows command-prompt and Mac terminal.
<br> If you want to include this program as an internal api in your own program, you can read the installation guide in the official maraud documentation.
<br>
maraud is just a single executable that is completly standalone and needs minimal dependencies. You can find the newest release build but also legacy versions in the GitHub Release section.
1. Download maraud in your desired configuration depending on your architecture and operating system and place the file somewhere on your drive.
> You now need to export the application path to your system environment variables. This depends on the operating system you are using.
2. On Windows, you can add the application path to the `PATH` environment variables using **Environment Variables**. If you are using a Mac, you can use this command to add maraud to the environment variables. On a Mac, depending on where you put the executable, there is a different way of adding it to the PATH variales. This can be done by creating a symlink to the maraud executable.
```
chmod +x ~/Desktop/maraud
sudo ln -s ~/Desktop/maraud /usr/local/bin/maraud
```
To verify that maraud is globally accessable by the terminal, type:
```
maraud --version
```

### Quick Start Guide
### Documentation
### How it works
### Cross-Platform Support
### Releases & Changelogs
### Gallery
### Demo
### Credits
### License