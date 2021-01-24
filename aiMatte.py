import maya.cmds as cmds
sel = cmds.ls(ni=1, typ=["mesh", "nurbsSurface", "subdiv"])
num = len(sel)
for i in range(0,num):
	selAttr = sel[i] + ".aiMatte"
	cmds.setAttr(selAttr, 1)