@echo off
setlocal
cd /d "%~dp0"
python --version >nul 2>&1
if errorlevel 1 (
  echo Python nao encontrado no PATH.
  exit /b 1
)
for %%A in (%*) do if /I "%%~A"=="--aplicar" goto dependencias
goto executar
:dependencias
python -c "from PIL import Image" >nul 2>&1
if errorlevel 1 (
  python -m pip install --user "Pillow==13.0.0"
  if errorlevel 1 exit /b 1
)
:executar
python "%~dp0scripts\importar_srd_local.py" %*
exit /b %errorlevel%
