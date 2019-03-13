import os
import shutil

if __name__ == "__main__":
	rootPath = os.getcwd()
	os.chdir(rootPath+"/../frameworks/runtime-src/proj.android-studio/")
	p=os.popen("gradle aR")
	print p.read()
	