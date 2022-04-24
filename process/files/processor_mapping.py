from collections import defaultdict

from files.armory_collections.armory_collections import \
    ArmoryCollectionsProcessor
from files.armory_gears.armory_gears import ArmoryGearsProcessor
from files.armory_stat_progressions.armory_stat_progressions import \
    ArmoryStatProgressionsProcessor
from files.armory_stat_sets.armory_stat_sets import ArmoryStatSetsProcessor
from files.gear_set_progressions.gear_set_progressions import \
    GearSetProgressionsProcessor
from files.gear_sets.gear_sets import GearSetsProcessor
from files.gear_stat_progressions.gear_stat_progressions import \
    GearStatProgressionsProcessor
from files.gear_stat_sets.gear_stat_sets import GearStatSetsProcessor
from files.gears.gears import GearsProcessor
from files.hero_collection_action_progressions.hero_collection_action_progressions import \
    HeroCollectionActionProgressionsProcessor
from files.hero_collection_action_properties.hero_collection_action_properties import \
    HeroCollectionActionPropertiesProcessor
from files.hero_collection_actions.hero_collection_actions import \
    HeroCollectionActionsProcessor
from files.hero_progressions.hero_progressions import HeroProgressionsProcessor
from files.hero_skill_progressions.hero_skill_progressions import \
    HeroSkillProgressionsProcessor
from files.hero_skills.hero_skills import HeroSkillsProcessor
from files.heroes.heroes import HeroesProcessor
from files.items.items import ItemsProcessor
from files.properties.properties import PropertiesProcessor
from files.summon_odds.summon_odds import SummonOddsProcessor
from files.summons.summons import SummonsProcessor
from files.translations.translations import TranslationsProcessor
from files.trinket_gear_sets.trinket_gear_sets import TrinketGearSetsProcessor
from files.recurring_rewards.recurring_rewards import RecurringRewardsProcessor

FILE_PROCESSOR_MAPPING_CONFIG = {
    ('GearSetTable', 'json', 'gear_set_1', GearSetsProcessor),
    ('GearsetTable_GearGen_GearSets', 'json',
     'gear_set_2', GearSetsProcessor),
    ('GearSetTable_Trinkets', 'json',
     'trinket_gear_sets', TrinketGearSetsProcessor),
    ('GearSetProgressions', 'pb', 'gear_set_progressions_1',
     GearSetProgressionsProcessor),
    ('ProgressionTable_GearGen_GearSets', 'pb', 'gear_set_progressions_2',
     GearSetProgressionsProcessor),
    ('GearTable', 'pb', 'gears_1', GearsProcessor),
    ('ItemTable_GearGen_GearSets', 'pb', 'gears_2', GearsProcessor),
    ('ItemTable_GearGen_Trinkets', 'pb', 'trinket_gears', GearsProcessor),
    ('GearTable_PropertyModderTable', 'pb',
     'gear_stat_sets_1', GearStatSetsProcessor),
    ('ItemTable_GearGen_GearSets_PropertyModderTable',
     'pb', 'gear_stat_sets_2', GearStatSetsProcessor),
    ('ItemTable_GearGen_Trinkets_PropertyModderTable',
     'pb', 'trinket_gear_stat_sets', GearStatSetsProcessor),
    ('GearProgressions', 'pb', 'gear_stat_progressions', GearStatProgressionsProcessor),
    ('ArmoryCollectionsTable', 'pb',
     'armory_collections_1', ArmoryCollectionsProcessor),
    ('ArmoryCollectionTable_GearGen_GearSets', 'pb',
     'armory_collections_2', ArmoryCollectionsProcessor),
    ('ArmoryCollectionsTable_ArmoryPropertyModderTable', 'pb',
     'armory_stat_sets_1', ArmoryStatSetsProcessor),
    ('ArmoryCollectionTable_GearGen_GearSets_ArmoryPropertyModderTable', 'pb',
     'armory_stat_sets_2', ArmoryStatSetsProcessor),
    ('ArmoryPropertyProgressions', 'pb',
     'armory_stat_progressions', ArmoryStatProgressionsProcessor),
    ('GearTable_ArmoryGearTable', 'json', 'armory_gears_1', ArmoryGearsProcessor),
    ('ItemTable_GearGen_GearSets_ArmoryGearTable',
     'json', 'armory_gears_2', ArmoryGearsProcessor),
    ('ItemTable_GearGen_Trinkets_ArmoryGearTable',
     'json', 'armory_gears_3', ArmoryGearsProcessor),
    ('HeroTable_VisGen_Launch', 'json', 'heroes', HeroesProcessor),
    ('HeroProgressions', 'json', 'hero_progressions', HeroProgressionsProcessor),
    ('HeroSkillsTable_VisGen_Launch', 'json', 'hero_skills', HeroSkillsProcessor),
    ('HeroPropertyProgressions_VisGen_Launch', 'pb',
     'hero_skill_progressions', HeroSkillProgressionsProcessor),
    ('HeroCollectionActionTable', 'json',
     'hero_collection_actions', HeroCollectionActionsProcessor),
    ('HeroCollectionActionProgressions', 'json',
     'hero_collection_action_progressions', HeroCollectionActionProgressionsProcessor),
    ('HeroCollectionActionPropertyProgressions', 'pb',
     'hero_collection_action_properties', HeroCollectionActionPropertiesProcessor),
    ('SummonTable', 'json', 'summons', SummonsProcessor),
    ('SummoningOddsTable', 'pb', 'summon_odds', SummonOddsProcessor),
    ('ItemTable', 'pb', 'items', ItemsProcessor),
    ('ItemTable_Heroes', 'pb', 'hero_items', ItemsProcessor),
    ('ItemTable_Dragon_1', 'pb', 'dragon_items', ItemsProcessor),
    ('ItemTable_Gift_1', 'pb', 'items_gift', ItemsProcessor),
    ('ItemTable_Event_1', 'pb', 'items_event', ItemsProcessor),
    ('AnnuitiesTable', 'pb', 'recurring_rewards', RecurringRewardsProcessor),
    ('PropertyTable', 'pb', 'properties', PropertiesProcessor),
    ('enUS', 'txt', 'translations', TranslationsProcessor)
}


def _preprocess_mapping_config(config):
    mapping = defaultdict(dict)
    for file_name, file_extension, output_id, processor_class in config:
        mapping[file_name][file_extension] = (output_id, processor_class)
    return mapping


FILE_PROCESSOR_MAPPING = _preprocess_mapping_config(
    FILE_PROCESSOR_MAPPING_CONFIG)


def find_processor(file_name, file_extension):
    if file_name in FILE_PROCESSOR_MAPPING and file_extension in FILE_PROCESSOR_MAPPING[file_name]:
        return FILE_PROCESSOR_MAPPING[file_name][file_extension]
    return None
