@ECHO OFF
SETLOCAL
SET "sourcedir=D:\Sync\Teaching\Elasticity\Lectures\Chapter 4\"
PUSHD "%sourcedir%"
FOR /f "delims=" %%a IN (
 'dir /b /s /a-d *.tex'
 ) DO (
 IF NOT EXIST "%%~dpna.md" pandoc "%%a" -f latex --ascii -t markdown_github -o "%%~dpna.md"
 )
)
popd
GOTO :EOF
