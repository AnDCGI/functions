# Dynamics Quick Selection Set
# Copyright ©  2020  AnD CGI
# This Tool Collects Different Types of Objects* by Searching the Whole Scene
# User Have to Choose the Type of Object, Click Create & the Tool Will Create A Quick Selection Set
# Every Quick Selection Set Will Have a QSS Suffix 
# *Drop Down Options are Related to FX Only
# Coding = utf-8

# Imports Libraries
import maya.cmds as cmds
# Declares Variable
winID_A = 'QSS Create'
# Check To See If Window Exists
if cmds.window(winID_A, exists=True):
    cmds.deleteUI(winID_A)
# Defines Create Button Action   
def CreateButtonPush(*args):
    currentValue = cmds.optionMenu('Object_Type', query=True, value=True)
    if currentValue == 'Fluid Emitter':
        set = cmds.ls(type='fluidEmitter')
        if bool(set):
            cmds.select(set)    
            action = cmds.sets(name = 'fluidEmitterQSS', text = 'gCharacterSet')
            print('Created Quick Selection Set with all Fluid Emitters')
        else:
            print('No Fluid Emitter in Scene')
    elif currentValue == 'nParticle/Particle Emitter':
        set=cmds.ls(exactType='pointEmitter')
        if bool(set):
            cmds.select(set)    
            action = cmds.sets(name = 'particleEmitterQSS', text = 'gCharacterSet')
            print('Created Quick Selection Set with all Particle Emitters')
        else:
            print('No Particle Emitter in Scene')
    elif currentValue == 'nRigid':
        set = cmds.ls(type='nRigid')
        if bool(set):
            cmds.select(set)    
            action = cmds.sets(name = 'nRigidQSS', text = 'gCharacterSet')
            print('Created Quick Selection Set with all nRigids')
        else:
            print('No nRigid in Scene')
    elif currentValue == 'Fluid Container':
        set = cmds.ls(type='fluidShape')
        if bool(set):
            cmds.select(set)    
            action = cmds.sets(name = 'fluidShapeQSS', text = 'gCharacterSet')
            print('Created Quick Selection Set with all Fluid Containers')
        else:
            print('No Fluid Container in Scene')
    elif currentValue == 'Nucleus':
        set = cmds.ls(type='nucleus')
        if bool(set):
            cmds.select(set)    
            action = cmds.sets(name = 'nucleusQSS', text = 'gCharacterSet')
            print('Created Quick Selection Set with all Nucleus')
        else:
            print('No Nucleus in Scene')
    elif currentValue == 'nParticle':
        set = cmds.ls(type='nParticle')
        if bool(set):
            cmds.select(set)    
            action = cmds.sets(name = 'nParticleQSS', text = 'gCharacterSet')
            print('Created Quick Selection Set with all nParticles')
        else:
            print('No nParticle in Scene')
    elif currentValue == 'Force Field':
        set = cmds.ls(type='field')
        if bool(set):
            cmds.select(set)    
            action = cmds.sets(name = 'forceFieldQSS', text = 'gCharacterSet')
            print('Created Quick Selection Set with all Force Fields')
        else:
            print('No Force Field in Scene')
    elif currentValue == 'Legacy Particle':
        set=cmds.ls(exactType='particle')
        if bool(set):
            cmds.select(set)    
            action = cmds.sets(name = 'ParticleQSS', text = 'gCharacterSet')
            print('Created Quick Selection Set with all Particles')
        else:
            print('No Particle in Scene')
    elif currentValue == 'nCloth':
        set=cmds.ls(exactType='nCloth')
        if bool(set):
            cmds.select(set)    
            action = cmds.sets(name = 'nClothQSS', text = 'gCharacterSet')
            print('Created Quick Selection Set with all nClothes')
        else:
            print('No nCloth in Scene')
    elif currentValue == 'Dynamic Constraint':
        set=cmds.ls(exactType='dynamicConstraint')
        if bool(set):
            cmds.select(set)    
            action = cmds.sets(name = 'dynamicConstraintQSS', text = 'gCharacterSet')
            print('Created Quick Selection Set with all Dynamic Constraints')
        else:
            print('No Dynamic Constraint in Scene')
    elif currentValue == 'Rigid Body':
        set=cmds.ls(exactType='rigidBody')
        if bool(set):
            cmds.select(set)    
            action = cmds.sets(name = 'rigidBodyQSS', text = 'gCharacterSet')
            print('Created Quick Selection Set with all Rigid Bodies')
        else:
            print('No Rigid Body in Scene')
    elif currentValue == 'Rigid Constraint':
        set=cmds.ls(exactType='rigidConstraint')
        if bool(set):
            cmds.select(set)    
            action = cmds.sets(name = 'rigidConstraintQSS', text = 'gCharacterSet')
            print('Created Quick Selection Set with all Rigid Constraints')
        else:
            print('No Rigid Constraint in Scene')
    elif currentValue == 'Anim Constraint':
        set=cmds.ls(type='constraint')
        if bool(set):
            cmds.select(set)    
            action = cmds.sets(name = 'constraintQSS', text = 'gCharacterSet')
            print('Created Quick Selection Set with all Anim Constraints')
        else:
            print('No Anim Constraint in Scene')
    elif currentValue == 'Rigid Body':
        set=cmds.ls(type='rigidBody')
        if bool(set):
            cmds.select(set)    
            action = cmds.sets(name = 'rigidBodyQSS', text = 'gCharacterSet')
            print('Created Quick Selection Set with all Rigid bodies')
        else:
            print('No Rigid Body in Scene')
# Defines Done Button Action
def DoneButtonPush(*args):
    cmds.deleteUI( window, window=True )
# Creates Actual Window
window = cmds.window('winID_A',title='FX Quick Set', resizeToFitChildren=True, sizeable=False)
# Creates Layout
cmds.frameLayout(label='Dynamics Quick Selection Set Options', collapsable=False, mw=5, mh=5)
cmds.text(label='AnD CGI © 2020', font='smallPlainLabelFont')
cmds.columnLayout()
cmds.optionMenu('Object_Type', label='Object Type')
cmds.menuItem(label=' ')
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
# Creates Buttons
cmds.rowLayout(numberOfColumns=2, columnWidth2=(117,117),columnAttach=[(1, 'both', 0), (2, 'both', 0)])
cmds.button(label='Create', command=CreateButtonPush)
cmds.button(label='Done', command=DoneButtonPush)
# Shows Window
cmds.showWindow()