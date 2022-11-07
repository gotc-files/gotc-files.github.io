from pages.page_processor import PageProcessor
from pages.page_processor import InsufficientDataException


class ResearchProcessor(PageProcessor):
    def process(self):
        researches = []
        for raw_research in self.iterate_files(
            ["researches_1", "researches_2", "researches_3"]
        ):
            if "Expeditions" in raw_research["category"]:
                continue
            try:
                researches.append(self._process_research(raw_research))
            except InsufficientDataException as e:
                print(e)
        return researches

    def _process_research(self, raw_research):
        research_stats = self.lookup_files(
            ["research_stat_sets_1", "research_stat_sets_2", "research_stat_sets_3"],
            "name",
            raw_research["name"].lower(),
        )
        research_stat_with_values = [
            self._process_research_stat(stat) for stat in research_stats["stats"]
        ]
        power_progression = self.lookup_files(
            [
                "research_progressions_1",
                "research_progressions_2",
                "research_progressions_3",
            ],
            "name",
            raw_research["power_progression"],
        )["values"]
        event_score_progression = self.lookup_files(
            [
                "event_scoring_progressions",
                "event_scoring_progressions_dragon",
                "event_scoring_progressions_research_1",
                "event_scoring_progressions_research_2",
            ],
            "name",
            raw_research["event_score_progression"],
        )["values"]
        time_progression = self.lookup_files(
            [
                "research_progressions_1",
                "research_progressions_2",
                "research_progressions_3",
            ],
            "name",
            raw_research["time_progression"],
        )["values"]
        cost_progressions = [
            (
                cost_entry["item_name"],
                self.lookup_files(
                    [
                        "research_progressions_1",
                        "research_progressions_2",
                        "research_progressions_3",
                    ],
                    "name",
                    cost_entry["progression"],
                )["values"],
            )
            for cost_entry in raw_research["costs"]
        ]
        building_level_progression = self.lookup_files(
            [
                "research_progressions_1",
                "research_progressions_2",
                "research_progressions_3",
            ],
            "name",
            raw_research["building_level_progression"],
        )["values"]
        dragon_pit_requirement_progression = (
            self.lookup_file(
                "research_progressions_1",
                "name",
                raw_research["dragon_pit_requirement_progression"],
            )["values"]
            if "dragon_pit_requirement_progression" in raw_research
            else None
        )
        dragon_requirement_progression = (
            self.lookup_file(
                "research_progressions_1",
                "name",
                raw_research["dragon_requirement_progression"],
            )["values"]
            if "dragon_requirement_progression" in raw_research
            else None
        )
        category = self.lookup_files(
            ["research_categories_1", "research_categories_2", "research_categories_3"],
            "name",
            raw_research["category"],
        )
        return {
            "id": raw_research["id"],
            "name": self.translate(raw_research["name_placeholder"]),
            "description": self.translate(raw_research["description_placeholder"]),
            "category_name": self.translate(category["name_placeholder"]),
            "levels": [
                self._process_research_level(
                    i,
                    power_progression[i],
                    event_score_progression[i]
                    if i < len(event_score_progression)
                    else event_score_progression[0],
                    time_progression[i],
                    [
                        {
                            "name": stat["name"],
                            "description": stat["description"],
                            "value": stat["values"][i],
                        }
                        for stat in research_stat_with_values
                    ],
                    [
                        self._process_item_cost(
                            item_name, cost_values[i] if i < len(cost_values) else 0
                        )
                        for item_name, cost_values in cost_progressions
                    ],
                    building_level_progression[i],
                    self._get_dragon_requirement(dragon_pit_requirement_progression, i),
                    self._get_dragon_requirement(dragon_requirement_progression, i),
                )
                for i in range(raw_research["num_levels"])
            ],
            "requirements": [
                self._process_requirement(requirement)
                for requirement in raw_research["requirements"]
            ],
        }

    def _get_dragon_requirement(self, progression, level):
        if not progression:
            return None
        if level >= len(progression):
            return progression[0]
        return progression[level]

    def _process_research_level(
        self,
        index,
        power,
        event_score,
        time,
        stats,
        costs,
        building_level_requirement,
        dragon_pit_requirement,
        dragon_requirement,
    ):
        research_level = {
            "level": index + 1,
            "power": power,
            "event_score": event_score,
            "upgrade_time_seconds": time,
            "stats": stats,
            "costs": costs,
            "building_level_requirement": building_level_requirement,
            "dragon_pit_requirement": dragon_pit_requirement,
            "dragon_requirement": dragon_requirement,
        }
        if dragon_pit_requirement:
            research_level["dragon_pit_requirement"] = dragon_pit_requirement
        if dragon_requirement:
            research_level["dragon_requirement"] = dragon_requirement
        return research_level

    def _process_research_stat(self, stat):
        stat_info = self.lookup_file("properties", "name", stat["name"])
        return {
            "name": self.translate(stat_info["name_placeholder"]),
            "description": self.translate(stat_info["description_placeholder"]),
            "values": self.lookup_files(
                [
                    "research_progressions_1",
                    "research_progressions_2",
                    "research_progressions_3",
                ],
                "name",
                stat["progression"],
            )["values"],
        }

    def _process_item_cost(self, item_name, cost):
        item = self.lookup_files(["items", "dragon_items"], "name", item_name)
        return {
            "name": self.translate(item["name_placeholder"]),
            "description": self.translate(item["description_placeholder"]),
            "cost": cost,
        }

    def _process_requirement(self, requirement):
        research = self.lookup_files(
            ["researches_1", "researches_2", "researches_3"],
            "name",
            requirement["research"],
        )
        return {
            "id": research["id"],
            "name": self.translate(research["name_placeholder"]),
            "level": requirement["level"],
        }
