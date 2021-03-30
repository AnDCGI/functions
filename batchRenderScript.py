# Copyright 2020 By Dhrubajyoti.S, AnD CGI
# All Rights Reserved.
# This Script Is Released Under The "GPL-3.0 License". Please See The License
# The Scripts Has "AnD CGI © 20XX" Symbol Which Is To Remind That Donations Or Credit Aren't Necessary But Very Appreciated
# How To Connect "https://github.com/AnDCGI"

# This Batch Render Script Designed To Work As A Shelf Button Inside Maya
# The Purpose Is To Work On As Many Shots/files As Possible In A Shift
# After One File/shot Is Done Click On The Shelf Button That Will Add It To An Auto Generated Batch File
# So At The End Of The Shift User/artist Can Just Run The Batch File & All Added Shots Will Be Rendered One After Another
# Some Requirements For This To Work Is As Expected Are
# 1. Make Sure All Render Settings Are There Including Render Camera
# 2. Frame Range Is Set Inside Maya Render Settings
# 3. Ideally The Render Folder Directory Should Exits Before Hand If Not That Need To Be Created First
# 4. This Will Work With Any Render Engines, Make Sure To Have A "mayabatch" License
# This Is A Headless Script So Doesn't Prints Anything To Maya Command Line As Of Now
import maya.cmds as cmds
import getpass
import os
import sys
insDir = sys.argv[0]
renDir = "\"" + str.replace(insDir, "maya", "Render") + "\""
# Where The Render Batch Script Will Be Generated
globalPath = "A:\\01prj\\XYZ\\prod\\assetbuildpub\\fx_assets\\batchRenderScript\\"
# Getting The Maya File Path, Since The Batch Script Expects "" Thus Adding Those
mayaFilePath = "\"" + cmds.file(query=True, sceneName=True) + "\""
# Windows Path Replacing "/" With "\", Skip If Not Required
mayaFilePath = mayaFilePath.replace("/", "\\")
# Removing Some Character From The String & Adding Render Folder Location
# This Step Is Custom, Depends On How The Project Is Set
rndrFilePath = mayaFilePath[:44] + "/fx_renderLayers/v000\""
# Windows Path Replacing "/" With "\", Skip If Not Required
rndrFilePath = rndrFilePath.replace("/", "\\")
# Getting User Name, Uppercase All Letters & Keeping Only First And Last Character
userName = getpass.getuser()
userName = userName.upper()
userName = userName[0:1] + userName[-1:]
# The Batch File Will Have A Different Name Everyday, Thus Getting Date & Adding User Name With It
# Can Skip "cmds.date" Thing & Use Python To Get Date, This Will Make It Work Independently
fileName = cmds.date(format="DD•MM•YYYY" + "_" + userName)
# Generating Batch File Also Appending Lines
fileHandle = open(globalPath + fileName + ".bat", "a+")
# Adding Lines One After Another, Thats How Maya Accepts The Batch File
fileHandle.write(renDir + " -r file -rd " + rndrFilePath + " " + mayaFilePath)
fileHandle.write("\n")
fileHandle.close()
