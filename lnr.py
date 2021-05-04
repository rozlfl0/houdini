def set_aov_beauty():
    arnolds = getArnolds()

    if not arnolds:
        hou.ui.displayMessage('select renderer')

    else:

        for i in arnolds:
            aovs_count = i.parm('ar_aovs').eval()
            i.parm('ar_aovs').set(aovs_count + 1)
            aov_label_num = i.parm('ar_aovs').eval()
            i.parm('ar_aov_label{}'.format(aov_label_num)).set('diffuse_direct')

            aovs_count = i.parm('ar_aovs').eval()
            i.parm('ar_aovs').set(aovs_count + 1)
            aov_label_num = i.parm('ar_aovs').eval()
            i.parm('ar_aov_label{}'.format(aov_label_num)).set('diffuse_indirect')

            aovs_count = i.parm('ar_aovs').eval()
            i.parm('ar_aovs').set(aovs_count + 1)
            aov_label_num = i.parm('ar_aovs').eval()
            i.parm('ar_aov_label{}'.format(aov_label_num)).set('specular_direct')

            aovs_count = i.parm('ar_aovs').eval()
            i.parm('ar_aovs').set(aovs_count + 1)
            aov_label_num = i.parm('ar_aovs').eval()
            i.parm('ar_aov_label{}'.format(aov_label_num)).set('specular_indirect')

            aovs_count = i.parm('ar_aovs').eval()
            i.parm('ar_aovs').set(aovs_count + 1)
            aov_label_num = i.parm('ar_aovs').eval()
            i.parm('ar_aov_label{}'.format(aov_label_num)).set('transmission_direct')

            aovs_count = i.parm('ar_aovs').eval()
            i.parm('ar_aovs').set(aovs_count + 1)
            aov_label_num = i.parm('ar_aovs').eval()
            i.parm('ar_aov_label{}'.format(aov_label_num)).set('transmission_indirect')

            aovs_count = i.parm('ar_aovs').eval()
            i.parm('ar_aovs').set(aovs_count + 1)
            aov_label_num = i.parm('ar_aovs').eval()
            i.parm('ar_aov_label{}'.format(aov_label_num)).set('sss_direct')

            aovs_count = i.parm('ar_aovs').eval()
            i.parm('ar_aovs').set(aovs_count + 1)
            aov_label_num = i.parm('ar_aovs').eval()
            i.parm('ar_aov_label{}'.format(aov_label_num)).set('sss_indirect')

            aovs_count = i.parm('ar_aovs').eval()
            i.parm('ar_aovs').set(aovs_count + 1)
            aov_label_num = i.parm('ar_aovs').eval()
            i.parm('ar_aov_label{}'.format(aov_label_num)).set('occ')

            aovs_count = i.parm('ar_aovs').eval()
            i.parm('ar_aovs').set(aovs_count + 1)
            aov_label_num = i.parm('ar_aovs').eval()
            i.parm('ar_aov_label{}'.format(aov_label_num)).set('emission')
            i.parm('ar_aov_lpe_enable{}'.format(aov_label_num)).set(1)
            i.parm('ar_aov_lpe{}'.format(aov_label_num)).set('C.*O')

            aovs_count = i.parm('ar_aovs').eval()
            i.parm('ar_aovs').set(aovs_count + 1)
            aov_label_num = i.parm('ar_aovs').eval()
            i.parm('ar_aov_label{}'.format(aov_label_num)).set('N')

            aovs_count = i.parm('ar_aovs').eval()
            i.parm('ar_aovs').set(aovs_count + 1)
            aov_label_num = i.parm('ar_aovs').eval()
            i.parm('ar_aov_label{}'.format(aov_label_num)).set('P')

            aovs_count = i.parm('ar_aovs').eval()
            i.parm('ar_aovs').set(aovs_count + 1)
            aov_label_num = i.parm('ar_aovs').eval()
            i.parm('ar_aov_label{}'.format(aov_label_num)).set('Z')

            aovs_count = i.parm('ar_aovs').eval()
            i.parm('ar_aovs').set(aovs_count + 1)
            aov_label_num = i.parm('ar_aovs').eval()
            # i.parmTuple('ar_aov_pixel_filter{}'.format(aov_label_num)).set('4')
            i.parm('ar_aov_label{}'.format(aov_label_num)).set('zdepth')

            aovs_count = i.parm('ar_aovs').eval()
            i.parm('ar_aovs').set(aovs_count + 1)
            aov_label_num = i.parm('ar_aovs').eval()
            i.parm('ar_aov_label{}'.format(aov_label_num)).set('crypto_material')

            aovs_count = i.parm('ar_aovs').eval()
            i.parm('ar_aovs').set(aovs_count + 1)
            aov_label_num = i.parm('ar_aovs').eval()
            i.parm('ar_aov_label{}'.format(aov_label_num)).set('crypto_object')

            aovs_count = i.parm('ar_aovs').eval()
            i.parm('ar_aovs').set(aovs_count + 1)
            aov_label_num = i.parm('ar_aovs').eval()
            i.parm('ar_aov_label{}'.format(aov_label_num)).set('crypto_asset')

            hou.ui.displayMessage('Succeed!')


def set_aov_utility():
    ar_vop = hou.node('/shop/').createNode('arnold_vopnet', 'Utility')
    ar_vop.children()[0].destroy()

    # connet render
    utility_aov = ar_vop.createNode('arnold_aov', 'utility_aov')

    # create occ
    occ_mat = ar_vop.createNode('arnold::ambient_occlusion', 'occ_mat')
    occ_write = ar_vop.createNode('arnold::aov_write_rgb', 'occ_write')
    # connect
    utility_aov.setInput(0, occ_write)
    occ_write.setInput(1, occ_mat)
    # parm
    occ_write.parm('aov_name').set('occ')

    # create zdepth
    zdepth_float = ar_vop.createNode('arnold::state_float', 'zdepth_float')
    zdepth_range = ar_vop.createNode('arnold::range', 'zdepth_range')
    zdepth_write = ar_vop.createNode('arnold::aov_write_rgb', 'zdepth_write')
    # connect
    utility_aov.setInput(1, zdepth_write)
    zdepth_write.setInput(1, zdepth_range)
    zdepth_range.setInput(0, zdepth_float)
    # parm
    zdepth_float.parmTuple('variable').set('5')
    zdepth_range.parm('smoothstep').set('1')
    zdepth_write.parm('aov_name').set('zdepth')

    # create crytomatte
    cryptomatte = ar_vop.createNode('arnold::cryptomatte')

    # connect
    utility_aov.setInput(2, cryptomatte)

    ar_vop.layoutChildren()

    hou.ui.displayMessage('Succeed!')


def getLights():
    selnode = hou.selectedNodes()
    lights_list = []
    for light in selnode:
        if light.type().name() == 'arnold_light':
            lights_list.append(light)
        else:
            pass
    return lights_list


def getArnolds():
    selnode = hou.selectedNodes()
    arnold_list = []
    for arnold in selnode:
        if arnold.type().name() == 'arnold':
            arnold_list.append(arnold)
    return arnold_list


def lightLen():
    lit_len = len(getLights())
    return lit_len


def chooseState():
    user_selection = hou.ui.displayMessage("Light & Render", close_choice=4, title="LNR",
                                           buttons=(
                                           "Lit_Grp_Name", "Create_LPE", "Shop_Utility", "Create_PBR_Aovs", "Close"))
    return user_selection


def setLightGroupName():
    lights = getLights()

    if not lights:
        hou.ui.displayMessage('select light node')

    else:
        for i in lights:
            i.parm('ar_aov').set(i.name())

        hou.ui.displayMessage('Succeed!')


def createLPE():
    lights = getLights()
    arnolds = getArnolds()
    lit_len = lightLen()

    if not arnolds and lights:
        hou.ui.displayMessage('select renderer and light node')

    else:

        for i in lights:

            for x in arnolds:
                aovs_count = x.parm('ar_aovs').eval()
                x.parm('ar_aovs').set(aovs_count + 1)
                aov_label_num = x.parm('ar_aovs').eval()
                x.parm('ar_aov_label{}'.format(aov_label_num)).set(i.parm('ar_aov').eval() + '_diffuse')
                x.parm('ar_aov_lpe_enable{}'.format(aov_label_num)).set(1)
                x.parm('ar_aov_lpe{}'.format(aov_label_num)).set("C<RD>.*<L.'{}'>".format(i.parm('ar_aov').eval()))

        for i in lights:

            for x in arnolds:
                aovs_count = x.parm('ar_aovs').eval()
                x.parm('ar_aovs').set(aovs_count + 1)
                aov_label_num = x.parm('ar_aovs').eval()
                x.parm('ar_aov_label{}'.format(aov_label_num)).set(i.parm('ar_aov').eval() + '_specular')
                x.parm('ar_aov_lpe_enable{}'.format(aov_label_num)).set(1)
                x.parm('ar_aov_lpe{}'.format(aov_label_num)).set(
                    "C<RS[^'coat']>.*<L.'{}'>".format(i.parm('ar_aov').eval()))

        hou.ui.displayMessage('Succeed!')


def setLPE(state):
    if state == 0:
        setLightGroupName()

    elif state == 1:
        createLPE()

    elif state == 2:
        set_aov_utility()

    elif state == 3:
        set_aov_beauty()


setLPE(chooseState())
