# Clean Unknown Plugins
# © 2020 AnD CGI This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
# This Script Will Delete Any Unknown Plugins From Maya Scene
# The List of Deleted Plugins Can Be Seen On Maya Script Editor
import maya.cmds as cmds
cmds.delete(cmds.ls(type="unknown"))
plg_ls = cmds.unknownPlugin(q=True, l=True)
if plg_ls:
    for plugin in plg_ls:
        print(plugin)
        cmds.unknownPlugin(plugin, r=True)
#Use The Bottom Line Only If You Have "_UNKNOWN_REF_NODE_"
cmds.delete("_UNKNOWN_REF_NODE_")
