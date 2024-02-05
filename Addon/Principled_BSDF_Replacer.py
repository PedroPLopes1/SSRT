bl_info = {
    "name": "Principled BSDF SSRT Replacer",
    "author": "Gabriel.Saretti",
    "version": (1, 9),
    "blender": (4, 0, 2),
    "location": "View3D > Sidebar > Principled BSDF SSRT Replacer",
    "description": "Replaces all Principled BSDF nodes by Principled BSDF SSRT nodes",
    "warning": "",
    "doc_url": "",
    "category": "Material",
}

import bpy

def replace_nodes (materials):
    
    bpy.context.scene.eevee.ssr_quality = 1
    bpy.context.scene.eevee.ssr_max_roughness = 1
    
    for mat in materials:
        if mat.node_tree:
            nodes = mat.node_tree.nodes
            principled_nodes = [node for node in nodes if node.type == "BSDF_PRINCIPLED"]
            for principled_node in principled_nodes:
                new_node = nodes.new ("ShaderNodeGroup")
                new_node.node_tree = bpy.data.node_groups ["Principled BSDF SSRT"]
                new_node.location = principled_node.location
                new_node.width = principled_node.width
                new_node.height = principled_node.height
                new_node.label = principled_node.label
                new_node.mute = principled_node.mute
                new_node.hide = principled_node.hide

                for input in principled_node.inputs:
                    if input.name in new_node.inputs:
                        new_node.inputs[input.name].default_value = input.default_value

                links = mat.node_tree.links
                for input in principled_node.inputs:
                    for link in input.links:
                        links.new (link.from_socket, new_node.inputs [input.name])
                for output in principled_node.outputs:
                    for link in output.links:
                        links.new (new_node.outputs ["BSDF SSRT"], link.to_socket)

                nodes.remove (principled_node)

class PRINCIPLED_BSDF_SSRT_OT_replace_nodes_selected (bpy.types.Operator):
    bl_idname = "principled_bsdf_ssrt.replace_nodes_selected"
    bl_label = "Replace Nodes in Selected Objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        selected_objects = bpy.context.selected_objects
        selected_materials = []
        for obj in selected_objects:
            for slot in obj.material_slots:
                if slot.material not in selected_materials:
                    selected_materials.append(slot.material)

        replace_nodes(selected_materials)
        return {'FINISHED'}

class PRINCIPLED_BSDF_SSRT_OT_replace_nodes_scene (bpy.types.Operator):
    bl_idname = "principled_bsdf_ssrt.replace_nodes_scene"
    bl_label = "Replace Nodes in Entire Scene"
    bl_options = {'REGISTER', 'UNDO'}

    def execute (self, context):
        scene_objects = bpy.context.scene.objects
        scene_materials = []
        for obj in scene_objects:
            for slot in obj.material_slots:
                if slot.material not in scene_materials:
                    scene_materials.append(slot.material)
                
        replace_nodes (scene_materials)
        return {'FINISHED'}

class PRINCIPLED_BSDF_SSRT_PT_panel (bpy.types.Panel):
    bl_label = "Principled BSDF SSRT Replacer"
    bl_idname = "PRINCIPLED_BSDF_SSRT_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Principled BSDF SSRT Replacer"

    def draw (self, context):
        layout = self.layout

        row = layout.row ()
        row.operator ("principled_bsdf_ssrt.replace_nodes_selected")

        row = layout.row ()
        row.operator ("principled_bsdf_ssrt.replace_nodes_scene")

def register ():
    bpy.utils.register_class (PRINCIPLED_BSDF_SSRT_PT_panel)
    bpy.utils.register_class (PRINCIPLED_BSDF_SSRT_OT_replace_nodes_selected)
    bpy.utils.register_class (PRINCIPLED_BSDF_SSRT_OT_replace_nodes_scene)

def unregister ():
    bpy.utils.unregister_class (PRINCIPLED_BSDF_SSRT_PT_panel)
    bpy.utils.unregister_class (PRINCIPLED_BSDF_SSRT_OT_replace_nodes_selected)
    bpy.utils.unregister_class (PRINCIPLED_BSDF_SSRT_OT_replace_nodes_scene)

if __name__ == "__main__":
    register ()
