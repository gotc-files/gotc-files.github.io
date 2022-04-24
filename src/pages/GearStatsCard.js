import StatsCard from "../common/StatsCard";
import { displayWithRegexFallback } from "../common/util";

function GearStatsCard(props) {
  return (
    <StatsCard
      title={displayWithRegexFallback(
        props.gear.gear_with_level.find(
          (gear) => gear.level === props.currentLevel
        ).name,
        new RegExp(/^n:EQ_EVENTS_(\w+_[0-9]+_\w+)_LORD[0-9]+_NAME$/)
      )}
      color={props.armory.color}
      stats={props.gear.gear_with_level
        .find((gear) => gear.level === props.currentLevel)
        .stats.map((stat) => ({
          name: stat.name,
          description: stat.description,
          value: stat.progression[props.currentQualityIndex],
        }))}
    />
  );
}

export default GearStatsCard;
