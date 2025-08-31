from pyxivdata.resource.excel.reader import ExdRow
import typing

class AOZArrangementRow(ExdRow):
    AOZContentBriefingBNpc: typing.Any = 0
    Position: typing.Any = 1

class AOZBossRow(ExdRow):
    _display_field: str = 'Boss'

    Boss: typing.Any = 0
    Position: typing.Any = 1

class AOZContentRow(ExdRow):
    GilReward: typing.Any = 0
    AlliedSealsReward: typing.Any = 1
    TomestonesReward: typing.Any = 2
    ContentEntry: typing.Any = 3
    StandardFinishTime: typing.Any = 4
    IdealFinishTime: typing.Any = 5
    Act1: typing.Any = 6
    Act2: typing.Any = 7
    Act3: typing.Any = 8
    Unknown0: typing.Any = 9
    Unknown1: typing.Any = 10
    Unknown2: typing.Any = 11
    Act1FightType: typing.Any = 12
    Act2FightType: typing.Any = 13
    Act3FightType: typing.Any = 14
    ArenaType1: typing.Any = 15
    ArenaType2: typing.Any = 16
    ArenaType3: typing.Any = 17
    Order: typing.Any = 18

class AOZContentBriefingBNpcRow(ExdRow):
    _display_field: str = 'BNpcName'

    BNpcName: typing.Any = 0
    TargetSmall: typing.Any = 1
    TargetLarge: typing.Any = 2
    Endurance: typing.Any = 3
    Fire: typing.Any = 4
    Ice: typing.Any = 5
    Wind: typing.Any = 6
    Earth: typing.Any = 7
    Thunder: typing.Any = 8
    Water: typing.Any = 9
    Slashing: typing.Any = 10
    Piercing: typing.Any = 11
    Blunt: typing.Any = 12
    Magic: typing.Any = 13
    HideStats: typing.Any = 14
    SlowVuln: typing.Any = 15
    PetrificationVuln: typing.Any = 16
    ParalysisVuln: typing.Any = 17
    InterruptionVuln: typing.Any = 18
    BlindVuln: typing.Any = 19
    StunVuln: typing.Any = 20
    SleepVuln: typing.Any = 21
    BindVuln: typing.Any = 22
    HeavyVuln: typing.Any = 23
    FlatOrDeathVuln: typing.Any = 24

class AOZContentBriefingObjectRow(ExdRow):
    Icon: typing.Any = 0
    Unknown0: typing.Any = 1

class AOZReportRow(ExdRow):
    Unknown0: typing.Any = 0
    Reward: typing.Any = 1
    Order: typing.Any = 2

class AOZReportRewardRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class AOZScoreRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Score: typing.Any = 2
    IsVisible: typing.Any = 3

class AOZWeeklyRewardRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class AchievementRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Item: typing.Any = 2
    Key: typing.Any = 3
    Data0: typing.Any = 4
    Data1: typing.Any = 5
    Data2: typing.Any = 6
    Data3: typing.Any = 7
    Data4: typing.Any = 8
    Data5: typing.Any = 9
    Data6: typing.Any = 10
    Data7: typing.Any = 11
    Title: typing.Any = 12
    Icon: typing.Any = 13
    Order: typing.Any = 14
    AchievementCategory: typing.Any = 15
    AchievementTarget: typing.Any = 16
    Unknown0: typing.Any = 17
    Points: typing.Any = 18
    Unknown1: typing.Any = 19
    Unknown2: typing.Any = 20
    Unknown3: typing.Any = 21
    Unknown4: typing.Any = 22
    Type: typing.Any = 23
    Unknown5: typing.Any = 24
    AchievementHideCondition: typing.Any = 25

class AchievementCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    AchievementKind: typing.Any = 1
    Order: typing.Any = 2
    ShowComplete: typing.Any = 3
    HideCategory: typing.Any = 4

class AchievementHideConditionRow(ExdRow):
    HideAchievement: typing.Any = 0
    HideName: typing.Any = 1
    HideConditions: typing.Any = 2

class AchievementKindRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Order: typing.Any = 1

class AchievementTargetRow(ExdRow):
    _display_field: str = 'Value'

    Value: typing.Any = 0
    Type: typing.Any = 1

class ActionRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    UnlockLink: typing.Any = 1
    Icon: typing.Any = 2
    VFX: typing.Any = 3
    ActionTimelineHit: typing.Any = 4
    PrimaryCostValue: typing.Any = 5
    SecondaryCostValue: typing.Any = 6
    ActionCombo: typing.Any = 7
    Cast100ms: typing.Any = 8
    Recast100ms: typing.Any = 9
    ActionProcStatus: typing.Any = 10
    StatusGainSelf: typing.Any = 11
    Omen: typing.Any = 12
    OmenAlt: typing.Any = 13
    AnimationEnd: typing.Any = 14
    ActionCategory: typing.Any = 15
    Unknown1: typing.Any = 16
    AnimationStart: typing.Any = 17
    Unknown2: typing.Any = 18
    BehaviourType: typing.Any = 19
    ClassJobLevel: typing.Any = 20
    CastType: typing.Any = 21
    EffectRange: typing.Any = 22
    XAxisModifier: typing.Any = 23
    PrimaryCostType: typing.Any = 24
    SecondaryCostType: typing.Any = 25
    ExtraCastTime100ms: typing.Any = 26
    CooldownGroup: typing.Any = 27
    AdditionalCooldownGroup: typing.Any = 28
    MaxCharges: typing.Any = 29
    Aspect: typing.Any = 30
    Unknown4: typing.Any = 31
    ClassJobCategory: typing.Any = 32
    AutoAttackBehaviour: typing.Any = 33
    EquivalenceGroup: typing.Any = 34
    Unknown_70: typing.Any = 35
    ClassJob: typing.Any = 36
    Range: typing.Any = 37
    DeadTargetBehaviour: typing.Any = 38
    AttackType: typing.Any = 39
    Unknown8: typing.Any = 40
    IsRoleAction: typing.Any = 41
    CanTargetSelf: typing.Any = 42
    CanTargetParty: typing.Any = 43
    CanTargetAlliance: typing.Any = 44
    CanTargetHostile: typing.Any = 45
    CanTargetAlly: typing.Any = 46
    Unknown10: typing.Any = 47
    TargetArea: typing.Any = 48
    CanTargetOwnPet: typing.Any = 49
    CanTargetPartyPet: typing.Any = 50
    RequiresLineOfSight: typing.Any = 51
    NeedToFaceTarget: typing.Any = 52
    Unknown14: typing.Any = 53
    PreservesCombo: typing.Any = 54
    Unknown15: typing.Any = 55
    AffectsPosition: typing.Any = 56
    IsPvP: typing.Any = 57
    Unknown16: typing.Any = 58
    LogCastMessage: typing.Any = 59
    Unknown18: typing.Any = 60
    LogMissMessage: typing.Any = 61
    LogActionMessage: typing.Any = 62
    Unknown21: typing.Any = 63
    Unknown22: typing.Any = 64
    Unknown23: typing.Any = 65
    CanUseWhileMounted: typing.Any = 66
    Unknown25: typing.Any = 67
    IsPlayerAction: typing.Any = 68
    Unknown27: typing.Any = 69

class ActionCastTimelineRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    VFX: typing.Any = 1

class ActionCastVFXRow(ExdRow):
    _display_field: str = 'VFX'

    VFX: typing.Any = 0

class ActionCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class ActionComboRouteRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Action0: typing.Any = 1
    Action1: typing.Any = 2
    Action2: typing.Any = 3
    Action3: typing.Any = 4
    Action4: typing.Any = 5
    Action5: typing.Any = 6
    Action6: typing.Any = 7
    Unknown3: typing.Any = 8
    Unknown4: typing.Any = 9

class ActionComboRouteTransientRow(ExdRow):
    Unknown0: typing.Any = 0

class ActionCostTypeRow(ExdRow):
    Unknown0: typing.Any = 0

class ActionIndirectionRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    PreviousComboAction: typing.Any = 1
    ClassJob: typing.Any = 2

class ActionInitRow(ExdRow):
    Unknown0: typing.Any = 0

class ActionParamRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Unknown0: typing.Any = 1

class ActionProcStatusRow(ExdRow):
    _display_field: str = 'Status'

    Status: typing.Any = 0

class ActionSettingRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6

class ActionTimelineRow(ExdRow):
    _display_field: str = 'Key'

    Key: typing.Any = 0
    WeaponTimeline: typing.Any = 1
    KillUpper: typing.Any = 2
    Unknown_70: typing.Any = 3
    Type: typing.Any = 4
    Priority: typing.Any = 5
    Stance: typing.Any = 6
    Slot: typing.Any = 7
    LookAtMode: typing.Any = 8
    ActionTimelineIDMode: typing.Any = 9
    LoadType: typing.Any = 10
    StartAttach: typing.Any = 11
    ResidentPap: typing.Any = 12
    Unknown6: typing.Any = 13
    Unknown1: typing.Any = 14
    Pause: typing.Any = 15
    Resident: typing.Any = 16
    IsMotionCanceledByMoving: typing.Any = 17
    Unknown2: typing.Any = 18
    Unknown3: typing.Any = 19
    IsLoop: typing.Any = 20
    Unknown4: typing.Any = 21

class ActionTimelineMoveRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class ActionTimelineReplaceRow(ExdRow):
    Old: typing.Any = 0
    New: typing.Any = 1

class ActionTransientRow(ExdRow):
    _display_field: str = 'Description'

    Description: typing.Any = 0

class ActivityFeedButtonsRow(ExdRow):
    BannerURL: typing.Any = 0
    Description: typing.Any = 1
    Language: typing.Any = 2
    PictureURL: typing.Any = 3
    Unknown0: typing.Any = 4

class ActivityFeedCaptionsRow(ExdRow):
    JA: typing.Any = 0
    EN: typing.Any = 1
    DE: typing.Any = 2
    FR: typing.Any = 3

class ActivityFeedGroupCaptionsRow(ExdRow):
    JA: typing.Any = 0
    EN: typing.Any = 1
    DE: typing.Any = 2
    FR: typing.Any = 3

class ActivityFeedImagesRow(ExdRow):
    ExpansionImage: typing.Any = 0
    ActivityFeedJA: typing.Any = 1
    ActivityFeedEN: typing.Any = 2
    ActivityFeedDE: typing.Any = 3
    ActivityFeedFR: typing.Any = 4

class AddonRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0

class AddonHudSizeRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class AddonLayoutRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class AddonParamRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class AddonTalkParamRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6

class AddonTransientRow(ExdRow):
    Unknown0: typing.Any = 0

class AdvancedVibrationRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class AdventureRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Impression: typing.Any = 1
    Description: typing.Any = 2
    Level: typing.Any = 3
    MinLevel: typing.Any = 4
    PlaceName: typing.Any = 5
    IconList: typing.Any = 6
    IconDiscovered: typing.Any = 7
    IconUndiscovered: typing.Any = 8
    Emote: typing.Any = 9
    MinTime: typing.Any = 10
    MaxTime: typing.Any = 11
    MaxLevel: typing.Any = 12
    IsInitial: typing.Any = 13

class AdventureExPhaseRow(ExdRow):
    Quest: typing.Any = 0
    AdventureBegin: typing.Any = 1
    AdventureEnd: typing.Any = 2
    AllVistasCompletedScreenImage: typing.Any = 3
    Expansion: typing.Any = 4

class AetherCurrentRow(ExdRow):
    _display_field: str = 'Quest'

    Quest: typing.Any = 0

class AetherCurrentCompFlgSetRow(ExdRow):
    Territory: typing.Any = 0
    AetherCurrents0: typing.Any = 1
    AetherCurrents1: typing.Any = 2
    AetherCurrents2: typing.Any = 3
    AetherCurrents3: typing.Any = 4
    AetherCurrents4: typing.Any = 5
    AetherCurrents5: typing.Any = 6
    AetherCurrents6: typing.Any = 7
    AetherCurrents7: typing.Any = 8
    AetherCurrents8: typing.Any = 9
    AetherCurrents9: typing.Any = 10
    AetherCurrents10: typing.Any = 11
    AetherCurrents11: typing.Any = 12
    AetherCurrents12: typing.Any = 13
    AetherCurrents13: typing.Any = 14
    AetherCurrents14: typing.Any = 15

class AetherialWheelRow(ExdRow):
    ItemUnprimed: typing.Any = 0
    ItemPrimed: typing.Any = 1
    Grade: typing.Any = 2
    HoursRequired: typing.Any = 3

class AetheryteRow(ExdRow):
    _display_field: str = 'PlaceName'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Adjective: typing.Any = 2
    PossessivePronoun: typing.Any = 3
    StartsWithVowel: typing.Any = 4
    Unknown0: typing.Any = 5
    Pronoun: typing.Any = 6
    Article: typing.Any = 7
    Unknown1: typing.Any = 8
    Level0: typing.Any = 9
    Level1: typing.Any = 10
    Level2: typing.Any = 11
    Level3: typing.Any = 12
    RequiredQuest: typing.Any = 13
    PlaceName: typing.Any = 14
    AethernetName: typing.Any = 15
    Territory: typing.Any = 16
    Map: typing.Any = 17
    AetherstreamX: typing.Any = 18
    AetherstreamY: typing.Any = 19
    Unknown2: typing.Any = 20
    AethernetGroup: typing.Any = 21
    Order: typing.Any = 22
    IsAetheryte: typing.Any = 23
    Invisible: typing.Any = 24

class AetheryteSystemDefineRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0
    DefineValue: typing.Any = 1

class AetheryteTransientRow(ExdRow):
    Unknown0: typing.Any = 0

class AirshipExplorationLevelRow(ExdRow):
    ExpToNext: typing.Any = 0
    Capacity: typing.Any = 1

class AirshipExplorationLogRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0

class AirshipExplorationParamTypeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class AirshipExplorationPartRow(ExdRow):
    Class: typing.Any = 0
    Surveillance: typing.Any = 1
    Retrieval: typing.Any = 2
    Speed: typing.Any = 3
    Range: typing.Any = 4
    Favor: typing.Any = 5
    Slot: typing.Any = 6
    Rank: typing.Any = 7
    Components: typing.Any = 8
    RepairMaterials: typing.Any = 9

class AirshipExplorationPointRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    NameShort: typing.Any = 1
    ExpReward: typing.Any = 2
    CeruleumTankReq: typing.Any = 3
    SurveyDurationmin: typing.Any = 4
    SurveyDistance: typing.Any = 5
    X: typing.Any = 6
    Y: typing.Any = 7
    RankReq: typing.Any = 8
    Unknown0: typing.Any = 9
    Unknown1: typing.Any = 10
    SurveillanceReq: typing.Any = 11
    Unknown2: typing.Any = 12
    Passengers: typing.Any = 13

class AirshipSkyIslandRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class AkatsukiNoteRow(ExdRow):
    _display_field: str = 'ListName'

    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    ListName: typing.Any = 2
    UnlockOnQuest: typing.Any = 3
    Unknown4: typing.Any = 4
    Title: typing.Any = 5
    Icon: typing.Any = 6
    Subtitle: typing.Any = 7
    Text: typing.Any = 8

class AkatsukiNoteStringRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0

class AnimaWeapon5Row(ExdRow):
    Item: typing.Any = 0
    Unknown0: typing.Any = 1
    SecondaryStatTotal: typing.Any = 2
    Parameter0: typing.Any = 3
    Parameter1: typing.Any = 4
    Parameter2: typing.Any = 5
    Parameter3: typing.Any = 6
    Parameter4: typing.Any = 7

class AnimaWeapon5ParamRow(ExdRow):
    _display_field: str = 'BaseParam'

    Name: typing.Any = 0
    BaseParam: typing.Any = 1

class AnimaWeapon5PatternGroupRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class AnimaWeapon5SpiritTalkRow(ExdRow):
    _display_field: str = 'Dialogue'

    Dialogue: typing.Any = 0

class AnimaWeapon5SpiritTalkParamRow(ExdRow):
    _display_field: str = 'Prologue'

    Prologue: typing.Any = 0
    Epilogue: typing.Any = 1

class AnimaWeapon5SpiritTalkTypeRow(ExdRow):
    Unknown0: typing.Any = 0

class AnimaWeapon5TradeItemRow(ExdRow):
    CrystalSand: typing.Any = 0
    Item0: typing.Any = 1
    Item1: typing.Any = 2
    Item2: typing.Any = 3
    Item3: typing.Any = 4
    Item4: typing.Any = 5
    Item5: typing.Any = 6
    Item6: typing.Any = 7
    Item7: typing.Any = 8
    Order: typing.Any = 9
    ReceiveQuantity: typing.Any = 10
    Quantity0: typing.Any = 11
    Quantity1: typing.Any = 12
    Quantity2: typing.Any = 13
    Quantity3: typing.Any = 14
    Quantity4: typing.Any = 15
    Quantity5: typing.Any = 16
    Quantity6: typing.Any = 17
    Quantity7: typing.Any = 18
    Category: typing.Any = 19
    IsHQ0: typing.Any = 20
    IsHQ1: typing.Any = 21
    IsHQ2: typing.Any = 22
    IsHQ3: typing.Any = 23
    IsHQ4: typing.Any = 24
    IsHQ5: typing.Any = 25
    IsHQ6: typing.Any = 26
    IsHQ7: typing.Any = 27

class AnimaWeaponFUITalkRow(ExdRow):
    _display_field: str = 'Dialogue'

    Dialogue: typing.Any = 0

class AnimaWeaponFUITalkParamRow(ExdRow):
    _display_field: str = 'Prologue'

    Prologue: typing.Any = 0
    Epilogue: typing.Any = 1

class AnimaWeaponIconRow(ExdRow):
    Hyperconductive: typing.Any = 0
    Reborn: typing.Any = 1
    Sharpened: typing.Any = 2
    Zodiac: typing.Any = 3
    ZodiacLux: typing.Any = 4

class AnimaWeaponItemRow(ExdRow):
    Item0: typing.Any = 0
    Item1: typing.Any = 1
    Item2: typing.Any = 2
    Item3: typing.Any = 3
    Item4: typing.Any = 4
    Item5: typing.Any = 5
    Item6: typing.Any = 6
    Item7: typing.Any = 7
    Item8: typing.Any = 8
    Item9: typing.Any = 9
    Item10: typing.Any = 10
    Item11: typing.Any = 11
    Item12: typing.Any = 12
    Item13: typing.Any = 13

class AnimationLODRow(ExdRow):
    CameraDistance: typing.Any = 0
    SampleInterval: typing.Any = 1
    BoneLOD: typing.Any = 2
    AnimationEnable0: typing.Any = 3
    AnimationEnable1: typing.Any = 4
    AnimationEnable2: typing.Any = 5
    AnimationEnable3: typing.Any = 6
    AnimationEnable4: typing.Any = 7
    AnimationEnable5: typing.Any = 8
    AnimationEnable6: typing.Any = 9
    AnimationEnable7: typing.Any = 10

class AozActionRow(ExdRow):
    _display_field: str = 'Action'

    Action: typing.Any = 0
    Rank: typing.Any = 1

class AozActionTransientRow(ExdRow):
    _display_field: str = 'Icon'

    Stats: typing.Any = 0
    Description: typing.Any = 1
    Icon: typing.Any = 2
    RequiredForQuest: typing.Any = 3
    PreviousQuest: typing.Any = 4
    Location: typing.Any = 5
    Number: typing.Any = 6
    LocationKey: typing.Any = 7
    TargetsEnemy: typing.Any = 8
    TargetsSelfOrAlly: typing.Any = 9
    CauseSlow: typing.Any = 10
    CausePetrify: typing.Any = 11
    CauseParalysis: typing.Any = 12
    CauseInterrupt: typing.Any = 13
    CauseBlind: typing.Any = 14
    CauseStun: typing.Any = 15
    CauseSleep: typing.Any = 16
    CauseBind: typing.Any = 17
    CauseHeavy: typing.Any = 18
    CauseDeath: typing.Any = 19

class AquariumFishRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0
    Unknown0: typing.Any = 1
    AquariumWater: typing.Any = 2
    Size: typing.Any = 3

class AquariumWaterRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Unknown0: typing.Any = 1

class ArchiveItemRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class ArrayEventHandlerRow(ExdRow):
    Data0: typing.Any = 0
    Data1: typing.Any = 1
    Data2: typing.Any = 2
    Data3: typing.Any = 3
    Data4: typing.Any = 4
    Data5: typing.Any = 5
    Data6: typing.Any = 6
    Data7: typing.Any = 7
    Data8: typing.Any = 8
    Data9: typing.Any = 9
    Data10: typing.Any = 10
    Data11: typing.Any = 11
    Data12: typing.Any = 12
    Data13: typing.Any = 13
    Data14: typing.Any = 14
    Data15: typing.Any = 15

class AttackTypeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class AttractRow(ExdRow):
    MaxDistance: typing.Any = 0
    Speed: typing.Any = 1
    MinRemainingDistance: typing.Any = 2
    Direction: typing.Any = 3
    UseDistanceBetweenHitboxes: typing.Any = 4

class AttributiveRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown24: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    Unknown27: typing.Any = 27
    Unknown28: typing.Any = 28
    Unknown29: typing.Any = 29
    Unknown30: typing.Any = 30
    Unknown31: typing.Any = 31
    Unknown32: typing.Any = 32
    Unknown33: typing.Any = 33
    Unknown34: typing.Any = 34
    Unknown35: typing.Any = 35
    Unknown36: typing.Any = 36
    Unknown37: typing.Any = 37
    Unknown38: typing.Any = 38
    Unknown39: typing.Any = 39
    Unknown40: typing.Any = 40

class BGMRow(ExdRow):
    _display_field: str = 'File'

    File: typing.Any = 0
    DisableRestartResetTime: typing.Any = 1
    Priority: typing.Any = 2
    SpecialMode: typing.Any = 3
    DisableRestartTimeOut: typing.Any = 4
    DisableRestart: typing.Any = 5
    PassEnd: typing.Any = 6

class BGMFadeRow(ExdRow):
    SceneOut: typing.Any = 0
    SceneIn: typing.Any = 1
    BGMFadeType: typing.Any = 2

class BGMFadeTypeRow(ExdRow):
    FadeOutTime: typing.Any = 0
    FadeInTime: typing.Any = 1
    FadeInStartTime: typing.Any = 2
    ResumeFadeInTime: typing.Any = 3

class BGMSceneRow(ExdRow):
    EnableDisableRestart: typing.Any = 0
    Resume: typing.Any = 1
    EnablePassEnd: typing.Any = 2
    ForceAutoReset: typing.Any = 3
    IgnoreBattle: typing.Any = 4

class BGMSituationRow(ExdRow):
    DaytimeID: typing.Any = 0
    NightID: typing.Any = 1
    BattleID: typing.Any = 2
    DaybreakID: typing.Any = 3
    TwilightID: typing.Any = 4

class BGMSwitchRow(ExdRow):
    Quest: typing.Any = 0
    BGM: typing.Any = 1
    BGMSystemDefine: typing.Any = 2
    Unknown0: typing.Any = 3

class BGMSystemDefineRow(ExdRow):
    _display_field: str = 'Define'

    Define: typing.Any = 0

class BNpcAnnounceIconRow(ExdRow):
    _display_field: str = 'Icon'

    Icon: typing.Any = 0

class BNpcBaseRow(ExdRow):
    Scale: typing.Any = 0
    ArrayEventHandler: typing.Any = 1
    Behavior: typing.Any = 2
    ModelChara: typing.Any = 3
    BNpcCustomize: typing.Any = 4
    NpcEquip: typing.Any = 5
    Special: typing.Any = 6
    Unknown9: typing.Any = 7
    Battalion: typing.Any = 8
    LinkRace: typing.Any = 9
    Rank: typing.Any = 10
    SEPack: typing.Any = 11
    Unknown0: typing.Any = 12
    BNpcParts: typing.Any = 13
    Unknown1: typing.Any = 14
    Unknown2: typing.Any = 15
    Unknown3: typing.Any = 16
    Unknown10: typing.Any = 17
    Unknown4: typing.Any = 18
    IsOmnidirectional: typing.Any = 19
    Unknown6: typing.Any = 20
    IsTargetLine: typing.Any = 21
    IsDisplayLevel: typing.Any = 22
    Unknown7: typing.Any = 23
    Unknown_70: typing.Any = 24
    Unknown8: typing.Any = 25

class BNpcBasePopVfxRow(ExdRow):
    Unknown0: typing.Any = 0

class BNpcCustomizeRow(ExdRow):
    Race: typing.Any = 0
    Gender: typing.Any = 1
    BodyType: typing.Any = 2
    Height: typing.Any = 3
    Tribe: typing.Any = 4
    Face: typing.Any = 5
    HairStyle: typing.Any = 6
    HairHighlight: typing.Any = 7
    SkinColor: typing.Any = 8
    EyeHeterochromia: typing.Any = 9
    HairColor: typing.Any = 10
    HairHighlightColor: typing.Any = 11
    FacialFeature: typing.Any = 12
    FacialFeatureColor: typing.Any = 13
    Eyebrows: typing.Any = 14
    EyeColor: typing.Any = 15
    EyeShape: typing.Any = 16
    Nose: typing.Any = 17
    Jaw: typing.Any = 18
    Mouth: typing.Any = 19
    LipColor: typing.Any = 20
    BustOrTone1: typing.Any = 21
    ExtraFeature1: typing.Any = 22
    ExtraFeature2OrBust: typing.Any = 23
    FacePaint: typing.Any = 24
    FacePaintColor: typing.Any = 25

class BNpcNameRow(ExdRow):
    _display_field: str = 'Singular'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Adjective: typing.Any = 2
    PossessivePronoun: typing.Any = 3
    StartsWithVowel: typing.Any = 4
    Unknown0: typing.Any = 5
    Pronoun: typing.Any = 6
    Article: typing.Any = 7

class BNpcPartsRow(ExdRow):
    X1: typing.Any = 0
    X2: typing.Any = 1
    X3: typing.Any = 2
    X4: typing.Any = 3
    X5: typing.Any = 4
    Unknown0: typing.Any = 5
    Y1: typing.Any = 6
    Y2: typing.Any = 7
    Y3: typing.Any = 8
    Y4: typing.Any = 9
    Y5: typing.Any = 10
    Unknown1: typing.Any = 11
    Z1: typing.Any = 12
    Z2: typing.Any = 13
    Z3: typing.Any = 14
    Z4: typing.Any = 15
    Z5: typing.Any = 16
    Unknown2: typing.Any = 17
    Scale1: typing.Any = 18
    Scale2: typing.Any = 19
    Unknown3: typing.Any = 20
    Scale4: typing.Any = 21
    Scale5: typing.Any = 22
    Unknown4: typing.Any = 23
    BNpcBase1: typing.Any = 24
    BNpcBase2: typing.Any = 25
    BNpcBase3: typing.Any = 26
    BNpcBase4: typing.Any = 27
    BNpcBase5: typing.Any = 28
    Unknown5: typing.Any = 29
    Unknown6: typing.Any = 30
    Unknown7: typing.Any = 31
    Scale3: typing.Any = 32
    Unknown8: typing.Any = 33
    Unknown9: typing.Any = 34
    Unknown10: typing.Any = 35
    PartSlot1: typing.Any = 36
    PartSlot2: typing.Any = 37
    PartSlot3: typing.Any = 38
    PartSlot4: typing.Any = 39
    PartSlot5: typing.Any = 40
    Unknown11: typing.Any = 41
    Unknown12: typing.Any = 42
    Unknown13: typing.Any = 43
    Unknown14: typing.Any = 44
    Unknown15: typing.Any = 45
    Unknown16: typing.Any = 46
    Unknown17: typing.Any = 47
    Unknown18: typing.Any = 48
    Unknown19: typing.Any = 49
    Unknown20: typing.Any = 50
    Unknown21: typing.Any = 51
    Unknown22: typing.Any = 52
    Unknown23: typing.Any = 53
    Unknown24: typing.Any = 54
    Unknown25: typing.Any = 55
    Unknown26: typing.Any = 56
    Unknown27: typing.Any = 57
    Unknown28: typing.Any = 58
    Unknown29: typing.Any = 59
    Unknown30: typing.Any = 60
    Unknown31: typing.Any = 61
    Unknown32: typing.Any = 62
    Unknown33: typing.Any = 63
    Unknown34: typing.Any = 64
    Unknown35: typing.Any = 65
    Unknown36: typing.Any = 66

class BNpcStateRow(ExdRow):
    Scale: typing.Any = 0
    LoopTimeline: typing.Any = 1
    Idle: typing.Any = 2
    Slot: typing.Any = 3
    Unknown0: typing.Any = 4
    Attribute0: typing.Any = 5
    Attribute1: typing.Any = 6
    Attribute2: typing.Any = 7
    Unknown1: typing.Any = 8
    OverRay: typing.Any = 9
    Unknown2: typing.Any = 10
    AttributeFlag0: typing.Any = 11
    AttributeFlag1: typing.Any = 12
    AttributeFlag2: typing.Any = 13
    Unknown3: typing.Any = 14

class BacklightColorRow(ExdRow):
    _display_field: str = 'Color'

    Color: typing.Any = 0

class BallistaRow(ExdRow):
    BNPC: typing.Any = 0
    Angle: typing.Any = 1
    Action0: typing.Any = 2
    Action1: typing.Any = 3
    Action2: typing.Any = 4
    Action3: typing.Any = 5
    Bullet: typing.Any = 6
    Unknown0: typing.Any = 7
    Unknown1: typing.Any = 8
    Near: typing.Any = 9
    Far: typing.Any = 10

class BalloonRow(ExdRow):
    _display_field: str = 'Dialogue'

    Dialogue: typing.Any = 0
    Slowly: typing.Any = 1

class BankaCraftWorksRow(ExdRow):
    Description: typing.Any = 0
    Questgiver: typing.Any = 1
    Unknown2: typing.Any = 2

class BankaCraftWorksSupplyRow(ExdRow):
    Item0: typing.Any = 0
    Item1: typing.Any = 1
    Item2: typing.Any = 2
    Item3: typing.Any = 3

class BannerBgRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Image: typing.Any = 1
    Icon: typing.Any = 2
    UnlockCondition: typing.Any = 3
    Unknown_70_1: typing.Any = 4
    Unknown_70_2: typing.Any = 5
    Unknown0: typing.Any = 6
    SortKey: typing.Any = 7
    Unknown_70_3: typing.Any = 8

class BannerConditionRow(ExdRow):
    UnlockCriteria10: typing.Any = 0
    UnlockCriteria11: typing.Any = 1
    UnlockCriteria2: typing.Any = 2
    UnlockCriteria3: typing.Any = 3
    UnlockCriteria4: typing.Any = 4
    Unknown1: typing.Any = 5
    Prerequisite: typing.Any = 6
    UnlockType1: typing.Any = 7
    UnlockType2: typing.Any = 8
    PrerequisiteType: typing.Any = 9
    UnlockHint: typing.Any = 10
    Unknown0: typing.Any = 11

class BannerDecorationRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Image: typing.Any = 1
    Icon: typing.Any = 2
    UnlockCondition: typing.Any = 3
    Unknown_70_1: typing.Any = 4
    Unknown_70_2: typing.Any = 5
    Unknown0: typing.Any = 6
    SortKey: typing.Any = 7
    Unknown_70_3: typing.Any = 8

class BannerDesignPresetRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Background: typing.Any = 1
    Frame: typing.Any = 2
    Decoration: typing.Any = 3
    SortKey: typing.Any = 4

class BannerFacialRow(ExdRow):
    Emote: typing.Any = 0
    UnlockCondition: typing.Any = 1
    Unknown_70_1: typing.Any = 2
    Unknown_70_2: typing.Any = 3
    Unknown0: typing.Any = 4
    SortKey: typing.Any = 5

class BannerFrameRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Image: typing.Any = 1
    Icon: typing.Any = 2
    UnlockCondition: typing.Any = 3
    Unknown_70_1: typing.Any = 4
    Unknown_70_2: typing.Any = 5
    Unknown0: typing.Any = 6
    SortKey: typing.Any = 7
    Unknown_70_3: typing.Any = 8

class BannerObtainHintTypeRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0

class BannerPresetRow(ExdRow):
    CameraPositionX: typing.Any = 0
    CameraPositionY: typing.Any = 1
    CameraPositionZ: typing.Any = 2
    CameraTargetX: typing.Any = 3
    CameraTargetY: typing.Any = 4
    CameraTargetZ: typing.Any = 5
    AnimationProgress: typing.Any = 6
    HeadDirectionX: typing.Any = 7
    HeadDirectionY: typing.Any = 8
    EyeDirectionX: typing.Any = 9
    EyeDirectionY: typing.Any = 10
    Expression: typing.Any = 11
    BannerTimeline: typing.Any = 12
    ImageRotation: typing.Any = 13
    DirectionalLightingVerticalAngle: typing.Any = 14
    DirectionalLightingHorizontalAngle: typing.Any = 15
    CameraZoom: typing.Any = 16
    BannerDesignPreset: typing.Any = 17
    DirectionalLightingColorRed: typing.Any = 18
    DirectionalLightingColorGreen: typing.Any = 19
    DirectionalLightingColorBlue: typing.Any = 20
    DirectionalLightingBrightness: typing.Any = 21
    AmbientLightingColorRed: typing.Any = 22
    AmbientLightingColorGreen: typing.Any = 23
    AmbientLightingColorBlue: typing.Any = 24
    AmbientLightingBrightness: typing.Any = 25

class BannerTimelineRow(ExdRow):
    Name: typing.Any = 0
    AdditionalData: typing.Any = 1
    Icon: typing.Any = 2
    UnlockCondition: typing.Any = 3
    Unknown_70_1: typing.Any = 4
    Unknown_70_2: typing.Any = 5
    Unknown0: typing.Any = 6
    SortKey: typing.Any = 7
    Type: typing.Any = 8
    AcceptClassJobCategory: typing.Any = 9
    Category: typing.Any = 10

class BaseParamRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    OneHandWeaponPercent: typing.Any = 2
    OffHandPercent: typing.Any = 3
    HeadPercent: typing.Any = 4
    ChestPercent: typing.Any = 5
    HandsPercent: typing.Any = 6
    WaistPercent: typing.Any = 7
    LegsPercent: typing.Any = 8
    FeetPercent: typing.Any = 9
    EarringPercent: typing.Any = 10
    NecklacePercent: typing.Any = 11
    BraceletPercent: typing.Any = 12
    RingPercent: typing.Any = 13
    TwoHandWeaponPercent: typing.Any = 14
    UnderArmorPercent: typing.Any = 15
    ChestHeadPercent: typing.Any = 16
    ChestHeadLegsFeetPercent: typing.Any = 17
    Unknown0: typing.Any = 18
    LegsFeetPercent: typing.Any = 19
    HeadChestHandsLegsFeetPercent: typing.Any = 20
    ChestLegsGlovesPercent: typing.Any = 21
    ChestLegsFeetPercent: typing.Any = 22
    Unknown1: typing.Any = 23
    Unknown3: typing.Any = 24
    OrderPriority: typing.Any = 25
    MeldParam0: typing.Any = 26
    MeldParam1: typing.Any = 27
    MeldParam2: typing.Any = 28
    MeldParam3: typing.Any = 29
    MeldParam4: typing.Any = 30
    MeldParam5: typing.Any = 31
    MeldParam6: typing.Any = 32
    MeldParam7: typing.Any = 33
    MeldParam8: typing.Any = 34
    MeldParam9: typing.Any = 35
    MeldParam10: typing.Any = 36
    MeldParam11: typing.Any = 37
    MeldParam12: typing.Any = 38
    PacketIndex: typing.Any = 39
    Unknown2: typing.Any = 40

class BattalionRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14

class BattleLeveRow(ExdRow):
    Time0: typing.Any = 0
    Time1: typing.Any = 1
    Time2: typing.Any = 2
    Time3: typing.Any = 3
    Time4: typing.Any = 4
    Time5: typing.Any = 5
    Time6: typing.Any = 6
    Time7: typing.Any = 7
    LeveData0: typing.Any = 8
    LeveData1: typing.Any = 9
    LeveData2: typing.Any = 10
    LeveData3: typing.Any = 11
    LeveData4: typing.Any = 12
    LeveData5: typing.Any = 13
    LeveData6: typing.Any = 14
    LeveData7: typing.Any = 15
    ToDoSequence0: typing.Any = 16
    ToDoSequence1: typing.Any = 17
    ToDoSequence2: typing.Any = 18
    ToDoSequence3: typing.Any = 19
    ToDoSequence4: typing.Any = 20
    ToDoSequence5: typing.Any = 21
    ToDoSequence6: typing.Any = 22
    ToDoSequence7: typing.Any = 23
    Rule: typing.Any = 24
    Objectives0: typing.Any = 25
    Objectives1: typing.Any = 26
    Objectives2: typing.Any = 27
    Help0: typing.Any = 28
    Help1: typing.Any = 29
    Variant: typing.Any = 30

class BattleLeveRuleRow(ExdRow):
    _display_field: str = 'Rule'

    Rule: typing.Any = 0

class BeastRankBonusRow(ExdRow):
    Item: typing.Any = 0
    Neutral: typing.Any = 1
    Recognized: typing.Any = 2
    Friendly: typing.Any = 3
    Trusted: typing.Any = 4
    Respected: typing.Any = 5
    Honored: typing.Any = 6
    Sworn: typing.Any = 7
    AlliedBloodsworn: typing.Any = 8
    ItemQuantity0: typing.Any = 9
    ItemQuantity1: typing.Any = 10
    ItemQuantity2: typing.Any = 11
    ItemQuantity3: typing.Any = 12
    ItemQuantity4: typing.Any = 13
    ItemQuantity5: typing.Any = 14
    ItemQuantity6: typing.Any = 15
    ItemQuantity7: typing.Any = 16

class BeastReputationRankRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    AlliedNames: typing.Any = 1
    Color: typing.Any = 2
    RequiredReputation: typing.Any = 3

class BeastTribeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Plural: typing.Any = 1
    NameRelation: typing.Any = 2
    Adjective: typing.Any = 3
    PossessivePronoun: typing.Any = 4
    StartsWithVowel: typing.Any = 5
    Pronoun: typing.Any = 6
    Article: typing.Any = 7
    DEF: typing.Any = 8
    IconReputation: typing.Any = 9
    Icon: typing.Any = 10
    Unknown1: typing.Any = 11
    Unknown2: typing.Any = 12
    CurrencyItem: typing.Any = 13
    MinLevel: typing.Any = 14
    BeastRankBonus: typing.Any = 15
    MaxRank: typing.Any = 16
    Expansion: typing.Any = 17
    DisplayOrder: typing.Any = 18
    Unknown0: typing.Any = 19

class BehaviorRow(ExdRow):
    ContentArgument0: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2
    Unknown2: typing.Any = 3
    Unknown3: typing.Any = 4
    Balloon: typing.Any = 5
    Unknown4: typing.Any = 6
    Unknown5: typing.Any = 7
    Unknown6: typing.Any = 8
    Unknown7: typing.Any = 9
    Condition0Target: typing.Any = 10
    Condition0Type: typing.Any = 11
    Condition1Target: typing.Any = 12
    Condition1Type: typing.Any = 13
    ContentArgument1: typing.Any = 14
    Unknown8: typing.Any = 15
    Unknown9: typing.Any = 16

class BehaviorMoveRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class BehaviorPathRow(ExdRow):
    Speed: typing.Any = 0
    IsTurnTransition: typing.Any = 1
    IsFadeOut: typing.Any = 2
    IsFadeIn: typing.Any = 3
    IsWalking: typing.Any = 4
    Unknown0: typing.Any = 5

class BenchmarkCutSceneTableRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6

class BenchmarkOverrideEquipmentRow(ExdRow):
    ModelMainHand: typing.Any = 0
    ModelOffHand: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown2: typing.Any = 4
    ModelHead: typing.Any = 5
    ModelBody: typing.Any = 6
    ModelHands: typing.Any = 7
    ModelLegs: typing.Any = 8
    ModelFeet: typing.Any = 9
    ModelEars: typing.Any = 10
    ModelNeck: typing.Any = 11
    ModelWrists: typing.Any = 12
    ModelLeftRing: typing.Any = 13
    ModelRightRing: typing.Any = 14
    Unknown3: typing.Any = 15
    DyeMainHand: typing.Any = 16
    DyeOffHand: typing.Any = 17
    Unknown4: typing.Any = 18
    DyeHead: typing.Any = 19
    DyeBody: typing.Any = 20
    DyeHands: typing.Any = 21
    DyeLegs: typing.Any = 22
    DyeFeet: typing.Any = 23
    DyeEars: typing.Any = 24
    DyeNeck: typing.Any = 25
    DyeWrists: typing.Any = 26
    DyeLeftRing: typing.Any = 27
    DyeRightRing: typing.Any = 28
    Unknown5: typing.Any = 29

class BgcArmyActionRow(ExdRow):
    Name: typing.Any = 0
    Icon: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class BgcArmyActionTransientRow(ExdRow):
    Text: typing.Any = 0

class BoosterRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown_70: typing.Any = 4

class BuddyRow(ExdRow):
    SoundEffect4: typing.Any = 0
    SoundEffect3: typing.Any = 1
    SoundEffect2: typing.Any = 2
    SoundEffect1: typing.Any = 3
    QuestRequirement2: typing.Any = 4
    QuestRequirement1: typing.Any = 5
    BaseEquip: typing.Any = 6
    Base: typing.Any = 7

class BuddyActionRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Icon: typing.Any = 2
    IconStatus: typing.Any = 3
    UnlockLink: typing.Any = 4
    Sort: typing.Any = 5

class BuddyEquipRow(ExdRow):
    _display_field: str = 'Name'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Name: typing.Any = 2
    Adjective: typing.Any = 3
    PossessivePronoun: typing.Any = 4
    StartsWithVowel: typing.Any = 5
    Unknown0: typing.Any = 6
    Pronoun: typing.Any = 7
    Article: typing.Any = 8
    ModelTop: typing.Any = 9
    ModelBody: typing.Any = 10
    ModelLegs: typing.Any = 11
    IconHead: typing.Any = 12
    IconBody: typing.Any = 13
    IconLegs: typing.Any = 14
    GrandCompany: typing.Any = 15
    Order: typing.Any = 16

class BuddyItemRow(ExdRow):
    Item: typing.Any = 0
    Status: typing.Any = 1
    UseField: typing.Any = 2
    UseTraining: typing.Any = 3
    Unknown0: typing.Any = 4

class BuddyRankRow(ExdRow):
    ExpRequired: typing.Any = 0

class BuddySkillRow(ExdRow):
    Defender: typing.Any = 0
    Attacker: typing.Any = 1
    Healer: typing.Any = 2
    BuddyLevel: typing.Any = 3
    IsActive: typing.Any = 4

class CSBonusContentRow(ExdRow):
    _display_field: str = 'Content0'

    Score1: typing.Any = 0
    Score2: typing.Any = 1
    Score3: typing.Any = 2
    Score4: typing.Any = 3
    Score5: typing.Any = 4
    Content0: typing.Any = 5
    Content1: typing.Any = 6
    Score0: typing.Any = 7
    ContentType: typing.Any = 8
    RewardCount0: typing.Any = 9
    RewardCount1: typing.Any = 10
    RewardCount2: typing.Any = 11
    RewardCount3: typing.Any = 12
    RewardCount4: typing.Any = 13

class CSBonusContentIdentifierRow(ExdRow):
    _display_field: str = 'Content'

    Content: typing.Any = 0
    UnlockQuest0: typing.Any = 1
    UnlockQuest1: typing.Any = 2
    UnlockQuest2: typing.Any = 3
    Unknown6: typing.Any = 4
    Map: typing.Any = 5
    ContentLinkType: typing.Any = 6
    Unknown2: typing.Any = 7

class CSBonusContentTypeRow(ExdRow):
    _display_field: str = 'ContentType'

    Dialogue0: typing.Any = 0
    Dialogue1: typing.Any = 1
    Dialogue2: typing.Any = 2
    Dialogue3: typing.Any = 3
    Image: typing.Any = 4
    Unknown13: typing.Any = 5
    UnlockQuest: typing.Any = 6
    UnlockLink: typing.Any = 7
    Unknown12: typing.Any = 8
    ContentType: typing.Any = 9
    Unknown6: typing.Any = 10

class CSBonusMissionRow(ExdRow):
    Content0: typing.Any = 0
    Content1: typing.Any = 1

class CSBonusMissionTypeRow(ExdRow):
    Unknown0: typing.Any = 0

class CSBonusSeasonRow(ExdRow):
    Item: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Category0: typing.Any = 3
    Category1: typing.Any = 4
    Category2: typing.Any = 5
    Category3: typing.Any = 6
    Text0: typing.Any = 7
    Text1: typing.Any = 8
    Unknown12: typing.Any = 9
    Unknown3: typing.Any = 10
    Unknown4: typing.Any = 11
    Unknown0: typing.Any = 12

class CSBonusTextDataRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0

class CabinetRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0
    Order: typing.Any = 1
    Category: typing.Any = 2
    SubCategory: typing.Any = 3

class CabinetCategoryRow(ExdRow):
    _display_field: str = 'Category'

    Icon: typing.Any = 0
    Category: typing.Any = 1
    MenuOrder: typing.Any = 2
    HideOrder: typing.Any = 3

class CabinetSubCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    MenuOrder: typing.Any = 1

class CalendarRow(ExdRow):
    CalendarStruct0: typing.Any = 0
    CalendarStruct1: typing.Any = 1
    CalendarStruct2: typing.Any = 2
    CalendarStruct3: typing.Any = 3
    CalendarStruct4: typing.Any = 4
    CalendarStruct5: typing.Any = 5
    CalendarStruct6: typing.Any = 6
    CalendarStruct7: typing.Any = 7
    CalendarStruct8: typing.Any = 8
    CalendarStruct9: typing.Any = 9
    CalendarStruct10: typing.Any = 10
    CalendarStruct11: typing.Any = 11
    CalendarStruct12: typing.Any = 12
    CalendarStruct13: typing.Any = 13
    CalendarStruct14: typing.Any = 14
    CalendarStruct15: typing.Any = 15
    CalendarStruct16: typing.Any = 16
    CalendarStruct17: typing.Any = 17
    CalendarStruct18: typing.Any = 18
    CalendarStruct19: typing.Any = 19
    CalendarStruct20: typing.Any = 20
    CalendarStruct21: typing.Any = 21
    CalendarStruct22: typing.Any = 22
    CalendarStruct23: typing.Any = 23
    CalendarStruct24: typing.Any = 24
    CalendarStruct25: typing.Any = 25
    CalendarStruct26: typing.Any = 26
    CalendarStruct27: typing.Any = 27
    CalendarStruct28: typing.Any = 28
    CalendarStruct29: typing.Any = 29
    CalendarStruct30: typing.Any = 30
    CalendarStruct31: typing.Any = 31

class CarryRow(ExdRow):
    Model: typing.Any = 0
    Timeline: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3

class ChannelingRow(ExdRow):
    File: typing.Any = 0
    WidthScale: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown2: typing.Any = 4
    Unknown_70: typing.Any = 5

class CharaCardBaseRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Image: typing.Any = 1
    UnlockCondition: typing.Any = 2
    Unknown_70_1: typing.Any = 3
    Unknown_70_2: typing.Any = 4
    Unknown4: typing.Any = 5
    SortKey: typing.Any = 6
    FontColor: typing.Any = 7
    Unknown3: typing.Any = 8
    Unknown0: typing.Any = 9
    Unknown1: typing.Any = 10
    Unknown2: typing.Any = 11

class CharaCardDecorationRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Image: typing.Any = 1
    UnlockCondition: typing.Any = 2
    Unknown_70_1: typing.Any = 3
    Unknown_70_2: typing.Any = 4
    Unknown3: typing.Any = 5
    SortKey: typing.Any = 6
    Category: typing.Any = 7
    Subtype: typing.Any = 8
    Unknown1: typing.Any = 9
    Unknown2: typing.Any = 10

class CharaCardDesignCategoryRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class CharaCardDesignPresetRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    BasePlate: typing.Any = 1
    Backing: typing.Any = 2
    PatternOverlay: typing.Any = 3
    PortraitFrame: typing.Any = 4
    PlateFrame: typing.Any = 5
    Accent: typing.Any = 6
    SortKey: typing.Any = 7
    TopBorder: typing.Any = 8
    BottomBorder: typing.Any = 9

class CharaCardDesignTypeRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9

class CharaCardHeaderRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    TopImage: typing.Any = 1
    BottomImage: typing.Any = 2
    UnlockCondition: typing.Any = 3
    Unknown_70_1: typing.Any = 4
    Unknown_70_2: typing.Any = 5
    Unknown4: typing.Any = 6
    Unknown5: typing.Any = 7
    FontColor: typing.Any = 8
    Unknown2: typing.Any = 9
    Unknown1: typing.Any = 10
    Unknown0: typing.Any = 11
    Unknown3: typing.Any = 12

class CharaCardPlayStyleRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Icon: typing.Any = 1
    SortKey: typing.Any = 2

class CharaMakeClassEquipRow(ExdRow):
    Helmet: typing.Any = 0
    Top: typing.Any = 1
    Glove: typing.Any = 2
    Down: typing.Any = 3
    Shoes: typing.Any = 4
    Weapon: typing.Any = 5
    SubWeapon: typing.Any = 6
    Class: typing.Any = 7

class CharaMakeCustomizeRow(ExdRow):
    _display_field: str = 'Icon'

    Icon: typing.Any = 0
    Hint: typing.Any = 1
    HintItem: typing.Any = 2
    UnlockLink: typing.Any = 3
    FeatureID: typing.Any = 4
    Unknown0: typing.Any = 5
    IsPurchasable: typing.Any = 6

class CharaMakeNameRow(ExdRow):
    HyurMidlanderMale: typing.Any = 0
    HyurMidlanderFemale: typing.Any = 1
    HyurMidlanderLastName: typing.Any = 2
    HyurHighlanderMale: typing.Any = 3
    HyurHighlanderFemale: typing.Any = 4
    HyurHighlanderLastName: typing.Any = 5
    ElezenMale: typing.Any = 6
    ElezenFemale: typing.Any = 7
    ElezenWildwoodLastName: typing.Any = 8
    ElezenDuskwightLastName: typing.Any = 9
    MiqoteSunMale: typing.Any = 10
    MiqoteSunFemale: typing.Any = 11
    MiqoteSunMaleLastName: typing.Any = 12
    MiqoteSunFemaleLastName: typing.Any = 13
    MiqoteMoonMale: typing.Any = 14
    MiqoteMoonFemale: typing.Any = 15
    MiqoteMoonLastname: typing.Any = 16
    LalafellPlainsfolkFirstNameStart: typing.Any = 17
    LalafellPlainsfolkLastNameStart: typing.Any = 18
    LalafellPlainsfolkEndOfNames: typing.Any = 19
    LalafellDunesfolkMale: typing.Any = 20
    LalafellDunesfolkMaleLastName: typing.Any = 21
    LalafellDunesfolkFemale: typing.Any = 22
    LalafellDunesfolkFemaleLastName: typing.Any = 23
    RoegadynSeaWolfMale: typing.Any = 24
    RoegadynSeaWolfMaleLastName: typing.Any = 25
    RoegadynSeaWolfFemale: typing.Any = 26
    RoegadynSeaWolfFemaleLastName: typing.Any = 27
    RoegadynHellsguardFirstName: typing.Any = 28
    RoegadynHellsguardMaleLastName: typing.Any = 29
    RoegadynHellsguardFemaleLastName: typing.Any = 30
    AuRaRaenMale: typing.Any = 31
    AuRaRaenFemale: typing.Any = 32
    AuRaRaenLastName: typing.Any = 33
    AuRaXaelaMale: typing.Any = 34
    AuRaXaelaFemale: typing.Any = 35
    AuRaXaelaLastName: typing.Any = 36
    HrothgarHellionsFirstName: typing.Any = 37
    HrothgarHellionsLastName: typing.Any = 38
    HrothgarLostFirstName: typing.Any = 39
    HrothgarLostLastName: typing.Any = 40
    Unknown0: typing.Any = 41
    Unknown1: typing.Any = 42
    Unknown2: typing.Any = 43
    VieraFirstName: typing.Any = 44
    VieraRavaLastName: typing.Any = 45
    VieraVeenaLastName: typing.Any = 46
    Unknown_70_1: typing.Any = 47
    Unknown_70_2: typing.Any = 48
    Unknown_70_3: typing.Any = 49

class CharaMakeTypeRow(ExdRow):
    CharaMakeStruct0: typing.Any = 0
    CharaMakeStruct1: typing.Any = 1
    CharaMakeStruct2: typing.Any = 2
    CharaMakeStruct3: typing.Any = 3
    CharaMakeStruct4: typing.Any = 4
    CharaMakeStruct5: typing.Any = 5
    CharaMakeStruct6: typing.Any = 6
    CharaMakeStruct7: typing.Any = 7
    CharaMakeStruct8: typing.Any = 8
    CharaMakeStruct9: typing.Any = 9
    CharaMakeStruct10: typing.Any = 10
    CharaMakeStruct11: typing.Any = 11
    CharaMakeStruct12: typing.Any = 12
    CharaMakeStruct13: typing.Any = 13
    CharaMakeStruct14: typing.Any = 14
    CharaMakeStruct15: typing.Any = 15
    CharaMakeStruct16: typing.Any = 16
    CharaMakeStruct17: typing.Any = 17
    CharaMakeStruct18: typing.Any = 18
    CharaMakeStruct19: typing.Any = 19
    CharaMakeStruct20: typing.Any = 20
    CharaMakeStruct21: typing.Any = 21
    CharaMakeStruct22: typing.Any = 22
    CharaMakeStruct23: typing.Any = 23
    CharaMakeStruct24: typing.Any = 24
    CharaMakeStruct25: typing.Any = 25
    CharaMakeStruct26: typing.Any = 26
    CharaMakeStruct27: typing.Any = 27
    VoiceStruct0: typing.Any = 28
    VoiceStruct1: typing.Any = 29
    VoiceStruct2: typing.Any = 30
    VoiceStruct3: typing.Any = 31
    VoiceStruct4: typing.Any = 32
    VoiceStruct5: typing.Any = 33
    VoiceStruct6: typing.Any = 34
    VoiceStruct7: typing.Any = 35
    VoiceStruct8: typing.Any = 36
    VoiceStruct9: typing.Any = 37
    VoiceStruct10: typing.Any = 38
    VoiceStruct11: typing.Any = 39
    FacialFeatureOption0: typing.Any = 40
    FacialFeatureOption1: typing.Any = 41
    FacialFeatureOption2: typing.Any = 42
    FacialFeatureOption3: typing.Any = 43
    FacialFeatureOption4: typing.Any = 44
    FacialFeatureOption5: typing.Any = 45
    FacialFeatureOption6: typing.Any = 46
    FacialFeatureOption7: typing.Any = 47
    Equipment0: typing.Any = 48
    Equipment1: typing.Any = 49
    Equipment2: typing.Any = 50
    Race: typing.Any = 51
    Tribe: typing.Any = 52
    Gender: typing.Any = 53

class ChatBubbleSampeTextListRow(ExdRow):
    Unknown0: typing.Any = 0

class ChatBubbleTypeRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6

class ChocoboRaceRow(ExdRow):
    ChocoboRaceRank: typing.Any = 0
    ChocoboRaceTerritory: typing.Any = 1

class ChocoboRaceAbilityRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Icon: typing.Any = 2
    Value: typing.Any = 3
    ChocoboRaceAbilityType: typing.Any = 4

class ChocoboRaceAbilityTypeRow(ExdRow):
    _display_field: str = 'IsActive'

    IsActive: typing.Any = 0

class ChocoboRaceCalculateParamRow(ExdRow):
    Unknown0: typing.Any = 0

class ChocoboRaceChallengeRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class ChocoboRaceItemRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Icon: typing.Any = 2

class ChocoboRaceRankRow(ExdRow):
    _display_field: str = 'Name'

    Icon: typing.Any = 0
    RatingMin: typing.Any = 1
    RatingMax: typing.Any = 2
    Name: typing.Any = 3
    Fee: typing.Any = 4

class ChocoboRaceRankingRow(ExdRow):
    Unknown0: typing.Any = 0

class ChocoboRaceStatusRow(ExdRow):
    _display_field: str = 'Status'

    Status: typing.Any = 0
    Unknown0: typing.Any = 1

class ChocoboRaceTerritoryRow(ExdRow):
    _display_field: str = 'Name'

    Icon: typing.Any = 0
    Name: typing.Any = 1

class ChocoboRaceTutorialRow(ExdRow):
    NpcYell0: typing.Any = 0
    NpcYell1: typing.Any = 1
    NpcYell2: typing.Any = 2
    NpcYell3: typing.Any = 3
    NpcYell4: typing.Any = 4
    NpcYell5: typing.Any = 5
    NpcYell6: typing.Any = 6
    NpcYell7: typing.Any = 7
    Unknown0: typing.Any = 8
    Unknown1: typing.Any = 9

class ChocoboRaceWeatherRow(ExdRow):
    WeatherType1: typing.Any = 0
    WeatherType2: typing.Any = 1

class ChocoboTaxiRow(ExdRow):
    _display_field: str = 'Location'

    Location: typing.Any = 0
    TimeRequired: typing.Any = 1
    Unknown0: typing.Any = 2
    Fare: typing.Any = 3
    Unknown1: typing.Any = 4

class ChocoboTaxiStandRow(ExdRow):
    _display_field: str = 'PlaceName'

    PlaceName: typing.Any = 0
    TargetLocations0: typing.Any = 1
    TargetLocations1: typing.Any = 2
    TargetLocations2: typing.Any = 3
    TargetLocations3: typing.Any = 4
    TargetLocations4: typing.Any = 5
    TargetLocations5: typing.Any = 6
    TargetLocations6: typing.Any = 7
    TargetLocations7: typing.Any = 8

class CircleActivityRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Icon: typing.Any = 1
    Order: typing.Any = 2

class ClassJobRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Abbreviation: typing.Any = 1
    NameFemale: typing.Any = 2
    CanQueueForDuty: typing.Any = 3
    NameEnglish: typing.Any = 4
    ItemSoulCrystal: typing.Any = 5
    UnlockQuest: typing.Any = 6
    RelicQuest: typing.Any = 7
    Prerequisite: typing.Any = 8
    Unknown_70_1: typing.Any = 9
    Unknown_70_2: typing.Any = 10
    Unknown9: typing.Any = 11
    ItemStartingWeapon: typing.Any = 12
    Unknown1: typing.Any = 13
    ModifierHitPoints: typing.Any = 14
    ModifierManaPoints: typing.Any = 15
    ModifierStrength: typing.Any = 16
    ModifierVitality: typing.Any = 17
    ModifierDexterity: typing.Any = 18
    ModifierIntelligence: typing.Any = 19
    ModifierMind: typing.Any = 20
    ModifierPiety: typing.Any = 21
    Unknown2: typing.Any = 22
    Unknown3: typing.Any = 23
    Unknown4: typing.Any = 24
    Unknown5: typing.Any = 25
    Unknown6: typing.Any = 26
    Unknown7: typing.Any = 27
    LimitBreak1: typing.Any = 28
    LimitBreak2: typing.Any = 29
    LimitBreak3: typing.Any = 30
    ClassJobCategory: typing.Any = 31
    Unknown8: typing.Any = 32
    JobIndex: typing.Any = 33
    PvPBaseParamValue: typing.Any = 34
    PvPActionSortRow: typing.Any = 35
    PvPInitialSelectActionTrait: typing.Any = 36
    ClassJobParent: typing.Any = 37
    Role: typing.Any = 38
    StartingTown: typing.Any = 39
    PrimaryStat: typing.Any = 40
    UIPriority: typing.Any = 41
    StartingLevel: typing.Any = 42
    PartyBonus: typing.Any = 43
    Unknown11: typing.Any = 44
    ExpArrayIndex: typing.Any = 45
    BattleClassIndex: typing.Any = 46
    DohDolJobIndex: typing.Any = 47
    MonsterNote: typing.Any = 48
    IsLimitedJob: typing.Any = 49

class ClassJobActionUIRow(ExdRow):
    UpgradeAction: typing.Any = 0
    BaseAction: typing.Any = 1
    ComboTreeLayout: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    GroupedCell: typing.Any = 6

class ClassJobActionUICategoryRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class ClassJobCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    ADV: typing.Any = 1
    GLA: typing.Any = 2
    PGL: typing.Any = 3
    MRD: typing.Any = 4
    LNC: typing.Any = 5
    ARC: typing.Any = 6
    CNJ: typing.Any = 7
    THM: typing.Any = 8
    CRP: typing.Any = 9
    BSM: typing.Any = 10
    ARM: typing.Any = 11
    GSM: typing.Any = 12
    LTW: typing.Any = 13
    WVR: typing.Any = 14
    ALC: typing.Any = 15
    CUL: typing.Any = 16
    MIN: typing.Any = 17
    BTN: typing.Any = 18
    FSH: typing.Any = 19
    PLD: typing.Any = 20
    MNK: typing.Any = 21
    WAR: typing.Any = 22
    DRG: typing.Any = 23
    BRD: typing.Any = 24
    WHM: typing.Any = 25
    BLM: typing.Any = 26
    ACN: typing.Any = 27
    SMN: typing.Any = 28
    SCH: typing.Any = 29
    ROG: typing.Any = 30
    NIN: typing.Any = 31
    MCH: typing.Any = 32
    DRK: typing.Any = 33
    AST: typing.Any = 34
    SAM: typing.Any = 35
    RDM: typing.Any = 36
    BLU: typing.Any = 37
    GNB: typing.Any = 38
    DNC: typing.Any = 39
    RPR: typing.Any = 40
    SGE: typing.Any = 41
    VPR: typing.Any = 42
    PCT: typing.Any = 43
    Unknown0: typing.Any = 44
    Unknown1: typing.Any = 45
    Unknown2: typing.Any = 46

class ClassJobResidentRow(ExdRow):
    Unknown0: typing.Any = 0

class CollectablesRefineRow(ExdRow):
    CollectabilityLow: typing.Any = 0
    CollectabilityMid: typing.Any = 1
    CollectabilityHigh: typing.Any = 2

class CollectablesShopRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Quest: typing.Any = 1
    ShopItems0: typing.Any = 2
    ShopItems1: typing.Any = 3
    ShopItems2: typing.Any = 4
    ShopItems3: typing.Any = 5
    ShopItems4: typing.Any = 6
    ShopItems5: typing.Any = 7
    ShopItems6: typing.Any = 8
    ShopItems7: typing.Any = 9
    ShopItems8: typing.Any = 10
    ShopItems9: typing.Any = 11
    ShopItems10: typing.Any = 12
    RewardType: typing.Any = 13

class CollectablesShopItemRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0
    RequiredQuest: typing.Any = 1
    LevelMin: typing.Any = 2
    LevelMax: typing.Any = 3
    CollectablesShopRefine: typing.Any = 4
    CollectablesShopRewardScrip: typing.Any = 5
    CollectablesShopItemGroup: typing.Any = 6
    Stars: typing.Any = 7
    Key: typing.Any = 8

class CollectablesShopItemGroupRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class CollectablesShopRefineRow(ExdRow):
    LowCollectability: typing.Any = 0
    MidCollectability: typing.Any = 1
    HighCollectability: typing.Any = 2

class CollectablesShopRewardItemRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0
    Unknown0: typing.Any = 1
    RewardLow: typing.Any = 2
    RewardMid: typing.Any = 3
    RewardHigh: typing.Any = 4
    Unknown1: typing.Any = 5
    Unknown2: typing.Any = 6
    Unknown3: typing.Any = 7
    Unknown4: typing.Any = 8
    Unknown5: typing.Any = 9

class CollectablesShopRewardScripRow(ExdRow):
    _display_field: str = 'Currency'

    Currency: typing.Any = 0
    LowReward: typing.Any = 1
    MidReward: typing.Any = 2
    HighReward: typing.Any = 3
    ExpRatioLow: typing.Any = 4
    ExpRatioMid: typing.Any = 5
    ExpRatioHigh: typing.Any = 6

class CollisionIdPalletRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class ColorFilterRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15

class ColosseumRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class ColosseumMatchRankRow(ExdRow):
    Unknown0: typing.Any = 0

class CompanionRow(ExdRow):
    _display_field: str = 'Singular'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Adjective: typing.Any = 2
    PossessivePronoun: typing.Any = 3
    StartsWithVowel: typing.Any = 4
    Unknown0: typing.Any = 5
    Pronoun: typing.Any = 6
    Article: typing.Any = 7
    Model: typing.Any = 8
    Priority: typing.Any = 9
    Enemy: typing.Any = 10
    Icon: typing.Any = 11
    Order: typing.Any = 12
    HP: typing.Any = 13
    SkillAngle: typing.Any = 14
    Unknown1: typing.Any = 15
    Scale: typing.Any = 16
    InactiveIdle0: typing.Any = 17
    InactiveIdle1: typing.Any = 18
    InactiveBattle: typing.Any = 19
    InactiveWandering: typing.Any = 20
    Behavior: typing.Any = 21
    Special: typing.Any = 22
    Unknown10: typing.Any = 23
    Unknown11: typing.Any = 24
    WanderingWait: typing.Any = 25
    Unknown2: typing.Any = 26
    Cost: typing.Any = 27
    Unknown3: typing.Any = 28
    SkillCost: typing.Any = 29
    Unknown4: typing.Any = 30
    MinionRace: typing.Any = 31
    Unknown5: typing.Any = 32
    Unknown6: typing.Any = 33
    Unknown7: typing.Any = 34
    Unknown8: typing.Any = 35
    Unknown9: typing.Any = 36
    Battle: typing.Any = 37
    Roulette: typing.Any = 38
    IdleAnimation: typing.Any = 39

class CompanionMoveRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class CompanionTransientRow(ExdRow):
    _display_field: str = 'Description'

    Description: typing.Any = 0
    DescriptionEnhanced: typing.Any = 1
    Tooltip: typing.Any = 2
    SpecialActionName: typing.Any = 3
    SpecialActionDescription: typing.Any = 4
    Attack: typing.Any = 5
    Defense: typing.Any = 6
    Speed: typing.Any = 7
    MinionSkillType: typing.Any = 8
    HasAreaAttack: typing.Any = 9
    StrengthGate: typing.Any = 10
    StrengthEye: typing.Any = 11
    StrengthShield: typing.Any = 12
    StrengthArcana: typing.Any = 13

class CompanyActionRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Cost: typing.Any = 2
    Icon: typing.Any = 3
    FCRank: typing.Any = 4
    Order: typing.Any = 5
    Purchasable: typing.Any = 6

class CompanyCraftDraftRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Order: typing.Any = 1
    RequiredItem0: typing.Any = 2
    RequiredItem1: typing.Any = 3
    RequiredItem2: typing.Any = 4
    CompanyCraftDraftCategory: typing.Any = 5
    RequiredItemCount0: typing.Any = 6
    RequiredItemCount1: typing.Any = 7
    RequiredItemCount2: typing.Any = 8

class CompanyCraftDraftCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    CompanyCraftType0: typing.Any = 1
    CompanyCraftType1: typing.Any = 2
    CompanyCraftType2: typing.Any = 3
    CompanyCraftType3: typing.Any = 4
    CompanyCraftType4: typing.Any = 5
    CompanyCraftType5: typing.Any = 6
    CompanyCraftType6: typing.Any = 7
    CompanyCraftType7: typing.Any = 8
    CompanyCraftType8: typing.Any = 9
    CompanyCraftType9: typing.Any = 10

class CompanyCraftManufactoryStateRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class CompanyCraftPartRow(ExdRow):
    CompanyCraftProcess0: typing.Any = 0
    CompanyCraftProcess1: typing.Any = 1
    CompanyCraftProcess2: typing.Any = 2
    Unknown0: typing.Any = 3
    Unknown1: typing.Any = 4
    CompanyCraftType: typing.Any = 5

class CompanyCraftProcessRow(ExdRow):
    SupplyItem0: typing.Any = 0
    SupplyItem1: typing.Any = 1
    SupplyItem2: typing.Any = 2
    SupplyItem3: typing.Any = 3
    SupplyItem4: typing.Any = 4
    SupplyItem5: typing.Any = 5
    SupplyItem6: typing.Any = 6
    SupplyItem7: typing.Any = 7
    SupplyItem8: typing.Any = 8
    SupplyItem9: typing.Any = 9
    SupplyItem10: typing.Any = 10
    SupplyItem11: typing.Any = 11
    SetQuantity0: typing.Any = 12
    SetQuantity1: typing.Any = 13
    SetQuantity2: typing.Any = 14
    SetQuantity3: typing.Any = 15
    SetQuantity4: typing.Any = 16
    SetQuantity5: typing.Any = 17
    SetQuantity6: typing.Any = 18
    SetQuantity7: typing.Any = 19
    SetQuantity8: typing.Any = 20
    SetQuantity9: typing.Any = 21
    SetQuantity10: typing.Any = 22
    SetQuantity11: typing.Any = 23
    SetsRequired0: typing.Any = 24
    SetsRequired1: typing.Any = 25
    SetsRequired2: typing.Any = 26
    SetsRequired3: typing.Any = 27
    SetsRequired4: typing.Any = 28
    SetsRequired5: typing.Any = 29
    SetsRequired6: typing.Any = 30
    SetsRequired7: typing.Any = 31
    SetsRequired8: typing.Any = 32
    SetsRequired9: typing.Any = 33
    SetsRequired10: typing.Any = 34
    SetsRequired11: typing.Any = 35

class CompanyCraftSequenceRow(ExdRow):
    _display_field: str = 'ResultItem'

    Order: typing.Any = 0
    ResultItem: typing.Any = 1
    Category: typing.Any = 2
    CompanyCraftDraftCategory: typing.Any = 3
    CompanyCraftType: typing.Any = 4
    CompanyCraftDraft: typing.Any = 5
    CompanyCraftPart0: typing.Any = 6
    CompanyCraftPart1: typing.Any = 7
    CompanyCraftPart2: typing.Any = 8
    CompanyCraftPart3: typing.Any = 9
    CompanyCraftPart4: typing.Any = 10
    CompanyCraftPart5: typing.Any = 11
    CompanyCraftPart6: typing.Any = 12
    CompanyCraftPart7: typing.Any = 13

class CompanyCraftSupplyItemRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0

class CompanyCraftTypeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class CompanyLeveRow(ExdRow):
    RoutePointTime0: typing.Any = 0
    RoutePointTime1: typing.Any = 1
    RoutePointTime2: typing.Any = 2
    RoutePointTime3: typing.Any = 3
    RoutePointTime4: typing.Any = 4
    RoutePointTime5: typing.Any = 5
    RoutePointTime6: typing.Any = 6
    RoutePointTime7: typing.Any = 7
    CompanyLeveStruct0: typing.Any = 8
    CompanyLeveStruct1: typing.Any = 9
    CompanyLeveStruct2: typing.Any = 10
    CompanyLeveStruct3: typing.Any = 11
    CompanyLeveStruct4: typing.Any = 12
    CompanyLeveStruct5: typing.Any = 13
    CompanyLeveStruct6: typing.Any = 14
    CompanyLeveStruct7: typing.Any = 15
    ToDoSequence0: typing.Any = 16
    ToDoSequence1: typing.Any = 17
    ToDoSequence2: typing.Any = 18
    ToDoSequence3: typing.Any = 19
    ToDoSequence4: typing.Any = 20
    ToDoSequence5: typing.Any = 21
    ToDoSequence6: typing.Any = 22
    ToDoSequence7: typing.Any = 23
    Rule: typing.Any = 24
    RuleParam: typing.Any = 25

class CompanyLeveRuleRow(ExdRow):
    _display_field: str = 'Type'

    Type: typing.Any = 0
    Objective: typing.Any = 1
    Help: typing.Any = 2

class CompleteJournalRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2
    Icon: typing.Any = 3
    Cutscene0: typing.Any = 4
    Cutscene1: typing.Any = 5
    Cutscene2: typing.Any = 6
    Cutscene3: typing.Any = 7
    Cutscene4: typing.Any = 8
    Cutscene5: typing.Any = 9
    Cutscene6: typing.Any = 10
    Cutscene7: typing.Any = 11
    Cutscene8: typing.Any = 12
    Cutscene9: typing.Any = 13
    Cutscene10: typing.Any = 14
    Cutscene11: typing.Any = 15
    Cutscene12: typing.Any = 16
    Cutscene13: typing.Any = 17
    Cutscene14: typing.Any = 18
    Cutscene15: typing.Any = 19
    Cutscene16: typing.Any = 20
    Cutscene17: typing.Any = 21
    Cutscene18: typing.Any = 22
    Cutscene19: typing.Any = 23
    Cutscene20: typing.Any = 24
    Cutscene21: typing.Any = 25
    Cutscene22: typing.Any = 26
    Cutscene23: typing.Any = 27
    RequiredLevel: typing.Any = 28
    Unknown2: typing.Any = 29

class CompleteJournalCategoryRow(ExdRow):
    FirstQuest: typing.Any = 0
    LastQuest: typing.Any = 1
    Unknown0: typing.Any = 2

class CompletionRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0
    GroupTitle: typing.Any = 1
    LookupTable: typing.Any = 2
    Group: typing.Any = 3
    Key: typing.Any = 4

class ConditionRow(ExdRow):
    LogMessage: typing.Any = 0
    Permission: typing.Any = 1
    LogMessagePriority: typing.Any = 2
    IsNetworked: typing.Any = 3

class ConfigKeyRow(ExdRow):
    Text: typing.Any = 0
    Label: typing.Any = 1
    Unknown0: typing.Any = 2
    Param: typing.Any = 3
    Platform: typing.Any = 4
    Category: typing.Any = 5
    BacklightColor: typing.Any = 6
    Required: typing.Any = 7

class ContentAttributeRectRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown24: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    Unknown27: typing.Any = 27
    Unknown28: typing.Any = 28
    Unknown29: typing.Any = 29
    Unknown30: typing.Any = 30
    Unknown31: typing.Any = 31
    Unknown32: typing.Any = 32
    Unknown33: typing.Any = 33
    Unknown34: typing.Any = 34
    Unknown35: typing.Any = 35
    Unknown36: typing.Any = 36
    Unknown37: typing.Any = 37
    Unknown38: typing.Any = 38
    Unknown39: typing.Any = 39
    Unknown40: typing.Any = 40
    Unknown41: typing.Any = 41
    Unknown42: typing.Any = 42
    Unknown43: typing.Any = 43
    Unknown44: typing.Any = 44
    Unknown45: typing.Any = 45
    Unknown46: typing.Any = 46
    Unknown47: typing.Any = 47
    Unknown48: typing.Any = 48
    Unknown49: typing.Any = 49
    Unknown50: typing.Any = 50
    Unknown51: typing.Any = 51
    Unknown52: typing.Any = 52
    Unknown53: typing.Any = 53
    Unknown54: typing.Any = 54
    Unknown55: typing.Any = 55
    Unknown56: typing.Any = 56
    Unknown57: typing.Any = 57
    Unknown58: typing.Any = 58
    Unknown59: typing.Any = 59
    Unknown60: typing.Any = 60
    Unknown61: typing.Any = 61
    Unknown62: typing.Any = 62
    Unknown63: typing.Any = 63
    Unknown64: typing.Any = 64
    Unknown65: typing.Any = 65
    Unknown66: typing.Any = 66
    Unknown67: typing.Any = 67
    Unknown68: typing.Any = 68
    Unknown69: typing.Any = 69
    Unknown70: typing.Any = 70
    Unknown71: typing.Any = 71
    Unknown72: typing.Any = 72
    Unknown73: typing.Any = 73
    Unknown74: typing.Any = 74
    Unknown75: typing.Any = 75
    Unknown76: typing.Any = 76
    Unknown77: typing.Any = 77
    Unknown78: typing.Any = 78
    Unknown79: typing.Any = 79
    Unknown80: typing.Any = 80
    Unknown81: typing.Any = 81
    Unknown82: typing.Any = 82
    Unknown83: typing.Any = 83
    Unknown84: typing.Any = 84
    Unknown85: typing.Any = 85
    Unknown86: typing.Any = 86
    Unknown87: typing.Any = 87
    Unknown88: typing.Any = 88
    Unknown89: typing.Any = 89
    Unknown90: typing.Any = 90
    Unknown91: typing.Any = 91
    Unknown92: typing.Any = 92
    Unknown93: typing.Any = 93
    Unknown94: typing.Any = 94
    Unknown95: typing.Any = 95
    Unknown96: typing.Any = 96
    Unknown97: typing.Any = 97
    Unknown98: typing.Any = 98
    Unknown99: typing.Any = 99
    Unknown100: typing.Any = 100
    Unknown101: typing.Any = 101
    Unknown102: typing.Any = 102
    Unknown103: typing.Any = 103
    Unknown104: typing.Any = 104
    Unknown105: typing.Any = 105
    Unknown106: typing.Any = 106
    Unknown107: typing.Any = 107
    Unknown108: typing.Any = 108
    Unknown109: typing.Any = 109
    Unknown110: typing.Any = 110
    Unknown111: typing.Any = 111
    Unknown112: typing.Any = 112
    Unknown113: typing.Any = 113
    Unknown114: typing.Any = 114
    Unknown115: typing.Any = 115
    Unknown116: typing.Any = 116
    Unknown117: typing.Any = 117
    Unknown118: typing.Any = 118
    Unknown119: typing.Any = 119
    Unknown120: typing.Any = 120
    Unknown121: typing.Any = 121
    Unknown122: typing.Any = 122
    Unknown123: typing.Any = 123
    Unknown124: typing.Any = 124
    Unknown125: typing.Any = 125
    Unknown126: typing.Any = 126
    Unknown127: typing.Any = 127

class ContentCloseCycleRow(ExdRow):
    Unixtime: typing.Any = 0
    TimeSeconds: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown2: typing.Any = 4
    Unknown3: typing.Any = 5
    Unknown4: typing.Any = 6
    Unknown5: typing.Any = 7
    Unknown6: typing.Any = 8
    Unknown7: typing.Any = 9
    Unknown8: typing.Any = 10
    Unknown9: typing.Any = 11
    Unknown10: typing.Any = 12

class ContentDirectorBattleTalkRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Text: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class ContentDirectorManagedSGRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class ContentEffectiveTimeRow(ExdRow):
    Unknown0: typing.Any = 0

class ContentEntryRow(ExdRow):
    Unknown0: typing.Any = 0

class ContentEventItemRow(ExdRow):
    EventItem: typing.Any = 0

class ContentExActionRow(ExdRow):
    Name0: typing.Any = 0
    Name1: typing.Any = 1
    Charges0: typing.Any = 2
    Charges1: typing.Any = 3

class ContentFinderConditionRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    NameShort: typing.Any = 1
    LevelingRoulette: typing.Any = 2
    HighLevelRoulette: typing.Any = 3
    MSQRoulette: typing.Any = 4
    GuildHestRoulette: typing.Any = 5
    ExpertRoulette: typing.Any = 6
    TrialRoulette: typing.Any = 7
    DailyFrontlineChallenge: typing.Any = 8
    LevelCapRoulette: typing.Any = 9
    MentorRoulette: typing.Any = 10
    Unknown0: typing.Any = 11
    Unknown1: typing.Any = 12
    Unknown2: typing.Any = 13
    Unknown3: typing.Any = 14
    Unknown4: typing.Any = 15
    AllianceRoulette: typing.Any = 16
    FeastTeamRoulette: typing.Any = 17
    NormalRaidRoulette: typing.Any = 18
    Unknown5: typing.Any = 19
    Unknown6: typing.Any = 20
    Unknown7: typing.Any = 21
    Unknown8: typing.Any = 22
    Unknown9: typing.Any = 23
    Unknown10: typing.Any = 24
    Unknown11: typing.Any = 25
    Unknown12: typing.Any = 26
    Unknown13: typing.Any = 27
    Unknown14: typing.Any = 28
    Unknown15: typing.Any = 29
    Unknown16: typing.Any = 30
    Unknown17: typing.Any = 31
    Unknown18: typing.Any = 32
    Unknown19: typing.Any = 33
    Unknown20: typing.Any = 34
    Unknown21: typing.Any = 35
    Unknown22: typing.Any = 36
    Unknown23: typing.Any = 37
    Unknown24: typing.Any = 38
    Unknown25: typing.Any = 39
    Unknown26: typing.Any = 40
    Unknown27: typing.Any = 41
    Unknown28: typing.Any = 42
    ShortCode: typing.Any = 43
    Unknown29: typing.Any = 44
    Unknown30: typing.Any = 45
    UnlockQuest: typing.Any = 46
    Unknown31: typing.Any = 47
    Unknown_70_1: typing.Any = 48
    Transient: typing.Any = 49
    Image: typing.Any = 50
    Icon: typing.Any = 51
    Unknown32: typing.Any = 52
    TerritoryType: typing.Any = 53
    Content: typing.Any = 54
    ItemLevelRequired: typing.Any = 55
    ItemLevelSync: typing.Any = 56
    SortKey: typing.Any = 57
    ContentLinkType: typing.Any = 58
    Unknown33: typing.Any = 59
    AcceptClassJobCategory: typing.Any = 60
    ContentMemberType: typing.Any = 61
    Unknown34: typing.Any = 62
    Unknown35: typing.Any = 63
    Unknown36: typing.Any = 64
    Unknown37: typing.Any = 65
    ClassJobLevelRequired: typing.Any = 66
    ClassJobLevelSync: typing.Any = 67
    Unknown38: typing.Any = 68
    Unknown39: typing.Any = 69
    ContentType: typing.Any = 70
    ContentUICategory: typing.Any = 71
    Unknown40: typing.Any = 72
    Unknown41: typing.Any = 73
    PvP: typing.Any = 74
    Unknown_70_2: typing.Any = 75
    Unknown42: typing.Any = 76
    AllowUndersized: typing.Any = 77
    Unknown43: typing.Any = 78
    Unknown57: typing.Any = 79
    AllowReplacement: typing.Any = 80
    Unknown44: typing.Any = 81
    AllowExplorerMode: typing.Any = 82
    Unknown45: typing.Any = 83
    Unknown46: typing.Any = 84
    Unknown47: typing.Any = 85
    Unknown48: typing.Any = 86
    HighEndDuty: typing.Any = 87
    Unknown49: typing.Any = 88
    Unknown50: typing.Any = 89
    Unknown51: typing.Any = 90
    DutyRecorderAllowed: typing.Any = 91
    Unknown52: typing.Any = 92
    Unknown53: typing.Any = 93
    Unknown54: typing.Any = 94
    Unknown55: typing.Any = 95
    Unknown56: typing.Any = 96
    Unknown58: typing.Any = 97

class ContentFinderConditionTransientRow(ExdRow):
    _display_field: str = 'Description'

    Description: typing.Any = 0

class ContentGaugeRow(ExdRow):
    Name: typing.Any = 0
    TextString: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown2: typing.Any = 4
    Unknown3: typing.Any = 5
    Color: typing.Any = 6
    Unknown4: typing.Any = 7
    Unknown5: typing.Any = 8
    Unknown6: typing.Any = 9
    Unknown7: typing.Any = 10
    Unknown8: typing.Any = 11

class ContentGaugeColorRow(ExdRow):
    AndroidColor1: typing.Any = 0
    AndroidColor2: typing.Any = 1
    AndroidColor3: typing.Any = 2

class ContentMemberTypeRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown15: typing.Any = 6
    Unknown6: typing.Any = 7
    TanksPerParty: typing.Any = 8
    HealersPerParty: typing.Any = 9
    MeleesPerParty: typing.Any = 10
    RangedPerParty: typing.Any = 11
    Unknown16: typing.Any = 12
    Unknown7: typing.Any = 13
    Unknown8: typing.Any = 14
    Unknown9: typing.Any = 15
    Unknown10: typing.Any = 16
    Unknown11: typing.Any = 17
    Unknown12: typing.Any = 18
    Unknown13: typing.Any = 19
    Unknown14: typing.Any = 20

class ContentNpcRow(ExdRow):
    Unknown0: typing.Any = 0

class ContentNpcTalkRow(ExdRow):
    ContentTalk0: typing.Any = 0
    ContentTalk1: typing.Any = 1
    ContentTalk2: typing.Any = 2
    ContentTalk3: typing.Any = 3
    ContentTalk4: typing.Any = 4
    ContentTalk5: typing.Any = 5
    ContentTalk6: typing.Any = 6
    ContentTalk7: typing.Any = 7
    Type: typing.Any = 8

class ContentRandomSelectRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class ContentRewardConditionRow(ExdRow):
    Unknown0: typing.Any = 0

class ContentRouletteRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Category: typing.Any = 1
    Unknown0: typing.Any = 2
    Description: typing.Any = 3
    DutyType: typing.Any = 4
    Unknown1: typing.Any = 5
    Icon: typing.Any = 6
    Unknown2: typing.Any = 7
    Unknown3: typing.Any = 8
    ItemLevelRequired: typing.Any = 9
    Unknown4: typing.Any = 10
    RewardTomeA: typing.Any = 11
    RewardTomeB: typing.Any = 12
    RewardTomeC: typing.Any = 13
    Unknown5: typing.Any = 14
    InstanceContent: typing.Any = 15
    Unknown6: typing.Any = 16
    OpenRule: typing.Any = 17
    RequiredLevel: typing.Any = 18
    Unknown7: typing.Any = 19
    ContentRouletteRoleBonus: typing.Any = 20
    SortKey: typing.Any = 21
    Unknown8: typing.Any = 22
    ContentMemberType: typing.Any = 23
    Unknown9: typing.Any = 24
    Unknown10: typing.Any = 25
    Unknown11: typing.Any = 26
    Unknown12: typing.Any = 27
    Unknown13: typing.Any = 28
    Unknown14: typing.Any = 29
    ContentRouletteOpenRule: typing.Any = 30
    Unknown15: typing.Any = 31
    Unknown16: typing.Any = 32
    Unknown17: typing.Any = 33
    IsGoldSaucer: typing.Any = 34
    IsInDutyFinder: typing.Any = 35
    IsPvP: typing.Any = 36
    Unknown25: typing.Any = 37
    Unknown18: typing.Any = 38
    Unknown19: typing.Any = 39
    Unknown27: typing.Any = 40
    Unknown20: typing.Any = 41
    RequireAllDuties: typing.Any = 42
    Unknown21: typing.Any = 43
    Unknown22: typing.Any = 44
    Unknown23: typing.Any = 45
    Unknown24: typing.Any = 46
    Unknown26: typing.Any = 47

class ContentRouletteOpenRuleRow(ExdRow):
    Type: typing.Any = 0
    Unknown0: typing.Any = 1

class ContentRouletteRoleBonusRow(ExdRow):
    ItemRewardType: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2
    Unknown2: typing.Any = 3
    Unknown3: typing.Any = 4
    Unknown4: typing.Any = 5
    Unknown5: typing.Any = 6
    Unknown6: typing.Any = 7
    RewardAmount: typing.Any = 8
    Unknown7: typing.Any = 9
    Unknown8: typing.Any = 10
    Unknown9: typing.Any = 11

class ContentTalkRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0
    ContentTalkParam: typing.Any = 1

class ContentTalkParamRow(ExdRow):
    TestAction: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2
    Unknown2: typing.Any = 3
    Unknown3: typing.Any = 4
    Param: typing.Any = 5

class ContentTodoRow(ExdRow):
    Unknown0: typing.Any = 0
    Text: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class ContentTourismConstructRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13

class ContentTypeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Icon: typing.Any = 1
    IconDutyFinder: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown2: typing.Any = 4

class ContentUICategoryRow(ExdRow):
    Name: typing.Any = 0

class ContentsNoteRow(ExdRow):
    Name: typing.Any = 0
    Description: typing.Any = 1
    ReqUnlock: typing.Any = 2
    Icon: typing.Any = 3
    RequiredAmount: typing.Any = 4
    ExpMultiplier: typing.Any = 5
    GilRward: typing.Any = 6
    ExpCap: typing.Any = 7
    LevelUnlock: typing.Any = 8
    HowTo: typing.Any = 9
    ContentType: typing.Any = 10
    MenuOrder: typing.Any = 11
    Reward0: typing.Any = 12
    Reward1: typing.Any = 13

class ContentsNoteCategoryRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class ContentsNoteLevelRow(ExdRow):
    Unknown0: typing.Any = 0

class ContentsNoteRewardEurekaEXPRow(ExdRow):
    Unknown0: typing.Any = 0

class ContentsTutorialRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Unknown1: typing.Any = 2
    Page0: typing.Any = 3
    Page1: typing.Any = 4
    Page2: typing.Any = 5
    Page3: typing.Any = 6
    Page4: typing.Any = 7
    Page5: typing.Any = 8
    Page6: typing.Any = 9
    Page7: typing.Any = 10

class ContentsTutorialPageRow(ExdRow):
    Description: typing.Any = 0
    Image: typing.Any = 1

class CraftActionRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    QuestRequirement: typing.Any = 2
    CRP: typing.Any = 3
    BSM: typing.Any = 4
    ARM: typing.Any = 5
    GSM: typing.Any = 6
    LTW: typing.Any = 7
    WVR: typing.Any = 8
    ALC: typing.Any = 9
    CUL: typing.Any = 10
    AnimationStart: typing.Any = 11
    AnimationEnd: typing.Any = 12
    Icon: typing.Any = 13
    RequiredStatus: typing.Any = 14
    ClassJobCategory: typing.Any = 15
    ClassJobLevel: typing.Any = 16
    Cost: typing.Any = 17
    ClassJob: typing.Any = 18
    Specialist: typing.Any = 19

class CraftActionIndirectionRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class CraftLeveRow(ExdRow):
    _display_field: str = 'Leve'

    Leve: typing.Any = 0
    CraftLeveTalk: typing.Any = 1
    Item0: typing.Any = 2
    Item1: typing.Any = 3
    Item2: typing.Any = 4
    Item3: typing.Any = 5
    ItemCount0: typing.Any = 6
    ItemCount1: typing.Any = 7
    ItemCount2: typing.Any = 8
    ItemCount3: typing.Any = 9
    Repeats: typing.Any = 10

class CraftLeveTalkRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown24: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    Unknown27: typing.Any = 27
    Unknown28: typing.Any = 28
    Unknown29: typing.Any = 29
    Unknown30: typing.Any = 30
    Unknown31: typing.Any = 31
    Unknown32: typing.Any = 32
    Unknown33: typing.Any = 33
    Unknown34: typing.Any = 34
    Unknown35: typing.Any = 35
    Talk0: typing.Any = 36
    Talk1: typing.Any = 37
    Talk2: typing.Any = 38
    Talk3: typing.Any = 39
    Talk4: typing.Any = 40
    Talk5: typing.Any = 41

class CraftTypeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    MainPhysical: typing.Any = 1
    SubPhysical: typing.Any = 2

class CreditRow(ExdRow):
    Roles1: typing.Any = 0
    JapaneseCast1: typing.Any = 1
    EnglishCast1: typing.Any = 2
    FrenchCast1: typing.Any = 3
    GermanCast1: typing.Any = 4
    Roles2: typing.Any = 5
    JapaneseCast2: typing.Any = 6
    EnglishCast2: typing.Any = 7
    FrenchCast2: typing.Any = 8
    GermanCast2: typing.Any = 9
    Unknown0: typing.Any = 10

class CreditBackImageRow(ExdRow):
    BackImage: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2
    Unknown2: typing.Any = 3
    Unknown3: typing.Any = 4
    Unknown4: typing.Any = 5
    Unknown5: typing.Any = 6

class CreditCastRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class CreditDataSetRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown5: typing.Any = 3
    Unknown3: typing.Any = 4
    Unknown4: typing.Any = 5

class CreditFontRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8

class CreditListRow(ExdRow):
    Icon: typing.Any = 0
    Font: typing.Any = 1
    Cast: typing.Any = 2
    Scale: typing.Any = 3
    Unknown0: typing.Any = 4
    Unknown1: typing.Any = 5

class CreditListTextRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class CreditVersionRow(ExdRow):
    Unknown0: typing.Any = 0

class CurrencyScripConvertRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class CustomTalkRow(ExdRow):
    _display_field: str = 'Name'

    Script0: typing.Any = 0
    Script1: typing.Any = 1
    Script2: typing.Any = 2
    Script3: typing.Any = 3
    Script4: typing.Any = 4
    Script5: typing.Any = 5
    Script6: typing.Any = 6
    Script7: typing.Any = 7
    Script8: typing.Any = 8
    Script9: typing.Any = 9
    Script10: typing.Any = 10
    Script11: typing.Any = 11
    Script12: typing.Any = 12
    Script13: typing.Any = 13
    Script14: typing.Any = 14
    Script15: typing.Any = 15
    Script16: typing.Any = 16
    Script17: typing.Any = 17
    Script18: typing.Any = 18
    Script19: typing.Any = 19
    Script20: typing.Any = 20
    Script21: typing.Any = 21
    Script22: typing.Any = 22
    Script23: typing.Any = 23
    Script24: typing.Any = 24
    Script25: typing.Any = 25
    Script26: typing.Any = 26
    Script27: typing.Any = 27
    Script28: typing.Any = 28
    Script29: typing.Any = 29
    MainOption: typing.Any = 30
    SubOption: typing.Any = 31
    Name: typing.Any = 32
    IconActor: typing.Any = 33
    IconMap: typing.Any = 34
    SpecialLinks: typing.Any = 35
    Unknown0: typing.Any = 36
    Unknown1: typing.Any = 37
    Unknown2: typing.Any = 38
    Unknown3: typing.Any = 39
    Unknown4: typing.Any = 40
    Unknown5: typing.Any = 41
    Unknown6: typing.Any = 42
    Unknown7: typing.Any = 43
    Unknown8: typing.Any = 44
    Unknown9: typing.Any = 45
    Unknown10: typing.Any = 46
    Unknown11: typing.Any = 47
    Unknown12: typing.Any = 48

class CustomTalkDefineClientRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class CustomTalkNestHandlersRow(ExdRow):
    NestHandler: typing.Any = 0

class CustomTalkResidentRow(ExdRow):
    Unknown0: typing.Any = 0

class CutActionTimelineRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class CutSceneIncompQuestRow(ExdRow):
    _display_field: str = 'Quest'

    Quest: typing.Any = 0

class CutScreenImageRow(ExdRow):
    Image: typing.Any = 0
    Type: typing.Any = 1
    Unknown0: typing.Any = 2

class CutsceneRow(ExdRow):
    _display_field: str = 'Path'

    Path: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2
    Unknown2: typing.Any = 3
    Unknown3: typing.Any = 4
    Unknown4: typing.Any = 5
    Unknown5: typing.Any = 6
    Unknown6: typing.Any = 7
    Unknown7: typing.Any = 8
    Unknown8: typing.Any = 9

class CutsceneActorSizeRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class CutsceneEventMotionRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13

class CutsceneMotionRow(ExdRow):
    WALK_LOOP_SPEED: typing.Any = 0
    RUN_LOOP_SPEED: typing.Any = 1
    SLOWWALK_LOOP_SPEED: typing.Any = 2
    SLOWRUN_LOOP_SPEED: typing.Any = 3
    BATTLEWALK_LOOP_SPEED: typing.Any = 4
    BATTLERUN_LOOP_SPEED: typing.Any = 5
    DASH_LOOP_SPEED: typing.Any = 6
    TURN_CW90_FRAME: typing.Any = 7
    TURN_CCW90_FRAME: typing.Any = 8
    TURN_CW180_FRAME: typing.Any = 9
    TURN_CCW180_FRAME: typing.Any = 10

class CutsceneNameRow(ExdRow):
    Unknown0: typing.Any = 0

class CutsceneWorkIndexRow(ExdRow):
    WorkIndex: typing.Any = 0

class CuttingGrassRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6

class CycleTimeRow(ExdRow):
    FirstCycle: typing.Any = 0
    Cycle: typing.Any = 1

class DailySupplyItemRow(ExdRow):
    Item0: typing.Any = 0
    Item1: typing.Any = 1
    Item2: typing.Any = 2
    Item3: typing.Any = 3
    Item4: typing.Any = 4
    Item5: typing.Any = 5
    Item6: typing.Any = 6
    Item7: typing.Any = 7
    Quantity0: typing.Any = 8
    Quantity1: typing.Any = 9
    Quantity2: typing.Any = 10
    Quantity3: typing.Any = 11
    Quantity4: typing.Any = 12
    Quantity5: typing.Any = 13
    Quantity6: typing.Any = 14
    Quantity7: typing.Any = 15
    RecipeLevel0: typing.Any = 16
    RecipeLevel1: typing.Any = 17
    RecipeLevel2: typing.Any = 18
    RecipeLevel3: typing.Any = 19
    RecipeLevel4: typing.Any = 20
    RecipeLevel5: typing.Any = 21
    RecipeLevel6: typing.Any = 22
    RecipeLevel7: typing.Any = 23

class DawnContentRow(ExdRow):
    _display_field: str = 'Content'

    Content: typing.Any = 0
    ExpBelowExMaxLvl: typing.Any = 1
    ExpAboveExMaxLvl: typing.Any = 2
    Unknown0: typing.Any = 3
    Unknown1: typing.Any = 4
    Unknown2: typing.Any = 5
    Unknown3: typing.Any = 6
    Unknown4: typing.Any = 7
    Unknown5: typing.Any = 8
    Unknown6: typing.Any = 9
    Unknown7: typing.Any = 10
    Unknown8: typing.Any = 11
    Unknown9: typing.Any = 12
    Unknown10: typing.Any = 13
    Unknown15: typing.Any = 14
    Unknown11: typing.Any = 15
    Unknown12: typing.Any = 16
    Unknown16: typing.Any = 17
    Unknown13: typing.Any = 18
    Unknown14: typing.Any = 19

class DawnContentParticipableRow(ExdRow):
    Unknown0: typing.Any = 0

class DawnGrowMemberRow(ExdRow):
    _display_field: str = 'Class'

    SelectImage0: typing.Any = 0
    SelectImage1: typing.Any = 1
    SelectImage2: typing.Any = 2
    SelectImage3: typing.Any = 3
    PortraitImage0: typing.Any = 4
    PortraitImage1: typing.Any = 5
    PortraitImage2: typing.Any = 6
    PortraitImage3: typing.Any = 7
    Class: typing.Any = 8

class DawnMemberRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class DawnMemberUIParamRow(ExdRow):
    _display_field: str = 'ClassSingular'

    Unknown0: typing.Any = 0
    ClassPlural: typing.Any = 1
    VoiceLine: typing.Any = 2
    ClassSingular: typing.Any = 3

class DawnQuestMemberRow(ExdRow):
    _display_field: str = 'Member'

    Member: typing.Any = 0
    BigImageOld: typing.Any = 1
    BigImageNew: typing.Any = 2
    Unknown0: typing.Any = 3
    Unknown1: typing.Any = 4
    Class: typing.Any = 5

class DeepDungeonRow(ExdRow):
    _display_field: str = 'Name'

    PomanderSlot0: typing.Any = 0
    PomanderSlot1: typing.Any = 1
    PomanderSlot2: typing.Any = 2
    PomanderSlot3: typing.Any = 3
    PomanderSlot4: typing.Any = 4
    PomanderSlot5: typing.Any = 5
    PomanderSlot6: typing.Any = 6
    PomanderSlot7: typing.Any = 7
    PomanderSlot8: typing.Any = 8
    PomanderSlot9: typing.Any = 9
    PomanderSlot10: typing.Any = 10
    PomanderSlot11: typing.Any = 11
    PomanderSlot12: typing.Any = 12
    PomanderSlot13: typing.Any = 13
    PomanderSlot14: typing.Any = 14
    PomanderSlot15: typing.Any = 15
    Unknown2: typing.Any = 16
    Unknown3: typing.Any = 17
    Unknown4: typing.Any = 18
    Unknown5: typing.Any = 19
    Unknown6: typing.Any = 20
    Unknown7: typing.Any = 21
    Unknown8: typing.Any = 22
    Unknown9: typing.Any = 23
    Unknown10: typing.Any = 24
    Unknown11: typing.Any = 25
    Unknown12: typing.Any = 26
    Unknown13: typing.Any = 27
    MagiciteSlot0: typing.Any = 28
    MagiciteSlot1: typing.Any = 29
    MagiciteSlot2: typing.Any = 30
    MagiciteSlot3: typing.Any = 31
    Name: typing.Any = 32
    Unknown14: typing.Any = 33
    ContentFinderConditionStart: typing.Any = 34
    AetherpoolArm: typing.Any = 35
    AetherpoolArmor: typing.Any = 36
    DeepDungeonType: typing.Any = 37

class DeepDungeon4GimmickEffectRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class DeepDungeon4GimmickEffectTransientRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class DeepDungeonBanRow(ExdRow):
    _display_field: str = 'Name'

    ScreenImage: typing.Any = 0
    LogMessage: typing.Any = 1
    Name: typing.Any = 2

class DeepDungeonDangerRow(ExdRow):
    ScreenImage: typing.Any = 0
    LogMessage: typing.Any = 1
    Name: typing.Any = 2

class DeepDungeonDemicloneRow(ExdRow):
    _display_field: str = 'TitleCase'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    TitleCase: typing.Any = 2
    Description: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Icon: typing.Any = 10

class DeepDungeonEquipmentRow(ExdRow):
    _display_field: str = 'Name'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Name: typing.Any = 2
    Description: typing.Any = 3
    Adjective: typing.Any = 4
    PossessivePronoun: typing.Any = 5
    StartsWithVowel: typing.Any = 6
    Unknown0: typing.Any = 7
    Pronoun: typing.Any = 8
    Article: typing.Any = 9
    Icon: typing.Any = 10

class DeepDungeonFloorEffectUIRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Icon: typing.Any = 2

class DeepDungeonGrowDataRow(ExdRow):
    Unknown0: typing.Any = 0

class DeepDungeonHardModeItemRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class DeepDungeonItemRow(ExdRow):
    _display_field: str = 'Name'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Name: typing.Any = 2
    Tooltip: typing.Any = 3
    Adjective: typing.Any = 4
    PossessivePronoun: typing.Any = 5
    StartsWithVowel: typing.Any = 6
    Unknown0: typing.Any = 7
    Pronoun: typing.Any = 8
    Article: typing.Any = 9
    Icon: typing.Any = 10
    Action: typing.Any = 11

class DeepDungeonLayerRow(ExdRow):
    RoomA: typing.Any = 0
    RoomB: typing.Any = 1
    RoomC: typing.Any = 2
    DeepDungeon: typing.Any = 3
    FloorSet: typing.Any = 4
    WepMinLv: typing.Any = 5
    ArmourMinLv: typing.Any = 6
    Unknown0: typing.Any = 7

class DeepDungeonMagicStoneRow(ExdRow):
    _display_field: str = 'Name'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Name: typing.Any = 2
    Tooltip: typing.Any = 3
    Adjective: typing.Any = 4
    PossessivePronoun: typing.Any = 5
    StartsWithVowel: typing.Any = 6
    Unknown0: typing.Any = 7
    Pronoun: typing.Any = 8
    Article: typing.Any = 9
    Icon: typing.Any = 10

class DeepDungeonMap5XRow(ExdRow):
    DeepDungeonRoom0: typing.Any = 0
    DeepDungeonRoom1: typing.Any = 1
    DeepDungeonRoom2: typing.Any = 2
    DeepDungeonRoom3: typing.Any = 3
    DeepDungeonRoom4: typing.Any = 4

class DeepDungeonResidentRow(ExdRow):
    Unknown0: typing.Any = 0

class DeepDungeonRoomRow(ExdRow):
    Level0: typing.Any = 0
    Level1: typing.Any = 1
    Level2: typing.Any = 2
    Level3: typing.Any = 3
    Level4: typing.Any = 4

class DeepDungeonStatusRow(ExdRow):
    ScreenImage: typing.Any = 0
    LogMessage: typing.Any = 1
    Name: typing.Any = 2

class DefaultTalkRow(ExdRow):
    DefaultTalkParams0: typing.Any = 0
    DefaultTalkParams1: typing.Any = 1
    DefaultTalkParams2: typing.Any = 2
    Text0: typing.Any = 3
    Text1: typing.Any = 4
    Text2: typing.Any = 5
    Unknown0: typing.Any = 6
    Unknown1: typing.Any = 7

class DefaultTalkLipSyncTypeRow(ExdRow):
    _display_field: str = 'ActionTimeline'

    ActionTimeline: typing.Any = 0

class DeliveryQuestRow(ExdRow):
    _display_field: str = 'Quest'

    Quest: typing.Any = 0

class DescriptionRow(ExdRow):
    _display_field: str = 'TextLong'

    TextLong: typing.Any = 0
    TextShort: typing.Any = 1
    TextCommentary: typing.Any = 2
    Quest: typing.Any = 3
    Section: typing.Any = 4
    Unknown0: typing.Any = 5
    Unknown1: typing.Any = 6

class DescriptionPageRow(ExdRow):
    Quest: typing.Any = 0
    Unknown2: typing.Any = 1
    Image0: typing.Any = 2
    Image1: typing.Any = 3
    Image2: typing.Any = 4
    Image3: typing.Any = 5
    Image4: typing.Any = 6
    Image5: typing.Any = 7
    Image6: typing.Any = 8
    Image7: typing.Any = 9
    Image8: typing.Any = 10
    Image9: typing.Any = 11
    Image10: typing.Any = 12
    Text0: typing.Any = 13
    Text1: typing.Any = 14
    Text2: typing.Any = 15
    Text3: typing.Any = 16
    Text4: typing.Any = 17
    Text5: typing.Any = 18
    Text6: typing.Any = 19
    Text7: typing.Any = 20
    Text8: typing.Any = 21
    Text9: typing.Any = 22
    Text10: typing.Any = 23
    Unknown0: typing.Any = 24
    Unknown1: typing.Any = 25

class DescriptionSectionRow(ExdRow):
    _display_field: str = 'String'

    String: typing.Any = 0
    Page: typing.Any = 1

class DescriptionStandAloneRow(ExdRow):
    Unknown0: typing.Any = 0

class DescriptionStandAloneTransientRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class DescriptionStringRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0

class DirectorSystemDefineRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class DirectorTypeRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class DisposalShopRow(ExdRow):
    _display_field: str = 'ShopName'

    ShopName: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2
    Unknown2: typing.Any = 3
    Unknown3: typing.Any = 4
    Unknown4: typing.Any = 5
    Unknown5: typing.Any = 6
    Unknown6: typing.Any = 7
    Unknown7: typing.Any = 8
    Unknown8: typing.Any = 9
    Unknown9: typing.Any = 10
    Unknown10: typing.Any = 11
    Unknown11: typing.Any = 12
    Unknown12: typing.Any = 13
    Unknown13: typing.Any = 14
    Unknown14: typing.Any = 15
    Unknown15: typing.Any = 16
    Unknown16: typing.Any = 17

class DisposalShopFilterTypeRow(ExdRow):
    _display_field: str = 'Category'

    Category: typing.Any = 0

class DisposalShopItemRow(ExdRow):
    _display_field: str = 'ItemDisposed'

    QuantityReceived: typing.Any = 0
    ItemDisposed: typing.Any = 1
    ItemReceived: typing.Any = 2
    Unknown0: typing.Any = 3
    Unknown1: typing.Any = 4
    Unknown2: typing.Any = 5

class DomaStoryProgressRow(ExdRow):
    Unknown0: typing.Any = 0

class DpsChallengeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Icon: typing.Any = 2
    PlayerLevel: typing.Any = 3
    Unknown0: typing.Any = 4
    PlaceName: typing.Any = 5
    Order: typing.Any = 6
    Unknown1: typing.Any = 7

class DpsChallengeOfficerRow(ExdRow):
    ChallengeName0: typing.Any = 0
    ChallengeName1: typing.Any = 1
    ChallengeName2: typing.Any = 2
    ChallengeName3: typing.Any = 3
    ChallengeName4: typing.Any = 4
    ChallengeName5: typing.Any = 5
    ChallengeName6: typing.Any = 6
    ChallengeName7: typing.Any = 7
    ChallengeName8: typing.Any = 8
    ChallengeName9: typing.Any = 9
    ChallengeName10: typing.Any = 10
    ChallengeName11: typing.Any = 11
    ChallengeName12: typing.Any = 12
    ChallengeName13: typing.Any = 13
    ChallengeName14: typing.Any = 14
    ChallengeName15: typing.Any = 15
    ChallengeName16: typing.Any = 16
    ChallengeName17: typing.Any = 17
    ChallengeName18: typing.Any = 18
    ChallengeName19: typing.Any = 19
    ChallengeName20: typing.Any = 20
    ChallengeName21: typing.Any = 21
    ChallengeName22: typing.Any = 22
    ChallengeName23: typing.Any = 23
    ChallengeName24: typing.Any = 24
    UnlockQuest: typing.Any = 25

class DpsChallengeTransientRow(ExdRow):
    InstanceContent: typing.Any = 0

class DynamicEventRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    LGBEventObject: typing.Any = 2
    LGBMapRange: typing.Any = 3
    Quest: typing.Any = 4
    Announce: typing.Any = 5
    Unknown0: typing.Any = 6
    Unknown1: typing.Any = 7
    Unknown6: typing.Any = 8
    Unknown7: typing.Any = 9
    Unknown2: typing.Any = 10
    EventType: typing.Any = 11
    EnemyType: typing.Any = 12
    MaxParticipants: typing.Any = 13
    Unknown4: typing.Any = 14
    Unknown5: typing.Any = 15
    SingleBattle: typing.Any = 16
    Unknown8: typing.Any = 17

class DynamicEventEnemyTypeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class DynamicEventManagerRow(ExdRow):
    Unknown1: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown2: typing.Any = 2

class DynamicEventSetRow(ExdRow):
    Unknown0: typing.Any = 0

class DynamicEventSingleBattleRow(ExdRow):
    Text: typing.Any = 0
    Icon: typing.Any = 1
    BNpcName: typing.Any = 2

class DynamicEventTypeRow(ExdRow):
    IconObjective0: typing.Any = 0
    IconObjective1: typing.Any = 1

class DynamicEventUITypeRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18

class ENpcBaseRow(ExdRow):
    ENpcData0: typing.Any = 0
    ENpcData1: typing.Any = 1
    ENpcData2: typing.Any = 2
    ENpcData3: typing.Any = 3
    ENpcData4: typing.Any = 4
    ENpcData5: typing.Any = 5
    ENpcData6: typing.Any = 6
    ENpcData7: typing.Any = 7
    ENpcData8: typing.Any = 8
    ENpcData9: typing.Any = 9
    ENpcData10: typing.Any = 10
    ENpcData11: typing.Any = 11
    ENpcData12: typing.Any = 12
    ENpcData13: typing.Any = 13
    ENpcData14: typing.Any = 14
    ENpcData15: typing.Any = 15
    ENpcData16: typing.Any = 16
    ENpcData17: typing.Any = 17
    ENpcData18: typing.Any = 18
    ENpcData19: typing.Any = 19
    ENpcData20: typing.Any = 20
    ENpcData21: typing.Any = 21
    ENpcData22: typing.Any = 22
    ENpcData23: typing.Any = 23
    ENpcData24: typing.Any = 24
    ENpcData25: typing.Any = 25
    ENpcData26: typing.Any = 26
    ENpcData27: typing.Any = 27
    ENpcData28: typing.Any = 28
    ENpcData29: typing.Any = 29
    ENpcData30: typing.Any = 30
    ENpcData31: typing.Any = 31
    ModelMainHand: typing.Any = 32
    ModelOffHand: typing.Any = 33
    Scale: typing.Any = 34
    ModelHead: typing.Any = 35
    ModelBody: typing.Any = 36
    ModelHands: typing.Any = 37
    ModelLegs: typing.Any = 38
    ModelFeet: typing.Any = 39
    ModelEars: typing.Any = 40
    ModelNeck: typing.Any = 41
    ModelWrists: typing.Any = 42
    ModelLeftRing: typing.Any = 43
    ModelRightRing: typing.Any = 44
    EventHandler: typing.Any = 45
    ModelChara: typing.Any = 46
    NpcEquip: typing.Any = 47
    Behavior: typing.Any = 48
    Unknown_70_1: typing.Any = 49
    Unknown_70_2: typing.Any = 50
    Balloon: typing.Any = 51
    Race: typing.Any = 52
    Gender: typing.Any = 53
    BodyType: typing.Any = 54
    Height: typing.Any = 55
    Tribe: typing.Any = 56
    Face: typing.Any = 57
    HairStyle: typing.Any = 58
    HairHighlight: typing.Any = 59
    SkinColor: typing.Any = 60
    EyeHeterochromia: typing.Any = 61
    HairColor: typing.Any = 62
    HairHighlightColor: typing.Any = 63
    FacialFeature: typing.Any = 64
    FacialFeatureColor: typing.Any = 65
    Eyebrows: typing.Any = 66
    EyeColor: typing.Any = 67
    EyeShape: typing.Any = 68
    Nose: typing.Any = 69
    Jaw: typing.Any = 70
    Mouth: typing.Any = 71
    LipColor: typing.Any = 72
    BustOrTone1: typing.Any = 73
    ExtraFeature1: typing.Any = 74
    ExtraFeature2OrBust: typing.Any = 75
    FacePaint: typing.Any = 76
    FacePaintColor: typing.Any = 77
    Unknown0: typing.Any = 78
    DyeMainHand: typing.Any = 79
    Dye2MainHand: typing.Any = 80
    DyeOffHand: typing.Any = 81
    Dye2OffHand: typing.Any = 82
    DyeHead: typing.Any = 83
    DyeBody: typing.Any = 84
    DyeHands: typing.Any = 85
    DyeLegs: typing.Any = 86
    DyeFeet: typing.Any = 87
    DyeEars: typing.Any = 88
    DyeNeck: typing.Any = 89
    DyeWrists: typing.Any = 90
    DyeLeftRing: typing.Any = 91
    DyeRightRing: typing.Any = 92
    Dye2Head: typing.Any = 93
    Dye2Body: typing.Any = 94
    Dye2Hands: typing.Any = 95
    Dye2Legs: typing.Any = 96
    Dye2Feet: typing.Any = 97
    Dye2Ears: typing.Any = 98
    Dye2Neck: typing.Any = 99
    Dye2Wrists: typing.Any = 100
    Dye2LeftRing: typing.Any = 101
    Dye2RightRing: typing.Any = 102
    Invisibility: typing.Any = 103
    DefaultBalloon: typing.Any = 104
    Unknown1: typing.Any = 105
    Important: typing.Any = 106
    Visor: typing.Any = 107
    NotRewriteHeight: typing.Any = 108
    Unknown2: typing.Any = 109

class ENpcDressUpRow(ExdRow):
    Unknown0: typing.Any = 0
    ENpcDressUpDress: typing.Any = 1

class ENpcDressUpDressRow(ExdRow):
    ModelMainHand: typing.Any = 0
    ModelOffHand: typing.Any = 1
    Unknown0: typing.Any = 2
    ENpc: typing.Any = 3
    ModelHead: typing.Any = 4
    ModelBody: typing.Any = 5
    ModelHands: typing.Any = 6
    ModelLegs: typing.Any = 7
    ModelFeet: typing.Any = 8
    Unknown1: typing.Any = 9
    Unknown2: typing.Any = 10
    Unknown3: typing.Any = 11
    Unknown4: typing.Any = 12
    Unknown5: typing.Any = 13
    Unknown6: typing.Any = 14
    Behavior: typing.Any = 15
    Unknown7: typing.Any = 16
    Unknown8: typing.Any = 17
    Unknown9: typing.Any = 18
    Unknown10: typing.Any = 19
    Unknown11: typing.Any = 20
    Unknown12: typing.Any = 21
    Unknown13: typing.Any = 22
    Unknown14: typing.Any = 23
    Unknown15: typing.Any = 24
    Unknown16: typing.Any = 25
    Unknown17: typing.Any = 26
    Unknown18: typing.Any = 27
    Unknown19: typing.Any = 28
    Unknown20: typing.Any = 29
    Unknown21: typing.Any = 30
    Unknown22: typing.Any = 31
    Unknown23: typing.Any = 32
    Unknown24: typing.Any = 33
    Unknown25: typing.Any = 34
    Unknown26: typing.Any = 35
    Unknown27: typing.Any = 36
    Unknown28: typing.Any = 37
    Unknown29: typing.Any = 38
    Unknown30: typing.Any = 39
    Unknown31: typing.Any = 40
    Unknown32: typing.Any = 41
    Unknown33: typing.Any = 42
    Unknown34: typing.Any = 43
    DyeMainHand: typing.Any = 44
    Dye2MainHand: typing.Any = 45
    DyeOffHand: typing.Any = 46
    Dye2OffHand: typing.Any = 47
    DyeHead: typing.Any = 48
    DyeBody: typing.Any = 49
    DyeHands: typing.Any = 50
    DyeLegs: typing.Any = 51
    DyeFeet: typing.Any = 52
    DyeEars: typing.Any = 53
    DyeNeck: typing.Any = 54
    DyeWrists: typing.Any = 55
    DyeLeftRing: typing.Any = 56
    DyeRightRing: typing.Any = 57
    Dye2Head: typing.Any = 58
    Dye2Body: typing.Any = 59
    Dye2Hands: typing.Any = 60
    Dye2Legs: typing.Any = 61
    Dye2Feet: typing.Any = 62
    Dye2Ears: typing.Any = 63
    Dye2Neck: typing.Any = 64
    Dye2Wrists: typing.Any = 65
    Dye2LeftRing: typing.Any = 66
    Dye2RightRing: typing.Any = 67
    Unknown40: typing.Any = 68
    Unknown41: typing.Any = 69
    Unknown42: typing.Any = 70
    Unknown43: typing.Any = 71
    Unknown44: typing.Any = 72

class ENpcResidentRow(ExdRow):
    _display_field: str = 'Singular'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Title: typing.Any = 2
    Adjective: typing.Any = 3
    PossessivePronoun: typing.Any = 4
    StartsWithVowel: typing.Any = 5
    Unknown0: typing.Any = 6
    Pronoun: typing.Any = 7
    Article: typing.Any = 8
    Map: typing.Any = 9
    Unknown1: typing.Any = 10

class EObjRow(ExdRow):
    Data: typing.Any = 0
    SgbPath: typing.Any = 1
    PopType: typing.Any = 2
    Invisibility: typing.Any = 3
    EventHighAddition: typing.Any = 4
    Unknown0: typing.Any = 5
    Unknown1: typing.Any = 6
    Unknown2: typing.Any = 7
    Unknown3: typing.Any = 8
    Unknown4: typing.Any = 9
    Unknown5: typing.Any = 10
    Unknown6: typing.Any = 11
    Unknown7: typing.Any = 12
    Unknown8: typing.Any = 13
    EyeCollision: typing.Any = 14
    DirectorControl: typing.Any = 15
    Target: typing.Any = 16
    Unknown9: typing.Any = 17
    AddedIn53: typing.Any = 18
    Unknown10: typing.Any = 19

class EObjNameRow(ExdRow):
    _display_field: str = 'Singular'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Adjective: typing.Any = 2
    PossessivePronoun: typing.Any = 3
    StartsWithVowel: typing.Any = 4
    Unknown0: typing.Any = 5
    Pronoun: typing.Any = 6
    Article: typing.Any = 7

class EmjAddonRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0

class EmjCharaViewCameraRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class EmjCostumeRow(ExdRow):
    Unknown2: typing.Any = 0
    Unknown3: typing.Any = 1
    Unknown4: typing.Any = 2
    Unknown0: typing.Any = 3
    Unknown1: typing.Any = 4
    Data: typing.Any = 5
    Unknown5: typing.Any = 6

class EmjCostumeDataRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class EmjDaniRow(ExdRow):
    Icon: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2
    Unknown2: typing.Any = 3
    Unknown3: typing.Any = 4
    Unknown4: typing.Any = 5
    Unknown5: typing.Any = 6
    Unknown6: typing.Any = 7
    Unknown7: typing.Any = 8
    Unknown8: typing.Any = 9
    Unknown9: typing.Any = 10
    Unknown10: typing.Any = 11

class EmjVoiceNpcRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown28: typing.Any = 24
    Unknown24: typing.Any = 25
    Unknown25: typing.Any = 26
    Unknown26: typing.Any = 27
    Unknown27: typing.Any = 28

class EmoteRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    UnlockLink: typing.Any = 1
    TextCommand: typing.Any = 2
    ActionTimeline0: typing.Any = 3
    ActionTimeline1: typing.Any = 4
    ActionTimeline2: typing.Any = 5
    ActionTimeline3: typing.Any = 6
    ActionTimeline4: typing.Any = 7
    ActionTimeline5: typing.Any = 8
    ActionTimeline6: typing.Any = 9
    Order: typing.Any = 10
    Icon: typing.Any = 11
    LogMessageTargeted: typing.Any = 12
    LogMessageUntargeted: typing.Any = 13
    Unknown0: typing.Any = 14
    EmoteCategory: typing.Any = 15
    EmoteMode: typing.Any = 16
    Unknown1: typing.Any = 17
    Unknown2: typing.Any = 18
    Unknown3: typing.Any = 19
    Unknown4: typing.Any = 20
    Unknown5: typing.Any = 21
    HasCancelEmote: typing.Any = 22
    DrawsWeapon: typing.Any = 23
    Unknown6: typing.Any = 24

class EmoteCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class EmoteModeRow(ExdRow):
    _display_field: str = 'StartEmote'

    StartEmote: typing.Any = 0
    EndEmote: typing.Any = 1
    ConditionMode: typing.Any = 2
    Move: typing.Any = 3
    Camera: typing.Any = 4
    EndOnRotate: typing.Any = 5
    EndOnEmote: typing.Any = 6
    Unknown0: typing.Any = 7

class EmoteTransientRow(ExdRow):
    Unknown0: typing.Any = 0

class EquipRaceCategoryRow(ExdRow):
    Hyur: typing.Any = 0
    Elezen: typing.Any = 1
    Lalafell: typing.Any = 2
    Miqote: typing.Any = 3
    Roegadyn: typing.Any = 4
    AuRa: typing.Any = 5
    Hrothgar: typing.Any = 6
    Viera: typing.Any = 7
    Male: typing.Any = 8
    Female: typing.Any = 9

class EquipSlotCategoryRow(ExdRow):
    MainHand: typing.Any = 0
    OffHand: typing.Any = 1
    Head: typing.Any = 2
    Body: typing.Any = 3
    Gloves: typing.Any = 4
    Waist: typing.Any = 5
    Legs: typing.Any = 6
    Feet: typing.Any = 7
    Ears: typing.Any = 8
    Neck: typing.Any = 9
    Wrists: typing.Any = 10
    FingerL: typing.Any = 11
    FingerR: typing.Any = 12
    SoulCrystal: typing.Any = 13

class ErrorRow(ExdRow):
    Unknown0: typing.Any = 0

class EurekaRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class EurekaAetherItemRow(ExdRow):
    _display_field: str = 'Singular'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Name: typing.Any = 2
    Adjective: typing.Any = 3
    PossessivePronoun: typing.Any = 4
    StartsWithVowel: typing.Any = 5
    Unknown0: typing.Any = 6
    Pronoun: typing.Any = 7
    Article: typing.Any = 8

class EurekaAethernetRow(ExdRow):
    _display_field: str = 'Location'

    Location: typing.Any = 0

class EurekaDungeonPortalRow(ExdRow):
    Unknown0: typing.Any = 0

class EurekaGrowDataRow(ExdRow):
    _display_field: str = 'BaseResistance'

    BaseResistance: typing.Any = 0

class EurekaLogosMixerProbabilityRow(ExdRow):
    ProbabilityPercent: typing.Any = 0

class EurekaMagiaActionRow(ExdRow):
    Action: typing.Any = 0
    MaxUses: typing.Any = 1

class EurekaMagiciteItemRow(ExdRow):
    Item: typing.Any = 0
    EurekaMagiciteItemType: typing.Any = 1
    ClassJobCategory: typing.Any = 2

class EurekaMagiciteItemTypeRow(ExdRow):
    _display_field: str = 'Type'

    Type: typing.Any = 0

class EurekaSphereElementAdjustRow(ExdRow):
    _display_field: str = 'PowerModifier'

    PowerModifier: typing.Any = 0

class EurekaStoryProgressRow(ExdRow):
    Unknown0: typing.Any = 0

class EventActionRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Icon: typing.Any = 1
    StartAnimation: typing.Any = 2
    LoopAnimation: typing.Any = 3
    EndAnimation: typing.Any = 4
    CastTime: typing.Any = 5

class EventCustomIconTypeRow(ExdRow):
    Icons0: typing.Any = 0
    Icons1: typing.Any = 1
    Icons2: typing.Any = 2
    Icons3: typing.Any = 3
    Icons4: typing.Any = 4
    Icons5: typing.Any = 5
    Icons6: typing.Any = 6
    Icons7: typing.Any = 7
    Icons8: typing.Any = 8
    Icons9: typing.Any = 9
    Unknown0: typing.Any = 10

class EventExtraConditionSetRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class EventGimmickPathMoveRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class EventIconPriorityRow(ExdRow):
    Icon0: typing.Any = 0
    Icon1: typing.Any = 1
    Icon2: typing.Any = 2
    Icon3: typing.Any = 3
    Icon4: typing.Any = 4
    Icon5: typing.Any = 5
    Icon6: typing.Any = 6
    Icon7: typing.Any = 7
    Icon8: typing.Any = 8
    Icon9: typing.Any = 9
    Icon10: typing.Any = 10
    Icon11: typing.Any = 11
    Icon12: typing.Any = 12
    Icon13: typing.Any = 13
    Icon14: typing.Any = 14
    Icon15: typing.Any = 15
    Icon16: typing.Any = 16
    Icon17: typing.Any = 17
    Icon18: typing.Any = 18
    Icon19: typing.Any = 19
    Icon20: typing.Any = 20
    Icon21: typing.Any = 21
    Icon22: typing.Any = 22
    Icon23: typing.Any = 23
    Icon24: typing.Any = 24
    Icon25: typing.Any = 25
    Icon26: typing.Any = 26
    Icon27: typing.Any = 27
    Icon28: typing.Any = 28

class EventIconPriorityPairRow(ExdRow):
    Icon: typing.Any = 0

class EventIconTypeRow(ExdRow):
    NpcIconAvailable: typing.Any = 0
    MapIconAvailable: typing.Any = 1
    NpcIconInvalid: typing.Any = 2
    MapIconInvalid: typing.Any = 3
    IconRange: typing.Any = 4

class EventItemRow(ExdRow):
    _display_field: str = 'Singular'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Name: typing.Any = 2
    Adjective: typing.Any = 3
    PossessivePronoun: typing.Any = 4
    StartsWithVowel: typing.Any = 5
    Unknown0: typing.Any = 6
    Pronoun: typing.Any = 7
    Article: typing.Any = 8
    Unknown1: typing.Any = 9
    Quest: typing.Any = 10
    Icon: typing.Any = 11
    Action: typing.Any = 12
    StackSize: typing.Any = 13
    Category: typing.Any = 14
    CastTime: typing.Any = 15
    CastTimeline: typing.Any = 16
    Timeline: typing.Any = 17

class EventItemCastTimelineRow(ExdRow):
    _display_field: str = 'ActionTimeline'

    ActionTimeline: typing.Any = 0

class EventItemCategoryRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class EventItemHelpRow(ExdRow):
    _display_field: str = 'Description'

    Description: typing.Any = 0
    Unknown0: typing.Any = 1

class EventItemTimelineRow(ExdRow):
    _display_field: str = 'ActionTimeline'

    ActionTimeline: typing.Any = 0

class EventMountGimmickPathMoveRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown3: typing.Any = 2
    Unknown2: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8

class EventPathMoveRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11

class EventSituationIconTooltipRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class EventSystemDefineRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0
    DefineValue: typing.Any = 1

class EventTutorialRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10

class EventTutorialPageRow(ExdRow):
    Name: typing.Any = 0
    Text: typing.Any = 1
    Unknown2: typing.Any = 2

class EventVfxRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class ExHotbarCrossbarIndexTypeRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15

class ExVersionRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    MenuScreen: typing.Any = 1
    Unknown0: typing.Any = 2
    AcceptJingle: typing.Any = 3
    CompleteJingle: typing.Any = 4

class ExportedGatheringPointRow(ExdRow):
    X: typing.Any = 0
    Y: typing.Any = 1
    Radius: typing.Any = 2
    GatheringType: typing.Any = 3
    GatheringPointType: typing.Any = 4

class ExportedSGRow(ExdRow):
    _display_field: str = 'SgbPath'

    SgbPath: typing.Any = 0

class ExtraCommandRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Icon: typing.Any = 2
    Order: typing.Any = 3

class FCActivityRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0
    SelfKind: typing.Any = 1
    TargetKind: typing.Any = 2
    NumParam: typing.Any = 3
    FCActivityCategory: typing.Any = 4
    IconType: typing.Any = 5

class FCActivityCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Priority: typing.Any = 1

class FCAuthorityRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    FCAuthorityCategory: typing.Any = 1
    Unknown0: typing.Any = 2

class FCAuthorityCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class FCChestNameRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Unknown0: typing.Any = 1

class FCCrestSymbolRow(ExdRow):
    Unknown0: typing.Any = 0
    ColorNum: typing.Any = 1
    FCRight: typing.Any = 2

class FCDefineRow(ExdRow):
    Unknown0: typing.Any = 0

class FCHierarchyRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class FCProfileRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Priority: typing.Any = 1

class FCRankRow(ExdRow):
    NextPoint: typing.Any = 0
    CurrentPoint: typing.Any = 1
    Rights: typing.Any = 2
    Unknown0: typing.Any = 3
    Unknown1: typing.Any = 4
    FCActionActiveNum: typing.Any = 5
    FCActionStockNum: typing.Any = 6
    FCChestCompartments: typing.Any = 7

class FCReputationRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    PointsToNext: typing.Any = 1
    RequiredPoints: typing.Any = 2
    Color: typing.Any = 3
    DiscountRate: typing.Any = 4

class FCRightsRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Icon: typing.Any = 2
    FCRank: typing.Any = 3

class FGSAddonRow(ExdRow):
    Unknown0: typing.Any = 0

class FGSStageUIRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7

class FashionCheckThemeCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class FashionCheckWeeklyThemeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class FateRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Objective: typing.Any = 2
    StatusText0: typing.Any = 3
    StatusText1: typing.Any = 4
    StatusText2: typing.Any = 5
    Unknown0: typing.Any = 6
    Unknown1: typing.Any = 7
    ReqEventItem: typing.Any = 8
    TurnInEventItem: typing.Any = 9
    Unknown20: typing.Any = 10
    Unknown21: typing.Any = 11
    Unknown22: typing.Any = 12
    Unknown10: typing.Any = 13
    Unknown11: typing.Any = 14
    Unknown12: typing.Any = 15
    ObjectiveIcon0: typing.Any = 16
    ObjectiveIcon1: typing.Any = 17
    ObjectiveIcon2: typing.Any = 18
    ObjectiveIcon3: typing.Any = 19
    ObjectiveIcon4: typing.Any = 20
    ObjectiveIcon5: typing.Any = 21
    ObjectiveIcon6: typing.Any = 22
    ObjectiveIcon7: typing.Any = 23
    ObjectiveIcon8: typing.Any = 24
    ObjectiveIcon9: typing.Any = 25
    ObjectiveIcon10: typing.Any = 26
    ObjectiveIcon11: typing.Any = 27
    ObjectiveIcon12: typing.Any = 28
    ObjectiveIcon13: typing.Any = 29
    ObjectiveIcon14: typing.Any = 30
    ObjectiveIcon15: typing.Any = 31
    ObjectiveIcon16: typing.Any = 32
    ObjectiveIcon17: typing.Any = 33
    ObjectiveIcon18: typing.Any = 34
    ObjectiveIcon19: typing.Any = 35
    ObjectiveIcon20: typing.Any = 36
    ObjectiveIcon21: typing.Any = 37
    ObjectiveIcon22: typing.Any = 38
    ObjectiveIcon23: typing.Any = 39
    ObjectiveIcon24: typing.Any = 40
    ObjectiveIcon25: typing.Any = 41
    ObjectiveIcon26: typing.Any = 42
    ObjectiveIcon27: typing.Any = 43
    ObjectiveIcon28: typing.Any = 44
    ObjectiveIcon29: typing.Any = 45
    ObjectiveIcon30: typing.Any = 46
    ObjectiveIcon31: typing.Any = 47
    Location: typing.Any = 48
    EventItem: typing.Any = 49
    Icon: typing.Any = 50
    MapIcon: typing.Any = 51
    InactiveMapIcon: typing.Any = 52
    LGBGuardNPCLocation: typing.Any = 53
    RequiredQuest: typing.Any = 54
    FATEChain: typing.Any = 55
    Unknown13: typing.Any = 56
    FateRuleEx: typing.Any = 57
    Music: typing.Any = 58
    ScreenImageAccept: typing.Any = 59
    ScreenImageComplete: typing.Any = 60
    ScreenImageFailed: typing.Any = 61
    GivenStatus: typing.Any = 62
    Unknown4: typing.Any = 63
    Unknown5: typing.Any = 64
    EurekaFate: typing.Any = 65
    Rule: typing.Any = 66
    ClassJobLevel: typing.Any = 67
    ClassJobLevelMax: typing.Any = 68
    StatusValue0: typing.Any = 69
    StatusValue1: typing.Any = 70
    StatusValue2: typing.Any = 71
    Unknown6: typing.Any = 72
    Unknown7: typing.Any = 73
    SpecialFate: typing.Any = 74
    Unknown8: typing.Any = 75
    AdventEvent: typing.Any = 76
    MoonFaireEvent: typing.Any = 77
    Unknown9: typing.Any = 78

class FateEventRow(ExdRow):
    EventParameters0: typing.Any = 0
    EventParameters1: typing.Any = 1
    EventParameters2: typing.Any = 2
    EventParameters3: typing.Any = 3
    EventParameters4: typing.Any = 4
    EventParameters5: typing.Any = 5
    EventParameters6: typing.Any = 6
    EventParameters7: typing.Any = 7
    Text0: typing.Any = 8
    Text1: typing.Any = 9
    Text2: typing.Any = 10
    Text3: typing.Any = 11
    Text4: typing.Any = 12
    Text5: typing.Any = 13
    Text6: typing.Any = 14
    Text7: typing.Any = 15

class FateModeRow(ExdRow):
    Unknown0: typing.Any = 0
    MotivationIcon: typing.Any = 1
    MotivationMapMarker: typing.Any = 2
    ObjectiveIcon: typing.Any = 3
    ObjectiveMapMarker: typing.Any = 4

class FateProgressUIRow(ExdRow):
    _display_field: str = 'Location'

    Location: typing.Any = 0
    ReqFatesToRank2: typing.Any = 1
    ReqFatesToRank3: typing.Any = 2
    ReqFatesToRank4: typing.Any = 3
    DisplayOrder: typing.Any = 4
    Unknown0: typing.Any = 5

class FateRuleExRow(ExdRow):
    Unknown0: typing.Any = 0

class FateShopRow(ExdRow):
    SpecialShop0: typing.Any = 0
    SpecialShop1: typing.Any = 1
    SpecialShop2: typing.Any = 2
    DefaultTalk0: typing.Any = 3
    DefaultTalk1: typing.Any = 4
    DefaultTalk2: typing.Any = 5
    DefaultTalk3: typing.Any = 6
    DefaultTalk4: typing.Any = 7
    DefaultTalk5: typing.Any = 8
    DefaultTalk6: typing.Any = 9
    DefaultTalk7: typing.Any = 10
    DefaultTalk8: typing.Any = 11

class FateTokenTypeRow(ExdRow):
    _display_field: str = 'Currency'

    Currency: typing.Any = 0

class FccShopRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    ItemData0: typing.Any = 1
    ItemData1: typing.Any = 2
    ItemData2: typing.Any = 3
    ItemData3: typing.Any = 4
    ItemData4: typing.Any = 5
    ItemData5: typing.Any = 6
    ItemData6: typing.Any = 7
    ItemData7: typing.Any = 8
    ItemData8: typing.Any = 9
    ItemData9: typing.Any = 10

class FestivalRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown0: typing.Any = 2

class FieldMarkerRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    VFX: typing.Any = 1
    UiIcon: typing.Any = 2
    MapIcon: typing.Any = 3

class FishParameterRow(ExdRow):
    _display_field: str = 'Item'

    Text: typing.Any = 0
    Unknown_70_1: typing.Any = 1
    Unknown_70_2: typing.Any = 2
    Unknown_70_3: typing.Any = 3
    AchievementCredit: typing.Any = 4
    Item: typing.Any = 5
    GatheringItemLevel: typing.Any = 6
    Unknown1: typing.Any = 7
    FishingSpot: typing.Any = 8
    GatheringSubCategory: typing.Any = 9
    OceanStars: typing.Any = 10
    FishingRecordType: typing.Any = 11
    IsHidden: typing.Any = 12
    IsInLog: typing.Any = 13

class FishParameterReverseRow(ExdRow):
    Unknown0: typing.Any = 0

class FishingBaitParameterRow(ExdRow):
    Unknown0: typing.Any = 0

class FishingNoteInfoRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0
    Size: typing.Any = 1
    AquariumWater: typing.Any = 2
    WeatherRestriction: typing.Any = 3
    TimeRestriction: typing.Any = 4
    SpecialConditions: typing.Any = 5
    IsCollectable: typing.Any = 6

class FishingRecordTypeRow(ExdRow):
    _display_field: str = 'Addon'

    Addon: typing.Any = 0
    RankBRequirement: typing.Any = 1
    RankARequirement: typing.Any = 2
    RankAARequirement: typing.Any = 3
    RankAAARequirement: typing.Any = 4
    RankSRequirement: typing.Any = 5
    IsSpearfishing: typing.Any = 6

class FishingRecordTypeTransientRow(ExdRow):
    _display_field: str = 'Image'

    Image: typing.Any = 0

class FishingSpotRow(ExdRow):
    _display_field: str = 'PlaceName'

    BigFishOnReach: typing.Any = 0
    BigFishOnEnd: typing.Any = 1
    Unknown_70_1: typing.Any = 2
    Item0: typing.Any = 3
    Item1: typing.Any = 4
    Item2: typing.Any = 5
    Item3: typing.Any = 6
    Item4: typing.Any = 7
    Item5: typing.Any = 8
    Item6: typing.Any = 9
    Item7: typing.Any = 10
    Item8: typing.Any = 11
    Item9: typing.Any = 12
    TerritoryType: typing.Any = 13
    PlaceNameMain: typing.Any = 14
    PlaceNameSub: typing.Any = 15
    Radius: typing.Any = 16
    PlaceName: typing.Any = 17
    Order: typing.Any = 18
    X: typing.Any = 19
    Z: typing.Any = 20
    GatheringLevel: typing.Any = 21
    FishingSpotCategory: typing.Any = 22
    Unknown0: typing.Any = 23
    Rare: typing.Any = 24

class FittingShopRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown24: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    Unknown27: typing.Any = 27
    Unknown28: typing.Any = 28
    Unknown29: typing.Any = 29
    Unknown30: typing.Any = 30
    Unknown31: typing.Any = 31

class FittingShopCategoryRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class FittingShopCategoryItemRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class FittingShopItemSetRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6

class FollowMountRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17

class FrontlineRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22

class Frontline01Row(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown24: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    Unknown27: typing.Any = 27
    Unknown28: typing.Any = 28
    Unknown29: typing.Any = 29
    Unknown30: typing.Any = 30
    Unknown31: typing.Any = 31
    Unknown32: typing.Any = 32
    Unknown33: typing.Any = 33
    Unknown34: typing.Any = 34
    Unknown35: typing.Any = 35

class Frontline02Row(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown24: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    Unknown27: typing.Any = 27
    Unknown28: typing.Any = 28
    Unknown29: typing.Any = 29

class Frontline03Row(ExdRow):
    OvooData0: typing.Any = 0
    OvooData1: typing.Any = 1
    OvooData2: typing.Any = 2

class FurnitureCatalogCategoryRow(ExdRow):
    _display_field: str = 'Category'

    Category: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2

class FurnitureCatalogItemListRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0
    Category: typing.Any = 1
    Patch: typing.Any = 2

class GCRankGridaniaFemaleTextRow(ExdRow):
    _display_field: str = 'Singular'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    NameRank: typing.Any = 2
    Unknown0: typing.Any = 3
    Adjective: typing.Any = 4
    PossessivePronoun: typing.Any = 5
    StartsWithVowel: typing.Any = 6
    Unknown1: typing.Any = 7
    Pronoun: typing.Any = 8
    Article: typing.Any = 9

class GCRankGridaniaMaleTextRow(ExdRow):
    _display_field: str = 'Singular'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    NameRank: typing.Any = 2
    Unknown0: typing.Any = 3
    Adjective: typing.Any = 4
    PossessivePronoun: typing.Any = 5
    StartsWithVowel: typing.Any = 6
    Unknown1: typing.Any = 7
    Pronoun: typing.Any = 8
    Article: typing.Any = 9

class GCRankLimsaFemaleTextRow(ExdRow):
    _display_field: str = 'Singular'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    NameRank: typing.Any = 2
    Unknown0: typing.Any = 3
    Adjective: typing.Any = 4
    PossessivePronoun: typing.Any = 5
    StartsWithVowel: typing.Any = 6
    Unknown1: typing.Any = 7
    Pronoun: typing.Any = 8
    Article: typing.Any = 9

class GCRankLimsaMaleTextRow(ExdRow):
    _display_field: str = 'Singular'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    NameRank: typing.Any = 2
    Unknown0: typing.Any = 3
    Adjective: typing.Any = 4
    PossessivePronoun: typing.Any = 5
    StartsWithVowel: typing.Any = 6
    Unknown1: typing.Any = 7
    Pronoun: typing.Any = 8
    Article: typing.Any = 9

class GCRankUldahFemaleTextRow(ExdRow):
    _display_field: str = 'Singular'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    NameRank: typing.Any = 2
    Unknown0: typing.Any = 3
    Adjective: typing.Any = 4
    PossessivePronoun: typing.Any = 5
    StartsWithVowel: typing.Any = 6
    Unknown1: typing.Any = 7
    Pronoun: typing.Any = 8
    Article: typing.Any = 9

class GCRankUldahMaleTextRow(ExdRow):
    _display_field: str = 'Singular'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    NameRank: typing.Any = 2
    Unknown0: typing.Any = 3
    Adjective: typing.Any = 4
    PossessivePronoun: typing.Any = 5
    StartsWithVowel: typing.Any = 6
    Unknown1: typing.Any = 7
    Pronoun: typing.Any = 8
    Article: typing.Any = 9

class GCScripShopCategoryRow(ExdRow):
    GrandCompany: typing.Any = 0
    Tier: typing.Any = 1
    SubCategory: typing.Any = 2

class GCScripShopItemRow(ExdRow):
    _display_field: str = 'Item'

    CostGCSeals: typing.Any = 0
    Item: typing.Any = 1
    RequiredGrandCompanyRank: typing.Any = 2
    SortKey: typing.Any = 3

class GCShopRow(ExdRow):
    GrandCompany: typing.Any = 0

class GCShopItemCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class GCSupplyDefineRow(ExdRow):
    Unknown0: typing.Any = 0

class GCSupplyDutyRow(ExdRow):
    SupplyData0: typing.Any = 0
    SupplyData1: typing.Any = 1
    SupplyData2: typing.Any = 2
    SupplyData3: typing.Any = 3
    SupplyData4: typing.Any = 4
    SupplyData5: typing.Any = 5
    SupplyData6: typing.Any = 6
    SupplyData7: typing.Any = 7
    SupplyData8: typing.Any = 8
    SupplyData9: typing.Any = 9
    SupplyData10: typing.Any = 10

class GCSupplyDutyRewardRow(ExdRow):
    ExperienceSupply: typing.Any = 0
    ExperienceProvisioning: typing.Any = 1
    SealsExpertDelivery: typing.Any = 2
    SealsSupply: typing.Any = 3
    SealsProvisioning: typing.Any = 4

class GFATERow(ExdRow):
    GFATEParams0: typing.Any = 0
    GFATEParams1: typing.Any = 1
    GFATEParams2: typing.Any = 2
    GFATEParams3: typing.Any = 3
    GFATEParams4: typing.Any = 4
    GFATEParams5: typing.Any = 5
    GFATEParams6: typing.Any = 6
    GFATEParams7: typing.Any = 7
    GFATEParams8: typing.Any = 8
    GFATEParams9: typing.Any = 9
    GFATEParams10: typing.Any = 10
    GFATEParams11: typing.Any = 11
    GFATEParams12: typing.Any = 12
    GFATEParams13: typing.Any = 13
    GFATEParams14: typing.Any = 14
    Unknown0: typing.Any = 15
    Unknown1: typing.Any = 16
    Unknown2: typing.Any = 17
    Unknown3: typing.Any = 18
    Unknown4: typing.Any = 19
    Unknown5: typing.Any = 20
    Unknown6: typing.Any = 21
    Unknown7: typing.Any = 22
    Unknown8: typing.Any = 23
    Unknown9: typing.Any = 24
    Unknown10: typing.Any = 25
    Unknown11: typing.Any = 26

class GFateClimbingRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class GFateClimbing2Row(ExdRow):
    ContentEntry: typing.Any = 0

class GFateClimbing2ContentRow(ExdRow):
    PublicContentTextData: typing.Any = 0

class GFateClimbing2TotemTypeRow(ExdRow):
    PublicContentTextData: typing.Any = 0

class GFateDanceRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class GFateHiddenObjectRow(ExdRow):
    Unknown0: typing.Any = 0

class GFateRideShootingRow(ExdRow):
    ContentEntry: typing.Any = 0

class GFateRouletteRow(ExdRow):
    Unknown0: typing.Any = 0

class GFateStelthRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class GFateTypeRow(ExdRow):
    Unknown0: typing.Any = 0

class GameConditionValueArrayRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7

class GameRewardObtainTypeRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class GardeningSeedRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0
    Icon: typing.Any = 1
    ModelID: typing.Any = 2
    Unknown0: typing.Any = 3
    SE: typing.Any = 4
    Unknown1: typing.Any = 5

class GathererCrafterLvAdjustTableRow(ExdRow):
    RecipeLevel: typing.Any = 0
    Unknown1: typing.Any = 1
    CrafterLevel: typing.Any = 2
    GathererLevel: typing.Any = 3
    FisherLevel: typing.Any = 4

class GathererCrafterToolRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class GathererReductionRewardRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class GatheringConditionRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0

class GatheringExpRow(ExdRow):
    Exp: typing.Any = 0

class GatheringItemRow(ExdRow):
    _display_field: str = 'Item'

    Unknown0: typing.Any = 0
    SublimeVariant: typing.Any = 1
    Item: typing.Any = 2
    GatheringItemLevel: typing.Any = 3
    PerceptionReq: typing.Any = 4
    Unknown2: typing.Any = 5
    Unknown3: typing.Any = 6
    Unknown4: typing.Any = 7
    Unknown5: typing.Any = 8
    IsHidden: typing.Any = 9

class GatheringItemLevelConvertTableRow(ExdRow):
    GatheringItemLevel: typing.Any = 0
    Stars: typing.Any = 1

class GatheringItemPointRow(ExdRow):
    _display_field: str = 'GatheringPoint'

    GatheringPoint: typing.Any = 0

class GatheringLeveRow(ExdRow):
    Route0: typing.Any = 0
    Route1: typing.Any = 1
    Route2: typing.Any = 2
    Route3: typing.Any = 3
    RequiredItem0: typing.Any = 4
    RequiredItem1: typing.Any = 5
    RequiredItem2: typing.Any = 6
    RequiredItem3: typing.Any = 7
    Rule: typing.Any = 8
    BNpcEntry: typing.Any = 9
    Objective0: typing.Any = 10
    Objective1: typing.Any = 11
    RequiredItemQuantity0: typing.Any = 12
    RequiredItemQuantity1: typing.Any = 13
    RequiredItemQuantity2: typing.Any = 14
    RequiredItemQuantity3: typing.Any = 15
    ItemNumber: typing.Any = 16
    Varient: typing.Any = 17
    UseSecondaryTool: typing.Any = 18

class GatheringLeveBNpcEntryRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11

class GatheringLeveRouteRow(ExdRow):
    GatheringPoint0: typing.Any = 0
    GatheringPoint1: typing.Any = 1
    GatheringPoint2: typing.Any = 2
    GatheringPoint3: typing.Any = 3
    GatheringPoint4: typing.Any = 4
    GatheringPoint5: typing.Any = 5
    GatheringPoint6: typing.Any = 6
    GatheringPoint7: typing.Any = 7
    GatheringPoint8: typing.Any = 8
    GatheringPoint9: typing.Any = 9
    GatheringPoint10: typing.Any = 10
    GatheringPoint11: typing.Any = 11
    PopRange0: typing.Any = 12
    PopRange1: typing.Any = 13
    PopRange2: typing.Any = 14
    PopRange3: typing.Any = 15
    PopRange4: typing.Any = 16
    PopRange5: typing.Any = 17
    PopRange6: typing.Any = 18
    PopRange7: typing.Any = 19
    PopRange8: typing.Any = 20
    PopRange9: typing.Any = 21
    PopRange10: typing.Any = 22
    PopRange11: typing.Any = 23

class GatheringLeveRuleRow(ExdRow):
    _display_field: str = 'Rule'

    Rule: typing.Any = 0

class GatheringNotebookItemRow(ExdRow):
    Unknown0: typing.Any = 0

class GatheringNotebookListRow(ExdRow):
    GatheringItem0: typing.Any = 0
    GatheringItem1: typing.Any = 1
    GatheringItem2: typing.Any = 2
    GatheringItem3: typing.Any = 3
    GatheringItem4: typing.Any = 4
    GatheringItem5: typing.Any = 5
    GatheringItem6: typing.Any = 6
    GatheringItem7: typing.Any = 7
    GatheringItem8: typing.Any = 8
    GatheringItem9: typing.Any = 9
    GatheringItem10: typing.Any = 10
    GatheringItem11: typing.Any = 11
    GatheringItem12: typing.Any = 12
    GatheringItem13: typing.Any = 13
    GatheringItem14: typing.Any = 14
    GatheringItem15: typing.Any = 15
    GatheringItem16: typing.Any = 16
    GatheringItem17: typing.Any = 17
    GatheringItem18: typing.Any = 18
    GatheringItem19: typing.Any = 19
    GatheringItem20: typing.Any = 20
    GatheringItem21: typing.Any = 21
    GatheringItem22: typing.Any = 22
    GatheringItem23: typing.Any = 23
    GatheringItem24: typing.Any = 24
    GatheringItem25: typing.Any = 25
    GatheringItem26: typing.Any = 26
    GatheringItem27: typing.Any = 27
    GatheringItem28: typing.Any = 28
    GatheringItem29: typing.Any = 29
    GatheringItem30: typing.Any = 30
    GatheringItem31: typing.Any = 31
    GatheringItem32: typing.Any = 32
    GatheringItem33: typing.Any = 33
    GatheringItem34: typing.Any = 34
    GatheringItem35: typing.Any = 35
    GatheringItem36: typing.Any = 36
    GatheringItem37: typing.Any = 37
    GatheringItem38: typing.Any = 38
    GatheringItem39: typing.Any = 39
    GatheringItem40: typing.Any = 40
    GatheringItem41: typing.Any = 41
    GatheringItem42: typing.Any = 42
    GatheringItem43: typing.Any = 43
    GatheringItem44: typing.Any = 44
    GatheringItem45: typing.Any = 45
    GatheringItem46: typing.Any = 46
    GatheringItem47: typing.Any = 47
    GatheringItem48: typing.Any = 48
    GatheringItem49: typing.Any = 49
    GatheringItem50: typing.Any = 50
    GatheringItem51: typing.Any = 51
    GatheringItem52: typing.Any = 52
    GatheringItem53: typing.Any = 53
    GatheringItem54: typing.Any = 54
    GatheringItem55: typing.Any = 55
    GatheringItem56: typing.Any = 56
    GatheringItem57: typing.Any = 57
    GatheringItem58: typing.Any = 58
    GatheringItem59: typing.Any = 59
    GatheringItem60: typing.Any = 60
    GatheringItem61: typing.Any = 61
    GatheringItem62: typing.Any = 62
    GatheringItem63: typing.Any = 63
    GatheringItem64: typing.Any = 64
    GatheringItem65: typing.Any = 65
    GatheringItem66: typing.Any = 66
    GatheringItem67: typing.Any = 67
    GatheringItem68: typing.Any = 68
    GatheringItem69: typing.Any = 69
    GatheringItem70: typing.Any = 70
    GatheringItem71: typing.Any = 71
    GatheringItem72: typing.Any = 72
    GatheringItem73: typing.Any = 73
    GatheringItem74: typing.Any = 74
    GatheringItem75: typing.Any = 75
    GatheringItem76: typing.Any = 76
    GatheringItem77: typing.Any = 77
    GatheringItem78: typing.Any = 78
    GatheringItem79: typing.Any = 79
    GatheringItem80: typing.Any = 80
    GatheringItem81: typing.Any = 81
    GatheringItem82: typing.Any = 82
    GatheringItem83: typing.Any = 83
    GatheringItem84: typing.Any = 84
    GatheringItem85: typing.Any = 85
    GatheringItem86: typing.Any = 86
    GatheringItem87: typing.Any = 87
    GatheringItem88: typing.Any = 88
    GatheringItem89: typing.Any = 89
    GatheringItem90: typing.Any = 90
    GatheringItem91: typing.Any = 91
    GatheringItem92: typing.Any = 92
    GatheringItem93: typing.Any = 93
    GatheringItem94: typing.Any = 94
    GatheringItem95: typing.Any = 95
    GatheringItem96: typing.Any = 96
    GatheringItem97: typing.Any = 97
    GatheringItem98: typing.Any = 98
    GatheringItem99: typing.Any = 99
    Unknown0: typing.Any = 100

class GatheringPointRow(ExdRow):
    GatheringPointBase: typing.Any = 0
    GatheringPointBonus0: typing.Any = 1
    GatheringPointBonus1: typing.Any = 2
    TerritoryType: typing.Any = 3
    PlaceName: typing.Any = 4
    GatheringSubCategory: typing.Any = 5
    Type: typing.Any = 6
    Unknown0: typing.Any = 7
    Count: typing.Any = 8
    Unknown1: typing.Any = 9

class GatheringPointBaseRow(ExdRow):
    GatheringType: typing.Any = 0
    Item0: typing.Any = 1
    Item1: typing.Any = 2
    Item2: typing.Any = 3
    Item3: typing.Any = 4
    Item4: typing.Any = 5
    Item5: typing.Any = 6
    Item6: typing.Any = 7
    Item7: typing.Any = 8
    GatheringLevel: typing.Any = 9

class GatheringPointBonusRow(ExdRow):
    ConditionValue: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2
    BonusValue: typing.Any = 3
    Unknown2: typing.Any = 4
    Condition: typing.Any = 5
    BonusType: typing.Any = 6
    Unknown3: typing.Any = 7

class GatheringPointBonusTypeRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0

class GatheringPointNameRow(ExdRow):
    _display_field: str = 'Singular'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Adjective: typing.Any = 2
    PossessivePronoun: typing.Any = 3
    StartsWithVowel: typing.Any = 4
    Unknown0: typing.Any = 5
    Pronoun: typing.Any = 6
    Article: typing.Any = 7

class GatheringPointTransientRow(ExdRow):
    GatheringRarePopTimeTable: typing.Any = 0
    EphemeralStartTime: typing.Any = 1
    EphemeralEndTime: typing.Any = 2

class GatheringRarePopTimeTableRow(ExdRow):
    StartTime0: typing.Any = 0
    StartTime1: typing.Any = 1
    StartTime2: typing.Any = 2
    Duration0: typing.Any = 3
    Duration1: typing.Any = 4
    Duration2: typing.Any = 5

class GatheringSubCategoryRow(ExdRow):
    _display_field: str = 'FolkloreBook'

    FolkloreBook: typing.Any = 0
    Quest: typing.Any = 1
    Item: typing.Any = 2
    Division: typing.Any = 3
    GatheringType: typing.Any = 4
    ClassJob: typing.Any = 5
    Unknown0: typing.Any = 6

class GatheringTypeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    IconMain: typing.Any = 1
    IconOff: typing.Any = 2

class GcArmyCandidateCategoryRow(ExdRow):
    Unknown0: typing.Any = 0

class GcArmyCaptureRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7

class GcArmyCaptureTacticsRow(ExdRow):
    _display_field: str = 'Name'

    Tactic: typing.Any = 0
    Icon: typing.Any = 1
    Name: typing.Any = 2
    HP: typing.Any = 3
    DamageDealt: typing.Any = 4
    DamageReceived: typing.Any = 5

class GcArmyEquipPresetRow(ExdRow):
    MainHand: typing.Any = 0
    OffHand: typing.Any = 1
    Head: typing.Any = 2
    Body: typing.Any = 3
    Gloves: typing.Any = 4
    Legs: typing.Any = 5
    Feet: typing.Any = 6

class GcArmyExpeditionRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    ExpeditionParams0: typing.Any = 2
    ExpeditionParams1: typing.Any = 3
    ExpeditionParams2: typing.Any = 4
    ExpeditionParams3: typing.Any = 5
    ExpeditionParams4: typing.Any = 6
    ExpeditionParams5: typing.Any = 7
    RewardExperience: typing.Any = 8
    RequiredSeals: typing.Any = 9
    RequiredFlag: typing.Any = 10
    UnlockFlag: typing.Any = 11
    RequiredLevel: typing.Any = 12
    PercentBase: typing.Any = 13
    Unknown0: typing.Any = 14
    GcArmyExpeditionType: typing.Any = 15

class GcArmyExpeditionMemberBonusRow(ExdRow):
    Race: typing.Any = 0
    ClassJob: typing.Any = 1

class GcArmyExpeditionTraitRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10

class GcArmyExpeditionTraitCondRow(ExdRow):
    Unknown0: typing.Any = 0

class GcArmyExpeditionTypeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class GcArmyMemberRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class GcArmyMemberGrowRow(ExdRow):
    MemberParams0: typing.Any = 0
    MemberParams1: typing.Any = 1
    MemberParams2: typing.Any = 2
    MemberParams3: typing.Any = 3
    MemberParams4: typing.Any = 4
    MemberParams5: typing.Any = 5
    MemberParams6: typing.Any = 6
    MemberParams7: typing.Any = 7
    MemberParams8: typing.Any = 8
    MemberParams9: typing.Any = 9
    MemberParams10: typing.Any = 10
    MemberParams11: typing.Any = 11
    MemberParams12: typing.Any = 12
    MemberParams13: typing.Any = 13
    MemberParams14: typing.Any = 14
    MemberParams15: typing.Any = 15
    MemberParams16: typing.Any = 16
    MemberParams17: typing.Any = 17
    MemberParams18: typing.Any = 18
    MemberParams19: typing.Any = 19
    MemberParams20: typing.Any = 20
    MemberParams21: typing.Any = 21
    MemberParams22: typing.Any = 22
    MemberParams23: typing.Any = 23
    MemberParams24: typing.Any = 24
    MemberParams25: typing.Any = 25
    MemberParams26: typing.Any = 26
    MemberParams27: typing.Any = 27
    MemberParams28: typing.Any = 28
    MemberParams29: typing.Any = 29
    MemberParams30: typing.Any = 30
    MemberParams31: typing.Any = 31
    MemberParams32: typing.Any = 32
    MemberParams33: typing.Any = 33
    MemberParams34: typing.Any = 34
    MemberParams35: typing.Any = 35
    MemberParams36: typing.Any = 36
    MemberParams37: typing.Any = 37
    MemberParams38: typing.Any = 38
    MemberParams39: typing.Any = 39
    MemberParams40: typing.Any = 40
    MemberParams41: typing.Any = 41
    MemberParams42: typing.Any = 42
    MemberParams43: typing.Any = 43
    MemberParams44: typing.Any = 44
    MemberParams45: typing.Any = 45
    MemberParams46: typing.Any = 46
    MemberParams47: typing.Any = 47
    MemberParams48: typing.Any = 48
    MemberParams49: typing.Any = 49
    MemberParams50: typing.Any = 50
    MemberParams51: typing.Any = 51
    MemberParams52: typing.Any = 52
    MemberParams53: typing.Any = 53
    MemberParams54: typing.Any = 54
    MemberParams55: typing.Any = 55
    MemberParams56: typing.Any = 56
    MemberParams57: typing.Any = 57
    MemberParams58: typing.Any = 58
    MemberParams59: typing.Any = 59
    Unknown0: typing.Any = 60
    Unknown1: typing.Any = 61
    Unknown2: typing.Any = 62
    Unknown3: typing.Any = 63
    ClassBook: typing.Any = 64
    ClassJob: typing.Any = 65

class GcArmyMemberGrowExpRow(ExdRow):
    Unknown0: typing.Any = 0

class GcArmyProgressRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class GcArmyTrainingRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Experience: typing.Any = 2
    PhysicalBonus: typing.Any = 3
    MentalBonus: typing.Any = 4
    TacticalBonus: typing.Any = 5

class GeneralActionRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Icon: typing.Any = 2
    Action: typing.Any = 3
    UnlockLink: typing.Any = 4
    Unknown0: typing.Any = 5
    Recast: typing.Any = 6
    UIPriority: typing.Any = 7
    Unknown2: typing.Any = 8
    Unknown1: typing.Any = 9

class GilShopRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Icon: typing.Any = 1
    Quest: typing.Any = 2
    AcceptTalk: typing.Any = 3
    FailTalk: typing.Any = 4
    FestivalId: typing.Any = 5
    FestivalPhase: typing.Any = 6
    Unknown2: typing.Any = 7

class GilShopInfoRow(ExdRow):
    Unknown0: typing.Any = 0

class GilShopItemRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0
    QuestRequired0: typing.Any = 1
    QuestRequired1: typing.Any = 2
    AchievementRequired: typing.Any = 3
    StateRequired: typing.Any = 4
    Patch: typing.Any = 5
    Unknown_70_1: typing.Any = 6
    Unknown_70_2: typing.Any = 7
    Unknown1: typing.Any = 8
    IsHQ: typing.Any = 9

class GimmickAccessorRow(ExdRow):
    Param1: typing.Any = 0
    Param2: typing.Any = 1
    Type: typing.Any = 2
    Unknown0: typing.Any = 3
    Unknown1: typing.Any = 4
    Unknown2: typing.Any = 5
    Param0: typing.Any = 6
    Unknown6: typing.Any = 7
    Unknown3: typing.Any = 8
    Unknown4: typing.Any = 9
    Unknown5: typing.Any = 10

class GimmickBillRow(ExdRow):
    Unknown0: typing.Any = 0

class GimmickJumpRow(ExdRow):
    LoopMotion: typing.Any = 0
    EndMotion: typing.Any = 1
    FallDamage: typing.Any = 2
    Height: typing.Any = 3
    Unknown1: typing.Any = 4
    Unknown2: typing.Any = 5
    StartClient: typing.Any = 6
    Unknown0: typing.Any = 7

class GimmickRectRow(ExdRow):
    LayoutID: typing.Any = 0
    Param0: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown2: typing.Any = 4
    Param1: typing.Any = 5
    Unknown3: typing.Any = 6
    Unknown4: typing.Any = 7
    Unknown5: typing.Any = 8
    TriggerIn: typing.Any = 9
    TriggerOut: typing.Any = 10

class GimmickTalkRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class GimmickYesNoRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class GlassesRow(ExdRow):
    _display_field: str = 'Name'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Description: typing.Any = 2
    Name: typing.Any = 3
    Unknown_70_1: typing.Any = 4
    Unknown_70_2: typing.Any = 5
    Unknown_70_3: typing.Any = 6
    Unknown_70_4: typing.Any = 7
    Unknown_70_5: typing.Any = 8
    Unknown_70_6: typing.Any = 9
    Unknown_70_7: typing.Any = 10
    Icon: typing.Any = 11
    Unknown_70_8: typing.Any = 12
    Style: typing.Any = 13

class GlassesStyleRow(ExdRow):
    _display_field: str = 'Name'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Name: typing.Any = 2
    Unknown_70_1: typing.Any = 3
    Unknown_70_2: typing.Any = 4
    Unknown_70_3: typing.Any = 5
    Unknown_70_4: typing.Any = 6
    Unknown_70_5: typing.Any = 7
    Unknown_70_6: typing.Any = 8
    Icon: typing.Any = 9
    Order: typing.Any = 10
    Glasses0: typing.Any = 11
    Glasses1: typing.Any = 12
    Glasses2: typing.Any = 13
    Glasses3: typing.Any = 14
    Glasses4: typing.Any = 15
    Glasses5: typing.Any = 16
    Glasses6: typing.Any = 17
    Glasses7: typing.Any = 18
    Glasses8: typing.Any = 19
    Glasses9: typing.Any = 20
    Glasses10: typing.Any = 21
    Glasses11: typing.Any = 22
    Unknown_70_7: typing.Any = 23

class GoldSaucerArcadeMachineRow(ExdRow):
    Unknown0: typing.Any = 0
    Poor: typing.Any = 1
    Unknown1: typing.Any = 2
    Unknown2: typing.Any = 3
    Unknown3: typing.Any = 4
    Unknown4: typing.Any = 5
    Unknown5: typing.Any = 6
    Good: typing.Any = 7
    Unknown6: typing.Any = 8
    Unknown7: typing.Any = 9
    Unknown8: typing.Any = 10
    Unknown9: typing.Any = 11
    Unknown10: typing.Any = 12
    Great: typing.Any = 13
    Unknown11: typing.Any = 14
    Unknown12: typing.Any = 15
    Unknown13: typing.Any = 16
    Unknown14: typing.Any = 17
    Unknown15: typing.Any = 18
    Excellent: typing.Any = 19
    Unknown16: typing.Any = 20
    Unknown17: typing.Any = 21
    Unknown18: typing.Any = 22
    Unknown19: typing.Any = 23
    Unknown20: typing.Any = 24
    Unknown21: typing.Any = 25
    Unknown22: typing.Any = 26
    Unknown23: typing.Any = 27
    FailImage: typing.Any = 28
    Unknown24: typing.Any = 29
    Unknown25: typing.Any = 30
    Unknown26: typing.Any = 31
    Unknown27: typing.Any = 32
    Unknown28: typing.Any = 33
    Unknown29: typing.Any = 34
    Unknown30: typing.Any = 35
    Unknown31: typing.Any = 36
    Unknown32: typing.Any = 37
    Unknown33: typing.Any = 38
    Unknown34: typing.Any = 39
    Unknown35: typing.Any = 40
    Unknown36: typing.Any = 41
    Unknown37: typing.Any = 42

class GoldSaucerContentRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class GoldSaucerTalkRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown24: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    Unknown27: typing.Any = 27

class GoldSaucerTextDataRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0

class GrandCompanyRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2
    Unknown2: typing.Any = 3
    Unknown3: typing.Any = 4
    Unknown4: typing.Any = 5
    Unknown5: typing.Any = 6
    Unknown6: typing.Any = 7
    Unknown7: typing.Any = 8
    MonsterNote: typing.Any = 9

class GrandCompanyRankRow(ExdRow):
    MaxSeals: typing.Any = 0
    RequiredSeals: typing.Any = 1
    IconMaelstrom: typing.Any = 2
    IconSerpents: typing.Any = 3
    IconFlames: typing.Any = 4
    QuestMaelstrom: typing.Any = 5
    QuestSerpents: typing.Any = 6
    QuestFlames: typing.Any = 7
    Tier: typing.Any = 8
    Order: typing.Any = 9
    Unknown0: typing.Any = 10

class GroupPoseCharaStatusRow(ExdRow):
    Unknown0: typing.Any = 0

class GroupPoseCharacterShowPresetRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13

class GroupPoseFrameRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0
    GridText: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3
    Image: typing.Any = 4
    Unknown2: typing.Any = 5
    Unknown3: typing.Any = 6
    Unknown4: typing.Any = 7

class GroupPoseStampRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Unknown0: typing.Any = 1
    StampIcon: typing.Any = 2
    Unknown1: typing.Any = 3
    Category: typing.Any = 4
    Unknown2: typing.Any = 5
    Unknown3: typing.Any = 6
    Unknown4: typing.Any = 7
    Unknown5: typing.Any = 8
    Unknown6: typing.Any = 9
    Unknown7: typing.Any = 10

class GroupPoseStampCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Unknown0: typing.Any = 1

class GroupPoseStampFontColorRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class GuardianDeityRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Icon: typing.Any = 2

class GuideRow(ExdRow):
    GuideTitle: typing.Any = 0
    GuidePage: typing.Any = 1

class GuidePageRow(ExdRow):
    Output: typing.Any = 0
    Key: typing.Any = 1
    Unknown_70: typing.Any = 2

class GuidePageStringRow(ExdRow):
    _display_field: str = 'String'

    String: typing.Any = 0

class GuideTitleRow(ExdRow):
    _display_field: str = 'Title'

    Title: typing.Any = 0
    Unknown0: typing.Any = 1

class GuildOrderRow(ExdRow):
    Objective: typing.Any = 0
    Description1: typing.Any = 1
    Description2: typing.Any = 2
    Description3: typing.Any = 3
    CompletionBonusExp: typing.Any = 4
    RewardExp: typing.Any = 5
    CompletionBonusGil: typing.Any = 6
    RewardGil: typing.Any = 7
    Unknown0: typing.Any = 8
    Unknown1: typing.Any = 9
    Unknown2: typing.Any = 10
    Unknown3: typing.Any = 11
    Unknown4: typing.Any = 12
    Unknown5: typing.Any = 13
    Unknown6: typing.Any = 14
    Unknown7: typing.Any = 15
    ENpcName: typing.Any = 16

class GuildOrderGuideRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class GuildOrderOfficerRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class GuildleveAssignmentRow(ExdRow):
    Type: typing.Any = 0
    AssignmentTalk: typing.Any = 1
    Quest0: typing.Any = 2
    Quest1: typing.Any = 3
    Unknown0: typing.Any = 4
    Unknown1: typing.Any = 5
    Unknown2: typing.Any = 6
    Unknown3: typing.Any = 7
    Unknown4: typing.Any = 8
    Unknown5: typing.Any = 9
    Unknown6: typing.Any = 10

class GuildleveAssignmentCategoryRow(ExdRow):
    Category0: typing.Any = 0
    Category1: typing.Any = 1
    Category2: typing.Any = 2
    Category3: typing.Any = 3
    Category4: typing.Any = 4
    Category5: typing.Any = 5
    Category6: typing.Any = 6
    Category7: typing.Any = 7

class GuildleveAssignmentTalkRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown24: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    Unknown27: typing.Any = 27
    Unknown28: typing.Any = 28
    Unknown29: typing.Any = 29
    Talk0: typing.Any = 30
    Talk1: typing.Any = 31
    Talk2: typing.Any = 32
    Talk3: typing.Any = 33
    Talk4: typing.Any = 34
    Talk5: typing.Any = 35
    Talk6: typing.Any = 36
    Talk7: typing.Any = 37

class HWDAnnounceRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    ENPC: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3

class HWDCrafterSupplyRow(ExdRow):
    HWDCrafterSupplyParams0: typing.Any = 0
    HWDCrafterSupplyParams1: typing.Any = 1
    HWDCrafterSupplyParams2: typing.Any = 2
    HWDCrafterSupplyParams3: typing.Any = 3
    HWDCrafterSupplyParams4: typing.Any = 4
    HWDCrafterSupplyParams5: typing.Any = 5
    HWDCrafterSupplyParams6: typing.Any = 6
    HWDCrafterSupplyParams7: typing.Any = 7
    HWDCrafterSupplyParams8: typing.Any = 8
    HWDCrafterSupplyParams9: typing.Any = 9
    HWDCrafterSupplyParams10: typing.Any = 10
    HWDCrafterSupplyParams11: typing.Any = 11
    HWDCrafterSupplyParams12: typing.Any = 12
    HWDCrafterSupplyParams13: typing.Any = 13
    HWDCrafterSupplyParams14: typing.Any = 14
    HWDCrafterSupplyParams15: typing.Any = 15
    HWDCrafterSupplyParams16: typing.Any = 16
    HWDCrafterSupplyParams17: typing.Any = 17
    HWDCrafterSupplyParams18: typing.Any = 18
    HWDCrafterSupplyParams19: typing.Any = 19
    HWDCrafterSupplyParams20: typing.Any = 20
    HWDCrafterSupplyParams21: typing.Any = 21
    HWDCrafterSupplyParams22: typing.Any = 22

class HWDCrafterSupplyRewardRow(ExdRow):
    ExpReward: typing.Any = 0
    ScriptRewardAmount: typing.Any = 1
    Points: typing.Any = 2

class HWDCrafterSupplyTermRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class HWDDevLayerControlRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class HWDDevLevelUIRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class HWDDevLevelWebTextRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class HWDDevLivelyRow(ExdRow):
    _display_field: str = 'ENPC'

    ENPC: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2

class HWDDevProgressRow(ExdRow):
    _display_field: str = 'CanGoNext'

    CanGoNext: typing.Any = 0

class HWDGathereInspectTermRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class HWDGathererInspectionRow(ExdRow):
    HWDGathererInspectionData0: typing.Any = 0
    HWDGathererInspectionData1: typing.Any = 1
    HWDGathererInspectionData2: typing.Any = 2
    HWDGathererInspectionData3: typing.Any = 3
    HWDGathererInspectionData4: typing.Any = 4
    HWDGathererInspectionData5: typing.Any = 5
    HWDGathererInspectionData6: typing.Any = 6
    HWDGathererInspectionData7: typing.Any = 7
    HWDGathererInspectionData8: typing.Any = 8
    HWDGathererInspectionData9: typing.Any = 9
    HWDGathererInspectionData10: typing.Any = 10
    HWDGathererInspectionData11: typing.Any = 11
    HWDGathererInspectionData12: typing.Any = 12
    HWDGathererInspectionData13: typing.Any = 13
    HWDGathererInspectionData14: typing.Any = 14
    HWDGathererInspectionData15: typing.Any = 15
    HWDGathererInspectionData16: typing.Any = 16
    HWDGathererInspectionData17: typing.Any = 17
    HWDGathererInspectionData18: typing.Any = 18
    HWDGathererInspectionData19: typing.Any = 19
    HWDGathererInspectionData20: typing.Any = 20
    HWDGathererInspectionData21: typing.Any = 21
    HWDGathererInspectionData22: typing.Any = 22
    HWDGathererInspectionData23: typing.Any = 23
    HWDGathererInspectionData24: typing.Any = 24
    HWDGathererInspectionData25: typing.Any = 25
    HWDGathererInspectionData26: typing.Any = 26
    HWDGathererInspectionData27: typing.Any = 27
    HWDGathererInspectionData28: typing.Any = 28
    HWDGathererInspectionData29: typing.Any = 29
    HWDGathererInspectionData30: typing.Any = 30
    HWDGathererInspectionData31: typing.Any = 31
    HWDGathererInspectionData32: typing.Any = 32
    HWDGathererInspectionData33: typing.Any = 33
    HWDGathererInspectionData34: typing.Any = 34
    HWDGathererInspectionData35: typing.Any = 35
    HWDGathererInspectionData36: typing.Any = 36
    HWDGathererInspectionData37: typing.Any = 37
    HWDGathererInspectionData38: typing.Any = 38
    HWDGathererInspectionData39: typing.Any = 39
    HWDGathererInspectionData40: typing.Any = 40
    HWDGathererInspectionData41: typing.Any = 41
    HWDGathererInspectionData42: typing.Any = 42
    HWDGathererInspectionData43: typing.Any = 43
    HWDGathererInspectionData44: typing.Any = 44
    HWDGathererInspectionData45: typing.Any = 45
    HWDGathererInspectionData46: typing.Any = 46
    HWDGathererInspectionData47: typing.Any = 47
    HWDGathererInspectionData48: typing.Any = 48
    HWDGathererInspectionData49: typing.Any = 49
    HWDGathererInspectionData50: typing.Any = 50
    HWDGathererInspectionData51: typing.Any = 51
    HWDGathererInspectionData52: typing.Any = 52
    HWDGathererInspectionData53: typing.Any = 53
    HWDGathererInspectionData54: typing.Any = 54
    HWDGathererInspectionData55: typing.Any = 55
    HWDGathererInspectionData56: typing.Any = 56
    HWDGathererInspectionData57: typing.Any = 57
    HWDGathererInspectionData58: typing.Any = 58
    HWDGathererInspectionData59: typing.Any = 59
    HWDGathererInspectionData60: typing.Any = 60
    HWDGathererInspectionData61: typing.Any = 61
    HWDGathererInspectionData62: typing.Any = 62
    HWDGathererInspectionData63: typing.Any = 63
    HWDGathererInspectionData64: typing.Any = 64
    HWDGathererInspectionData65: typing.Any = 65
    HWDGathererInspectionData66: typing.Any = 66
    HWDGathererInspectionData67: typing.Any = 67
    HWDGathererInspectionData68: typing.Any = 68
    HWDGathererInspectionData69: typing.Any = 69
    HWDGathererInspectionData70: typing.Any = 70
    HWDGathererInspectionData71: typing.Any = 71
    HWDGathererInspectionData72: typing.Any = 72
    HWDGathererInspectionData73: typing.Any = 73
    HWDGathererInspectionData74: typing.Any = 74
    HWDGathererInspectionData75: typing.Any = 75
    HWDGathererInspectionData76: typing.Any = 76
    HWDGathererInspectionData77: typing.Any = 77
    HWDGathererInspectionData78: typing.Any = 78

class HWDGathererInspectionRewardRow(ExdRow):
    _display_field: str = 'Scrips'

    Scrips: typing.Any = 0
    Points: typing.Any = 1

class HWDInfoBoardArticleRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0
    Unknown0: typing.Any = 1
    Type: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown2: typing.Any = 4

class HWDInfoBoardArticleTransientRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0
    NpcName: typing.Any = 1
    Image: typing.Any = 2

class HWDInfoBoardArticleTypeRow(ExdRow):
    _display_field: str = 'Type'

    Type: typing.Any = 0

class HWDInfoBoardBackNumberRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class HWDLevelChangeDeceptionRow(ExdRow):
    _display_field: str = 'Image'

    Image: typing.Any = 0

class HWDSharedGroupRow(ExdRow):
    _display_field: str = 'LGBSharedGroup'

    LGBSharedGroup: typing.Any = 0
    Param: typing.Any = 1

class HWDSharedGroupControlParamRow(ExdRow):
    Unknown0: typing.Any = 0
    ParamValue: typing.Any = 1

class HairMakeTypeRow(ExdRow):
    CharaMakeStruct0: typing.Any = 0
    CharaMakeStruct1: typing.Any = 1
    CharaMakeStruct2: typing.Any = 2
    CharaMakeStruct3: typing.Any = 3
    CharaMakeStruct4: typing.Any = 4
    CharaMakeStruct5: typing.Any = 5
    CharaMakeStruct6: typing.Any = 6
    CharaMakeStruct7: typing.Any = 7
    CharaMakeStruct8: typing.Any = 8
    FacialFeatureOption0: typing.Any = 9
    FacialFeatureOption1: typing.Any = 10
    FacialFeatureOption2: typing.Any = 11
    FacialFeatureOption3: typing.Any = 12
    FacialFeatureOption4: typing.Any = 13
    FacialFeatureOption5: typing.Any = 14
    FacialFeatureOption6: typing.Any = 15
    FacialFeatureOption7: typing.Any = 16
    Race: typing.Any = 17
    Tribe: typing.Any = 18
    Gender: typing.Any = 19

class HalloweenNpcSelectRow(ExdRow):
    Description: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6

class HouseRetainerPoseRow(ExdRow):
    _display_field: str = 'ActionTimeline'

    ActionTimeline: typing.Any = 0

class HousingAethernetRow(ExdRow):
    Level: typing.Any = 0
    TerritoryType: typing.Any = 1
    PlaceName: typing.Any = 2
    Order: typing.Any = 3

class HousingAppealRow(ExdRow):
    _display_field: str = 'Tag'

    Tag: typing.Any = 0
    Icon: typing.Any = 1
    Order: typing.Any = 2

class HousingEmploymentNpcListRow(ExdRow):
    MaleENpcBase: typing.Any = 0
    FemaleENpcBase: typing.Any = 1
    Race: typing.Any = 2

class HousingEmploymentNpcRaceRow(ExdRow):
    _display_field: str = 'Race'

    Race: typing.Any = 0

class HousingExteriorRow(ExdRow):
    Model: typing.Any = 0
    PlaceName: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3
    HousingSize: typing.Any = 4

class HousingFurnitureRow(ExdRow):
    _display_field: str = 'Item'

    UsageParameter: typing.Any = 0
    CustomTalk: typing.Any = 1
    Item: typing.Any = 2
    ModelKey: typing.Any = 3
    HousingItemCategory: typing.Any = 4
    UsageType: typing.Any = 5
    Unknown0: typing.Any = 6
    AquariumTier: typing.Any = 7
    Unknown1: typing.Any = 8
    Unknown2: typing.Any = 9
    Unknown3: typing.Any = 10
    DestroyOnRemoval: typing.Any = 11
    Unknown4: typing.Any = 12
    Unknown5: typing.Any = 13
    Unknown6: typing.Any = 14

class HousingIndoorTerritoryRow(ExdRow):
    Unknown0: typing.Any = 0

class HousingInteriorRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class HousingLandSetRow(ExdRow):
    LandSet0: typing.Any = 0
    LandSet1: typing.Any = 1
    LandSet2: typing.Any = 2
    LandSet3: typing.Any = 3
    LandSet4: typing.Any = 4
    LandSet5: typing.Any = 5
    LandSet6: typing.Any = 6
    LandSet7: typing.Any = 7
    LandSet8: typing.Any = 8
    LandSet9: typing.Any = 9
    LandSet10: typing.Any = 10
    LandSet11: typing.Any = 11
    LandSet12: typing.Any = 12
    LandSet13: typing.Any = 13
    LandSet14: typing.Any = 14
    LandSet15: typing.Any = 15
    LandSet16: typing.Any = 16
    LandSet17: typing.Any = 17
    LandSet18: typing.Any = 18
    LandSet19: typing.Any = 19
    LandSet20: typing.Any = 20
    LandSet21: typing.Any = 21
    LandSet22: typing.Any = 22
    LandSet23: typing.Any = 23
    LandSet24: typing.Any = 24
    LandSet25: typing.Any = 25
    LandSet26: typing.Any = 26
    LandSet27: typing.Any = 27
    LandSet28: typing.Any = 28
    LandSet29: typing.Any = 29
    LandSet30: typing.Any = 30
    LandSet31: typing.Any = 31
    LandSet32: typing.Any = 32
    LandSet33: typing.Any = 33
    LandSet34: typing.Any = 34
    LandSet35: typing.Any = 35
    LandSet36: typing.Any = 36
    LandSet37: typing.Any = 37
    LandSet38: typing.Any = 38
    LandSet39: typing.Any = 39
    LandSet40: typing.Any = 40
    LandSet41: typing.Any = 41
    LandSet42: typing.Any = 42
    LandSet43: typing.Any = 43
    LandSet44: typing.Any = 44
    LandSet45: typing.Any = 45
    LandSet46: typing.Any = 46
    LandSet47: typing.Any = 47
    LandSet48: typing.Any = 48
    LandSet49: typing.Any = 49
    LandSet50: typing.Any = 50
    LandSet51: typing.Any = 51
    LandSet52: typing.Any = 52
    LandSet53: typing.Any = 53
    LandSet54: typing.Any = 54
    LandSet55: typing.Any = 55
    LandSet56: typing.Any = 56
    LandSet57: typing.Any = 57
    LandSet58: typing.Any = 58
    LandSet59: typing.Any = 59
    UnknownRange1: typing.Any = 60
    UnknownRange2: typing.Any = 61

class HousingMapMarkerInfoRow(ExdRow):
    X: typing.Any = 0
    Y: typing.Any = 1
    Z: typing.Any = 2
    Unknown0: typing.Any = 3
    Map: typing.Any = 4

class HousingMateAuthorityRow(ExdRow):
    Unknown0: typing.Any = 0

class HousingMerchantPoseRow(ExdRow):
    _display_field: str = 'Pose'

    Pose: typing.Any = 0
    ActionTimeline: typing.Any = 1

class HousingPileLimitRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7

class HousingPlacementRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0

class HousingPresetRow(ExdRow):
    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Adjective: typing.Any = 2
    PossessivePronoun: typing.Any = 3
    StartsWithVowel: typing.Any = 4
    Unknown0: typing.Any = 5
    Pronoun: typing.Any = 6
    Article: typing.Any = 7
    ExteriorRoof: typing.Any = 8
    ExteriorWall: typing.Any = 9
    ExteriorWindow: typing.Any = 10
    ExteriorDoor: typing.Any = 11
    InteriorWall: typing.Any = 12
    InteriorFlooring: typing.Any = 13
    InteriorLighting: typing.Any = 14
    OtherFloorWall: typing.Any = 15
    OtherFloorFlooring: typing.Any = 16
    OtherFloorLighting: typing.Any = 17
    BasementWall: typing.Any = 18
    BasementFlooring: typing.Any = 19
    BasementLighting: typing.Any = 20
    MansionLighting: typing.Any = 21
    PlaceName: typing.Any = 22
    HousingSize: typing.Any = 23

class HousingRenovationRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3

class HousingTrainingDollRow(ExdRow):
    Unknown0: typing.Any = 0

class HousingUnitedExteriorRow(ExdRow):
    Roof: typing.Any = 0
    Walls: typing.Any = 1
    Windows: typing.Any = 2
    Door: typing.Any = 3
    OptionalRoof: typing.Any = 4
    OptionalWall: typing.Any = 5
    OptionalSignboard: typing.Any = 6
    Fence: typing.Any = 7
    PlotSize: typing.Any = 8

class HousingUnplacementRow(ExdRow):
    Unknown0: typing.Any = 0

class HousingYardObjectRow(ExdRow):
    _display_field: str = 'Item'

    UsageParameter: typing.Any = 0
    CustomTalk: typing.Any = 1
    Item: typing.Any = 2
    ModelKey: typing.Any = 3
    HousingItemCategory: typing.Any = 4
    UsageType: typing.Any = 5
    Unknown0: typing.Any = 6
    Unknown1: typing.Any = 7
    Unknown2: typing.Any = 8
    Unknown3: typing.Any = 9
    DestroyOnRemoval: typing.Any = 10
    Unknown4: typing.Any = 11
    Unknown5: typing.Any = 12
    Unknown6: typing.Any = 13
    Unknown7: typing.Any = 14

class HowToRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    HowToPagePC0: typing.Any = 1
    HowToPagePC1: typing.Any = 2
    HowToPagePC2: typing.Any = 3
    HowToPagePC3: typing.Any = 4
    HowToPagePC4: typing.Any = 5
    HowToPageController0: typing.Any = 6
    HowToPageController1: typing.Any = 7
    HowToPageController2: typing.Any = 8
    HowToPageController3: typing.Any = 9
    HowToPageController4: typing.Any = 10
    Sort: typing.Any = 11
    Category: typing.Any = 12
    Announce: typing.Any = 13

class HowToCategoryRow(ExdRow):
    _display_field: str = 'Category'

    Category: typing.Any = 0

class HowToPageRow(ExdRow):
    _display_field: str = 'Image'

    Text0: typing.Any = 0
    Text1: typing.Any = 1
    Text2: typing.Any = 2
    Image: typing.Any = 3
    Type: typing.Any = 4
    IconType: typing.Any = 5
    TextType: typing.Any = 6

class HudRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class HudTransientRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class HugeCraftworksNpcRow(ExdRow):
    _display_field: str = 'EventNpc'

    HugeCraftworksTurnInParam0: typing.Any = 0
    HugeCraftworksTurnInParam1: typing.Any = 1
    HugeCraftworksTurnInParam2: typing.Any = 2
    HugeCraftworksTurnInParam3: typing.Any = 3
    HugeCraftworksTurnInParam4: typing.Any = 4
    HugeCraftworksTurnInParam5: typing.Any = 5
    HugeCraftworksRewardParam0: typing.Any = 6
    HugeCraftworksRewardParam1: typing.Any = 7
    HugeCraftworksRewardParam2: typing.Any = 8
    HugeCraftworksRewardParam3: typing.Any = 9
    HugeCraftworksRewardParam4: typing.Any = 10
    HugeCraftworksRewardParam5: typing.Any = 11
    Transient: typing.Any = 12
    EventNpc: typing.Any = 13
    ClassJobCategory: typing.Any = 14

class HugeCraftworksRankRow(ExdRow):
    ExpRewardPerItem: typing.Any = 0
    CrafterLevel: typing.Any = 1
    Unknown0: typing.Any = 2

class IKDContentBonusRow(ExdRow):
    _display_field: str = 'Objective'

    Objective: typing.Any = 0
    Requirement: typing.Any = 1
    Image: typing.Any = 2
    Unknown0: typing.Any = 3
    Order: typing.Any = 4

class IKDFishParamRow(ExdRow):
    _display_field: str = 'Fish'

    Fish: typing.Any = 0
    IKDContentBonus: typing.Any = 1
    Unknown0: typing.Any = 2

class IKDPlayerMissionConditionRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class IKDRouteRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Spot0: typing.Any = 1
    Spot1: typing.Any = 2
    Spot2: typing.Any = 3
    Image: typing.Any = 4
    Unknown0: typing.Any = 5
    Unknown1: typing.Any = 6
    Instance: typing.Any = 7
    Unknown2: typing.Any = 8
    Time0: typing.Any = 9
    Time1: typing.Any = 10
    Time2: typing.Any = 11

class IKDRouteTableRow(ExdRow):
    _display_field: str = 'Route'

    Route: typing.Any = 0
    Unknown0: typing.Any = 1

class IKDSpotRow(ExdRow):
    _display_field: str = 'SpotMain'

    SpotMain: typing.Any = 0
    SpotSub: typing.Any = 1
    PlaceName: typing.Any = 2

class IKDTimeDefineRow(ExdRow):
    Unknown0: typing.Any = 0

class IconLanguageRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9

class InclusionShopRow(ExdRow):
    Unknown0: typing.Any = 0
    Category0: typing.Any = 1
    Category1: typing.Any = 2
    Category2: typing.Any = 3
    Category3: typing.Any = 4
    Category4: typing.Any = 5
    Category5: typing.Any = 6
    Category6: typing.Any = 7
    Category7: typing.Any = 8
    Category8: typing.Any = 9
    Category9: typing.Any = 10
    Category10: typing.Any = 11
    Category11: typing.Any = 12
    Category12: typing.Any = 13
    Category13: typing.Any = 14
    Category14: typing.Any = 15
    Category15: typing.Any = 16
    Category16: typing.Any = 17
    Category17: typing.Any = 18
    Category18: typing.Any = 19
    Category19: typing.Any = 20
    Category20: typing.Any = 21
    Category21: typing.Any = 22
    Category22: typing.Any = 23
    Category23: typing.Any = 24
    Category24: typing.Any = 25
    Category25: typing.Any = 26
    Category26: typing.Any = 27
    Category27: typing.Any = 28
    Category28: typing.Any = 29
    Category29: typing.Any = 30
    Unknown1: typing.Any = 31
    Unknown2: typing.Any = 32

class InclusionShopCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    InclusionShopSeries: typing.Any = 1
    ClassJobCategory: typing.Any = 2

class InclusionShopSeriesRow(ExdRow):
    _display_field: str = 'SpecialShop'

    SpecialShop: typing.Any = 0

class InclusionShopWelcomRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class InclusionShopWelcomTextRow(ExdRow):
    Unknown0: typing.Any = 0

class IndividualWeatherRow(ExdRow):
    IndividualWeatherData0: typing.Any = 0
    IndividualWeatherData1: typing.Any = 1
    IndividualWeatherData2: typing.Any = 2
    IndividualWeatherData3: typing.Any = 3
    IndividualWeatherData4: typing.Any = 4
    IndividualWeatherData5: typing.Any = 5
    IndividualWeatherData6: typing.Any = 6

class InstanceContentRow(ExdRow):
    NewPlayerBonusGil: typing.Any = 0
    NewPlayerBonusExp: typing.Any = 1
    FinalBossExp: typing.Any = 2
    Unknown0: typing.Any = 3
    BossExp0: typing.Any = 4
    BossExp1: typing.Any = 5
    BossExp2: typing.Any = 6
    BossExp3: typing.Any = 7
    BossExp4: typing.Any = 8
    InstanceClearExp: typing.Any = 9
    InstanceClearGil: typing.Any = 10
    InstanceContentRewardItem: typing.Any = 11
    NewPlayerBonusA: typing.Any = 12
    NewPlayerBonusB: typing.Any = 13
    FinalBossCurrencyA: typing.Any = 14
    FinalBossCurrencyB: typing.Any = 15
    FinalBossCurrencyC: typing.Any = 16
    BossCurrencyA0: typing.Any = 17
    BossCurrencyA1: typing.Any = 18
    BossCurrencyA2: typing.Any = 19
    BossCurrencyA3: typing.Any = 20
    BossCurrencyA4: typing.Any = 21
    BossCurrencyB0: typing.Any = 22
    BossCurrencyB1: typing.Any = 23
    BossCurrencyB2: typing.Any = 24
    BossCurrencyB3: typing.Any = 25
    BossCurrencyB4: typing.Any = 26
    BossCurrencyC0: typing.Any = 27
    BossCurrencyC1: typing.Any = 28
    BossCurrencyC2: typing.Any = 29
    BossCurrencyC3: typing.Any = 30
    BossCurrencyC4: typing.Any = 31
    Unknown1: typing.Any = 32
    LimitedTimeBonus: typing.Any = 33
    Cutscene: typing.Any = 34
    LGBEventRange: typing.Any = 35
    InstanceContentTextDataBossStart: typing.Any = 36
    InstanceContentTextDataBossEnd: typing.Any = 37
    BNpcBaseBoss: typing.Any = 38
    InstanceContentTextDataObjectiveStart: typing.Any = 39
    InstanceContentTextDataObjectiveEnd: typing.Any = 40
    Unknown2: typing.Any = 41
    ReqInstance: typing.Any = 42
    InstanceContentBuff: typing.Any = 43
    TimeLimitmin: typing.Any = 44
    BGM: typing.Any = 45
    WinBGM: typing.Any = 46
    ContentFinderCondition: typing.Any = 47
    SortKey: typing.Any = 48
    ContentRoute: typing.Any = 49
    ContentDirectorManagedSG: typing.Any = 50
    ContentTodo: typing.Any = 51
    Unknown6: typing.Any = 52
    Unknown7: typing.Any = 53
    ContentEventItem: typing.Any = 54
    ContentDirectorBattleTalk: typing.Any = 55
    PartyCondition: typing.Any = 56
    InstanceContentType: typing.Any = 57
    WeekRestriction: typing.Any = 58
    Colosseum: typing.Any = 59
    Unknown9: typing.Any = 60
    QTE1: typing.Any = 61
    QTE2: typing.Any = 62
    Unknown12: typing.Any = 63
    ContentAttributeRect: typing.Any = 64
    Unknown13: typing.Any = 65
    Unknown14: typing.Any = 66
    Unknown15: typing.Any = 67
    Unknown16: typing.Any = 68
    Unknown17: typing.Any = 69
    Unknown18: typing.Any = 70
    Unknown19: typing.Any = 71

class InstanceContentBuffRow(ExdRow):
    EchoStart: typing.Any = 0
    EchoDeath: typing.Any = 1

class InstanceContentGuideRow(ExdRow):
    Instance: typing.Any = 0
    Unknown0: typing.Any = 1

class InstanceContentQICDataRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class InstanceContentRewardItemRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class InstanceContentTextDataRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0

class InstanceContentTypeRow(ExdRow):
    StartLogMessage: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    SupportsPartyMemberPortraits: typing.Any = 7
    Unknown8: typing.Any = 8

class ItemRow(ExdRow):
    _display_field: str = 'Name'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Description: typing.Any = 2
    Name: typing.Any = 3
    Adjective: typing.Any = 4
    PossessivePronoun: typing.Any = 5
    StartsWithVowel: typing.Any = 6
    Unknown0: typing.Any = 7
    Pronoun: typing.Any = 8
    Article: typing.Any = 9
    ModelMain: typing.Any = 10
    ModelSub: typing.Any = 11
    DamagePhys: typing.Any = 12
    DamageMag: typing.Any = 13
    Delayms: typing.Any = 14
    BlockRate: typing.Any = 15
    Block: typing.Any = 16
    DefensePhys: typing.Any = 17
    DefenseMag: typing.Any = 18
    BaseParamValue0: typing.Any = 19
    BaseParamValue1: typing.Any = 20
    BaseParamValue2: typing.Any = 21
    BaseParamValue3: typing.Any = 22
    BaseParamValue4: typing.Any = 23
    BaseParamValue5: typing.Any = 24
    BaseParamValueSpecial0: typing.Any = 25
    BaseParamValueSpecial1: typing.Any = 26
    BaseParamValueSpecial2: typing.Any = 27
    BaseParamValueSpecial3: typing.Any = 28
    BaseParamValueSpecial4: typing.Any = 29
    BaseParamValueSpecial5: typing.Any = 30
    LevelEquip: typing.Any = 31
    RequiredPvpRank: typing.Any = 32
    EquipRestriction: typing.Any = 33
    ClassJobCategory: typing.Any = 34
    GrandCompany: typing.Any = 35
    ItemSeries: typing.Any = 36
    BaseParamModifier: typing.Any = 37
    ClassJobUse: typing.Any = 38
    Unknown2: typing.Any = 39
    Unknown3: typing.Any = 40
    BaseParam0: typing.Any = 41
    BaseParam1: typing.Any = 42
    BaseParam2: typing.Any = 43
    BaseParam3: typing.Any = 44
    BaseParam4: typing.Any = 45
    BaseParam5: typing.Any = 46
    ItemSpecialBonus: typing.Any = 47
    ItemSpecialBonusParam: typing.Any = 48
    BaseParamSpecial0: typing.Any = 49
    BaseParamSpecial1: typing.Any = 50
    BaseParamSpecial2: typing.Any = 51
    BaseParamSpecial3: typing.Any = 52
    BaseParamSpecial4: typing.Any = 53
    BaseParamSpecial5: typing.Any = 54
    MaterializeType: typing.Any = 55
    MateriaSlotCount: typing.Any = 56
    SubStatCategory: typing.Any = 57
    IsAdvancedMeldingPermitted: typing.Any = 58
    IsPvP: typing.Any = 59
    IsGlamorous: typing.Any = 60
    AdditionalData: typing.Any = 61
    StackSize: typing.Any = 62
    PriceMid: typing.Any = 63
    PriceLow: typing.Any = 64
    ItemRepair: typing.Any = 65
    ItemGlamour: typing.Any = 66
    Icon: typing.Any = 67
    LevelItem: typing.Any = 68
    Unknown4: typing.Any = 69
    ItemAction: typing.Any = 70
    Cooldowns: typing.Any = 71
    Desynth: typing.Any = 72
    AetherialReduce: typing.Any = 73
    Rarity: typing.Any = 74
    FilterGroup: typing.Any = 75
    ItemUICategory: typing.Any = 76
    ItemSearchCategory: typing.Any = 77
    EquipSlotCategory: typing.Any = 78
    ItemSortCategory: typing.Any = 79
    DyeCount: typing.Any = 80
    CastTimeSeconds: typing.Any = 81
    ClassJobRepair: typing.Any = 82
    IsUnique: typing.Any = 83
    IsUntradable: typing.Any = 84
    IsIndisposable: typing.Any = 85
    Lot: typing.Any = 86
    CanBeHq: typing.Any = 87
    IsCrestWorthy: typing.Any = 88
    IsCollectable: typing.Any = 89
    AlwaysCollectable: typing.Any = 90

class ItemActionRow(ExdRow):
    Type: typing.Any = 0
    Data0: typing.Any = 1
    Data1: typing.Any = 2
    Data2: typing.Any = 3
    Data3: typing.Any = 4
    Data4: typing.Any = 5
    Data5: typing.Any = 6
    Data6: typing.Any = 7
    Data7: typing.Any = 8
    Data8: typing.Any = 9
    DataHQ0: typing.Any = 10
    DataHQ1: typing.Any = 11
    DataHQ2: typing.Any = 12
    DataHQ3: typing.Any = 13
    DataHQ4: typing.Any = 14
    DataHQ5: typing.Any = 15
    DataHQ6: typing.Any = 16
    DataHQ7: typing.Any = 17
    DataHQ8: typing.Any = 18
    CondLv: typing.Any = 19
    CondBattle: typing.Any = 20
    CondPVP: typing.Any = 21
    CondPVPOnly: typing.Any = 22

class ItemActionTelepoRow(ExdRow):
    _display_field: str = 'Requirement'

    Requirement: typing.Any = 0
    DenyMessage: typing.Any = 1

class ItemBarterCheckRow(ExdRow):
    Question: typing.Any = 0
    Confirm: typing.Any = 1
    Category: typing.Any = 2

class ItemBarterWarningRow(ExdRow):
    Unknown0: typing.Any = 0

class ItemFoodRow(ExdRow):
    Max0: typing.Any = 0
    Max1: typing.Any = 1
    Max2: typing.Any = 2
    MaxHQ0: typing.Any = 3
    MaxHQ1: typing.Any = 4
    MaxHQ2: typing.Any = 5
    EXPBonusPercent: typing.Any = 6
    BaseParam0: typing.Any = 7
    BaseParam1: typing.Any = 8
    BaseParam2: typing.Any = 9
    Value0: typing.Any = 10
    Value1: typing.Any = 11
    Value2: typing.Any = 12
    ValueHQ0: typing.Any = 13
    ValueHQ1: typing.Any = 14
    ValueHQ2: typing.Any = 15
    IsRelative0: typing.Any = 16
    IsRelative1: typing.Any = 17
    IsRelative2: typing.Any = 18

class ItemLevelRow(ExdRow):
    Strength: typing.Any = 0
    Dexterity: typing.Any = 1
    Vitality: typing.Any = 2
    Intelligence: typing.Any = 3
    Mind: typing.Any = 4
    Piety: typing.Any = 5
    HP: typing.Any = 6
    MP: typing.Any = 7
    TP: typing.Any = 8
    GP: typing.Any = 9
    CP: typing.Any = 10
    PhysicalDamage: typing.Any = 11
    MagicalDamage: typing.Any = 12
    Delay: typing.Any = 13
    AdditionalEffect: typing.Any = 14
    AttackSpeed: typing.Any = 15
    BlockRate: typing.Any = 16
    BlockStrength: typing.Any = 17
    Tenacity: typing.Any = 18
    AttackPower: typing.Any = 19
    Defense: typing.Any = 20
    DirectHitRate: typing.Any = 21
    Evasion: typing.Any = 22
    MagicDefense: typing.Any = 23
    CriticalHitPower: typing.Any = 24
    CriticalHitResilience: typing.Any = 25
    CriticalHit: typing.Any = 26
    CriticalHitEvasion: typing.Any = 27
    SlashingResistance: typing.Any = 28
    PiercingResistance: typing.Any = 29
    BluntResistance: typing.Any = 30
    ProjectileResistance: typing.Any = 31
    AttackMagicPotency: typing.Any = 32
    HealingMagicPotency: typing.Any = 33
    EnhancementMagicPotency: typing.Any = 34
    EnfeeblingMagicPotency: typing.Any = 35
    FireResistance: typing.Any = 36
    IceResistance: typing.Any = 37
    WindResistance: typing.Any = 38
    EarthResistance: typing.Any = 39
    LightningResistance: typing.Any = 40
    WaterResistance: typing.Any = 41
    MagicResistance: typing.Any = 42
    Determination: typing.Any = 43
    SkillSpeed: typing.Any = 44
    SpellSpeed: typing.Any = 45
    Haste: typing.Any = 46
    Morale: typing.Any = 47
    Enmity: typing.Any = 48
    EnmityReduction: typing.Any = 49
    CarefulDesynthesis: typing.Any = 50
    EXPBonus: typing.Any = 51
    Regen: typing.Any = 52
    Refresh: typing.Any = 53
    MovementSpeed: typing.Any = 54
    Spikes: typing.Any = 55
    SlowResistance: typing.Any = 56
    PetrificationResistance: typing.Any = 57
    ParalysisResistance: typing.Any = 58
    SilenceResistance: typing.Any = 59
    BlindResistance: typing.Any = 60
    PoisonResistance: typing.Any = 61
    StunResistance: typing.Any = 62
    SleepResistance: typing.Any = 63
    BindResistance: typing.Any = 64
    HeavyResistance: typing.Any = 65
    DoomResistance: typing.Any = 66
    ReducedDurabilityLoss: typing.Any = 67
    IncreasedSpiritbondGain: typing.Any = 68
    Craftsmanship: typing.Any = 69
    Control: typing.Any = 70
    Gathering: typing.Any = 71
    Perception: typing.Any = 72
    Unknown0: typing.Any = 73

class ItemOnceHqMasterpieceRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class ItemRepairPriceRow(ExdRow):
    Unknown0: typing.Any = 0

class ItemRepairResourceRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0

class ItemRetainerLevelUpRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class ItemSearchCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Icon: typing.Any = 1
    Category: typing.Any = 2
    Order: typing.Any = 3
    ClassJob: typing.Any = 4
    Unknown0: typing.Any = 5

class ItemSeriesRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class ItemSortCategoryRow(ExdRow):
    _display_field: str = 'Param'

    Param: typing.Any = 0

class ItemSpecialBonusRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class ItemStainConditionRow(ExdRow):
    UnlockQuest: typing.Any = 0

class ItemUICategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Icon: typing.Any = 1
    OrderMinor: typing.Any = 2
    OrderMajor: typing.Any = 3

class JigsawScoreRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class JigsawTimeBonusRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21

class JingleRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class JobHudManualRow(ExdRow):
    _display_field: str = 'Action'

    Action: typing.Any = 0
    Unknown0: typing.Any = 1
    Guide: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown_70: typing.Any = 4
    Unknown2: typing.Any = 5
    Unknown3: typing.Any = 6

class JobHudManualPriorityRow(ExdRow):
    JobHudManual0: typing.Any = 0
    JobHudManual1: typing.Any = 1
    JobHudManual2: typing.Any = 2
    JobHudManual3: typing.Any = 3
    JobHudManual4: typing.Any = 4
    JobHudManual5: typing.Any = 5
    JobHudManual6: typing.Any = 6
    JobHudManual7: typing.Any = 7

class JournalCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    SeparateType: typing.Any = 1
    DataType: typing.Any = 2
    JournalSection: typing.Any = 3
    MapCondition: typing.Any = 4

class JournalGenreRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Icon: typing.Any = 1
    JournalCategory: typing.Any = 2
    Unknown0: typing.Any = 3

class JournalSectionRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2

class KineDriverOffGroupRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class KnockbackRow(ExdRow):
    Distance: typing.Any = 0
    Speed: typing.Any = 1
    NearDistance: typing.Any = 2
    Direction: typing.Any = 3
    DirectionArg: typing.Any = 4
    Motion: typing.Any = 5
    CancelMove: typing.Any = 6

class LFGExtensionContentRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class LegacyQuestRow(ExdRow):
    Text: typing.Any = 0
    String: typing.Any = 1
    Genre: typing.Any = 2
    LegacyQuestID: typing.Any = 3
    SortKey: typing.Any = 4

class LeveRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    ExpFactor: typing.Any = 2
    ExpReward: typing.Any = 3
    GilReward: typing.Any = 4
    LeveRewardItem: typing.Any = 5
    JournalGenre: typing.Any = 6
    LevelLevemete: typing.Any = 7
    LevelStart: typing.Any = 8
    LeveClient: typing.Any = 9
    LeveAssignmentType: typing.Any = 10
    Town: typing.Any = 11
    PlaceNameStart: typing.Any = 12
    PlaceNameIssued: typing.Any = 13
    PlaceNameStartZone: typing.Any = 14
    IconCityState: typing.Any = 15
    DataId: typing.Any = 16
    IconIssuer: typing.Any = 17
    ClassJobLevel: typing.Any = 18
    FishingSpot: typing.Any = 19
    BGM: typing.Any = 20
    Unknown1: typing.Any = 21
    TimeLimit: typing.Any = 22
    AllowanceCost: typing.Any = 23
    Unknown2: typing.Any = 24
    ClassJobCategory: typing.Any = 25
    MaxDifficulty: typing.Any = 26
    LeveVfx: typing.Any = 27
    LeveVfxFrame: typing.Any = 28
    CanCancel: typing.Any = 29
    LockedLeve: typing.Any = 30

class LeveAssignmentTypeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Icon: typing.Any = 1

class LeveClientRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class LeveRewardItemRow(ExdRow):
    LeveRewardItemGroup0: typing.Any = 0
    LeveRewardItemGroup1: typing.Any = 1
    LeveRewardItemGroup2: typing.Any = 2
    LeveRewardItemGroup3: typing.Any = 3
    LeveRewardItemGroup4: typing.Any = 4
    LeveRewardItemGroup5: typing.Any = 5
    LeveRewardItemGroup6: typing.Any = 6
    LeveRewardItemGroup7: typing.Any = 7
    ProbabilityPercent0: typing.Any = 8
    ProbabilityPercent1: typing.Any = 9
    ProbabilityPercent2: typing.Any = 10
    ProbabilityPercent3: typing.Any = 11
    ProbabilityPercent4: typing.Any = 12
    ProbabilityPercent5: typing.Any = 13
    ProbabilityPercent6: typing.Any = 14
    ProbabilityPercent7: typing.Any = 15

class LeveRewardItemGroupRow(ExdRow):
    Item0: typing.Any = 0
    Item1: typing.Any = 1
    Item2: typing.Any = 2
    Item3: typing.Any = 3
    Item4: typing.Any = 4
    Item5: typing.Any = 5
    Item6: typing.Any = 6
    Item7: typing.Any = 7
    Item8: typing.Any = 8
    Count0: typing.Any = 9
    Count1: typing.Any = 10
    Count2: typing.Any = 11
    Count3: typing.Any = 12
    Count4: typing.Any = 13
    Count5: typing.Any = 14
    Count6: typing.Any = 15
    Count7: typing.Any = 16
    Count8: typing.Any = 17
    IsHQ0: typing.Any = 18
    IsHQ1: typing.Any = 19
    IsHQ2: typing.Any = 20
    IsHQ3: typing.Any = 21
    IsHQ4: typing.Any = 22
    IsHQ5: typing.Any = 23
    IsHQ6: typing.Any = 24
    IsHQ7: typing.Any = 25
    IsHQ8: typing.Any = 26

class LeveStringRow(ExdRow):
    _display_field: str = 'Objective'

    Objective: typing.Any = 0

class LeveSystemDefineRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class LeveVfxRow(ExdRow):
    _display_field: str = 'Icon'

    Effect: typing.Any = 0
    Icon: typing.Any = 1

class LevelRow(ExdRow):
    X: typing.Any = 0
    Y: typing.Any = 1
    Z: typing.Any = 2
    Yaw: typing.Any = 3
    Radius: typing.Any = 4
    Object: typing.Any = 5
    EventId: typing.Any = 6
    Map: typing.Any = 7
    Territory: typing.Any = 8
    Type: typing.Any = 9

class LinkRaceRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class LiveMinigamesRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class LiveMinigamesTerritoryTypeRow(ExdRow):
    Unknown0: typing.Any = 0

class LivelyActorGroupRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class LoadingImageRow(ExdRow):
    FileName: typing.Any = 0

class LoadingTipsRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class LoadingTipsSubRow(ExdRow):
    Unknown0: typing.Any = 0

class LobbyRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2
    TYPE: typing.Any = 3
    PARAM: typing.Any = 4
    LINK: typing.Any = 5

class LockonRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class LogFilterRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Example: typing.Any = 1
    Caster: typing.Any = 2
    Target: typing.Any = 3
    LogKind: typing.Any = 4
    Category: typing.Any = 5
    DisplayOrder: typing.Any = 6
    Preset: typing.Any = 7

class LogKindRow(ExdRow):
    Format: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown1: typing.Any = 3

class LogMessageRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0
    LogKind: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown_70: typing.Any = 4
    Unknown2: typing.Any = 5

class LootModeTypeRow(ExdRow):
    Unknown0: typing.Any = 0

class LotteryExchangeShopRow(ExdRow):
    Name: typing.Any = 0
    LotteryExchangeParams0: typing.Any = 1
    LotteryExchangeParams1: typing.Any = 2
    LotteryExchangeParams2: typing.Any = 3
    LotteryExchangeParams3: typing.Any = 4
    LotteryExchangeParams4: typing.Any = 5
    LotteryExchangeParams5: typing.Any = 6
    LotteryExchangeParams6: typing.Any = 7
    LotteryExchangeParams7: typing.Any = 8
    LotteryExchangeParams8: typing.Any = 9
    LotteryExchangeParams9: typing.Any = 10
    LotteryExchangeParams10: typing.Any = 11
    LotteryExchangeParams11: typing.Any = 12
    LotteryExchangeParams12: typing.Any = 13
    LotteryExchangeParams13: typing.Any = 14
    LotteryExchangeParams14: typing.Any = 15
    LotteryExchangeParams15: typing.Any = 16
    LotteryExchangeParams16: typing.Any = 17
    LotteryExchangeParams17: typing.Any = 18
    LotteryExchangeParams18: typing.Any = 19
    LotteryExchangeParams19: typing.Any = 20
    LotteryExchangeParams20: typing.Any = 21
    LotteryExchangeParams21: typing.Any = 22
    LotteryExchangeParams22: typing.Any = 23
    LotteryExchangeParams23: typing.Any = 24
    LotteryExchangeParams24: typing.Any = 25
    LotteryExchangeParams25: typing.Any = 26
    LotteryExchangeParams26: typing.Any = 27
    LotteryExchangeParams27: typing.Any = 28
    LotteryExchangeParams28: typing.Any = 29
    LotteryExchangeParams29: typing.Any = 30
    LotteryExchangeParams30: typing.Any = 31
    LotteryExchangeParams31: typing.Any = 32
    Script: typing.Any = 33
    LogMessage0: typing.Any = 34
    LogMessage1: typing.Any = 35
    LogMessage2: typing.Any = 36
    Unknown0: typing.Any = 37

class MJIAnimalsRow(ExdRow):
    BNpcBase: typing.Any = 0
    Reward0: typing.Any = 1
    Reward1: typing.Any = 2
    Icon: typing.Any = 3
    Size: typing.Any = 4
    Unknown0: typing.Any = 5
    Unknown1: typing.Any = 6

class MJIBuildingRow(ExdRow):
    Name: typing.Any = 0
    Unknown0: typing.Any = 1
    Icon: typing.Any = 2
    Sgb0: typing.Any = 3
    Sgb1: typing.Any = 4
    Sgb2: typing.Any = 5
    Sgb3: typing.Any = 6
    Sgb4: typing.Any = 7
    Unknown1: typing.Any = 8
    Unknown2: typing.Any = 9
    Unknown3: typing.Any = 10
    Unknown4: typing.Any = 11
    Unknown5: typing.Any = 12
    Unknown6: typing.Any = 13
    Unknown7: typing.Any = 14
    Unknown8: typing.Any = 15
    Unknown9: typing.Any = 16
    Unknown10: typing.Any = 17
    Unknown11: typing.Any = 18
    Unknown12: typing.Any = 19
    Unknown13: typing.Any = 20
    Unknown14: typing.Any = 21
    Material0: typing.Any = 22
    Material1: typing.Any = 23
    Material2: typing.Any = 24
    Material3: typing.Any = 25
    Material4: typing.Any = 26
    Amount0: typing.Any = 27
    Amount1: typing.Any = 28
    Amount2: typing.Any = 29
    Amount3: typing.Any = 30
    Amount4: typing.Any = 31

class MJIBuildingPlaceRow(ExdRow):
    Unknown0: typing.Any = 0
    Name: typing.Any = 1
    SGB: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown2: typing.Any = 4
    Unknown3: typing.Any = 5

class MJICraftworksObjectRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0
    Theme0: typing.Any = 1
    Theme1: typing.Any = 2
    Unknown0: typing.Any = 3
    Material0: typing.Any = 4
    Material1: typing.Any = 5
    Material2: typing.Any = 6
    Material3: typing.Any = 7
    Amount0: typing.Any = 8
    Amount1: typing.Any = 9
    Amount2: typing.Any = 10
    Amount3: typing.Any = 11
    LevelReq: typing.Any = 12
    CraftingTime: typing.Any = 13
    Value: typing.Any = 14

class MJICraftworksObjectThemeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class MJICraftworksPopularityRow(ExdRow):
    Popularity0: typing.Any = 0
    Popularity1: typing.Any = 1
    Popularity2: typing.Any = 2
    Popularity3: typing.Any = 3
    Popularity4: typing.Any = 4
    Popularity5: typing.Any = 5
    Popularity6: typing.Any = 6
    Popularity7: typing.Any = 7
    Popularity8: typing.Any = 8
    Popularity9: typing.Any = 9
    Popularity10: typing.Any = 10
    Popularity11: typing.Any = 11
    Popularity12: typing.Any = 12
    Popularity13: typing.Any = 13
    Popularity14: typing.Any = 14
    Popularity15: typing.Any = 15
    Popularity16: typing.Any = 16
    Popularity17: typing.Any = 17
    Popularity18: typing.Any = 18
    Popularity19: typing.Any = 19
    Popularity20: typing.Any = 20
    Popularity21: typing.Any = 21
    Popularity22: typing.Any = 22
    Popularity23: typing.Any = 23
    Popularity24: typing.Any = 24
    Popularity25: typing.Any = 25
    Popularity26: typing.Any = 26
    Popularity27: typing.Any = 27
    Popularity28: typing.Any = 28
    Popularity29: typing.Any = 29
    Popularity30: typing.Any = 30
    Popularity31: typing.Any = 31
    Popularity32: typing.Any = 32
    Popularity33: typing.Any = 33
    Popularity34: typing.Any = 34
    Popularity35: typing.Any = 35
    Popularity36: typing.Any = 36
    Popularity37: typing.Any = 37
    Popularity38: typing.Any = 38
    Popularity39: typing.Any = 39
    Popularity40: typing.Any = 40
    Popularity41: typing.Any = 41
    Popularity42: typing.Any = 42
    Popularity43: typing.Any = 43
    Popularity44: typing.Any = 44
    Popularity45: typing.Any = 45
    Popularity46: typing.Any = 46
    Popularity47: typing.Any = 47
    Popularity48: typing.Any = 48
    Popularity49: typing.Any = 49
    Popularity50: typing.Any = 50
    Popularity51: typing.Any = 51
    Popularity52: typing.Any = 52
    Popularity53: typing.Any = 53
    Popularity54: typing.Any = 54
    Popularity55: typing.Any = 55
    Popularity56: typing.Any = 56
    Popularity57: typing.Any = 57
    Popularity58: typing.Any = 58
    Popularity59: typing.Any = 59
    Popularity60: typing.Any = 60
    Popularity61: typing.Any = 61
    Popularity62: typing.Any = 62
    Popularity63: typing.Any = 63
    Popularity64: typing.Any = 64
    Popularity65: typing.Any = 65
    Popularity66: typing.Any = 66
    Popularity67: typing.Any = 67
    Popularity68: typing.Any = 68
    Popularity69: typing.Any = 69
    Popularity70: typing.Any = 70
    Popularity71: typing.Any = 71
    Popularity72: typing.Any = 72
    Popularity73: typing.Any = 73
    Popularity74: typing.Any = 74
    Popularity75: typing.Any = 75
    Popularity76: typing.Any = 76
    Popularity77: typing.Any = 77
    Popularity78: typing.Any = 78
    Popularity79: typing.Any = 79
    Popularity80: typing.Any = 80
    Popularity81: typing.Any = 81
    Popularity82: typing.Any = 82
    Popularity83: typing.Any = 83
    Popularity84: typing.Any = 84
    Popularity85: typing.Any = 85
    Popularity86: typing.Any = 86
    Popularity87: typing.Any = 87
    Popularity88: typing.Any = 88
    Popularity89: typing.Any = 89
    Popularity90: typing.Any = 90

class MJICraftworksPopularityTypeRow(ExdRow):
    _display_field: str = 'Ratio'

    Ratio: typing.Any = 0

class MJICraftworksRankRatioRow(ExdRow):
    Ratio: typing.Any = 0

class MJICraftworksSupplyDefineRow(ExdRow):
    Ratio: typing.Any = 0
    Supply: typing.Any = 1

class MJICraftworksTensionRow(ExdRow):
    Unknown0: typing.Any = 0

class MJICropSeedRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0
    Name: typing.Any = 1
    SGB: typing.Any = 2

class MJIDisposalShopItemRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Category: typing.Any = 3
    Unknown3: typing.Any = 4

class MJIDisposalShopUICategoryRow(ExdRow):
    _display_field: str = 'Category'

    Category: typing.Any = 0

class MJIFarmPastureRankRow(ExdRow):
    RankData0: typing.Any = 0
    RankData1: typing.Any = 1
    RankData2: typing.Any = 2
    RankData3: typing.Any = 3

class MJIFunctionRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class MJIGardenscapingRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Item: typing.Any = 3
    Unknown3: typing.Any = 4
    Unknown4: typing.Any = 5
    Unknown5: typing.Any = 6
    Unknown6: typing.Any = 7
    Level: typing.Any = 8

class MJIGatheringRow(ExdRow):
    _display_field: str = 'GatheringObject'

    GatheringObject: typing.Any = 0

class MJIGatheringItemRow(ExdRow):
    _display_field: str = 'Item'

    Radius: typing.Any = 0
    X: typing.Any = 1
    Y: typing.Any = 2
    Unknown0: typing.Any = 3
    Unknown1: typing.Any = 4
    Item: typing.Any = 5
    Sort: typing.Any = 6

class MJIGatheringObjectRow(ExdRow):
    _display_field: str = 'Name'

    MapIcon: typing.Any = 0
    Unknown0: typing.Any = 1
    Name: typing.Any = 2
    SGB: typing.Any = 3
    Unknown1: typing.Any = 4

class MJIGatheringToolRow(ExdRow):
    Unknown0: typing.Any = 0

class MJIHudModeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Title: typing.Any = 1
    Icon: typing.Any = 2
    Unknown0: typing.Any = 3

class MJIItemCategoryRow(ExdRow):
    _display_field: str = 'Singular'

    Singular: typing.Any = 0
    Plural: typing.Any = 1

class MJIItemPouchRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0
    Category: typing.Any = 1
    Crop: typing.Any = 2
    Unknown0: typing.Any = 3

class MJIKeyItemRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0
    Unknown0: typing.Any = 1

class MJILandmarkRow(ExdRow):
    Name: typing.Any = 0
    Icon: typing.Any = 1
    UnlockLink: typing.Any = 2
    SGB0: typing.Any = 3
    SGB1: typing.Any = 4
    SGB2: typing.Any = 5
    SGB3: typing.Any = 6
    SGB4: typing.Any = 7
    SGB5: typing.Any = 8
    SGB6: typing.Any = 9
    Material0: typing.Any = 10
    Material1: typing.Any = 11
    Material2: typing.Any = 12
    Material3: typing.Any = 13
    Material4: typing.Any = 14
    Unknown1: typing.Any = 15
    Unknown2: typing.Any = 16
    Unknown3: typing.Any = 17
    Unknown4: typing.Any = 18
    Unknown5: typing.Any = 19
    Unknown6: typing.Any = 20
    Unknown7: typing.Any = 21
    Unknown8: typing.Any = 22
    Unknown9: typing.Any = 23
    Unknown10: typing.Any = 24
    Unknown11: typing.Any = 25
    Unknown12: typing.Any = 26
    Unknown13: typing.Any = 27
    Amount0: typing.Any = 28
    Amount1: typing.Any = 29
    Amount2: typing.Any = 30
    Amount3: typing.Any = 31
    Amount4: typing.Any = 32

class MJILandmarkPlaceRow(ExdRow):
    Unknown0: typing.Any = 0
    Name: typing.Any = 1
    SGB0: typing.Any = 2
    SGB1: typing.Any = 3
    Unknown1: typing.Any = 4
    Unknown2: typing.Any = 5
    Unknown3: typing.Any = 6

class MJILivelyActorRow(ExdRow):
    X: typing.Any = 0
    Y: typing.Any = 1
    Z: typing.Any = 2
    Rot: typing.Any = 3
    ENPC: typing.Any = 4
    Behavior: typing.Any = 5

class MJIMinionPopAreasRow(ExdRow):
    Text: typing.Any = 0
    X: typing.Any = 1
    Y: typing.Any = 2
    RequiredFunction: typing.Any = 3
    Unknown4: typing.Any = 4

class MJINameRow(ExdRow):
    _display_field: str = 'Singular'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Adjective: typing.Any = 2
    PossessivePronoun: typing.Any = 3
    StartsWithVowel: typing.Any = 4
    Unknown0: typing.Any = 5
    Pronoun: typing.Any = 6
    Article: typing.Any = 7

class MJINekomimiRequestRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class MJIProgressRow(ExdRow):
    Vision: typing.Any = 0
    Objective: typing.Any = 1
    PreviousObjective: typing.Any = 2
    Unknown0: typing.Any = 3
    Unknown1: typing.Any = 4
    Unknown2: typing.Any = 5
    Unknown3: typing.Any = 6
    Unknown4: typing.Any = 7
    Unknown5: typing.Any = 8
    Unknown6: typing.Any = 9
    Unknown7: typing.Any = 10
    Unknown8: typing.Any = 11
    Unknown9: typing.Any = 12
    Unknown10: typing.Any = 13
    Unknown11: typing.Any = 14
    Unknown12: typing.Any = 15
    Unknown13: typing.Any = 16
    Unknown14: typing.Any = 17
    Unknown15: typing.Any = 18
    Unknown16: typing.Any = 19
    Unknown17: typing.Any = 20
    Unknown18: typing.Any = 21
    Unknown19: typing.Any = 22

class MJIRankRow(ExdRow):
    ExpToNext: typing.Any = 0
    LogMessage0: typing.Any = 1
    LogMessage1: typing.Any = 2
    LogMessage2: typing.Any = 3
    Unknown0: typing.Any = 4

class MJIRecipeRow(ExdRow):
    _display_field: str = 'KeyItem'

    LogMessage: typing.Any = 0
    KeyItem: typing.Any = 1
    ItemPouch: typing.Any = 2
    Yield: typing.Any = 3
    Material0: typing.Any = 4
    Material1: typing.Any = 5
    Material2: typing.Any = 6
    Material3: typing.Any = 7
    Material4: typing.Any = 8
    Amount0: typing.Any = 9
    Amount1: typing.Any = 10
    Amount2: typing.Any = 11
    Amount3: typing.Any = 12
    Amount4: typing.Any = 13
    Order: typing.Any = 14

class MJIRecipeMaterialRow(ExdRow):
    _display_field: str = 'ItemPouch'

    ItemPouch: typing.Any = 0
    Unknown0: typing.Any = 1

class MJIStockyardManagementAreaRow(ExdRow):
    _display_field: str = 'Area'

    Area: typing.Any = 0
    RareMaterial: typing.Any = 1
    Unknown0: typing.Any = 2

class MJIStockyardManagementTableRow(ExdRow):
    _display_field: str = 'Material'

    Material: typing.Any = 0

class MJITextRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0

class MJIVillageAppearanceSGRow(ExdRow):
    VillageAppearanceData0: typing.Any = 0
    VillageAppearanceData1: typing.Any = 1
    VillageAppearanceData2: typing.Any = 2
    VillageAppearanceData3: typing.Any = 3
    VillageAppearanceData4: typing.Any = 4

class MJIVillageAppearanceUIRow(ExdRow):
    Floor: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2

class MJIVillageDevelopmentRow(ExdRow):
    ENPC: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2
    Unknown2: typing.Any = 3
    Unknown3: typing.Any = 4
    Unknown4: typing.Any = 5
    Behavior0: typing.Any = 6
    Behavior1: typing.Any = 7
    Unknown5: typing.Any = 8
    Unknown6: typing.Any = 9
    Unknown7: typing.Any = 10
    Unknown8: typing.Any = 11
    Unknown9: typing.Any = 12
    Unknown10: typing.Any = 13
    Unknown11: typing.Any = 14

class MKDBNpcDataRow(ExdRow):
    Unknown0: typing.Any = 0

class MKDChainRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class MKDDataRow(ExdRow):
    Quest: typing.Any = 0
    ZoneName: typing.Any = 1
    CurrencyItem0: typing.Any = 2
    CurrencyItem1: typing.Any = 3
    CipherItem: typing.Any = 4
    CurrencyName0: typing.Any = 5
    CurrencyName1: typing.Any = 6
    CipherName: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9

class MKDGrowDataRow(ExdRow):
    Unknown0: typing.Any = 0

class MKDGrowDataSJobRow(ExdRow):
    Unknown0: typing.Any = 0

class MKDLoreRow(ExdRow):
    Name: typing.Any = 0
    Description: typing.Any = 1
    Unknown2: typing.Any = 2
    Image: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6

class MKDSupportJobRow(ExdRow):
    Name: typing.Any = 0
    NameShort: typing.Any = 1
    NameFemale: typing.Any = 2
    Description: typing.Any = 3
    NameEnglish: typing.Any = 4
    Action0: typing.Any = 5
    Action1: typing.Any = 6
    Action2: typing.Any = 7
    Action3: typing.Any = 8
    Action4: typing.Any = 9
    LevelMax: typing.Any = 10
    JobIndex: typing.Any = 11
    LevelUnlock0: typing.Any = 12
    LevelUnlock1: typing.Any = 13
    LevelUnlock2: typing.Any = 14
    LevelUnlock3: typing.Any = 15
    LevelUnlock4: typing.Any = 16

class MKDTraitRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class MYCTemporaryItemRow(ExdRow):
    _display_field: str = 'Action'

    Action: typing.Any = 0
    Category: typing.Any = 1
    Type: typing.Any = 2
    Max: typing.Any = 3
    Weight: typing.Any = 4
    Order: typing.Any = 5

class MYCTemporaryItemUICategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Unknown0: typing.Any = 1

class MYCWarResultNotebookRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    NameJP: typing.Any = 2
    Quest: typing.Any = 3
    Unknown0: typing.Any = 4
    Icon: typing.Any = 5
    Image: typing.Any = 6
    Number: typing.Any = 7
    Unknown1: typing.Any = 8
    Link: typing.Any = 9
    Rarity: typing.Any = 10

class MacroIconRow(ExdRow):
    _display_field: str = 'Icon'

    Icon: typing.Any = 0
    Unknown0: typing.Any = 1

class MacroIconRedirectOldRow(ExdRow):
    IconOld: typing.Any = 0
    IconNew: typing.Any = 1

class MainCommandRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Icon: typing.Any = 2
    Category: typing.Any = 3
    MainCommandCategory: typing.Any = 4
    Unknown0: typing.Any = 5
    SortID: typing.Any = 6

class MainCommandCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Unknown0: typing.Any = 1

class MandervilleWeaponEnhanceRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15

class ManeuversRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class ManeuversArmorRow(ExdRow):
    Name: typing.Any = 0
    Description: typing.Any = 1
    FalconName: typing.Any = 2
    RavenName: typing.Any = 3
    NeutralMapIcon: typing.Any = 4
    FalconImage: typing.Any = 5
    RavenImage: typing.Any = 6
    FalconMapImage: typing.Any = 7
    RavenMapImage: typing.Any = 8
    Unknown0: typing.Any = 9
    Unknown1: typing.Any = 10
    Unknown2: typing.Any = 11

class MapRow(ExdRow):
    _display_field: str = 'PlaceName'

    Id: typing.Any = 0
    DiscoveryFlag: typing.Any = 1
    MapMarkerRange: typing.Any = 2
    SizeFactor: typing.Any = 3
    PlaceNameRegion: typing.Any = 4
    PlaceName: typing.Any = 5
    PlaceNameSub: typing.Any = 6
    TerritoryType: typing.Any = 7
    OffsetX: typing.Any = 8
    OffsetY: typing.Any = 9
    DiscoveryIndex: typing.Any = 10
    MapCondition: typing.Any = 11
    PriorityCategoryUI: typing.Any = 12
    PriorityUI: typing.Any = 13
    Hierarchy: typing.Any = 14
    Unknown2: typing.Any = 15
    Unknown0: typing.Any = 16
    MapIndex: typing.Any = 17
    DiscoveryArrayByte: typing.Any = 18
    IsEvent: typing.Any = 19
    Unknown1: typing.Any = 20

class MapConditionRow(ExdRow):
    _display_field: str = 'Quest'

    Quest: typing.Any = 0
    InstanceContent: typing.Any = 1
    QuestSequence: typing.Any = 2

class MapExclusiveRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class MapMarkerRow(ExdRow):
    Icon: typing.Any = 0
    PlaceNameSubtext: typing.Any = 1
    DataKey: typing.Any = 2
    X: typing.Any = 3
    Y: typing.Any = 4
    SubtextOrientation: typing.Any = 5
    MapMarkerRegion: typing.Any = 6
    Type: typing.Any = 7
    DataType: typing.Any = 8
    Unknown0: typing.Any = 9
    Unknown1: typing.Any = 10

class MapMarkerRegionRow(ExdRow):
    _display_field: str = 'X'

    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    X: typing.Any = 4
    Unknown4: typing.Any = 5
    Unknown5: typing.Any = 6
    Unknown6: typing.Any = 7
    Unknown7: typing.Any = 8
    Unknown8: typing.Any = 9
    Unknown9: typing.Any = 10
    Unknown10: typing.Any = 11

class MapReplaceRow(ExdRow):
    Quest: typing.Any = 0
    Map: typing.Any = 1
    TerritoryType: typing.Any = 2
    Unknown4: typing.Any = 3
    Unknown7: typing.Any = 4
    Unknown8: typing.Any = 5
    Unknown5: typing.Any = 6
    Unknown6: typing.Any = 7
    QuestSequence: typing.Any = 8

class MapSymbolRow(ExdRow):
    Icon: typing.Any = 0
    PlaceName: typing.Any = 1
    DisplayNavi: typing.Any = 2

class MapTransientPvPMapRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class MapTypeRow(ExdRow):
    Unknown0: typing.Any = 0

class MarkerRow(ExdRow):
    Name: typing.Any = 0
    Icon: typing.Any = 1
    SortOrder: typing.Any = 2

class MassivePcContentRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown8: typing.Any = 3
    Unknown9: typing.Any = 4
    Unknown10: typing.Any = 5
    Unknown11: typing.Any = 6
    Unknown3: typing.Any = 7
    Unknown4: typing.Any = 8
    Unknown5: typing.Any = 9
    Unknown6: typing.Any = 10
    Unknown7: typing.Any = 11

class MassivePcContentBattleTalkRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6

class MassivePcContentTextDataRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0

class MassivePcContentTodoRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class MateAuthorityCategoryRow(ExdRow):
    Unknown0: typing.Any = 0

class MateriaRow(ExdRow):
    Item0: typing.Any = 0
    Item1: typing.Any = 1
    Item2: typing.Any = 2
    Item3: typing.Any = 3
    Item4: typing.Any = 4
    Item5: typing.Any = 5
    Item6: typing.Any = 6
    Item7: typing.Any = 7
    Item8: typing.Any = 8
    Item9: typing.Any = 9
    Item10: typing.Any = 10
    Item11: typing.Any = 11
    Item12: typing.Any = 12
    Item13: typing.Any = 13
    Item14: typing.Any = 14
    Item15: typing.Any = 15
    Value0: typing.Any = 16
    Value1: typing.Any = 17
    Value2: typing.Any = 18
    Value3: typing.Any = 19
    Value4: typing.Any = 20
    Value5: typing.Any = 21
    Value6: typing.Any = 22
    Value7: typing.Any = 23
    Value8: typing.Any = 24
    Value9: typing.Any = 25
    Value10: typing.Any = 26
    Value11: typing.Any = 27
    Value12: typing.Any = 28
    Value13: typing.Any = 29
    Value14: typing.Any = 30
    Value15: typing.Any = 31
    BaseParam: typing.Any = 32

class MateriaGradeRow(ExdRow):
    MeldFee: typing.Any = 0
    ReturnRate: typing.Any = 1
    OvermeldNQPercent0: typing.Any = 2
    OvermeldNQPercent1: typing.Any = 3
    OvermeldNQPercent2: typing.Any = 4
    OvermeldNQPercent3: typing.Any = 5
    OvermeldHQPercent0: typing.Any = 6
    OvermeldHQPercent1: typing.Any = 7
    OvermeldHQPercent2: typing.Any = 8
    OvermeldHQPercent3: typing.Any = 9

class MateriaJoinRateRow(ExdRow):
    NQOvermeldPercentSlot0: typing.Any = 0
    NQOvermeldPercentSlot1: typing.Any = 1
    NQOvermeldPercentSlot2: typing.Any = 2
    NQOvermeldPercentSlot3: typing.Any = 3
    HQOvermeldPercentSlot0: typing.Any = 4
    HQOvermeldPercentSlot1: typing.Any = 5
    HQOvermeldPercentSlot2: typing.Any = 6
    HQOvermeldPercentSlot3: typing.Any = 7

class MateriaJoinRateGatherCraftRow(ExdRow):
    NQOvermeldPercentSlot0: typing.Any = 0
    NQOvermeldPercentSlot1: typing.Any = 1
    NQOvermeldPercentSlot2: typing.Any = 2
    NQOvermeldPercentSlot3: typing.Any = 3
    HQOvermeldPercentSlot0: typing.Any = 4
    HQOvermeldPercentSlot1: typing.Any = 5
    HQOvermeldPercentSlot2: typing.Any = 6
    HQOvermeldPercentSlot3: typing.Any = 7

class MateriaParamRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15

class McGuffinRow(ExdRow):
    UIData: typing.Any = 0

class McGuffinUIDataRow(ExdRow):
    Name: typing.Any = 0
    Icon: typing.Any = 1
    Order: typing.Any = 2

class MiniGameRARow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Icon: typing.Any = 2
    Image: typing.Any = 3
    BGM: typing.Any = 4
    Unknown2: typing.Any = 5
    Unknown3: typing.Any = 6
    Unknown4: typing.Any = 7
    Unknown5: typing.Any = 8
    Unknown6: typing.Any = 9
    Unknown7: typing.Any = 10
    Unknown8: typing.Any = 11
    Unknown9: typing.Any = 12
    Unknown10: typing.Any = 13
    Unknown11: typing.Any = 14
    Unknown12: typing.Any = 15
    Unknown13: typing.Any = 16
    Unknown14: typing.Any = 17
    Unknown15: typing.Any = 18
    Unknown16: typing.Any = 19
    Unknown17: typing.Any = 20
    Unknown18: typing.Any = 21

class MiniGameRANotesRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6

class MiniGameTurnBreakActionRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9

class MiniGameTurnBreakConstRow(ExdRow):
    Unknown0: typing.Any = 0

class MiniGameTurnBreakEnemyRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown24: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    Unknown27: typing.Any = 27
    Unknown28: typing.Any = 28
    Unknown29: typing.Any = 29
    Unknown30: typing.Any = 30
    Unknown31: typing.Any = 31
    Unknown32: typing.Any = 32
    Unknown33: typing.Any = 33
    Unknown34: typing.Any = 34

class MiniGameTurnBreakPopRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class MiniGameTurnBreakPopOffsetRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7

class MiniGameTurnBreakStageRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9

class MiniGameTurnBreakStatusRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class MinionRaceRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class MinionRulesRow(ExdRow):
    _display_field: str = 'Rule'

    Rule: typing.Any = 0
    Description: typing.Any = 1

class MinionSkillTypeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class MinionStageRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class MirageStoreSetItemRow(ExdRow):
    MainHand: typing.Any = 0
    OffHand: typing.Any = 1
    Head: typing.Any = 2
    Body: typing.Any = 3
    Hands: typing.Any = 4
    Legs: typing.Any = 5
    Feet: typing.Any = 6
    Earrings: typing.Any = 7
    Necklace: typing.Any = 8
    Bracelets: typing.Any = 9
    Ring: typing.Any = 10

class MirageStoreSetItemLookupRow(ExdRow):
    Item0: typing.Any = 0
    Item1: typing.Any = 1
    Item2: typing.Any = 2
    Item3: typing.Any = 3
    Item4: typing.Any = 4

class MobHuntOrderRow(ExdRow):
    Target: typing.Any = 0
    NeededKills: typing.Any = 1
    Type: typing.Any = 2
    Rank: typing.Any = 3
    MobHuntReward: typing.Any = 4

class MobHuntOrderTypeRow(ExdRow):
    Quest: typing.Any = 0
    EventItem: typing.Any = 1
    OrderStart: typing.Any = 2
    Type: typing.Any = 3
    OrderAmount: typing.Any = 4

class MobHuntRewardRow(ExdRow):
    ExpReward: typing.Any = 0
    GilReward: typing.Any = 1
    CurrencyReward: typing.Any = 2
    Expansion: typing.Any = 3

class MobHuntRewardCapRow(ExdRow):
    ExpCap: typing.Any = 0

class MobHuntTargetRow(ExdRow):
    _display_field: str = 'Name'

    Icon: typing.Any = 0
    Name: typing.Any = 1
    FATE: typing.Any = 2
    TerritoryType: typing.Any = 3
    PlaceName: typing.Any = 4

class ModelAttributeRow(ExdRow):
    Unknown0: typing.Any = 0

class ModelCharaRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown15: typing.Any = 2
    Model: typing.Any = 3
    SEPack: typing.Any = 4
    Type: typing.Any = 5
    Base: typing.Any = 6
    Variant: typing.Any = 7
    Unknown2: typing.Any = 8
    Unknown3: typing.Any = 9
    Unknown4: typing.Any = 10
    Unknown5: typing.Any = 11
    Unknown14: typing.Any = 12
    Unknown_70: typing.Any = 13
    Unknown6: typing.Any = 14
    Unknown7: typing.Any = 15
    PapVariation: typing.Any = 16
    Unknown8: typing.Any = 17
    Unknown9: typing.Any = 18
    Unknown10: typing.Any = 19
    Unknown11: typing.Any = 20
    Unknown12: typing.Any = 21
    Unknown13: typing.Any = 22

class ModelScaleRow(ExdRow):
    Unknown0: typing.Any = 0

class ModelSkeletonRow(ExdRow):
    Radius: typing.Any = 0
    Height: typing.Any = 1
    VFXScale: typing.Any = 2
    FloatHeight: typing.Any = 3
    FloatDown: typing.Any = 4
    Unknown0: typing.Any = 5
    Unknown1: typing.Any = 6
    Unknown2: typing.Any = 7
    Unknown3: typing.Any = 8
    Unknown4: typing.Any = 9
    Unknown5: typing.Any = 10
    Unknown6: typing.Any = 11
    Unknown7: typing.Any = 12
    FloatUp: typing.Any = 13
    Unknown8: typing.Any = 14
    LoopFlySE: typing.Any = 15
    MotionBlendType: typing.Any = 16

class ModelStateRow(ExdRow):
    _display_field: str = 'Start'

    Start: typing.Any = 0
    Unknown0: typing.Any = 1

class MonsterNoteRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Reward: typing.Any = 1
    MonsterNoteTarget0: typing.Any = 2
    MonsterNoteTarget1: typing.Any = 3
    MonsterNoteTarget2: typing.Any = 4
    MonsterNoteTarget3: typing.Any = 5
    Count0: typing.Any = 6
    Count1: typing.Any = 7
    Count2: typing.Any = 8
    Count3: typing.Any = 9

class MonsterNoteTargetRow(ExdRow):
    _display_field: str = 'BNpcName'

    Icon: typing.Any = 0
    BNpcName: typing.Any = 1
    PlaceNameZone0: typing.Any = 2
    PlaceNameZone1: typing.Any = 3
    PlaceNameZone2: typing.Any = 4
    PlaceNameLocation0: typing.Any = 5
    PlaceNameLocation1: typing.Any = 6
    PlaceNameLocation2: typing.Any = 7
    Town: typing.Any = 8

class MotionTimelineRow(ExdRow):
    Filename: typing.Any = 0
    BlendGroup: typing.Any = 1
    Unknown_70_1: typing.Any = 2
    Unknown_70_2: typing.Any = 3
    IsLoop: typing.Any = 4
    IsBlinkEnable: typing.Any = 5
    IsLipEnable: typing.Any = 6
    Unknown0: typing.Any = 7

class MotionTimelineAdvanceBlendRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class MotionTimelineBlendTableRow(ExdRow):
    DestBlendGroup: typing.Any = 0
    SrcBlendGroup: typing.Any = 1
    BlendFrame_PC: typing.Any = 2
    BlendFram_TypeA: typing.Any = 3
    BlendFram_TypeB: typing.Any = 4
    BlendFram_TypeC: typing.Any = 5

class MountRow(ExdRow):
    _display_field: str = 'Singular'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Adjective: typing.Any = 2
    PossessivePronoun: typing.Any = 3
    StartsWithVowel: typing.Any = 4
    Unknown0: typing.Any = 5
    Pronoun: typing.Any = 6
    Article: typing.Any = 7
    Unknown1: typing.Any = 8
    Unknown2: typing.Any = 9
    Unknown3: typing.Any = 10
    ModelChara: typing.Any = 11
    EquipHead: typing.Any = 12
    EquipBody: typing.Any = 13
    EquipLeg: typing.Any = 14
    EquipFoot: typing.Any = 15
    MoveControl: typing.Any = 16
    RideBGM: typing.Any = 17
    Icon: typing.Any = 18
    UIPriority: typing.Any = 19
    MountAction: typing.Any = 20
    Unknown_70_1: typing.Any = 21
    Unknown_70_2: typing.Any = 22
    Unknown16: typing.Any = 23
    Unknown17: typing.Any = 24
    Order: typing.Any = 25
    FlyingCondition: typing.Any = 26
    Unknown5: typing.Any = 27
    Unknown6: typing.Any = 28
    Unknown7: typing.Any = 29
    IsFlying: typing.Any = 30
    Unknown8: typing.Any = 31
    MountCustomize: typing.Any = 32
    ExitMoveDist: typing.Any = 33
    ExitMoveSpeed: typing.Any = 34
    RadiusRate: typing.Any = 35
    BaseMotionSpeed_Run: typing.Any = 36
    BaseMotionSpeed_Walk: typing.Any = 37
    Unknown9: typing.Any = 38
    ExtraSeats: typing.Any = 39
    Unknown10: typing.Any = 40
    Unknown11: typing.Any = 41
    Unknown12: typing.Any = 42
    IsEmote: typing.Any = 43
    Unknown20: typing.Any = 44
    IsAirborne: typing.Any = 45
    ExHotbarEnableConfig: typing.Any = 46
    UseEP: typing.Any = 47
    Unknown13: typing.Any = 48
    IsImmobile: typing.Any = 49
    Unknown14: typing.Any = 50
    Unknown15: typing.Any = 51
    Unknown18: typing.Any = 52
    Unknown19: typing.Any = 53

class MountActionRow(ExdRow):
    Action0: typing.Any = 0
    Action1: typing.Any = 1
    Action2: typing.Any = 2
    Action3: typing.Any = 3
    Action4: typing.Any = 4
    Action5: typing.Any = 5

class MountCustomizeRow(ExdRow):
    HyurMidlanderMaleScale: typing.Any = 0
    HyurMidlanderFemaleScale: typing.Any = 1
    HyurHighlanderMaleScale: typing.Any = 2
    HyurHighlanderFemaleScale: typing.Any = 3
    ElezenMaleScale: typing.Any = 4
    ElezenFemaleScale: typing.Any = 5
    LalaMaleScale: typing.Any = 6
    LalaFemaleScale: typing.Any = 7
    MiqoMaleScale: typing.Any = 8
    MiqoFemaleScale: typing.Any = 9
    RoeMaleScale: typing.Any = 10
    RoeFemaleScale: typing.Any = 11
    AuRaMaleScale: typing.Any = 12
    AuRaFemaleScale: typing.Any = 13
    HrothgarMaleScale: typing.Any = 14
    HrothgarFemaleScale: typing.Any = 15
    VieraMaleScale: typing.Any = 16
    VieraFemaleScale: typing.Any = 17
    HyurMidlanderMaleCameraHeight: typing.Any = 18
    HyurMidlanderFemaleCameraHeight: typing.Any = 19
    HyurHighlanderMaleCameraHeight: typing.Any = 20
    HyurHighlanderFemaleCameraHeight: typing.Any = 21
    ElezenMaleCameraHeight: typing.Any = 22
    ElezenFemaleCameraHeight: typing.Any = 23
    LalaMaleCameraHeight: typing.Any = 24
    LalaFemaleCameraHeight: typing.Any = 25
    MiqoMaleCameraHeight: typing.Any = 26
    MiqoFemaleCameraHeight: typing.Any = 27
    RoeMaleCameraHeight: typing.Any = 28
    RoeFemaleCameraHeight: typing.Any = 29
    AuRaMaleCameraHeight: typing.Any = 30
    AuRaFemaleCameraHeight: typing.Any = 31
    HrothgarMaleCameraHeight: typing.Any = 32
    HrothgarFemaleCameraHeight: typing.Any = 33
    VieraMaleCameraHeight: typing.Any = 34
    VieraFemaleCameraHeight: typing.Any = 35
    Unknown0: typing.Any = 36
    Unknown1: typing.Any = 37
    Unknown_70_1: typing.Any = 38
    Unknown_70_2: typing.Any = 39
    Unknown2: typing.Any = 40
    Unknown3: typing.Any = 41
    Unknown4: typing.Any = 42

class MountFlyingConditionRow(ExdRow):
    _display_field: str = 'Quest'

    Quest: typing.Any = 0

class MountSpeedRow(ExdRow):
    _display_field: str = 'Quest'

    Quest: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2

class MountTransientRow(ExdRow):
    Description: typing.Any = 0
    DescriptionEnhanced: typing.Any = 1
    Tooltip: typing.Any = 2

class MoveControlRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9

class MoveTimelineRow(ExdRow):
    _display_field: str = 'Idle'

    Idle: typing.Any = 0
    MoveForward: typing.Any = 1
    MoveBack: typing.Any = 2
    MoveLeft: typing.Any = 3
    MoveRight: typing.Any = 4
    MoveUp: typing.Any = 5
    MoveDown: typing.Any = 6
    MoveTurnLeft: typing.Any = 7
    MoveTurnRight: typing.Any = 8
    Extra: typing.Any = 9

class MoveVfxRow(ExdRow):
    _display_field: str = 'VFXNormal'

    VFXNormal: typing.Any = 0
    VFXWalking: typing.Any = 1

class MovieStaffListRow(ExdRow):
    StartTime: typing.Any = 0
    EndTime: typing.Any = 1
    Image: typing.Any = 2
    Unknown0: typing.Any = 3

class MovieSubtitleRow(ExdRow):
    StartTime: typing.Any = 0
    EndTime: typing.Any = 1

class MovieSubtitle500Row(ExdRow):
    StartTime: typing.Any = 0
    EndTime: typing.Any = 1

class MovieSubtitleVoyageRow(ExdRow):
    StartTime: typing.Any = 0
    EndTime: typing.Any = 1

class MultipleHelpRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class MultipleHelpPageRow(ExdRow):
    Unknown0: typing.Any = 0

class MultipleHelpStringRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class NotebookDivisionRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    QuestUnlock: typing.Any = 1
    NotebookDivisionCategory: typing.Any = 2
    CraftOpeningLevel: typing.Any = 3
    GatheringOpeningLevel: typing.Any = 4
    Unknown0: typing.Any = 5
    Unknown2: typing.Any = 6
    Unknown3: typing.Any = 7
    CRPCraft: typing.Any = 8
    BSMCraft: typing.Any = 9
    ARMCraft: typing.Any = 10
    GSMCraft: typing.Any = 11
    LTWCraft: typing.Any = 12
    WVRCraft: typing.Any = 13
    ALCCraft: typing.Any = 14
    CULCraft: typing.Any = 15
    Unknown1: typing.Any = 16

class NotebookDivisionCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Index: typing.Any = 1

class NotebookListRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class NotoriousMonsterRow(ExdRow):
    BNpcName: typing.Any = 0
    BNpcBase: typing.Any = 1
    Unknown0: typing.Any = 2
    Rank: typing.Any = 3

class NotoriousMonsterTerritoryRow(ExdRow):
    NotoriousMonsters0: typing.Any = 0
    NotoriousMonsters1: typing.Any = 1
    NotoriousMonsters2: typing.Any = 2
    NotoriousMonsters3: typing.Any = 3
    NotoriousMonsters4: typing.Any = 4
    NotoriousMonsters5: typing.Any = 5
    NotoriousMonsters6: typing.Any = 6
    NotoriousMonsters7: typing.Any = 7
    NotoriousMonsters8: typing.Any = 8
    NotoriousMonsters9: typing.Any = 9

class NpcEquipRow(ExdRow):
    ModelMainHand: typing.Any = 0
    ModelOffHand: typing.Any = 1
    ModelHead: typing.Any = 2
    ModelBody: typing.Any = 3
    ModelHands: typing.Any = 4
    ModelLegs: typing.Any = 5
    ModelFeet: typing.Any = 6
    ModelEars: typing.Any = 7
    ModelNeck: typing.Any = 8
    ModelWrists: typing.Any = 9
    ModelLeftRing: typing.Any = 10
    ModelRightRing: typing.Any = 11
    Unknown_70_1: typing.Any = 12
    Unknown_70_2: typing.Any = 13
    DyeMainHand: typing.Any = 14
    Dye2MainHand: typing.Any = 15
    DyeOffHand: typing.Any = 16
    Dye2OffHand: typing.Any = 17
    DyeHead: typing.Any = 18
    DyeBody: typing.Any = 19
    DyeHands: typing.Any = 20
    DyeLegs: typing.Any = 21
    DyeFeet: typing.Any = 22
    DyeEars: typing.Any = 23
    DyeNeck: typing.Any = 24
    DyeWrists: typing.Any = 25
    DyeLeftRing: typing.Any = 26
    DyeRightRing: typing.Any = 27
    Dye2Head: typing.Any = 28
    Dye2Body: typing.Any = 29
    Dye2Hands: typing.Any = 30
    Dye2Legs: typing.Any = 31
    Dye2Feet: typing.Any = 32
    Dye2Ears: typing.Any = 33
    Dye2Neck: typing.Any = 34
    Dye2Wrists: typing.Any = 35
    Dye2LeftRing: typing.Any = 36
    Dye2RightRing: typing.Any = 37
    Visor: typing.Any = 38
    Unknown0: typing.Any = 39

class NpcYellRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0
    Unknown6: typing.Any = 1
    BalloonTime: typing.Any = 2
    Unknown0: typing.Any = 3
    Unknown7: typing.Any = 4
    Unknown8: typing.Any = 5
    OutputType: typing.Any = 6
    Unknown_70: typing.Any = 7
    Unknown1: typing.Any = 8
    Unknown2: typing.Any = 9
    Unknown3: typing.Any = 10
    Unknown4: typing.Any = 11
    Unknown5: typing.Any = 12
    IsBalloonSlow: typing.Any = 13
    BattleTalkTime: typing.Any = 14

class OmenRow(ExdRow):
    _display_field: str = 'Path'

    Path: typing.Any = 0
    PathAlly: typing.Any = 1
    Type: typing.Any = 2
    Unknown0: typing.Any = 3
    RestrictYScale: typing.Any = 4
    LargeScale: typing.Any = 5

class OmikujiRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6

class OmikujiGuidanceRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class OnlineStatusRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Icon: typing.Any = 1
    Unknown0: typing.Any = 2
    Priority: typing.Any = 3
    Unknown1: typing.Any = 4
    List: typing.Any = 5
    Unknown2: typing.Any = 6

class OpenContentRow(ExdRow):
    OpenContentData0: typing.Any = 0
    OpenContentData1: typing.Any = 1
    OpenContentData2: typing.Any = 2
    OpenContentData3: typing.Any = 3
    OpenContentData4: typing.Any = 4
    OpenContentData5: typing.Any = 5
    OpenContentData6: typing.Any = 6
    OpenContentData7: typing.Any = 7
    OpenContentData8: typing.Any = 8
    OpenContentData9: typing.Any = 9
    OpenContentData10: typing.Any = 10
    OpenContentData11: typing.Any = 11
    OpenContentData12: typing.Any = 12
    OpenContentData13: typing.Any = 13
    OpenContentData14: typing.Any = 14
    OpenContentData15: typing.Any = 15

class OpenContentCandidateNameRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class OpenLuaUIRow(ExdRow):
    Unknown0: typing.Any = 0

class OpeningRow(ExdRow):
    _display_field: str = 'Name'

    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown24: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    Unknown27: typing.Any = 27
    Unknown28: typing.Any = 28
    Unknown29: typing.Any = 29
    Unknown30: typing.Any = 30
    Unknown31: typing.Any = 31
    Unknown32: typing.Any = 32
    Unknown33: typing.Any = 33
    Unknown34: typing.Any = 34
    Unknown35: typing.Any = 35
    Unknown36: typing.Any = 36
    Unknown37: typing.Any = 37
    Unknown38: typing.Any = 38
    Unknown39: typing.Any = 39
    Unknown40: typing.Any = 40
    Unknown41: typing.Any = 41
    Unknown42: typing.Any = 42
    Unknown43: typing.Any = 43
    Unknown44: typing.Any = 44
    Unknown45: typing.Any = 45
    Unknown46: typing.Any = 46
    Unknown47: typing.Any = 47
    Unknown48: typing.Any = 48
    Unknown49: typing.Any = 49
    Unknown50: typing.Any = 50
    Unknown51: typing.Any = 51
    Unknown52: typing.Any = 52
    Unknown53: typing.Any = 53
    Unknown54: typing.Any = 54
    Unknown55: typing.Any = 55
    Unknown56: typing.Any = 56
    Unknown57: typing.Any = 57
    Unknown58: typing.Any = 58
    Unknown59: typing.Any = 59
    Unknown60: typing.Any = 60
    Unknown61: typing.Any = 61
    Unknown62: typing.Any = 62
    Unknown63: typing.Any = 63
    Unknown64: typing.Any = 64
    Unknown65: typing.Any = 65
    Unknown66: typing.Any = 66
    Unknown67: typing.Any = 67
    Unknown68: typing.Any = 68
    Unknown69: typing.Any = 69
    Unknown70: typing.Any = 70
    Unknown71: typing.Any = 71
    Unknown72: typing.Any = 72
    Unknown73: typing.Any = 73
    Unknown74: typing.Any = 74
    Unknown75: typing.Any = 75
    Unknown76: typing.Any = 76
    Unknown77: typing.Any = 77
    Unknown78: typing.Any = 78
    Unknown79: typing.Any = 79
    Name: typing.Any = 80
    Quest: typing.Any = 81

class OpeningSystemDefineRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class OrchestrionRow(ExdRow):
    Name: typing.Any = 0
    Description: typing.Any = 1

class OrchestrionCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Icon: typing.Any = 1
    HideOrder: typing.Any = 2
    Order: typing.Any = 3
    Unknown0: typing.Any = 4

class OrchestrionPathRow(ExdRow):
    File: typing.Any = 0

class OrchestrionUiparamRow(ExdRow):
    Order: typing.Any = 0
    OrchestrionCategory: typing.Any = 1

class OrnamentRow(ExdRow):
    _display_field: str = 'Singular'

    Singular: typing.Any = 0
    Plural: typing.Any = 1
    Adjective: typing.Any = 2
    PossessivePronoun: typing.Any = 3
    StartsWithVowel: typing.Any = 4
    Unknown0: typing.Any = 5
    Pronoun: typing.Any = 6
    Article: typing.Any = 7
    Model: typing.Any = 8
    Action: typing.Any = 9
    Icon: typing.Any = 10
    Transient: typing.Any = 11
    Order: typing.Any = 12
    AttachmentPoint: typing.Any = 13
    Unknown3: typing.Any = 14
    Unknown4: typing.Any = 15

class OrnamentActionRow(ExdRow):
    Actions0: typing.Any = 0
    Actions1: typing.Any = 1
    Actions2: typing.Any = 2
    Actions3: typing.Any = 3
    Actions4: typing.Any = 4
    Actions5: typing.Any = 5

class OrnamentCustomizeRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6

class OrnamentCustomizeGroupRow(ExdRow):
    Customize0: typing.Any = 0
    Customize1: typing.Any = 1
    Customize2: typing.Any = 2
    Customize3: typing.Any = 3
    Customize4: typing.Any = 4
    Customize5: typing.Any = 5
    Customize6: typing.Any = 6
    Customize7: typing.Any = 7
    Customize8: typing.Any = 8
    Customize9: typing.Any = 9
    Customize10: typing.Any = 10
    Customize11: typing.Any = 11
    Customize12: typing.Any = 12
    Customize13: typing.Any = 13
    Customize14: typing.Any = 14
    Customize15: typing.Any = 15
    Customize16: typing.Any = 16
    Customize17: typing.Any = 17
    Customize18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown18: typing.Any = 21

class OrnamentTransientRow(ExdRow):
    Text: typing.Any = 0

class ParamGrowRow(ExdRow):
    ExpToNext: typing.Any = 0
    MpModifier: typing.Any = 1
    BaseSpeed: typing.Any = 2
    LevelModifier: typing.Any = 3
    HuntingLogExpReward: typing.Any = 4
    MonsterNoteSeals: typing.Any = 5
    ScaledQuestXP: typing.Any = 6
    HpModifier: typing.Any = 7
    ItemLevelSync: typing.Any = 8
    ProperDungeon: typing.Any = 9
    ProperGuildOrder: typing.Any = 10
    CraftingLevel: typing.Any = 11
    AdditionalActions: typing.Any = 12
    ApplyAction: typing.Any = 13
    QuestExpModifier: typing.Any = 14

class PartyContentRow(ExdRow):
    _display_field: str = 'ContentFinderCondition'

    LGBEventObject0: typing.Any = 0
    LGBEventObject1: typing.Any = 1
    LGBEventObject2: typing.Any = 2
    LGBEventObject3: typing.Any = 3
    LGBEventObject4: typing.Any = 4
    LGBEventObject5: typing.Any = 5
    LGBEventObject6: typing.Any = 6
    LGBEventObject7: typing.Any = 7
    LGBEventObject8: typing.Any = 8
    LGBEventRange0: typing.Any = 9
    LGBEventRange1: typing.Any = 10
    LGBEventRange2: typing.Any = 11
    LGBEventRange3: typing.Any = 12
    LGBEventRange4: typing.Any = 13
    LGBEventRange5: typing.Any = 14
    LGBEventRange6: typing.Any = 15
    LGBEventRange7: typing.Any = 16
    LGBEventRange8: typing.Any = 17
    LGBEventObject20: typing.Any = 18
    LGBEventObject21: typing.Any = 19
    LGBEventObject22: typing.Any = 20
    LGBEventObject23: typing.Any = 21
    LGBEventObject24: typing.Any = 22
    LGBEventObject25: typing.Any = 23
    LGBEventObject26: typing.Any = 24
    LGBEventObject27: typing.Any = 25
    LGBEventObject28: typing.Any = 26
    TextDataStart: typing.Any = 27
    TextDataEnd: typing.Any = 28
    Image: typing.Any = 29
    TimeLimit: typing.Any = 30
    Unknown0: typing.Any = 31
    ContentFinderCondition: typing.Any = 32
    Key: typing.Any = 33
    Unknown1: typing.Any = 34
    Name: typing.Any = 35

class PartyContentCutsceneRow(ExdRow):
    _display_field: str = 'Cutscene'

    Cutscene: typing.Any = 0
    Unknown0: typing.Any = 1

class PartyContentTextDataRow(ExdRow):
    _display_field: str = 'Data'

    Data: typing.Any = 0

class PartyContentTransientRow(ExdRow):
    Unknown0: typing.Any = 0

class PatchMarkRow(ExdRow):
    Unknown0: typing.Any = 0
    MarkID: typing.Any = 1
    SubCategory: typing.Any = 2
    Unknown1: typing.Any = 3
    SubCategoryType: typing.Any = 4
    Unknown2: typing.Any = 5
    Version: typing.Any = 6
    Category: typing.Any = 7

class PerformRow(ExdRow):
    _display_field: str = 'Name'

    AnimationPlay01: typing.Any = 0
    AnimationPlay02: typing.Any = 1
    Instrument: typing.Any = 2
    ModelKey: typing.Any = 3
    Name: typing.Any = 4
    UnlockLink: typing.Any = 5
    Icon: typing.Any = 6
    AnimationStart: typing.Any = 7
    AnimationEnd: typing.Any = 8
    AnimationIdle: typing.Any = 9
    Transient: typing.Any = 10
    PerformGroup: typing.Any = 11
    Unknown1: typing.Any = 12

class PerformGroupRow(ExdRow):
    Perform0: typing.Any = 0
    Perform1: typing.Any = 1
    Perform2: typing.Any = 2
    Perform3: typing.Any = 3
    Perform4: typing.Any = 4

class PerformGuideScoreRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class PerformTransientRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0

class PermissionRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown24: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    Unknown27: typing.Any = 27
    Unknown28: typing.Any = 28
    Unknown29: typing.Any = 29
    Unknown30: typing.Any = 30
    Unknown31: typing.Any = 31
    Unknown32: typing.Any = 32
    Unknown33: typing.Any = 33
    Unknown34: typing.Any = 34
    Unknown35: typing.Any = 35
    Unknown36: typing.Any = 36
    Unknown37: typing.Any = 37
    Unknown38: typing.Any = 38
    Unknown39: typing.Any = 39
    Unknown40: typing.Any = 40
    Unknown41: typing.Any = 41
    Unknown42: typing.Any = 42
    Unknown43: typing.Any = 43
    Unknown44: typing.Any = 44
    Unknown45: typing.Any = 45
    Unknown46: typing.Any = 46
    Unknown47: typing.Any = 47
    Unknown48: typing.Any = 48
    Unknown49: typing.Any = 49
    Unknown50: typing.Any = 50
    Unknown51: typing.Any = 51
    Unknown52: typing.Any = 52
    Unknown53: typing.Any = 53
    Unknown54: typing.Any = 54
    Unknown55: typing.Any = 55
    Unknown56: typing.Any = 56
    Unknown57: typing.Any = 57
    Unknown58: typing.Any = 58
    Unknown59: typing.Any = 59
    Unknown60: typing.Any = 60
    Unknown61: typing.Any = 61
    Unknown62: typing.Any = 62
    Unknown63: typing.Any = 63
    Unknown64: typing.Any = 64
    Unknown65: typing.Any = 65
    Unknown66: typing.Any = 66
    Unknown67: typing.Any = 67
    Unknown68: typing.Any = 68
    Unknown69: typing.Any = 69
    Unknown70: typing.Any = 70
    Unknown71: typing.Any = 71
    Unknown72: typing.Any = 72
    Unknown73: typing.Any = 73
    Unknown74: typing.Any = 74
    Unknown75: typing.Any = 75
    Unknown76: typing.Any = 76
    Unknown77: typing.Any = 77
    Unknown78: typing.Any = 78
    Unknown79: typing.Any = 79
    Unknown80: typing.Any = 80
    Unknown81: typing.Any = 81
    Unknown82: typing.Any = 82
    Unknown83: typing.Any = 83
    Unknown84: typing.Any = 84
    Unknown85: typing.Any = 85
    Unknown86: typing.Any = 86
    Unknown87: typing.Any = 87
    Unknown88: typing.Any = 88
    Unknown89: typing.Any = 89
    Unknown90: typing.Any = 90
    Unknown91: typing.Any = 91
    Unknown92: typing.Any = 92
    Unknown93: typing.Any = 93
    Unknown94: typing.Any = 94
    Unknown95: typing.Any = 95
    Unknown96: typing.Any = 96
    Unknown97: typing.Any = 97
    Unknown98: typing.Any = 98
    Unknown99: typing.Any = 99
    Unknown100: typing.Any = 100
    Unknown101: typing.Any = 101
    Unknown102: typing.Any = 102
    Unknown103: typing.Any = 103

class PetRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Abilities0: typing.Any = 1
    Abilities1: typing.Any = 2
    Abilities2: typing.Any = 3
    Abilities3: typing.Any = 4
    AutoAction: typing.Any = 5
    SmallScalePercentage: typing.Any = 6
    MediumScalePercentage: typing.Any = 7
    LargeScalePercentage: typing.Any = 8
    Unknown8: typing.Any = 9
    Unknown9: typing.Any = 10
    Unknown10: typing.Any = 11
    Unknown11: typing.Any = 12
    Unknown12: typing.Any = 13
    Unknown13: typing.Any = 14
    Unknown14: typing.Any = 15
    Unknown15: typing.Any = 16
    NonCombatSummon: typing.Any = 17
    Unknown17: typing.Any = 18

class PetActionRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Icon: typing.Any = 2
    Action: typing.Any = 3
    Pet: typing.Any = 4
    MasterOrder: typing.Any = 5
    DisableOrder: typing.Any = 6
    Unknown0: typing.Any = 7

class PetMirageRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2
    Unknown2: typing.Any = 3
    Unknown3: typing.Any = 4
    Unknown4: typing.Any = 5
    Unknown5: typing.Any = 6
    Unknown6: typing.Any = 7
    Unknown7: typing.Any = 8
    Unknown8: typing.Any = 9
    Unknown9: typing.Any = 10
    Unknown10: typing.Any = 11
    Unknown11: typing.Any = 12
    Unknown12: typing.Any = 13
    Unknown13: typing.Any = 14
    Unknown14: typing.Any = 15
    Unknown15: typing.Any = 16
    Unknown16: typing.Any = 17
    Unknown17: typing.Any = 18
    Unknown18: typing.Any = 19
    Unknown19: typing.Any = 20
    Unknown20: typing.Any = 21
    Unknown21: typing.Any = 22
    Unknown22: typing.Any = 23
    Unknown23: typing.Any = 24
    Unknown24: typing.Any = 25
    Unknown25: typing.Any = 26
    Unknown26: typing.Any = 27
    Unknown27: typing.Any = 28
    Unknown28: typing.Any = 29
    Unknown29: typing.Any = 30
    Unknown30: typing.Any = 31
    Unknown31: typing.Any = 32
    Unknown32: typing.Any = 33
    Unknown33: typing.Any = 34
    Unknown34: typing.Any = 35
    Unknown35: typing.Any = 36
    Unknown36: typing.Any = 37
    Unknown37: typing.Any = 38
    Unknown38: typing.Any = 39
    Unknown39: typing.Any = 40
    Unknown40: typing.Any = 41
    Unknown41: typing.Any = 42
    Unknown42: typing.Any = 43
    Unknown43: typing.Any = 44
    Unknown44: typing.Any = 45
    Unknown45: typing.Any = 46
    Unknown46: typing.Any = 47
    Unknown47: typing.Any = 48
    Unknown48: typing.Any = 49
    Unknown49: typing.Any = 50
    Unknown50: typing.Any = 51
    Unknown51: typing.Any = 52
    Unknown52: typing.Any = 53
    Unknown53: typing.Any = 54
    Unknown54: typing.Any = 55
    Unknown55: typing.Any = 56
    Unknown56: typing.Any = 57
    Unknown57: typing.Any = 58
    Unknown58: typing.Any = 59
    Unknown59: typing.Any = 60
    Scale: typing.Any = 61
    ModelChara: typing.Any = 62

class PhysicsGroupRow(ExdRow):
    SimulationTime0: typing.Any = 0
    SimulationTime1: typing.Any = 1
    SimulationTime2: typing.Any = 2
    SimulationTime3: typing.Any = 3
    SimulationTime4: typing.Any = 4
    SimulationTime5: typing.Any = 5
    PS3SimulationTime0: typing.Any = 6
    PS3SimulationTime1: typing.Any = 7
    PS3SimulationTime2: typing.Any = 8
    PS3SimulationTime3: typing.Any = 9
    PS3SimulationTime4: typing.Any = 10
    PS3SimulationTime5: typing.Any = 11
    RootFollowingGame: typing.Any = 12
    RootFollowingCutScene: typing.Any = 13
    ConfigSwitch0: typing.Any = 14
    ConfigSwitch1: typing.Any = 15
    ConfigSwitch2: typing.Any = 16
    ResetByLookAt: typing.Any = 17
    ForceAttractByPhysicsOff: typing.Any = 18

class PhysicsOffGroupRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown_70_1: typing.Any = 2
    Unknown_70_2: typing.Any = 3
    Unknown_70_3: typing.Any = 4
    Unknown_70_4: typing.Any = 5
    Unknown_70_5: typing.Any = 6
    Unknown_70_6: typing.Any = 7
    Unknown_70_7: typing.Any = 8
    Unknown_70_8: typing.Any = 9
    Unknown_70_9: typing.Any = 10
    Unknown_70_10: typing.Any = 11
    Unknown_70_11: typing.Any = 12
    Unknown_70_12: typing.Any = 13
    Unknown_70_13: typing.Any = 14
    Unknown_70_14: typing.Any = 15

class PhysicsParameterRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class PhysicsWindRow(ExdRow):
    Threshold: typing.Any = 0
    Amplitude: typing.Any = 1
    AmplitudeFrequency: typing.Any = 2
    PowerMin: typing.Any = 3
    PowerMax: typing.Any = 4
    PowerFrequency: typing.Any = 5

class PictureRow(ExdRow):
    _display_field: str = 'Image'

    Image: typing.Any = 0
    Signature: typing.Any = 1

class PlaceNameRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    NameNoArticle: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown2: typing.Any = 4
    Unknown3: typing.Any = 5
    Unknown4: typing.Any = 6
    Unknown5: typing.Any = 7
    Unknown6: typing.Any = 8
    Unknown7: typing.Any = 9
    Unknown8: typing.Any = 10
    MapCondition: typing.Any = 11

class PlaceNameReplaceRow(ExdRow):
    Unknown0: typing.Any = 0

class PlantPotFlowerSeedRow(ExdRow):
    SeedIcon0: typing.Any = 0
    SeedIcon1: typing.Any = 1
    SeedIcon2: typing.Any = 2
    SeedIcon3: typing.Any = 3
    SeedIcon4: typing.Any = 4
    SeedIcon5: typing.Any = 5
    SeedIcon6: typing.Any = 6
    SeedIcon7: typing.Any = 7
    SeedIcon8: typing.Any = 8

class PlatformRow(ExdRow):
    Name: typing.Any = 0

class PlayerSearchLocationRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class PlayerSearchSubLocationRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class PointMenuRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class PointMenuChoiceRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12

class PointMenuStringRow(ExdRow):
    Unknown0: typing.Any = 0

class PreHandlerRow(ExdRow):
    _display_field: str = 'Target'

    Unknown0: typing.Any = 0
    Image: typing.Any = 1
    Target: typing.Any = 2
    UnlockQuest: typing.Any = 3
    AcceptMessage: typing.Any = 4
    DenyMessage: typing.Any = 5
    Unknown1: typing.Any = 6
    Unknown2: typing.Any = 7

class PreHandlerMovementRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class PresetCameraRow(ExdRow):
    PosX: typing.Any = 0
    PosY: typing.Any = 1
    PosZ: typing.Any = 2
    Elezen: typing.Any = 3
    Lalafell: typing.Any = 4
    Miqote: typing.Any = 5
    Roe: typing.Any = 6
    Hrothgar: typing.Any = 7
    Viera: typing.Any = 8
    Unknown0: typing.Any = 9
    Hyur_F: typing.Any = 10
    Elezen_F: typing.Any = 11
    Lalafell_F: typing.Any = 12
    Miqote_F: typing.Any = 13
    Roe_F: typing.Any = 14
    Hrothgar_F: typing.Any = 15
    Viera_F: typing.Any = 16
    Unknown_70: typing.Any = 17
    EID: typing.Any = 18

class PresetCameraAdjustRow(ExdRow):
    Hyur_M: typing.Any = 0
    Hyur_F: typing.Any = 1
    Elezen_M: typing.Any = 2
    Elezen_F: typing.Any = 3
    Lalafell_M: typing.Any = 4
    Lalafell_F: typing.Any = 5
    Miqote_M: typing.Any = 6
    Miqote_F: typing.Any = 7
    Roe_M: typing.Any = 8
    Roe_F: typing.Any = 9
    Hrothgar_M: typing.Any = 10
    Hrothgar_F: typing.Any = 11
    Viera_M: typing.Any = 12
    Viera_F: typing.Any = 13
    Unknown_70: typing.Any = 14
    Unknown0: typing.Any = 15

class PreviewableItemsRow(ExdRow):
    Unknown0: typing.Any = 0

class PublicContentRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    MapIcon: typing.Any = 1
    TextDataStart: typing.Any = 2
    TextDataEnd: typing.Any = 3
    StartCutscene: typing.Any = 4
    LGBEventRange: typing.Any = 5
    LGBPopRange: typing.Any = 6
    EndCutscene: typing.Any = 7
    TimeLimit: typing.Any = 8
    ContentFinderCondition: typing.Any = 9
    AdditionalData: typing.Any = 10
    Unknown0: typing.Any = 11
    Unknown1: typing.Any = 12
    Unknown2: typing.Any = 13
    Unknown3: typing.Any = 14
    Unknown5: typing.Any = 15
    Type: typing.Any = 16
    Unknown4: typing.Any = 17

class PublicContentCutsceneRow(ExdRow):
    Cutscene: typing.Any = 0
    Cutscene2: typing.Any = 1

class PublicContentTextDataRow(ExdRow):
    _display_field: str = 'TextData'

    TextData: typing.Any = 0

class PublicContentTypeRow(ExdRow):
    Unknown0: typing.Any = 0

class PvPActionRow(ExdRow):
    _display_field: str = 'Action'

    Action: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2
    Unknown2: typing.Any = 3
    Unknown3: typing.Any = 4
    Unknown4: typing.Any = 5
    GrandCompany0: typing.Any = 6
    GrandCompany1: typing.Any = 7
    GrandCompany2: typing.Any = 8

class PvPActionSortRow(ExdRow):
    _display_field: str = 'Action'

    Unknown0: typing.Any = 0
    Action: typing.Any = 1
    ActionType: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown2: typing.Any = 4

class PvPBaseParamValueRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class PvPInitialSelectActionTraitRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class PvPRankRow(ExdRow):
    ExpRequired: typing.Any = 0

class PvPRankTransientRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class PvPSelectActionRow(ExdRow):
    Unknown0: typing.Any = 0

class PvPSelectTraitRow(ExdRow):
    Effect: typing.Any = 0
    Icon: typing.Any = 1
    Value: typing.Any = 2

class PvPSelectTraitTransientRow(ExdRow):
    Unknown0: typing.Any = 0

class PvPSeriesRow(ExdRow):
    LevelRewards0: typing.Any = 0
    LevelRewards1: typing.Any = 1
    LevelRewards2: typing.Any = 2
    LevelRewards3: typing.Any = 3
    LevelRewards4: typing.Any = 4
    LevelRewards5: typing.Any = 5
    LevelRewards6: typing.Any = 6
    LevelRewards7: typing.Any = 7
    LevelRewards8: typing.Any = 8
    LevelRewards9: typing.Any = 9
    LevelRewards10: typing.Any = 10
    LevelRewards11: typing.Any = 11
    LevelRewards12: typing.Any = 12
    LevelRewards13: typing.Any = 13
    LevelRewards14: typing.Any = 14
    LevelRewards15: typing.Any = 15
    LevelRewards16: typing.Any = 16
    LevelRewards17: typing.Any = 17
    LevelRewards18: typing.Any = 18
    LevelRewards19: typing.Any = 19
    LevelRewards20: typing.Any = 20
    LevelRewards21: typing.Any = 21
    LevelRewards22: typing.Any = 22
    LevelRewards23: typing.Any = 23
    LevelRewards24: typing.Any = 24
    LevelRewards25: typing.Any = 25
    LevelRewards26: typing.Any = 26
    LevelRewards27: typing.Any = 27
    LevelRewards28: typing.Any = 28
    LevelRewards29: typing.Any = 29
    LevelRewards30: typing.Any = 30
    LevelRewards31: typing.Any = 31
    Unknown0: typing.Any = 32

class PvPSeriesLevelRow(ExdRow):
    ExpToNext: typing.Any = 0

class PvPTraitRow(ExdRow):
    Trait1: typing.Any = 0
    Trait2: typing.Any = 1
    Trait3: typing.Any = 2

class QTERow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14

class QuestRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    QuestParams0: typing.Any = 1
    QuestParams1: typing.Any = 2
    QuestParams2: typing.Any = 3
    QuestParams3: typing.Any = 4
    QuestParams4: typing.Any = 5
    QuestParams5: typing.Any = 6
    QuestParams6: typing.Any = 7
    QuestParams7: typing.Any = 8
    QuestParams8: typing.Any = 9
    QuestParams9: typing.Any = 10
    QuestParams10: typing.Any = 11
    QuestParams11: typing.Any = 12
    QuestParams12: typing.Any = 13
    QuestParams13: typing.Any = 14
    QuestParams14: typing.Any = 15
    QuestParams15: typing.Any = 16
    QuestParams16: typing.Any = 17
    QuestParams17: typing.Any = 18
    QuestParams18: typing.Any = 19
    QuestParams19: typing.Any = 20
    QuestParams20: typing.Any = 21
    QuestParams21: typing.Any = 22
    QuestParams22: typing.Any = 23
    QuestParams23: typing.Any = 24
    QuestParams24: typing.Any = 25
    QuestParams25: typing.Any = 26
    QuestParams26: typing.Any = 27
    QuestParams27: typing.Any = 28
    QuestParams28: typing.Any = 29
    QuestParams29: typing.Any = 30
    QuestParams30: typing.Any = 31
    QuestParams31: typing.Any = 32
    QuestParams32: typing.Any = 33
    QuestParams33: typing.Any = 34
    QuestParams34: typing.Any = 35
    QuestParams35: typing.Any = 36
    QuestParams36: typing.Any = 37
    QuestParams37: typing.Any = 38
    QuestParams38: typing.Any = 39
    QuestParams39: typing.Any = 40
    QuestParams40: typing.Any = 41
    QuestParams41: typing.Any = 42
    QuestParams42: typing.Any = 43
    QuestParams43: typing.Any = 44
    QuestParams44: typing.Any = 45
    QuestParams45: typing.Any = 46
    QuestParams46: typing.Any = 47
    QuestParams47: typing.Any = 48
    QuestParams48: typing.Any = 49
    QuestParams49: typing.Any = 50
    QuestListenerParams0: typing.Any = 51
    QuestListenerParams1: typing.Any = 52
    QuestListenerParams2: typing.Any = 53
    QuestListenerParams3: typing.Any = 54
    QuestListenerParams4: typing.Any = 55
    QuestListenerParams5: typing.Any = 56
    QuestListenerParams6: typing.Any = 57
    QuestListenerParams7: typing.Any = 58
    QuestListenerParams8: typing.Any = 59
    QuestListenerParams9: typing.Any = 60
    QuestListenerParams10: typing.Any = 61
    QuestListenerParams11: typing.Any = 62
    QuestListenerParams12: typing.Any = 63
    QuestListenerParams13: typing.Any = 64
    QuestListenerParams14: typing.Any = 65
    QuestListenerParams15: typing.Any = 66
    QuestListenerParams16: typing.Any = 67
    QuestListenerParams17: typing.Any = 68
    QuestListenerParams18: typing.Any = 69
    QuestListenerParams19: typing.Any = 70
    QuestListenerParams20: typing.Any = 71
    QuestListenerParams21: typing.Any = 72
    QuestListenerParams22: typing.Any = 73
    QuestListenerParams23: typing.Any = 74
    QuestListenerParams24: typing.Any = 75
    QuestListenerParams25: typing.Any = 76
    QuestListenerParams26: typing.Any = 77
    QuestListenerParams27: typing.Any = 78
    QuestListenerParams28: typing.Any = 79
    QuestListenerParams29: typing.Any = 80
    QuestListenerParams30: typing.Any = 81
    QuestListenerParams31: typing.Any = 82
    QuestListenerParams32: typing.Any = 83
    QuestListenerParams33: typing.Any = 84
    QuestListenerParams34: typing.Any = 85
    QuestListenerParams35: typing.Any = 86
    QuestListenerParams36: typing.Any = 87
    QuestListenerParams37: typing.Any = 88
    QuestListenerParams38: typing.Any = 89
    QuestListenerParams39: typing.Any = 90
    QuestListenerParams40: typing.Any = 91
    QuestListenerParams41: typing.Any = 92
    QuestListenerParams42: typing.Any = 93
    QuestListenerParams43: typing.Any = 94
    QuestListenerParams44: typing.Any = 95
    QuestListenerParams45: typing.Any = 96
    QuestListenerParams46: typing.Any = 97
    QuestListenerParams47: typing.Any = 98
    QuestListenerParams48: typing.Any = 99
    QuestListenerParams49: typing.Any = 100
    QuestListenerParams50: typing.Any = 101
    QuestListenerParams51: typing.Any = 102
    QuestListenerParams52: typing.Any = 103
    QuestListenerParams53: typing.Any = 104
    QuestListenerParams54: typing.Any = 105
    QuestListenerParams55: typing.Any = 106
    QuestListenerParams56: typing.Any = 107
    QuestListenerParams57: typing.Any = 108
    QuestListenerParams58: typing.Any = 109
    QuestListenerParams59: typing.Any = 110
    QuestListenerParams60: typing.Any = 111
    QuestListenerParams61: typing.Any = 112
    QuestListenerParams62: typing.Any = 113
    QuestListenerParams63: typing.Any = 114
    TodoParams0: typing.Any = 115
    TodoParams1: typing.Any = 116
    TodoParams2: typing.Any = 117
    TodoParams3: typing.Any = 118
    TodoParams4: typing.Any = 119
    TodoParams5: typing.Any = 120
    TodoParams6: typing.Any = 121
    TodoParams7: typing.Any = 122
    TodoParams8: typing.Any = 123
    TodoParams9: typing.Any = 124
    TodoParams10: typing.Any = 125
    TodoParams11: typing.Any = 126
    TodoParams12: typing.Any = 127
    TodoParams13: typing.Any = 128
    TodoParams14: typing.Any = 129
    TodoParams15: typing.Any = 130
    TodoParams16: typing.Any = 131
    TodoParams17: typing.Any = 132
    TodoParams18: typing.Any = 133
    TodoParams19: typing.Any = 134
    TodoParams20: typing.Any = 135
    TodoParams21: typing.Any = 136
    TodoParams22: typing.Any = 137
    TodoParams23: typing.Any = 138
    GilReward: typing.Any = 139
    CurrencyReward: typing.Any = 140
    CurrencyRewardCount: typing.Any = 141
    Reward0: typing.Any = 142
    Reward1: typing.Any = 143
    Reward2: typing.Any = 144
    Reward3: typing.Any = 145
    Reward4: typing.Any = 146
    Reward5: typing.Any = 147
    Reward6: typing.Any = 148
    OptionalItemReward0: typing.Any = 149
    OptionalItemReward1: typing.Any = 150
    OptionalItemReward2: typing.Any = 151
    OptionalItemReward3: typing.Any = 152
    OptionalItemReward4: typing.Any = 153
    InstanceContentUnlock: typing.Any = 154
    ExpFactor: typing.Any = 155
    EmoteReward: typing.Any = 156
    ActionReward: typing.Any = 157
    SystemReward0: typing.Any = 158
    SystemReward1: typing.Any = 159
    GCTypeReward: typing.Any = 160
    ItemCatalyst0: typing.Any = 161
    ItemCatalyst1: typing.Any = 162
    ItemCatalyst2: typing.Any = 163
    ItemCountCatalyst0: typing.Any = 164
    ItemCountCatalyst1: typing.Any = 165
    ItemCountCatalyst2: typing.Any = 166
    ItemRewardType: typing.Any = 167
    ItemCountReward0: typing.Any = 168
    ItemCountReward1: typing.Any = 169
    ItemCountReward2: typing.Any = 170
    ItemCountReward3: typing.Any = 171
    ItemCountReward4: typing.Any = 172
    ItemCountReward5: typing.Any = 173
    ItemCountReward6: typing.Any = 174
    RewardStain0: typing.Any = 175
    RewardStain1: typing.Any = 176
    RewardStain2: typing.Any = 177
    RewardStain3: typing.Any = 178
    RewardStain4: typing.Any = 179
    RewardStain5: typing.Any = 180
    RewardStain6: typing.Any = 181
    OptionalItemCountReward0: typing.Any = 182
    OptionalItemCountReward1: typing.Any = 183
    OptionalItemCountReward2: typing.Any = 184
    OptionalItemCountReward3: typing.Any = 185
    OptionalItemCountReward4: typing.Any = 186
    OptionalItemStainReward0: typing.Any = 187
    OptionalItemStainReward1: typing.Any = 188
    OptionalItemStainReward2: typing.Any = 189
    OptionalItemStainReward3: typing.Any = 190
    OptionalItemStainReward4: typing.Any = 191
    GeneralActionReward0: typing.Any = 192
    GeneralActionReward1: typing.Any = 193
    OtherReward: typing.Any = 194
    Tomestone: typing.Any = 195
    TomestoneReward: typing.Any = 196
    TomestoneCountReward: typing.Any = 197
    ReputationReward: typing.Any = 198
    Unknown0: typing.Any = 199
    Unknown1: typing.Any = 200
    Unknown2: typing.Any = 201
    Unknown3: typing.Any = 202
    Unknown4: typing.Any = 203
    Unknown5: typing.Any = 204
    Unknown6: typing.Any = 205
    OptionalItemIsHQReward0: typing.Any = 206
    OptionalItemIsHQReward1: typing.Any = 207
    OptionalItemIsHQReward2: typing.Any = 208
    OptionalItemIsHQReward3: typing.Any = 209
    OptionalItemIsHQReward4: typing.Any = 210
    Id: typing.Any = 211
    PreviousQuest0: typing.Any = 212
    PreviousQuest1: typing.Any = 213
    PreviousQuest2: typing.Any = 214
    QuestLock0: typing.Any = 215
    QuestLock1: typing.Any = 216
    InstanceContent0: typing.Any = 217
    InstanceContent1: typing.Any = 218
    InstanceContent2: typing.Any = 219
    IssuerStart: typing.Any = 220
    IssuerLocation: typing.Any = 221
    TargetEnd: typing.Any = 222
    JournalGenre: typing.Any = 223
    Icon: typing.Any = 224
    IconSpecial: typing.Any = 225
    MountRequired: typing.Any = 226
    ClassJobLevel0: typing.Any = 227
    ClassJobLevel1: typing.Any = 228
    Header: typing.Any = 229
    BellStart: typing.Any = 230
    BellEnd: typing.Any = 231
    BeastReputationValue: typing.Any = 232
    ClientBehavior: typing.Any = 233
    QuestClassJobSupply: typing.Any = 234
    PlaceName: typing.Any = 235
    SortKey: typing.Any = 236
    Expansion: typing.Any = 237
    ClassJobCategory0: typing.Any = 238
    QuestLevelOffset: typing.Any = 239
    ClassJobCategory1: typing.Any = 240
    PreviousQuestJoin: typing.Any = 241
    Unknown7: typing.Any = 242
    QuestLockJoin: typing.Any = 243
    Unknown8: typing.Any = 244
    Unknown9: typing.Any = 245
    ClassJobUnlock: typing.Any = 246
    GrandCompany: typing.Any = 247
    GrandCompanyRank: typing.Any = 248
    InstanceContentJoin: typing.Any = 249
    Festival: typing.Any = 250
    FestivalBegin: typing.Any = 251
    FestivalEnd: typing.Any = 252
    BeastTribe: typing.Any = 253
    BeastReputationRank: typing.Any = 254
    SatisfactionNpc: typing.Any = 255
    SatisfactionLevel: typing.Any = 256
    DeliveryQuest: typing.Any = 257
    RepeatIntervalType: typing.Any = 258
    QuestRepeatFlag: typing.Any = 259
    Type: typing.Any = 260
    Unknown_70: typing.Any = 261
    LevelMax: typing.Any = 262
    ClassJobRequired: typing.Any = 263
    QuestRewardOtherDisplay: typing.Any = 264
    Unknown10: typing.Any = 265
    EventIconType: typing.Any = 266
    DailyQuestPool: typing.Any = 267
    IsHouseRequired: typing.Any = 268
    IsRepeatable: typing.Any = 269
    CanCancel: typing.Any = 270
    Introduction: typing.Any = 271
    HideOfferIcon: typing.Any = 272
    Unknown12: typing.Any = 273
    Unknown13: typing.Any = 274

class QuestAcceptAdditionConditionRow(ExdRow):
    Requirement0: typing.Any = 0
    Requirement1: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown2: typing.Any = 3
    Unknown1: typing.Any = 4

class QuestAdditionalToolIconRow(ExdRow):
    Unknown0: typing.Any = 0

class QuestAroundPlayerHideRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class QuestAroundPlayerHideExtRow(ExdRow):
    Unknown0: typing.Any = 0

class QuestBattleRow(ExdRow):
    QuestBattleParams0: typing.Any = 0
    QuestBattleParams1: typing.Any = 1
    QuestBattleParams2: typing.Any = 2
    QuestBattleParams3: typing.Any = 3
    QuestBattleParams4: typing.Any = 4
    QuestBattleParams5: typing.Any = 5
    QuestBattleParams6: typing.Any = 6
    QuestBattleParams7: typing.Any = 7
    QuestBattleParams8: typing.Any = 8
    QuestBattleParams9: typing.Any = 9
    QuestBattleParams10: typing.Any = 10
    QuestBattleParams11: typing.Any = 11
    QuestBattleParams12: typing.Any = 12
    QuestBattleParams13: typing.Any = 13
    QuestBattleParams14: typing.Any = 14
    QuestBattleParams15: typing.Any = 15
    QuestBattleParams16: typing.Any = 16
    QuestBattleParams17: typing.Any = 17
    QuestBattleParams18: typing.Any = 18
    QuestBattleParams19: typing.Any = 19
    QuestBattleParams20: typing.Any = 20
    QuestBattleParams21: typing.Any = 21
    QuestBattleParams22: typing.Any = 22
    QuestBattleParams23: typing.Any = 23
    QuestBattleParams24: typing.Any = 24
    QuestBattleParams25: typing.Any = 25
    QuestBattleParams26: typing.Any = 26
    QuestBattleParams27: typing.Any = 27
    QuestBattleParams28: typing.Any = 28
    QuestBattleParams29: typing.Any = 29
    QuestBattleParams30: typing.Any = 30
    QuestBattleParams31: typing.Any = 31
    QuestBattleParams32: typing.Any = 32
    QuestBattleParams33: typing.Any = 33
    QuestBattleParams34: typing.Any = 34
    QuestBattleParams35: typing.Any = 35
    QuestBattleParams36: typing.Any = 36
    QuestBattleParams37: typing.Any = 37
    QuestBattleParams38: typing.Any = 38
    QuestBattleParams39: typing.Any = 39
    QuestBattleParams40: typing.Any = 40
    QuestBattleParams41: typing.Any = 41
    QuestBattleParams42: typing.Any = 42
    QuestBattleParams43: typing.Any = 43
    QuestBattleParams44: typing.Any = 44
    QuestBattleParams45: typing.Any = 45
    QuestBattleParams46: typing.Any = 46
    QuestBattleParams47: typing.Any = 47
    QuestBattleParams48: typing.Any = 48
    QuestBattleParams49: typing.Any = 49
    QuestBattleParams50: typing.Any = 50
    QuestBattleParams51: typing.Any = 51
    QuestBattleParams52: typing.Any = 52
    QuestBattleParams53: typing.Any = 53
    QuestBattleParams54: typing.Any = 54
    QuestBattleParams55: typing.Any = 55
    QuestBattleParams56: typing.Any = 56
    QuestBattleParams57: typing.Any = 57
    QuestBattleParams58: typing.Any = 58
    QuestBattleParams59: typing.Any = 59
    QuestBattleParams60: typing.Any = 60
    QuestBattleParams61: typing.Any = 61
    QuestBattleParams62: typing.Any = 62
    QuestBattleParams63: typing.Any = 63
    QuestBattleParams64: typing.Any = 64
    QuestBattleParams65: typing.Any = 65
    QuestBattleParams66: typing.Any = 66
    QuestBattleParams67: typing.Any = 67
    QuestBattleParams68: typing.Any = 68
    QuestBattleParams69: typing.Any = 69
    QuestBattleParams70: typing.Any = 70
    QuestBattleParams71: typing.Any = 71
    QuestBattleParams72: typing.Any = 72
    QuestBattleParams73: typing.Any = 73
    QuestBattleParams74: typing.Any = 74
    QuestBattleParams75: typing.Any = 75
    QuestBattleParams76: typing.Any = 76
    QuestBattleParams77: typing.Any = 77
    QuestBattleParams78: typing.Any = 78
    QuestBattleParams79: typing.Any = 79
    QuestBattleParams80: typing.Any = 80
    QuestBattleParams81: typing.Any = 81
    QuestBattleParams82: typing.Any = 82
    QuestBattleParams83: typing.Any = 83
    QuestBattleParams84: typing.Any = 84
    QuestBattleParams85: typing.Any = 85
    QuestBattleParams86: typing.Any = 86
    QuestBattleParams87: typing.Any = 87
    QuestBattleParams88: typing.Any = 88
    QuestBattleParams89: typing.Any = 89
    QuestBattleParams90: typing.Any = 90
    QuestBattleParams91: typing.Any = 91
    QuestBattleParams92: typing.Any = 92
    QuestBattleParams93: typing.Any = 93
    QuestBattleParams94: typing.Any = 94
    QuestBattleParams95: typing.Any = 95
    QuestBattleParams96: typing.Any = 96
    QuestBattleParams97: typing.Any = 97
    QuestBattleParams98: typing.Any = 98
    QuestBattleParams99: typing.Any = 99
    QuestBattleParams100: typing.Any = 100
    QuestBattleParams101: typing.Any = 101
    QuestBattleParams102: typing.Any = 102
    QuestBattleParams103: typing.Any = 103
    QuestBattleParams104: typing.Any = 104
    QuestBattleParams105: typing.Any = 105
    QuestBattleParams106: typing.Any = 106
    QuestBattleParams107: typing.Any = 107
    QuestBattleParams108: typing.Any = 108
    QuestBattleParams109: typing.Any = 109
    QuestBattleParams110: typing.Any = 110
    QuestBattleParams111: typing.Any = 111
    QuestBattleParams112: typing.Any = 112
    QuestBattleParams113: typing.Any = 113
    QuestBattleParams114: typing.Any = 114
    QuestBattleParams115: typing.Any = 115
    QuestBattleParams116: typing.Any = 116
    QuestBattleParams117: typing.Any = 117
    QuestBattleParams118: typing.Any = 118
    QuestBattleParams119: typing.Any = 119
    QuestBattleParams120: typing.Any = 120
    QuestBattleParams121: typing.Any = 121
    QuestBattleParams122: typing.Any = 122
    QuestBattleParams123: typing.Any = 123
    QuestBattleParams124: typing.Any = 124
    QuestBattleParams125: typing.Any = 125
    QuestBattleParams126: typing.Any = 126
    QuestBattleParams127: typing.Any = 127
    QuestBattleParams128: typing.Any = 128
    QuestBattleParams129: typing.Any = 129
    QuestBattleParams130: typing.Any = 130
    QuestBattleParams131: typing.Any = 131
    QuestBattleParams132: typing.Any = 132
    QuestBattleParams133: typing.Any = 133
    QuestBattleParams134: typing.Any = 134
    QuestBattleParams135: typing.Any = 135
    QuestBattleParams136: typing.Any = 136
    QuestBattleParams137: typing.Any = 137
    QuestBattleParams138: typing.Any = 138
    QuestBattleParams139: typing.Any = 139
    QuestBattleParams140: typing.Any = 140
    QuestBattleParams141: typing.Any = 141
    QuestBattleParams142: typing.Any = 142
    QuestBattleParams143: typing.Any = 143
    QuestBattleParams144: typing.Any = 144
    QuestBattleParams145: typing.Any = 145
    QuestBattleParams146: typing.Any = 146
    QuestBattleParams147: typing.Any = 147
    QuestBattleParams148: typing.Any = 148
    QuestBattleParams149: typing.Any = 149
    QuestBattleParams150: typing.Any = 150
    QuestBattleParams151: typing.Any = 151
    QuestBattleParams152: typing.Any = 152
    QuestBattleParams153: typing.Any = 153
    QuestBattleParams154: typing.Any = 154
    QuestBattleParams155: typing.Any = 155
    QuestBattleParams156: typing.Any = 156
    QuestBattleParams157: typing.Any = 157
    QuestBattleParams158: typing.Any = 158
    QuestBattleParams159: typing.Any = 159
    QuestBattleParams160: typing.Any = 160
    QuestBattleParams161: typing.Any = 161
    QuestBattleParams162: typing.Any = 162
    QuestBattleParams163: typing.Any = 163
    QuestBattleParams164: typing.Any = 164
    QuestBattleParams165: typing.Any = 165
    QuestBattleParams166: typing.Any = 166
    QuestBattleParams167: typing.Any = 167
    QuestBattleParams168: typing.Any = 168
    QuestBattleParams169: typing.Any = 169
    QuestBattleParams170: typing.Any = 170
    QuestBattleParams171: typing.Any = 171
    QuestBattleParams172: typing.Any = 172
    QuestBattleParams173: typing.Any = 173
    QuestBattleParams174: typing.Any = 174
    QuestBattleParams175: typing.Any = 175
    QuestBattleParams176: typing.Any = 176
    QuestBattleParams177: typing.Any = 177
    QuestBattleParams178: typing.Any = 178
    QuestBattleParams179: typing.Any = 179
    QuestBattleParams180: typing.Any = 180
    QuestBattleParams181: typing.Any = 181
    QuestBattleParams182: typing.Any = 182
    QuestBattleParams183: typing.Any = 183
    QuestBattleParams184: typing.Any = 184
    QuestBattleParams185: typing.Any = 185
    QuestBattleParams186: typing.Any = 186
    QuestBattleParams187: typing.Any = 187
    QuestBattleParams188: typing.Any = 188
    QuestBattleParams189: typing.Any = 189
    QuestBattleParams190: typing.Any = 190
    QuestBattleParams191: typing.Any = 191
    QuestBattleParams192: typing.Any = 192
    QuestBattleParams193: typing.Any = 193
    QuestBattleParams194: typing.Any = 194
    QuestBattleParams195: typing.Any = 195
    QuestBattleParams196: typing.Any = 196
    QuestBattleParams197: typing.Any = 197
    QuestBattleParams198: typing.Any = 198
    QuestBattleParams199: typing.Any = 199
    QuestBattleParams200: typing.Any = 200
    QuestBattleParams201: typing.Any = 201
    QuestBattleParams202: typing.Any = 202
    QuestBattleParams203: typing.Any = 203
    QuestBattleParams204: typing.Any = 204
    QuestBattleParams205: typing.Any = 205
    QuestBattleParams206: typing.Any = 206
    QuestBattleParams207: typing.Any = 207
    QuestBattleParams208: typing.Any = 208
    QuestBattleParams209: typing.Any = 209
    QuestBattleParams210: typing.Any = 210
    QuestBattleParams211: typing.Any = 211
    QuestBattleParams212: typing.Any = 212
    QuestBattleParams213: typing.Any = 213
    QuestBattleParams214: typing.Any = 214
    QuestBattleParams215: typing.Any = 215
    QuestBattleParams216: typing.Any = 216
    QuestBattleParams217: typing.Any = 217
    QuestBattleParams218: typing.Any = 218
    QuestBattleParams219: typing.Any = 219
    Quest: typing.Any = 220
    TimeLimit: typing.Any = 221
    LevelSync: typing.Any = 222
    QuestBattleScene: typing.Any = 223

class QuestBattleResidentRow(ExdRow):
    Unknown0: typing.Any = 0

class QuestBattleSystemDefineRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class QuestChapterRow(ExdRow):
    _display_field: str = 'Quest'

    Quest: typing.Any = 0
    Redo: typing.Any = 1

class QuestClassJobRewardRow(ExdRow):
    RewardItem0: typing.Any = 0
    RewardItem1: typing.Any = 1
    RewardItem2: typing.Any = 2
    RewardItem3: typing.Any = 3
    RequiredItem0: typing.Any = 4
    RequiredItem1: typing.Any = 5
    RequiredItem2: typing.Any = 6
    RequiredItem3: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    ClassJobCategory: typing.Any = 10
    RewardAmount0: typing.Any = 11
    RewardAmount1: typing.Any = 12
    RewardAmount2: typing.Any = 13
    RewardAmount3: typing.Any = 14
    RequiredAmount0: typing.Any = 15
    RequiredAmount1: typing.Any = 16
    RequiredAmount2: typing.Any = 17
    RequiredAmount3: typing.Any = 18
    Unknown10: typing.Any = 19
    Unknown11: typing.Any = 20
    Unknown0: typing.Any = 21
    Unknown1: typing.Any = 22
    Unknown2: typing.Any = 23
    Unknown3: typing.Any = 24
    Unknown4: typing.Any = 25
    Unknown5: typing.Any = 26
    Unknown6: typing.Any = 27
    Unknown7: typing.Any = 28
    Unknown12: typing.Any = 29
    Unknown13: typing.Any = 30
    Unknown14: typing.Any = 31
    Unknown15: typing.Any = 32

class QuestClassJobSupplyRow(ExdRow):
    Unknown_70_1: typing.Any = 0
    ENpcResident: typing.Any = 1
    Item: typing.Any = 2
    Unknown_70_2: typing.Any = 3
    Unknown_70_3: typing.Any = 4
    Unknown1: typing.Any = 5
    Unknown2: typing.Any = 6
    ClassJobCategory: typing.Any = 7
    Unknown0: typing.Any = 8
    AmountRequired: typing.Any = 9
    Unknown3: typing.Any = 10
    ItemHQ: typing.Any = 11

class QuestCustomTodoRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown2: typing.Any = 1
    Unknown3: typing.Any = 2
    Unknown4: typing.Any = 3
    Unknown1: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8

class QuestDefineClientRow(ExdRow):
    Unknown0: typing.Any = 0
    Target: typing.Any = 1

class QuestDerivedClassRow(ExdRow):
    _display_field: str = 'ClassJob'

    ClassJob: typing.Any = 0

class QuestEffectRow(ExdRow):
    UnknownStruct0: typing.Any = 0
    UnknownStruct1: typing.Any = 1
    UnknownStruct2: typing.Any = 2
    UnknownStruct3: typing.Any = 3
    Unknown8: typing.Any = 4
    Unknown9: typing.Any = 5
    Unknown_70: typing.Any = 6

class QuestEffectDefineRow(ExdRow):
    _display_field: str = 'Effect'

    Effect: typing.Any = 0

class QuestEffectTypeRow(ExdRow):
    Unknown0: typing.Any = 0

class QuestEquipModelRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class QuestEventAreaEntranceInfoRow(ExdRow):
    Quest: typing.Any = 0
    Location: typing.Any = 1
    Unknown0: typing.Any = 2

class QuestHideRewardRow(ExdRow):
    Unknown0: typing.Any = 0

class QuestLinkMarkerRow(ExdRow):
    SourceMap: typing.Any = 0
    Level: typing.Any = 1
    TargetMap: typing.Any = 2
    Unknown0: typing.Any = 3
    Unknown1: typing.Any = 4

class QuestLinkMarkerIconRow(ExdRow):
    Icon: typing.Any = 0

class QuestLinkMarkerSetRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6

class QuestRecompleteRow(ExdRow):
    Unknown0: typing.Any = 0

class QuestRedoRow(ExdRow):
    _display_field: str = 'FinalQuest'

    QuestRedoParam0: typing.Any = 0
    QuestRedoParam1: typing.Any = 1
    QuestRedoParam2: typing.Any = 2
    QuestRedoParam3: typing.Any = 3
    QuestRedoParam4: typing.Any = 4
    QuestRedoParam5: typing.Any = 5
    QuestRedoParam6: typing.Any = 6
    QuestRedoParam7: typing.Any = 7
    QuestRedoParam8: typing.Any = 8
    QuestRedoParam9: typing.Any = 9
    QuestRedoParam10: typing.Any = 10
    QuestRedoParam11: typing.Any = 11
    QuestRedoParam12: typing.Any = 12
    QuestRedoParam13: typing.Any = 13
    QuestRedoParam14: typing.Any = 14
    QuestRedoParam15: typing.Any = 15
    QuestRedoParam16: typing.Any = 16
    QuestRedoParam17: typing.Any = 17
    QuestRedoParam18: typing.Any = 18
    QuestRedoParam19: typing.Any = 19
    QuestRedoParam20: typing.Any = 20
    QuestRedoParam21: typing.Any = 21
    QuestRedoParam22: typing.Any = 22
    QuestRedoParam23: typing.Any = 23
    QuestRedoParam24: typing.Any = 24
    QuestRedoParam25: typing.Any = 25
    QuestRedoParam26: typing.Any = 26
    QuestRedoParam27: typing.Any = 27
    QuestRedoParam28: typing.Any = 28
    QuestRedoParam29: typing.Any = 29
    QuestRedoParam30: typing.Any = 30
    QuestRedoParam31: typing.Any = 31
    FinalQuest: typing.Any = 32
    Unknown0: typing.Any = 33
    Chapter: typing.Any = 34
    Unknown1: typing.Any = 35

class QuestRedoChapterRow(ExdRow):
    Unknown3: typing.Any = 0
    Unknown4: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown2: typing.Any = 4
    Unknown5: typing.Any = 5

class QuestRedoChapterUIRow(ExdRow):
    _display_field: str = 'Quest'

    ChapterName: typing.Any = 0
    ChapterPart: typing.Any = 1
    Transient: typing.Any = 2
    Quest: typing.Any = 3
    Unknown0: typing.Any = 4
    QuestRedoUISmall: typing.Any = 5
    QuestRedoUILarge: typing.Any = 6
    QuestRedoUIWide: typing.Any = 7
    UITab: typing.Any = 8
    Category: typing.Any = 9
    Unknown1: typing.Any = 10

class QuestRedoChapterUICategoryRow(ExdRow):
    _display_field: str = 'Expac'

    Expac: typing.Any = 0
    Unknown0: typing.Any = 1

class QuestRedoChapterUITabRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0
    Icon1: typing.Any = 1
    Icon2: typing.Any = 2
    Unknown0: typing.Any = 3

class QuestRedoIncompChapterRow(ExdRow):
    _display_field: str = 'Chapter'

    Chapter: typing.Any = 0

class QuestRedoValidCustomTalkRow(ExdRow):
    Unknown0: typing.Any = 0

class QuestRepeatFlagRow(ExdRow):
    _display_field: str = 'Quest'

    Quest: typing.Any = 0

class QuestRewardOtherRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Icon: typing.Any = 1

class QuestSceneAbortConditionRow(ExdRow):
    Unknown0: typing.Any = 0

class QuestSceneAbortConditionFlagRow(ExdRow):
    Unknown0: typing.Any = 0

class QuestSceneAbortConditionTypeRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class QuestSelectTitleRow(ExdRow):
    Unknown0: typing.Any = 0

class QuestSetDefineRow(ExdRow):
    Unknown0: typing.Any = 0

class QuestStatusParamRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class QuestSubCommandRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23

class QuestSystemDefineRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class QuickChatRow(ExdRow):
    _display_field: str = 'NameAction'

    NameAction: typing.Any = 0
    Icon: typing.Any = 1
    Addon: typing.Any = 2
    Unknown0: typing.Any = 3
    QuickChatTransient: typing.Any = 4

class QuickChatTransientRow(ExdRow):
    _display_field: str = 'TextOutput'

    TextOutput: typing.Any = 0

class RPParameterRow(ExdRow):
    _display_field: str = 'BNpcName'

    BNpcName: typing.Any = 0
    ClassJob: typing.Any = 1
    Sex: typing.Any = 2

class RaceRow(ExdRow):
    _display_field: str = 'Feminine'

    Masculine: typing.Any = 0
    Feminine: typing.Any = 1
    RSEMBody: typing.Any = 2
    RSEFBody: typing.Any = 3
    RSEMHands: typing.Any = 4
    RSEFHands: typing.Any = 5
    RSEMLegs: typing.Any = 6
    RSEFLegs: typing.Any = 7
    RSEMFeet: typing.Any = 8
    RSEFFeet: typing.Any = 9
    Unknown0: typing.Any = 10
    ExPac: typing.Any = 11

class RacingChocoboGradeRow(ExdRow):
    Unknown0: typing.Any = 0

class RacingChocoboItemRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0
    Category: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3

class RacingChocoboNameRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class RacingChocoboNameCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    SortKey: typing.Any = 1

class RacingChocoboNameInfoRow(ExdRow):
    Name0: typing.Any = 0
    Name1: typing.Any = 1
    Name2: typing.Any = 2
    Unknown4: typing.Any = 3
    RacingChocoboNameCategory: typing.Any = 4
    Unknown0: typing.Any = 5
    Unknown1: typing.Any = 6
    Unknown2: typing.Any = 7
    Unknown3: typing.Any = 8

class RacingChocoboParamRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class RaidFinderParamRow(ExdRow):
    Unknown0: typing.Any = 0

class ReactionEventObjectRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class ReactionEventObjectInfoRow(ExdRow):
    Unknown0: typing.Any = 0

class RecastNavimeshRow(ExdRow):
    Unknown0: typing.Any = 0
    TileSize: typing.Any = 1
    CellSize: typing.Any = 2
    CellHeight: typing.Any = 3
    AgentHeight: typing.Any = 4
    AgentRadius: typing.Any = 5
    AgentMaxClimb: typing.Any = 6
    AgentMaxSlope: typing.Any = 7
    RegionMinSize: typing.Any = 8
    RegionMergedSize: typing.Any = 9
    MaxEdgeLength: typing.Any = 10
    MaxEdgeError: typing.Any = 11
    VertsPerPoly: typing.Any = 12
    DetailMeshSampleDistance: typing.Any = 13
    DetailMeshMaxSampleError: typing.Any = 14
    Unknown1: typing.Any = 15
    Unknown2: typing.Any = 16
    Unknown3: typing.Any = 17
    Unknown4: typing.Any = 18
    Unknown5: typing.Any = 19
    Unknown6: typing.Any = 20
    Unknown7: typing.Any = 21
    Unknown8: typing.Any = 22
    Unknown9: typing.Any = 23
    Unknown10: typing.Any = 24
    Unknown11: typing.Any = 25
    Unknown12: typing.Any = 26
    Unknown13: typing.Any = 27
    Unknown14: typing.Any = 28
    Unknown15: typing.Any = 29
    Unknown16: typing.Any = 30
    Unknown17: typing.Any = 31
    Unknown18: typing.Any = 32
    Unknown19: typing.Any = 33
    Unknown20: typing.Any = 34

class RecipeRow(ExdRow):
    _display_field: str = 'ItemResult'

    RequiredQuality: typing.Any = 0
    Quest: typing.Any = 1
    Number: typing.Any = 2
    CraftType: typing.Any = 3
    ItemResult: typing.Any = 4
    Ingredient0: typing.Any = 5
    Ingredient1: typing.Any = 6
    Ingredient2: typing.Any = 7
    Ingredient3: typing.Any = 8
    Ingredient4: typing.Any = 9
    Ingredient5: typing.Any = 10
    Ingredient6: typing.Any = 11
    Ingredient7: typing.Any = 12
    StatusRequired: typing.Any = 13
    ItemRequired: typing.Any = 14
    RecipeLevelTable: typing.Any = 15
    MaxAdjustableJobLevel: typing.Any = 16
    RecipeNotebookList: typing.Any = 17
    DisplayPriority: typing.Any = 18
    DifficultyFactor: typing.Any = 19
    QualityFactor: typing.Any = 20
    DurabilityFactor: typing.Any = 21
    RequiredCraftsmanship: typing.Any = 22
    RequiredControl: typing.Any = 23
    QuickSynthCraftsmanship: typing.Any = 24
    QuickSynthControl: typing.Any = 25
    SecretRecipeBook: typing.Any = 26
    CollectableMetadata: typing.Any = 27
    PatchNumber: typing.Any = 28
    AmountResult: typing.Any = 29
    AmountIngredient0: typing.Any = 30
    AmountIngredient1: typing.Any = 31
    AmountIngredient2: typing.Any = 32
    AmountIngredient3: typing.Any = 33
    AmountIngredient4: typing.Any = 34
    AmountIngredient5: typing.Any = 35
    AmountIngredient6: typing.Any = 36
    AmountIngredient7: typing.Any = 37
    MaterialQualityFactor: typing.Any = 38
    CollectableMetadataKey: typing.Any = 39
    IsSecondary: typing.Any = 40
    CanQuickSynth: typing.Any = 41
    CanHq: typing.Any = 42
    ExpRewarded: typing.Any = 43
    Unknown1: typing.Any = 44
    IsSpecializationRequired: typing.Any = 45
    IsExpert: typing.Any = 46

class RecipeLevelTableRow(ExdRow):
    Quality: typing.Any = 0
    SuggestedCraftsmanship: typing.Any = 1
    Difficulty: typing.Any = 2
    Durability: typing.Any = 3
    ConditionsFlag: typing.Any = 4
    ClassJobLevel: typing.Any = 5
    Stars: typing.Any = 6
    ProgressDivider: typing.Any = 7
    QualityDivider: typing.Any = 8
    ProgressModifier: typing.Any = 9
    QualityModifier: typing.Any = 10

class RecipeLookupRow(ExdRow):
    CRP: typing.Any = 0
    BSM: typing.Any = 1
    ARM: typing.Any = 2
    GSM: typing.Any = 3
    LTW: typing.Any = 4
    WVR: typing.Any = 5
    ALC: typing.Any = 6
    CUL: typing.Any = 7

class RecipeNotebookListRow(ExdRow):
    Recipe0: typing.Any = 0
    Recipe1: typing.Any = 1
    Recipe2: typing.Any = 2
    Recipe3: typing.Any = 3
    Recipe4: typing.Any = 4
    Recipe5: typing.Any = 5
    Recipe6: typing.Any = 6
    Recipe7: typing.Any = 7
    Recipe8: typing.Any = 8
    Recipe9: typing.Any = 9
    Recipe10: typing.Any = 10
    Recipe11: typing.Any = 11
    Recipe12: typing.Any = 12
    Recipe13: typing.Any = 13
    Recipe14: typing.Any = 14
    Recipe15: typing.Any = 15
    Recipe16: typing.Any = 16
    Recipe17: typing.Any = 17
    Recipe18: typing.Any = 18
    Recipe19: typing.Any = 19
    Recipe20: typing.Any = 20
    Recipe21: typing.Any = 21
    Recipe22: typing.Any = 22
    Recipe23: typing.Any = 23
    Recipe24: typing.Any = 24
    Recipe25: typing.Any = 25
    Recipe26: typing.Any = 26
    Recipe27: typing.Any = 27
    Recipe28: typing.Any = 28
    Recipe29: typing.Any = 29
    Recipe30: typing.Any = 30
    Recipe31: typing.Any = 31
    Recipe32: typing.Any = 32
    Recipe33: typing.Any = 33
    Recipe34: typing.Any = 34
    Recipe35: typing.Any = 35
    Recipe36: typing.Any = 36
    Recipe37: typing.Any = 37
    Recipe38: typing.Any = 38
    Recipe39: typing.Any = 39
    Recipe40: typing.Any = 40
    Recipe41: typing.Any = 41
    Recipe42: typing.Any = 42
    Recipe43: typing.Any = 43
    Recipe44: typing.Any = 44
    Recipe45: typing.Any = 45
    Recipe46: typing.Any = 46
    Recipe47: typing.Any = 47
    Recipe48: typing.Any = 48
    Recipe49: typing.Any = 49
    Recipe50: typing.Any = 50
    Recipe51: typing.Any = 51
    Recipe52: typing.Any = 52
    Recipe53: typing.Any = 53
    Recipe54: typing.Any = 54
    Recipe55: typing.Any = 55
    Recipe56: typing.Any = 56
    Recipe57: typing.Any = 57
    Recipe58: typing.Any = 58
    Recipe59: typing.Any = 59
    Recipe60: typing.Any = 60
    Recipe61: typing.Any = 61
    Recipe62: typing.Any = 62
    Recipe63: typing.Any = 63
    Recipe64: typing.Any = 64
    Recipe65: typing.Any = 65
    Recipe66: typing.Any = 66
    Recipe67: typing.Any = 67
    Recipe68: typing.Any = 68
    Recipe69: typing.Any = 69
    Recipe70: typing.Any = 70
    Recipe71: typing.Any = 71
    Recipe72: typing.Any = 72
    Recipe73: typing.Any = 73
    Recipe74: typing.Any = 74
    Recipe75: typing.Any = 75
    Recipe76: typing.Any = 76
    Recipe77: typing.Any = 77
    Recipe78: typing.Any = 78
    Recipe79: typing.Any = 79
    Recipe80: typing.Any = 80
    Recipe81: typing.Any = 81
    Recipe82: typing.Any = 82
    Recipe83: typing.Any = 83
    Recipe84: typing.Any = 84
    Recipe85: typing.Any = 85
    Recipe86: typing.Any = 86
    Recipe87: typing.Any = 87
    Recipe88: typing.Any = 88
    Recipe89: typing.Any = 89
    Recipe90: typing.Any = 90
    Recipe91: typing.Any = 91
    Recipe92: typing.Any = 92
    Recipe93: typing.Any = 93
    Recipe94: typing.Any = 94
    Recipe95: typing.Any = 95
    Recipe96: typing.Any = 96
    Recipe97: typing.Any = 97
    Recipe98: typing.Any = 98
    Recipe99: typing.Any = 99
    Recipe100: typing.Any = 100
    Recipe101: typing.Any = 101
    Recipe102: typing.Any = 102
    Recipe103: typing.Any = 103
    Recipe104: typing.Any = 104
    Recipe105: typing.Any = 105
    Recipe106: typing.Any = 106
    Recipe107: typing.Any = 107
    Recipe108: typing.Any = 108
    Recipe109: typing.Any = 109
    Recipe110: typing.Any = 110
    Recipe111: typing.Any = 111
    Recipe112: typing.Any = 112
    Recipe113: typing.Any = 113
    Recipe114: typing.Any = 114
    Recipe115: typing.Any = 115
    Recipe116: typing.Any = 116
    Recipe117: typing.Any = 117
    Recipe118: typing.Any = 118
    Recipe119: typing.Any = 119
    Recipe120: typing.Any = 120
    Recipe121: typing.Any = 121
    Recipe122: typing.Any = 122
    Recipe123: typing.Any = 123
    Recipe124: typing.Any = 124
    Recipe125: typing.Any = 125
    Recipe126: typing.Any = 126
    Recipe127: typing.Any = 127
    Recipe128: typing.Any = 128
    Recipe129: typing.Any = 129
    Recipe130: typing.Any = 130
    Recipe131: typing.Any = 131
    Recipe132: typing.Any = 132
    Recipe133: typing.Any = 133
    Recipe134: typing.Any = 134
    Recipe135: typing.Any = 135
    Recipe136: typing.Any = 136
    Recipe137: typing.Any = 137
    Recipe138: typing.Any = 138
    Recipe139: typing.Any = 139
    Recipe140: typing.Any = 140
    Recipe141: typing.Any = 141
    Recipe142: typing.Any = 142
    Recipe143: typing.Any = 143
    Recipe144: typing.Any = 144
    Recipe145: typing.Any = 145
    Recipe146: typing.Any = 146
    Recipe147: typing.Any = 147
    Recipe148: typing.Any = 148
    Recipe149: typing.Any = 149
    Recipe150: typing.Any = 150
    Recipe151: typing.Any = 151
    Recipe152: typing.Any = 152
    Recipe153: typing.Any = 153
    Recipe154: typing.Any = 154
    Recipe155: typing.Any = 155
    Recipe156: typing.Any = 156
    Recipe157: typing.Any = 157
    Recipe158: typing.Any = 158
    Recipe159: typing.Any = 159
    Count: typing.Any = 160

class RecipeSubCategoryRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class RecommendContentsRow(ExdRow):
    _display_field: str = 'Level'

    Level: typing.Any = 0
    ClassJob: typing.Any = 1
    MinLevel: typing.Any = 2
    MaxLevel: typing.Any = 3

class RelicRow(ExdRow):
    _display_field: str = 'ItemAnimus'

    ItemAtma: typing.Any = 0
    ItemAnimus: typing.Any = 1
    Icon: typing.Any = 2
    Materia0: typing.Any = 3
    Materia1: typing.Any = 4
    Materia2: typing.Any = 5
    Materia3: typing.Any = 6
    NoteMain0: typing.Any = 7
    NoteSub0: typing.Any = 8
    NoteSelection10: typing.Any = 9
    NoteMain1: typing.Any = 10
    NoteSub1: typing.Any = 11
    NoteSelection1: typing.Any = 12
    NoteMain2: typing.Any = 13
    NoteSub2: typing.Any = 14
    NoteSelection3: typing.Any = 15

class Relic3Row(ExdRow):
    _display_field: str = 'ItemNovus'

    ItemAnimus: typing.Any = 0
    ItemScroll: typing.Any = 1
    ItemNovus: typing.Any = 2
    Icon: typing.Any = 3
    MateriaLimit: typing.Any = 4
    Unknown0: typing.Any = 5

class Relic3MateriaRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8

class Relic3RateRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8

class Relic3RatePatternRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class Relic6MagiciteRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class RelicItemRow(ExdRow):
    GladiatorItem: typing.Any = 0
    PugilistItem: typing.Any = 1
    MarauderItem: typing.Any = 2
    LancerItem: typing.Any = 3
    ArcherItem: typing.Any = 4
    ConjurerItem: typing.Any = 5
    ThaumaturgeItem: typing.Any = 6
    ArcanistSMNItem: typing.Any = 7
    ArcanistSCHItem: typing.Any = 8
    ShieldItem: typing.Any = 9
    RogueItem: typing.Any = 10
    Unknown0: typing.Any = 11
    Unknown1: typing.Any = 12
    Unknown2: typing.Any = 13
    Unknown3: typing.Any = 14
    Unknown4: typing.Any = 15
    Unknown5: typing.Any = 16

class RelicMateriaRow(ExdRow):
    Unknown0: typing.Any = 0

class RelicNoteRow(ExdRow):
    _display_field: str = 'EventItem'

    EventItem: typing.Any = 0
    MonsterNoteTargetCommon0: typing.Any = 1
    MonsterNoteTargetCommon1: typing.Any = 2
    MonsterNoteTargetCommon2: typing.Any = 3
    MonsterNoteTargetCommon3: typing.Any = 4
    MonsterNoteTargetCommon4: typing.Any = 5
    MonsterNoteTargetCommon5: typing.Any = 6
    MonsterNoteTargetCommon6: typing.Any = 7
    MonsterNoteTargetCommon7: typing.Any = 8
    MonsterNoteTargetCommon8: typing.Any = 9
    MonsterNoteTargetCommon9: typing.Any = 10
    MonsterNoteTargetNM0: typing.Any = 11
    MonsterNoteTargetNM1: typing.Any = 12
    MonsterNoteTargetNM2: typing.Any = 13
    Unknown0: typing.Any = 14
    Fate0: typing.Any = 15
    Fate1: typing.Any = 16
    Fate2: typing.Any = 17
    PlaceNameFate0: typing.Any = 18
    PlaceNameFate1: typing.Any = 19
    PlaceNameFate2: typing.Any = 20
    Leve0: typing.Any = 21
    Leve1: typing.Any = 22
    Leve2: typing.Any = 23
    MonsterCount0: typing.Any = 24
    MonsterCount1: typing.Any = 25
    MonsterCount2: typing.Any = 26
    MonsterCount3: typing.Any = 27
    MonsterCount4: typing.Any = 28
    MonsterCount5: typing.Any = 29
    MonsterCount6: typing.Any = 30
    MonsterCount7: typing.Any = 31
    MonsterCount8: typing.Any = 32
    MonsterCount9: typing.Any = 33

class RelicNoteCategoryRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0
    Unknown0: typing.Any = 1

class ReplaceActionRow(ExdRow):
    Action: typing.Any = 0
    ReplaceActions0: typing.Any = 1
    ReplaceActions1: typing.Any = 2
    ReplaceActions2: typing.Any = 3
    ReplaceActions3: typing.Any = 4
    Param1: typing.Any = 5
    Param2: typing.Any = 6
    Param3: typing.Any = 7
    Param4: typing.Any = 8
    Type1: typing.Any = 9
    Type2: typing.Any = 10
    Type3: typing.Any = 11
    Type4: typing.Any = 12
    ReplaceSettable: typing.Any = 13
    Unknown_70: typing.Any = 14

class ResidentRow(ExdRow):
    Model: typing.Any = 0
    NpcYell: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3
    ResidentMotionType: typing.Any = 4

class ResidentMotionTypeRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7

class ResistanceWeaponAdjustRow(ExdRow):
    Image: typing.Any = 0
    MaxTotalStats: typing.Any = 1
    MaxEachStat: typing.Any = 2
    BaseParam0: typing.Any = 3
    BaseParam1: typing.Any = 4
    BaseParam2: typing.Any = 5
    BaseParam3: typing.Any = 6
    Unknown0: typing.Any = 7

class RetainerFortuneRewardRangeRow(ExdRow):
    PercentOfLevel: typing.Any = 0

class RetainerTaskRow(ExdRow):
    Experience: typing.Any = 0
    Unknown0: typing.Any = 1
    RetainerTaskParameter: typing.Any = 2
    VentureCost: typing.Any = 3
    MaxTimemin: typing.Any = 4
    RequiredItemLevel: typing.Any = 5
    RequiredGathering: typing.Any = 6
    Unknown1: typing.Any = 7
    Task: typing.Any = 8
    ClassJobCategory: typing.Any = 9
    RetainerLevel: typing.Any = 10
    ConditionParam0: typing.Any = 11
    ConditionParam1: typing.Any = 12
    IsRandom: typing.Any = 13

class RetainerTaskLvRangeRow(ExdRow):
    Min: typing.Any = 0
    Max: typing.Any = 1

class RetainerTaskNormalRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0
    GatheringLog: typing.Any = 1
    FishingLog: typing.Any = 2
    Quantity0: typing.Any = 3
    Quantity1: typing.Any = 4
    Quantity2: typing.Any = 5
    Quantity3: typing.Any = 6
    Quantity4: typing.Any = 7

class RetainerTaskParameterRow(ExdRow):
    ItemLevelDoW0: typing.Any = 0
    ItemLevelDoW1: typing.Any = 1
    ItemLevelDoW2: typing.Any = 2
    ItemLevelDoW3: typing.Any = 3
    PerceptionDoL0: typing.Any = 4
    PerceptionDoL1: typing.Any = 5
    PerceptionDoL2: typing.Any = 6
    PerceptionDoL3: typing.Any = 7
    PerceptionFSH0: typing.Any = 8
    PerceptionFSH1: typing.Any = 9
    PerceptionFSH2: typing.Any = 10
    PerceptionFSH3: typing.Any = 11

class RetainerTaskParameterLvDiffRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class RetainerTaskRandomRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Requirement: typing.Any = 1

class RideShootingRow(ExdRow):
    RideShootingParams0: typing.Any = 0
    RideShootingParams1: typing.Any = 1
    RideShootingParams2: typing.Any = 2
    RideShootingParams3: typing.Any = 3
    RideShootingParams4: typing.Any = 4
    RideShootingParams5: typing.Any = 5
    RideShootingParams6: typing.Any = 6
    RideShootingParams7: typing.Any = 7
    GFateRideShooting: typing.Any = 8
    Unknown0: typing.Any = 9
    Unknown1: typing.Any = 10
    StartText: typing.Any = 11
    Unknown2: typing.Any = 12
    Unknown3: typing.Any = 13

class RideShootingSchedulerRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class RideShootingTargetRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class RideShootingTargetSchedulerRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7

class RideShootingTargetTypeRow(ExdRow):
    EObj: typing.Any = 0
    Score: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown2: typing.Any = 4
    Unknown3: typing.Any = 5

class RideShootingTextDataRow(ExdRow):
    _display_field: str = 'String'

    String: typing.Any = 0

class RoleRow(ExdRow):
    Type: typing.Any = 0

class SERow(ExdRow):
    Unknown0: typing.Any = 0

class SEBattleRow(ExdRow):
    Unknown0: typing.Any = 0

class SatisfactionArbitrationRow(ExdRow):
    _display_field: str = 'Quest'

    Quest: typing.Any = 0
    SatisfactionLevel: typing.Any = 1
    SatisfactionNpc: typing.Any = 2
    Unknown0: typing.Any = 3

class SatisfactionBonusGuaranteeRow(ExdRow):
    BonusDoH0: typing.Any = 0
    BonusDoH1: typing.Any = 1
    BonusDoL0: typing.Any = 2
    BonusDoL1: typing.Any = 3
    BonusFisher0: typing.Any = 4
    BonusFisher1: typing.Any = 5

class SatisfactionNpcRow(ExdRow):
    _display_field: str = 'Npc'

    SatisfactionNpcParams0: typing.Any = 0
    SatisfactionNpcParams1: typing.Any = 1
    SatisfactionNpcParams2: typing.Any = 2
    SatisfactionNpcParams3: typing.Any = 3
    SatisfactionNpcParams4: typing.Any = 4
    SatisfactionNpcParams5: typing.Any = 5
    RankParams0: typing.Any = 6
    RankParams1: typing.Any = 7
    RankParams2: typing.Any = 8
    RankParams3: typing.Any = 9
    RankParams4: typing.Any = 10
    RankParams5: typing.Any = 11
    Unknown0: typing.Any = 12
    Npc: typing.Any = 13
    QuestRequired: typing.Any = 14
    Icon: typing.Any = 15
    LevelUnlock: typing.Any = 16
    DeliveriesPerWeek: typing.Any = 17
    GlamourIndex: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20

class SatisfactionSupplyRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0
    CollectabilityLow: typing.Any = 1
    CollectabilityMid: typing.Any = 2
    CollectabilityHigh: typing.Any = 3
    Reward: typing.Any = 4
    FishingSpotId: typing.Any = 5
    SpearFishingSpotId: typing.Any = 6
    Slot: typing.Any = 7
    ProbabilityPercent: typing.Any = 8
    IsBonus: typing.Any = 9

class SatisfactionSupplyRewardRow(ExdRow):
    SatisfactionSupplyRewardData0: typing.Any = 0
    SatisfactionSupplyRewardData1: typing.Any = 1
    SatisfactionLow: typing.Any = 2
    SatisfactionMid: typing.Any = 3
    SatisfactionHigh: typing.Any = 4
    GilLow: typing.Any = 5
    GilMid: typing.Any = 6
    GilHigh: typing.Any = 7
    BonusMultiplier: typing.Any = 8
    MinLevelForSecondReward: typing.Any = 9

class SatisfactionSupplyRewardExpRow(ExdRow):
    PercentOfLevelLow: typing.Any = 0
    PercentOfLevelMid: typing.Any = 1
    PercentOfLevelHigh: typing.Any = 2

class ScenarioTreeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Addon: typing.Any = 1
    QuestChapter: typing.Any = 2
    Unknown0: typing.Any = 3
    Unknown1: typing.Any = 4
    Unknown2: typing.Any = 5
    Type: typing.Any = 6

class ScenarioTreeTipsRow(ExdRow):
    Tips1: typing.Any = 0
    Tips2: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3

class ScenarioTreeTipsClassQuestRow(ExdRow):
    _display_field: str = 'Quest'

    Quest: typing.Any = 0
    RequiredQuest: typing.Any = 1
    RequiredLevel: typing.Any = 2
    RequiredExpansion: typing.Any = 3
    Unknown0: typing.Any = 4
    Unknown1: typing.Any = 5

class ScenarioTypeRow(ExdRow):
    _display_field: str = 'Type'

    Type: typing.Any = 0
    Unknown0: typing.Any = 1

class ScreenImageRow(ExdRow):
    Image: typing.Any = 0
    Jingle: typing.Any = 1
    Type: typing.Any = 2
    Lang: typing.Any = 3

class SecretRecipeBookRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Item: typing.Any = 1

class SecretRecipeBookGroupRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7

class SequentialEventRow(ExdRow):
    UnknownStruct0: typing.Any = 0
    UnknownStruct1: typing.Any = 1
    UnknownStruct2: typing.Any = 2
    UnknownStruct3: typing.Any = 3
    UnknownStruct4: typing.Any = 4
    UnknownStruct5: typing.Any = 5
    UnknownStruct6: typing.Any = 6
    UnknownStruct7: typing.Any = 7
    UnknownStruct8: typing.Any = 8
    UnknownStruct9: typing.Any = 9
    UnknownStruct10: typing.Any = 10
    UnknownStruct11: typing.Any = 11
    UnknownStruct12: typing.Any = 12
    UnknownStruct13: typing.Any = 13
    UnknownStruct14: typing.Any = 14
    UnknownStruct15: typing.Any = 15
    UnknownStruct16: typing.Any = 16
    UnknownStruct17: typing.Any = 17
    UnknownStruct18: typing.Any = 18
    UnknownStruct19: typing.Any = 19
    UnknownStruct20: typing.Any = 20
    UnknownStruct21: typing.Any = 21
    UnknownStruct22: typing.Any = 22
    UnknownStruct23: typing.Any = 23
    UnknownStruct24: typing.Any = 24
    UnknownStruct25: typing.Any = 25
    UnknownStruct26: typing.Any = 26
    UnknownStruct27: typing.Any = 27
    UnknownStruct28: typing.Any = 28
    UnknownStruct29: typing.Any = 29
    UnknownStruct30: typing.Any = 30
    UnknownStruct31: typing.Any = 31
    UnknownStruct32: typing.Any = 32
    UnknownStruct33: typing.Any = 33
    UnknownStruct34: typing.Any = 34
    UnknownStruct35: typing.Any = 35
    UnknownStruct36: typing.Any = 36
    UnknownStruct37: typing.Any = 37
    UnknownStruct38: typing.Any = 38
    UnknownStruct39: typing.Any = 39
    UnknownStruct40: typing.Any = 40
    UnknownStruct41: typing.Any = 41
    UnknownStruct42: typing.Any = 42
    UnknownStruct43: typing.Any = 43
    UnknownStruct44: typing.Any = 44
    UnknownStruct45: typing.Any = 45
    UnknownStruct46: typing.Any = 46
    UnknownStruct47: typing.Any = 47
    UnknownStruct48: typing.Any = 48
    UnknownStruct49: typing.Any = 49
    UnknownStruct50: typing.Any = 50
    UnknownStruct51: typing.Any = 51
    UnknownStruct52: typing.Any = 52
    UnknownStruct53: typing.Any = 53
    UnknownStruct54: typing.Any = 54
    UnknownStruct55: typing.Any = 55
    UnknownStruct56: typing.Any = 56
    UnknownStruct57: typing.Any = 57
    UnknownStruct58: typing.Any = 58
    UnknownStruct59: typing.Any = 59
    UnknownStruct60: typing.Any = 60
    UnknownStruct61: typing.Any = 61
    UnknownStruct62: typing.Any = 62
    UnknownStruct63: typing.Any = 63
    Unknown320: typing.Any = 64
    Unknown_70: typing.Any = 65
    Unknown321: typing.Any = 66

class SequentialEventMultipleRangeRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class SharlayanCraftWorksRow(ExdRow):
    Description: typing.Any = 0
    Questgiver: typing.Any = 1
    Unknown2: typing.Any = 2

class SharlayanCraftWorksSupplyRow(ExdRow):
    Item0: typing.Any = 0
    Item1: typing.Any = 1
    Item2: typing.Any = 2
    Item3: typing.Any = 3

class ShellFixedFromCommandRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21

class SkirmishRow(ExdRow):
    Unknown0: typing.Any = 0

class SkyIslandRow(ExdRow):
    Unknown0: typing.Any = 0

class SkyIsland2Row(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class SkyIsland2MissionRow(ExdRow):
    _display_field: str = 'Item1'

    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Item1: typing.Any = 5
    Item2: typing.Any = 6
    PopRange0: typing.Any = 7
    PopRange1: typing.Any = 8
    PopRange2: typing.Any = 9
    Unknown5: typing.Any = 10
    Unknown6: typing.Any = 11
    Unknown7: typing.Any = 12
    Unknown8: typing.Any = 13
    Image: typing.Any = 14
    PlaceName: typing.Any = 15
    Unknown9: typing.Any = 16
    Objective1: typing.Any = 17
    Objective2: typing.Any = 18
    Objective3: typing.Any = 19
    RequiredAmount1: typing.Any = 20
    RequiredAmount2: typing.Any = 21
    Unknown10: typing.Any = 22
    Unknown11: typing.Any = 23
    Unknown12: typing.Any = 24
    Unknown13: typing.Any = 25

class SkyIsland2MissionDetailRow(ExdRow):
    _display_field: str = 'Objective'

    Objective: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2
    Unknown2: typing.Any = 3
    EObj: typing.Any = 4
    Unknown3: typing.Any = 5
    Unknown4: typing.Any = 6
    Type: typing.Any = 7
    Unknown5: typing.Any = 8
    Range: typing.Any = 9
    Unknown6: typing.Any = 10

class SkyIsland2MissionTypeRow(ExdRow):
    _display_field: str = 'Type'

    Type: typing.Any = 0

class SkyIsland2RangeTypeRow(ExdRow):
    _display_field: str = 'Type'

    Type: typing.Any = 0

class SkyIslandMapMarkerRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16

class SkyIslandSubjectRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17

class SnipeRow(ExdRow):
    SnipeData0: typing.Any = 0
    SnipeData1: typing.Any = 1
    SnipeData2: typing.Any = 2
    SnipeData3: typing.Any = 3
    SnipeData4: typing.Any = 4
    SnipeData5: typing.Any = 5
    SnipeData6: typing.Any = 6
    SnipeData7: typing.Any = 7
    EventNPC0: typing.Any = 8
    EventNPC1: typing.Any = 9
    EventNPC2: typing.Any = 10
    EventNPC3: typing.Any = 11
    EventNPC4: typing.Any = 12
    EventNPC5: typing.Any = 13
    EventNPC6: typing.Any = 14
    EventNPC7: typing.Any = 15
    Unknown0: typing.Any = 16
    Unknown1: typing.Any = 17
    Unknown2: typing.Any = 18
    Unknown3: typing.Any = 19
    Unknown4: typing.Any = 20
    Unknown5: typing.Any = 21
    Unknown6: typing.Any = 22
    Unknown7: typing.Any = 23
    Unknown8: typing.Any = 24
    Unknown9: typing.Any = 25
    Unknown10: typing.Any = 26
    Unknown11: typing.Any = 27
    Objective0: typing.Any = 28
    Hint0: typing.Any = 29
    Objective1: typing.Any = 30
    Hint1: typing.Any = 31
    Unknown12: typing.Any = 32
    Unknown13: typing.Any = 33
    Unknown14: typing.Any = 34
    Unknown15: typing.Any = 35
    Unknown16: typing.Any = 36
    Unknown17: typing.Any = 37
    Unknown18: typing.Any = 38
    ActionText: typing.Any = 39
    Unknown19: typing.Any = 40
    Unknown20: typing.Any = 41
    VFXFire: typing.Any = 42
    VFXHit: typing.Any = 43
    VFXMiss: typing.Any = 44
    VFXAdditional: typing.Any = 45
    LGBTargetMarker: typing.Any = 46
    Unknown21: typing.Any = 47
    Unknown22: typing.Any = 48
    Unknown23: typing.Any = 49
    Unknown24: typing.Any = 50
    Unknown25: typing.Any = 51
    Unknown26: typing.Any = 52
    Unknown27: typing.Any = 53
    Unknown28: typing.Any = 54
    Unknown29: typing.Any = 55
    Unknown30: typing.Any = 56
    Unknown31: typing.Any = 57
    Unknown32: typing.Any = 58

class SnipeCollisionRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class SnipeElementIdRow(ExdRow):
    Unknown0: typing.Any = 0

class SnipeHitEventRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class SnipePerformanceCameraRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9

class SnipeTalkRow(ExdRow):
    Text: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2
    Name: typing.Any = 3
    Unknown2: typing.Any = 4
    Unknown3: typing.Any = 5

class SnipeTalkNameRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class SpearfishingComboTargetRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown_70: typing.Any = 2

class SpearfishingEcologyRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class SpearfishingItemRow(ExdRow):
    _display_field: str = 'Item'

    Description: typing.Any = 0
    Item: typing.Any = 1
    GatheringItemLevel: typing.Any = 2
    Unknown2: typing.Any = 3
    TerritoryType: typing.Any = 4
    Unknown0: typing.Any = 5
    FishingRecordType: typing.Any = 6
    Unknown1: typing.Any = 7
    IsVisible: typing.Any = 8

class SpearfishingItemReverseRow(ExdRow):
    Unknown0: typing.Any = 0

class SpearfishingNotebookRow(ExdRow):
    _display_field: str = 'PlaceName'

    TerritoryType: typing.Any = 0
    Radius: typing.Any = 1
    PlaceName: typing.Any = 2
    GatheringPointBase: typing.Any = 3
    Unknown0: typing.Any = 4
    Unknown1: typing.Any = 5
    X: typing.Any = 6
    Y: typing.Any = 7
    GatheringLevel: typing.Any = 8
    Unknown2: typing.Any = 9
    Unknown3: typing.Any = 10
    IsShadowNode: typing.Any = 11

class SpearfishingRecordPageRow(ExdRow):
    PlaceName: typing.Any = 0
    Image: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown2: typing.Any = 4
    Unknown3: typing.Any = 5
    Unknown4: typing.Any = 6

class SpearfishingSilhouetteRow(ExdRow):
    Unknown0: typing.Any = 0

class SpecialShopRow(ExdRow):
    Name: typing.Any = 0
    Item0: typing.Any = 1
    Item1: typing.Any = 2
    Item2: typing.Any = 3
    Item3: typing.Any = 4
    Item4: typing.Any = 5
    Item5: typing.Any = 6
    Item6: typing.Any = 7
    Item7: typing.Any = 8
    Item8: typing.Any = 9
    Item9: typing.Any = 10
    Item10: typing.Any = 11
    Item11: typing.Any = 12
    Item12: typing.Any = 13
    Item13: typing.Any = 14
    Item14: typing.Any = 15
    Item15: typing.Any = 16
    Item16: typing.Any = 17
    Item17: typing.Any = 18
    Item18: typing.Any = 19
    Item19: typing.Any = 20
    Item20: typing.Any = 21
    Item21: typing.Any = 22
    Item22: typing.Any = 23
    Item23: typing.Any = 24
    Item24: typing.Any = 25
    Item25: typing.Any = 26
    Item26: typing.Any = 27
    Item27: typing.Any = 28
    Item28: typing.Any = 29
    Item29: typing.Any = 30
    Item30: typing.Any = 31
    Item31: typing.Any = 32
    Item32: typing.Any = 33
    Item33: typing.Any = 34
    Item34: typing.Any = 35
    Item35: typing.Any = 36
    Item36: typing.Any = 37
    Item37: typing.Any = 38
    Item38: typing.Any = 39
    Item39: typing.Any = 40
    Item40: typing.Any = 41
    Item41: typing.Any = 42
    Item42: typing.Any = 43
    Item43: typing.Any = 44
    Item44: typing.Any = 45
    Item45: typing.Any = 46
    Item46: typing.Any = 47
    Item47: typing.Any = 48
    Item48: typing.Any = 49
    Item49: typing.Any = 50
    Item50: typing.Any = 51
    Item51: typing.Any = 52
    Item52: typing.Any = 53
    Item53: typing.Any = 54
    Item54: typing.Any = 55
    Item55: typing.Any = 56
    Item56: typing.Any = 57
    Item57: typing.Any = 58
    Item58: typing.Any = 59
    Item59: typing.Any = 60
    Quest: typing.Any = 61
    Unknown0: typing.Any = 62
    RequiredContentFinderCondition: typing.Any = 63
    CompleteText: typing.Any = 64
    NotCompleteText: typing.Any = 65
    RequiredFestival: typing.Any = 66
    RequiredFestivalPhase: typing.Any = 67
    UseCurrencyType: typing.Any = 68
    Unknown3: typing.Any = 69
    RequiredContentFinderConditionComplete: typing.Any = 70

class SpecialShopItemCategoryRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class SpectatorRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown24: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    Unknown27: typing.Any = 27
    Unknown28: typing.Any = 28
    Unknown29: typing.Any = 29
    Unknown30: typing.Any = 30
    Unknown31: typing.Any = 31
    Unknown32: typing.Any = 32
    Unknown33: typing.Any = 33
    Unknown34: typing.Any = 34
    Unknown35: typing.Any = 35
    Unknown36: typing.Any = 36
    Unknown37: typing.Any = 37
    Unknown38: typing.Any = 38
    Unknown39: typing.Any = 39
    Unknown40: typing.Any = 40

class StainRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Name2: typing.Any = 1
    Color: typing.Any = 2
    Shade: typing.Any = 3
    SubOrder: typing.Any = 4
    Unknown1: typing.Any = 5
    Unknown2: typing.Any = 6

class StainTransientRow(ExdRow):
    _display_field: str = 'Item1'

    Item1: typing.Any = 0
    Item2: typing.Any = 1

class StanceChangeRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Action0: typing.Any = 2
    Action1: typing.Any = 3
    Unknown2: typing.Any = 4

class StatusRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Icon: typing.Any = 2
    ParamModifier: typing.Any = 3
    VFX: typing.Any = 4
    Log: typing.Any = 5
    Unknown0: typing.Any = 6
    MaxStacks: typing.Any = 7
    ClassJobCategory: typing.Any = 8
    StatusCategory: typing.Any = 9
    HitEffect: typing.Any = 10
    PartyListPriority: typing.Any = 11
    CanIncreaseRewards: typing.Any = 12
    ParamEffect: typing.Any = 13
    TargetType: typing.Any = 14
    Flags: typing.Any = 15
    Flag2: typing.Any = 16
    Unknown_70_1: typing.Any = 17
    Unknown2: typing.Any = 18
    LockMovement: typing.Any = 19
    Unknown3: typing.Any = 20
    LockActions: typing.Any = 21
    LockControl: typing.Any = 22
    Transfiguration: typing.Any = 23
    IsGaze: typing.Any = 24
    CanDispel: typing.Any = 25
    InflictedByActor: typing.Any = 26
    IsPermanent: typing.Any = 27
    NoLogVfx: typing.Any = 28
    Unknown5: typing.Any = 29
    CanStatusOff: typing.Any = 30
    IsFcBuff: typing.Any = 31
    Invisibility: typing.Any = 32
    Unknown6: typing.Any = 33
    Unknown_70_2: typing.Any = 34
    Unknown7: typing.Any = 35

class StatusHitEffectRow(ExdRow):
    _display_field: str = 'Location'

    Location: typing.Any = 0

class StatusLoopVFXRow(ExdRow):
    _display_field: str = 'VFX'

    VFX0: typing.Any = 0
    VFX1: typing.Any = 1
    VFX2: typing.Any = 2
    VFX3: typing.Any = 3
    Unknown0: typing.Any = 4
    Unknown1: typing.Any = 5
    Unknown2: typing.Any = 6
    Unknown3: typing.Any = 7
    Unknown4: typing.Any = 8
    Unknown5: typing.Any = 9
    Unknown6: typing.Any = 10

class StoryRow(ExdRow):
    StoryParams0: typing.Any = 0
    StoryParams1: typing.Any = 1
    StoryParams2: typing.Any = 2
    StoryParams3: typing.Any = 3
    StoryParams4: typing.Any = 4
    StoryParams5: typing.Any = 5
    StoryParams6: typing.Any = 6
    StoryParams7: typing.Any = 7
    StoryParams8: typing.Any = 8
    StoryParams9: typing.Any = 9
    StoryParams10: typing.Any = 10
    StoryParams11: typing.Any = 11
    StoryParams12: typing.Any = 12
    StoryParams13: typing.Any = 13
    StoryParams14: typing.Any = 14
    StoryParams15: typing.Any = 15
    StoryParams16: typing.Any = 16
    StoryParams17: typing.Any = 17
    StoryParams18: typing.Any = 18
    StoryParams19: typing.Any = 19
    StoryParams20: typing.Any = 20
    StoryParams21: typing.Any = 21
    StoryParams22: typing.Any = 22
    StoryParams23: typing.Any = 23
    StoryParams24: typing.Any = 24
    StoryParams25: typing.Any = 25
    StoryParams26: typing.Any = 26
    StoryParams27: typing.Any = 27
    StoryParams28: typing.Any = 28
    StoryParams29: typing.Any = 29
    StoryParams30: typing.Any = 30
    StoryParams31: typing.Any = 31
    StoryParams32: typing.Any = 32
    StoryParams33: typing.Any = 33
    StoryParams34: typing.Any = 34
    StoryParams35: typing.Any = 35
    StoryParams36: typing.Any = 36
    StoryParams37: typing.Any = 37
    StoryParams38: typing.Any = 38
    StoryParams39: typing.Any = 39
    StoryDefine0: typing.Any = 40
    StoryDefine1: typing.Any = 41
    StoryDefine2: typing.Any = 42
    StoryDefine3: typing.Any = 43
    StoryDefine4: typing.Any = 44
    StoryDefine5: typing.Any = 45
    StoryDefine6: typing.Any = 46
    StoryDefine7: typing.Any = 47
    StoryDefine8: typing.Any = 48
    StoryDefine9: typing.Any = 49
    StoryDefine10: typing.Any = 50
    StoryDefine11: typing.Any = 51
    StoryDefine12: typing.Any = 52
    StoryDefine13: typing.Any = 53
    StoryDefine14: typing.Any = 54
    StoryDefine15: typing.Any = 55
    StoryDefine16: typing.Any = 56
    StoryDefine17: typing.Any = 57
    StoryDefine18: typing.Any = 58
    StoryDefine19: typing.Any = 59
    StoryDefine20: typing.Any = 60
    StoryDefine21: typing.Any = 61
    StoryDefine22: typing.Any = 62
    StoryDefine23: typing.Any = 63
    StoryDefine24: typing.Any = 64
    StoryDefine25: typing.Any = 65
    StoryDefine26: typing.Any = 66
    StoryDefine27: typing.Any = 67
    StoryDefine28: typing.Any = 68
    StoryDefine29: typing.Any = 69
    StoryDefine30: typing.Any = 70
    StoryDefine31: typing.Any = 71
    StoryDefine32: typing.Any = 72
    StoryDefine33: typing.Any = 73
    StoryDefine34: typing.Any = 74
    StoryDefine35: typing.Any = 75
    StoryDefine36: typing.Any = 76
    StoryDefine37: typing.Any = 77
    StoryDefine38: typing.Any = 78
    StoryDefine39: typing.Any = 79
    StoryDefine40: typing.Any = 80
    StoryDefine41: typing.Any = 81
    StoryDefine42: typing.Any = 82
    StoryDefine43: typing.Any = 83
    StoryDefine44: typing.Any = 84
    StoryDefine45: typing.Any = 85
    StoryDefine46: typing.Any = 86
    StoryDefine47: typing.Any = 87
    StoryDefine48: typing.Any = 88
    StoryDefine49: typing.Any = 89
    StoryDefine50: typing.Any = 90
    StoryDefine51: typing.Any = 91
    StoryDefine52: typing.Any = 92
    StoryDefine53: typing.Any = 93
    StoryDefine54: typing.Any = 94
    StoryDefine55: typing.Any = 95
    StoryDefine56: typing.Any = 96
    StoryDefine57: typing.Any = 97
    StoryDefine58: typing.Any = 98
    StoryDefine59: typing.Any = 99
    StoryDefine60: typing.Any = 100
    StoryDefine61: typing.Any = 101
    StoryDefine62: typing.Any = 102
    StoryDefine63: typing.Any = 103
    StoryDefine64: typing.Any = 104
    StoryDefine65: typing.Any = 105
    StoryDefine66: typing.Any = 106
    StoryDefine67: typing.Any = 107
    StoryDefine68: typing.Any = 108
    StoryDefine69: typing.Any = 109
    StoryDefine70: typing.Any = 110
    StoryDefine71: typing.Any = 111
    StoryDefine72: typing.Any = 112
    StoryDefine73: typing.Any = 113
    StoryDefine74: typing.Any = 114
    StoryDefine75: typing.Any = 115
    StoryDefine76: typing.Any = 116
    StoryDefine77: typing.Any = 117
    StoryDefine78: typing.Any = 118
    StoryDefine79: typing.Any = 119
    StoryDefine80: typing.Any = 120
    StoryDefine81: typing.Any = 121
    StoryDefine82: typing.Any = 122
    StoryDefine83: typing.Any = 123
    StoryDefine84: typing.Any = 124
    StoryDefine85: typing.Any = 125
    StoryDefine86: typing.Any = 126
    StoryDefine87: typing.Any = 127
    StoryDefine88: typing.Any = 128
    StoryDefine89: typing.Any = 129
    StoryDefine90: typing.Any = 130
    StoryDefine91: typing.Any = 131
    StoryDefine92: typing.Any = 132
    StoryDefine93: typing.Any = 133
    StoryDefine94: typing.Any = 134
    StoryDefine95: typing.Any = 135
    StoryDefine96: typing.Any = 136
    StoryDefine97: typing.Any = 137
    StoryDefine98: typing.Any = 138
    StoryDefine99: typing.Any = 139
    StoryDefine100: typing.Any = 140
    StoryDefine101: typing.Any = 141
    StoryDefine102: typing.Any = 142
    StoryDefine103: typing.Any = 143
    StoryDefine104: typing.Any = 144
    StoryDefine105: typing.Any = 145
    StoryDefine106: typing.Any = 146
    StoryDefine107: typing.Any = 147
    StoryDefine108: typing.Any = 148
    StoryDefine109: typing.Any = 149
    StoryListener0: typing.Any = 150
    StoryListener1: typing.Any = 151
    StoryListener2: typing.Any = 152
    StoryListener3: typing.Any = 153
    StoryListener4: typing.Any = 154
    StoryListener5: typing.Any = 155
    StoryListener6: typing.Any = 156
    StoryListener7: typing.Any = 157
    StoryListener8: typing.Any = 158
    StoryListener9: typing.Any = 159
    StoryListener10: typing.Any = 160
    StoryListener11: typing.Any = 161
    StoryListener12: typing.Any = 162
    StoryListener13: typing.Any = 163
    StoryListener14: typing.Any = 164
    StoryListener15: typing.Any = 165
    StoryListener16: typing.Any = 166
    StoryListener17: typing.Any = 167
    StoryListener18: typing.Any = 168
    StoryListener19: typing.Any = 169
    StoryListener20: typing.Any = 170
    StoryListener21: typing.Any = 171
    StoryListener22: typing.Any = 172
    StoryListener23: typing.Any = 173
    StoryListener24: typing.Any = 174
    StoryListener25: typing.Any = 175
    StoryListener26: typing.Any = 176
    StoryListener27: typing.Any = 177
    StoryListener28: typing.Any = 178
    StoryListener29: typing.Any = 179
    StoryListener30: typing.Any = 180
    StoryListener31: typing.Any = 181
    StoryListener32: typing.Any = 182
    StoryListener33: typing.Any = 183
    StoryListener34: typing.Any = 184
    StoryListener35: typing.Any = 185
    StoryListener36: typing.Any = 186
    StoryListener37: typing.Any = 187
    StoryListener38: typing.Any = 188
    StoryListener39: typing.Any = 189
    StoryListener40: typing.Any = 190
    StoryListener41: typing.Any = 191
    StoryListener42: typing.Any = 192
    StoryListener43: typing.Any = 193
    StoryListener44: typing.Any = 194
    StoryListener45: typing.Any = 195
    StoryListener46: typing.Any = 196
    StoryListener47: typing.Any = 197
    StoryListener48: typing.Any = 198
    StoryListener49: typing.Any = 199
    StoryListener50: typing.Any = 200
    StoryListener51: typing.Any = 201
    StoryListener52: typing.Any = 202
    StoryListener53: typing.Any = 203
    StoryListener54: typing.Any = 204
    StoryListener55: typing.Any = 205
    StoryListener56: typing.Any = 206
    StoryListener57: typing.Any = 207
    StoryListener58: typing.Any = 208
    StoryListener59: typing.Any = 209
    StoryListener60: typing.Any = 210
    StoryListener61: typing.Any = 211
    StoryListener62: typing.Any = 212
    StoryListener63: typing.Any = 213
    StoryListener64: typing.Any = 214
    StoryListener65: typing.Any = 215
    StoryListener66: typing.Any = 216
    StoryListener67: typing.Any = 217
    StoryListener68: typing.Any = 218
    StoryListener69: typing.Any = 219
    StoryListener70: typing.Any = 220
    StoryListener71: typing.Any = 221
    StoryListener72: typing.Any = 222
    StoryListener73: typing.Any = 223
    StoryListener74: typing.Any = 224
    StoryListener75: typing.Any = 225
    StoryListener76: typing.Any = 226
    StoryListener77: typing.Any = 227
    StoryListener78: typing.Any = 228
    StoryListener79: typing.Any = 229
    Script: typing.Any = 230
    LayerSetTerritoryType0: typing.Any = 231
    LayerSetTerritoryType1: typing.Any = 232

class StorySystemDefineRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class SubmarineExplorationRow(ExdRow):
    _display_field: str = 'Destination'

    Destination: typing.Any = 0
    Location: typing.Any = 1
    ExpReward: typing.Any = 2
    SurveyDurationmin: typing.Any = 3
    X: typing.Any = 4
    Y: typing.Any = 5
    Z: typing.Any = 6
    Map: typing.Any = 7
    Stars: typing.Any = 8
    RankReq: typing.Any = 9
    CeruleumTankReq: typing.Any = 10
    SurveyDistance: typing.Any = 11
    StartingPoint: typing.Any = 12

class SubmarineExplorationLogRow(ExdRow):
    Unknown0: typing.Any = 0

class SubmarineMapRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Image: typing.Any = 1

class SubmarinePartRow(ExdRow):
    _display_field: str = 'Slot'

    Class: typing.Any = 0
    Surveillance: typing.Any = 1
    Retrieval: typing.Any = 2
    Speed: typing.Any = 3
    Range: typing.Any = 4
    Favor: typing.Any = 5
    Slot: typing.Any = 6
    Rank: typing.Any = 7
    Components: typing.Any = 8
    RepairMaterials: typing.Any = 9

class SubmarineRankRow(ExdRow):
    ExpToNext: typing.Any = 0
    Capacity: typing.Any = 1
    SurveillanceBonus: typing.Any = 2
    RetrievalBonus: typing.Any = 3
    SpeedBonus: typing.Any = 4
    RangeBonus: typing.Any = 5
    FavorBonus: typing.Any = 6

class SubmarineSpecCategoryRow(ExdRow):
    Unknown0: typing.Any = 0

class SwitchTalkRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class SwitchTalkVariationRow(ExdRow):
    _display_field: str = 'Quest0'

    Quest0: typing.Any = 0
    Quest1: typing.Any = 1
    DefaultTalk: typing.Any = 2
    Unknown0: typing.Any = 3

class SystemGraphicPresetRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown24: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    Unknown27: typing.Any = 27
    Unknown28: typing.Any = 28
    Unknown29: typing.Any = 29
    Unknown30: typing.Any = 30
    Unknown31: typing.Any = 31
    Unknown32: typing.Any = 32
    Unknown_70_1: typing.Any = 33
    Unknown_70_2: typing.Any = 34
    Unknown_70_3: typing.Any = 35
    Unknown_70_4: typing.Any = 36
    Unknown_70_5: typing.Any = 37
    Unknown_70_6: typing.Any = 38
    Unknown_70_7: typing.Any = 39

class TelepoRelayRow(ExdRow):
    Relays0: typing.Any = 0
    Relays1: typing.Any = 1
    Relays2: typing.Any = 2
    Relays3: typing.Any = 3
    Relays4: typing.Any = 4
    Relays5: typing.Any = 5
    Relays6: typing.Any = 6
    Relays7: typing.Any = 7
    Relays8: typing.Any = 8
    Unknown_70: typing.Any = 9

class TerritoryAethernetRow(ExdRow):
    Unknown0: typing.Any = 0

class TerritoryAetheryteListRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class TerritoryChatRuleRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7

class TerritoryIntendedUseRow(ExdRow):
    Unknown0: typing.Any = 0
    GayaSoundId: typing.Any = 1
    ChatRule: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    EnableCompanion: typing.Any = 10
    EnablePets: typing.Any = 11
    EnableRidePillion: typing.Any = 12
    DisableLogoutTimer: typing.Any = 13
    Unknown14: typing.Any = 14
    EnableReturn: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    EnableRecommendList: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    DisableFieldMarkers: typing.Any = 22
    Unknown23: typing.Any = 23
    EnableActions: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    EnableTripleTriadMatches: typing.Any = 27
    EnableTripleTriadMatchesAnywhere: typing.Any = 28
    Unknown29: typing.Any = 29
    Unknown30: typing.Any = 30
    Unknown31: typing.Any = 31
    CanPauseTimeWeather: typing.Any = 32
    Unknown33: typing.Any = 33
    EnablePvPQuickChat: typing.Any = 34
    Unknown35: typing.Any = 35
    Unknown36: typing.Any = 36
    CanApplyGlamourPlatesAnywhere: typing.Any = 37
    Unknown38: typing.Any = 38
    EnableFieldMarkerPresets: typing.Any = 39
    Unknown40: typing.Any = 40
    Unknown41: typing.Any = 41
    Unknown42: typing.Any = 42

class TerritoryTypeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Bg: typing.Any = 1
    ArrayEventHandler: typing.Any = 2
    PlaceNameRegionIcon: typing.Any = 3
    PlaceNameIcon: typing.Any = 4
    Aetheryte: typing.Any = 5
    FixedTime: typing.Any = 6
    PlaceNameRegion: typing.Any = 7
    PlaceNameZone: typing.Any = 8
    PlaceName: typing.Any = 9
    Map: typing.Any = 10
    ContentFinderCondition: typing.Any = 11
    BGM: typing.Any = 12
    QuestBattle: typing.Any = 13
    Resident: typing.Any = 14
    NotoriousMonsterTerritory: typing.Any = 15
    BattalionMode: typing.Any = 16
    LoadingImage: typing.Any = 17
    ExclusiveType: typing.Any = 18
    TerritoryIntendedUse: typing.Any = 19
    WeatherRate: typing.Any = 20
    Unknown1: typing.Any = 21
    ExVersion: typing.Any = 22
    Unknown2: typing.Any = 23
    ZoneSharedGroup: typing.Any = 24
    AetherCurrentCompFlgSet: typing.Any = 25
    MountSpeed: typing.Any = 26
    IndividualWeather: typing.Any = 27
    AchievementIndex: typing.Any = 28
    Unknown6: typing.Any = 29
    Unknown7: typing.Any = 30
    PCSearch: typing.Any = 31
    Stealth: typing.Any = 32
    Mount: typing.Any = 33
    Unknown8: typing.Any = 34
    IsPvpZone: typing.Any = 35
    Unknown9: typing.Any = 36
    Unknown10: typing.Any = 37
    Unknown11: typing.Any = 38
    Unknown12: typing.Any = 39
    Unknown13: typing.Any = 40
    Unknown14: typing.Any = 41
    Unknown15: typing.Any = 42
    Unknown16: typing.Any = 43

class TerritoryTypeTelepoRow(ExdRow):
    X: typing.Any = 0
    Y: typing.Any = 1
    Expansion: typing.Any = 2
    Relay: typing.Any = 3

class TerritoryTypeTransientRow(ExdRow):
    _display_field: str = 'OffsetZ'

    OffsetZ: typing.Any = 0

class TextCommandRow(ExdRow):
    _display_field: str = 'Command'

    Description: typing.Any = 0
    Alias: typing.Any = 1
    ShortAlias: typing.Any = 2
    Command: typing.Any = 3
    ShortCommand: typing.Any = 4
    Unknown0: typing.Any = 5
    Param: typing.Any = 6
    Unknown1: typing.Any = 7
    Unknown2: typing.Any = 8
    Unknown3: typing.Any = 9
    Unknown4: typing.Any = 10
    Unknown5: typing.Any = 11

class TextCommandParamRow(ExdRow):
    _display_field: str = 'Param'

    Param: typing.Any = 0

class TiltParamRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class TitleRow(ExdRow):
    _display_field: str = 'Feminine'

    Masculine: typing.Any = 0
    Feminine: typing.Any = 1
    IsPrefix: typing.Any = 2
    Order: typing.Any = 3

class TofuBgRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class TofuEditParamRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class TofuObjectRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown16: typing.Any = 10
    Unknown17: typing.Any = 11
    Unknown18: typing.Any = 12
    Unknown19: typing.Any = 13
    Unknown20: typing.Any = 14
    Unknown21: typing.Any = 15
    Unknown10: typing.Any = 16
    Unknown11: typing.Any = 17
    Unknown12: typing.Any = 18
    Unknown13: typing.Any = 19

class TofuObjectCategoryRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class TofuPresetRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13

class TofuPresetCategoryRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class TofuPresetObjectRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8

class TomestoneConvertRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class TomestonesRow(ExdRow):
    WeeklyLimit: typing.Any = 0

class TomestonesItemRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0
    Tomestones: typing.Any = 1
    CurrencyInventorySlot: typing.Any = 2

class TopicSelectRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Shop0: typing.Any = 1
    Shop1: typing.Any = 2
    Shop2: typing.Any = 3
    Shop3: typing.Any = 4
    Shop4: typing.Any = 5
    Shop5: typing.Any = 6
    Shop6: typing.Any = 7
    Shop7: typing.Any = 8
    Shop8: typing.Any = 9
    Shop9: typing.Any = 10
    Unknown0: typing.Any = 11
    Unknown1: typing.Any = 12
    Unknown2: typing.Any = 13

class TownRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Icon: typing.Any = 1

class TradeScreenImageRow(ExdRow):
    Items0: typing.Any = 0
    Items1: typing.Any = 1
    ItemIcons0: typing.Any = 2
    ItemIcons1: typing.Any = 3
    ItemValues0: typing.Any = 4
    ItemValues1: typing.Any = 5
    BannerType: typing.Any = 6

class TraitRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Quest: typing.Any = 1
    Icon: typing.Any = 2
    Value: typing.Any = 3
    ClassJob: typing.Any = 4
    Unknown_70: typing.Any = 5
    Level: typing.Any = 6
    ClassJobCategory: typing.Any = 7
    Unknown0: typing.Any = 8
    Unknown1: typing.Any = 9

class TraitRecastRow(ExdRow):
    _display_field: str = 'Trait'

    Trait: typing.Any = 0
    Action: typing.Any = 1
    Timeds: typing.Any = 2

class TraitTransientRow(ExdRow):
    _display_field: str = 'Description'

    Description: typing.Any = 0

class TransformationRow(ExdRow):
    Speed: typing.Any = 0
    Scale: typing.Any = 1
    Action6: typing.Any = 2
    BNpcCustomize: typing.Any = 3
    NpcEquip: typing.Any = 4
    BNpcName: typing.Any = 5
    Action0: typing.Any = 6
    Action1: typing.Any = 7
    Action2: typing.Any = 8
    Action3: typing.Any = 9
    Action4: typing.Any = 10
    Action5: typing.Any = 11
    RPParameter: typing.Any = 12
    RemoveAction: typing.Any = 13
    StartVFX: typing.Any = 14
    EndVFX: typing.Any = 15
    Action7: typing.Any = 16
    Model: typing.Any = 17
    Unknown0: typing.Any = 18
    Unknown1: typing.Any = 19
    RPParameter2: typing.Any = 20
    Unknown3: typing.Any = 21
    Unknown4: typing.Any = 22
    ExHotbarEnableConfig: typing.Any = 23
    Unknown5: typing.Any = 24
    Unknown6: typing.Any = 25
    Unknown7: typing.Any = 26
    Unknown8: typing.Any = 27
    Unknown9: typing.Any = 28
    Unknown10: typing.Any = 29
    Unknown11: typing.Any = 30
    Unknown12: typing.Any = 31
    Unknown13: typing.Any = 32
    IsPvP: typing.Any = 33
    IsEvent: typing.Any = 34
    PlayerCamera: typing.Any = 35
    Unknown14: typing.Any = 36
    Unknown15: typing.Any = 37
    Unknown16: typing.Any = 38
    Unknown17: typing.Any = 39

class TreasureRow(ExdRow):
    _display_field: str = 'SGB'

    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    SGB: typing.Any = 8
    Unknown_70: typing.Any = 9
    Unknown8: typing.Any = 10
    Unknown9: typing.Any = 11

class TreasureHuntRankRow(ExdRow):
    _display_field: str = 'ItemName'

    Icon: typing.Any = 0
    ItemName: typing.Any = 1
    KeyItemName: typing.Any = 2
    InstanceMap: typing.Any = 3
    Unknown0: typing.Any = 4
    Unknown1: typing.Any = 5
    MaxPartySize: typing.Any = 6
    TreasureHuntTexture: typing.Any = 7
    Unknown2: typing.Any = 8

class TreasureHuntTextureRow(ExdRow):
    Unknown0: typing.Any = 0

class TreasureModelRow(ExdRow):
    _display_field: str = 'Path'

    Path: typing.Any = 0

class TreasureSpotRow(ExdRow):
    _display_field: str = 'Location'

    MapOffsetX: typing.Any = 0
    MapOffsetY: typing.Any = 1
    Location: typing.Any = 2

class TribeRow(ExdRow):
    _display_field: str = 'Feminine'

    Masculine: typing.Any = 0
    Feminine: typing.Any = 1
    Hp: typing.Any = 2
    Mp: typing.Any = 3
    STR: typing.Any = 4
    VIT: typing.Any = 5
    DEX: typing.Any = 6
    INT: typing.Any = 7
    MND: typing.Any = 8
    PIE: typing.Any = 9

class TriggerEffectRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7

class TripleTriadRow(ExdRow):
    ItemPossibleReward0: typing.Any = 0
    ItemPossibleReward1: typing.Any = 1
    ItemPossibleReward2: typing.Any = 2
    ItemPossibleReward3: typing.Any = 3
    PreviousQuest0: typing.Any = 4
    PreviousQuest1: typing.Any = 5
    PreviousQuest2: typing.Any = 6
    DefaultTalkChallenge: typing.Any = 7
    DefaultTalkUnavailable: typing.Any = 8
    DefaultTalkNPCWin: typing.Any = 9
    DefaultTalkDraw: typing.Any = 10
    DefaultTalkPCWin: typing.Any = 11
    TripleTriadCardFixed0: typing.Any = 12
    TripleTriadCardFixed1: typing.Any = 13
    TripleTriadCardFixed2: typing.Any = 14
    TripleTriadCardFixed3: typing.Any = 15
    TripleTriadCardFixed4: typing.Any = 16
    TripleTriadCardVariable0: typing.Any = 17
    TripleTriadCardVariable1: typing.Any = 18
    TripleTriadCardVariable2: typing.Any = 19
    TripleTriadCardVariable3: typing.Any = 20
    TripleTriadCardVariable4: typing.Any = 21
    Fee: typing.Any = 22
    StartTime: typing.Any = 23
    EndTime: typing.Any = 24
    TripleTriadRule0: typing.Any = 25
    TripleTriadRule1: typing.Any = 26
    PreviousQuestJoin: typing.Any = 27
    UsesRegionalRules: typing.Any = 28
    Unknown0: typing.Any = 29

class TripleTriadCardRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Unknown0: typing.Any = 1
    Description: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown2: typing.Any = 4
    StartsWithVowel: typing.Any = 5
    Unknown3: typing.Any = 6
    Unknown4: typing.Any = 7
    Unknown5: typing.Any = 8

class TripleTriadCardObtainRow(ExdRow):
    Icon: typing.Any = 0
    Text: typing.Any = 1

class TripleTriadCardRarityRow(ExdRow):
    _display_field: str = 'Stars'

    Stars: typing.Any = 0

class TripleTriadCardResidentRow(ExdRow):
    Acquisition: typing.Any = 0
    Location: typing.Any = 1
    Quest: typing.Any = 2
    Unknown0: typing.Any = 3
    SaleValue: typing.Any = 4
    Order: typing.Any = 5
    Top: typing.Any = 6
    Bottom: typing.Any = 7
    Left: typing.Any = 8
    Right: typing.Any = 9
    TripleTriadCardRarity: typing.Any = 10
    TripleTriadCardType: typing.Any = 11
    SortKey: typing.Any = 12
    UIPriority: typing.Any = 13
    AcquisitionType: typing.Any = 14
    Unknown1: typing.Any = 15

class TripleTriadCardTypeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class TripleTriadCompetitionRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0

class TripleTriadDefineRow(ExdRow):
    Unknown0: typing.Any = 0

class TripleTriadResidentRow(ExdRow):
    Order: typing.Any = 0

class TripleTriadRuleRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown2: typing.Any = 4
    Unknown3: typing.Any = 5
    Unknown4: typing.Any = 6

class TripleTriadTournamentRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class TutorialRow(ExdRow):
    _display_field: str = 'Objective'

    Exp: typing.Any = 0
    Gil: typing.Any = 1
    RewardTank: typing.Any = 2
    RewardMelee: typing.Any = 3
    RewardRanged: typing.Any = 4
    Unknown4: typing.Any = 5
    Objective: typing.Any = 6
    Unknown5: typing.Any = 7
    Unknown0: typing.Any = 8
    Unknown1: typing.Any = 9
    Unknown2: typing.Any = 10
    Unknown3: typing.Any = 11

class TutorialDPSRow(ExdRow):
    Image: typing.Any = 0
    Objective: typing.Any = 1

class TutorialGimmickRow(ExdRow):
    Image: typing.Any = 0
    Objective: typing.Any = 1

class TutorialHealerRow(ExdRow):
    Image: typing.Any = 0
    Objective: typing.Any = 1

class TutorialTankRow(ExdRow):
    Image: typing.Any = 0
    Objective: typing.Any = 1

class UDS_EventRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0
    Type: typing.Any = 1
    Property0: typing.Any = 2
    Property1: typing.Any = 3
    Property2: typing.Any = 4
    Property3: typing.Any = 5
    Property4: typing.Any = 6
    Property5: typing.Any = 7
    Property6: typing.Any = 8
    Property7: typing.Any = 9
    Property8: typing.Any = 10
    Property9: typing.Any = 11
    Property10: typing.Any = 12
    Property11: typing.Any = 13
    Property12: typing.Any = 14
    Property13: typing.Any = 15
    Property14: typing.Any = 16
    Property15: typing.Any = 17
    Property16: typing.Any = 18
    Property17: typing.Any = 19
    Property18: typing.Any = 20
    Property19: typing.Any = 21
    Property20: typing.Any = 22
    Property21: typing.Any = 23
    Property22: typing.Any = 24
    Property23: typing.Any = 25
    Property24: typing.Any = 26
    Property25: typing.Any = 27
    Property26: typing.Any = 28
    Property27: typing.Any = 29
    Property28: typing.Any = 30
    Property29: typing.Any = 31
    Property30: typing.Any = 32
    Property31: typing.Any = 33

class UDS_ObjectRow(ExdRow):
    Unknown0: typing.Any = 0

class UDS_PropertyRow(ExdRow):
    _display_field: str = 'Text'

    Text: typing.Any = 0
    Type: typing.Any = 1

class UDS_StatsRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class UIColorRow(ExdRow):
    _display_field: str = 'Dark'

    Dark: typing.Any = 0
    Light: typing.Any = 1
    ClassicFF: typing.Any = 2
    ClearBlue: typing.Any = 3
    Unknown0: typing.Any = 4
    Unknown1: typing.Any = 5
    Unknown2: typing.Any = 6
    Unknown3: typing.Any = 7

class UIColorPickerTableRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class UIConstRow(ExdRow):
    Unknown0: typing.Any = 0

class UILevelLookupRow(ExdRow):
    Unknown0: typing.Any = 0

class VFXRow(ExdRow):
    _display_field: str = 'Location'

    Location: typing.Any = 0

class VVDDataRow(ExdRow):
    ContentFinderCondition: typing.Any = 0
    CurrencyItem: typing.Any = 1
    ContentExAction: typing.Any = 2
    UnlockQuest: typing.Any = 3
    Series: typing.Any = 4
    Unknown5: typing.Any = 5

class VVDNotebookContentsRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Icon: typing.Any = 2
    Image: typing.Any = 3

class VVDNotebookSeriesRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Contents0: typing.Any = 1
    Contents1: typing.Any = 2
    Contents2: typing.Any = 3
    Contents3: typing.Any = 4
    Contents4: typing.Any = 5
    Contents5: typing.Any = 6
    Contents6: typing.Any = 7
    Contents7: typing.Any = 8
    Contents8: typing.Any = 9
    Contents9: typing.Any = 10
    Contents10: typing.Any = 11
    Contents11: typing.Any = 12

class VVDRouteDataRow(ExdRow):
    NotebookEntry: typing.Any = 0

class VVDVariantActionRow(ExdRow):
    _display_field: str = 'Action'

    Action: typing.Any = 0

class ValentionSweetsMaterialRow(ExdRow):
    Unknown0: typing.Any = 0

class ValentionSweetsRecipeRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16

class VaseRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class VaseFlowerRow(ExdRow):
    Item: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2
    Unknown2: typing.Any = 3

class WKSAchievementRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5

class WKSAchievementDailyDefineRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    RewardItem0: typing.Any = 4
    RewardItem1: typing.Any = 5
    Unknown4: typing.Any = 6
    Unknown5: typing.Any = 7
    SuccessPointsRequired0: typing.Any = 8
    SuccessPointsRequired1: typing.Any = 9
    Unknown6: typing.Any = 10
    Unknown7: typing.Any = 11
    RewardQuantity: typing.Any = 12

class WKSAchievementRewardItemRow(ExdRow):
    Item: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class WKSCosmoToolClassRow(ExdRow):
    Stages0: typing.Any = 0
    Stages1: typing.Any = 1
    Stages2: typing.Any = 2
    Stages3: typing.Any = 3
    Stages4: typing.Any = 4
    Stages5: typing.Any = 5
    Stages6: typing.Any = 6
    Stages7: typing.Any = 7
    Stages8: typing.Any = 8
    Stages9: typing.Any = 9
    Stages10: typing.Any = 10
    Stages11: typing.Any = 11
    Stages12: typing.Any = 12
    Stages13: typing.Any = 13
    Types0: typing.Any = 14
    Types1: typing.Any = 15
    Types2: typing.Any = 16
    Types3: typing.Any = 17
    Types4: typing.Any = 18
    Name: typing.Any = 19
    DataAmount: typing.Any = 20

class WKSCosmoToolCommonLevelRow(ExdRow):
    IsCommon: typing.Any = 0

class WKSCosmoToolDataAmountRow(ExdRow):
    Stages0: typing.Any = 0
    Stages1: typing.Any = 1
    Stages2: typing.Any = 2
    Stages3: typing.Any = 3
    Stages4: typing.Any = 4
    Stages5: typing.Any = 5
    Stages6: typing.Any = 6
    Stages7: typing.Any = 7
    Stages8: typing.Any = 8
    Stages9: typing.Any = 9
    Stages10: typing.Any = 10
    Stages11: typing.Any = 11
    Stages12: typing.Any = 12
    Stages13: typing.Any = 13

class WKSCosmoToolNameRow(ExdRow):
    Name: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7

class WKSCosmoToolPassiveBuffRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class WKSDevGradeRow(ExdRow):
    StageFull: typing.Any = 0
    Stage: typing.Any = 1
    IndexText2: typing.Any = 2
    IndexText: typing.Any = 3
    IndexNpc: typing.Any = 4
    Unknown3: typing.Any = 5
    Unknown4: typing.Any = 6
    Unknown12: typing.Any = 7
    Unknown13: typing.Any = 8
    Unknown5: typing.Any = 9
    Unknown6: typing.Any = 10
    Unknown7: typing.Any = 11
    Unknown8: typing.Any = 12
    Unknown9: typing.Any = 13
    Unknown10: typing.Any = 14
    Unknown11: typing.Any = 15

class WKSDevGradeBGSetRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown24: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    Unknown27: typing.Any = 27
    Unknown28: typing.Any = 28
    Unknown29: typing.Any = 29
    Unknown30: typing.Any = 30
    Unknown31: typing.Any = 31
    Unknown32: typing.Any = 32
    Unknown33: typing.Any = 33
    Unknown34: typing.Any = 34
    Unknown35: typing.Any = 35
    Unknown36: typing.Any = 36
    Unknown37: typing.Any = 37
    Unknown38: typing.Any = 38
    Unknown39: typing.Any = 39
    Unknown40: typing.Any = 40

class WKSEmergencyInfoRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class WKSEmergencyInfoTextRow(ExdRow):
    Unknown0: typing.Any = 0

class WKSEmergencyMissionRow(ExdRow):
    Unknown0: typing.Any = 0

class WKSEmergencyMissionGroupRow(ExdRow):
    Unknown0: typing.Any = 0

class WKSEmergencyProblemRow(ExdRow):
    Unknown3: typing.Any = 0
    Unknown4: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown2: typing.Any = 4

class WKSFateControlRow(ExdRow):
    StartupText: typing.Any = 0
    RunningText: typing.Any = 1
    Unknown0: typing.Any = 2

class WKSFortunePatternUIColorSetRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class WKSFortunePatternUIPlaceRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown24: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    Unknown27: typing.Any = 27
    Unknown28: typing.Any = 28
    Unknown29: typing.Any = 29
    Unknown30: typing.Any = 30
    Unknown31: typing.Any = 31
    Unknown32: typing.Any = 32
    Unknown33: typing.Any = 33
    Unknown34: typing.Any = 34
    Unknown35: typing.Any = 35
    Unknown36: typing.Any = 36
    Unknown37: typing.Any = 37
    Unknown38: typing.Any = 38
    Unknown39: typing.Any = 39

class WKSFortunePrizeGradeRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class WKSFortuneSPPatternUIPlaceRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown24: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    Unknown27: typing.Any = 27
    Unknown28: typing.Any = 28
    Unknown29: typing.Any = 29
    Unknown30: typing.Any = 30
    Unknown31: typing.Any = 31
    Unknown32: typing.Any = 32
    Unknown33: typing.Any = 33
    Unknown34: typing.Any = 34
    Unknown35: typing.Any = 35
    Unknown36: typing.Any = 36
    Unknown37: typing.Any = 37
    Unknown38: typing.Any = 38
    Unknown39: typing.Any = 39

class WKSFunctionRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown16: typing.Any = 8
    Unknown17: typing.Any = 9
    Unknown18: typing.Any = 10
    Unknown19: typing.Any = 11
    Unknown8: typing.Any = 12
    Unknown9: typing.Any = 13
    Unknown10: typing.Any = 14
    Unknown11: typing.Any = 15
    Unknown12: typing.Any = 16
    Unknown13: typing.Any = 17
    Unknown14: typing.Any = 18
    Unknown15: typing.Any = 19

class WKSItemInfoRow(ExdRow):
    Item: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    WKSItemSubCategory: typing.Any = 3
    Unknown3: typing.Any = 4

class WKSItemSubCategoryRow(ExdRow):
    Name: typing.Any = 0
    MenuOrder: typing.Any = 1

class WKSMechaEventDataRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19
    Unknown20: typing.Any = 20
    Unknown21: typing.Any = 21
    Unknown22: typing.Any = 22
    Unknown23: typing.Any = 23
    Unknown24: typing.Any = 24
    Unknown25: typing.Any = 25
    Unknown26: typing.Any = 26
    Unknown27: typing.Any = 27
    Unknown28: typing.Any = 28
    Unknown29: typing.Any = 29
    Unknown30: typing.Any = 30
    Unknown31: typing.Any = 31
    Unknown32: typing.Any = 32
    Unknown33: typing.Any = 33
    Unknown34: typing.Any = 34
    Unknown35: typing.Any = 35
    Unknown36: typing.Any = 36
    Unknown37: typing.Any = 37
    Unknown38: typing.Any = 38
    Unknown39: typing.Any = 39
    Unknown40: typing.Any = 40
    Unknown41: typing.Any = 41
    Unknown42: typing.Any = 42
    Unknown43: typing.Any = 43
    Unknown44: typing.Any = 44
    Unknown45: typing.Any = 45
    Unknown46: typing.Any = 46
    Unknown47: typing.Any = 47

class WKSMechaEventObjectRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown5: typing.Any = 3
    Unknown3: typing.Any = 4
    Unknown4: typing.Any = 5

class WKSMechaEventObjectGroupRow(ExdRow):
    Unknown0: typing.Any = 0

class WKSMechaEventRewardUIRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class WKSMechaFieldSearcherRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class WKSMechaLivelyActorGroupRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown6: typing.Any = 4
    Unknown4: typing.Any = 5
    Unknown5: typing.Any = 6

class WKSMissionInfoRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class WKSMissionLotteryCondRow(ExdRow):
    Unknown0: typing.Any = 0

class WKSMissionLotterySpecialCondRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class WKSMissionMapMarkerRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class WKSMissionPromotionConditionRow(ExdRow):
    Unknown2: typing.Any = 0
    Unknown3: typing.Any = 1

class WKSMissionRecipeRow(ExdRow):
    Recipe0: typing.Any = 0
    Recipe1: typing.Any = 1
    Recipe2: typing.Any = 2
    Recipe3: typing.Any = 3
    Recipe4: typing.Any = 4

class WKSMissionRewardRow(ExdRow):
    Unknown15: typing.Any = 0
    Unknown16: typing.Any = 1
    Unknown17: typing.Any = 2
    Unknown18: typing.Any = 3
    Unknown0: typing.Any = 4
    Unknown1: typing.Any = 5
    Unknown2: typing.Any = 6
    Unknown3: typing.Any = 7
    Unknown4: typing.Any = 8
    Unknown8: typing.Any = 9
    Unknown19: typing.Any = 10
    Unknown9: typing.Any = 11
    Unknown10: typing.Any = 12
    Unknown11: typing.Any = 13
    Unknown12: typing.Any = 14
    Unknown13: typing.Any = 15
    Unknown14: typing.Any = 16

class WKSMissionSupplyItemRow(ExdRow):
    Item0: typing.Any = 0
    Item1: typing.Any = 1
    Item2: typing.Any = 2
    ItemCount0: typing.Any = 3
    ItemCount1: typing.Any = 4
    ItemCount2: typing.Any = 5

class WKSMissionTextRow(ExdRow):
    Text: typing.Any = 0

class WKSMissionToDoRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    RequiredItem0: typing.Any = 3
    RequiredItem1: typing.Any = 4
    RequiredItem2: typing.Any = 5
    RequiredItemQuantity0: typing.Any = 6
    RequiredItemQuantity1: typing.Any = 7
    RequiredItemQuantity2: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    MissionType: typing.Any = 18
    WKSMissionText: typing.Any = 19

class WKSMissionToDoEvalutionItemRow(ExdRow):
    Item: typing.Any = 0

class WKSMissionToDoEvalutionRefinRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class WKSMissionToDoSuccessTypeRow(ExdRow):
    Unknown0: typing.Any = 0

class WKSMissionUnitRow(ExdRow):
    Name: typing.Any = 0
    ClassJobCategory0: typing.Any = 1
    ClassJobCategory1: typing.Any = 2
    MissionTime: typing.Any = 3
    MissionReward: typing.Any = 4
    SilverStarRequirement: typing.Any = 5
    GoldStarRequirement: typing.Any = 6
    MissionToDo0: typing.Any = 7
    MissionToDo1: typing.Any = 8
    MissionToDo2: typing.Any = 9
    LockedBehind: typing.Any = 10
    WKSMissionSupplyItem: typing.Any = 11
    WKSMissionRecipe: typing.Any = 12
    PlaceName: typing.Any = 13
    SortKey: typing.Any = 14
    WKSMissionText: typing.Any = 15
    WKSFunction: typing.Any = 16
    LevelGroup: typing.Any = 17
    Unknown0: typing.Any = 18
    WKSMissionLotterySpecialCond: typing.Any = 19
    IsSynced: typing.Any = 20
    IsSpecialQuest: typing.Any = 21

class WKSNextPlanetGuidanceRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class WKSParamRow(ExdRow):
    Unknown0: typing.Any = 0

class WKSPioneeringTrailRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class WKSPioneeringTrailStringRow(ExdRow):
    DevelopmentLogText: typing.Any = 0
    DevelopmentLogName: typing.Any = 1
    DevelopmentLogDescription: typing.Any = 2

class WKSPlanetSelectRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class WKSPraiseHologramRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class WKSPraiseUIRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1

class WKSScoreListRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4

class WKSSharedGroupRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown5: typing.Any = 2
    Unknown2: typing.Any = 3
    Unknown3: typing.Any = 4
    Unknown4: typing.Any = 5

class WKSTerritoryInfoRow(ExdRow):
    Unknown6: typing.Any = 0
    Unknown7: typing.Any = 1
    Unknown8: typing.Any = 2
    Unknown9: typing.Any = 3
    Unknown10: typing.Any = 4
    Unknown11: typing.Any = 5
    Unknown12: typing.Any = 6
    Unknown0: typing.Any = 7
    MechaEventNpc: typing.Any = 8
    Item: typing.Any = 9
    Unknown3: typing.Any = 10
    Unknown4: typing.Any = 11
    Unknown5: typing.Any = 12

class WKSTextRow(ExdRow):
    Text: typing.Any = 0

class WKSZoneFloorCollisionRow(ExdRow):
    Unknown0: typing.Any = 0

class WarpRow(ExdRow):
    Name: typing.Any = 0
    Question: typing.Any = 1
    PopRange: typing.Any = 2
    ConditionSuccessEvent: typing.Any = 3
    ConditionFailEvent: typing.Any = 4
    ConfirmEvent: typing.Any = 5
    TerritoryType: typing.Any = 6
    WarpCondition: typing.Any = 7
    WarpLogic: typing.Any = 8
    StartCutscene: typing.Any = 9
    EndCutscene: typing.Any = 10
    CanSkipCutscene: typing.Any = 11

class WarpConditionRow(ExdRow):
    RequiredQuest1: typing.Any = 0
    RequiredQuest2: typing.Any = 1
    RequiredQuest3: typing.Any = 2
    RequiredQuest4: typing.Any = 3
    Gil: typing.Any = 4
    QuestReward: typing.Any = 5
    ClassLevel: typing.Any = 6
    CompleteParam: typing.Any = 7

class WarpLogicRow(ExdRow):
    _display_field: str = 'WarpName'

    WarpParams0: typing.Any = 0
    WarpParams1: typing.Any = 1
    WarpParams2: typing.Any = 2
    WarpParams3: typing.Any = 3
    WarpParams4: typing.Any = 4
    WarpParams5: typing.Any = 5
    WarpParams6: typing.Any = 6
    WarpParams7: typing.Any = 7
    WarpParams8: typing.Any = 8
    WarpParams9: typing.Any = 9
    Question: typing.Any = 10
    ResponseYes: typing.Any = 11
    ResponseNo: typing.Any = 12
    WarpName: typing.Any = 13
    Unknown0: typing.Any = 14
    CanSkipCutscene: typing.Any = 15

class WeaponTimelineRow(ExdRow):
    File: typing.Any = 0
    NextWeaponTimeline: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3

class WeatherRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Description: typing.Any = 1
    Unknown0: typing.Any = 2
    Unknown1: typing.Any = 3
    Unknown2: typing.Any = 4
    Unknown3: typing.Any = 5
    Icon: typing.Any = 6

class WeatherGroupRow(ExdRow):
    _display_field: str = 'WeatherRate'

    Unknown0: typing.Any = 0
    WeatherRate: typing.Any = 1

class WeatherRateRow(ExdRow):
    Weather0: typing.Any = 0
    Weather1: typing.Any = 1
    Weather2: typing.Any = 2
    Weather3: typing.Any = 3
    Weather4: typing.Any = 4
    Weather5: typing.Any = 5
    Weather6: typing.Any = 6
    Weather7: typing.Any = 7
    Rate0: typing.Any = 8
    Rate1: typing.Any = 9
    Rate2: typing.Any = 10
    Rate3: typing.Any = 11
    Rate4: typing.Any = 12
    Rate5: typing.Any = 13
    Rate6: typing.Any = 14
    Rate7: typing.Any = 15

class WeatherReportReplaceRow(ExdRow):
    PlaceNameSub: typing.Any = 0
    PlaceNameParent: typing.Any = 1

class WebGuidanceRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    Unknown0: typing.Any = 1
    Description: typing.Any = 2
    Image: typing.Any = 3
    Url: typing.Any = 4

class WebURLRow(ExdRow):
    _display_field: str = 'URL'

    URL: typing.Any = 0

class WeddingBGMRow(ExdRow):
    _display_field: str = 'Song'

    SongName: typing.Any = 0
    Song: typing.Any = 1

class WeddingFlowerColorRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2

class WeddingPlanRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19

class WeeklyBingoMultipleOrderRow(ExdRow):
    Content0: typing.Any = 0
    Content1: typing.Any = 1
    Content2: typing.Any = 2
    Content3: typing.Any = 3
    Content4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6
    Unknown7: typing.Any = 7
    Unknown8: typing.Any = 8
    Unknown9: typing.Any = 9
    Unknown10: typing.Any = 10
    Unknown11: typing.Any = 11
    Unknown12: typing.Any = 12
    Unknown13: typing.Any = 13
    Unknown14: typing.Any = 14
    Unknown15: typing.Any = 15
    Unknown16: typing.Any = 16
    Unknown17: typing.Any = 17
    Unknown18: typing.Any = 18
    Unknown19: typing.Any = 19

class WeeklyBingoOrderDataRow(ExdRow):
    Type: typing.Any = 0
    Data: typing.Any = 1
    Unknown2: typing.Any = 2
    Icon: typing.Any = 3
    Unknown0: typing.Any = 4
    Text: typing.Any = 5
    Unknown1: typing.Any = 6

class WeeklyBingoRewardDataRow(ExdRow):
    _display_field: str = 'RewardItem1'

    RewardItem1: typing.Any = 0
    RewardItem2: typing.Any = 1
    RewardItem3: typing.Any = 2
    RewardQuantity1: typing.Any = 3
    RewardQuantity2: typing.Any = 4
    RewardQuantity3: typing.Any = 5
    RewardType1: typing.Any = 6
    Unknown0: typing.Any = 7
    RewardType2: typing.Any = 8
    RewardType3: typing.Any = 9
    RewardHq2: typing.Any = 10
    RewardHq3: typing.Any = 11
    RewardHq1: typing.Any = 12

class WeeklyBingoTextRow(ExdRow):
    _display_field: str = 'Description'

    Description: typing.Any = 0

class WeeklyLotBonusRow(ExdRow):
    WeeklyLotBonusParam0: typing.Any = 0
    WeeklyLotBonusParam1: typing.Any = 1
    WeeklyLotBonusParam2: typing.Any = 2
    WeeklyLotBonusParam3: typing.Any = 3
    WeeklyLotBonusParam4: typing.Any = 4
    WeeklyLotBonusParam5: typing.Any = 5
    WeeklyLotBonusParam6: typing.Any = 6
    WeeklyLotBonusParam7: typing.Any = 7
    WeeklyLotBonusParam8: typing.Any = 8
    WeeklyLotBonusParam9: typing.Any = 9
    WeeklyLotBonusParam10: typing.Any = 10
    WeeklyLotBonusParam11: typing.Any = 11
    WeeklyLotBonusParam12: typing.Any = 12
    WeeklyLotBonusParam13: typing.Any = 13
    WeeklyLotBonusParam14: typing.Any = 14
    WeeklyLotBonusParam15: typing.Any = 15
    WeeklyLotBonusParam16: typing.Any = 16
    WeeklyLotBonusParam17: typing.Any = 17
    WeeklyLotBonusParam18: typing.Any = 18
    WeeklyLotBonusParam19: typing.Any = 19
    WeeklyLotBonusParam20: typing.Any = 20
    WeeklyLotBonusParam21: typing.Any = 21
    WeeklyLotBonusParam22: typing.Any = 22
    WeeklyLotBonusParam23: typing.Any = 23
    WeeklyLotBonusParam24: typing.Any = 24
    WeeklyLotBonusParam25: typing.Any = 25
    WeeklyLotBonusParam26: typing.Any = 26
    WeeklyLotBonusParam27: typing.Any = 27
    WeeklyLotBonusParam28: typing.Any = 28
    WeeklyLotBonusParam29: typing.Any = 29
    WeeklyLotBonusParam30: typing.Any = 30
    WeeklyLotBonusParam31: typing.Any = 31

class WeeklyLotBonusThresholdRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3
    Unknown4: typing.Any = 4
    Unknown5: typing.Any = 5
    Unknown6: typing.Any = 6

class WorldRow(ExdRow):
    InternalName: typing.Any = 0
    Name: typing.Any = 1
    Region: typing.Any = 2
    UserType: typing.Any = 3
    DataCenter: typing.Any = 4
    IsPublic: typing.Any = 5

class WorldDCGroupTypeRow(ExdRow):
    _display_field: str = 'Name'

    Name: typing.Any = 0
    PvPRegion: typing.Any = 1
    NeolobbyId: typing.Any = 2
    Region: typing.Any = 3
    IsCloud: typing.Any = 4

class XBMPetRow(ExdRow):
    Unknown0: typing.Any = 0

class XPVPGroupActivityRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

class YKWRow(ExdRow):
    Transient: typing.Any = 0
    Item: typing.Any = 1
    Companion: typing.Any = 2
    Location0: typing.Any = 3
    Location1: typing.Any = 4
    Location2: typing.Any = 5
    Location3: typing.Any = 6
    Location4: typing.Any = 7
    Location5: typing.Any = 8

class YardCatalogCategoryRow(ExdRow):
    _display_field: str = 'Category'

    Category: typing.Any = 0
    Unknown0: typing.Any = 1
    Unknown1: typing.Any = 2

class YardCatalogItemListRow(ExdRow):
    _display_field: str = 'Item'

    Item: typing.Any = 0
    Category: typing.Any = 1
    Patch: typing.Any = 2

class ZoneSharedGroupRow(ExdRow):
    LGBSharedGroup: typing.Any = 0
    RequirementRow0: typing.Any = 1
    RequirementRow1: typing.Any = 2
    RequirementRow2: typing.Any = 3
    RequirementRow3: typing.Any = 4
    RequirementRow4: typing.Any = 5
    RequirementRow5: typing.Any = 6
    Unknown0: typing.Any = 7
    RequirementQuestSequence0: typing.Any = 8
    RequirementQuestSequence1: typing.Any = 9
    RequirementQuestSequence2: typing.Any = 10
    RequirementQuestSequence3: typing.Any = 11
    RequirementQuestSequence4: typing.Any = 12
    RequirementQuestSequence5: typing.Any = 13
    Unknown1: typing.Any = 14
    RequirementType0: typing.Any = 15
    RequirementType1: typing.Any = 16
    RequirementType2: typing.Any = 17
    RequirementType3: typing.Any = 18
    RequirementType4: typing.Any = 19
    RequirementType5: typing.Any = 20
    Unknown8: typing.Any = 21
    Unknown9: typing.Any = 22
    Unknown10: typing.Any = 23
    Unknown11: typing.Any = 24
    Unknown12: typing.Any = 25
    Unknown13: typing.Any = 26
    Unknown14: typing.Any = 27
    Unknown15: typing.Any = 28

class ZoneTimelineRow(ExdRow):
    Unknown0: typing.Any = 0
    Unknown1: typing.Any = 1
    Unknown2: typing.Any = 2
    Unknown3: typing.Any = 3

