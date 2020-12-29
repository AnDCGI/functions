# Coding=utf-8
# Imports Libraries
import maya.cmds as cmds
import maya.mel as mel
# Declares Varibale
winID_A = 'Set Desired FPS'
# Check To See If Window Exists
if cmds.window(winID_A, exists=True):
    cmds.deleteUI(winID_A)
# Defines Set Button Action   
def SetButtonPush(*args):
    currentValue = cmds.optionMenu('Select_FPS', query=True, value=True)
    if currentValue == 'Game 15 FPS':
        mel.eval('currentUnit -time game')
        mel.eval('playbackOptions -ps 0')
        mel.eval('playbackOptions -e -ast 101 -min 101 -max 500 -aet 500')
        mel.eval('playButtonStart')
    elif currentValue == 'Film 24 FPS':
        mel.eval('currentUnit -time film')
        mel.eval('playbackOptions -ps 0')
        mel.eval('playbackOptions -e -ast 101 -min 101 -max 500 -aet 500')
        mel.eval('playButtonStart')
    elif currentValue == 'PAL/SECAM 25 FPS':
        mel.eval('currentUnit -time pal')
        mel.eval('playbackOptions -ps 0')
        mel.eval('playbackOptions -e -ast 101 -min 101 -max 500 -aet 500')
        mel.eval('playButtonStart')
    elif currentValue == 'NTSC 30 FPS':
        mel.eval('currentUnit -time ntsc')
        mel.eval('playbackOptions -ps 0')
        mel.eval('playbackOptions -e -ast 101 -min 101 -max 500 -aet 500')
        mel.eval('playButtonStart')
    elif currentValue == 'Show 48 FPS':
        mel.eval('currentUnit -time show')
        mel.eval('playbackOptions -ps 0')
        mel.eval('playbackOptions -e -ast 101 -min 101 -max 500 -aet 500')
        mel.eval('playButtonStart')
    elif currentValue == 'PAL F 50 FPS':
        mel.eval('currentUnit -time palf')
        mel.eval('playbackOptions -ps 0')
        mel.eval('playbackOptions -e -ast 101 -min 101 -max 500 -aet 500')
        mel.eval('playButtonStart')
    elif currentValue == 'NTSC F 60 FPS':
        mel.eval('currentUnit -time ntscf')
        mel.eval('playbackOptions -ps 0')
        mel.eval('playbackOptions -e -ast 101 -min 101 -max 500 -aet 500')
        mel.eval('playButtonStart')
# Defines Done Button Action
def DoneButtonPush(*args):
    cmds.deleteUI( window, window=True )
# Creates Actual Window
window = cmds.window('winID_A', title='Maya FPS Change', resizeToFitChildren=False, sizeable=False)
# Creates Layout
cmds.frameLayout(label='Broadcast FPS Options', collapsable=False, mw=5, mh=5)
cmds.text(label='AnD CGI © 2020', font='smallPlainLabelFont')
cmds.columnLayout()
cmds.optionMenu('Select_FPS', label='Select FPS')
cmds.menuItem(label=" ")
cmds.menuItem(label='Game 15 FPS')
cmds.menuItem(label='Film 24 FPS')
cmds.menuItem(label='PAL/SECAM 25 FPS')
cmds.menuItem(label='NTSC 30 FPS')
cmds.menuItem(label='Show 48 FPS')
cmds.menuItem(label='PAL F 50 FPS')
cmds.menuItem(label='NTSC F 60 FPS')
# Creates Buttons
cmds.rowLayout(numberOfColumns=2, columnWidth2=(80,80),columnAttach=[(1, 'both', 0), (2, 'both', 0)])
cmds.button(label='Set', command=SetButtonPush)
cmds.button(label='Done', command=DoneButtonPush)
# Shows Window
cmds.showWindow()