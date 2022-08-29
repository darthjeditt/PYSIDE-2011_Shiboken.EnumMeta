# -*- coding: utf-8 -*-
'''Shotgun config'''

from __future__ import annotations


class Shotgun:
    '''ShotGrid credentials and config'''

    host = 'https://proxi-vp.shotgunstudio.com'
    clientId = 'App_Unreal'
    clientSecret = 'Hbsau&qvor4xellhnufopdgnk'
    debugProjectId = 650 # `Dan's Secret Page 2021-03-30`
    devPassThroughProjects = [
        815 # `Dan's TNIB Clone`
    ]

    class Entity:
        '''Entity types'''

        project = 'Project'
        camera = 'Camera'
        version = 'Version'
        playlist = 'Playlist'
        shot = 'Shot'
        cut = 'Cut'
        cutItem = 'CutItem'
        sequence = 'Sequence'
        subSequence = 'CustomEntity07'
        sequenceMaster = 'CustomEntity04'
        scriptConfig = 'CustomNonProjectEntity02'
        note = 'Note'
        user = 'HumanUser'
        adCharacter = 'CustomEntity31'
        adStuntCharacter = 'CustomEntity37'
        adVehicle = 'CustomEntity38'
        assetLink = 'CustomEntity28'
        adDood = 'customEntity39'
        asset = 'Asset'

    class RequestType:
        '''Request types, usually only specified in batch CRUD methods'''

        create = 'create'
        update = 'update'
        delete = 'delete'

    class ProjectStatus:
        '''Project status codes'''

        bidding = 'Bidding'
        active = 'Active'
        lost = 'Lost'
        hold = 'Hold'
        completed = 'Completed'

    class NoteType:
        '''Note types'''

        animationMobu = 'Animation-Mobu'
        animationUe4 = 'Animation-UE4'
        techViz = 'TechViz'
        asset = 'Asset'
        camera = 'Camera'
        cut = 'Cut'
        client = 'Client'
        environment = 'Environment'
        fx = 'FX'
        internal = 'Internal'
        lighting = 'Lighting'
        misc = 'Miscellaneous'
        pipeline = 'Pipeline'
        rd = 'R&D'
        render = 'Render'

    class NoteStatus:
        '''Note status codes'''

        open = 'opn'
        dumpsterFire = 'fire'
        inProgress = 'ip'
        closed = 'clsd'
        approved = 'apr'
        waiting = 'wtg'
        onHold= 'hld'
        omit = 'omt'
        qc = 'qc'
        pendingReview = 'rev'
        returned = 'rtn'
        complete = 'cmpt'
        needsRender = 'ren'

    class Fields:
        '''Default field requests'''

        _default = ['id', 'code', 'sg_status', 'sg_status_list', 'sg_metadata', 'description']
        project = _default + ['name', 'archived', 'is_template', 'is_template_project']
        camera = _default + ['sg_camera_type', 'sg_camera_lens', 'sg_lens_kit']
        shot = _default + ['sg_camera_type_1', 'sg_camera_lens', 'sg_camera_framing', 'sg_camera_description', 'sg_sub_sequence', 'sg_sub_sequence.CustomEntity07.sg_sequence', 'sg_ue_guid', 'sg_auto_set_ranges', 'sg_frame_in', 'sg_frame_out']
        sequence = _default
        subSequence = _default
        cut = _default
        asset = _default
        note = _default + ['subject', 'content', 'sg_note_type', 'sg_urgency', 'sg_status_list', 'metadata']
        cutItem = _default + ['cut_order', 'edit_in', 'edit_out', 'cut_item_in', 'cut_item_out', 'cut_item_duration', 'timecode_edit_in_text', 'timecode_edit_out_text', 'timecode_cut_item_in_text', 'timecode_cut_item_out_text', 'version', 'shot', 'shot.Shot.description', 'shot.Shot.sg_camera_framing']
        sequenceMaster = _default + ['sg_sub_sequence', 'sg_sub_sequence.CustomEntity07.sg_sequence', 'sg_sub_sequence.CustomEntity07.sg_sequence.Sequence.sg_sequence_name']
        # assetLink = _default + ['sg_asset_link_type', 'sg_sequence.Sequence.code', 'sg_abbreviation.CustomEntity25.sg_full_name', 'sg_ad_link.CustomEntity31.sg_id']
        assetLink = _default + ['sg_asset_link_type', 'sg_sequence.Sequence.code', 'sg_ad_dood.CustomEntity39.sg_ad_id', 'sg_ad_dood.CustomEntity39.sg_type', 'sg_ad_dood.CustomEntity39.sg_ad_name', 'sg_ad_dood.CustomEntity39.sg_ad_name_raw', 'sg_cg']
        version = _default + ['sg_version_num', 'sg_version_type', 'sg_version_sub_type', 'path_to_movie']

    class AssetLinkTypeMapping:
        '''Lookup/mapping between Shotgun value for field `sg_asset_link_type` and Unreal display value

        Public static access method via one-way method `getUnrealValue`
        '''

        # Lower-case keys!
        _lookup = {
            'cast': 'cst',
            'creature': 'cre',
            'dummy': 'dum',
            'extra': 'xta',
            'stunt': 'stu',
            'vehicle': 'vhl'
        }

        @classmethod
        def getUnrealValue(cls, shotgunType: str|None):
            '''Retrieve the corresponding Unreal display value for Shotgun key

            Args:
                shotgunType (str): Value from `CustomEntity28.sg_asset_link_type`

            Returns:
                str|None: Mapped display value if found, None otherwise
            '''

            if not shotgunType:
                return None

            return cls._lookup.get(shotgunType.lower())