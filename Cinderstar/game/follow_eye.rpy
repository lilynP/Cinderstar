# Default eyes movment parameters
init -10 python:
  eye_center = {"x": 910, "y": 550}
  eye_radius_scale = {"x": 1.0, "y": 0.55} # moving at elipse
  eye_radius = 150 # maximum distance from center
  eye_smooth = 0.35 # 1.0 is no smoothing, 0.0 is infinite smoothing
  falloff_index = 3.0 # 1.0 is no falloff, higher values make the falloff more pronounced

default mouse = {"x": 0.0, "y": 0.0} # current eye offset from center, updated by update_image()

init python:
    _defaults = {
        "eye_center": eye_center,
        "eye_radius_scale": eye_radius_scale,
        "eye_radius": eye_radius,
        "eye_smooth": eye_smooth,
        "falloff_index": falloff_index,
    }
    for key, value in _defaults.items():
        if getattr(persistent, key) is None:
            setattr(persistent, key, value)

    def eyes_reset_persistent():
        for key, value in _defaults.items():
            setattr(persistent, key, value.copy() if isinstance(value, dict) else value)
        renpy.save_persistent()

    def update_image():
        center = persistent.eye_center
        scaleR = persistent.eye_radius_scale
        radius = persistent.eye_radius
        smooth = persistent.eye_smooth
        falloff_index = persistent.falloff_index
        mx, my = renpy.get_mouse_pos()
        dx = mx - center["x"]
        dy = my - center["y"]
        dist = (dx*dx + dy*dy) ** 0.5
        if dist == 0:
            target_x = target_y = 0.0
        else:
            # distance-based response curve
            falloff = min(dist / (radius * falloff_index), 1.0)
            movement_scale = min(radius / dist, 1.0) * falloff
            target_x = dx * movement_scale * scaleR["x"]
            target_y = dy * movement_scale * scaleR["y"]
        # smoothing
        store.mouse["x"] += (target_x - store.mouse["x"]) * smooth
        store.mouse["y"] += (target_y - store.mouse["y"]) * smooth
        store.mouse["x"] = int(store.mouse["x"])
        store.mouse["y"] = int(store.mouse["y"])
        renpy.restart_interaction()

default debug_square = 1
default eyes_panel_x = 0.00
default eyes_panel_y = 0.00
screen eyes_tuning_overlay():
    style_prefix "debug"
    zorder 200
    textbutton 'Hide eyes settings':
        align (0.95, 0.02)
        action ToggleVariable("eyes_debug", 1, 0)
    drag:
      drag_name "eyes_tuning_panel"
      draggable True
      drag_handle (0, 0, 1.0, 40)
      xalign 0.0
      yalign 0.5
      xysize (520, config.screen_height)
      frame:
          background "#0000004D"
          xsize 520  ysize config.screen_height
          padding (25, 25)
          vbox:
              spacing 20
              align (0.0, 0.65)
              frame xsize 520 ysize 40 xpos -25 ypos -12 background "#33333360":
                text "DRAG" xalign 0.5 ypos 15
              vbox:
                label "Center X [int(persistent.eye_center['x'])]"
                text "Horizontal center of the eyes anchor point." style "debug_desc"
                bar value DictValue(persistent.eye_center, "x", min=0, max=config.screen_width, step=1)
              vbox:
                label "Center Y [int(persistent.eye_center['y'])]"
                text "Vertical center of the eyes anchor point." style "debug_desc"
                bar value DictValue(persistent.eye_center, "y", min=0, max=config.screen_height, step=1)
              vbox:
                label "Radius [int(persistent.eye_radius)]"
                text "Maximum pixel distance the eyes can travel from center." style "debug_desc"
                bar value VariableValue("persistent.eye_radius", min=10, max=min(config.screen_width, config.screen_height), step=1)
              vbox:
                label "Scale Radius X [persistent.eye_radius_scale['x']:.2f]"
                text "Horizontal radius multiplier (ellipse width)." style "debug_desc"
                bar value DictValue(persistent.eye_radius_scale, "x", min=0.1, max=2.0, step=0.1)
              vbox:
                label "Scale Radius Y [persistent.eye_radius_scale['y']:.2f]"
                text "Vertical radius multiplier (ellipse height)." style "debug_desc"
                bar value DictValue(persistent.eye_radius_scale, "y", min=0.1, max=2.0, step=0.1)
              vbox:
                label "Smooth [persistent.eye_smooth:.2f]"
                text "How fast eyes approach the target per update tick." style "debug_desc"
                bar value VariableValue("persistent.eye_smooth", min=0.01, max=1.0, step=0.01)
              vbox:
                label "Falloff Index [persistent.falloff_index:.2f]"
                text "Distance curve softness (higher = more responsive near center but less responsive at edges)." style "debug_desc"
                bar value VariableValue("persistent.falloff_index", min=1.0, max=8.0, step=0.5)
              hbox spacing 20:
                textbutton "Reset":
                  action ShowMenu("confirm",
                    message="Reset eye tracking settings to defaults?",
                    yes_action=[Function(eyes_reset_persistent), Hide("confirm")],
                    no_action=Hide("confirm")
                  )
                textbutton 'Toggle debug square':
                  action ToggleVariable("debug_square", 1, 0)
    if debug_square:
      frame:
          style "debug_square"
          xpos persistent.eye_center["x"]
          ypos persistent.eye_center["y"]
          background "#f9919130"
      frame:
          style "debug_square"
          xpos persistent.eye_center["x"] + mouse["x"]
          ypos persistent.eye_center["y"] + mouse["y"]
          background "#ff000090"
          vbox:
            spacing 10
            text "offset x: [mouse['x']]"
            text "offset y: [mouse['y']]"
            text "radius_scale x: [persistent.eye_radius_scale['x']:.3f]"
            text "radius_scale y: [persistent.eye_radius_scale['y']:.3f]"
            text "radius: [persistent.eye_radius]"
            text "smooth: [persistent.eye_smooth]"

style debug_bar is slider:
  base_bar Frame("gui/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
  thumb "gui/slider/horizontal_[prefix_]thumb.webp"
  ysize 37
style debug_text is text:
  font "fonts/Dongle-Regular.ttf"
  size 30
  line_leading -20
style debug_label_text is debug_text:
  size 40
style debug_desc is debug_text:
  color "#cccccc"
style debug_button is button:
  padding (15, 15, 15, 15)
style debug_button_text is button_text:
  font "fonts/Dongle-Regular.ttf"
  size 50
  idle_color "#cccccc"
  hover_color "#f1ebeb"
style debug_square:
  padding (20, 20)
  anchor (0.5, 0.5)
  xsize 250 ysize 250
