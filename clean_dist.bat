@echo off
pushd dist
for %%i in (*.tar.gz) do (
    del "%%i"
)
popd