# Clean Unknown Plugins
import maya.cmds as cmds
cmds.delete(cmds.ls(type="unknown"))
plg_ls = cmds.unknownPlugin(q=True, l=True)
if plg_ls:
    for plugin in plg_ls:
        print(plugin)
        cmds.unknownPlugin(plugin, r=True)