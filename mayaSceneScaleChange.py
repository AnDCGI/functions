'''
© 2020 AnD CGI This work is licensed under a
Creative Commons Attribution-ShareAlike 4.0 International License.

Maya One Click Scene Change
this Script Is Designed To Change Scene Scale Like For FX, Lighting Etc.
Designed To Work As A Shelf Button Inside Maya And Especially Made To Work
With Alembic Files.
By Default It Will Scale Everything Down To 0.1 In All Axis, User Can Later
Change The Scale At Any Point.

This Is A Headless Script So Doesn't Prints Anything To Maya Command Line As
Of Now
'''
import maya.cmds as cmds
import maya.mel as mel
# Selecting Everything Inside Scene Then Getting Transform Node
cmds.select(all=True, hierarchy=True)
selection = cmds.ls(selection=True)
transformNode = cmds.listRelatives(selection, p=True)
# Setting Inherit Transform On For Alembic Files If It Wasn't Already
# Skip This Step While Working With Regular Files
for obj in transformNode:
    cmds.setAttr(obj + ".inheritsTransform", 1)
# Selecting Everything Inside Scene Again
cmds.select(all=True)
selection = cmds.ls(selection=True)
# Creating Locator, Renaming & Making It Parent Of Everything Inside Scene
locator = cmds.spaceLocator()
cmds.parent(selection, locator)
cmds.select(locator)
cmds.rename(locator, 'sceneScale')
# Setting Scene Scale, Here Default Is 0.1
cmds.setAttr("sceneScale.scaleX", 0.1)
cmds.setAttr("sceneScale.scaleY", 0.1)
cmds.setAttr("sceneScale.scaleZ", 0.1)
# Some Beautification Of The Locator So It Stands Out
cmds.setAttr("sceneScale.useOutlinerColor", 1)
cmds.setAttr("sceneScale" + ".outlinerColor", 0, 1, 0)
cmds.setAttr("sceneScale.overrideEnabled", 1)
cmds.setAttr("sceneScale" + ".overrideColor", 13)
# Refreshing Outliner & Attribute Editor So That It Can Reflects The Change
mel.eval('AEdagNodeCommonRefreshOutliners()')
mel.eval('AttributeEditor;updateAE("sceneScale")')
