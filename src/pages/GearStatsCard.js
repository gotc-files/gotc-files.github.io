import StatsCard from "../common/StatsCard";

function GearStatsCard(props) {
  return (
    <StatsCard
      title={
        props.gear.gear_with_level.find(
          (gear) => gear.level === props.currentLevel
        ).name
      }
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
