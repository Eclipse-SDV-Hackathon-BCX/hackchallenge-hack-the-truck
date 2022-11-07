@echo off

pushd %~dp0

if not exist "_build" mkdir "_build"

set "CMAKE_PREFIX_PATH=C:/Qt/5.15.2/msvc2015_64"

pushd "%~dp0\_build"

cmake .. -A x64

popd

popd

pause