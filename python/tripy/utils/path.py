import os
import shutil
import math

class Path (object):

    def __init__(self, path):
        self._pathStr = path

    def basename(self):
        return os.path.basename(self._pathStr)

    def dirname(self):
        return Path( os.path.dirname(self._pathStr) )
    
    def ext(self):
        if self.isDir():
            raise ValueError("Cannot get extension.  %s is not a file" % self._pathStr)
        return self._pathStr.split(".")[-1]
    
    def changeExt(self, ext):
        if self.isDir():
            raise ValueError("Cannot change extension.  %s is not a file" % self._pathStr)
        toks = self._pathStr.split(".")
        toks[-1] = ext
        self._pathStr = ".".join(toks)

    def copy(self, dest):
        shutil.copy(self._pathStr, dest)
        return Path(dest)

    def move(self, dest):
        shutil.move(self._pathStr, dest)
        return Path(dest)

    def exists(self):
        return os.path.exists(self._pathStr)

    def abspath(self):
        return Path(os.path.abspath(self._pathStr))

    def relpath(self, to=None):
        return Path(os.path.relpath(self._pathStr, to))

    def isDir(self):
        return os.path.isdir(self._pathStr)

    def chown(self, uid=-1, gid=-1):
        return os.chown(self._pathStr, uid, gid)

    def link(self, path):
        return os.link(self._pathStr, path)

    def listdir(self):
        if self.isdir():
            return os.listdir(self._pathStr)
        else:
            raise ValueError("Cannot list directory.  %s is not a directory" % self._pathStr)

    def mkdirs(self, mode=0777):
        os.makedirs(self._pathStr, mode)

    def openFile(self, *args):
        return open(self._pathStr, *args)
    
    def hashStr(self):
        return "hash%d" % math.fabs(hash(self._pathStr))

    def remove(self):
        os.remove(self._pathStr)

    def rmdir(self):
        os.rmdir(self._pathStr)

    def removedirs(self):
        os.removedirs(self._pathStr)

    def rename(self, dest, selfRename=False):
        os.rename(self._pathStr, dest)

        return Path(dest)

    def stat(self):
        return os.stat(self._pathStr)

    def __str__(self):
        return self._pathStr

    def __div__(self, path):
        return Path( os.path.join(self._pathStr, str(path)) )

