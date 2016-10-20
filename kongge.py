import os

def rename():
    path=r"F:\laopo\1"
    filelist=os.listdir(path)
    for files in filelist:
        Olddir=os.path.join(path,files);
        if os.path.isdir(Olddir):
            continue;
        filename=os.path.splitext(files)[0];
        newfilename = filename.strip()
        filetype=os.path.splitext(files)[1];
        Newdir=os.path.join(path,newfilename+filetype);
        os.rename(Olddir,Newdir);

rename();
