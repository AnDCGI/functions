'''
© 2020 AnD CGI This work is licensed under a
Creative Commons Attribution-ShareAlike 4.0 International License.

Dynamics Quick Selection Set

This Dynamics Quick Selection Set Script Designed To Work As A Shelf Button
Inside Maya Which Will Open A New Pop Up UI With All The Presets
The Tool Changes The FPS Based On Selected Preset
Althogh Kind Of A Similar Option Is Avilavle Inside Maya But The Timeline And
Timeslider Goes Into Float Values, This Fixes That Also Sets The Start & End
As 101 - 500 Respectively
Which Can Be Changed By Changing The Values Inside The Code

DISCLAIMER This Doesnt Changes Any Keyframe Nor Converts FPS, It Just Sets
FPS, Meant To Be Used On A Empty Scene
'''
# Coding = utf-8
# Imports Libraries
import maya.cmds as cmds
import maya.mel as mel
# Declares Varibale
winID = 'SetDesiredFPS'
# Check To See If Window Exists
if cmds.window(winID, exists=True):
    cmds.deleteUI(winID)


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


# Creates Actual Window
window = cmds.window(winID, title='Maya FPS Switch',
                     resizeToFitChildren=True, sizeable=False, tlb=True)
# Creates Layout
cmds.frameLayout(label='Broadcast FPS Options', collapsable=False, mw=5, mh=5)
cmds.text(label='© 2020 AnD CGI (CC BY-SA 4.0)', font='smallPlainLabelFont')
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
cmds.setParent('..')
# Creates Buttons
cmds.rowLayout(numberOfColumns=2)
cmds.text(label='', width=46)
cmds.button(label='Set', command=SetButtonPush, w=100)
cmds.setParent('..')
# Shows Window
cmds.showWindow()
