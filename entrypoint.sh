#!/bash/sh

if [[  sc == 'failure' ]]
then
    echo "[FAILURE] Can't load model"
    exit 1
else
    echo "[SUCCESS] Model loaded"
fi