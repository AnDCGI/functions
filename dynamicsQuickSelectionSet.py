#Coding=utf-8
#Imports Libraries
import maya.cmds as cmds
import maya.mel as mel
#Declares Varibale
winID_Q = 'QSS Create'
#Check To See If Window Exists
if cmds.window(winID_Q, exists=True):
    cmds.deleteUI(winID_Q)
#Defines Create Button Action   
def CreateButtonPush(*args):
    currentValue = cmds.optionMenu('Object_Type', query=True, value=True)
    if currentValue == 'Fluid Emitter':
        set = cmds.ls(type="fluidEmitter")
        cmds.select(set)
        action = cmds.sets(name = "fluidEmitterQSS", text = "gCharacterSet")
        print("Created QSS with all Fluid Emitters")
    elif currentValue == 'nParticle/Particle Emitter':
        set=cmds.ls(exactType="pointEmitter")
        cmds.select(set)
        action = cmds.sets(name = "particleEmitterQSS", text = "gCharacterSet")
        print("Created QSS with all particle emitter")
    elif currentValue == 'nRigid':
        set = cmds.ls(type="nRigid")
        cmds.select(set)
        action = cmds.sets(name = "nRigidQSS", text = "gCharacterSet")
        print("Created QSS with all nRigids")
    elif currentValue == 'Fluid Container':
        set = cmds.ls(type="fluidShape")
        cmds.select(set)
        action = cmds.sets(name = "fluidShapeQSS", text = "gCharacterSet")
        print("Created QSS with all Fluid Shapes")
    elif currentValue == 'Nucleus':
        set = cmds.ls(type="nucleus")
        cmds.select(set)
        action = cmds.sets(name = "nucleusQSS", text = "gCharacterSet")
        print("Created QSS with all nuclei")
    elif currentValue == 'nParticle':
        set = cmds.ls(type="nParticle")
        cmds.select(set)
        action = cmds.sets(name = "nParticleQSS", text = "gCharacterSet")
        print("Created QSS with all nParticles")
    elif currentValue == 'Force Field':
        set = cmds.ls(type="field")
        cmds.select(set)
        action = cmds.sets(name = "forceFieldQSS", text = "gCharacterSet")
        print("Created QSS with all force fields")
    elif currentValue == 'Legacy Particle':
        set=cmds.ls(exactType="particle")
        cmds.select(set)
        action = cmds.sets(name = "ParticleQSS", text = "gCharacterSet")
        print("Created QSS with all Particles")
    elif currentValue == 'nCloth':
        set=cmds.ls(exactType="nCloth")
        cmds.select(set)
        action = cmds.sets(name = "nClothQSS", text = "gCharacterSet")
        print("Created QSS with all nClothes")
    elif currentValue == 'Dynamic Constraint':
        set=cmds.ls(exactType="dynamicConstraint")
        cmds.select(set)
        action = cmds.sets(name = "dynamicConstraintQSS", text = "gCharacterSet")
        print("Created QSS with all dynamic constraints")
    elif currentValue == 'Rigid Body':
        set=cmds.ls(exactType="rigidBody")
        cmds.select(set)
        action = cmds.sets(name = "rigidBodyQSS", text = "gCharacterSet")
        print("Created QSS with all rigid bodys")
    elif currentValue == 'Rigid Constraint':
        set=cmds.ls(exactType="rigidConstraint")
        cmds.select(set)
        action = cmds.sets(name = "rigidConstraintQSS", text = "gCharacterSet")
        print("Created QSS with all rigid constraints")
    elif currentValue == 'Anim Constraint':
        set=cmds.ls(type="constraint")
        cmds.select(set)
        action = cmds.sets(name = "constraintQSS", text = "gCharacterSet")
        print("Created QSS with all anim constraints")
    elif currentValue == 'Rigid Body':
        set=cmds.ls(type="rigidBody")
        cmds.select(set)
        action = cmds.sets(name = "rigidBodyQSS", text = "gCharacterSet")
        print("Created QSS with all rigid bodies")
#Defines Done Button Action
def DoneButtonPush(*args):
    cmds.deleteUI( window, window=True )
#Creates Actual Window
window = cmds.window('winID_K',title='Quick Selection Set', resizeToFitChildren=True, sizeable=False)
#Creates Layout
cmds.frameLayout(label='Quick Selection Set Options', collapsable=False, mw=5, mh=5)
cmds.text(label='AnD CGI © 2020', font='smallPlainLabelFont')
cmds.columnLayout()
cmds.optionMenu('Object_Type', label='Object Type')
cmds.menuItem(label=" ")
cmds.menuItem(label='Fluid Emitter')
cmds.menuItem(label='nParticle/Particle Emitter')
cmds.menuItem(label='Fluid Container')
cmds.menuItem(label='nRigid')
cmds.menuItem(label='nCloth')
cmds.menuItem(label='nParticle')
cmds.menuItem(label='Rigid Body')
cmds.menuItem(label='Legacy Particle')
cmds.menuItem(label='Dynamic Constraint')
cmds.menuItem(label='Rigid Constraint')
cmds.menuItem(label='Anim Constraint')
cmds.menuItem(label='Force Field')
cmds.menuItem(label='Nucleus')
#Creates Gaps
cmds.rowColumnLayout(numberOfRows=1, rowHeight=(1, 50))
#Creates Buttons
cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 70), (2, 70)], cs=[(1, 40), (2, 15)])
cmds.button(label='Create', command=CreateButtonPush)
cmds.button(label='Done', command=DoneButtonPush)
#Shows Window
cmds.showWindow()
