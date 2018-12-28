#!/bin/sh
PWD=$(pwd)
export PYTHONPATH="$PWD:$PWD/Header:$PWD/ID:$PWD/Process"
python -B "Process/process_init.py"
python -B "Process/process_global_variables.py"
python -B "Process/process_strings.py"
python -B "Process/process_skills.py"
python -B "Process/process_music.py"
python -B "Process/process_animations.py"
python -B "Process/process_meshes.py"
python -B "Process/process_sounds.py"
python -B "Process/process_skins.py"
python -B "Process/process_map_icons.py"
python -B "Process/process_factions.py"
python -B "Process/process_items.py"
python -B "Process/process_scenes.py"
python -B "Process/process_troops.py"
python -B "Process/process_particle_sys.py"
python -B "Process/process_scene_props.py"
python -B "Process/process_tableau_materials.py"
python -B "Process/process_presentations.py"
python -B "Process/process_party_tmps.py"
python -B "Process/process_parties.py"
python -B "Process/process_quests.py"
python -B "Process/process_info_pages.py"
python -B "Process/process_scripts.py"
python -B "Process/process_mission_tmps.py"
python -B "Process/process_game_menus.py"
python -B "Process/process_simple_triggers.py"
python -B "Process/process_dialogs.py"
python -B "Process/process_global_variables_unused.py"
python -B "Process/process_postfx.py"
