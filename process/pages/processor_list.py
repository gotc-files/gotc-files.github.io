from pages.armory import ArmoryProcessor
from pages.building import BuildingProcessor
from pages.daily_delivery import DailyDeliveryProcessor
from pages.enhancement import EnhancementProcessor
from pages.hero import HeroProcessor
from pages.hero_collection_action import HeroCollectionActionProcessor
from pages.recipe import RecipeProcessor
from pages.research import ResearchProcessor
from pages.summon import SummonProcessor
from pages.trinket_armory import TrinketArmoryProcessor


def page_processor_list():
    return (
        ('armory', ArmoryProcessor),
        ('trinket_armory', TrinketArmoryProcessor),
        ('hero', HeroProcessor),
        ('summon', SummonProcessor),
        ('daily_delivery', DailyDeliveryProcessor),
        ('building', BuildingProcessor),
        ('enhancement', EnhancementProcessor),
        ('research', ResearchProcessor),
        ('hero_collection_action', HeroCollectionActionProcessor),
        ('recipe', RecipeProcessor),
    )
