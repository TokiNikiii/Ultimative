@echo off
@mode con cols=35 lines=5
title QF-HACKER

color c
echo DON'T CLOSE ME OR I'LL  DESTROY YOU

:check
for /F "usebackq" %%a in (./questionfile.qf) do set load=%%a

if %load% == MagmaticSancturay goto WOW
goto check

:WOW
start OPFER.gif
start OPFER.gif
start OPFER.gif
start OPFER.gif
start OPFER.gif
start OPFER.gif

start schlecht.pyw
start schlecht.pyw
start schlecht.pyw
start schlecht.pyw
start schlecht.pyw
start schlecht.pyw

pause>NUL