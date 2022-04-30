from pages.armory import ArmoryProcessor
from pages.hero import HeroProcessor
from pages.summon import SummonProcessor
from pages.trinket_armory import TrinketArmoryProcessor
from pages.daily_delivery import DailyDeliveryProcessor
from pages.building import BuildingProcessor
from pages.enhancement import EnhancementProcessor


def page_processor_list():
    return (
        ('armory', ArmoryProcessor),
        ('trinket_armory', TrinketArmoryProcessor),
        ('hero', HeroProcessor),
        ('summon', SummonProcessor),
        ('daily_delivery', DailyDeliveryProcessor),
        ('building', BuildingProcessor),
        ('enhancement', EnhancementProcessor),
    )
