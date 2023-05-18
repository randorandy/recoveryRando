from typing import ClassVar

from connection_data import area_doors_unpackable
from door_logic import canOpen
from item_data import items_unpackable
from loadout import Loadout
from logicInterface import AreaLogicType, LocationLogicType, LogicInterface
from logic_shortcut import LogicShortcut

# TODO: There are a bunch of places where where Expert logic needed energy tanks even if they had Varia suit.
# Need to make sure everything is right in those places.
# (They will probably work right when they're combined like this,
#  but they wouldn't have worked right when casual was separated from expert.)

# TODO: There are also a bunch of places where casual used icePod, where expert only used Ice. Is that right?

(
    CraterR, SunkenNestL, RuinedConcourseBL, RuinedConcourseTR, CausewayR,
    SporeFieldTR, SporeFieldBR, OceanShoreR, EleToTurbidPassageR, PileAnchorL,
    ExcavationSiteL, WestCorridorR, FoyerR, ConstructionSiteL, AlluringCenoteR,
    FieldAccessL, TransferStationR, CellarR, SubbasementFissureL,
    WestTerminalAccessL, MezzanineConcourseL, VulnarCanyonL, CanyonPassageR,
    ElevatorToCondenserL, LoadingDockSecurityAreaL, ElevatorToWellspringL,
    NorakBrookL, NorakPerimeterTR, NorakPerimeterBL, VulnarDepthsElevatorEL,
    VulnarDepthsElevatorER, HiveBurrowL, SequesteredInfernoL,
    CollapsedPassageR, MagmaPumpL, ReservoirMaintenanceTunnelR, IntakePumpR,
    ThermalReservoir1R, GeneratorAccessTunnelL, ElevatorToMagmaLakeR,
    MagmaPumpAccessR, FieryGalleryL, RagingPitL, HollowChamberR, PlacidPoolR,
    SporousNookL, RockyRidgeTrailL, TramToSuziIslandR
) = area_doors_unpackable

(
    Missile, Super, PowerBomb, Morph, Springball, Bombs, HiJump,
    GravitySuit, Varia, Wave, SpeedBooster, Spazer, Ice, Grapple,
    Plasma, Screw, Charge, SpaceJump, Energy, Reserve, Xray, Missilex75
) = items_unpackable


exitSpacePort = LogicShortcut(lambda loadout: (
    True
    # TODO: Why did one definition have somethings different?
    # (Morph in loadout) or (Missile in loadout) or (Super in loadout) or (Wave in loadout)
))
canIBJ = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Bombs in loadout)
))
canUseBombs = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    ((Bombs in loadout) or (PowerBomb in loadout))
))

canFly = LogicShortcut(lambda loadout: (
    (canIBJ in loadout) or
    (SpaceJump in loadout)
))
canUsePB = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (PowerBomb in loadout)
))
fireMissiles = LogicShortcut(lambda loadout: (
    (Missile in loadout) or
    (Missilex75 in loadout)
))
pinkDoor = LogicShortcut(lambda loadout: (
    (fireMissiles in loadout) or
    (Super in loadout)
))
goingLeft = LogicShortcut(lambda loadout: (
    (
        (Morph in loadout) and
        (
            (pinkDoor in loadout) or
            (SpeedBooster in loadout)
            )
        ) or
    (canUseBombs in loadout)
))
greenBrin = LogicShortcut(lambda loadout: (
    (pinkDoor in loadout) and
    (canUseBombs in loadout)
))
wreckedShip = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout)
))
phantoon = LogicShortcut(lambda loadout: (
    (canUseBombs in loadout) and
    (fireMissiles in loadout)
))
businessCenter = LogicShortcut(lambda loadout: (
    (pinkDoor in loadout) and
    (
        (canUseBombs in loadout) or
        (
            (Morph in loadout) and
            (Screw in loadout)
            )
        ) and
    (
        (Grapple in loadout) or
        (Ice in loadout) or
        (SpaceJump in loadout) or
        (HiJump in loadout) or
        (Springball in loadout) or
        (GravitySuit in loadout)
        )
))
warehouse = LogicShortcut(lambda loadout: (
    (businessCenter in loadout) and
    (
        (Grapple in loadout) or
        (canFly in loadout) or
        (Springball in loadout) or
        (HiJump in loadout)
        )
))
kraid = LogicShortcut(lambda loadout: (
    (warehouse in loadout) and
    (canUseBombs in loadout) and
    (
        (fireMissiles in loadout) or
        (Charge in loadout)
        )
))
heatedNorfair = LogicShortcut(lambda loadout: (
    (businessCenter in loadout) and
    (Varia in loadout)
))
GTsideLN = LogicShortcut(lambda loadout: (
    (heatedNorfair in loadout) and
    (canUseBombs in loadout) and
    (
        ((fireMissiles in loadout) or (Charge in loadout)) or
        (SpeedBooster in loadout)
        )
    
))
ridleySideLN = LogicShortcut(lambda loadout: (
    (heatedNorfair in loadout) and
    (canUseBombs in loadout) and
    (
        ((fireMissiles in loadout) or (Charge in loadout)) or
        (SpeedBooster in loadout)
        ) and
    (
        (Super in loadout) or
        (GravitySuit in loadout)
        )
))
bubbleMountain = LogicShortcut(lambda loadout: (
    (heatedNorfair in loadout) and
    (
        (SpeedBooster in loadout) or
        (canUsePB in loadout)
        )
))
forgottenHighwayTop = LogicShortcut(lambda loadout: (
    (wreckedShip in loadout) and
    (Super in loadout) and
    (GravitySuit in loadout) #for now
))
toiletBottom = LogicShortcut(lambda loadout: (
    (
        (canUseBombs in loadout) or
        (
            (Morph in loadout) and
            (Screw in loadout)
            )
        ) and
    (
        (Grapple in loadout) or
        (Ice in loadout) or
        (SpaceJump in loadout) or
        (HiJump in loadout) or
        (Springball in loadout) or
        (GravitySuit in loadout)
        ) and
    (GravitySuit in loadout) #for now
))
mainStreet = LogicShortcut(lambda loadout: (
    (toiletBottom in loadout) and
    (canUsePB in loadout) and
    (GravitySuit in loadout) #for now
))
innerMaridia = LogicShortcut(lambda loadout: (
    (mainStreet in loadout) and
    (Super in loadout) and
    (Springball in loadout) and
    (SpaceJump in loadout)
))

area_logic: AreaLogicType = {
    "Early": {
        # using SunkenNestL as the hub for this area, so we don't need a path from every door to every other door
        # just need at least a path with sunken nest to and from every other door in the area
        ("CraterR", "SunkenNestL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "CraterR"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseBL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseTR"): lambda loadout: (
            True
        ),   
    },
}


location_logic: LocationLogicType = {
    "Morph Ball": lambda loadout: (
        True
        #Requires morph to escape, will force Morph at Morph
    ),
    "Top Landing Site Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Top Right Red Tower Chozo Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "230 Missile": lambda loadout: (
        (Morph in loadout) and
        (pinkDoor in loadout)
    ),
    "Bombs": lambda loadout: (
        (pinkDoor in loadout)
    ),
    "Green Hill Wave Gate": lambda loadout: (
        (goingLeft in loadout)
    ),
    "Blue Alpha Missile": lambda loadout: (
        (goingLeft in loadout)
    ),
    "Climb Energy Tank": lambda loadout: (
        (goingLeft in loadout)
    ),
    "Terminator Pirates Hidden": lambda loadout: (
        (canUseBombs in loadout)
    ),
    "Charge Beam": lambda loadout: (
        (greenBrin in loadout)
    ),
    "Etecoons Pirate Chozo": lambda loadout: (
        (greenBrin in loadout)
    ),
    "Etecoons Left Chozo": lambda loadout: (
        (greenBrin in loadout)
    ),
    "Springball": lambda loadout: (
        (greenBrin in loadout) and
        (Springball in loadout)
    ),
    "Back of Gauntlet Wall": lambda loadout: (
        (greenBrin in loadout) and
        (Springball in loadout)
    ),
    "Sky Energy Tank": lambda loadout: (
        (wreckedShip in loadout) and
        (
            (canFly in loadout) or
            (SpeedBooster in loadout) or
            (Grapple in loadout)
            )
    ),
    "Ocean Floor Missile": lambda loadout: (
        (wreckedShip in loadout)
    ),
    "Ocean Grapple Missile": lambda loadout: (
        (wreckedShip in loadout)
    ),
    "Plasma Beam": lambda loadout: (
        (phantoon in loadout) and
        (SpeedBooster in loadout) and
        (
            (SpaceJump in loadout) or
            (
                (Energy in loadout) and
                (Varia in loadout) and
                (GravitySuit in loadout)
                )
            )
    ),
    "Spooky Speed Missile": lambda loadout: (
        (wreckedShip in loadout) and
        (SpeedBooster in loadout)
    ),
    "Bowling Reserve": lambda loadout: (
        (phantoon in loadout)
    ),
    "Bowling Bottom Missile": lambda loadout: (
        (phantoon in loadout) and
        (SpeedBooster in loadout)
    ),
    "Varia Suit": lambda loadout: (
        (phantoon in loadout)
    ),
    "Wrecked Ship Right Side Energy Tank": lambda loadout: (
        (phantoon in loadout)
    ),
    "Grapple Beam": lambda loadout: (
        (phantoon in loadout)
    ),
    "Wrecked Ship Vanilla Energy": lambda loadout: (
        (phantoon in loadout) and
        (
            (SpaceJump in loadout) or
            (GravitySuit in loadout) or
            (Grapple in loadout) or
            (HiJump in loadout)
            )
    ),
    "Old Mother Brain": lambda loadout: (
        (Super in loadout) and
        (
            (canUseBombs in loadout) or
            (
                (GravitySuit in loadout) and
                (Screw in loadout)
                )
            ) and
        (
            (GravitySuit in loadout) or
            (
                (Energy in loadout) and
                (Reserve in loadout) and
                (Varia in loadout)
                )
            )
    ),
    "X-Ray Missile": lambda loadout: (
        (Morph in loadout) and
        (pinkDoor in loadout)
    ),
    "X-Ray": lambda loadout: (
        (Morph in loadout) and
        (pinkDoor in loadout)
    ),
    "Vanilla Spazer": lambda loadout: (
        (canUseBombs in loadout) and
        (Grapple in loadout)
    ),
    "Top Left Red Tower Chozo Missile": lambda loadout: (
        (canUseBombs in loadout)
    ),
    "Red Tower Speed Wall": lambda loadout: (
        (Morph in loadout) and
        (SpeedBooster in loadout)
    ),
    "Red Tower Missile": lambda loadout: (
        (canUseBombs in loadout) or
        ((Morph in loadout) and (Screw in loadout))
    ),
    "Spazer Reserve": lambda loadout: (
        (businessCenter in loadout) and
        (pinkDoor in loadout)
    ),
    "Spazer": lambda loadout: (
        (businessCenter in loadout) and
        (pinkDoor in loadout)
    ),
    "Kraid Warehouse First Chozo": lambda loadout: (
        (warehouse in loadout)
    ),
    "Kraid Warehouse Second Chozo": lambda loadout: (
        (warehouse in loadout)
    ),
    "Kraid Elevator Chozo": lambda loadout: (
        (businessCenter in loadout)
    ),
    "Kraid 75 Missile": lambda loadout: (
        (kraid in loadout)
    ),
    "Spore Spawn Shaft": lambda loadout: (
        (kraid in loadout)
    ),
    "Ice Beam": lambda loadout: (
        (kraid in loadout)
    ),
    "Spore Spawn Big Hoppers": lambda loadout: (
        (kraid in loadout)
    ),
    "Hidden Waterway": lambda loadout: (
        (kraid in loadout)
    ),
    "Lower Billy Speed Missile": lambda loadout: (
        (Morph in loadout) and
        (SpeedBooster in loadout)
    ),
    "Waterway": lambda loadout: (
        (kraid in loadout)
    ),
    "Construction Zone": lambda loadout: (
        (canUsePB in loadout)
    ),
    "Brinstar Reserve": lambda loadout: (
        (kraid in loadout)
    ),
    "Billy Maze Missile": lambda loadout: (
        (canUseBombs in loadout)
    ),
    "Cathedral Missile": lambda loadout: (
        (heatedNorfair in loadout) and
        (
            (Grapple in loadout) or
            (canFly in loadout) or
            (Ice in loadout) or
            (HiJump in loadout) or
            (SpeedBooster in loadout) or
            (Springball in loadout)
            )
    ),
    "Frog Speedway": lambda loadout: (
        (heatedNorfair in loadout) and
        (
            (Grapple in loadout) or
            (canFly in loadout) or
            (Ice in loadout) or
            (HiJump in loadout) or
            (SpeedBooster in loadout) or
            (Springball in loadout)
            )
    ),
    "Vanilla Ice Chozo": lambda loadout: (
        (businessCenter in loadout) and
        (Varia in loadout)
    ),
    "Screw Attack": lambda loadout: (
        (GTsideLN in loadout) and
        (
            (Charge in loadout) or
            (Super in loadout)
            )
    ),
    "Indiana Jones": lambda loadout: (
        (GTsideLN in loadout)
    ),
    "Norfair Vanilla Reserve": lambda loadout: (
        (bubbleMountain in loadout) and
        (Super in loadout)
    ),
    "Speed Booster": lambda loadout: (
        (bubbleMountain in loadout) and
        (
            (Springball in loadout) or
            (canIBJ in loadout)
            ) and
        (Super in loadout)
    ),
    "Lower Norfair Escape Chozo": lambda loadout: (
        (bubbleMountain in loadout)
    ),
    "Desgeega Chozo": lambda loadout: (
        (bubbleMountain in loadout) and
        (Super in loadout) and
        (
            (Grapple in loadout) or
            (canFly in loadout) or
            (SpeedBooster in loadout) or
            (Springball in loadout)
            )
    ),
    "Lower Norfair Top Chozo": lambda loadout: (
        (GTsideLN in loadout)
    ),
    "Jail Missile": lambda loadout: (
        (bubbleMountain in loadout)
    ),
    "Missile of Shame": lambda loadout: (
        (ridleySideLN in loadout) and
        (canUsePB in loadout)
    ),
    "Power Bomb of Shame": lambda loadout: (
        (ridleySideLN in loadout) and
        (
            (Super in loadout) or
            (canUsePB in loadout)
            )
    ),
    "Gravity Suit": lambda loadout: (
        (ridleySideLN in loadout) and
        (Charge in loadout)
    ),
    "Fireflea Lava": lambda loadout: (
        (ridleySideLN in loadout) and
        (GravitySuit in loadout)
    ),
    "Hotarubi Chozo": lambda loadout: (
        (bubbleMountain in loadout)
    ),
    "Wave Beam": lambda loadout: (
        (GTsideLN in loadout) and
        (Wave in loadout)
    ),
    "Crocomire Energy Tank": lambda loadout: (
        (heatedNorfair in loadout) and
        (
            (Missile in loadout) or
            (Charge in loadout)
            )
    ),
    "Vanilla Grapple": lambda loadout: (
        (GTsideLN in loadout)
    ),
    "Behind Vanilla Ice Chozo": lambda loadout: (
        (heatedNorfair in loadout) and
        (canUseBombs in loadout)
    ),
    "Maridia Tube Speedlocked": lambda loadout: (
        (toiletBottom in loadout) and
        (SpeedBooster in loadout)
    ),
    "Green Maridia Morph Wall": lambda loadout: (
        (GravitySuit in loadout) and #for now
        (mainStreet in loadout)
    ),
    "Speedlocked Main Street": lambda loadout: (
        (GravitySuit in loadout) and
        (mainStreet in loadout) and
        (SpeedBooster in loadout) and
        (pinkDoor in loadout)
    ),
    "Watering Hole": lambda loadout: (
        (GravitySuit in loadout) and #for now
        (mainStreet in loadout) and
        (canUsePB in loadout) and
        (SpeedBooster in loadout)
    ),
    "HiJump": lambda loadout: (
        (GravitySuit in loadout) and #for now
        (
            (forgottenHighwayTop in loadout) or
            (
                (toiletBottom in loadout) and
                (
                    (Super in loadout) and
                    (canUsePB in loadout)
                    )
                )
            )
    ),
    "Green Maridia Right Chozo": lambda loadout: (
        (GravitySuit in loadout) and #for now
        (mainStreet in loadout) and
        (Super in loadout)
    ),
    "Green Maridia Ceiling Missile": lambda loadout: (
        (GravitySuit in loadout) and
        (mainStreet in loadout) and
        (Super in loadout) and
        (canUsePB in loadout)
        
    ),
    "Butterfly Secret": lambda loadout: (
        (forgottenHighwayTop in loadout) and
        (canUsePB in loadout) 
    ),
    "Shaktool Power Bomb": lambda loadout: (
        (GravitySuit in loadout) and #for now
        (
            ((wreckedShip in loadout) and (Super in loadout)) or
            (businessCenter in loadout)
            ) and
        (
            ((HiJump in loadout) and (canUsePB in loadout)) or
            (GravitySuit in loadout)
            ) and
        (Charge in loadout)
            
    ),
    "Draygon Energy Tank": lambda loadout: (
        (innerMaridia in loadout) and
        (Charge in loadout) and
        (SpeedBooster in loadout)
    ),

    "Green Maridia Boulder Chozo": lambda loadout: (
        (GravitySuit in loadout) and #for now
        (mainStreet in loadout)
    ),
    "Space Jump": lambda loadout: (
        (innerMaridia in loadout) and
        (Charge in loadout)
    ),
    "Behind Botwoon Chozo": lambda loadout: (
        (innerMaridia in loadout)
    ),
    "Red Tower Secret 1": lambda loadout: (
        (Morph in loadout) and
        (pinkDoor in loadout) and
        (SpeedBooster in loadout)
    ),
    "Red Tower Secret 2": lambda loadout: (
        (Morph in loadout) and
        (pinkDoor in loadout) and
        (SpeedBooster in loadout)
    ),
    "Red Tower Secret 3": lambda loadout: (
        (Morph in loadout) and
        (pinkDoor in loadout) and
        (SpeedBooster in loadout)
    ),
    "Red Tower Secret 4": lambda loadout: (
        (Morph in loadout) and
        (pinkDoor in loadout) and
        (SpeedBooster in loadout)
    ),
}


class Expert(LogicInterface):
    area_logic: ClassVar[AreaLogicType] = area_logic
    location_logic: ClassVar[LocationLogicType] = location_logic

    @staticmethod
    def can_fall_from_spaceport(loadout: Loadout) -> bool:
        return True
