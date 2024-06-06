bl_info = {
    "name:": "Remove_unused_material_slots",
    "catergory": "Object"
}

import bpy

# Define the custom operator
class OBJECT_OT_remove_unused_material_slots(bpy.types.Operator):
    bl_idname = "object.remove_unused_material_slots"
    bl_label = "Remove Unused Material Slots for Selected Objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for ob in context.selected_objects:
            # Check if the object has material slots
            if ob.material_slots:
                context.view_layer.objects.active = ob
                bpy.ops.object.material_slot_remove_unused()
        return {'FINISHED'}

# Add the operator to the Object > Clean Up menu
def menu_func(self, context):
    self.layout.operator(OBJECT_OT_remove_unused_material_slots.bl_idname)

# Register and unregister the operator and menu
def register():
    bpy.utils.register_class(OBJECT_OT_remove_unused_material_slots)
    bpy.types.VIEW3D_MT_object_cleanup.append(menu_func)

def unregister():
    bpy.types.VIEW3D_MT_object_cleanup.remove(menu_func)
    bpy.utils.unregister_class(OBJECT_OT_remove_unused_material_slots)

if __name__ == "__main__":
    register()
