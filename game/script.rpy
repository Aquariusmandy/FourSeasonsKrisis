#メインメニューの音楽
define config.main_menu_music = "audio/main_theme.mp3"

style default:
    font FontGroup().add("BaiJamjuree-Regular.ttf", 0x0020, 0x007f).add("GlowSansSC-Normal-Regular.ttf", 0x0000, 0xffff)

# セリフテキストボックスの定義。20は左右上下の余白
style narration_window:
    background Frame("gui/narration_window.png", 20,20)   
style vanta_window:
    background Frame("gui/gui/ui_dialoguebox_vanta.png", 20,20)   
style wilson_window:
    background Frame("gui/gui/ui_dialoguebox_wilson.png", 20,20)   
style zali_window:
    background Frame("gui/gui/ui_dialoguebox_zali.png", 20,20)   
style npc_window:
    background Frame("gui/gui/ui_dialoguebox_npc.png", 20,20)
style vandw_window:
    background Frame("gui/gui/ui_dialoguebox_v&w.png", 20,20)
style wandv_window:
    background Frame("gui/gui/ui_dialoguebox_w&v.png", 20,20) 
style vandz_window:
    background Frame("gui/gui/ui_dialoguebox_v&z.png", 20,20)  
style zandw_window:
    background Frame("gui/gui/ui_dialoguebox_z&w.png", 20,20)        
style vandc_window:
    background Frame("gui/gui/ui_dialoguebox_crew.png", 20,20)       
    
init:    
    # ネームボックスの定義
    if (_preferences.language == "japanese"):
        style vanta_namebox:
            background "gui/gui/jp/ui_namebox_vanta_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style wilson_namebox:
            background "gui/gui/jp/ui_namebox_wilson_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style zali_namebox:
            background "gui/gui/jp/ui_namebox_zali_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandw_namebox:
            background "gui/gui/jp/ui_namebox_v&w_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style wandv_namebox:
            background "gui/gui/jp/ui_namebox_w&v_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandz_namebox:
            background "gui/gui/jp/ui_namebox_z&v_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style zandw_namebox:
            background "gui/gui/jp/ui_namebox_z&w_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandc_namebox:
            background "gui/gui/jp/ui_namebox_v&c_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる
        style npc01_namebox:
            background "gui/gui/jp/ui_namebox_npc03_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc02_namebox:
            background "gui/gui/jp/ui_namebox_npc02_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc03_namebox:
            background "gui/gui/jp/ui_namebox_npc01_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc04_namebox:
            background "gui/gui/jp/ui_namebox_npc04_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc05_namebox:
            background "gui/gui/jp/ui_namebox_npc05_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc06_namebox:
            background "gui/gui/jp/ui_namebox_npc06_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる
    elif (_preferences.language == "mandarin"):
        style vanta_namebox:
            background "gui/gui/ui_namebox_vanta.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style wilson_namebox:
            background "gui/gui/ui_namebox_wilson.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style zali_namebox:
            background "gui/gui/ui_namebox_zali.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandw_namebox:
            background "gui/gui/ui_namebox_v&w.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style wandv_namebox:
            background "gui/gui/ui_namebox_w+v.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandz_namebox:
            background "gui/gui/ui_namebox_v&z.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style zandw_namebox:
            background "gui/gui/ui_namebox_z&w.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandc_namebox:
            background "gui/gui/ui_namebox_v&c.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる
        
        style npc01_namebox:
            background "gui/gui/cn/ui_namebox_npc03_cn.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc02_namebox:
            background "gui/gui/cn/ui_namebox_npc02_cn.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc03_namebox:
            background "gui/gui/cn/ui_namebox_npc01_cn.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc04_namebox:
            background "gui/gui/cn/ui_namebox_npc04_cn.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc05_namebox:
            background "gui/gui/cn/ui_namebox_npc05_cn.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc06_namebox:
            background "gui/gui/cn/ui_namebox_npc06_cn.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

    else:
        style vanta_namebox:
            background "gui/gui/ui_namebox_vanta.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style wilson_namebox:
            background "gui/gui/ui_namebox_wilson.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style zali_namebox:
            background "gui/gui/ui_namebox_zali.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandw_namebox:
            background "gui/gui/ui_namebox_v&w.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style wandv_namebox:
            background "gui/gui/ui_namebox_w+v.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandz_namebox:
            background "gui/gui/ui_namebox_v&z.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style zandw_namebox:
            background "gui/gui/ui_namebox_z&w.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandc_namebox:
            background "gui/gui/ui_namebox_v&c.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる
        style npc01_namebox:
            background "gui/gui/ui_namebox_npc01.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc02_namebox:
            background "gui/gui/ui_namebox_npc02.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc03_namebox:
            background "gui/gui/ui_namebox_npc03.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc04_namebox:
            background "gui/gui/ui_namebox_npc04.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc05_namebox:
            background "gui/gui/ui_namebox_npc05.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc06_namebox:
            background "gui/gui/ui_namebox_npc06.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる
init:
    # キャラクター画像の定義
    image van_sum_nor = "images/chara/van_sum_nor.png"
    image van_sum_thi = "images/chara/van_sum_thi.png"
    image van_sum_ser = "images/chara/van_sum_ser.png"
    image van_sum_hap = "images/chara/van_sum_hap.png"
    image van_sum_sur = "images/chara/van_sum_sur.png"
    image van_sum_emb = "images/chara/van_sum_emb.png"
    image van_sum_con = "images/chara/van_sum_con.png"

    image van_ci_nor = "images/chara/van_ci_nor.png"
    image van_ci_thi = "images/chara/van_ci_thi.png"
    image van_ci_ser = "images/chara/van_ci_ser.png"
    image van_ci_hap = "images/chara/van_ci_hap.png"
    image van_ci_sur = "images/chara/van_ci_sur.png"
    image van_ci_emb = "images/chara/van_ci_emb.png"
    image van_ci_con = "images/chara/van_ci_con.png"
    image van_ci_3 = "images/chara/van_ci_3.png" 

    image van_hr_nor = "images/chara/van_hr_nor.png"
    image van_hr_thi = "images/chara/van_hr_thi.png"
    image van_hr_ser = "images/chara/van_hr_ser.png"
    image van_hr_hap = "images/chara/van_hr_hap.png"
    image van_hr_sur = "images/chara/van_hr_sur.png"
    image van_hr_emb = "images/chara/van_hr_emb.png"
    image van_hr_con = "images/chara/van_hr_con.png"
    image van_hr_3 = "images/chara/van_hr_3.png"

    image wil_ci_nor = "images/chara/wil_ci_nor.png"
    image wil_ci_thi = "images/chara/wil_ci_thi.png"
    image wil_ci_ser = "images/chara/wil_ci_ser.png"
    image wil_ci_hap = "images/chara/wil_ci_hap.png"
    image wil_ci_sur = "images/chara/wil_ci_sur.png"
    
    image wil_hr_nor = "images/chara/wil_hr_nor.png"
    image wil_hr_thi = "images/chara/wil_hr_thi.png"
    image wil_hr_ser = "images/chara/wil_hr_ser.png"
    image wil_hr_hap = "images/chara/wil_hr_hap.png"
    image wil_hr_sur = "images/chara/wil_hr_sur.png"

    image zal_ci_nor = "images/chara/zal_ci_nor.png"
    image zal_ci_thi = "images/chara/zal_ci_thi.png"
    image zal_ci_ser = "images/chara/zal_ci_ser.png"
    image zal_ci_hap = "images/chara/zal_ci_hap.png"
    image zal_ci_sur = "images/chara/zal_ci_sur.png"
    
    image zal_hr_nor = "images/chara/zal_hr_nor.png"
    image zal_hr_thi = "images/chara/zal_hr_thi.png"
    image zal_hr_ser = "images/chara/zal_hr_ser.png"
    image zal_hr_hap = "images/chara/zal_hr_hap.png"
    image zal_hr_sur = "images/chara/zal_hr_sur.png"
    
    image crew1_nor_img = "images/chara/crew1_nor.png"
    image crew1_3_img = "images/chara/crew1_3.png"
    image crew3_nor_img = "images/chara/crew3_nor.png"
    image crew3_ang_img = "images/chara/crew3_ang.png"
    image crew3_hap_img = "images/chara/crew3_hap.png"
    image crew3_3_img = "images/chara/crew3_3.png"

    image npc1_img = "images/chara/npc_01.png"
    image npc2_img = "images/chara/npc_02.png"
    image npc3_img = "images/chara/npc_03.png"
    image npc4_img = "images/chara/npc_04.png"
    image npc5_img = "images/chara/npc_05.png"
    image npc6_img = "images/chara/npc_06.png"

    image sum_cv_img = "images/cvisual/sum_cv.png"
    image aut_cv_img = "images/cvisual/aut_cv.png"
    image win_cv_img = "images/cvisual/win_cv.png"
    image spr_cv_img = "images/cvisual/spr_cv.png"

    image sum_bg_beach1_img = "images/bg/sum_bg_beach_01.png"
    image sum_bg_beach2_img = "images/bg/sum_bg_beach_02.png"
    image sum_bg_beach3_img = "images/bg/sum_bg_beach_03.png"
    image sum_bg_beach4_img = "images/bg/sum_bg_beach_04.png"
    image sum_bg_shop1_img = "images/bg/sum_bg_shop_01.png"
    image sum_bg_shop2_img = "images/bg/sum_bg_shop_02.png"

    image aut_bg_village1_img = "images/bg/aut_bg_village_01.png"
    image aut_bg_village2_img = "images/bg/aut_bg_village_02.png"
    image aut_bg_forest1_img = "images/bg/aut_bg_forest_01.png"
    image aut_bg_forest2_img = "images/bg/aut_bg_forest_02.png"
    image aut_bg_forest3_img = "images/bg/aut_bg_forest_03.png"

    image win_bg_office1_img = "images/bg/win_bg_office_01.png"
    image win_bg_office2_img = "images/bg/win_bg_office_02.png"
    image win_bg_shop_img = "images/bg/win_bg_shop_01.png"
    image win_bg_park_img = "images/bg/win_bg_park_01.png"
    image win_bg_home_img = "images/bg/win_bg_home_01.png"
    image win_bg_street1_img = "images/bg/win_bg_street_01.png"
    image win_bg_street2_img = "images/bg/win_bg_street_02.png"
    image win_bg_run_img = "images/bg/win_bg_run.png"

    image spr_bg_office1_img = "images/bg/spr_bg_office_01.png"
    image spr_bg_buil1_img = "images/bg/spr_bg_buil_01.png"
    image spr_bg_buil2_img = "images/bg/spr_bg_buil_02.png"
    image spr_bg_lab1_img = "images/bg/spr_bg_lab_01.png"
    image spr_bg_lab2_img = "images/bg/spr_bg_lab_02.png"
    image spr_bg_hall1_img = "images/bg/spr_bg_hall_01.png"
    image spr_bg_hall2_img = "images/bg/spr_bg_hall_02.png"

    image sum_st_btst_img = "images/still/sum_st_btst.png"
    image sum_st_bten_img = "images/still/sum_st_bten.png"
    image sum_st_fny_img = "images/still/sum_st_fny.png"
    image sum_edcg_img = "images/still/sum_st_edcg.png"

    image aut_st_btst_img = "images/still/aut_st_btst.png"
    image aut_st_bten_img = "images/still/aut_st_bten.png"
    image aut_st_fny_img = "images/still/aut_st_fny.png"
    image aut_edcg_img = "images/still/aut_st_edcg.png"

    image win_st_btst_img = "images/still/win_st_btst.png"
    image win_st_bten_img = "images/still/win_st_bten.png"
    image win_st_fny_img = "images/still/win_st_fny.png"
    image win_edcg_img = "images/still/win_st_edcg.png"

    image spr_st_wilson_img = "images/still/spr_st_wilson.png"
    image spr_st_zali_img = "images/still/spr_st_zali.png"
    image spr_st_fny_img = "images/still/spr_st_fny.png"
    image spr_edcg_img = "images/still/spr_st_edcg.png"

    image com_base_img = "images/comic/com_base.png"

    image sum_com_1_img = "images/comic/sum_com_1.png"
    image sum_com_2_img = "images/comic/sum_com_2.png"
    image sum_com_3_img = "images/comic/sum_com_3.png"
    image sum_com_4_img = "images/comic/sum_com_4.png"
    image sum_com_5_img = "images/comic/sum_com_5.png"
    image sum_com_6_img = "images/comic/sum_com_6.png"
    image sum_com_7_img = "images/comic/sum_com_7.png"
    image sum_com_8_img = "images/comic/sum_com_8.png"

    image aut_com_1_img = "images/comic/aut_com_1.png"
    image aut_com_2_img = "images/comic/aut_com_2.png"
    image aut_com_3_img = "images/comic/aut_com_3.png"
    image aut_com_4_img = "images/comic/aut_com_4.png"
    image aut_com_5_img = "images/comic/aut_com_5.png"
    image aut_com_6_img = "images/comic/aut_com_6.png"
    image aut_com_7_img = "images/comic/aut_com_7.png"
    image aut_com_8_img = "images/comic/aut_com_8.png"
    image aut_com_9_img = "images/comic/aut_com_9.png"
    image aut_com_10_img = "images/comic/aut_com_10.png"

    image win_com_1_img = "images/comic/win_com_1.png"
    image win_com_2_img = "images/comic/win_com_2.png"
    image win_com_3_img = "images/comic/win_com_3.png"
    image win_com_4_img = "images/comic/win_com_4.png"
    image win_com_5_img = "images/comic/win_com_5.png"

    image spr_com_1_img = "images/comic/spr/spr_com_01.png"
    image spr_com_2_img = "images/comic/spr/spr_com_02.png"
    image spr_com_3_img = "images/comic/spr/spr_com_03.png"
    image spr_com_4_img = "images/comic/spr/spr_com_04.png"
    image spr_com_5_img = "images/comic/spr/spr_com_05.png"
    image spr_com_6_img = "images/comic/spr/spr_com_06.png"
    image spr_com_7_img = "images/comic/spr/spr_com_07.png"
    image spr_com_8_img = "images/comic/spr/spr_com_08.png"
    image spr_com_9_img = "images/comic/spr/spr_com_09.png"
    image spr_com_10_img = "images/comic/spr/spr_com_10.png"
    image spr_com_11_img = "images/comic/spr/spr_com_11.png"
    image spr_com_12_img = "images/comic/spr/spr_com_12.png"
    image spr_com_13_img = "images/comic/spr/spr_com_13.png"
    image spr_com_14_img = "images/comic/spr/spr_com_14.png"
    image spr_com_15_img = "images/comic/spr/spr_com_15.png"
    image spr_com_16_img = "images/comic/spr/spr_com_16.png"
    image spr_com_17_img = "images/comic/spr/spr_com_17.png"
    image spr_com_18_img = "images/comic/spr/spr_com_18.png"
    image spr_com_19_img = "images/comic/spr/spr_com_19.png"
    image spr_com_20_img = "images/comic/spr/spr_com_20.png"
    image spr_com_21_img = "images/comic/spr/spr_com_21.png"
    image spr_com_22_img = "images/comic/spr/spr_com_22.png"
    image spr_com_23_img = "images/comic/spr/spr_com_23.png"
    image spr_com_24_img = "images/comic/spr/spr_com_24.png"
    image spr_com_25_img = "images/comic/spr/spr_com_25.png"
    image spr_com_26_img = "images/comic/spr/spr_com_26.png"

# キャラクター定義
# define vanta_char = Character("", color="#ffffff", window_style='vanta_window', namebox_style="vanta_namebox")
# define wilson_char = Character("", color="#ffffff", window_style='wilson_window', namebox_style="wilson_namebox")
# define zali_char = Character("", color="#ffffff", window_style='zali_window', namebox_style="zali_namebox")
# define vandw_char = Character("", color="#ffffff", window_style='vandw_window', namebox_style="vandw_namebox")
# define wandv_char = Character("", color="#ffffff", window_style='wandv_window', namebox_style="wandv_namebox")
# define vandz_char = Character("", color="#ffffff", window_style='vandz_window', namebox_style="vandz_namebox")
# define zandw_char = Character("", color="#ffffff", window_style='zandw_window', namebox_style="zandw_namebox")
# define vandc_char = Character("", color="#ffffff", window_style='vandc_window', namebox_style="vandc_namebox")
# define npc1_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc01_namebox")
# define npc2_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc02_namebox")
# define npc3_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc03_namebox")
# define npc4_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc04_namebox")
# define npc5_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc05_namebox")
# define npc6_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc06_namebox")




#キャラクターの立ち位置2人の時
transform left_2p:
    xalign 0.0
    yalign 0.2
    zoom 1.1  # 110%の拡大
transform right_2p:
    xalign 0.9
    yalign 0.2
    zoom 1.1  # 110%の拡大

#キャラクターの立ち位置3人の時
transform center:
    xalign 0.5
    yalign 0.2
    zoom 1.1  # 110%の拡大
transform left:
    xalign -0.1
    yalign 0.2
    zoom 1.1  # 110%の拡大
transform right:
    xalign 1.1
    yalign 0.2
    zoom 1.1  # 110%の拡大


# 夏のコミックオーバーレイの配置
transform sum_com_1_upper:
    xalign 0.45 # 中央より左。0.5が中央なので、それより小さな値。
    yalign -0.1 # 中央より上。0.5が中央なので、それより小さな値。
transform sum_com_2_upper:
    xalign 0.5 # 中央より右。0.5が中央なので、それより大きな値。
    yalign 0.1 # 中央より上。0.5が中央なので、それより小さな値。
transform sum_com_4_upper:
    xalign 0.0 # 中央より右。0.5が中央なので、それより大きな値。
    yalign 0.0 # 中央より上。0.5が中央なので、それより小さな値。
transform sum_com_5_upper:
    xalign 0.5 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.05 # 中央より上。0.5が中央なので、それより小さな値。
transform sum_com_6_upper:
    xalign 0.8 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.45 # 中央より上。0.5が中央なので、それより小さな値。
transform sum_com_7_upper:
    xalign 0.1 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.0 # 中央より上。0.5が中央なので、それより小さな値。

# 秋のコミックオーバーレイの配置
transform aut_com_1_upper:
    xalign 0.05 # 中央より左。0.5が中央なので、それより小さな値。
    yalign 0.2 # 中央より上。0.5が中央なので、それより小さな値。
transform aut_com_2_upper:
    xalign 0.95 # 中央より右。0.5が中央なので、それより大きな値。
    yalign 0.4 # 中央より上。0.5が中央なので、それより小さな値。
transform aut_com_3_upper:
    xalign 0.03 # 中央より左。0.5が中央なので、それより小さな値。
    yalign 0.2 # 中央より上。0.5が中央なので、それより小さな値。
transform aut_com_4_upper:
    xalign 0.37 # 中央より右。0.5が中央なので、それより大きな値。
    yalign 0.0 # 中央より上。0.5が中央なので、それより小さな値。
transform aut_com_5_upper:
    xalign 1.0 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.25 # 中央より上。0.5が中央なので、それより小さな値。
transform aut_com_6_upper:
    xalign 0.0 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.0 # 中央より上。0.5が中央なので、それより小さな値。
transform aut_com_7_upper:
    xalign 1.0 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.15 # 中央より上。0.5が中央なので、それより小さな値。
transform aut_com_8_upper:
    xalign 1.0 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.45 # 中央より上。0.5が中央なので、それより小さな値。
transform aut_com_9_upper:
    xalign 0.43 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.2 # 中央より上。0.5が中央なので、それより小さな値。
transform aut_com_10_upper:
    xalign 0.0 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.0 # 中央より上。0.5が中央なので、それより小さな値。

# 冬のコミックオーバーレイの配置
transform win_com_1_upper:
    xalign 0.5 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.0 # 中央より上。0.5が中央なので、それより小さな値。
transform win_com_3_upper:
    xalign 0.5 # 中央。0.5が中央なので、それより大きな値。
    yalign 0.2 # 中央より上。0.5が中央なので、それより小さな値。

# 春のコミックオーバーレイの配置
transform spr_com_upper:
    xalign 0.5 # 中央より左。0.5が中央なので、それより小さな値。
    yalign 0.1 # 中央より上。0.5が中央なので、それより小さな値。


transform earthquake_before:
    xpos 0.5 ypos 0.5
    anchor (0.5, 0.5)
    zoom 1.1

transform earthquake:
    xpos 0.5 ypos 0.5
    anchor (0.5, 0.5)
    zoom 1.1
    linear 0.05 xoffset -10 yoffset -10
    linear 0.05 xoffset 10 yoffset 10
    linear 0.05 xoffset -10 yoffset -10
    linear 0.05 xoffset 10 yoffset 10
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset -10 yoffset -10
    linear 0.05 xoffset 10 yoffset 10
    linear 0.05 xoffset -10 yoffset -10
    linear 0.05 xoffset 10 yoffset 10
    linear 0.05 xoffset 0 yoffset 0

default last_screen = None
default active_set = "set1"  
default active_tab = "tab1"


image 5 = "images/home_image.jpg"

label splashscreen:
    
    show white
    $ renpy.music.play("audio/main_theme.mp3", channel="music", loop=True)
    # Display the video
    $ renpy.movie_cutscene("movies/60 seconds.webm", loops=20, stop_music=False) 
    show white with dissolve
    # show 5 with dissolve
    pause 0.5

    # Hide the image with dissolve
    # hide 5 
    return
image red_dot = "gui/menubutton/red_dot.png" 
image white = "temp/white.jpg"

init python:

    # translate_font("Mandarin", "GlowSansSC-Normal-BRegular.ttf")
    # translate_font("Japanese", "GlowSansSC-Normal-BRegular.ttf")
        


    # achievement.clear_all() ### test if it can init
    class Item(object):
        def __init__(self, name, idle, hover, locked, background):
            self.name = name
            self.idle = idle
            self.hover = hover
            self.locked = locked
            self.background = background
    # Initialize items
    items = ['croissant', 'drink', 'takoyaki', 'walkietalkie', 'mushroom', 'maplesyrup', 'eggplant', 'icecreamcake', 'dietsoda']

    itemlist = {}
    for i in items:
        name = i
        defaultname ="gui/archive/Collected Items/btn/btn_"+name+"_default.png"
        hovername="gui/archive/Collected Items/btn/btn_"+name+"_hover.png"
        lockname = "gui/archive/Collected Items/btn/btn_"+name+"_locked.png"
        popname = "gui/archive/Collected Items/popup_"+name+".png"
        jppopname = "gui/archive/Collected Items/jp/popup_"+name+"_jp.png"
        cnpopname = "gui/archive/Collected Items/cn/popup_"+name+"_cn.png"
        itemlist[i]=[name,
                            defaultname,
                            hovername,
                            lockname,
                            popname,
                            jppopname,
                            cnpopname
        ]
    
    
    ### CGs ###
    cglist = ['sum_cv','sum_st_fny','sum_st_btst','sum_st_bten','sum_st_edcg',
            'aut_cv','aut_st_fny','aut_st_btst','aut_st_bten','aut_st_edcg',
            'win_cv',"win_st_fny",'win_st_btst','win_st_bten','win_st_edcg',
            'spr_cv','spr_st_fny','spr_st_zali','spr_st_wilson','spr_st_edcg']

    sum_cv = Item("sum_cv", 
                    "gui/archive/sum_cv_thu.png",
                    "gui/archive/sum_cv_thu.png",
                    "gui/archive/sum_cv_thu_sil.png",
                    "images/cvisual/sum_cv.png",
    )
    sum_st_fny = Item("sum_st_fny", 
                    "gui/archive/sum_st_fny_thu.png",
                    "gui/archive/sum_st_fny_thu.png",
                    "gui/archive/sum_st_fny_thu_blur.png",
                    "images/still/sum_st_fny.png",
    )
    sum_st_btst = Item("sum_st_btst", 
                    "gui/archive/sum_st_btst_thu.png",
                    "gui/archive/sum_st_btst_thu.png",
                    "gui/archive/sum_st_btst_thu_blur.png",
                    "images/still/sum_st_btst.png",
    )
    sum_st_edcg = Item("sum_st_edcg", 
                    "gui/archive/sum_st_edcg_thu.png",
                    "gui/archive/sum_st_edcg_thu.png",
                    "gui/archive/sum_st_edcg_thu_blur.png",
                    "images/still/sum_st_edcg.png",
    )
    sum_st_bten = Item("sum_st_bten", 
                    "gui/archive/sum_st_bten_thu.png",
                    "gui/archive/sum_st_bten_thu.png",
                    "gui/archive/sum_st_bten_thu_blur.png",
                    "images/still/sum_st_bten.png",
    )
    aut_cv = Item("aut_cv", 
                    "gui/archive/aut_cv_thu.png",
                    "gui/archive/aut_cv_thu.png",
                    "gui/archive/aut_cv_thu_sil.png",
                    "images/cvisual/aut_cv.png",
    )
    aut_st_fny = Item("aut_st_fny", 
                    "gui/archive/aut_st_fny_thu.png",
                    "gui/archive/aut_st_fny_thu.png",
                    "gui/archive/aut_st_fny_thu_sil.png",
                    "images/still/aut_st_fny.png",
    )
    aut_st_btst = Item("aut_st_btst", 
                    "gui/archive/aut_st_btst_thu.png",
                    "gui/archive/aut_st_btst_thu.png",
                    "gui/archive/aut_st_btst_thu_sil.png",
                    "images/still/aut_st_btst.png",
    )
    aut_st_edcg = Item("aut_st_edcg", 
                    "gui/archive/aut_st_edcg_thu.png",
                    "gui/archive/aut_st_edcg_thu.png",
                    "gui/archive/aut_st_edcg_thu_sil.png",
                    "images/still/aut_st_edcg.png",
    )
    aut_st_bten = Item("aut_st_bten", 
                    "gui/archive/aut_st_bten_thu.png",
                    "gui/archive/aut_st_bten_thu.png",
                    "gui/archive/aut_st_bten_thu_sil.png",
                    "images/still/aut_st_bten.png",
    )
    win_cv = Item("win_cv", 
                    "gui/archive/win_cv_thu.png",
                    "gui/archive/win_cv_thu.png",
                    "gui/archive/win_cv_thu_sil.png",
                    "images/cvisual/win_cv.png",
    )
    win_st_fny = Item("win_st_fny", 
                    "gui/archive/win_st_fny_thu.png",
                    "gui/archive/win_st_fny_thu.png",
                    "gui/archive/win_st_fny_thu_blur.png",
                    "images/still/win_st_fny.png",
    )
    win_st_btst = Item("win_st_btst", 
                    "gui/archive/win_st_btst_thu.png",
                    "gui/archive/win_st_btst_thu.png",
                    "gui/archive/win_st_btst_thu_blur.png",
                    "images/still/win_st_btst.png",
    )
    win_st_edcg = Item("win_st_edcg", 
                    "gui/archive/win_st_edcg_thu.png",
                    "gui/archive/win_st_edcg_thu.png",
                    "gui/archive/win_st_edcg_thu_blur.png",
                    "images/still/win_st_edcg.png",
    )
    win_st_bten = Item("win_st_bten", 
                    "gui/archive/win_st_bten_thu.png",
                    "gui/archive/win_st_bten_thu.png",
                    "gui/archive/win_st_bten_thu_blur.png",
                    "images/still/win_st_bten.png",
    )
    spr_cv = Item("spr_cv", 
                    "gui/archive/spr_cv_thu.png",
                    "gui/archive/spr_cv_thu.png",
                    "gui/archive/spr_cv_thu_sil.png",
                    "images/cvisual/spr_cv.png",
    )
    spr_st_fny = Item("spr_st_fny", 
                    "gui/archive/spr_st_fny_thu.png",
                    "gui/archive/spr_st_fny_thu.png",
                    "gui/archive/spr_st_fny_thu_blur.png",
                    "images/still/spr_st_fny.png",
    )
    spr_st_zali = Item("spr_st_zali", 
                    "gui/archive/spr_st_zali_thu.png",
                    "gui/archive/spr_st_zali_thu.png",
                    "gui/archive/spr_st_zali_thu_sil.png",
                    "images/still/spr_st_zali.png",
    )
    spr_st_wilson = Item("spr_st_wilson", 
                    "gui/archive/spr_st_wilson_thu.png",
                    "gui/archive/spr_st_wilson_thu.png",
                    "gui/archive/spr_st_wilson_thu_sil.png",
                    "images/still/spr_st_wilson.png",
    )
    spr_st_edcg = Item("spr_st_edcg", 
                    "gui/archive/spr_st_end_thu.png",
                    "gui/archive/spr_st_end_thu.png",
                    "gui/archive/spr_st_end_thu_sil.png",
                    "images/still/spr_st_edcg.png",
    )
    
    ### claim gallery contents ###  
    sum_gallery_list = {}
    for i in range(15):
        j = i+1
        if j<10:
            name = 'fsk_gall_sum_0'+str(j)

        else:
            name = 'fsk_gall_sum_'+str(j)
        filename ="images/gallery/"+name +".webp"
        lockname = "gui/archive/Secret Snaps/frame_snaps_locked.png"
        sum_gallery_list[j]=[name,
                            filename,
                            filename,
                            lockname,
                            filename
        ]
    aut_gallery_list = {}
    for i in range(14):
        j = i+1
        if j<10:
            name = 'fsk_gall_aut_0'+str(j)

        else:
            name = 'fsk_gall_aut_'+str(j)
        filename ="images/gallery/"+name +".webp"
        lockname ="gui/archive/Secret Snaps/frame_snaps_locked.png"
        aut_gallery_list[j]=[name,
                            filename,
                            filename,
                            lockname,
                            filename
        ]

    spr_gallery_list = {}
    for i in range(13):
        j = i+1
        if j<10:
            name = 'fsk_gall_spr_0'+str(j)

        else:
            name = 'fsk_gall_spr_'+str(j)
        filename ="images/gallery/"+name +".webp"
        lockname = "gui/archive/Secret Snaps/frame_snaps_locked.png"
        spr_gallery_list[j]=[name,
                            filename,
                            filename,
                            lockname,
                            filename
        ]
    win_gallery_list = {}
    for i in range(11):
        j = i+1
        if j<10:
            name = 'fsk_gall_win_0'+str(j)

        else:
            name = 'fsk_gall_win_'+str(j)
        filename ="images/gallery/"+name +".webp"
        lockname = "gui/archive/Secret Snaps/frame_snaps_locked.png"
        win_gallery_list[j]=[name,
                            filename,
                            filename,
                            lockname,
                            filename
        ]

    achievement.register('sum_gallery')
    achievement.register('aut_gallery')
    achievement.register('win_gallery')
    achievement.register('spr_gallery')
    example1 = Item("example", 
                "gui/archive/sum_st_bten_thu.png",
                "gui/archive/sum_st_bten_thu.png",
                "gui/archive/Collected Items/btn/btn_soda_locked.png",
                "images/still/aut_st_bten.png",
    )



    # Try to use achievement to implement the "lock item" function

    achievement.register('croissant')
    achievement.register('drink')
    achievement.register('takoyaki')
    achievement.register('walkietalkie')
    achievement.register('mushroom')
    achievement.register('maplesyrup')
    achievement.register('eggplant')
    achievement.register('icecreamcake')
    achievement.register('dietsoda')

    achievement.register('controlnew')

    # Lock cgs

    for i in range(len(cglist)):
        achievement.register(cglist[i])
    # achievement.clear_all()

    seenlist = {}
    ### popup first see item
    for i in range(9):
        name = "seen_"+str(i)
        seenlist[name] = True


    # Obtain items

    def get_item_background(set_name, tab_name, item_index):
        try:
            background_info = image_button_images[set_name][tab_name][item_index]["background"]
            if tab_name == "gallery" and background_info == "images/still/sum_st_btst.png":
                xpos = image_button_images[set_name][tab_name][item_index]["xpos"]
                ypos = image_button_images[set_name][tab_name][item_index]["ypos"]
                # Adjust xpos and ypos to move the image to the left and up
                new_xpos = xpos - 1000.0  # Move 1 unit to the left
                new_ypos = ypos - 1000.0 # Move 1 unit up
                return (background_info, new_xpos, new_ypos)
            else:
                return background_info  # Default alignment for other tabs
        except KeyError:
            return "Background not available"  # Return a default placeholder image if background is not available

    def get_item_jpbackground(set_name, tab_name, item_index):
        try:
            return image_button_images[set_name][tab_name][item_index]["jpbackground"]
            
        except KeyError:
            return "Background not available"
    def get_item_cnbackground(set_name, tab_name, item_index):
        try:
            return image_button_images[set_name][tab_name][item_index]["cnbackground"]
            
        except KeyError:
            return "Background not available"

    def get_item_name(set_name, tab_name, item_index):
        try:
            return image_button_images[set_name][tab_name][item_index]["name"]
        except KeyError:
            return "Name not available"

    def get_item_locked(set_name, tab_name, item_index):
        try:
            return image_button_images[set_name][tab_name][item_index]["locked"]
        except KeyError:
            return "Name not available"

  
    image_button_images = {
        "set1": {
            "tab1": [
                {"name": itemlist['croissant'][0], "idle": itemlist['croissant'][1], "hover": itemlist['croissant'][2], "locked": itemlist['croissant'][3],"background": itemlist['croissant'][4],"jpbackground": itemlist['croissant'][5],"cnbackground": itemlist['croissant'][6] },
                {"name": itemlist['drink'][0], "idle": itemlist['drink'][1], "hover": itemlist['drink'][2], "locked": itemlist['drink'][3], "background": itemlist['drink'][4],"jpbackground": itemlist['drink'][5],"cnbackground": itemlist['drink'][6] },
                {"name": itemlist['takoyaki'][0], "idle": itemlist['takoyaki'][1], "hover": itemlist['takoyaki'][2], "locked": itemlist['takoyaki'][3], "background": itemlist['takoyaki'][4],"jpbackground": itemlist['takoyaki'][5],"cnbackground": itemlist['takoyaki'][6] },
                {"name": itemlist['walkietalkie'][0], "idle": itemlist['walkietalkie'][1], "hover": itemlist['walkietalkie'][2], "locked": itemlist['walkietalkie'][3], "background": itemlist['walkietalkie'][4],"jpbackground": itemlist['walkietalkie'][5],"cnbackground": itemlist['walkietalkie'][6] },
                {"name": itemlist['mushroom'][0], "idle": itemlist['mushroom'][1], "hover":itemlist['mushroom'][2] , "locked": itemlist['mushroom'][3], "background": itemlist['mushroom'][4],"jpbackground": itemlist['mushroom'][5],"cnbackground": itemlist['mushroom'][6] },
                {"name": itemlist['maplesyrup'][0], "idle": itemlist['maplesyrup'][1], "hover": itemlist['maplesyrup'][2] , "locked": itemlist['maplesyrup'][3], "background": itemlist['maplesyrup'][4],"jpbackground": itemlist['maplesyrup'][5],"cnbackground": itemlist['maplesyrup'][6] },
                {"name": itemlist['eggplant'][0], "idle": itemlist['eggplant'][1], "hover": itemlist['eggplant'][2], "locked": itemlist['eggplant'][3], "background": itemlist['eggplant'][4],"jpbackground": itemlist['eggplant'][5],"cnbackground": itemlist['eggplant'][6] },
                {"name": itemlist['dietsoda'][0], "idle": itemlist['dietsoda'][1], "hover": itemlist['dietsoda'][2] , "locked": itemlist['dietsoda'][3], "background": itemlist['dietsoda'][4],"jpbackground": itemlist['dietsoda'][5],"cnbackground": itemlist['dietsoda'][6] },
                {"name": itemlist['icecreamcake'][0], "idle": itemlist['icecreamcake'][1], "hover": itemlist['icecreamcake'][2] , "locked": itemlist['icecreamcake'][3], "background": itemlist['icecreamcake'][4],"jpbackground": itemlist['icecreamcake'][5],"cnbackground": itemlist['icecreamcake'][6] },
                

            ],
        },
        "gallery": {
            "tab1": [
                {"name": sum_gallery_list[1][0], "idle": sum_gallery_list[1][1], "hover": sum_gallery_list[1][2], "locked": sum_gallery_list[1][3], "background": sum_gallery_list[1][4]},
                {"name": sum_gallery_list[2][0], "idle": sum_gallery_list[2][1], "hover": sum_gallery_list[2][2], "locked": sum_gallery_list[2][3], "background": sum_gallery_list[2][4]},
                {"name": sum_gallery_list[3][0], "idle": sum_gallery_list[3][1], "hover": sum_gallery_list[3][2], "locked": sum_gallery_list[3][3], "background": sum_gallery_list[3][4]},
                {"name": sum_gallery_list[4][0], "idle": sum_gallery_list[4][1], "hover": sum_gallery_list[4][2], "locked": sum_gallery_list[4][3], "background": sum_gallery_list[4][4]},
                {"name": sum_gallery_list[5][0], "idle": sum_gallery_list[5][1], "hover": sum_gallery_list[5][2], "locked": sum_gallery_list[5][3], "background": sum_gallery_list[5][4]},
                {"name": sum_gallery_list[6][0], "idle": sum_gallery_list[6][1], "hover": sum_gallery_list[6][2], "locked": sum_gallery_list[6][3], "background": sum_gallery_list[6][4]},
                {"name": sum_gallery_list[7][0], "idle": sum_gallery_list[7][1], "hover": sum_gallery_list[7][2], "locked": sum_gallery_list[7][3], "background": sum_gallery_list[7][4]},
                {"name": sum_gallery_list[8][0], "idle": sum_gallery_list[8][1], "hover": sum_gallery_list[8][2], "locked": sum_gallery_list[8][3], "background": sum_gallery_list[8][4]},
                {"name": sum_gallery_list[9][0], "idle": sum_gallery_list[9][1], "hover": sum_gallery_list[9][2], "locked": sum_gallery_list[9][3], "background": sum_gallery_list[9][4]},
                {"name": sum_gallery_list[10][0], "idle": sum_gallery_list[10][1], "hover": sum_gallery_list[10][2], "locked": sum_gallery_list[10][3], "background": sum_gallery_list[10][4]},
                {"name": sum_gallery_list[11][0], "idle": sum_gallery_list[11][1], "hover": sum_gallery_list[11][2], "locked": sum_gallery_list[11][3], "background": sum_gallery_list[11][4]},
                {"name": sum_gallery_list[12][0], "idle": sum_gallery_list[12][1], "hover": sum_gallery_list[12][2], "locked": sum_gallery_list[12][3], "background": sum_gallery_list[12][4]},
                {"name": sum_gallery_list[13][0], "idle": sum_gallery_list[13][1], "hover": sum_gallery_list[13][2], "locked": sum_gallery_list[13][3], "background": sum_gallery_list[13][4]},
                {"name": sum_gallery_list[14][0], "idle": sum_gallery_list[14][1], "hover": sum_gallery_list[14][2], "locked": sum_gallery_list[14][3], "background": sum_gallery_list[14][4]},
                {"name": sum_gallery_list[15][0], "idle": sum_gallery_list[15][1], "hover": sum_gallery_list[15][2], "locked": sum_gallery_list[15][3], "background": sum_gallery_list[15][4]},
            ],
            "tab2": [
                {"name": aut_gallery_list[1][0], "idle": aut_gallery_list[1][1], "hover": aut_gallery_list[1][2], "locked": aut_gallery_list[1][3], "background": aut_gallery_list[1][4]},
                {"name": aut_gallery_list[2][0], "idle": aut_gallery_list[2][1], "hover": aut_gallery_list[2][2], "locked": aut_gallery_list[2][3], "background": aut_gallery_list[2][4]},
                {"name": aut_gallery_list[3][0], "idle": aut_gallery_list[3][1], "hover": aut_gallery_list[3][2], "locked": aut_gallery_list[3][3], "background": aut_gallery_list[3][4]},
                {"name": aut_gallery_list[4][0], "idle": aut_gallery_list[4][1], "hover": aut_gallery_list[4][2], "locked": aut_gallery_list[4][3], "background": aut_gallery_list[4][4]},
                {"name": aut_gallery_list[5][0], "idle": aut_gallery_list[5][1], "hover": aut_gallery_list[5][2], "locked": aut_gallery_list[5][3], "background": aut_gallery_list[5][4]},
                {"name": aut_gallery_list[6][0], "idle": aut_gallery_list[6][1], "hover": aut_gallery_list[6][2], "locked": aut_gallery_list[6][3], "background": aut_gallery_list[6][4]},
                {"name": aut_gallery_list[7][0], "idle": aut_gallery_list[7][1], "hover": aut_gallery_list[7][2], "locked": aut_gallery_list[7][3], "background": aut_gallery_list[7][4]},
                {"name": aut_gallery_list[8][0], "idle": aut_gallery_list[8][1], "hover": aut_gallery_list[8][2], "locked": aut_gallery_list[8][3], "background": aut_gallery_list[8][4]},
                {"name": aut_gallery_list[9][0], "idle": aut_gallery_list[9][1], "hover": aut_gallery_list[9][2], "locked": aut_gallery_list[9][3], "background": aut_gallery_list[9][4]},
                {"name": aut_gallery_list[10][0], "idle": aut_gallery_list[10][1], "hover": aut_gallery_list[10][2], "locked": aut_gallery_list[10][3], "background": aut_gallery_list[10][4]},
                {"name": aut_gallery_list[11][0], "idle": aut_gallery_list[11][1], "hover": aut_gallery_list[11][2], "locked": aut_gallery_list[11][3], "background": aut_gallery_list[11][4]},
                {"name": aut_gallery_list[12][0], "idle": aut_gallery_list[12][1], "hover": aut_gallery_list[12][2], "locked": aut_gallery_list[12][3], "background": aut_gallery_list[12][4]},
                {"name": aut_gallery_list[13][0], "idle": aut_gallery_list[13][1], "hover": aut_gallery_list[13][2], "locked": aut_gallery_list[13][3], "background": aut_gallery_list[13][4]},
                {"name": aut_gallery_list[14][0], "idle": aut_gallery_list[14][1], "hover": aut_gallery_list[14][2], "locked": aut_gallery_list[14][3], "background": aut_gallery_list[14][4]},
            ],
            "tab3": [
                {"name": win_gallery_list[1][0], "idle": win_gallery_list[1][1], "hover": win_gallery_list[1][2], "locked": win_gallery_list[1][3], "background": win_gallery_list[1][4]},
                {"name": win_gallery_list[2][0], "idle": win_gallery_list[2][1], "hover": win_gallery_list[2][2], "locked": win_gallery_list[2][3], "background": win_gallery_list[2][4]},
                {"name": win_gallery_list[3][0], "idle": win_gallery_list[3][1], "hover": win_gallery_list[3][2], "locked": win_gallery_list[3][3], "background": win_gallery_list[3][4]},
                {"name": win_gallery_list[4][0], "idle": win_gallery_list[4][1], "hover": win_gallery_list[4][2], "locked": win_gallery_list[4][3], "background": win_gallery_list[4][4]},
                {"name": win_gallery_list[5][0], "idle": win_gallery_list[5][1], "hover": win_gallery_list[5][2], "locked": win_gallery_list[5][3], "background": win_gallery_list[5][4]},
                {"name": win_gallery_list[6][0], "idle": win_gallery_list[6][1], "hover": win_gallery_list[6][2], "locked": win_gallery_list[6][3], "background": win_gallery_list[6][4]},
                {"name": win_gallery_list[7][0], "idle": win_gallery_list[7][1], "hover": win_gallery_list[7][2], "locked": win_gallery_list[7][3], "background": win_gallery_list[7][4]},
                {"name": win_gallery_list[8][0], "idle": win_gallery_list[8][1], "hover": win_gallery_list[8][2], "locked": win_gallery_list[8][3], "background": win_gallery_list[8][4]},
                {"name": win_gallery_list[9][0], "idle": win_gallery_list[9][1], "hover": win_gallery_list[9][2], "locked": win_gallery_list[9][3], "background": win_gallery_list[9][4]},
                {"name": win_gallery_list[10][0], "idle": win_gallery_list[10][1], "hover": win_gallery_list[10][2], "locked": win_gallery_list[10][3], "background": win_gallery_list[10][4]},
                {"name": win_gallery_list[11][0], "idle": win_gallery_list[11][1], "hover": win_gallery_list[11][2], "locked": win_gallery_list[11][3], "background": win_gallery_list[11][4]},
            ],
            "tab4": [
                {"name": spr_gallery_list[1][0], "idle": spr_gallery_list[1][1], "hover": spr_gallery_list[1][2], "locked": spr_gallery_list[1][3], "background": spr_gallery_list[1][4]},
                {"name": spr_gallery_list[2][0], "idle": spr_gallery_list[2][1], "hover": spr_gallery_list[2][2], "locked": spr_gallery_list[2][3], "background": spr_gallery_list[2][4]},
                {"name": spr_gallery_list[3][0], "idle": spr_gallery_list[3][1], "hover": spr_gallery_list[3][2], "locked": spr_gallery_list[3][3], "background": spr_gallery_list[3][4]},
                {"name": spr_gallery_list[4][0], "idle": spr_gallery_list[4][1], "hover": spr_gallery_list[4][2], "locked": spr_gallery_list[4][3], "background": spr_gallery_list[4][4]},
                {"name": spr_gallery_list[5][0], "idle": spr_gallery_list[5][1], "hover": spr_gallery_list[5][2], "locked": spr_gallery_list[5][3], "background": spr_gallery_list[5][4]},
                {"name": spr_gallery_list[6][0], "idle": spr_gallery_list[6][1], "hover": spr_gallery_list[6][2], "locked": spr_gallery_list[6][3], "background": spr_gallery_list[6][4]},
                {"name": spr_gallery_list[7][0], "idle": spr_gallery_list[7][1], "hover": spr_gallery_list[7][2], "locked": spr_gallery_list[7][3], "background": spr_gallery_list[7][4]},
                {"name": spr_gallery_list[8][0], "idle": spr_gallery_list[8][1], "hover": spr_gallery_list[8][2], "locked": spr_gallery_list[8][3], "background": spr_gallery_list[8][4]},
                {"name": spr_gallery_list[9][0], "idle": spr_gallery_list[9][1], "hover": spr_gallery_list[9][2], "locked": spr_gallery_list[9][3], "background": spr_gallery_list[9][4]},
                {"name": spr_gallery_list[10][0], "idle": spr_gallery_list[10][1], "hover": spr_gallery_list[10][2], "locked": spr_gallery_list[10][3], "background": spr_gallery_list[10][4]},
                {"name": spr_gallery_list[11][0], "idle": spr_gallery_list[11][1], "hover": spr_gallery_list[11][2], "locked": spr_gallery_list[11][3], "background": spr_gallery_list[11][4]},
                {"name": spr_gallery_list[12][0], "idle": spr_gallery_list[12][1], "hover": spr_gallery_list[12][2], "locked": spr_gallery_list[12][3], "background": spr_gallery_list[12][4]},   
                {"name": spr_gallery_list[13][0], "idle": spr_gallery_list[13][1], "hover": spr_gallery_list[13][2], "locked": spr_gallery_list[13][3], "background": spr_gallery_list[13][4]},         
                ],
            # Add images for other tabs in gallery here
        },
        "cg": {
            "tab1": [
                {"name": sum_cv.name, "idle": sum_cv.idle, "hover": sum_cv.hover , "locked": sum_cv.locked, "background": sum_cv.background},
                {"name": sum_st_fny.name, "idle": sum_st_fny.idle, "hover": sum_st_fny.hover , "locked": sum_st_fny.locked, "background": sum_st_fny.background},
                {"name": sum_st_btst.name, "idle": sum_st_btst.idle, "hover": sum_st_btst.hover , "locked": sum_st_btst.locked, "background": sum_st_btst.background},
                {"name": sum_st_bten.name, "idle": sum_st_bten.idle, "hover": sum_st_bten.hover , "locked": sum_st_bten.locked, "background": sum_st_bten.background},
                {"name": sum_st_edcg.name, "idle": sum_st_edcg.idle, "hover": sum_st_edcg.hover , "locked": sum_st_edcg.locked, "background": sum_st_edcg.background},
                   
            ],
            "tab2": [
                {"name": aut_cv.name, "idle": aut_cv.idle, "hover": aut_cv.hover , "locked": aut_cv.locked, "background": aut_cv.background},
                {"name": aut_st_fny.name, "idle": aut_st_fny.idle, "hover": aut_st_fny.hover , "locked": aut_st_fny.locked, "background": aut_st_fny.background},
                {"name": aut_st_btst.name, "idle": aut_st_btst.idle, "hover": aut_st_btst.hover , "locked": aut_st_btst.locked, "background": aut_st_btst.background},
                {"name": aut_st_bten.name, "idle": aut_st_bten.idle, "hover": aut_st_bten.hover , "locked": aut_st_bten.locked, "background": aut_st_bten.background},
                {"name": aut_st_edcg.name, "idle": aut_st_edcg.idle, "hover": aut_st_edcg.hover , "locked": aut_st_edcg.locked, "background": aut_st_edcg.background},
                
            ],
            "tab3": [
                {"name": win_cv.name, "idle": win_cv.idle, "hover": win_cv.hover , "locked": win_cv.locked, "background": win_cv.background},
                {"name": win_st_fny.name, "idle": win_st_fny.idle, "hover": win_st_fny.hover , "locked": win_st_fny.locked, "background": win_st_fny.background},
                {"name": win_st_btst.name, "idle": win_st_btst.idle, "hover": win_st_btst.hover , "locked": win_st_btst.locked, "background": win_st_btst.background},
                {"name": win_st_bten.name, "idle": win_st_bten.idle, "hover": win_st_bten.hover , "locked": win_st_bten.locked, "background": win_st_bten.background},
                {"name": win_st_edcg.name, "idle": win_st_edcg.idle, "hover": win_st_edcg.hover , "locked": win_st_edcg.locked, "background": win_st_edcg.background},
                
            ],
            "tab4": [
                {"name": spr_cv.name, "idle": spr_cv.idle, "hover": spr_cv.hover , "locked": spr_cv.locked, "background": spr_cv.background},
                {"name": spr_st_wilson.name, "idle": spr_st_wilson.idle, "hover": spr_st_wilson.hover , "locked": spr_st_wilson.locked, "background": spr_st_wilson.background},
                {"name": spr_st_zali.name, "idle": spr_st_zali.idle, "hover": spr_st_zali.hover , "locked": spr_st_zali.locked, "background": spr_st_zali.background},
                {"name": spr_st_fny.name, "idle": spr_st_fny.idle, "hover": spr_st_fny.hover , "locked": spr_st_fny.locked, "background": spr_st_fny.background},
                {"name": spr_st_edcg.name, "idle": spr_st_edcg.idle, "hover": spr_st_edcg.hover , "locked": spr_st_edcg.locked, "background": spr_st_edcg.background},
                

            ],
            # Add images for other tabs in cg here
        }
    }
    
    

default zorder = -2
default red_dot_shown = False
default havetakoyaki = False
default showItem = -1 #this is for option 2
default persistent.achievement_popup_shown = False # this is for option 1
default persistent.croissant = False
default persistent.drink = False
default persistent.takoyaki = False
default persistent.walkietalkie = False
default persistent.mushroom = False
default persistent.maplesyrup = False
default persistent.eggplant = False
default persistent.dietsoda = False
default persistent.icecreamcake = False

default current_ch = 0


# ### achievement package ###
# if (achievement.has('sum_st_edcg')== False):
#     $ achievement.grant('sum_st_edcg')
#     $ achievement.grant('sum_gallery')        
#     show screen OverlayScreen1
#     show screen ClickableArea
#     python:
#
# ### achievement package ###
# ### ending screen ###
# show screen OverlayScreen

# ### obtain stuff in archive ###
# $ achievement.grant('croissant')





label start:
    $ achievement.clear_all()
    $ persistent._clear()
    $ renpy.clear_retain()
    $ renpy.restart_interaction() 
    
    jump chapter_1 
    return
label after_load:
    if (_preferences.language == "japanese"):
        style vanta_namebox:
            background "gui/gui/jp/ui_namebox_vanta_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style wilson_namebox:
            background "gui/gui/jp/ui_namebox_wilson_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style zali_namebox:
            background "gui/gui/jp/ui_namebox_zali_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandw_namebox:
            background "gui/gui/jp/ui_namebox_v&w_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style wandv_namebox:
            background "gui/gui/jp/ui_namebox_w&v_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandz_namebox:
            background "gui/gui/jp/ui_namebox_z&v_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style zandw_namebox:
            background "gui/gui/jp/ui_namebox_z&w_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandc_namebox:
            background "gui/gui/jp/ui_namebox_v&c_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる
        style npc01_namebox:
            background "gui/gui/jp/ui_namebox_npc03_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc02_namebox:
            background "gui/gui/jp/ui_namebox_npc02_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc03_namebox:
            background "gui/gui/jp/ui_namebox_npc01_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc04_namebox:
            background "gui/gui/jp/ui_namebox_npc04_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc05_namebox:
            background "gui/gui/jp/ui_namebox_npc05_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc06_namebox:
            background "gui/gui/jp/ui_namebox_npc06_jp.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる
    elif (_preferences.language == "mandarin"):
        style vanta_namebox:
            background "gui/gui/ui_namebox_vanta.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style wilson_namebox:
            background "gui/gui/ui_namebox_wilson.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style zali_namebox:
            background "gui/gui/ui_namebox_zali.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandw_namebox:
            background "gui/gui/ui_namebox_v&w.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style wandv_namebox:
            background "gui/gui/ui_namebox_w+v.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandz_namebox:
            background "gui/gui/ui_namebox_v&z.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style zandw_namebox:
            background "gui/gui/ui_namebox_z&w.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandc_namebox:
            background "gui/gui/ui_namebox_v&c.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる
        
        style npc01_namebox:
            background "gui/gui/cn/ui_namebox_npc03_cn.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc02_namebox:
            background "gui/gui/cn/ui_namebox_npc02_cn.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc03_namebox:
            background "gui/gui/cn/ui_namebox_npc01_cn.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc04_namebox:
            background "gui/gui/cn/ui_namebox_npc04_cn.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc05_namebox:
            background "gui/gui/cn/ui_namebox_npc05_cn.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc06_namebox:
            background "gui/gui/cn/ui_namebox_npc06_cn.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

    else:
        style vanta_namebox:
            background "gui/gui/ui_namebox_vanta.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style wilson_namebox:
            background "gui/gui/ui_namebox_wilson.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style zali_namebox:
            background "gui/gui/ui_namebox_zali.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandw_namebox:
            background "gui/gui/ui_namebox_v&w.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style wandv_namebox:
            background "gui/gui/ui_namebox_w+v.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandz_namebox:
            background "gui/gui/ui_namebox_v&z.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style zandw_namebox:
            background "gui/gui/ui_namebox_z&w.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style vandc_namebox:
            background "gui/gui/ui_namebox_v&c.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる
        style npc01_namebox:
            background "gui/gui/ui_namebox_npc01.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc02_namebox:
            background "gui/gui/ui_namebox_npc02.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc03_namebox:
            background "gui/gui/ui_namebox_npc03.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc04_namebox:
            background "gui/gui/ui_namebox_npc04.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc05_namebox:
            background "gui/gui/ui_namebox_npc05.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる

        style npc06_namebox:
            background "gui/gui/ui_namebox_npc06.png"
            xalign 0.135
            xoffset 2 # これはピクセル単位での指定です。
            yalign 1.0  # ネームボックスを画面の下端に配置することを意味する
            yoffset -285  # ネームボックスをピクセル単位で上に移動させる
        define vanta_char = Character("", color="#ffffff", window_style='vanta_window', namebox_style="vanta_namebox")
        define wilson_char = Character("", color="#ffffff", window_style='wilson_window', namebox_style="wilson_namebox")
        define zali_char = Character("", color="#ffffff", window_style='zali_window', namebox_style="zali_namebox")
        define vandw_char = Character("", color="#ffffff", window_style='vandw_window', namebox_style="vandw_namebox")
        define wandv_char = Character("", color="#ffffff", window_style='wandv_window', namebox_style="wandv_namebox")
        define vandz_char = Character("", color="#ffffff", window_style='vandz_window', namebox_style="vandz_namebox")
        define zandw_char = Character("", color="#ffffff", window_style='zandw_window', namebox_style="zandw_namebox")
        define vandc_char = Character("", color="#ffffff", window_style='vandc_window', namebox_style="vandc_namebox")
        define npc1_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc01_namebox")
        define npc2_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc02_namebox")
        define npc3_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc03_namebox")
        define npc4_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc04_namebox")
        define npc5_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc05_namebox")
        define npc6_char = Character("", color="#ffffff", window_style='npc_window', namebox_style="npc06_namebox")
    return


label chapter_1:
    $ current_ch = 1
    stop music fadeout 1.0  # Fade out the menu music
    play music "audio/sum/sum_bgm_01.mp3" loop fadein 1.0  # Loop game music with fade in

    show sum_cv_img
    $ achievement.grant('sum_cv')
    # Wait for user to click
    pause

    scene sum_bg_beach1_img
    # show text "{b}{size=34}Chapter 1.  SUMMER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    play sound "audio/sum/sum_se_waves_01.mp3" #The Sound of Waves

    window hide
    show van_sum_nor at center
    with fade
    vanta_char "3, 2, 1 ! Touchdown!"
    hide van_sum_nor
    show van_sum_hap at center
    "You are Vantacrow Bringer, fearsome tyrant and ace of the hero team Krisis."
    stop sound fadeout 3.0  #Stop sound effects
    "Ever since becoming a hero, you've been working tirelessly.\nYou save civilians, fight bad guys and say stuff like \"Crazy dayo\" or \"We ball!\""
    vanta_char "My first summer vacation has finally started!"
    vanta_char "My friends recommended this small local beach, it looks just as nice as they said."
    hide van_sum_hap
    show van_sum_nor at center
    "The air is filled with a fresh sea-side breeze, and the hustle and bustle of people enjoying the summer."
    "Further along, there's a trendy drink shop that catches everyone's attention with its visually captivating beverages."
    "As you stroll along the lively beach, you spot a souvenir shop ahead—"
    hide van_sum_nor
    show van_sum_thi at center
    vanta_char "Oh? Is that a souvenir shop?"
    vanta_char "On god on god, for real for real?"
    hide van_sum_thi
    show van_sum_nor at center
    "Seeing the shop, you think about your teammates."
    "You wonder if you should take a look inside to see if there's anything worth buying."
    menu:
        "Enter the Souvenir Shop":
            play sound "audio/sum/sum_se_bell.mp3"  #Bell sounds
            jump cho_one1_accepted
    label cho_one1_accepted:
       
    scene sum_bg_shop1_img
    # show text "{b}{size=34}Chapter 1.  SUMMER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    show van_sum_nor at center
    with fade
    "You browse through the shop and spot a cute croissant-shaped keychain."
    play sound "audio/sum/sum_se_cash.mp3" #Cash register sound
    "You pay for it at the register, but as you are about to leave, you hear a shout from the other side of the shop."
    ### achievement package ###
    if (achievement.has('croissant')== False):
        $ achievement.grant('croissant')        
        show screen OverlayScreen1
        show screen ClickableArea
        play sound "audio/collected_item_ping.mp3"
        python:
            active_set = "set1"
            active_tab ="tab1"
            showItem = 0 # this is for option 2
            seenlist['seen_0'] = False # this is for option 2
        $ achievement.grant('controlnew') # this is for option 2
    ### achievement package ###
    hide van_sum_nor
    show van_sum_thi at center
    show npc2_img at left
    npc2_char "Are you out of your mind? Clearly, this is chicken!"
    show npc3_img at right
    npc3_char "Are you crazy? Does that look edible to you? That's iron!"
    hide van_sum_thi
    show van_sum_ser at center
    vanta_char "Hey hey hey, chill!"
    vanta_char "This is a public space, don't yell like that."
    vanta_char "You should know not to eat iron, alright? We're done here."
    npc2_char "Oh, I'm so sorry. I've been agitated all day. This place is just...driving me crazy."
    npc3_char "Yeah, me too... Sorry for yelling at you..."
    hide van_sum_ser
    show van_sum_nor at center 
    vanta_char "Good. Now you two can just keep calm, and enjoy the rest of your day!" 
    hide npc2_img
    hide npc3_img
    with dissolve
    "You send the couple on their way and check in with the shopkeeper to make sure there are no more problems."
    show npc1_img at left_2p
    show van_sum_nor at right_2p
    with dissolve
    npc1_char "Thank you for stepping in before it got worse; I was worried that you would cause trouble, too."
    npc1_char "Phew! I'm glad my assumptions were wrong. You appeared from nowhere, just like a hero!"
    hide van_sum_nor
    show van_sum_con at right_2p
    vanta_char "Haha! To tell you the truth, I am an incredibly influential individual, the true paragon of virtue. Standing before you is—"
    "The shopkeeper isn't paying attention to your glorious self introduction."
    hide van_sum_con
    show van_sum_nor at right_2p
    "Instead she sighs and starts to talk about the recent events."
    hide van_sum_nor
    show van_sum_thi at right_2p
    npc1_char "I've seen a lot more people come to this beach. For some reason, they're getting out of control. Fights like today are happening more and more."
    vanta_char "Did you notice anything that could be causing the fighting?"
    hide van_sum_thi
    show van_sum_nor at right_2p
    npc1_char "I haven't had time to investigate, but something in my gut says it has to do with the new drinks shop, Octa-Brew."
    npc1_char "I love this place, and I wish everyone could enjoy the beautiful beach in peace..."
    hide van_sum_nor
    show van_sum_con at right_2p
    vanta_char "Thanks for all the info, I'll go check it out."
    menu:
        "Exit the Souvenir Shop":
            play sound "audio/sum/sum_se_bell.mp3"  #Bell sounds
            jump cho_one2_accepted
    label cho_one2_accepted:
    
    scene sum_bg_shop2_img
    # show text "{b}{size=34}Chapter 1.  SUMMER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with fade
    
    play sound "audio/sum/sum_se_sand_01.mp3"  #Sound of walking on sand
    show van_sum_nor at center
    "You walk further down the beach and see a crowd outside of Octa-Brew. You decide to join the queue."
    stop sound
    vanta_char "The shopkeeper was right, this place is popular."

    menu:
        "Check the menu":
            play sound "audio/sum/sum_se_paper.mp3"  #Sound of flipping through menus
            jump cho_one3_accepted
    label cho_one3_accepted:

    "You order a purple drink from the menu that reminds you of a dear friend."
    "After you get your order you decide to—"
    menu:
        "Resist curiosity and not take a sip":
            vanta_char "I don't want to get told off for messing with the samples again, better not taste this."
            "You decide to be careful and send the drink to A.S.H. for analysis."
            hide van_sum_nor
            jump JXJX_accepted
        "We ball! Take a sip of the drink":
            "You've defeated 100,000 armed combatants without breaking a sweat, what's the worst that could happen?"
            "You taste the drink...and nothing happens"
            hide van_sum_nor
            show van_sum_hap at center
            vanta_char "Huh. It actually tastes quite nice. Esperanza!"
            "Since it tastes so good and nothing happened, you decide to keep this one for yourself, and order another one to send to A.S.H. for analysis."
            ### achievement package ###
            if (achievement.has('drink')== False):
                $ achievement.grant('drink')        
                show screen OverlayScreen1
                show screen ClickableArea
                play sound "audio/collected_item_ping.mp3"
                python:
                    active_set = "set1"
                    active_tab = "tab1"
                    showItem = 1
                    seenlist['seen_1'] = False
                $ achievement.grant('controlnew') 
            ### achievement package ###
            hide van_sum_hap
            jump JXJX_accepted
    label JXJX_accepted:
    
    show van_sum_hap at center
    vanta_char "I shall receive the analysis result soon.\nNow I can enjoy the rest of the day relaxing in the sun, getting vitamin D."

    # Screen fades to black once, then fades back in
    scene black
    # show text "{b}{size=34}Chapter 1.  SUMMER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with fade
    pause(0.3)  # Wait a bit while the screen is dark
    scene sum_bg_beach1_img
    # show text "{b}{size=34}Chapter 1.  SUMMER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    show van_sum_nor at center
    with fade
    "The next day, you receive the analysis report from A.S.H."
    hide van_sum_nor
    show van_sum_sur at center
    "To your surprise, the investigation uncovered a troubling connection—"
    "A pharmaceutical company is the supplier of the drinks."
    vanta_char "A pharmaceutical company? That can't be good!"
    vanta_char "I should find out more, something seems fishy."

    menu:
        "Go to Octa-Brew":
            play sound "audio/sum/sum_se_sand_01.mp3"  #Sound of walking on sand
            jump cho_one4_accepted
    label cho_one4_accepted:
    
    scene sum_bg_shop2_img
    # show text "{b}{size=34}Chapter 1.  SUMMER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    stop sound
    show van_sum_ser at center
    with fade
    vanta_char "I'm Special Agent Vantacrow Bringer from A.S.H. Mind if I take a look at your kitchen?"
    "The clerk seems shocked and starts to panic. They grab a bottle of unknown substance and run away."
    hide van_sum_ser
    show van_sum_sur at center
    vanta_char " {size=40}Hey, hey! Where do you think you're going?{/size}"

    play sound "audio/sum/sum_se_sand_02.mp3"  #Sound of running on sand
    scene sum_bg_beach3_img
    # show text "{b}{size=34}Chapter 1.  SUMMER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    show van_sum_ser at center
    with dissolve
    "You chase after them, but the clerk, desperate to erase evidence, tosses the bottle into the ocean."
    play sound "audio/sum/sum_se_bochan.mp3" #The sound of something sinking into the water. Bo-chan.
    "You tackle the clerk to the ground. As you click the handcuffs onto their wrists, you watch the bottle disappear into the waves."

    play sound "audio/sum/sum_se_tako_01.mp3" # Octopus Cry
    play music "audio/sum/sum_bgm_02.mp3" loop   # Loop game music
    "All of a sudden, the waves in the sea start to thrash violently as a giant octopus rises from the water."

    scene sum_st_btst_img
    # show text "{b}{size=34}Chapter 1.  SUMMER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with fade
    pause 2.0 
    vanta_char "{size=40}Holy guacamole! {/size}That thing is massive! What the frick frack snick snack?"
    play sound "audio/sum/sum_se_tako_04.mp3"
    "The giant octopus lets out an ear-piercing roar. People begin to flee in a panic."
    "Faced with this unexpected threat, you make a prompt decision to—"
    ### achievement package ###
    if (achievement.has('sum_st_btst')== False):
        $ achievement.grant('sum_st_btst')          
        # show screen OverlayScreen1
        # show screen ClickableArea
        python:
            active_set = "cg"
            active_tab = "tab1"

    ### achievement package ###

    scene sum_bg_beach2_img
    # show text "{b}{size=34}Chapter 1.  SUMMER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    show van_sum_ser at center
    with fade
    menu:
        "Run towards the ferocious octopus and fight":
            jump BT1_accepted
        "Evacuate the area first":
            "You notice a small child who tripped and is crying on the ground. You quickly scoop her into your arms and bring her to a safe spot."
            "Once there are no civilians in the immediate vicinity, you run towards the ferocious octopus."
            python:
                havetakoyaki = True
            jump BT1_accepted
    label BT1_accepted:
    vanta_char "Did the octopus just drink whatever was in the bottle? That must be what's driving people crazy!"

    hide van_sum_ser
    show van_sum_con at center
    vanta_char "You're cooked! You're done! I'm the cook and I'm about to have takoyaki tonight!"
    "The octopus has no intention of becoming your dinner tonight."
    play sound "audio/sum/sum_se_tako_02.mp3"  #Sound of tentacles attacking
    "It hurtles one of its tentacles towards you."
    "Reacting immediately, you jump to the—"
    menu:

        "Left":
            play sound "audio/sum/sum_se_koke.mp3" #Cocking sound
            scene sum_st_fny_img
            # show text "{b}{size=34}Chapter 1.  SUMMER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
            with fade
            pause 2.0 
            "You trip over a particularly large shell lying innocently in the sand and fall to the ground rather ungracefully."
            play sound "audio/sum/sum_se_fanfan.mp3" #Sloppy fanfare
            "The screech you let out was so unfitting of your appearance that even the octopus was too stunned to speak."
            "Embarrassed, you quickly stand up and brush the sand off you."
            pause 0.5
            ### achievement package ###
            if (achievement.has('sum_st_fny')== False):
                $ achievement.grant('sum_st_fny')        
                # show screen OverlayScreen1
                # show screen ClickableArea
                python:
                    active_set = "cg"
                    active_tab = "tab1"
            ### achievement package ###
            scene sum_bg_beach2_img
            # show text "{b}{size=34}Chapter 1.  SUMMER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
            with fade
            show van_sum_emb at center
            vanta_char "{size=50}Ahem!! Moving on!{/size}"
            "Moving swiftly on from your embarrassing performance, you give a war cry."
            hide van_sum_emb
            jump after_accepted

        "Right":
            hide van_sum_con
            show van_sum_hap at center
            vanta_char "{size=50}AH HA! {/size}This is too easy! I'm always right!"
            "Grinning with excitement, you spin around, waving a hand to get the octopus' attention, then sprint off with a shout."
            hide van_sum_hap
            jump after_accepted

    label after_accepted:

    show van_sum_con at center
    "You run further along the beach, leading the octopus away from people."
    "It chases you, swinging its arms."
    hide van_sum_con
    show com_base_img
    show sum_com_1_img at sum_com_1_upper
    play sound "audio/sum/sum_se_tako_03.mp3" #Sound of tentacles attacking
    "A limb wraps around your leg and pulls you up in the air."
    hide sum_com_1_img
    show sum_com_2_img at sum_com_2_upper
    "Hanging upside down, you see the octopus' blood-red eyes staring right at you."
    "To your luck, and the octopus' grief, you are no ordinary human."
    "You gain a huge burst of strength."
    "You twist your body upwards, punching hard into the tentacles, pushing them back."
    play sound "audio/sum/sum_se_kougeki_01.mp3" #Attack sound
    hide sum_com_2_img
    show sum_com_3_img at sum_com_2_upper
    vanta_char "{size=50}PARCAW !{/size}"
    "You parkour through the other waving limbs to get closer to the octopus' body."
    show sum_com_4_img at sum_com_4_upper
    "With each forceful stomp on the arms, they drop to the ground, paralyzed."
    hide sum_com_3_img
    hide sum_com_4_img
    show sum_com_5_img at sum_com_2_upper
    play sound "audio/sum/sum_se_kougeki_02.mp3" #Attack sound
    "In the final sprint, you somersault kick right between its eyes with all your might."
    hide sum_com_5_img
    show sum_com_6_img at sum_com_6_upper 
    "The massive force destroys the octopus' head."
    show sum_com_7_img at sum_com_7_upper 
    "Your body bounces back in the air from the kick."
    "It was graceful, magnificent, breathtaking even."
    play sound "audio/sum/sum_se_syakin.mp3" #Sound of posing
    hide sum_com_6_img
    hide sum_com_7_img
    show sum_com_8_img at sum_com_2_upper 
    "You land in a superhero pose, of course."
    play sound "audio/sum/sum_se_cheer.mp3" #cheer
    "You can hear people clapping in the back."
    "Now that the exciting battle is over, you look back at the octopus. It has stopped moving."
    play music "audio/sum/sum_bgm_01.mp3" loop fadein 1.0   # Loop game music
    scene sum_st_bten_img
    # show text "{b}{size=34}Chapter 1.  SUMMER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with fade
    pause 2.0 
    vanta_char "Well, that's my workout done for today, nice!"
    ### achievement package ###
    if (achievement.has('takoyaki')== False) and (havetakoyaki == True):
        $ achievement.grant('takoyaki')        
        show screen OverlayScreen1
        show screen ClickableArea
        python:
            active_set = "set1"
            active_tab = "tab1"
            showItem = 2
            seenlist['seen_2'] = False
        $ achievement.grant('controlnew') 
        play sound "audio/collected_item_ping.mp3"
    ### achievement package ###
    "A.S.H. personnel arrive with the freshly developed antidotes. You see the agents handing them out to the people who were affected by the drinks."
    "Everyone on the beach, including the shopkeeper, expresses their thanks to you and the A.S.H. team for averting disaster."
    pause 0.5
    ### achievement package ###
    if (achievement.has('sum_st_bten')== False):
        $ achievement.grant('sum_st_bten')         
        # show screen OverlayScreen1
        # show screen ClickableArea
        python:
            active_set = "cg"
            active_tab = "tab1"
    ### achievement package ###
    scene sum_bg_beach3_img
    # show text "{b}{size=34}Chapter 1.  SUMMER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    show van_sum_hap at center
    with fade
    vanta_char "Everyone's safe now. We can once again enjoy the beautiful beach in peace."
    "You see the smile on everyone's face. The happiness of saving them all filled your heart. Just another day; you never get tired of it."
    hide van_sum_hap
    show van_sum_con at center
    vanta_char "Well, that was certainly one way for my vacation to go."
    "Your adventure has only just begun, and the world awaits your epic journey—"

    show sum_edcg_img
    with fade
    pause 1.5
    ### achievement package ###
    if (achievement.has('sum_st_edcg')== False) or(achievement.has('sum_gallery')== False):
        $ achievement.grant('sum_st_edcg')
        $ achievement.grant('sum_gallery')        
        show screen OverlayScreen1
        show screen ClickableArea
        python:
            active_set = "gallery"
            active_tab = "tab1"
        # add a popup screen?
        play sound "audio/collected_item_ping.mp3"
        
    ### achievement package ###
    # show text "{b}{size=34}Chapter 1.  SUMMER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    ### ending screen ###
    python:
        active_set = "gallery"
        active_tab = "tab1"
    show screen OverlayScreen

    if _preferences.language == 'mandarin':
        show screen chapterend_popup("恭喜！We ball！")
    elif _preferences.language == 'japanese':
        show screen chapterend_popup("We Ball! よく出来ましたね！")
    else:
        show screen chapterend_popup("Congratulations! We ball!")
    # Wait until the user clicks
    pause
    call chapter_2 from _call_chapter_2

label chapter_2:
    hide screen OverlayScreen
    hide screen chapterend_popup

    python:
        current_ch = 2
        active_set="cg"
        active_tab="tab2"
    stop music fadeout 1.0  # Fade out menu music
    play music "audio/aut/aut_bgm_01.mp3" loop fadein 1.0  #Loop playback of peaceful songs with fade-in
    show aut_cv_img
    $ achievement.grant('aut_cv')
    # Wait until the user clicks
    pause
 
    scene aut_bg_village1_img
    # show text "{b}{size=34}Chapter 2.  AUTUMN{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with fade
    play sound "audio/aut/aut_se_bird.mp3" #birdcall

    window hide

    "Krisis has been deployed on a new assignment. You, Zali and Wilson embark on the mission. After a short travel, you arrive at your destination. It's a quiet, cozy village located in the mountains."
    "The village leader is expecting you upon your arrival."
    show npc4_img at center
    npc4_char "Welcome to the village, you must be Krisis! I'm so glad you came quickly. I'm the leader of this village."
    hide npc4_img
    show van_ci_nor at center
    stop sound fadeout 3.0 #Stop sound effects
    vanta_char "Of course! We need no introduction. But regardless, my name is Vantacrow Bringer. Here to save you all."
    show zal_ci_nor at left
    zali_char "It's our pleasure to meet you. I'm Vezalius Bandage, the medic hero of our team Krisis."
    show wil_ci_nor at right
    wilson_char "We come when you call! I'm Yu Q. Wilson, the most talented hero of our team."
    hide zal_ci_nor
    show zal_ci_hap at left
    zali_char "Um, anyway, this is a lovely village."
    hide wil_ci_nor
    hide van_ci_nor
    hide zal_ci_hap
    show npc4_img at center 
    npc4_char "Absolutely, especially this time of year; look at how beautiful the mountains are!"
    scene aut_bg_village2_img
    # show text "{b}{size=34}Chapter 2.  AUTUMN{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with fade
    "As you discuss the details of the mission, the village leader guides you to the town hall."
    show npc4_img at center
    npc4_char "Our village has always had a good mushroom business. However, this year we have a big quota to fill. So, we decided to venture further up the mountains."
    npc4_char "While the team was foraging the mushrooms, they were attacked by some oddly aggressive bears, which had never happened before."
    show npc4_img at left_2p
    hide zal_ci_nor
    show zal_ci_sur at right_2p
    with dissolve
    zali_char "Gosh! That is terrible! Was anyone hurt?"
    npc4_char "Yes, there were some injuries, the bears spooked a few. They're resting in the infirmary over there."
    "The village leader points to a door across the room."
    hide zal_ci_sur
    show wil_ci_hap at right_2p
    wilson_char "You can trust Zali! They'll be in good hands."
    hide wil_ci_hap
    show zal_ci_nor at right_2p
    zali_char "Alright! You can count on us."
    hide zal_ci_nor
    show van_ci_con at right_2p
    vanta_char "Let's get ready and head out before it gets dark. We need to investigate."
    hide van_ci_con
    hide npc4_img
    
    scene black
    # show text "{b}{size=34}Chapter 2.  AUTUMN{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with fade
    scene aut_bg_village1_img
    # show text "{b}{size=34}Chapter 2.  AUTUMN{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    show wil_hr_nor at right
    show van_hr_nor at left
    with fade
    play sound "audio/aut/aut_se_clothes.mp3" #Change into a hero costume
    "You all decide to gear up for the mission. Meanwhile, you spot Wilson slipping a taser gun in his belt. You raise an eyebrow and stare at him."
    hide van_hr_nor
    show van_hr_3 at left
    vanta_char "You're not bringing your sword? Feeling confident?"
    hide wil_hr_nor
    show wil_hr_sur at right
    wilson_char "It's just a bear, there's no job I can't do!"
    hide van_hr_3
    show van_hr_con at left
    vanta_char "Look, I'm just saying, what if—"
    hide van_hr_con
    hide wil_hr_sur
    show wil_hr_nor at right
    show van_hr_nor at left 
    show zal_hr_hap at center
    zali_char "Alright alright! Come on guys, let's focus on the mission!"
    "Zali interrupts you and Wilson as he tosses you two walkie-talkies.\nYou catch them and pass one to Wilson."
    ### achievement package ###
    if (achievement.has('walkietalkie')== False):
        $ achievement.grant('walkietalkie')        
        show screen OverlayScreen1
        show screen ClickableArea
        python:
            active_set = "set1"
            active_tab = "tab1"
            showItem = 3
            seenlist['seen_3'] = False
        $ achievement.grant('controlnew') 
        play sound "audio/collected_item_ping.mp3"
    ### achievement package ###
    hide zal_hr_hap
    show zal_hr_nor at center
    zali_char "I'll stay behind and look after the people who were attacked."
    hide zal_hr_nor
    show zal_hr_ser at center
    zali_char "Be careful, don't die—if you do, then I can't heal you."
    "You give Zali a quick nod as he heads to the infirmary. You and Wilson turn towards the mountains."
    play sound "audio/aut/aut_se_bird.mp3" #birdcall   
    scene aut_bg_forest1_img
    # show text "{b}{size=34}Chapter 2.  AUTUMN{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with fade
    "The two of you hike along the path, taking in the surrounding scenery."
    "Everything is breathtaking—from the towering trees, to the crunching of the leaves underfoot, to the crisp autumn air."
    stop sound fadeout 3.0 #Stop sound effects
    show wil_hr_nor at right
    show van_hr_nor at left
    with fade
    "You take a deep breath."
    hide van_hr_nor
    show van_hr_hap at left
    vanta_char "The air is so fresh today. I love this time of year."
    wilson_char "Yeah. You're right, this is so beautiful. "
    hide wil_hr_nor
    show wil_hr_hap at right
    wilson_char "Do you remember that time we went to a forest to hunt down Bigfoot with Alban and Fulgur? You were princess carried the whole way during the mission. That was actually so funny. Ah-hahahah."
    wilson_char "Oh! And we had a group pee together! Actually... I don't want to be reminded of how Fulgur slapped my ass."
    hide van_hr_hap
    show van_hr_sur at left
    hide wil_hr_hap
    show wil_hr_nor at right
    vanta_char "Hmm, hold on... What's that smell?"
    "The scent is familiar, it's something earthy."
    "Intrigued by the smell, you want to find out where it's coming from."
    scene aut_bg_forest2_img
    # show text "{b}{size=34}Chapter 2.  AUTUMN{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with dissolve
    "You head off the path, and Wilson's yapping voice slowly fades behind you."
    show van_hr_nor at center
    "After a few minutes of walking, you find a cluster of amethyst-colored mushrooms."
    "You pick one up and—"
    menu:
        "Give it a sniff":
            hide van_hr_nor
            show van_hr_thi at center
            "You give it a sniff and decide that it's too risky to keep it. You drop the mushroom where you found it."
            hide van_hr_thi
            jump aut_cho01_accepted
        "Take a small bite":
            vanta_char "Hmm, the taste is familiar, I wish I could remember where I had it."
            hide van_hr_nor
            show van_hr_hap at center
            vanta_char "I like it though, I should grab some more! "
            "You grab a few more mushrooms, and put them in your pouch."
            ### achievement package ###
            if (achievement.has('mushroom')== False):
                $ achievement.grant('mushroom')        
                show screen OverlayScreen1
                show screen ClickableArea
                python:
                    active_set="set1"
                    active_tab="tab1"
                    showItem = 4
                    seenlist['seen_4'] = False
                $ achievement.grant('controlnew') 
                play sound "audio/collected_item_ping.mp3"
            ### achievement package ###
            hide van_hr_hap
            jump aut_cho01_accepted
    label aut_cho01_accepted:

    show van_hr_sur at center
    "Looking around, you don't recongize your surroundings."
    "You try to find the path you came from, but you can't see it. Yeah... You're lost."
    hide van_hr_sur
    show van_hr_nor at center
    "Realizing that you left Wilson behind, you take out your walkie-talkie and turn it on."
    play sound "audio/aut/aut_se_transceiver.mp3" #Transceiver sound
    show van_hr_nor at left
    show aut_bg_forest3_img
    show wil_hr_nor at right
    with dissolve
    wilson_char "Hello? Hello? Can you hear me? This is Wilson speaking. Over."
    wilson_char "Mr. Bringer, do you copy? Over."
    vanta_char "Hello? Wilson? This is Vantacrow Bringer. Over."
    hide van_hr_nor
    show van_hr_con at left
    hide aut_bg_forest3_img
    show aut_bg_forest3_img
    hide wil_hr_nor
    show wil_hr_nor at right
    vanta_char "You see, there's this small situation I'm in. I may or may not be lost, I'm not sure where I am. Over." 
    play sound "audio/aut/aut_se_transceiver.mp3" #Transceiver sound
    hide wil_hr_nor
    show wil_hr_sur at right
    wilson_char "Vanta, Vanta, Vanta... I look away for 10 seconds and you are gone. Over." 
    wilson_char "Tell me what you can see. Over."
    hide van_hr_con
    show van_hr_nor at left
    hide aut_bg_forest3_img
    show aut_bg_forest3_img
    hide wil_hr_sur
    show wil_hr_nor at right
    "You look around, and you answer confidently—"
    menu:
        "I'm under a cloud":
            "The walkie-talkie goes silent, is it broken?"           
            "Suddenly, laughter bursts from the speaker."
            play sound "audio/aut/aut_se_transceiver.mp3" #Transceiver sound
            hide wil_hr_nor
            show wil_hr_hap at right
            wilson_char "{size=40}Hahaha...{/size} Vanta, you're so stupid!"
            wilson_char "Just stay still, and I'll find you. Over."
            hide van_hr_nor
            show van_hr_ser at left
            hide aut_bg_forest3_img
            show aut_bg_forest3_img
            hide wil_hr_hap
            show wil_hr_hap at right
            vanta_char "Bro, I know this sounds insane, but the cloud I'm under actually looks like Tentapod! Over."
            play sound "audio/aut/aut_se_transceiver.mp3" #Transceiver sound
            wilson_char "Hey Bro... This also sounds insane, but I know exactly where you are, I can see the Tentapod cloud, too! Over."
            hide van_hr_ser
            show van_hr_nor at left
            hide aut_bg_forest3_img
            show aut_bg_forest3_img
            hide wil_hr_hap
            show wil_hr_nor at right
            "Miraculously, against all odds, Wilson manages to track you down with nothing more than a vague description of a cloud's shape."
            hide aut_bg_forest3_img
            with dissolve
            jump aut_cho02_accepted

        "I'm surrounded by ​​flowers":
            play sound "audio/aut/aut_se_transceiver.mp3" #Transceiver sound
            hide wil_hr_nor
            show wil_hr_thi at right
            wilson_char "Vanta... that doesn't tell me anything. There must be something else around you. Over."
            hide wil_hr_thi
            show wil_hr_hap at right
            wilson_char "Can you try to get to higher ground for a good vantage point? Haha!"
            wilson_char "Try to find a huge rock or a tall tree to climb for a better view. Let me know what you see. Over."
            vanta_char "Wilson! Don't laugh at my pain. Alright, I can see a huge tree. I'm going to climb up the tree and take a look. Over."
            play sound "audio/aut/aut_se_tree.mp3" #The sound of swaying trees
            "As you climb up the tree, you reach for a sturdy branch, inadvertently shaking it."
            "Suddenly, a bee hive plummets to the forest floor; you don't feel very good about this."
            hide van_hr_nor
            hide wil_hr_hap
            show van_hr_emb at left
            hide aut_bg_forest3_img
            show aut_bg_forest3_img
            show wil_hr_sur at right
            vanta_char "{size=34}ARE YOU SERIOUS? PINEAPPLES!{/size}"
            "Yes, we are serious."
            play sound "audio/aut/aut_se_wasp.mp3" #buzz of a bee
            "The air fills with buzzing as hundreds of bees swarm around, seeking the source of the disturbance to their home."
            "You are so distraught that you can't hear Wilson calling for you from the walkie-talkie."
            vanta_char "{size=34}Oh shittake mushroom—{/size}"
            vanta_char "Oh please, not like this!!"
            hide van_hr_emb
            show van_hr_sur at left
            hide aut_bg_forest3_img
            show aut_bg_forest3_img
            hide wil_hr_sur
            show wil_hr_sur at right
            vanta_char "{size=45}AHHHHHHHHHH!!!{/size}"
            play sound "audio/aut/aut_se_tree.mp3" #The sound of swaying trees
            "Panicked, you leap from the tree, but instead of landing in your signature hero pose, you stumble, struggling to maintain your balance."
            play sound "audio/aut/aut_se_transceiver.mp3" #Transceiver sound
            wilson_char "Vanta?{size=34} VANTA?{/size} Are you okay? Are you there?"
            wilson_char "Answer me! Tell me what's going on! OVER!"
            vanta_char "No {size=35}No{/size} {size=38}No{/size} {size=41}No{/size} {size=44}No{/size} {size=47}No{/size} {size=50}No!{/size} You can't see me! You can't see me!\nYou can't see me!"
            vanta_char "{size=45}WILSON—SHUT UP!!{/size}"
            vanta_char "{size=45}AHHHHHH!{/size}"
            play sound "audio/aut/aut_se_wasp.mp3" #buzz of a bee
            "The enraged bees chase you relentlessly. Your heart races as you sprint through the forest, weaving between trees in a frantic attempt to throw off the bees."
            play sound "audio/aut/aut_se_leaves_02.mp3" #The sound of running on fallen leaves
            "Adrenaline fuels your legs as you push yourself to your limits. Every step is a leap of faith."
            "This is not as easy as fighting a giant octopus, and certainly not feasible for an ordinary human. But you are Vantacrow Bringer, you refuse to be defeated."
            "You don't know how long you've been bolting, but the pursuit of the bees gradually fades into the distance."
            "You turn a corner with haste, colliding with something as a flash of yellow blocks your vision. Before you can regain your balance, strong arms wrap around you, lifting you effortlessly off your feet."
            hide aut_bg_forest3_img
            show aut_st_fny_img
            with fade
            play sound "audio/aut/aut_se_syojyo.mp3" #The Sound of Shoujo Manga
            pause 2.0 
            "Startled, you find yourself in a princess carry, the unexpected encounter leaving you momentarily breathless as you gaze up into the eyes of..."
            "Yu Q. Wilson."
            wilson_char "Oh I found you!"
            wilson_char "I told you to stay still and not to touch anything, Mr. Vantacrow Bringer."
            wilson_char "If you don't mind, can I let go now?"
            vanta_char "Wh—How would I know there would be a beehive on that tree?!"
            vanta_char "Anyway, thanks for the lift."
            pause 0.5
            ### achievement package ###
            if (achievement.has('aut_st_fny')== False):   
                $ achievement.grant('aut_st_fny')        
                # show screen OverlayScreen1
                # show screen ClickableArea
                python:
                    active_set = "cg"
                    active_tab = "tab2"
            ### achievement package ###
            hide aut_st_fny_img
            hide wil_hr_sur
            hide van_hr_sur
            show van_hr_nor at left
            show wil_hr_nor at right
            with fade
            jump aut_cho02_accepted

    label aut_cho02_accepted:

    "The two heroes finally reunite; now they can valiantly press on with their mission."
    "Now, you and Wilson are looking for any traces of evidence from the previous attacks. You comb through the bushes, parting leaves and branches to inspect every inch of the forest."
    "You find a suitable location to set up a trap, using the natural resources of the forest to camouflage it seamlessly within the surroundings."
    "There, amidst a vibrant carpet of fallen leaves, a playful cub frolics with joy. The air is filled with the sound of its carefree dance and rustling leaves. You whistle to get Wilson's attention to look at the cub amongst the golden foliage."
    hide wil_hr_nor
    show wil_hr_hap at right
    wilson_char "Oh my god, that is sho cyute. Oh! We should make sure it doesn't accidentally get into the trap."
    hide van_hr_nor
    show van_hr_hap at left
    vanta_char "Oh yeah! I'll grab a leaf to entice the cub away from it."
    wilson_char "Oh no, if the cub is here..."
    hide wil_hr_hap
    show wil_hr_sur at right
    wilson_char "Then the mama bear must be nearby, we should watch out—"
    play sound "audio/aut/aut_se_bear_01.mp3" # Bear growling sound  
    play music "audio/sum/sum_bgm_02.mp3" loop fadein 1.0 # Battle music
    show aut_st_btst_img
    with fade
    pause 2.0 
    "All of a sudden, a low, rumbling growl echoes from behind you."
    "Your heart skips a beat, you turn to face the source of the ominous sound, only to find yourself locking eyes with a bear whose fur bristles with aggression."
    "Ah, just what you need—another item checked off the bucket list:\nGetting chased by a bear. How thrilling!"
    ### achievement package ###
    if (achievement.has('aut_st_btst')== False):
        $ achievement.grant('aut_st_btst')      
        # show screen OverlayScreen1
        # show screen ClickableArea
        python:
            active_set = "cg"
            active_tab = "tab2"
    ### achievement package ###
    
    play sound "audio/aut/aut_se_bear_02.mp3" # Bear growling sound
    "The bear lets out a terrifying roar, the forest trembles in response. It exudes unusual agitation and aggression, its abnormally large form far surpassing any bears you've encountered before."
    "You and Wilson pause for a second, exchanging a look that says, 'Deuces!'"

    play sound "audio/aut/aut_se_leaves_02.mp3" # Sound of running on leaves
    "Without saying a word, you read your homie's mind, and simultaneously turn on your heels, racing down the mountain."
    stop sound fadeout 3.0 #Stop sound effects
    scene aut_bg_forest2_img
    # show text "{b}{size=34}Chapter 2.  AUTUMN{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    show van_hr_sur at left
    show wil_hr_sur at right
    with fade 
    wilson_char "Vanta? That's not just an angry bear!!"
    wilson_char "GO {size=35}GO{/size} {size=38}GO!{/size} I think we should go back to Zali!"
    vanta_char "Ahhh!!  THAT IS HUGE..."
    vanta_char "... That's what she said."
    scene aut_bg_forest1_img
    # show text "{b}{size=34}Chapter 2.  AUTUMN{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    show com_base_img
    show aut_com_1_img at aut_com_1_upper
    with fade 
    vandw_char "{size=45}AHHHHHHHHH!!!{/size}"

    play sound "audio/aut/aut_se_leaves_02.mp3" # Sound of running on leaves
    "You and Wilson rapidly approach the village entrance. You see Zali, his presence a beacon of hope."
    stop sound fadeout 3.0 # Stop sound with a fadeout
    show aut_com_2_img at aut_com_2_upper
    zali_char "{size=34}What the hell?! What did you guys do?!{/size}"
    zali_char "I said, 'Don't get hurt', not 'Bring me a surprise!'"
    
    play sound "audio/aut/aut_se_bear_02.mp3" # Bear growling sound
    "The bear catches up to the three of you, slashing towards Wilson."
    "With lightning reflexes, he swiftly dodges to the side, narrowly avoiding the deadly swipe. However, the bear's sheer force collides with a nearby tree, sending it crashing to the ground."
    hide aut_com_1_img
    hide aut_com_2_img
    show aut_com_3_img at aut_com_3_upper
    play sound "audio/sum/sum_se_tako_02.mp3" # Sound of dodging an attack, reused.
    wilson_char "HA! You can't lay a finger on the best former hitman ever—"
    wilson_char "{size=34}WOAHHHH!!{/size} Who put this thing here?!"
    show aut_com_4_img at aut_com_4_upper 
    play sound "audio/aut/aut_se_rope.mp3" # Sound of rope
    "As Wilson nimbly dodges the attack, he accidentally triggers a snare trap, finding himself abruptly hoisted upside down."
    zali_char "WILSON! Use your taser gun!"
    show aut_com_5_img at aut_com_5_upper
    play sound "audio/aut/aut_se_taser.mp3" # Sound of a taser gun
    "Wilson draws his taser gun from his belt, he skillfully aims and fires at the bear while hanging upside down. To everyone's surprise, the bear is only stunned for a few seconds. It's about to attack again."
    wilson_char "MY GOD! That barely did anything, just how strong is this bear?"
    "Seeing Wilson in peril, you quickly assess the situation and leap into action. You rush to Wilson's side and begin to untie the trap, wanting to free him from his precarious predicament."
    hide aut_com_3_img
    hide aut_com_4_img
    hide aut_com_5_img
    show aut_com_6_img at aut_com_6_upper
    vanta_char "Wilson, hang in there!"
    
    play sound "audio/aut/aut_se_rope.mp3" # Sound of rope
    vanta_char "God damn it. This rope is so fricking tight..."
    "However, you're not fast enough, the bear is about to strike again—"
    zali_char "Vanta! The bear!!! {size=40}WILSON—{/size}"
    
    play sound "audio/aut/aut_se_bandage.mp3" # Sound of bandages
    "As the bear unleashes another slashing attack on Wilson, strips of Zali's bandages shoot towards the bear's claws, ensnaring its movements and halting its impending strike."
    "The bear's immense strength begins to strain the bandages, causing them to fray as they are pulled."
    "As elegant as Zali has always been, his voice carries a tone of genuine concern for his teammates."
    zali_char "{size=40}I won't let you hurt Wilson!!{/size}"
    zali_char "UGHHHH!! Van..ta!! I can't hold this forever!"
    vanta_char "{size=40}ZALI!!! HANG ON!!! I'M COMING!!{/size}"
    vanta_char "Oh that sounds bad, I mean {size=40}I'M ARRIVING!!{/size}"
    vanta_char "... That also sounds bad, forget it. {size=40}I'LL BE THERE IN JUST A SECOND!!{/size}"
    "After freeing Wilson from the trap, you shift your focus to Zali."
    show aut_com_7_img at aut_com_7_upper
    play sound "audio/sum/sum_se_kougeki_01.mp3" # Sound of tackling, reused.
    "With unwavering determination, you leap onto the bear, swiftly wrapping your arms and legs around its massive form."
    "The moment Wilson's shoes touch the ground, he propels himself forward, launching into a fierce tackle aimed at the bear."
    vandw_char "{size=45}EUHHHHH AHHHHHH!!! ZALI! RIGHT NOW!!{/size}"
    zali_char "Don't worry, bear. This will be over quickly, and you won't feel a thing."
    hide aut_com_6_img
    hide aut_com_7_img
    show aut_com_8_img at aut_com_8_upper
    play sound "audio/aut/aut_se_needle.mp3" # Sound of needle
    "Zali regains his composure and speaks with a soothing tone. He produces a syringe seemingly out of thin air, and before you can register any movement, the needle is already under the bear's skin."
    show aut_com_9_img at aut_com_9_upper
    "The unknown liquid slowly disappears into the bear's body, as Zali expertly administers the sedative. "
    play sound "audio/sum/sum_se_koke.mp3" # Sound of bear collapsing, reused.
    "The tension in the bandages loosens as the bear slumps onto the ground, surrendering to the sedative's effects."
    hide aut_com_9_img
    show aut_com_10_img at aut_com_10_upper
    show aut_com_9_img at aut_com_9_upper
    "You and Wilson are stunned by the seamless execution of Zali's actions within mere seconds."
    hide com_base_img
    hide aut_com_8_img
    hide aut_com_9_img
    hide aut_com_10_img
    hide com_base_img
    with dissolve
    show zal_hr_nor at center
    zali_char "Alright! This potion will ensure that the bear sleeps peacefully until it gets to HQ."
    zali_char "I'll call A.S.H.'s team to get a case to take the bear back. If there are cubs, I'll take care of them, too."
    hide zal_hr_nor
    show zal_hr_hap at center
    zali_char "Alright then! Nice, guys! That was quite close. But it all worked out in the end. Hahaha!"
    stop music fadeout 1.0 
    play music "audio/aut/aut_bgm_01.mp3" loop fadein 1.0 # Peaceful music
    show aut_st_bten_img
    with fade
    pause 2.0 
    wilson_char "V… Vanta?"
    vanta_char "… Yeah?"
    wilson_char "Did you see what Zali just did?"
    vanta_char "… That he gracefully injected that mysterious syringe to sedate that huge bear, all without batting an eye?"
    "You and Wilson feel a chill go down your spines."
    "Once again, you can read your homie's mind."
    zali_char "What? What are you guys chatting about?"
    "Zali looks at the two of you, clearly puzzled, but with a smile adorning his face."
    zali_char "Your faces look weird. Did I do something wrong?"
    vandw_char "{size=50}No-nothing!{/size}"
    ### achievement package ###
    if (achievement.has('aut_st_bten')== False):
        $ achievement.grant('aut_st_bten')        
        # show screen OverlayScreen1
        # show screen ClickableArea
        python:
            active_set = "cg"
            active_tab = "tab2"
    ### achievement package ###
    scene aut_bg_village1_img
    # show text "{b}{size=34}Chapter 2.  AUTUMN{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    show van_hr_nor at left
    show wil_hr_nor at right
    show zal_hr_nor at center
    with fade
    "The A.S.H. logistics team arrives at the scene, just as the sun begins its descent, bringing with them a cage tailored for the massive bear."
    "As the intense battle finally concludes, the villagers express their appreciation for your efforts by offering a plethora of souvenirs."
    "They give you some locally made maple syrup and a bucket of their specialty mushrooms, each item symbolizing their heartfelt thanks."
    ### achievement package ###
    if (achievement.has('maplesyrup')== False):
        $ achievement.grant('maplesyrup')        
        show screen OverlayScreen1
        show screen ClickableArea
        python:
            active_set="set1"
            active_tab="tab1"
            showItem = 5
            seenlist['seen_5'] = False
        $ achievement.grant('controlnew') 
        play sound "audio/collected_item_ping.mp3"
    ### achievement package ###
    "Zali examines the mushrooms closely before instructing the logistics team to store them in his lab back at A.S.H."
    zali_char "These mushrooms look very interesting... They have a unique smell. I want to see what I can do with them."
    "The three of you also indulge in some delicious mushroom dishes prepared by the villagers, savoring the flavors of their generosity."
    "As peace returns to the mountain, you bid the villagers farewell, the tranquility of the moment etched in your memory."
    "A single maple leaf gently lands on your shoulder, a poignant reminder that even as you depart, nature itself bids its own farewell to the season."
    show aut_edcg_img
    with fade  
    pause 1.5
    # Display END at the bottom right
    ### achievement package ###
    if (achievement.has('aut_st_edcg')== False) or(achievement.has('aut_gallery')== False):
        $ achievement.grant('aut_st_edcg')
        $ achievement.grant('aut_gallery')        
        show screen OverlayScreen1
        show screen ClickableArea
        python:
            active_set ="gallery"
            active_tab ="tab2"
        play sound "audio/collected_item_ping.mp3"
        
    ### achievement package ###
    ### ending screen ###
    # Wait for user to click
    
    show screen OverlayScreen
    if _preferences.language == 'mandarin':
        show screen chapterend_popup("恭喜！Let's make conversation！")
    elif _preferences.language == 'japanese':
        show screen chapterend_popup("お見事！Let's make conversation!")
    else:
        show screen chapterend_popup("Congratulations! Let's make conversation!")
    python:
        active_set ="gallery"
        active_tab ="tab2"
    pause
    call chapter_3 from _call_chapter_3

label chapter_3:
    hide screen OverlayScreen
    hide screen chapterend_popup
    python:
        current_ch = 3
        active_set="cg"
        active_tab="tab3"
    stop music fadeout 1.0  # Fade out menu music
    play music "audio/win/win_bgm_01.mp3" loop fadein 1.0  #Loop playback of peaceful songs with fade-in

    show win_cv_img
    $ achievement.grant('win_cv')
    # Wait until the user clicks
    pause
 
    scene win_bg_office1_img
    # show text "{b}{size=34}Chapter 3.  WINTER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with fade

    window hide
    show van_ci_nor at center
    "The snow glistens on the bare trees, a shimmering blanket draped over the branches. Despite the fortress-like walls of A.S.H., the frigid wind insists on making its presence known."
    "Trying to focus on work feels like attempting to catch snowflakes with a fork. All you can think about is wrapping yourself in a warm blanket, and transforming into a burrito."
    "... Or you can just eat a burrito. "
    hide van_ci_nor
    show van_ci_thi at center
    vanta_char "God, I've been so busy with all of the back-to-back missions. I even had to work on my vacation. I really need to catch up on all this paperwork, but I've been sitting here for hours. I need some fresh air!"
    hide van_ci_thi
    show van_ci_nor at center
    vanta_char "Guys, do you want any drinks? Something to eat? I'm going to grab some snacks real quick."
    hide van_ci_nor
    show wil_ci_hap at center
    wilson_char "Ooo! I haven't had coffee today! I'm gonna go make myself a cup. Vanta, can I have a cheesecake, pwease?"
    wilson_char "Zali, do you want anything? A croissant maybe?"
    hide wil_ci_hap
    show zal_ci_hap at center
    zali_char "Haha, yeah sure! Anything sweet would be fine."
    zali_char "Oh, and hand me the report, Vanta. I'll help you finish this one."
    hide zal_ci_hap
    show van_ci_nor at center
    vanta_char "Alright then! Time to see if there are any new festive items on the menu!"
    "You walk to the door to grab your coat. As you lift it off the hanger, you're surprised by its unusual weight."
    "You check the inside and see a few slimes tucked in. You seem to have disturbed their nap."
    hide van_ci_nor
    show van_ci_sur at right_2p
    show crew3_nor_img at left_2p
    with dissolve
    vanta_char "Oh! My Crew! What are you doing in my coat? Were you napping? Did I wake you up? "
    "The Vantacrew woke up from hearing your voice, they seem to like being snug up in your coat."
    hide van_ci_sur
    show van_ci_3 at right_2p
    vanta_char "Sorry guys, I need my coat; I'm going out."
    play sound "audio/win/win_se_slime_01.mp3" #slime sound
    "The Crew begin bouncing up and down, looking eager to leave with you."
    vanta_char "AND... You're staying here."
    play sound "audio/win/win_se_slime_01.mp3" #slime sound
    hide van_ci_3
    show van_ci_sur at right_2p
    hide crew3_nor_img
    show crew3_ang_img at left_2p
    "The Crew, in apparent defiance, begin to bounce more vigorously and emit disgruntled noises, clearly expressing their disagreement with being told to stay put."
    "They start to huddle around your legs to keep you from going out without them. Sometimes you wonder who's really in charge here."
    hide van_ci_sur
    show van_ci_con at right_2p
    "You look down at them fondly—your Crew, a group of slimes that have been by your side since you joined A.S.H."
    vanta_char "You're telling me if you can't go, I can't either?"
    vanta_char "Ugh! Alright alright! Y'all are so stubborn. Fine then, come on!"
    play sound "audio/win/win_se_slime_01.mp3" #slime sound
    hide crew3_ang_img
    show crew3_3_img at left_2p
    "Despite the hint of annoyance in your voice, you open your coat, leaning forward to allow the Crew to hop inside."
    "After all, it's snowing, and you couldn't bear to let them bounce around in the cold."
    "Who knew being kind to a bunch of tiny and seemingly tasty creatures could be so bothersome? Yet here you are, playing the reluctant hero once again."
 
    scene win_bg_street1_img
    # show text "{b}{size=34}Chapter 3.  WINTER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with fade 
    "As you step out of A.S.H. HQ, a blast of cold wind smacks you in the face; you clutch your coat tighter around you, and the Crew bunch up in your booba—the best place to be."
    "You head to the store 'Le Petit Coin' just around the corner, which translates to 'the little corner'."
    show van_ci_nor at center
    vanta_char "Let's see, I'll need to get... A cheesecake for Wilson, a croissant, something sweet... And what else..."

    menu:
        "Enter Le Petit Coin": 
            play sound "audio/sum/sum_se_bell.mp3" #Sound of bell, reused
            jump win_cho_one1_accepted
    label win_cho_one1_accepted:

    scene win_bg_shop_img
    # show text "{b}{size=34}Chapter 3.  WINTER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with fade
    "As you enter Le Petit Coin, the warmth of the store washes over you. Festive decorations adorn every corner, from twinkling lights to garlands of holly, casting a cheerful glow over the space."
    "You can't help but smile as you take in the merry atmosphere. With a sense of excitement, you begin to browse the aisles."
    show van_ci_con at center
    vanta_char "Oh? There are some samples over there. I'm gonna try it! Oh my god, Zali is gonna hate these."
    "It looks like Le Petit Coin is promoting a new festive item—eggplant-shaped candy. You take a bite of the sample; it tastes nice, with a delightful grape flavor."
    "You decide to grab a bag for Zali, thinking maybe, just maybe, it might change his perception of eggplant."
    hide van_ci_con
    show van_ci_hap at center  
    vanta_char "Is that ice cream cake? I must get it for Wilson. Ahahaha!"
    vanta_char "I should also get something for myself to drink. Hmm, how about some diet soda?"
    ### achievement package ###
    if (achievement.has('dietsoda')== False):
        $ achievement.grant('eggplant')
        $ achievement.grant('dietsoda') 
        $ achievement.grant('icecreamcake')         
        show screen OverlayScreen1
        show screen ClickableArea
        python:
            active_set="set1"
            active_tab="tab1"
            showItem = 8
            seenlist['seen_6'] = False
            seenlist['seen_7'] = False
            seenlist['seen_8'] = False
        $ achievement.grant('controlnew') 
        play sound ["audio/collected_item_ping.mp3","audio/win/win_se_slime_01.mp3"]
    ### achievement package ### 
    play sound "audio/win/win_se_slime_01.mp3" #slime sound
    show crew3_hap_img at left_2p
    show van_ci_hap at right_2p
    with dissolve
    "The Crew seems to be excited, too. Their cheerful burbles fill the air as you walk past a beautifully decorated Christmas tree."
    hide van_ci_hap
    show van_ci_con at right_2p 
    vanta_char "Oh? You guys like the Christmas tree? {size=40}Merry Krisis!{/size}"
    play sound "audio/win/win_se_slime_01.mp3" #slime sound
    "They look eager to capture a festive photo, and you can't resist their enthusiasm. You oblige and take out your phone."
    
    menu:
        "Ask the Crew to nestle around the tree, and take a picture together":
            hide van_ci_con #### Tsumire
            show van_ci_hap at right_2p
            show crew3_hap_img at left_2p
            vanta_char "Alright! Come on, go in front of the tree, and smile!"
            play sound "audio/win/win_se_camera.mp3" #Camera shutter sound
            "You take a picture of the excited crew gathered around the tree, their tiny forms bobbing happily."
            play sound "audio/win/win_se_slime_01.mp3" #slime sound
            "One of the Crew accidentally gets their little leg entangled in the string lights, prompting a frantic tug. With a jolt, the wire gives way, and the tree begins to wobble."
            show win_st_fny_img
            with fade
            pause 2.0
            "Your instinct kicks in, you swiftly dart forward to intercept its downward trajectory."
            "You manage to steady the swaying tree, preventing it from toppling over completely."
            vanta_char "{size=40}Wo-woah!! Woah!!{/size} That was close!"
            vanta_char "You are banned from getting under the Christmas tree again. That was insane guys!"
            play sound "audio/win/win_se_slime_01.mp3" #slime sound
            "You stabilize the tree with a firm grip, the Crew looking somewhat apologetic. Laughter fills the air as you avert a potential disaster."
            pause 0.5
            ### achievement package ###
            if (achievement.has('win_st_fny')== False):   
                $ achievement.grant('win_st_fny')        
                # show screen OverlayScreen1
                # show screen ClickableArea
                python:
                    active_set ="cg"
                    active_tab="tab3"
            ### achievement package ###
            hide win_st_fny_img 
            scene win_bg_shop_img
            # show text "{b}{size=34}Chapter 3.  WINTER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
            with fade
            jump  win_cho2p_accepted

        "Take a selfie with the Christmas tree":
            hide van_ci_con
            hide crew3_hap_img
            show van_ci_hap at right_2p
            show crew3_ang_img at left_2p
            play sound "audio/win/win_se_camera.mp3" #Camera shutter sound
            "You take a selfie with the twinkling Christmas tree; the Crew sound annoyed that they aren't in the picture with you."
            play sound "audio/win/win_se_slime_01.mp3" #slime sound
            vanta_char "Haha, I'm joking. I'll take one more with you guys in it."
            play sound "audio/win/win_se_camera.mp3" #Camera shutter sound
            hide crew3_ang_img
            show crew3_hap_img at left_2p
            "The second picture seems to make them happier."
            hide crew3_hap_img
            hide van_ci_hap
            jump  win_cho2p_accepted

    label win_cho2p_accepted:

    show van_ci_hap at center 
    with dissolve  
    "You make your way to the counter to pay. After packing everything, you exit Le Petit Coin."
    play sound "audio/sum/sum_se_bell.mp3" # Sound of bell, reused
    scene win_bg_park_img
    # show text "{b}{size=34}Chapter 3.  WINTER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    show van_ci_nor at center
    with fade
    "As you head back to A.S.H., you walk past a nearby park..."
    "The snow has already started to lightly cover the playground, but you notice a small mound of bright colors that has yet to be covered."
    "Upon closer inspection, you notice that the colors are those of the coat of a little boy, crouched in the snow."
    hide van_ci_nor
    show van_ci_thi at center
    vanta_char "I wonder where his parents are. It's freezing out; let's go see if he's alright."
    play sound "audio/win/win_se_slime_01.mp3" #slime sound
    show van_ci_thi at right_2p
    show crew1_nor_img at left_2p
    with dissolve
    "The Crew seem to grow concerned as well. One of them wiggles out of your coat and bounces ahead of you, eager to make sure the kid is okay."
    menu:
        "Talk to the little boy":
            jump win_cho_one2_accepted
    label win_cho_one2_accepted:

    hide van_ci_thi
    show van_ci_nor at right_2p
    vanta_char "Hey kiddo, what are you doing here by yourself? Where's your family?"
    "You must seem tall and intimidating to him, which makes him a bit scared to speak."
    play sound "audio/win/win_se_kiran.mp3" #flash of inspiration sound
    hide van_ci_nor
    show van_ci_sur at right_2p
    "You look at the Vantacrew, and you have an idea!"
    play sound "audio/win/win_se_slime_01.mp3" #slime sound
    hide van_ci_sur
    show van_ci_3 at right_2p
    show crew1_3_img at left_2p
    vandc_char "{size=60}:3{/size}"
    "The boy looks confused, clearly unsure of what's going on."
    hide van_ci_3
    hide crew1_3_img
    show van_ci_sur at right_2p
    show crew1_nor_img at left_2p
    vanta_char "No reaction? Really? Okay, that wasn't my best shot, let's try again!"
    play sound "audio/win/win_se_slime_01.mp3" #slime sound
    hide van_ci_sur
    hide crew1_nor_img
    show van_ci_3 at right_2p
    show crew1_3_img at left_2p
    vandc_char "{size=100}:3{/size}"
    "The kid finally smiles, bringing a sense of relief to both you and the Vantacrew."
    hide crew1_3_img
    hide van_ci_3
    show van_ci_nor at right_2p
    show npc5_img at left_2p
    npc5_char "I... I play with my best friend in this park every day. She is about to move to a different town with her family. We had an argument yesterday, and she didn't show up today..."
    npc5_char "I shouldn't have been so mean to her. She lent me her favorite game, and now I might not even have the chance to return such an important thing to her..."
    "You notice he's holding a game tightly. The familiar blue slime on the cover reminds you of the Vantacrew. Glancing back, you see some of them bouncing in the snow behind you."
    hide van_ci_nor
    show van_ci_con at right_2p
    vanta_char "Listen kid, if your friend means a lot to you, you should go to her instead of waiting here for her to come to you."
    npc5_char "But...but...will I annoy her? What if she doesn't want to see me? What if she doesn't want to be friends with me anymore?"
    vanta_char "You know, sometimes you just shouldn't overthink things. You do what you can, and you can what you do. Don't be afraid of expressing your feelings to someone important to you."
    play music "audio/sum/sum_bgm_02.mp3" fadein 1.0 loop #Battle music
    show win_st_btst_img
    with fade
    pause 2.0  
    "With your encouragement, the boy asks you to accompany him to find his friend. Upon arriving at his friend's house, everything is gone, leaving only an empty house."
    "The boy starts to cry and you try to comfort him. You look around, realizing that the Vantacrew who were following behind you, have disappeared."
    "Immediately, you implore Kurococco to track the Crew's location. The results reveal that they are in a moving vehicle."
    vanta_char "Kid, ready for a little adventure? Hold on tight, and off we go!\nI'll dash so fast it'll feel like we're flying, even though it's just me running. You get what I'm saying, right?"
    ### achievement package ###
    if (achievement.has('win_st_btst')== False):
        $ achievement.grant('win_st_btst')       
        # show screen OverlayScreen1
        # show screen ClickableArea
        python:
            active_set = "cg"
            active_tab = "tab3"
    ### achievement package ###
    scene win_bg_run_img
    # show text "{b}{size=34}Chapter 3.  WINTER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    show com_base_img
    with fade
    show win_com_1_img at win_com_1_upper
    with dissolve
    "You effortlessly give the kid a piggyback while juggling the shopping bags like a pro. Multitasking is easy for an experienced hero like you."
    play sound "audio/win/win_se_snow_run.mp3" #Running on snow
    "You leap into action, showing off your parkour prowess."
    npc5_char "{size=45}WOW!! YOU'RE SO COOL!{/size}\nAre you Spider Guy? Oh, but... you're not wearing tights."
    hide win_com_1_img
    show win_com_2_img at win_com_1_upper
    vanta_char "I'm not Spider Guy! I'm a tyrant! A hero of Krisis!\nYeah, one of my fellow heroes does wear tights, but not all heroes wear tights!"
    scene win_bg_street2_img
    # show text "{b}{size=34}Chapter 3.  WINTER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with fade
    "As you catch up to the moving car, its speed gradually decreases until it eventually comes to a stop in front of a house."
    play sound "audio/win/win_se_car.mp3" #The sound of a car door closing.
    show npc6_img at left_2p
    show crew3_nor_img at right_2p
    "The door swings open, revealing a little girl accompanied by her parents. Among them, you spot the Vantacrew hopping out one after another, slipping by unnoticed."
    hide npc6_img
    hide crew3_nor_img
    show npc5_img at center
    npc5_char "Oh! That...that's my friend..."
    hide npc5_img
    show van_ci_thi at center
    vanta_char "Wait, really? LMAO? How did the Crew know...?"
    play sound "audio/win/win_se_slime_01.mp3" #slime sound
    hide van_ci_thi
    show crew3_hap_img at center
    "Watching the bouncing slimes, you can't help but think that there's absolutely not a single thought behind those colon three faces. It's probably just head empty, vibe happy!"
    "Well, at least it all worked out, just like in a Christmas movie."
    hide crew3_hap_img
    show win_com_3_img at win_com_3_upper
    "With a smile, you hand the boy the game he wishes to return and give him a reassuring push towards his friend's house."
    vanta_char "Come on, I believe in you. Go ahead and tell her how you feel."
    "The boy mustered up the courage to step forward and say hello to his friend."
    hide win_com_3_img
    show npc6_img at left_2p
    show npc5_img at right_2p
    npc5_char "Hi... I wanted to say, I'm sorry about yesterday.\nI hope we can still be friends. I want to play your favorite game together again."
    npc6_char "What? Of course we're still friends! I just thought we'd meet up again so I could get it back when you finish—"
    hide npc5_img
    hide npc6_img
    show win_com_4_img at win_com_1_upper
    npc6_char "Why are there so many slimes here? And who is that behind you? I'll protect you from him if he's doing anything suspicious."
    npc5_char "Oh, that guy! Um, apparently, he's a hero, even though he's not wearing tights... I think! He brought me here."
    "The boy has now reunited with his friend, and they appear to be in good spirits. Surrounded by their parents, they wave goodbye to you before heading into the girl's new house."
    stop music fadeout 1.0  # Fade out the menu music
    play music "audio/win/win_bgm_01.mp3" loop fadein 1.0  # Play a peaceful track on loop
    show win_st_bten_img 
    with fade
    pause 2.0  
    "You bask in the satisfaction of being a friendly neighborhood hero today, and the Vantacrew seems equally pleased with themselves for locating the moving car."
    play sound "audio/win/win_se_phone.mp3" #Cell Phone Sounds
    "Simultaneously, your phone vibrates in your pocket, signaling an incoming call from your teammates."
    pause 0.5
    ### achievement package ###
    if (achievement.has('win_st_bten')== False):
        $ achievement.grant('win_st_bten')         
        # show screen OverlayScreen1
        # show screen ClickableArea
        python:
            active_set = "cg"
            active_tab = "tab3"
    ### achievement package ###
    scene win_bg_street2_img
    # show text "{b}{size=34}Chapter 3.  WINTER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    show win_bg_office2_img
    show van_ci_nor at right
    show wil_ci_sur at left
    with fade
    stop sound fadeout 3.0 #Stop sound effects
    vanta_char "Hello? This is Vanta speaking."
    wilson_char "Vanta, what the hell? Zali and I are waiting for you!\nWhere did you go? Are you okay?"
    hide van_ci_nor #### Tsumire
    show van_ci_hap at right
    vanta_char "Oh, sorry bro, I'm okay! \nI got sidetracked by a small task; I helped a little kid! "
    hide wil_ci_sur
    show zal_ci_nor at left
    zali_char "We thought you just went to get some drinks and desserts. Wilson was yapping the whole time..."
    hide zal_ci_nor
    show zal_ci_thi at left 
    zali_char "Is everything alright now? Do you need us to come and help?"
    hide zal_ci_thi
    show zal_ci_nor at left 
    vanta_char "Nah, everything is good. We ball. I'm heading back now; let's have dinner together."
    "Glancing at the shopping bag, you notice the ice cream cake has begun to melt. Oh well, better pop it in the freezer pronto."
    hide van_ci_hap
    show van_ci_con at right
    vanta_char "And I—uh, bought something special for Wilson."
    hide zal_ci_nor
    show wil_ci_hap at left
    wilson_char "Really?! For me?! You're too kind, Vanta! Well, how about... I make some curry for dinner?"
    vanta_char "Sounds good, I'll be there."
    hide wil_ci_hap
    show zal_ci_hap at left
    zali_char "Hmm... Then I think I can make some macarons for dessert!"
    hide van_ci_con
    hide zal_ci_hap
    show wil_ci_sur at left
    show van_ci_sur at right
    wandv_char "{size=50}Please don't!{/size}"
    hide van_ci_sur
    hide wil_ci_sur
    hide win_bg_office2_img
    show van_ci_nor at right_2p
    show crew3_nor_img at left_2p
    with dissolve
    "You hang up the phone, scanning the area for the Vantacrew. Some are nestled at your feet, seeking warmth, while others frolic in the snow on the street."
    hide van_ci_nor
    show van_ci_con at right_2p  
    vanta_char "Come on, let's go home, my Crew."
    hide van_ci_con
    show van_ci_hap at right_2p
    vanta_char "{size=50}Ha...Merry Krisis!{/size}"
    play sound "audio/win/win_se_slime_01.mp3" #slime sound
    hide crew3_nor_img
    show crew3_hap_img at left_2p
    "You open your coat, and the Crew hop inside to snuggle with you. Despite the season's icy grip, an inner warmth envelops you, putting a smile on your face."

    show win_edcg_img
    # show text "{b}{size=34}Chapter 3.  WINTER{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with fade
    pause 1.5
    # Display END at the bottom right
    ### achievement package ###
    if (achievement.has('win_st_edcg')== False) or(achievement.has('win_gallery')== False):
        $ achievement.grant('win_st_edcg')
        $ achievement.grant('win_gallery')        
        show screen OverlayScreen1
        show screen ClickableArea
        python:
            active_set = "gallery"
            active_tab = "tab3"
        play sound "audio/collected_item_ping.mp3"
        
    ### achievement package ###
    ### ending screen ###
    show screen OverlayScreen
    if _preferences.language == 'mandarin':
        show screen chapterend_popup("恭喜！Oh my goodness！")
    elif _preferences.language == 'japanese':
        show screen chapterend_popup("クリアおめでとう！Oh my goodness!")
    else:
        show screen chapterend_popup("Congratulations! Oh my goodness!")
    python:
        active_set = "gallery"
        active_tab = "tab3"
    
    # Wait for user to click
    pause
    jump chapter_4 
    # from _call_chapter_4



label chapter_4:
    python:
        current_ch = 4
        active_set="cg"
        active_tab="tab4"
    hide screen OverlayScreen
    hide screen chapterend_popup
    stop music fadeout 1.0  # Fade out menu music
    play music "audio/spr/spr_bgm_01.mp3" loop fadein 1.0  #Loop playback with fade-in

    show spr_cv_img
    $ achievement.grant('spr_cv') 
    # show text "{b}{size=34}Chapter 4.  SPRING{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    # Wait for user to click
    pause
 
    scene spr_bg_office1_img
    # show text "{b}{size=34}Chapter 4.  SPRING{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with fade
    #Avoid momentary flickering when switching dialogue windows 
    window hide

    "Ah, spring—a time of longer days, warmer sunshine, and, unfortunately, the return of hay fever."
    show van_ci_nor at right_2p
    show zal_ci_nor at left_2p
    with dissolve
    "As you step into HQ, Zali is already there, surrounded by a couple of Vezkits, perhaps even earlier than usual. You head straight for the kitchen, eager to brew yourself a cup of coffee to kickstart your day."
    hide van_ci_nor
    show van_ci_hap at right_2p
    vanta_char "Good morning, Zali!"
    hide zal_ci_nor
    show zal_ci_hap at left_2p
    zali_char "Vanta! Good morning! Isn't it just lovely...spring!"
    vanta_char "Yeah! It is! Although it's still kind of gloomy, but the flowers have started to bloom for sure."
    zali_char "Yes! Ohhh, you know what we should do? {font=SourceHanSansLite.ttf}おはなみ !{/font} We should go see cherry blossoms!"
    show van_ci_hap at right
    show zal_ci_hap at left
    show wil_ci_nor at center
    with dissolve
    "Suddenly, someone opens the door. It's none other than Yu Q. Wilson, followed closely by a group of still sleepy Wilsoneers."
    hide wil_ci_nor
    show wil_ci_thi at center 
    wilson_char "WITHOUT ME? I want to go see the cherry blossoms too!"
    vandz_char "Good morning, Wilson!"
    hide wil_ci_thi
    show wil_ci_sur at center
    wilson_char "Morning guys! You guys aren't seriously going without me, are you?"
    zali_char " No, we were just talking about it. Don't worry!"
    hide van_ci_hap
    show van_ci_con at right
    hide wil_ci_sur
    show wil_ci_nor at center
    vanta_char "Hey, how about this: We go see the cherry blossoms next week?"
    zali_char "Alright! Sounds good!"
    hide wil_ci_nor
    show wil_ci_hap at center
    wilson_char "I can't wait!"
    hide zal_ci_hap
    hide wil_ci_hap
    hide van_ci_con
    show van_ci_nor at right
    show zal_ci_nor at left
    show wil_ci_nor at center
    "Wilson walks over to the coffee maker and makes his French vanilla latte. He's about to add the French vanilla coffee creamer, like he normally does, until he realizes that it's not there."
    hide wil_ci_nor
    show wil_ci_thi at center
    wilson_char "Oh shoot, did I run out?"
    hide zal_ci_nor
    hide wil_ci_thi
    show zal_ci_sur at left
    show wil_ci_thi at center
    zali_char "Run out of what?"
    wilson_char "My coffee creamer."
    hide zal_ci_sur
    hide wil_ci_thi
    show zal_ci_nor at left
    show wil_ci_nor at center  
    vanta_char "We can go get more when we head out for today. I have just the thing in the meantime."
    hide van_ci_nor
    hide zal_ci_nor  
    hide wil_ci_nor
    show van_ci_hap at right
    show zal_ci_hap at left
    show wil_ci_hap at center
    wilson_char "You're a lifesaver, thank you!"
    hide wil_ci_hap
    hide zal_ci_hap
    hide van_ci_hap
    show van_ci_nor at center
    with dissolve
    "You walk over to the fridge and open the doors. Two items stand out; maple syrup and ice cream cake."
    hide van_ci_nor
    show van_ci_3 at center
    "Maple syrup would work very well with Wilson's coffee. Technically, the same can be said for the ice cream cake, but it's been in here for a while…"
    "But for the content, it's tempting to show off to Wilson. Even a few of the Vantacrew seem to snicker at the notion. You decide to give Wilson—"

    menu:
        
        "Ice Cream Cake":
            hide van_ci_3
            show van_ci_con at center
            "Snickering to yourself, you bring out the ice cream cake, closing the doors with your back. You place the cake next to the coffee maker. Wilson turns in your direction and immediately furrows his brows."
            show van_ci_con at right_2p
            show wil_ci_sur at left_2p
            with dissolve
            wilson_char "Vanta, what on earth is this…"
            hide van_ci_con
            show van_ci_3 at right_2p
            vanta_char "Listen, the moment I saw this, I just thought of you. I thought you would appreciate this gift while having some sweetness with your coffee."
            hide wil_ci_sur
            show wil_ci_ser at left_2p
            wilson_char "Whatever dude, get this out of my face."
            "Going to the fridge himself, Wilson looks around and finds the unopened maple syrup from a couple of months ago."
            wilson_char "You idiot, you could've used this instead!"
            hide van_ci_3
            show van_ci_hap at right_2p 
            "You laugh at Wilson's reaction while he groans in response, now quietly sipping his cup of coffee."
            hide van_ci_hap
            hide wil_ci_ser
            with dissolve
            jump spr_cho2_1_accepted
        "Maple Syrup":
            scene spr_st_wilson_img
            # show text "{b}{size=34}Chapter 4.  SPRING{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
            with fade
            pause 2.0  
            "Despite how tempting it is to grab the ice cream cake, you decide to be a good teammate and grab the maple syrup. You close the fridge and hand Wilson the bottle."
            wilson_char "Oh my god! I remember this! Didn't we get this from that one village we helped out?"
            vanta_char "Yeah! It's still good, not close to expiring or anything like that."
            wilson_char "Now I really can't wait for my coffee! Thank you!"
            ### achievement package ###
            if (achievement.has('spr_st_wilson')== False):
                $ achievement.grant('spr_st_wilson')    
                # show screen OverlayScreen1
                # show screen ClickableArea
                python:
                    active_set = "cg"
                    active_tab = "tab4"
            ### achievement package ###
            hide spr_st_wilson_img
            scene spr_bg_office1_img
            # show text "{b}{size=34}Chapter 4.  SPRING{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
            with fade
            jump spr_cho2_1_accepted
    label spr_cho2_1_accepted:
    
    show zal_ci_nor at left_2p
    show van_ci_nor at right_2p
    "You, Zali, and Wilson begin to scroll through the website of the local bakery you frequently visit. Your eyes land on the pastries and you notice Zali looking at the croissants with expecting eyes."
    vanta_char "See something you like, Zali?"
    hide zal_ci_nor
    show zal_ci_hap at left_2p
    zali_char "Oh, I'm in the mood for that croissant, as always."
    hide van_ci_nor
    show van_ci_con at right_2p
    vanta_char "You know, Zali, it's funny that you like croissants because they lowkey look like they're eggplant-shaped."
    hide zal_ci_hap
    show zal_ci_thi at left_2p
    zali_char "Vanta, never joke about that ever again. My heart may never recover. Croissants do NOT look like eggplants. Oh, mon Dieu..."
    hide zal_ci_thi
    show van_ci_con at center
    with dissolve
    "You let out a chuckle as you hold your hands up in defeat. In the end, you all order what you usually get."
    "An idea pops into your mind, prompting you to glance over your desk."
    hide van_ci_con
    show van_ci_3 at center
    "Now is the perfect time to give Zali the gift you've been holding onto for a while."
    "There's the eggplant-shaped candy: knowing how much he hates eggplant, it would be pretty funny to see his reaction to the gag gift. "
    "On the other hand, you bought the croissant keychain with Zali in mind because it reminded you of him. In the end, you decided to give Zali—"
    menu:
        "Croissant Keychain":
            scene spr_st_zali_img
            # show text "{b}{size=34}Chapter 4.  SPRING{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
            with fade
            pause 2.0 
            "You grab the keychain from your desk and return to the kitchen. You tap Zali's shoulder to get his attention. When he turns his head, you show him the croissant keychain."
            zali_char "Haha, this is cute! Where did you get it?"
            vanta_char "I got it from a souvenir shop while I was on a brief vacation in the summer. I've been meaning to give it to you sooner, but there hasn't been a good time lately."
            zali_char "Better now than never, right?"
            "Zali smiles at you, fully appreciative of the gift. Seeing his reaction makes your heart grow a couple of sizes. You're glad you were finally able to give the gift to him."
            ### achievement package ###
            if (achievement.has('spr_st_zali')== False):
                $ achievement.grant('spr_st_zali')    
                # show screen OverlayScreen1
                # show screen ClickableArea
                python:
                    active_set = "cg"
                    active_tab = "tab4"
            ### achievement package ###
            hide spr_st_zali_img
            scene spr_bg_office1_img
            # show text "{b}{size=34}Chapter 4.  SPRING{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
            with fade
            jump spr_cho2_2_accepted
        "Eggplant-shaped Candy":
            hide van_ci_3
            show van_ci_hap at right_2p
            show zal_ci_sur at left_2p
            with dissolve
            vanta_char "Have some candy to hold you over. Our order should be here soon!"
            hide zal_ci_sur
            show zal_ci_thi at left_2p
            zali_char "Ah, thank you! Wait, why is this in the shape of an eggplant?"
            vanta_char "Ah, that's how the shop made it. Don't worry, it doesn't taste like eggplant, I promise."
            hide zal_ci_thi
            show zal_ci_ser at left_2p
            "You toss a piece of the eggplant-shaped candy over to Zali, who easily catches it. He opens the candy hesitantly and gives it a cautious sniff. He squints his eyes in your direction while you give a thumbs up in reassurance."
            "Zali puts the candy in his mouth, a little wary of the flavor. He widens his eyes in surprise, a small smile forming on his face."
            hide zal_ci_ser
            show zal_ci_hap at left_2p
            zali_char "This is really good, thank you!"
            show zal_ci_hap at left
            show van_ci_hap at right
            show wil_ci_hap at center
            with dissolve
            wilson_char "Wait, I wanna try some, too!"
            vanta_char "Go right ahead, there's plenty more where that came from!"
            "You grab the bag full of eggplant candy from the counter and put it on the table for the two to enjoy."
            hide wil_ci_hap
            hide zal_ci_hap
            hide van_ci_hap
            jump spr_cho2_2_accepted
    label spr_cho2_2_accepted:

    
    play sound "audio/aut/aut_se_clothes.mp3" #Sound of changing clothes Used
    "While waiting for the delivery, you suit up in your hero outfits to prepare for any possible missions that may come your way."
    show van_hr_nor at center
    with dissolve
    play sound "audio/spr/spr_se_buzzer.mp3" #Delivery Buzzer
    "A buzzing sound can be heard from the door. You head over and open it, revealing the breakfast order you made in advance."
    "You check the contents of the bag, making sure everything is there and correct."
    hide van_hr_nor
    show van_hr_hap at center
    vanta_char "Guys, our order's here!"
    show wil_hr_hap at left
    wilson_char "Yay! I need food right now!"
    show zal_hr_hap at right
    zali_char "Yay!! Bon appetit!"
    hide van_hr_hap
    hide wil_hr_hap
    hide zal_hr_hap
    show com_base_img
    show spr_com_1_img at spr_com_upper
    with dissolve
    play sound "audio/spr/spr_se_phone_vib.mp3" #Cell phone vibration
    "The three of you enjoy coffee and croissants for breakfast. Just as you take the last bite, all of your phones buzz simultaneously."
    stop sound fadeout 1.0 #Stop sound effects
    "You pull out your phone to find a new mission notification. The three of you read the brief together."
    zali_char "\"We have received a strong lead on the pharmaceutical company that was previously discovered during one of Vantacrow's missions.\""
    wilson_char "Wait, Vanta, is that the same place you found out about when you were on vacation in the summer?"
    hide spr_com_1_img
    show spr_com_2_img at spr_com_upper
    vanta_char "Oh yeah! The giant octopus and that suspicious drink shop.\nWhat about it?"
    zali_char "\"A.S.H.'s intel department has found a promising location the company has been using as a cover for their shady operation. We need Krisis to infiltrate the designated location quietly and gather pertinent data.\""
    wilson_char "\"It's imperative that the operation remain discreet and avoid any collateral damage. However, Squad A from A.S.H. will be positioned nearby, ready to intervene to neutralize any threats deemed too dangerous to the public.\"" 
    wilson_char "\"In case of any unforeseen circumstances, the Vezkits, Wilsoneers, and Vantacrew will also remain on the ready for any required backup.\""
    vanta_char "Wait, you mean Squad A, the demolitions team? Are they really going to be on standby?"
    hide spr_com_2_img
    show spr_com_3_img at spr_com_upper
    wilson_char "Looks like it's happening. Alright, boys, let's gear up and get ready to roll."
    stop music fadeout 1.0  #Fade out music
    play music "audio/spr/spr_bgm_02.mp3" loop fadein 1.0  #Loop playback with fade-in
    hide spr_com_3_img
    show spr_com_4_img at spr_com_upper
    # play sound "audio/aut/aut_se_clothes.mp3" #Sound of changing clothes Used
    "Getting ready for your mission is now, just second nature to you; you swiftly prepare. Your trusted partners, Tsuchi, Tentapod, and Kurococco, are also ready to go."
    hide spr_com_4_img
    scene spr_bg_lab1_img
    # show text "{b}{size=34}Chapter 4.  SPRING{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    show com_base_img
    show spr_com_5_img at spr_com_upper
    with fade
    play sound "audio/spr/spr_se_gatagata.mp3" #Rattling sound during infiltration
    "You skillfully sneak into the location specified in the mission brief. Quietly infiltrating the building, you keep a sharp eye out for anything worth investigating."
    hide spr_com_5_img
    show spr_com_6_img at spr_com_upper
    "Zali, Wilson, and you share an impeccable working dynamic; a simple gesture is all it takes for you to understand exactly what the other means."
    vanta_char "Pssst... This way. "
    zali_char "Oh my goodness... What are these?"
    hide spr_com_6_img
    show spr_com_7_img at spr_com_upper
    play sound "audio/spr/spr_se_mystery.mp3" #The sound of seeing mushrooms
    wilson_char "Oh... My... God..."
    hide spr_com_7_img
    show spr_com_8_img at spr_com_upper
    wilson_char "These mushrooms... There are so many of them. How long have they been planning this?"
    zali_char "Wait, guys, aren't these the same mushrooms we ate when we went to the mountain village to help them with the harvest? And didn't we encounter that oddly aggressive bear?"
    vanta_char "Oh, the smell! I remember it now. This scent is so familiar, just like the one in the drink when I fought the octopus."
    zali_char "Look at all these different food byproducts. How many are they producing, and how many have already made their way into the public?"
    vanta_char "What? The eggplant-shaped candy too? No way..."
    hide spr_com_8_img
    show spr_com_9_img at spr_com_upper
    wilson_char "Are they using these food products for mass human experimentation?"
    vanta_char "I'm unsure how we'll dispose of all these. It seems we may need to destroy them all together."
    zali_char "Alright, let me report this to Squad A so they're aware and can prepare if needed."
    play sound "audio/spr/spr_se_crush.mp3" #Clanging sound of metal falling to the floor
    wilson_char "Wait, wait, wait... What's that noise, guys? Can you hear it? Where is it coming from?"
    zali_char "I heard it too. Sounds like something metallic dropped onto the floor..."
    hide spr_com_9_img
    show spr_com_10_img at spr_com_upper
    "You look around the lab, noticing a door behind the shelves. The noises seem to come from there."
    vanta_char "Well, I guess we simply have to ball. Whatever's behind that door could be dangerous."
    "As the tank of the group, you decide to lead the way, with Zali close behind to provide support. Meanwhile, Wilson steps forward to examine the lockpad next to the door."
    hide spr_com_10_img
    show spr_com_11_img at spr_com_upper
    wilson_char "Are you ready, Vanta?"
    play sound "audio/spr/spr_se_Tentapod.mp3" #Tentapod
    "You take a deep breath and nod at Wilson. With precision, Tentapod swiftly extends its robotic octopus arm and effortlessly hacks into the lockpad. The door is unlocked within a matter of seconds."
    play sound "audio/spr/spr_se_door.mp3" #Sound of a metal door opening
    scene spr_bg_lab2_img
    # show text "{b}{size=34}Chapter 4.  SPRING{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with dissolve
    "The heavy metal door emits a soft hiss as it opens slowly, revealing darkness beyond. You step inside cautiously, your senses on high alert, ready for whatever lies ahead."
    show com_base_img
    hide spr_com_11_img
    show spr_com_12_img at spr_com_upper
    "You advance toward the source of the noise, with Zali and Wilson trailing a few steps behind you."
    zali_char "You see anything, Vanta?"
    hide spr_com_12_img
    show spr_com_13_img at spr_com_upper 
    vanta_char "It... It's a fox?"
    vanta_char "No, it's a puppy."
    play sound "audio/spr/spr_se_scrape.mp3" #Dog scratching sound
    "You turn your body sideways to show Zali and Wilson. Inside a small metal cage, an anxious puppy bites and scratches, whining with unease; its eyes pleading to be released."
    "You glance at the nearby table, suspecting that the puppy may have pushed the cage, causing it to fall to the floor and result in the noises you heard."
    wilson_char "Oh my god, it is sho small! Sho cyute!!"
    wilson_char "Is it a boy? Oh yeah, it's a boy."
    zali_char "We need to be careful; we don't know if the puppy is already part of an experiment."
    play sound "audio/spr/spr_se_padlock.mp3" #Sound of breaking a padlock
    hide spr_com_13_img
    show spr_com_14_img at spr_com_upper
    "You grab the padlock on the cage and forcefully remove it, startling the puppy. It starts to run aimlessly in all directions within the cage, letting out loud cries."
    play sound "audio/spr/spr_se_dog.mp3" #Puppy noises
    "You quickly extend your hand into the cage, scooping the puppy into your arms. Miraculously, the moment it's in your embrace, it becomes docile immediately."
    vanta_char "Don't worry, buddy. We'll get you out of here."
    wilson_char "Seems like your tyrant reputation does wonders for calming down the puppy!"
    "You inspect the puppy more closely. He's a red Shiba Inu boy, likely just 2-3 months old."
    "His paws are white, resembling tiny socks, and his belly is a soft cream color. His tail, mostly brown with a black tip, is curled up like a bun, giving him the appearance of a baby fox."
    hide spr_com_14_img
    show spr_com_15_img at spr_com_upper
    play sound "audio/spr/spr_se_keyboard.mp3" #keyboard sound
    zali_char "Oh my goodness. According to this data, the company was completely surprised by the effect of the octopus when it accidentally consumed a highly concentrated dosage of the mushroom solution. "
    zali_char "Now, they want to replicate these results by testing it on other animals. And this puppy is one of their test subjects."
    "Zali sifts through the recorded data on the computer, finding clips of the octopus incident captured by other witnesses. Among the files are numerous test results indicating ongoing experiments. "
    "Zali transfers the data from the computer to Tsuchi's cloud system, ensuring it reaches A.S.H.'s intel department promptly."
    wilson_char "Mild consumption might induce agitation or excessive excitement. With an increased dosage, it could lead to significant changes in physical ability..."
    wilson_char "Wait, Vanta, didn't you try that drink?"
    vanta_char "I did! But I didn't feel anything. Because I am not a lightweight."
    zali_char "Didn't we also eat the mushroom dishes in the mountain village?\nYou ate a lot at the time, Vanta."
    vanta_char "Well, it was pretty low-calorie, you know... But if that's the case, will my body mutate?"
    hide spr_com_15_img
    show spr_com_16_img at spr_com_upper
    zali_char "Hmm, here's my theory... Perhaps your body simply reacted differently, and the substance didn't affect you."
    zali_char "Given that you've participated in a few trials and tests since joining A.S.H., you're essentially my test subject too. Maybe that's why you weren't affected."
    wilson_char "What the hell? That's pretty cool, though, isn't it? Maybe I should've eaten more of those mushrooms."
    wilson_char "Who knows? Maybe I'd become taller, stronger, and finally an ikemen."
    "You and Zali exchange a knowing glance, silently agreeing to let Wilson continue living in his delusion."
    hide spr_com_16_img
    show spr_com_17_img at spr_com_upper
    "The little puppy stays snug in your arms, appearing quite comfortable. You lift him up to your face, and he gazes at you with a big smile, filling you with an indescribable burst of joy."
    "Your nose meets his in a gentle boop as you gaze into his big, round, black eyes."
    vanta_char "You were just a nameless Shiba without a home, but not anymore. From this moment forward, you belong to me, Vantacrow Bringer. You are my puppy."
    hide spr_com_17_img
    scene spr_st_fny_img
    # show text "{b}{size=34}Chapter 4.  SPRING{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with fade
    pause 2.0  
    "You're responded to with a big yawn, followed by the puppy's paws shoving against your face."
    zandw_char "Hahahahahaha!"
    ### achievement package ###
    if (achievement.has('spr_st_fny')== False):   
        $ achievement.grant('spr_st_fny')        
        # show screen OverlayScreen1
        # show screen ClickableArea
        python:
            active_set = "cg"
            active_tab = "tab4"
    ### achievement package ###
    hide spr_st_fny_img
    scene spr_bg_lab2_img at earthquake_before
    # show text "{b}{size=34}Chapter 4.  SPRING{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    show com_base_img
    show spr_com_18_img at spr_com_upper
    with fade
    vanta_char "Okay, now here's the question..."
    vanta_char "How do I get out of this building with you?"
    zali_char "Oh. Let me handle this, I am so good with bondage, I will wrap him onto your back. Let's go!"
    wilson_char "Alright then! Are we ready to go, guys?"
    stop music fadeout 1.0  # Fade out music
    play music "audio/sum/sum_bgm_02.mp3" fadein 1.0 loop #Music for Battle
    hide spr_com_18_img
    hide spr_bg_lab2_img
    scene spr_bg_hall1_img
    show spr_com_19_img at spr_com_upper
    "Seeing Wilson's signal, you spring into action, activating the fire alarm. The loud, echoing sirens reverberate throughout the entire building, filling every corner with urgency. "
    hide spr_bg_hall1_img
    scene spr_bg_hall2_img
    show spr_com_19_img at spr_com_upper
    play sound "audio/spr/spr_se_firealarm.mp3" #Fire alarm
    "Within moments, crimson lights flood each room, signaling the need for immediate evacuation, prompting people to swiftly leave the building."
    stop sound fadeout 2.0 #Stop sound effects
    wilson_char "Team Krisis to Squad A, come in. This is it."
    wilson_char "We have successfully retrieved the evidence and we are good to go."
    wilson_char "{size=35}ETA on our exit: 4 minutes, 20 seconds.{/size}"
    wilson_char "You are clear to initiate building demolition at the same time. Over."
    vanta_char "{size=35}Let's move out! Follow me!{/size}"
    hide spr_com_19_img
    show spr_com_20_img at spr_com_upper 
    "As several security personnel charge towards you, you brace yourself for a fight. However, before you can react, they all collapse in front of you. Turning around, you see Zali holding his tranquilizer gun."
    zali_char "{size=35}No time to waste, let's move!{/size}"
    play sound "audio/spr/spr_se_firealarm.mp3" #Fire alarm
    "With the majority of people already evacuated due to the blaring siren, the three of you make your way to the ground floor. Racing towards the front door, you can see Squad A standing by, prepared to detonate."
    play sound "audio/spr/spr_se_explosion.mp3" #Explosion sound
    hide spr_com_20_img
    scene spr_bg_hall2_img at earthquake
    # show text "{b}{size=34}Chapter 4.  SPRING{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    show com_base_img
    show spr_com_21_img at spr_com_upper
    "Squad A spots your exit. With a quick gesture, the explosion detonates, sending shockwaves rippling through the structure."
    play sound "audio/spr/spr_se_ground.mp3" #rumble in the ground
    "As the shockwave pushes against you, you suddenly remember the puppy secured on your back. With quick reflexes, you twist your body, shielding the puppy from the full force of the blast."
    scene spr_bg_buil1_img
    # show text "{b}{size=34}Chapter 4.  SPRING{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    with fade 
    "Smoke rises into the sky as the once-standing building structure becomes rubble in a matter of seconds."
    show com_base_img
    hide spr_com_21_img
    show spr_com_22_img at spr_com_upper
    zandw_char "{size=50}VANTA!!!{/size}"
    "Your body is propelled backward by the force of the explosion, sending you plummeting towards the ground."
    zandw_char "{size=50}Arghhhhhh!!!{/size}"
    hide spr_com_22_img
    show spr_com_23_img at spr_com_upper 
    "Zali yanks the harness on your chest, pulling your body towards him. With lightning speed, Wilson rushes forward and spins around to support your shoulders and shield the puppy."
    wilson_char "Whooo! I got him! He's all good!"
    "As the sky clears and the dust settles, the rush of adrenaline causes your heart to race."
    zali_char "Phew! Thank goodness for that safety belt thingy, or I wouldn't have been able to grab you in time."
    vanta_char "... Thanks bro."
    hide spr_com_23_img
    show spr_com_24_img at spr_com_upper 
    wilson_char "Excusez-moi, guys! Find your footing, or you're going to squash me."
    "You feel Wilson's hands shaking behind you as you stand up properly. Zali releases his grip on your harness a bit too quickly, causing the harness to snap back onto your chest with a crisp, loud whip."
    play sound "audio/spr/spr_se_belt.mp3" #The sound of a belt
    stop music fadeout 3.0  # Fade out music
    vanta_char "{size=45}AHHHHH!!! F—THAT HURTS!!!{/size}"
    zali_char "Ah hahah, sorry Vanta!!"
    play music "audio/spr/spr_bgm_01.mp3" loop fadein 1.0  #Loop playback with song fade-in  
    hide spr_com_24_img
    show spr_com_25_img at spr_com_upper 
    "You turn around to check if the puppy is okay, and to your relief, he gazes up at you and proceeds to lick your ear affectionately."
    wilson_char "Looks like another successful mission for us! Shall we leave the rest to the team?"
    wilson_char "Let's head back and ensure Vanta wasn't impacted by the blast."
    zali_char "Yeah, Wilson has a point. Vanta, you feeling alright?"
    "There's a hint of melancholy in your voice as you take a deep breath, the flashbacks still vivid in your mind."
    "The fact that your teammates will do anything for you, even in the most dangerous moments, fills you with an overwhelming warmth."
    vanta_char "I believe... I feel alright. Perhaps I wasn't impacted by the mushrooms. It's been quite a year, with its ups and downs. I have my moments of vulnerability, and sometimes I tend to overthink things."
    hide spr_com_25_img
    show spr_com_26_img at spr_com_upper
    "Just then, the Vezcrewneers arrive, surrounding the three of you with their cheerful presence, a constant reminder of the support you've had every step of the way."
    vanta_char "The Vantacrow Bringer from the past was alone, but not anymore. I couldn't have made it this far without you guys."
    "Zali places a reassuring hand on your shoulder. "
    zali_char "You're doing great, Vanta. We're all in this together.\nI mean, we may be Kris sometimes, but we are always Krisis, forever."
    "Wilson nods, a grin spreading across his face. He lightly bumps your chest with his fist."
    wilson_char "Absolutely. You've come a long way since we first teamed up.\nEven if you always disagree with me, I will always have your back."
    scene spr_bg_buil2_img
    # show text "{b}{size=34}Chapter 4.  SPRING{/size}{/b}" at Position(xalign=0.03, yalign=0.03)
    show van_hr_nor at center    
    show wil_hr_nor at right
    show zal_hr_nor at left
    with fade 
    "As you look at everyone surrounding you, a swell of pride fills your chest."
    hide wil_hr_nor
    hide zal_hr_nor
    hide van_hr_nor
    show van_hr_hap at center    
    show wil_hr_hap at right
    show zal_hr_hap at left
    "Laughter bubbles up, echoing the silliness and bickering you've shared. Even the puppy on your back gives you a little nudge of encouragement with his head."
    "Together, you all laugh, sharing a moment that solidifies the countless memories you've made. You feel a profound sense of belonging, knowing you've found a family in these two."
    "Under the gentle sway of cherry blossoms and their petals carpeting the ground, you link arms with Zali and Wilson, stepping away from the debris behind you."
    "As you move forward, the flowers signal the arrival of a new season. With each step, you embrace the promise of many seasons ahead—filled with love, support, and adventures waiting to unfold."
    "Cherry blossoms will continue bloom."
    pause 0.8
    stop music fadeout 4.0  # Fade out music
    hide wil_hr_hap with dissolve
    hide zal_hr_hap with dissolve
    hide van_hr_hap with dissolve
    play music "audio/main_theme.mp3" fadein 5.0 loop #Music for Battle
    ### achievement package ###
    if (achievement.has('spr_st_edcg')== False) or(achievement.has('spr_gallery')== False):
        $ achievement.grant('spr_st_edcg')#the ending cg video
        $ achievement.grant('spr_gallery')
        python:
            active_set = "gallery"
            active_tav = "tab4"
    # no need to notify in the end(?)        
    #     show screen OverlayScreen1
    #     show screen ClickableArea
    # ### achievement package ###
    # ### ending screen ###
    # show screen OverlayScreen

    # ユーザーがクリックするまで待つ
    # pause 1.0
    # show white with dissolve 
    pause 3.0
    show screen unclickable_screen
    $ renpy.movie_cutscene("movies/spr_animation.webm", stop_music=False)
    $ renpy.movie_cutscene("movies/credits_v3.webm", stop_music=False)
    hide screen unclickable_screen
    # $ renpy.show_screen("main_menu")  
    return