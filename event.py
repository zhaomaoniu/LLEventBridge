from typing import TYPE_CHECKING

from llpy import Player, Entity, Block, Item, FloatPos, IntPos, ActorDamageCause

if TYPE_CHECKING:
    from websocket import WebSocket


class EventForwarder:
    def __init__(self, ws: "WebSocket", events: list[str]):
        self.ws = ws
        self.events = events

    def forward(self, data: dict):
        if data["event_name"] in self.events:
            self.ws.forward(data)

    def on_pre_join(self, player: Player):
        self.forward({"event_name": "PreJoin", "player": player})

    def on_join(self, player: Player):
        self.forward({"event_name": "Join", "player": player})

    def on_left(self, player: Player):
        self.forward({"event_name": "Left", "player": player})

    def on_respawn(self, player: Player):
        self.forward({"event_name": "Respawn", "player": player})

    def on_player_die(self, player: Player, source: Entity):
        self.forward({"event_name": "PlayerDie", "player": player, "source": source})

    def on_player_cmd(self, player: Player, cmd: str):
        self.forward({"event_name": "PlayerCmd", "player": player, "cmd": cmd})

    def on_chat(self, player: Player, msg: str):
        self.forward({"event_name": "Chat", "player": player, "content": msg})

    def on_change_dim(self, player: Player, dimid: int):
        self.forward({"event_name": "ChangeDim", "player": player, "dim": dimid})

    def on_jump(self, player: Player):
        self.forward({"event_name": "Jump", "player": player})

    def on_sneak(self, player: Player, isSneaking: bool):
        self.forward(
            {"event_name": "Sneak", "player": player, "isSneaking": isSneaking}
        )

    def on_attack_entity(self, player: Player, entity: Entity, damage: float):
        self.forward(
            {
                "event_name": "AttackEntity",
                "player": player,
                "entity": entity,
                "damage": damage,
            },
        )

    def on_attack_block(self, player: Player, entity: Block, item: Item):
        self.forward(
            {
                "event_name": "AttackBlock",
                "player": player,
                "entity": entity,
                "item": item,
            },
        )

    def on_use_item(self, player: Player, item: Item):
        self.forward({"event_name": "UseItem", "player": player, "item": item})

    def on_use_item_on(
        self, player: Player, item: Item, block: Block, side: int, pos: FloatPos
    ):
        self.forward(
            {
                "event_name": "UseItemOn",
                "player": player,
                "item": item,
                "block": block,
                "side": side,
                "pos": pos,
            },
        )

    def on_use_bucket_place(
        self, player: Player, item: Item, block: Block, side: int, pos: FloatPos
    ):
        self.forward(
            {
                "event_name": "UseBucketPlace",
                "player": player,
                "item": item,
                "block": block,
                "side": side,
                "pos": pos,
            },
        )

    def on_use_bucket_take(
        self, player: Player, item: Item, block: Block, side: int, pos: FloatPos
    ):
        self.forward(
            {
                "event_name": "UseBucketTake",
                "player": player,
                "item": item,
                "block": block,
                "side": side,
                "pos": pos,
            },
        )

    def on_take_item(self, player: Player, entity: Entity, item: Item):
        self.forward(
            {
                "event_name": "TakeItem",
                "player": player,
                "entity": entity,
                "item": item,
            },
        )

    def on_drop_item(self, player: Player, item: Item):
        self.forward({"event_name": "DropItem", "player": player, "item": item})

    def on_eat(self, player: Player, item: Item):
        self.forward({"event_name": "Eat", "player": player, "item": item})

    def on_ate(self, player: Player, item: Item):
        self.forward({"event_name": "Ate", "player": player, "item": item})

    def on_consume_totem(self, player: Player):
        self.forward({"event_name": "ConsumeTotem", "player": player})

    def on_effect_added(
        self, player: Player, effectName: str, amplifier: int, duration: int
    ):
        self.forward(
            {
                "event_name": "EffectAdded",
                "player": player,
                "effectName": effectName,
                "amplifier": amplifier,
                "duration": duration,
            },
        )

    def on_effect_removed(self, player: Player, effectName: str):
        self.forward(
            {"event_name": "EffectRemoved", "player": player, "effectName": effectName},
        )

    def on_effect_updated(
        self, player: Player, effectName: str, amplifier: int, duration: int
    ):
        self.forward(
            {
                "event_name": "EffectUpdated",
                "player": player,
                "effectName": effectName,
                "amplifier": amplifier,
                "duration": duration,
            },
        )

    def on_start_destroy_block(self, player: Player, block: Block):
        self.forward(
            {"event_name": "StartDestroyBlock", "player": player, "block": block}
        )

    def on_destroy_block(self, player: Player, block: Block):
        self.forward({"event_name": "DestroyBlock", "player": player, "block": block})

    def on_place_block(self, player: Player, block: Block):
        self.forward({"event_name": "PlaceBlock", "player": player, "block": block})

    def after_place_block(self, player: Player, block: Block):
        self.forward(
            {"event_name": "AfterPlaceBlock", "player": player, "block": block}
        )

    def on_open_container(self, player: Player, block: Block):
        self.forward({"event_name": "OpenContainer", "player": player, "block": block})

    def on_close_container(self, player: Player, block: Block):
        self.forward({"event_name": "CloseContainer", "player": player, "block": block})

    def on_inventory_change(
        self, player: Player, slotNum: int, oldItem: Item, newItem: Item
    ):
        self.forward(
            {
                "event_name": "InventoryChange",
                "player": player,
                "slotNum": slotNum,
                "oldItem": oldItem,
                "newItem": newItem,
            },
        )

    def on_change_sprinting(self, player: Player, sprinting: bool):
        self.forward(
            {"event_name": "ChangeSprinting", "player": player, "sprinting": sprinting},
        )

    def on_set_armor(self, player: Player, slotNum: int, item: Item):
        self.forward(
            {
                "event_name": "SetArmor",
                "player": player,
                "slotNum": slotNum,
                "item": item,
            },
        )

    def on_use_respawn_anchor(self, player: Player, pos: IntPos):
        self.forward({"event_name": "UseRespawnAnchor", "player": player, "pos": pos})

    def on_open_container_screen(self, player: Player):
        self.forward({"event_name": "OpenContainerScreen", "player": player})

    def on_experience_add(self, player: Player, exp: int):
        self.forward({"event_name": "ExperienceAdd", "player": player, "exp": exp})

    def on_player_pull_fishing_hook(self, player: Player, entity: Entity, item: Item):
        self.forward(
            {
                "event_name": "PlayerPullFishingHook",
                "player": player,
                "entity": entity,
                "item": item,
            },
        )

    def on_bed_enter(self, player: Player, pos: IntPos):
        self.forward({"event_name": "BedEnter", "player": player, "pos": pos})

    # 实体相关事件

    def on_mob_die(self, mob: Entity, source: Entity, cause: int):
        self.forward(
            {"event_name": "MobDie", "mob": mob, "source": source, "cause": cause}
        )

    def on_mob_hurt(
        self, mob: Entity, source: Entity, damage: float, cause: ActorDamageCause
    ):
        self.forward(
            {
                "event_name": "MobHurt",
                "mob": mob,
                "source": source,
                "damage": damage,
                "cause": cause,
            },
        )

    def on_entity_explode(
        self,
        source: Entity,
        pos: FloatPos,
        radius: float,
        maxResistance: float,
        isDestroy: bool,
        isFire: bool,
    ):
        self.forward(
            {
                "event_name": "EntityExplode",
                "source": source,
                "pos": pos,
                "radius": radius,
                "maxResistance": maxResistance,
                "isDestroy": isDestroy,
                "isFire": isFire,
            },
        )

    def on_mob_try_spawn(self, typeName: str, pos: FloatPos):
        self.forward({"event_name": "MobTrySpawn", "typeName": typeName, "pos": pos})

    def on_mob_spawned(self, entity: Entity, pos: FloatPos):
        self.forward({"event_name": "MobSpawned", "entity": entity, "pos": pos})

    def on_projectile_hit_entity(self, entity: Entity, source: Entity):
        self.forward(
            {"event_name": "ProjectileHitEntity", "entity": entity, "source": source},
        )

    def on_wither_boss_destroy(self, witherBoss: Entity, AAbb: IntPos, aaBB: IntPos):
        self.forward(
            {
                "event_name": "WitherBossDestroy",
                "witherBoss": witherBoss,
                "AAbb": AAbb,
                "aaBB": aaBB,
            },
        )

    def on_ride(self, entity1: Entity, entity2: Entity):
        self.forward({"event_name": "Ride", "entity1": entity1, "entity2": entity2})

    def on_step_on_pressure_plate(self, entity: Entity, pressurePlate: Block):
        self.forward(
            {
                "event_name": "StepOnPressurePlate",
                "entity": entity,
                "pressurePlate": pressurePlate,
            },
        )

    def on_spawn_projectile(self, shooter: Entity, type: str):
        self.forward(
            {"event_name": "SpawnProjectile", "shooter": shooter, "type": type}
        )

    def on_projectile_created(self, shooter: Entity, entity: Entity):
        self.forward(
            {"event_name": "ProjectileCreated", "shooter": shooter, "entity": entity},
        )

    def on_change_armor_stand(self, armorStand: Entity, player: Player, slot: int):
        self.forward(
            {
                "event_name": "ChangeArmorStand",
                "armorStand": armorStand,
                "player": player,
                "slot": slot,
            },
        )

    def on_entity_transformation(self, uniqueId: str, entity: Entity):
        self.forward(
            {
                "event_name": "EntityTransformation",
                "uniqueId": uniqueId,
                "entity": entity,
            },
        )

    # 方块相关事件

    def on_block_interacted(self, player: Player, block: Block):
        self.forward(
            {"event_name": "BlockInteracted", "player": player, "block": block}
        )

    def on_block_changed(self, beforeBlock: Block, afterBlock: Block):
        self.forward(
            {
                "event_name": "BlockChanged",
                "beforeBlock": beforeBlock,
                "afterBlock": afterBlock,
            },
        )

    def on_block_explode(
        self,
        source: Block,
        pos: FloatPos,
        redius: float,
        maxResistance: float,
        isDestroy: bool,
        isFire: bool,
    ):
        self.forward(
            {
                "event_name": "BlockExplode",
                "source": source,
                "pos": pos,
                "redius": redius,
                "maxResistance": maxResistance,
                "isDestroy": isDestroy,
                "isFire": isFire,
            },
        )

    def on_respawn_anchor_explode(self, pos: IntPos, player: Player):
        self.forward(
            {"event_name": "RespawnAnchorExplode", "pos": pos, "player": player}
        )

    def on_block_exploded(self, block: Block, source: Entity):
        self.forward({"event_name": "BlockExploded", "block": block, "source": source})

    def on_fire_spread(self, pos: IntPos):
        self.forward({"event_name": "FireSpread", "pos": pos})

    def on_cmd_block_execute(self, cmd: str, pos: IntPos, isMinecart: bool):
        self.forward(
            {
                "event_name": "CmdBlockExecute",
                "cmd": cmd,
                "pos": pos,
                "isMinecart": isMinecart,
            },
        )

    def on_container_change(
        self,
        player: Player,
        cantainer: Block,
        slotNum: int,
        oldItem: Item,
        newItem: Item,
    ):
        self.forward(
            {
                "event_name": "ContainerChange",
                "player": player,
                "cantainer": cantainer,
                "slotNum": slotNum,
                "oldItem": oldItem,
                "newItem": newItem,
            },
        )

    def on_projectile_hit_block(self, block: Block, source: Entity):
        self.forward(
            {"event_name": "ProjectileHitBlock", "block": block, "source": source}
        )

    def on_red_stone_update(self, block: Block, level: int, isActive: bool):
        self.forward(
            {
                "event_name": "RedStoneUpdate",
                "block": block,
                "level": level,
                "isActive": isActive,
            },
        )

    def on_hopper_search_item(self, pos: FloatPos, isMinecart: bool, item: Item):
        self.forward(
            {
                "event_name": "HopperSearchItem",
                "pos": pos,
                "isMinecart": isMinecart,
                "item": item,
            },
        )

    def on_hopper_push_out(self, pos: FloatPos, isMinecart: bool, item: Item):
        self.forward(
            {
                "event_name": "HopperPushOut",
                "pos": pos,
                "isMinecart": isMinecart,
                "item": item,
            },
        )

    def on_piston_try_push(self, pistonPos: IntPos, block: Block):
        self.forward(
            {"event_name": "PistonTryPush", "pistonPos": pistonPos, "block": block},
        )

    def on_piston_push(self, pistonPos: IntPos, block: Block):
        self.forward(
            {"event_name": "PistonPush", "pistonPos": pistonPos, "block": block}
        )

    def on_farm_land_decay(self, pos: IntPos, entity: Entity):
        self.forward({"event_name": "FarmLandDecay", "pos": pos, "entity": entity})

    def on_use_frame_block(self, player: Player, block: Block):
        self.forward({"event_name": "UseFrameBlock", "player": player, "block": block})

    def on_liquid_flow(self, source: Block, to: IntPos):
        self.forward({"event_name": "LiquidFlow", "source": source, "to": to})

    # 其他事件

    def on_source_changed(self, player: Player, num: int, name: int, disName: str):
        self.forward(
            {
                "event_name": "SourceChanged",
                "player": player,
                "num": num,
                "name": name,
                "disName": disName,
            },
        )

    def on_tick(
        self,
    ):
        self.forward({"event_name": "Tick"})

    def on_console_cmd(self, cmd: str):
        self.forward({"event_name": "ConsoleCmd", "cmd": cmd})

    def on_console_output(self, cmd: str):
        self.forward({"event_name": "ConsoleOutput", "cmd": cmd})
