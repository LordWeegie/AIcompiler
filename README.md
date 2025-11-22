# AIcompiler
AIcompiler is a tool that lets you write pseudocode and automatically converts it into standard C code. Although the tool generates your C code, you will still need to have GCC installed to compile it yourself. Follow the steps below to get started!

## Getting Started
Prerequisites
Install Python (version 3.x recommended).

Install GCC (GNU Compiler Collection) to compile your C code.

Install Git if you want to clone the repository using the terminal.

## Installation and Setup
Clone the repository by running the following command in your terminal:
`git clone https://github.com/LordWeegie/AIcompiler.git`
Navigate into the cloned repository:
`cd AIcompiler`

Open the Python script (main.py) in your preferred text editor.

Locate the highlighted section shown in Figure 1.1 within main.py, and replace the placeholder with your Deepseek API key. If you are using a different API, you will need to update the URL accordingly. This guide covers only the Deepseek API configuration.

Create the input and output files as shown in Figure 1.2. You can name these files anything you want, but ensure they have the correct extensions (e.g., .txt for input pseudocode and .c for the output C code).

Run the Python script:

On Windows, run:
`python main.py`
On Unix-based systems (Linux, macOS), run:
`python3 main.py`

When prompted (see Figure 1.3), enter the names of your input pseudocode file and your desired output C file.

That's it! Your pseudocode will be converted into C code, ready for you to compile and run. Thank you for using AIcompiler!

# Visual References
Figure 1.1: API Key Configuration
<img src="https://github.com/user-attachments/assets/04394fe7-5548-41ca-a2fd-979e8270fdfe" alt="step1" style="max-width:500px; width:100%;" />
Figure 1.2: Required Files Setup
<img src="https://github.com/user-attachments/assets/cf453c2c-2dc4-4aa1-9cff-fe54fc6c28f7" alt="step2" style="max-width:300px; width:100%;" />
Figure 1.3: Running the Script
<img src="https://github.com/user-attachments/assets/986edfba-88c0-4a5e-b01a-3c305825faf6" alt="step3" style="max-width:520px; width:100%;" />
