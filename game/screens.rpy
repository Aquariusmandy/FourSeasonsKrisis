################################################################################
## Initialization
################################################################################

init offset = -1
init python:
    for i in range(100):
        FileDelete(i)

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style chaptertitle_text is gui_text:
    properties gui.text_properties("chaptertitle")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.0

style content_text is gui_text:
    properties gui.text_properties("content", accent=True)

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("system/slider_bar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("system/slider_bar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    # padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

style inventory_screen_frame is frame:
    idle_background Frame("gui/archive/Seasonal Album/frame_album_default.png")
    hover_background Frame("gui/archive/seasonal Album/frame_album_hover.png")

style navigation_textbutton is textbutton:
    idle_background Frame("temp/btn_menu_default.png", xoffset=-75, yoffset=-5, xanchor=0, yanchor=0)
    hover_background Frame("temp/btn_menu_hover.png", xoffset=-75, yoffset=-5, xanchor=0, yanchor=0)
    xysize (300, 56)
style navigation_textbutton_text:
    properties gui.text_properties("label")
    anchor (0.5,0.5)
    xpos 0.28 ypos 0.4

style slime_textbutton is textbutton:
    idle_background Frame("menubutton/btn_default.png", xoffset=-0, yoffset=-0, xanchor=0, yanchor=0)
    hover_background Frame("menubutton/btn_hover.png", xoffset=-0, yoffset=-0, xanchor=0, yanchor=0)
    xysize (230, 42)

style slime_textbutton_text:
    properties gui.text_properties("label")
    anchor (0.5,0.5)
    xpos 0.5 ypos 0.4

style chapterend_textbutton is textbutton:
    idle_background Frame("menubutton/btn_default.png", xoffset=-0, yoffset=-0, xanchor=0, yanchor=0)
    hover_background Frame("menubutton/btn_hover.png", xoffset=-0, yoffset=-0, xanchor=0, yanchor=0)
    xysize (270, 42)

style chapterend_textbutton_text:
    properties gui.text_properties("content")
    xalign 0.5 yalign 0.4

style menuback_textbutton is textbutton:
    idle_background Frame("system/btn/btn_system_default.png", xoffset=-0, yoffset=-0, xanchor=0, yanchor=0)
    hover_background Frame("system/btn/btn_system_hover.png", xoffset=-0, yoffset=-0, xanchor=0, yanchor=0)
    xysize (230, 42)
style menuback_textbutton_text:
    properties gui.text_properties("label")
    anchor (0.5,0.5)
    xpos 0.5 ypos 0.4

style choice_textbutton is textbutton:
    idle_background Frame("system/choice_idle_background.png", xoffset=-0, yoffset=-0, xanchor=0, yanchor=0)
    hover_background Frame("system/choice_hover_background.png", xoffset=-0, yoffset=-0, xanchor=0, yanchor=0)
    xysize (1500, 42)

style choice_textbutton_text:
    properties gui.text_properties("choice_button")
    xalign 0.5 
    

################################################################################
## In-game screens
################################################################################
# Define the inventory screen
screen inventory_screen():
    tag menu
    modal True
    add gui.inventory_background

    if active_set == "set1":
        add "images/main_button/frame_item.png":
            xalign 0.35  # Move the frame to the left
            yalign 0.8
        add "gui/archive/inventory-top.png":
            xalign 0.06
            yalign 0.115
    elif active_set == "cg":
        add "images/main_button/frame_cg1.png":
            xalign 0.35  # Move the frame to the left
            yalign 0.8
        add "gui/archive/inventory-top.png":
            xalign 0.06
            yalign 0.115
    elif active_set == "gallery":
        add "images/main_button/frame_album.png":
            xalign 0.35  # Move the frame to the left
            yalign 0.8
        add "gui/archive/inventory-top.png": 
            xalign 0.06
            yalign 0.115
    hbox:
        xalign 0.903
        yalign 0.115
        # imagebutton idle "images/main_button/btn_close_1.png" hover "images/main_button/btn_close_1-1.png" action [Function(renpy.hide_screen, "OverlayScreen1"),Return()]
        imagebutton idle "images/main_button/btn_close_1.png" hover "images/main_button/btn_close_1-1.png" action Return()

    # Separate vbox for each set
    if active_set == "cg":
        $ items_per_row = 0
        $ items_per_column = 5
    elif active_set == "gallery":
        $ items_per_column = 3
        $ items_per_row = 5
    elif active_set == "set1":
        $ items_per_row = 1
        $ items_per_column = 3
    else:
        $ items_per_row = 2
        $ items_per_column = 3

    vbox:
        xpos 0.88
        ypos 0.36
        # spacing 5

        imagebutton idle "images/main_button/btn_item_defalut.png" hover "images/main_button/btn_item_hover.png" action [SetVariable("active_set", "set1"), SetVariable("active_tab", "tab1")]:
            # xpos 900
            ypos 130
            # xalign 1.0 
            # yalign 1.0
        imagebutton idle "images/main_button/btn_album_default.png" hover "images/main_button/btn_album_hover.png" action [SetVariable("active_set", "gallery"), SetVariable("active_tab", "tab1")]:
            ypos 65
            # xalign 1.7 
            # yalign 1.0
        imagebutton idle "images/main_button/btn_snaps_default.png" hover "images/main_button/btn_snaps_default-1.png" action [SetVariable("active_set", "cg"), SetVariable("active_tab", "tab1")]:
            xalign 1.7 
            yalign 1.0

    # Define gallery tabs
    if (active_set == "gallery") or (active_set == "cg"):
                
        hbox:
            spacing 2
            ypos 0.224 # Adjust this value to move the gallery tabs up or down
            xpos 0.123  
            # Gallery Tab 1
            imagebutton idle "images/main_button/btn_summer_default.png" hover "images/main_button/btn_summer_pressed.png" action [SetVariable("active_tab", "tab1")]:
                yanchor 1.0
                ypos 35
            # Gallery Tab 2
            imagebutton idle "images/main_button/btn_autumn_default.png" hover "images/main_button/btn_autumn_pressed.png" action [SetVariable("active_tab", "tab2")]:
                yanchor 1.0
                ypos 35

            # Gallery Tab 3
            imagebutton idle "images/main_button/btn_winter_default.png" hover "images/main_button/btn_winter_pressed.png" action [SetVariable("active_tab", "tab3")]:
                yanchor 1.0
                ypos 35
            # Gallery Tab 4
            imagebutton idle "images/main_button/btn_spring_default.png" hover "images/main_button/btn_spring_pressed.png" action [SetVariable("active_tab", "tab4")]:
                yanchor 1.0 
                ypos 35           
        
        image "gui/archive/Seasonal Album/album_line.png":
            yanchor 0.0
            xpos 0.123
            ypos 275



    viewport:
        spacing 20
        xalign 0.35
        yalign 0.75
        if active_set == "cg":
            viewport_xsize 1200
            viewport_ysize 850
        if active_set == "gallery":
            scrollbars "vertical"
            mousewheel True
            draggable True  
            pagekeys True
        child_size (1380, 2000)
        side_spacing 2
        viewport_xsize 1380
        viewport_ysize 650

        vbox:

            $ items_count = len(image_button_images[active_set][active_tab])
            $ rows_count = (items_count - 1) // items_per_column + 1
            for row_index in range(rows_count):
            # for row_index in range(5):

                hbox:
                    if active_set == 'cg':
                        spacing -18
                    elif active_set == 'set1':
                        spacing 20
                    else:
                        spacing -10
                    # Loop through columns within the row
                    for column_index in range(items_per_column):
                        $ item_index = row_index * items_per_column + column_index
                        if item_index < items_count:
                            $ image_dict = image_button_images[active_set][active_tab][item_index]
                            $ item_background = get_item_background(active_set, active_tab, item_index)  # Function to get item description
                            $ item_name = get_item_name(active_set, active_tab, item_index)
                            $ item_locked = get_item_locked(active_set, active_tab, item_index)

                            
                            # Conditional statement to set frame background based on active_set
                            if active_set == "set1":
                                frame:
                                    xpos 0.8
                                    ypos 0.9
                                    background "transparent1.png"
                                    #items
                                    xysize (380, 250)
                                    if achievement.has(item_name):
                                        imagebutton idle image_dict["idle"] hover image_dict["hover"] action [Show("item_description_popup",item_click_background=item_background)]:
                                            anchor (0.5,0.5)
                                            xpos 0.5
                                            ypos 0.5
                                    else:
                                        image item_locked:
                                            anchor (0.5,0.5)
                                            xpos 0.5
                                            ypos 0.5
                                   
                            elif active_set == "cg":
                                frame:
                                    style "inventory_screen_frame" # make the frame empty
                                    xysize (290, 658)
                                    ypos 0.48
                                    xpos 0.77
                                    # cgs
                                    # xysize (380, 250)
                                    if achievement.has(item_name):
                                        imagebutton idle "gui/archive/Seasonal Album/frame_album_default.png" hover "gui/archive/seasonal Album/frame_album_hover2.png" action [Show("picture_popup",item_click_background=item_background,active_set=active_set ,active_tab=active_tab,index=item_index)]:
                                            xpos 0.5
                                            ypos 0.5
                                            xanchor 0.5
                                            yanchor 0.5
                                        image image_dict["idle"]:
                                            xysize (245,613)
                                            anchor (0.5,0.5)
                                            xpos 0.5
                                            ypos 0.5
                                    else:
                                        imagebutton idle "gui/archive/Seasonal Album/frame_album_default.png" hover "gui/archive/seasonal Album/frame_album_hover2.png" action NullAction():
                                            xpos 0.5
                                            ypos 0.5
                                            xanchor 0.5
                                            yanchor 0.5
                                        image item_locked:
                                            xysize (245,613)
                                            anchor (0.5,0.5)
                                            xpos 0.5
                                            ypos 0.5

                            elif active_set == "gallery":
                                frame:
                                    style "inventory_screen_frame" # make the frame empty
                                    xpos 0.3
                                    ypos 0.0 
                                    xysize (424, 256)
                                    if active_tab == 'tab1':
                                        $tab_name = 'sum_gallery'
                                    elif active_tab == 'tab2':
                                        $tab_name = 'aut_gallery'
                                    elif active_tab == 'tab3':
                                        $tab_name = 'win_gallery'
                                    else:
                                        $tab_name = 'spr_gallery'
                                    # create hover effect,and the button will do nothing when the item hasn't unlocked
                                    if achievement.has(tab_name):
                                        imagebutton idle "gui/archive/Secret Snaps/frame_snaps_default.png" hover "gui/archive/Secret Snaps/frame_snaps_hover2.png" action [Show("gallery_popup",item_click_background=item_background,active_set=active_set ,active_tab=active_tab,index=item_index)]:
                                            anchor (0.5,0.5)
                                            xpos 0.5
                                            ypos 0.5
                                        image image_dict["idle"]:
                                            xysize(379,211)
                                            anchor (0.5,0.5)
                                            xpos 0.5
                                            ypos 0.5
                                    else:
                                        imagebutton idle "gui/archive/Secret Snaps/frame_snaps_default.png" hover "gui/archive/Secret Snaps/frame_snaps_hover2.png" action NullAction():
                                            anchor (0.5,0.5)
                                            xpos 0.5
                                            ypos 0.5
                                        image item_locked:
                                            xysize(379,211)
                                            anchor (0.5,0.5)
                                            xpos 0.5
                                            ypos 0.5
                if active_set == 'set1':
                    hbox: # create the vertical spacing
                        xysize (1300,5)  


screen item_description_popup(item_click_background):
    modal True
    add "transparent2.png" xpos -0.1 ypos -0.8
    
    if active_set == "set1":
        hbox:
            xpos 0.3
            ypos 0.3
            xsize 800
            ysize 330 
            vbox:
                frame:
                    background item_click_background  # Change this to your description frame background

                imagebutton idle "images/main_button/btn_close.png" action Hide("item_description_popup"):
                    xpos 0.803
                    ypos -11.057


screen gallery_popup(item_click_background,active_set,active_tab,index):
    modal True
    add "transparent2.png" xpos -0.1 ypos -0.8
    $length = len(image_button_images[active_set][active_tab])
    hbox:
        xalign 0.5
        yalign 0.5
        # xysize(1700,1000)
        $ index_left = index - 1
        $ index_right =index + 1 

        if(index_left >-1):
            $ name_left = get_item_name(active_set, active_tab, index_left)
        if(index_right <length):
            $ name_right = get_item_name(active_set, active_tab, index_right)
        # left click then show the previous (index-1) cg
        if (index_left > -1):
            $ item_background = get_item_background(active_set, active_tab, index_left)
            imagebutton idle "gui/archive/Seasonal Album/btn/btn_left_1.png" hover "gui/archive/Seasonal Album/btn/btn_left_2.png" action [Show("gallery_popup",item_click_background=item_background,active_set=active_set ,active_tab=active_tab,index=index_left)]:
                xanchor 0.0
                xpos -0.05
                yalign 0.5
        else:
            imagebutton idle "gui/archive/Seasonal Album/btn/btn_left_1.png" hover "gui/archive/Seasonal Album/btn/btn_left_1.png" action NullAction():
                xanchor 0.0
                xpos -0.05
                yalign 0.5           
        vbox:
            xalign 0.5
            yalign 0.5
            imagebutton idle "gui/archive/Seasonal Album/btn/btn_close_2.png" action Hide("gallery_popup"):
                xpos 1.0
                ypos 0.0
            image item_click_background:
                xysize(1600,900)
                xalign 0.5
                yalign 0.5
        # right click then show the next (index+1) cg
        if (index_right < length) :
            $ item_background = get_item_background(active_set, active_tab, index_right)
            imagebutton idle "gui/archive/Seasonal Album/btn/btn_right_1.png" hover "gui/archive/Seasonal Album/btn/btn_right_2.png" action [Show("gallery_popup",item_click_background=item_background,active_set=active_set ,active_tab=active_tab,index=index_right)]:
                xanchor 1.0
                xpos 0.93
                yalign 0.5
        else:
            imagebutton idle "gui/archive/Seasonal Album/btn/btn_right_1.png" hover "gui/archive/Seasonal Album/btn/btn_right_1.png" action NullAction():
                xanchor 1.0
                xpos 0.93
                yalign 0.5




screen picture_popup(item_click_background,active_set,active_tab,index):
    modal True
    add "transparent2.png" xpos -0.1 ypos -0.8
    $length = len(image_button_images[active_set][active_tab])
    hbox:
        xalign 0.5
        yalign 0.5
        # xysize(1700,1000)
        $ index_left = index - 1
        $ index_right =index + 1   

        if(index_left >-1):
            $ name_left = get_item_name(active_set, active_tab, index_left)
        if(index_right <length):
            $ name_right = get_item_name(active_set, active_tab, index_right)
        # left click then show the previous (index-1) cg
        if (index_left > -1) and (achievement.has(name_left)):
            $ item_background = get_item_background(active_set, active_tab, index_left)
            imagebutton idle "gui/archive/Seasonal Album/btn/btn_left_1.png" hover "gui/archive/Seasonal Album/btn/btn_left_2.png" action [Show("picture_popup",item_click_background=item_background,active_set=active_set ,active_tab=active_tab,index=index_left)]:
                xanchor 0.0
                xpos -0.05
                yalign 0.5
        else:
            imagebutton idle "gui/archive/Seasonal Album/btn/btn_left_1.png" hover "gui/archive/Seasonal Album/btn/btn_left_1.png" action NullAction():
                xanchor 0.0
                xpos -0.05
                yalign 0.5           
        vbox:
            xalign 0.5
            yalign 0.5
            imagebutton idle "gui/archive/Seasonal Album/btn/btn_close_2.png" action Hide("picture_popup"):
                xpos 1.0
                ypos 0.0
            image item_click_background:
                xysize(1600,900)
                xalign 0.5
                yalign 0.5
        # right click then show the next (index+1) cg
        if (index_right < length) and (achievement.has(name_right)):
            $ item_background = get_item_background(active_set, active_tab, index_right)
            imagebutton idle "gui/archive/Seasonal Album/btn/btn_right_1.png" hover "gui/archive/Seasonal Album/btn/btn_right_2.png" action [Show("picture_popup",item_click_background=item_background,active_set=active_set ,active_tab=active_tab,index=index_right)]:
                xanchor 1.0
                xpos 0.93
                yalign 0.5
        else:
            imagebutton idle "gui/archive/Seasonal Album/btn/btn_right_1.png" hover "gui/archive/Seasonal Album/btn/btn_right_1.png" action NullAction():
                xanchor 1.0
                xpos 0.93
                yalign 0.5



screen OverlayScreen():
    modal True
    # Background to dim the underlying content.
    add "temp/transparent.png"  # Path to your overlay background image

    # Vertical box to contain your overlay content.
    vbox:
        
        xalign 0.96
        yalign 0.9
        spacing 10  # Adjust the spacing between items as needed.
        text _("To Be Continue") style "chapterend_text":
            anchor(0,0)
            xpos 0.1
        # Add your image buttons here.
        textbutton _("Check A.S.H. Archive") action ShowMenu("inventory") style "chapterend_textbutton":
            anchor (0,0)
            xpos 0.5
            ypos 0.88
        textbutton _("Next Chapter") action Return() style "chapterend_textbutton":
            anchor (0,0)
            xpos 0.5
            ypos 0.9

screen OverlayScreen1():
    add "system/red dot.png" xalign 0.937 yalign 0.02
    zorder 102
    modal False 

screen ClickableArea():
    zorder 101
    modal False
    imagebutton:
        xpos 0.899
        ypos 0.0315
        xanchor 0.0
        yanchor 0.0
        idle "temp/transparent3.png"
        hover "menubutton/btn_Archive_hover.png"
        action Function(renpy.hide_screen, "OverlayScreen1"), ShowMenu("inventory_screen")

screen white_fade:
    modal True
    add Solid(0, 0, gui.width(), gui.height(), (255, 255, 255, 0))
    on "show" action Ease(color.a, 255, 10.0)

style frame is default
style inventory_screen_frame is empty

## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action style "choice_textbutton"


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 656
    yanchor 0.5
    spacing 10

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100
    # if renpy.seen_label("chapter_3"):
    #     $titletext = "Chapter 4.  WINTER"
    # elif renpy.seen_label("chapter_2"):
    #     $titletext = "Chapter 3.  AUTUMN"
    # elif renpy.labelseen("chapter_2"):
    #     $titletext = "Chapter 2.  SUMMER"
    # else:
    #     $titletext = "Chapter 1.  SUMMER"

    # text _(titletext) style "chaptertitle_text":
    #     anchor(1,0)
    #     xpos 0.03
    #     ypos 0.032

    
    ## Display the button image
    vbox:
        anchor (0,0)
        xpos 0.03
        ypos 0.03
        text _("Debug Quick Menu")
        textbutton _("Back") action Rollback() style "slime_textbutton"
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True) style "slime_textbutton"
    imagebutton:
        idle "temp/btn_HBMenu_default.png"  # Replace "your_button_image.png" with your button image path
        hover "temp/btn_HBMenu_hover.png"  # Replace "your_button_image_hover.png" with hover image path
        action [ShowMenu("quick_menu_options")]  # Display the menu options upon clicking
        anchor(1,0)
        xpos 0.95  # Align the image button to the right
        ypos 0.032  # Align the image button to the top
    imagebutton:
        idle "temp/btn_Archive_default.png"  
        hover "temp/btn_Archive_hover.png"  
        action ShowMenu("inventory")  
        anchor(1,0)
        xpos 0.9  # Align the image button to the right
        ypos 0.032  # Align the image button to the top

## Define the menu options

## Define the menu options
screen quick_menu_options():
    modal True 
    ## Display the button image
    imagebutton:
        # xysize (1600,1280)
        xpos -0.1 
        ypos -0.8
        idle "images/transparent4.png"
        hover "images/transparent4.png"
        action Return()
    imagebutton:
        idle "temp/btn_HBMenu_default.png"  # Replace "your_button_image.png" with your button image path
        hover "temp/btn_HBMenu_hover.png"  # Replace "your_button_image_hover.png" with hover image path
        action Return()  # Display the menu options upon clicking
        anchor(0,1)
        xpos 0.95  # Align the image button to the right
        ypos 0.032  # Align the image button to the top
    imagebutton:
        idle "temp/btn_Archive_default.png"  
        hover "temp/btn_Archive_hover.png"  
        action ShowMenu("inventory")  
        anchor(0,1)
        xpos 0.9  # Align the image button to the right
        ypos 0.032  # Align the image button to the top

    vbox:
        spacing 10
        style_prefix "quick"
        anchor(0,1)
        xpos 0.8621
        ypos 0.1

        textbutton _("Save") action ShowMenu('save') style "slime_textbutton"

        textbutton _("Load") action ShowMenu("load") style "slime_textbutton"
            
        textbutton _("History") action ShowMenu('history') style "slime_textbutton"

        textbutton _("Settings") action ShowMenu('preferences') style "slime_textbutton"

        textbutton _("Main Menu") action MainMenu()style "slime_textbutton"

        textbutton _("Quit") action Quit() style "slime_textbutton"


        


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the inåterface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is gui_button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")

style slime_textbutton is quick_button
style menuback_textbutton is quick_button


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.
# Define a custom class to handle idle and hover images
# Adjust the size of the button to match the image size
screen navigation:
    add "temp/logo.png" ypos 0.1 xpos 0.6

        ### Debug Quick Menu ###
    vbox:
        anchor(0, 0)
        xpos 0.77
        ypos 0.75
        spacing 10
        label _("Debug Quick Menu")
        textbutton "Chapter 1" action Start("chapter_1"):
            style "slime_textbutton"
        textbutton "Chapter 2" action Start("chapter_2"):
            style "slime_textbutton"
        textbutton "Chapter 3" action Start("chapter_3"):
            style "slime_textbutton"
        textbutton "Chapter 4" action Start("chapter_4"):
            style "slime_textbutton"

    vbox:
        style_prefix "navigation"
        xpos 0.8
        yalign 0.5
        spacing gui.navigation_spacing
        

        ## Define the style for the textbuttons
        
        if main_menu:
            textbutton _("New Game") action Start() style "navigation_textbutton"

        else:
            
            textbutton _("Save") action ShowMenu("save") style "navigation_textbutton" 

        textbutton _("Load Game") action ShowMenu("load")  style "navigation_textbutton" 
        textbutton _("A.S.H. Archive") action ShowMenu("inventory") style "navigation_textbutton" 
        textbutton _("Settings") action ShowMenu("preferences") style "navigation_textbutton" 

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True) style "navigation_textbutton"
        elif not main_menu:
            textbutton _("Main Menu") action MainMenu() style "navigation_textbutton" 

        textbutton _("Credits") action ShowMenu("about") style "navigation_textbutton" 
        # textbutton _("History") action ShowMenu("history") style "navigation_textbutton" 

        # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
        #     textbutton _("Help") action ShowMenu("help") style "navigation_textbutton"
        
        if renpy.variant("pc"):
            textbutton _("Quit") action Quit(confirm=not main_menu) style "navigation_textbutton"


screen gamemenu_navigation:

    vbox:
        xpos 0.02
        ypos 0.3
        spacing gui.navigation_spacing
        

        ## Define the style for the textbuttons
        # textbutton _("Save") action ShowMenu("save") ## could not save in this action
        textbutton _("Load") action ShowMenu("load")  
        textbutton _("History") action ShowMenu("history") 
        textbutton _("Settings") action ShowMenu("preferences") 
        textbutton _("Credits") action ShowMenu("about") 
        if not main_menu:
            textbutton _("Main Menu") action MainMenu() 
        else:
            textbutton _("Main Menu") action Return()

        # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
        #     textbutton _("Help") action ShowMenu("help") style "navigation_textbutton"
        
        if renpy.variant("pc"):
            textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button is navigation_textbutton
style navigation_button_text is gui_button_text


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text

style main_menu_title is main_menu_text
style main_menu_version is main_menu_text
style chapterend_text is gui_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 7.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")
    color "#8D86C9"

style main_menu_version:
    properties gui.text_properties("version")

style chapterend_text:
    properties gui.text_properties("chapterend")
    outlines [ (absolute(1), "#000", absolute(2), absolute(2)) ]
    color "#ffffff"


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"
    
    frame:
        if CurrentScreenName() == "preferences":
            style "game_menu_settings_frame"
            text _("Setting"):
                style "main_menu_title"
                xalign 0.03
                yalign -0.1

        elif CurrentScreenName() == "save":
            style "game_menu_save_frame"
            text _("Save"):
                style "main_menu_title"
                xalign 0.03
                yalign -0.1
        elif CurrentScreenName() == "load":
            style "game_menu_load_frame"
            text _("Load"):
                style "main_menu_title"
                xalign 0.03
                yalign -0.1
        elif CurrentScreenName() == "history":
            style "game_menu_history_frame"
            text _("History"):
                style "main_menu_title"
                xalign 0.03
                yalign -0.1
        else:
            style "game_menu_outer_frame"
        
        hbox:
            
            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude
        use gamemenu_navigation
        textbutton _("Back") action Return() style "menuback_textbutton":
            xalign 0.05
            yalign 0.98
                
    # if main_menu:  # Condition to check if in main menu
    #     textbutton _("Return"):
    #         style "return_button"
    #         action Return()
    
    #     label title

    #     key "game_menu" action ShowMenu("main_menu")
             



style game_menu_outer_frame is empty
style game_menu_settings_frame is empty
style game_menu_save_frame is empty
style game_menu_load_frame is empty
style game_menu_history_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

### original game menu background setting
style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    xalign 0.5
    yalign 0.5
    background "gui/overlay/game_menu.png"

### trying to make various game menu backgrounds
style game_menu_settings_frame:
    bottom_padding 45
    top_padding 100
    xalign 0.5
    yalign 0.5
    background "system/settings_bg.png"

style game_menu_save_frame:
    bottom_padding 45
    top_padding 100
    xalign 0.5
    yalign 0.5
    background "system/save_bg.png"

style game_menu_load_frame:
    bottom_padding 45
    top_padding 100
    xalign 0.5
    yalign 0.5
    background "system/load_bg.png" 

style game_menu_history_frame:
    bottom_padding 45
    top_padding 100
    xalign 0.4
    yalign 0.5
    background "system/history_bg.png"       

style game_menu_navigation_frame:
    xsize 280
    yfill True
    

style game_menu_content_frame:
    xpos 0.03
    ypos 0.02
    top_margin 15
    right_margin 30

style game_menu_viewport:
    xsize 2000
    xpos 0.01
    ysize 3000

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15
    xalign -0.1

style game_menu_label:
    xpos 75
    ysize 180
    xalign 3.0

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    xalign 3.0

style return_button:
    xpos 0.1
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():
    tag menu
    
    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):
        
        
        vbox:
            style_prefix "about"
            xalign 1.0 

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
            
       

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size



## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu
    

    use file_slots(_("Save"))


screen load():

    tag menu
    

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"
                        # this is for debug    
                        # textbutton _("delete") action FileDelete(slot):
                        #     style "quick_menu_text"
                        #     ypos -0.9

                        key "save_delete" action FileDelete(slot)
                        

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5
                    yalign 0.9

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()

                # if config.has_sync:
                #     if CurrentScreenName() == "save":
                #         textbutton _("Upload Sync"):
                #             action UploadSync()
                #             xalign 0.5
                #     else:
                #         textbutton _("Download Sync"):
                #             action DownloadSync()
                #             xalign 0.5
       
style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text
style game_menu_viewport is gui_viewport


style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text
style return_button is navigation_button
style return_button_text is navigation_button_text
style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:
            xanchor 0.0
            xpos 0.15
            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
                
                vbox:
                    style_prefix "radio"
                    label _("Language")
                    # Real languages should go alphabetical order by English name.
                    textbutton _("English") text_font "DejaVuSans.ttf" action Language(None)
                    textbutton _("繁體中文") text_font "GlowSansSC-Normal-Regular.ttf" action Language("Mandarin")
                    textbutton _("日本語") text_font "GlowSansSC-Normal-Regular.ttf" action Language("Japanese")


                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    # if config.has_voice:
                    #     label _("Voice Volume")

                    #     hbox:
                    #         bar value Preference("voice volume")

                    #         if config.sample_voice:
                    #             textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
            
            

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style game_menu_viewport is gui_viewport


style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=0.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:
                xsize 1400
                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    
    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"
        
        vbox:
            spacing 10
            xysize (1000,700)
            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():
    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    # hbox:
    #     label "V"
    #     text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():
    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()
    

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "transparent2.png" xpos -0.1 ypos -0.8

    frame:

        vbox:
            xalign .55
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5
                yalign 0.5

            hbox:
                xalign 0.5
                yalign 0.7
                spacing 50

                textbutton _("Yes") action yes_action style "menuback_textbutton"
                textbutton _("No") action no_action style "menuback_textbutton"

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "system/system_popup.png", "system/system_popup.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    # background Frame([ "gui/confirm_frame.png", "temp/frame_album_default.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    properties gui.text_properties("content")
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900