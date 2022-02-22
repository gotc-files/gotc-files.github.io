import StatsTable from "../common/StatsTable";

function GearStatsCard(props) {
  return (
    <StatsTable
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
