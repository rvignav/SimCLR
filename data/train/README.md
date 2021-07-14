To set up the `train` folder, run the following in the `data` directory:

    kaggle competitions download diabetic-retinopathy-detection -f train.zip.001
    kaggle competitions download diabetic-retinopathy-detection -f train.zip.002
    kaggle competitions download diabetic-retinopathy-detection -f train.zip.003
    kaggle competitions download diabetic-retinopathy-detection -f train.zip.004
    kaggle competitions download diabetic-retinopathy-detection -f train.zip.005
    unzip train*
    rm *.zip 
    cat train.zip.* > train.zip
    unzip train.zip
    rm train.zip* 
