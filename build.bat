REM Description: Build the launcher

REM delete the old build
rmdir /s /q .\dist
REM create the new build
pyinstaller ./launch_exe.spec --noconfirm
REM copy repositories files
xcopy /s /y /i /h /k /e .\repositories .\dist\launch_exe\repositories
xcopy /s /y /i /h /k /e .\localizations .\dist\launch_exe\localizations
xcopy /s /y /i /h /k /e .\modules .\dist\launch_exe\modules
xcopy /s /y /i /h /k /e .\embeddings .\dist\launch_exe\embeddings
xcopy /s /y /i /h /k /e .\extensions .\dist\launch_exe\extensions
xcopy /s /y /i /h /k /e .\extensions-builtin .\dist\launch_exe\extensions-builtin
xcopy /s /y /i /h /k /e .\javascript .\dist\launch_exe\javascript
xcopy /y .\v1-inference.yaml .\dist\launch_exe\
xcopy /y .\script.js .\dist\launch_exe\
xcopy /s /y /i /h /k /e ".\models\Stable-diffusion\Put Stable Diffusion checkpoints here.txt" .\dist\launch_exe\models\Stable-diffusion\
REM zip the build
cd .\dist
7z a launch_exe.zip launch_exe