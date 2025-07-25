@echo off
setlocal EnableDelayedExpansion

rem Set the dimensions of the donut
set "width=40"
set "height=20"

rem Initialize variables for the donut
set "A=0"
set "B=0"

:loop
cls
set "output="

rem Generate the donut
for /L %%j in (0,1,%height%) do (
    set "line="
    for /L %%i in (0,1,%width%) do (
        set "x=!A!"
        set "y=!B!"
        set /a "x=!x! + (sin(!A!) * cos(!B!)) * 10"
        set /a "y=!y! + (sin(!B!) * 10)"
        set "line=!line! "
        if %%i==!x! if %%j==!y! set "line=!line!o"
        set "line=!line! "
    )
    set "output=!output!!line!^
"
)

echo !output!
set /a "A+=1"
set /a "B+=1"
timeout /nobreak /t 1 >nul
goto loop