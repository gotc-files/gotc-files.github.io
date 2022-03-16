from pages.armory import ArmoryProcessor
from pages.trinket_armory import TrinketArmoryProcessor


def page_processor_list():
    return (
        ('armory', ArmoryProcessor),
        ('trinket_armory', TrinketArmoryProcessor),
    )
