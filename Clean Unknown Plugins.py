# Clean Unknown Plugins
# Copyright ©  2020  AnD CGI
# This Script Will Delete Any Unknown Plugins From Maya Scene
# The List of Deleted Plugins Can Be Seen On Maya Script Editor
import maya.cmds as cmds
cmds.delete(cmds.ls(type="unknown"))
plg_ls = cmds.unknownPlugin(q=True, l=True)
if plg_ls:
    for plugin in plg_ls:
        print(plugin)
        cmds.unknownPlugin(plugin, r=True)