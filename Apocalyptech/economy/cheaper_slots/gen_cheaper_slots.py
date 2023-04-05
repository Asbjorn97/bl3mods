#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This Borderlands 3 Hotfix Mod is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This Borderlands 3 Hotfix Mod is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this Borderlands 3 Hotfix Mod.  If not, see
# <https://www.gnu.org/licenses/>.

import sys
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('cheaper_slots.bl3hotfix',
        'Cheaper Slots',
        'Apocalyptech',
        [
            "Makes the slot machines found through Borderlands 3 cheaper to use.",
            "Not much point, really, since there's nothing unique you can get from",
            "these that you can't get by just playing the game, but here it is",
            "regardless.",
        ],
        contact='https://apocalyptech.com/contact.php',
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='cheat, economy, slots',
        )

levels_money = [
        'Sanctuary3_P',
        'AtlasHQ_P',
        'OrbitalPlatform_P',
        'Mansion_P',
        'CasinoIntro_P',
        'Core_P',
        'Bar_P',
        'Town_P',
        ]

levels_eridium = [
        'Sanctuary3_P',
        'Bar_P',
        ]

mod.comment('Money-based machines')
for level in levels_money:
    mod.reg_hotfix(Mod.LEVEL, level,
            '/Game/UI/InteractionPrompt/UIData_PlaySlots',
            'Cost.BaseValueScale',
            0.2)
mod.newline()

mod.comment('Eridium-based machines')
for level in levels_eridium:
    mod.reg_hotfix(Mod.LEVEL, level,
            '/Game/UI/InteractionPrompt/UIData_PlaySlotsEridium',
            'Cost.BaseValueScale',
            0.2)
mod.newline()

mod.close()

