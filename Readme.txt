I don't like change the system. This creates a lot of problems for me. I created a batch file:

@ECHO OFF
REM change CHCP to UTF-8
CHCP 65001
CLS
I saved at C:\Windows\System32 as switch.bat.

I created a link for cmd.exe on the Desktop. 

In the properties of cmd, changed the destination to: C:\Windows\System32\cmd.exe /k switch

Voilá, when I need to type in UTF-8, I use this link.