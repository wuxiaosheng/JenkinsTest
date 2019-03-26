import os
import shutil
import datetime

def copyAssest(rootPath, srcPath, dstPath):
	JSScriptPath = rootPath+"/../frameworks/cocos2d-x/cocos/scripting/js-bindings"
	if os.path.exists(dstPath+"src"):
		shutil.rmtree(dstPath+"src")
	if os.path.exists(dstPath+"res"):
		shutil.rmtree(dstPath+"res")
	if os.path.exists(dstPath+"script"):
		shutil.rmtree(dstPath+"script")
	if os.path.exists(dstPath+"main.js"):
		os.remove(dstPath+"main.js")
	if os.path.exists(dstPath+"project.json"):
		os.remove(dstPath+"project.json")
	shutil.copyfile(rootPath+"/../main.js", rootPath+"/../frameworks/runtime-src/proj.android-studio/app/assets/main.js")
	shutil.copyfile(rootPath+"/../project.json", rootPath+"/../frameworks/runtime-src/proj.android-studio/app/assets/project.json")
	shutil.copytree(JSScriptPath+"/script", rootPath+"/../frameworks/runtime-src/proj.android-studio/app/assets/script")
	shutil.copytree(rootPath+"/../src", rootPath+"/../frameworks/runtime-src/proj.android-studio/app/assets/src")
	#os.system("cocos.py jscompile -s "+srcPath+"src"+" -d "+dstPath+"src")
	print 'compile script complete'
	shutil.copytree(rootPath+"/../res", rootPath+"/../frameworks/runtime-src/proj.android-studio/app/assets/res")
	print 'assets copy complete'
	
def runGradle(rootPath):
	os.chdir(rootPath+"/../frameworks/runtime-src/proj.android-studio/")
	os.system("gradle aR")
	os.chdir(rootPath+"/../frameworks/runtime-src/proj.android-studio/app/build/outputs/apk/release/")
	print "package complete"
	
def createApk(srcPath):
	if not os.path.exists(srcPath+"apk"):
		os.mkdir(srcPath+"apk")
	files = os.listdir(srcPath+"apk")
	if len(files) >= 5:
		print 'remove old apk:'+files[0]
		os.remove(srcPath+"apk/"+files[0])
	nowTime=datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
	shutil.copy("./release.apk", srcPath+"apk/"+nowTime+".apk")
	print "create apk complete name:"+srcPath+"apk/"+nowTime+".apk"

if __name__ == "__main__":
	rootPath = os.getcwd()
	dstPath = rootPath+"/../frameworks/runtime-src/proj.android-studio/app/assets/"
	srcPath = rootPath+"/../"
	
	copyAssest(rootPath, srcPath, dstPath)
	
	runGradle(rootPath)
	
	createApk(srcPath)
	