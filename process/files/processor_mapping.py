from collections import defaultdict

from files.armory_collections.armory_collections import ArmoryCollectionsProcessor
from files.armory_gears.armory_gears import ArmoryGearsProcessor
from files.armory_stat_progressions.armory_stat_progressions import (
    ArmoryStatProgressionsProcessor,
)
from files.buildings.buildings import BuildingsProcessor
from files.event_scoring_progressions.event_scoring_progressions import (
    EventScoringProgressionsProcessor,
)
from files.gear_set_progressions.gear_set_progressions import (
    GearSetProgressionsProcessor,
)
from files.gear_sets.gear_sets import GearSetsProcessor
from files.gear_stat_progressions.gear_stat_progressions import (
    GearStatProgressionsProcessor,
)
from files.gears.gears import GearsProcessor
from files.hero_collection_action_progressions.hero_collection_action_progressions import (
    HeroCollectionActionProgressionsProcessor,
)
from files.hero_collection_action_properties.hero_collection_action_properties import (
    HeroCollectionActionPropertiesProcessor,
)
from files.hero_collection_actions.hero_collection_actions import (
    HeroCollectionActionsProcessor,
)
from files.hero_progressions.hero_progressions import HeroProgressionsProcessor
from files.hero_skill_progressions.hero_skill_progressions import (
    HeroSkillProgressionsProcessor,
)
from files.hero_skills.hero_skills import HeroSkillsProcessor
from files.hero_traits.hero_traits import HeroTraitsProcessor
from files.heroes.heroes import HeroesProcessor
from files.items.items import ItemsProcessor
from files.progressions.progressions import ProgressionsProcessor
from files.properties.properties import PropertiesProcessor
from files.recipe_ingredient_sets.recipe_ingredient_sets import (
    RecipeIngredientSetsProcessor,
)
from files.recipes.recipies import RecipesProcessor
from files.recurring_rewards.recurring_rewards import RecurringRewardsProcessor
from files.research_categories.research_categories import ResearchCategoriesProcessor
from files.researches.researches import ResearchesProcessor
from files.stat_sets.stat_sets import StatSetsProcessor
from files.summon_odds.summon_odds import SummonOddsProcessor
from files.summons.summons import SummonsProcessor
from files.translations.translations import TranslationsProcessor
from files.trinket_gear_sets.trinket_gear_sets import TrinketGearSetsProcessor
from files.troops.troops import TroopsProcessor

FILE_PROCESSOR_MAPPING_CONFIG = {
    ("GearSetTable", "json", "gear_set_1", GearSetsProcessor),
    ("GearsetTable_GearGen_GearSets", "json", "gear_set_2", GearSetsProcessor),
    ("GearSetTable_Trinkets", "json", "trinket_gear_sets", TrinketGearSetsProcessor),
    (
        "GearSetProgressions",
        "pb",
        "gear_set_progressions_1",
        GearSetProgressionsProcessor,
    ),
    (
        "ProgressionTable_GearGen_GearSets",
        "pb",
        "gear_set_progressions_2",
        GearSetProgressionsProcessor,
    ),
    ("GearTable", "pb", "gears_1", GearsProcessor),
    ("ItemTable_GearGen_GearSets", "pb", "gears_2", GearsProcessor),
    ("ItemTable_GearGen_Trinkets", "pb", "trinket_gears", GearsProcessor),
    ("GearTable_PropertyModderTable", "pb", "gear_stat_sets_1", StatSetsProcessor),
    (
        "ItemTable_GearGen_GearSets_PropertyModderTable",
        "pb",
        "gear_stat_sets_2",
        StatSetsProcessor,
    ),
    (
        "ItemTable_GearGen_Trinkets_PropertyModderTable",
        "pb",
        "trinket_gear_stat_sets",
        StatSetsProcessor,
    ),
    ("GearProgressions", "pb", "gear_stat_progressions", GearStatProgressionsProcessor),
    (
        "ArmoryCollectionsTable",
        "pb",
        "armory_collections_1",
        ArmoryCollectionsProcessor,
    ),
    (
        "ArmoryCollectionTable_GearGen_GearSets",
        "pb",
        "armory_collections_2",
        ArmoryCollectionsProcessor,
    ),
    (
        "ArmoryCollectionsTable_ArmoryPropertyModderTable",
        "pb",
        "armory_stat_sets_1",
        StatSetsProcessor,
    ),
    (
        "ArmoryCollectionTable_GearGen_GearSets_ArmoryPropertyModderTable",
        "pb",
        "armory_stat_sets_2",
        StatSetsProcessor,
    ),
    (
        "ArmoryPropertyProgressions",
        "pb",
        "armory_stat_progressions",
        ArmoryStatProgressionsProcessor,
    ),
    ("GearTable_ArmoryGearTable", "json", "armory_gears_1", ArmoryGearsProcessor),
    (
        "ItemTable_GearGen_GearSets_ArmoryGearTable",
        "json",
        "armory_gears_2",
        ArmoryGearsProcessor,
    ),
    (
        "ItemTable_GearGen_Trinkets_ArmoryGearTable",
        "json",
        "armory_gears_3",
        ArmoryGearsProcessor,
    ),
    ("HeroTable_VisGen_Launch", "json", "heroes", HeroesProcessor),
    ("HeroProgressions", "json", "hero_progressions", HeroProgressionsProcessor),
    ("HeroSkillsTable_VisGen_Launch", "json", "hero_skills", HeroSkillsProcessor),
    ("HeroTraitsTable", "json", "hero_traits", HeroTraitsProcessor),
    (
        "HeroPropertyProgressions_VisGen_Launch",
        "pb",
        "hero_skill_progressions",
        HeroSkillProgressionsProcessor,
    ),
    (
        "HeroCollectionActionTable",
        "json",
        "hero_collection_actions",
        HeroCollectionActionsProcessor,
    ),
    (
        "HeroCollectionActionProgressions",
        "json",
        "hero_collection_action_progressions",
        HeroCollectionActionProgressionsProcessor,
    ),
    (
        "HeroCollectionActionPropertyProgressions",
        "pb",
        "hero_collection_action_properties",
        HeroCollectionActionPropertiesProcessor,
    ),
    ("SummonTable", "json", "summons", SummonsProcessor),
    ("SummoningOddsTable", "pb", "summon_odds", SummonOddsProcessor),
    ("ItemTable", "pb", "items", ItemsProcessor),
    ("ItemTable_Heroes", "pb", "hero_items", ItemsProcessor),
    ("ItemTable_Dragon_1", "pb", "dragon_items", ItemsProcessor),
    ("ItemTable_Gift_1", "pb", "items_gift", ItemsProcessor),
    ("ItemTable_Event_1", "pb", "items_event", ItemsProcessor),
    ("ItemTable_LevelCap", "pb", "items_writs_bounties", ItemsProcessor),
    ("AnnuitiesTable", "pb", "recurring_rewards", RecurringRewardsProcessor),
    ("BuildingTable", "pb", "buildings", BuildingsProcessor),
    ("BuildingProgressions", "pb", "building_progressions", ProgressionsProcessor),
    (
        "BuildingEnhancementProgressions",
        "pb",
        "enhancement_progressions",
        ProgressionsProcessor,
    ),
    (
        "BuildingTable_PropertyModderTable",
        "pb",
        "building_stat_sets",
        StatSetsProcessor,
    ),
    (
        "EventScoringProgressions",
        "json",
        "event_scoring_progressions",
        EventScoringProgressionsProcessor,
    ),
    (
        "EventScoringProgressions_Dragon",
        "json",
        "event_scoring_progressions_dragon",
        EventScoringProgressionsProcessor,
    ),
    (
        "EventScoreProgressionTable_ResearchGen_military2",
        "json",
        "event_scoring_progressions_research",
        EventScoringProgressionsProcessor,
    ),
    ("GenerationProgressions", "pb", "generation_progressions", ProgressionsProcessor),
    ("TechTable", "pb", "researches_1", ResearchesProcessor),
    ("TechTable_ResearchGen_military2", "pb", "researches_2", ResearchesProcessor),
    ("TechTable_ExpeditionGen_1", "pb", "expeditions", ResearchesProcessor),
    ("TechCategoryTable", "pb", "research_categories_1", ResearchCategoriesProcessor),
    (
        "TechCategoryTable_ResearchGen_military2",
        "pb",
        "research_categories_2",
        ResearchCategoriesProcessor,
    ),
    (
        "TechCategoryTable_ExpeditionGen_1",
        "pb",
        "expedition_categories",
        ResearchCategoriesProcessor,
    ),
    ("ResearchProgressions", "pb", "research_progressions_1", ProgressionsProcessor),
    (
        "ProgressionTable_ResearchGen_military2",
        "pb",
        "research_progressions_2",
        ProgressionsProcessor,
    ),
    ("TechTable_PropertyModderTable", "pb", "research_stat_sets_1", StatSetsProcessor),
    (
        "TechTable_ResearchGen_military2_PropertyModderTable",
        "pb",
        "research_stat_sets_2",
        StatSetsProcessor,
    ),
    ("AlchemyTable", "pb", "recipes_general", RecipesProcessor),
    (
        "AlchemyTable_AlchemyGen_EventArc",
        "pb",
        "recipes_monthly_trade_1",
        RecipesProcessor,
    ),
    (
        "AlchemyTable_AlchemyGen_EventArc_2",
        "pb",
        "recipes_monthly_trade_2",
        RecipesProcessor,
    ),
    (
        "AlchemyTable_AlchemyGen_Feast_Cakes",
        "pb",
        "recipes_feast_cakes",
        RecipesProcessor,
    ),
    (
        "AlchemyTable_AlchemyGen_QuantityLimited",
        "pb",
        "recipes_writs",
        RecipesProcessor,
    ),
    (
        "AlchemyTable_AlchemyGen_Repeatable",
        "pb",
        "recipes_repeatable",
        RecipesProcessor,
    ),
    (
        "AlchemyTable_AlchemyGen_Repeatable_Dragon",
        "pb",
        "recipes_dragon",
        RecipesProcessor,
    ),
    (
        "AlchemyTable_AlchemyGen_Repeatable_Flux",
        "pb",
        "recipes_flux",
        RecipesProcessor,
    ),
    (
        "AlchemyTable_AlchemyGen_Repeatable_Scrip",
        "pb",
        "recipes_traders_script",
        RecipesProcessor,
    ),
    (
        "AlchemyTable_AlchemyGen_Repeatable_StrategicTerrain",
        "pb",
        "recipes_nodes",
        RecipesProcessor,
    ),
    (
        "AlchemyTable_AlchemyGen_Repeatable_TGH",
        "pb",
        "recipes_venison",
        RecipesProcessor,
    ),
    (
        "AlchemyTable_AlchemyGen_Special",
        "pb",
        "recipes_festival",
        RecipesProcessor,
    ),
    (
        "AlchemyTable_AlchemyGen_Special_IronCrown",
        "pb",
        "recipes_iron_crown",
        RecipesProcessor,
    ),
    (
        "AlchemyTable_Bounties",
        "pb",
        "recipes_bounties",
        RecipesProcessor,
    ),
    (
        "AlchemyRecipeTable",
        "pb",
        "recipe_ingredient_sets_general",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_EventArc",
        "pb",
        "recipe_ingredient_sets_monthly_trade_1",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_EventArc_2",
        "pb",
        "recipe_ingredient_sets_monthly_trade_2",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Feast_Cakes",
        "pb",
        "recipe_ingredient_sets_feast_cakes",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_QuantityLimited",
        "pb",
        "recipe_ingredient_sets_writs",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Repeatable",
        "pb",
        "recipe_ingredient_sets_repeatable",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Repeatable_Dragon",
        "pb",
        "recipe_ingredient_sets_dragon",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Repeatable_Flux",
        "pb",
        "recipe_ingredient_sets_flux",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Repeatable_Scrip",
        "pb",
        "recipe_ingredient_sets_traders_script",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Repeatable_StrategicTerrain",
        "pb",
        "recipe_ingredient_sets_nodes",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Repeatable_TGH",
        "pb",
        "recipe_ingredient_sets_venison",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Special",
        "pb",
        "recipe_ingredient_sets_festival",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Special_IronCrown",
        "pb",
        "recipe_ingredient_sets_iron_crown",
        RecipeIngredientSetsProcessor,
    ),
    (
        "AlchemyRecipeTable_Bounties",
        "pb",
        "recipe_ingredient_sets_bounties",
        RecipeIngredientSetsProcessor,
    ),
    ("TroopTable", "pb", "troops", TroopsProcessor),
    ("PropertyTable", "pb", "properties", PropertiesProcessor),
    ("enUS", "txt", "translations", TranslationsProcessor),
}


def _preprocess_mapping_config(config):
    mapping = defaultdict(dict)
    for file_name, file_extension, output_id, processor_class in config:
        mapping[file_name][file_extension] = (output_id, processor_class)
    return mapping


FILE_PROCESSOR_MAPPING = _preprocess_mapping_config(FILE_PROCESSOR_MAPPING_CONFIG)


def find_processor(file_name, file_extension):
    if (
        file_name in FILE_PROCESSOR_MAPPING
        and file_extension in FILE_PROCESSOR_MAPPING[file_name]
    ):
        return FILE_PROCESSOR_MAPPING[file_name][file_extension]
    return None
