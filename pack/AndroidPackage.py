import os
import shutil
import datetime

if __name__ == "__main__":
	rootPath = os.getcwd()
	dstPath = rootPath+"/../frameworks/runtime-src/proj.android-studio/app/assets/"
	srcPath = rootPath+"/../"
	if os.path.exists(dstPath+"src"):
		shutil.rmtree(dstPath+"src")
	if os.path.exists(dstPath+"res"):
		shutil.rmtree(dstPath+"res")
	shutil.copytree(rootPath+"/../src", rootPath+"/../frameworks/runtime-src/proj.android-studio/app/assets/src")
	shutil.copytree(rootPath+"/../res", rootPath+"/../frameworks/runtime-src/proj.android-studio/app/assets/res")
	print 'assets copy complete'
	
	os.chdir(rootPath+"/../frameworks/runtime-src/proj.android-studio/")
	os.system("gradle aR")
	os.chdir(rootPath+"/../frameworks/runtime-src/proj.android-studio/app/build/outputs/apk/release/")
	print "package complete"
	
	if not os.path.exists(srcPath+"apk"):
		os.mkdir(srcPath+"apk")
	files = os.listdir(srcPath+"apk")
	if len(files) >= 5:
		print 'remove old apk:'+files[0]
		os.remove(srcPath+"apk/"+files[0])
	nowTime=datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
	shutil.copy("./release.apk", srcPath+"apk/"+nowTime+".apk")
	
	print "copy apk complete"
	