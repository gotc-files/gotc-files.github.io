import useLocalStorage from "@rehooks/local-storage";
import DataCard from "../common/DataCard";

export default function BuildingCard(props) {
  const building = props.building;
  const levels = building.levels.map((buildingLevel) => buildingLevel.level);
  const [level, setLevel] = useLocalStorage(
    `building-level-${building.name.replaceAll(" ", "-").toLowerCase()}`,
    Math.max(...levels)
  );
  const buildingLevel = building.levels.find(
    (buildingLevel) => buildingLevel.level === level
  );
  const data = [
    {
      name: "Event Score",
      value: buildingLevel.event_score,
      valueType: "number",
    },
    {
      name: "Power",
      value: buildingLevel.power,
      valueType: "number",
    },
    {
      name: "Upgrade Time",
      value: buildingLevel.upgrade_time_seconds,
      valueType: "time",
    },
  ];
  data.push(
    ...buildingLevel.requirements.map((requirement) => ({
      name: `(Requirement) ${requirement.building}`,
      value: requirement.level,
      valueType: "number",
    }))
  );
  data.push(
    ...buildingLevel.costs
      .filter((cost) => cost.cost > 0)
      .map((cost) => ({
        name: `(Cost) ${cost.name}`,
        tooltip: cost.description,
        value: cost.cost,
        valueType: "number",
      }))
  );
  data.push(
    ...building.stats
      .map((stat) => ({
        name: `(Stat) ${stat.name}`,
        tooltip: stat.description,
        value: stat.progression[level - 1],
      }))
      .filter((entry) => entry.value > 0)
  );

  return (
    <DataCard
      title={`${props.building.name} (${level})`}
      color="primary.main"
      slider={
        levels.length > 1 && {
          min: Math.min(...levels),
          max: Math.max(...levels),
          value: level,
          setValue: setLevel,
        }
      }
      data={data}
    />
  );
}
