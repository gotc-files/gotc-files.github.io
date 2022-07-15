from collections import defaultdict

from files.armory_collections.armory_collections import ArmoryCollectionsProcessor
from files.armory_gears.armory_gears import ArmoryGearsProcessor
from files.buildings.buildings import BuildingsProcessor
from files.crafting_recipes.crafting_recipes import CraftingRecipesProcessor
from files.gear_set_progressions.gear_set_progressions import (
    GearSetProgressionsProcessor,
)
from files.gear_sets.gear_sets import GearSetsProcessor
from files.gears.gears import GearsProcessor
from files.hero_collection_actions.hero_collection_actions import (
    HeroCollectionActionsProcessor,
)
from files.hero_progressions.hero_progressions import HeroProgressionsProcessor
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
from files.troops.troops import TroopsProcessor

FILE_PROCESSOR_MAPPING_CONFIG = {
    ("GearSetTable", "pb", "gear_set_1", GearSetsProcessor),
    ("GearsetTable_GearGen_GearSets", "pb", "gear_set_2", GearSetsProcessor),
    ("GearSetTable_Trinkets", "pb", "trinket_gear_sets", GearSetsProcessor),
    (
        "GearSetProgressions",
        ("pb", "json"),
        "gear_set_progressions_1",
        GearSetProgressionsProcessor,
    ),
    (
        "ProgressionTable_GearGen_GearSets",
        ("pb", "json"),
        "gear_set_progressions_2",
        GearSetProgressionsProcessor,
    ),
    ("GearTable", ("pb", "json"), "gears_1", GearsProcessor),
    ("ItemTable_GearGen_GearSets", ("pb", "json"), "gears_2", GearsProcessor),
    ("ItemTable_GearGen_Trinkets", ("pb", "json"), "trinket_gears", GearsProcessor),
    (
        "GearTable_PropertyModderTable",
        ("pb", "json"),
        "gear_stat_sets_1",
        StatSetsProcessor,
    ),
    (
        "ItemTable_GearGen_GearSets_PropertyModderTable",
        ("pb", "json"),
        "gear_stat_sets_2",
        StatSetsProcessor,
    ),
    (
        "ItemTable_GearGen_Trinkets_PropertyModderTable",
        ("pb", "json"),
        "trinket_gear_stat_sets",
        StatSetsProcessor,
    ),
    (
        "GearProgressions",
        ("pb", "json"),
        "gear_stat_progressions",
        ProgressionsProcessor,
    ),
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
        ("pb", "json"),
        "armory_stat_sets_1",
        StatSetsProcessor,
    ),
    (
        "ArmoryCollectionTable_GearGen_GearSets_ArmoryPropertyModderTable",
        ("pb", "json"),
        "armory_stat_sets_2",
        StatSetsProcessor,
    ),
    (
        "ArmoryPropertyProgressions",
        ("pb", "json"),
        "armory_stat_progressions",
        ProgressionsProcessor,
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
    ("RecipeTable", ("pb", "json"), "crafting_recipes_1", CraftingRecipesProcessor),
    (
        "RecipeTable_GearGen_GearSets",
        ("pb", "json"),
        "crafting_recipes_2",
        CraftingRecipesProcessor,
    ),
    (
        "RecipeTable_GearGen_Trinkets",
        ("pb", "json"),
        "trinket_crafting_recipes",
        CraftingRecipesProcessor,
    ),
    ("HeroTable_VisGen_Launch", "pb", "heroes", HeroesProcessor),
    ("HeroProgressions", "json", "hero_progressions", HeroProgressionsProcessor),
    (
        "HeroSkillsTable_VisGen_Launch",
        ("pb", "json"),
        "hero_skills",
        HeroSkillsProcessor,
    ),
    ("HeroTraitsTable", "pb", "hero_traits", HeroTraitsProcessor),
    (
        "HeroPropertyProgressions_VisGen_Launch",
        ("pb", "json"),
        "hero_skill_progressions",
        ProgressionsProcessor,
    ),
    (
        "HeroCollectionActionTable",
        "pb",
        "hero_collection_actions",
        HeroCollectionActionsProcessor,
    ),
    (
        "HeroCollectionActionProgressions",
        ("pb", "json"),
        "hero_collection_action_progressions",
        ProgressionsProcessor,
    ),
    (
        "HeroCollectionActionPropertyProgressions",
        ("pb", "json"),
        "hero_collection_action_properties",
        ProgressionsProcessor,
    ),
    ("SummonTable", ("pb", "json"), "summons", SummonsProcessor),
    ("SummoningOddsTable", ("pb", "json"), "summon_odds", SummonOddsProcessor),
    ("ItemTable", ("pb", "json"), "items", ItemsProcessor),
    ("ItemTable_Heroes", ("pb", "json"), "hero_items", ItemsProcessor),
    ("ItemTable_Dragon_1", ("pb", "json"), "dragon_items", ItemsProcessor),
    ("ItemTable_Gift_1", ("pb", "json"), "items_gift", ItemsProcessor),
    ("ItemTable_Event_1", ("pb", "json"), "items_event", ItemsProcessor),
    ("ItemTable_LevelCap", ("pb", "json"), "items_writs_bounties", ItemsProcessor),
    ("AnnuitiesTable", "pb", "recurring_rewards", RecurringRewardsProcessor),
    ("BuildingTable", "pb", "buildings", BuildingsProcessor),
    (
        "BuildingProgressions",
        ("pb", "json"),
        "building_progressions",
        ProgressionsProcessor,
    ),
    (
        "BuildingEnhancementProgressions",
        ("pb", "json"),
        "enhancement_progressions",
        ProgressionsProcessor,
    ),
    (
        "BuildingTable_PropertyModderTable",
        ("pb", "json"),
        "building_stat_sets",
        StatSetsProcessor,
    ),
    (
        "EventScoringProgressions",
        ("pb", "json"),
        "event_scoring_progressions",
        ProgressionsProcessor,
    ),
    (
        "EventScoringProgressions_Dragon",
        ("pb", "json"),
        "event_scoring_progressions_dragon",
        ProgressionsProcessor,
    ),
    (
        "EventScoreProgressionTable_ResearchGen_military2",
        ("pb", "json"),
        "event_scoring_progressions_research",
        ProgressionsProcessor,
    ),
    (
        "GenerationProgressions",
        ("pb", "json"),
        "generation_progressions",
        ProgressionsProcessor,
    ),
    ("TechTable", ("pb", "json"), "researches_1", ResearchesProcessor),
    (
        "TechTable_ResearchGen_military2",
        ("pb", "json"),
        "researches_2",
        ResearchesProcessor,
    ),
    ("TechTable_ExpeditionGen_1", ("pb", "json"), "expeditions", ResearchesProcessor),
    (
        "TechCategoryTable",
        ("pb", "json"),
        "research_categories_1",
        ResearchCategoriesProcessor,
    ),
    (
        "TechCategoryTable_ResearchGen_military2",
        ("pb", "json"),
        "research_categories_2",
        ResearchCategoriesProcessor,
    ),
    (
        "TechCategoryTable_ExpeditionGen_1",
        ("pb", "json"),
        "expedition_categories",
        ResearchCategoriesProcessor,
    ),
    (
        "ResearchProgressions",
        ("pb", "json"),
        "research_progressions_1",
        ProgressionsProcessor,
    ),
    (
        "ProgressionTable_ResearchGen_military2",
        ("pb", "json"),
        "research_progressions_2",
        ProgressionsProcessor,
    ),
    (
        "TechTable_PropertyModderTable",
        ("pb", "json"),
        "research_stat_sets_1",
        StatSetsProcessor,
    ),
    (
        "TechTable_ResearchGen_military2_PropertyModderTable",
        ("pb", "json"),
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
        ("pb", "json"),
        "recipe_ingredient_sets_general",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_EventArc",
        ("pb", "json"),
        "recipe_ingredient_sets_monthly_trade_1",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_EventArc_2",
        ("pb", "json"),
        "recipe_ingredient_sets_monthly_trade_2",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Feast_Cakes",
        ("pb", "json"),
        "recipe_ingredient_sets_feast_cakes",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_QuantityLimited",
        ("pb", "json"),
        "recipe_ingredient_sets_writs",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Repeatable",
        ("pb", "json"),
        "recipe_ingredient_sets_repeatable",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Repeatable_Dragon",
        ("pb", "json"),
        "recipe_ingredient_sets_dragon",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Repeatable_Flux",
        ("pb", "json"),
        "recipe_ingredient_sets_flux",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Repeatable_Scrip",
        ("pb", "json"),
        "recipe_ingredient_sets_traders_script",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Repeatable_StrategicTerrain",
        ("pb", "json"),
        "recipe_ingredient_sets_nodes",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Repeatable_TGH",
        ("pb", "json"),
        "recipe_ingredient_sets_venison",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Special",
        ("pb", "json"),
        "recipe_ingredient_sets_festival",
        RecipeIngredientSetsProcessor,
    ),
    (
        "UniversalRecipeTable_AlchemyGen_Special_IronCrown",
        ("pb", "json"),
        "recipe_ingredient_sets_iron_crown",
        RecipeIngredientSetsProcessor,
    ),
    (
        "AlchemyRecipeTable_Bounties",
        ("pb", "json"),
        "recipe_ingredient_sets_bounties",
        RecipeIngredientSetsProcessor,
    ),
    ("TroopTable", "pb", "troops", TroopsProcessor),
    ("PropertyTable", ("pb", "json"), "properties", PropertiesProcessor),
    ("enUS", "txt", "translations", TranslationsProcessor),
}


def _preprocess_mapping_config(config):
    mapping = defaultdict(dict)
    for file_name, file_extensions, output_id, processor_class in config:
        if type(file_extensions) is tuple:
            for file_extension in file_extensions:
                mapping[file_name][file_extension] = (output_id, processor_class)
        else:
            mapping[file_name][file_extensions] = (output_id, processor_class)
    return mapping


FILE_PROCESSOR_MAPPING = _preprocess_mapping_config(FILE_PROCESSOR_MAPPING_CONFIG)


def find_processor(file_name, file_extension):
    if (
        file_name in FILE_PROCESSOR_MAPPING
        and file_extension in FILE_PROCESSOR_MAPPING[file_name]
    ):
        return FILE_PROCESSOR_MAPPING[file_name][file_extension]
    return None
