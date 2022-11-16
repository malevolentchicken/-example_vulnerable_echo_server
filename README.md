# -example_vulnerable_echo_server

Note: Very old but may still be of some use. Extremely simple example for win32 buffer overflows.

Install and update. Drop overflow folder onto machine. Just execute server.exe with a cmd prompt. Binds to port 69. cygwin1.dll must reside in same folder as server.exe. Used to load jmp esps into address space.

overflow_step_by_step.py is the answer file for exploiting server.exe. Kind of messy but you'll get the idea.
